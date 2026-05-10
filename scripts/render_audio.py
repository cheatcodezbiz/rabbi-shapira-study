"""Pre-render article paragraphs to MP3 using Microsoft Edge TTS.

Microsoft's Edge "Read Aloud" Neural voices (Xiaoxiao, HsiaoChen, Aria, etc.)
are broadcaster-quality and exposed for free via the unofficial edge-tts API.
We render each article paragraph once, ship the MP3s as static assets, and
the player just <audio src="…">s them — no runtime API calls, no rate limits,
no key management, instant playback on iPhone.

Usage:
    python scripts/render_audio.py                              # all articles
    python scripts/render_audio.py article-messiah-birthing-iran.html
    python scripts/render_audio.py --force                      # re-render all
    python scripts/render_audio.py --voice-zh zh-TW-YunJheNeural  # male voice

Output:
    assets/audio/<slug>/manifest.json   { slug, zh: {…}, en: {…} }
    assets/audio/<slug>/zh/<index>.mp3
    assets/audio/<slug>/en/<index>.mp3

Run again later — already-rendered paragraphs are skipped via SHA-256 of
(voice, text). Only changed paragraphs get re-synthesized.
"""

from __future__ import annotations

import argparse
import asyncio
import hashlib
import json
import sys
from pathlib import Path

from bs4 import BeautifulSoup
import edge_tts


REPO_ROOT  = Path(__file__).resolve().parent.parent
AUDIO_ROOT = REPO_ROOT / "assets" / "audio"

# Default voices — both are Edge "Neural" tier (broadcaster quality).
# zh-TW because the article uses Traditional Chinese; HsiaoChen is warm/expressive.
# Aria is the friendliest US English voice in the Edge catalog.
DEFAULT_VOICES = {
    "zh": "zh-TW-HsiaoChenNeural",
    "en": "en-US-AriaNeural",
}

# Microsoft will rate-limit if we hammer it; 4 in flight is comfortable.
CONCURRENCY = 4


def slugify(html_path: Path) -> str:
    return html_path.stem


def extract_segments(html_text: str) -> list[dict[str, str]]:
    """Pull bilingual paragraphs out of the article body.

    Mirrors tts.js's segment selector: top-level p / h2 / h3 / blockquote
    inside .article-prose. Each element should contain a <span class="zh">
    and a <span class="en">; we fall back to the element's full textContent
    if a language span is missing.
    """
    soup = BeautifulSoup(html_text, "html.parser")
    prose = soup.find(class_="article-prose")
    if prose is None:
        raise ValueError("no <… class='article-prose'> in this HTML")
    out: list[dict[str, str]] = []
    for el in prose.find_all(["p", "h2", "h3", "blockquote"], recursive=False):
        zh_span = el.find("span", class_="zh")
        en_span = el.find("span", class_="en")
        zh_text = " ".join((zh_span.get_text() if zh_span else el.get_text()).split()).strip()
        en_text = " ".join((en_span.get_text() if en_span else el.get_text()).split()).strip()
        if zh_text or en_text:
            out.append({"zh": zh_text, "en": en_text})
    return out


def text_hash(text: str, voice: str) -> str:
    return hashlib.sha256((voice + "\0" + text).encode("utf-8")).hexdigest()[:16]


async def render_one(text: str, voice: str, out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    com = edge_tts.Communicate(text, voice)
    await com.save(str(out_path))


async def render_article(slug: str, segments: list[dict[str, str]], voices: dict[str, str], force: bool) -> None:
    out_dir = AUDIO_ROOT / slug
    manifest_path = out_dir / "manifest.json"

    existing: dict = {}
    if manifest_path.exists() and not force:
        try:
            existing = json.loads(manifest_path.read_text(encoding="utf-8"))
        except Exception:
            pass

    new_manifest: dict = {
        "slug": slug,
        "segments": len(segments),
    }
    for lang in ("zh", "en"):
        new_manifest[lang] = {
            "voice": voices[lang],
            "count": len(segments),
            "hashes": [text_hash(seg[lang], voices[lang]) for seg in segments],
        }

    sem = asyncio.Semaphore(CONCURRENCY)
    tasks: list = []

    for lang in ("zh", "en"):
        voice = voices[lang]
        existing_hashes = existing.get(lang, {}).get("hashes", []) if isinstance(existing.get(lang), dict) else []
        for i, seg in enumerate(segments):
            text = seg[lang]
            if not text:
                continue
            out_path = out_dir / lang / f"{i}.mp3"
            wanted = new_manifest[lang]["hashes"][i]
            cached = existing_hashes[i] if i < len(existing_hashes) else None
            if cached == wanted and out_path.exists():
                continue  # cache hit

            print(f"  [{lang}] {i+1:>3}/{len(segments)}  ({len(text):>4} chars)  → {out_path.relative_to(REPO_ROOT)}")

            async def task(text=text, voice=voice, out_path=out_path):
                async with sem:
                    await render_one(text, voice, out_path)

            tasks.append(task())

    if tasks:
        await asyncio.gather(*tasks)
    else:
        print("  (all segments cached — nothing to render)")

    out_dir.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(new_manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"  ✅ wrote {manifest_path.relative_to(REPO_ROOT)}\n")


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("htmls", nargs="*", help="article HTML files (default: article-*.html + study-*.html)")
    p.add_argument("--voice-zh", default=DEFAULT_VOICES["zh"])
    p.add_argument("--voice-en", default=DEFAULT_VOICES["en"])
    p.add_argument("--force", action="store_true", help="re-render even if hash matches existing manifest")
    args = p.parse_args()

    if args.htmls:
        html_paths = [Path(h).resolve() for h in args.htmls]
    else:
        html_paths = sorted(REPO_ROOT.glob("article-*.html")) + sorted(REPO_ROOT.glob("study-*.html"))

    if not html_paths:
        print("no article-*.html / study-*.html found in repo root", file=sys.stderr)
        sys.exit(1)

    voices = {"zh": args.voice_zh, "en": args.voice_en}

    for html_path in html_paths:
        if not html_path.exists():
            print(f"⚠ skipping (not found): {html_path}", file=sys.stderr)
            continue
        slug = slugify(html_path)
        print(f"📄 {html_path.name}  →  /assets/audio/{slug}/")
        try:
            segments = extract_segments(html_path.read_text(encoding="utf-8-sig"))
        except ValueError as e:
            print(f"   skipping: {e}", file=sys.stderr)
            continue
        print(f"   {len(segments)} segments  ·  zh={voices['zh']}  ·  en={voices['en']}")
        asyncio.run(render_article(slug, segments, voices, args.force))


if __name__ == "__main__":
    main()
