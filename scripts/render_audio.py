"""Pre-render article paragraphs to MP3 using Microsoft Edge TTS.

Microsoft's Edge "Read Aloud" Neural voices (Xiaoxiao, HsiaoChen, Aria, etc.)
are broadcaster-quality and exposed for free via the unofficial edge-tts API.
We render each article paragraph once into one MP3 per (voice, language) pair,
ship them as static assets, and the player just <audio src="…">s them — no
runtime API calls, no rate limits, no key management, instant playback.

Multi-voice: pre-render *several* voices per language so users can pick from
the player's settings panel. Each voice goes into its own subfolder:

    assets/audio/<slug>/
        manifest.json
        zh/zh-TW-HsiaoChenNeural/0.mp3
        zh/zh-TW-HsiaoChenNeural/1.mp3 …
        zh/zh-CN-XiaoxiaoNeural/0.mp3 …
        en/en-US-AriaNeural/0.mp3 …
        en/en-GB-SoniaNeural/0.mp3 …

Usage:
    python scripts/render_audio.py
    python scripts/render_audio.py article-messiah-birthing-iran.html
    python scripts/render_audio.py --force   # ignore cache, re-render everything
    python scripts/render_audio.py \\
        --voices-zh zh-TW-HsiaoChenNeural,zh-TW-YunJheNeural \\
        --voices-en en-US-AriaNeural,en-US-GuyNeural

Hashes per (voice, text) are stored in manifest.json — re-runs only
re-render paragraphs that actually changed.
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

# Default voice lists. The first voice in each list is the "default" played by
# the Listen button before the user opens the picker.
DEFAULT_VOICES: dict[str, list[dict[str, str]]] = {
    "zh": [
        {"id": "zh-TW-HsiaoChenNeural", "name": "HsiaoChen 曉臻", "gender": "Female", "locale": "zh-TW", "localeLabel": "繁體中文 (台灣)"},
        {"id": "zh-TW-YunJheNeural",    "name": "YunJhe 雲哲",    "gender": "Male",   "locale": "zh-TW", "localeLabel": "繁體中文 (台灣)"},
        {"id": "zh-CN-XiaoxiaoNeural",  "name": "Xiaoxiao 晓晓",  "gender": "Female", "locale": "zh-CN", "localeLabel": "简体中文 (大陆)"},
        {"id": "zh-CN-YunxiNeural",     "name": "Yunxi 云希",     "gender": "Male",   "locale": "zh-CN", "localeLabel": "简体中文 (大陆)"},
    ],
    "en": [
        {"id": "en-US-AriaNeural",  "name": "Aria",  "gender": "Female", "locale": "en-US", "localeLabel": "English (US)"},
        {"id": "en-US-GuyNeural",   "name": "Guy",   "gender": "Male",   "locale": "en-US", "localeLabel": "English (US)"},
        {"id": "en-GB-SoniaNeural", "name": "Sonia", "gender": "Female", "locale": "en-GB", "localeLabel": "English (UK)"},
        {"id": "en-GB-RyanNeural",  "name": "Ryan",  "gender": "Male",   "locale": "en-GB", "localeLabel": "English (UK)"},
    ],
}

CONCURRENCY = 4


def slugify(html_path: Path) -> str:
    return html_path.stem


def extract_segments(html_text: str) -> list[dict[str, str]]:
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


async def render_one_with_timings(text: str, voice: str, mp3_path: Path, json_path: Path) -> None:
    """Render audio AND capture word-level boundaries for karaoke highlighting.

    Edge TTS yields {type: 'WordBoundary', offset, duration, text} events
    interleaved with audio chunks. Offsets/durations are in 100-ns units.
    """
    mp3_path.parent.mkdir(parents=True, exist_ok=True)
    com = edge_tts.Communicate(text, voice, boundary="WordBoundary")
    audio_chunks: list[bytes] = []
    raw_boundaries: list[dict] = []
    async for chunk in com.stream():
        if chunk["type"] == "audio":
            audio_chunks.append(chunk["data"])
        elif chunk["type"] == "WordBoundary":
            raw_boundaries.append(chunk)
    mp3_path.write_bytes(b"".join(audio_chunks))

    # Map each spoken word back to its character offset in the source text.
    # Edge TTS doesn't include text_offset directly, so we walk the source
    # forward, finding each word's next occurrence.
    words: list[dict] = []
    pos = 0
    for b in raw_boundaries:
        word_text = b["text"]
        idx = text.find(word_text, pos)
        if idx < 0:
            # Fallback: search from start (unusual — Edge TTS speaks in order)
            idx = text.find(word_text, 0)
        words.append({
            "text": word_text,
            "offset": idx,  # -1 means "could not locate in source"
            "start": round(b["offset"] / 10_000_000, 3),
            "end": round((b["offset"] + b["duration"]) / 10_000_000, 3),
        })
        if idx >= 0:
            pos = idx + len(word_text)

    duration = words[-1]["end"] if words else 0.0
    json_path.write_text(
        json.dumps({"duration": duration, "words": words}, ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8",
    )


def voice_meta_lookup(default_list: list[dict[str, str]], voice_id: str) -> dict[str, str]:
    for v in default_list:
        if v["id"] == voice_id:
            return v
    # User passed a voice id that isn't in our default catalog — invent meta.
    parts = voice_id.split("-")
    return {
        "id": voice_id,
        "name": parts[-1].replace("Neural", ""),
        "gender": "Unknown",
        "locale": "-".join(parts[:2]) if len(parts) >= 2 else voice_id,
        "localeLabel": "-".join(parts[:2]) if len(parts) >= 2 else voice_id,
    }


async def render_article(slug: str, segments: list[dict[str, str]], voices: dict[str, list[dict]], force: bool, with_timings: bool) -> None:
    out_dir = AUDIO_ROOT / slug
    manifest_path = out_dir / "manifest.json"

    # Old manifest, if any, lets us skip already-rendered files.
    existing: dict = {}
    if manifest_path.exists() and not force:
        try:
            existing = json.loads(manifest_path.read_text(encoding="utf-8"))
        except Exception:
            pass

    # Build the new manifest skeleton. Each voice carries `withTimings` so the
    # client knows whether to fetch the per-segment timings JSON for karaoke
    # highlighting (true only for runs that used --with-timings).
    new_manifest: dict = {
        "slug": slug,
        "segments": len(segments),
    }
    for lang, voice_list in voices.items():
        new_manifest[lang] = {
            "default": voice_list[0]["id"] if voice_list else None,
            "count": len(segments),
            "voices": [
                {
                    **v,
                    "hashes": [text_hash(seg[lang], v["id"]) for seg in segments],
                    "withTimings": with_timings,
                }
                for v in voice_list
            ],
        }

    sem = asyncio.Semaphore(CONCURRENCY)
    tasks: list = []
    skipped = 0

    for lang, voice_list in voices.items():
        for v in voice_list:
            voice_id = v["id"]
            wanted_hashes = [text_hash(seg[lang], voice_id) for seg in segments]

            # Look up existing hashes for the same voice in the old manifest.
            existing_voices = (existing.get(lang) or {}).get("voices") or []
            existing_hashes = []
            existing_with_timings = False
            for ev in existing_voices:
                if ev.get("id") == voice_id:
                    existing_hashes = ev.get("hashes") or []
                    existing_with_timings = bool(ev.get("withTimings"))
                    break

            for i, seg in enumerate(segments):
                text = seg[lang]
                if not text:
                    continue
                out_path  = out_dir / lang / voice_id / f"{i}.mp3"
                json_path = out_dir / lang / voice_id / f"{i}.json"
                wanted = wanted_hashes[i]
                cached = existing_hashes[i] if i < len(existing_hashes) else None
                # Skip only if (a) hash matches, (b) MP3 exists, and (c) if
                # this run wants timings, the timings JSON also already exists
                # (i.e. previous run also had --with-timings).
                if (
                    cached == wanted
                    and out_path.exists()
                    and (not with_timings or (existing_with_timings and json_path.exists()))
                ):
                    skipped += 1
                    continue

                tag = "+t" if with_timings else "  "
                print(f"  [{lang}/{voice_id}]{tag} {i+1:>3}/{len(segments)}  ({len(text):>4} chars)")

                async def task(text=text, voice_id=voice_id, out_path=out_path, json_path=json_path):
                    async with sem:
                        if with_timings:
                            await render_one_with_timings(text, voice_id, out_path, json_path)
                        else:
                            await render_one(text, voice_id, out_path)

                tasks.append(task())

    if tasks:
        await asyncio.gather(*tasks)
    if skipped:
        print(f"  (skipped {skipped} cached files)")

    out_dir.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(new_manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"  wrote {manifest_path.relative_to(REPO_ROOT)}\n")


def parse_voice_list(s: str | None, defaults: list[dict[str, str]]) -> list[dict[str, str]]:
    if not s:
        return defaults
    ids = [v.strip() for v in s.split(",") if v.strip()]
    return [voice_meta_lookup(defaults, vid) for vid in ids]


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("htmls", nargs="*", help="article HTML files (default: article-*.html + study-*.html)")
    p.add_argument("--voices-zh", default=None, help="comma-separated zh voice ids (overrides defaults)")
    p.add_argument("--voices-en", default=None, help="comma-separated en voice ids (overrides defaults)")
    p.add_argument("--force", action="store_true", help="re-render even if hash matches existing manifest")
    p.add_argument("--with-timings", action="store_true", help="capture per-word timings into <idx>.json next to each MP3 (for karaoke-style highlighting)")
    args = p.parse_args()

    if args.htmls:
        html_paths = [Path(h).resolve() for h in args.htmls]
    else:
        html_paths = sorted(REPO_ROOT.glob("article-*.html")) + sorted(REPO_ROOT.glob("study-*.html"))

    if not html_paths:
        print("no article-*.html / study-*.html found in repo root", file=sys.stderr)
        sys.exit(1)

    voices = {
        "zh": parse_voice_list(args.voices_zh, DEFAULT_VOICES["zh"]),
        "en": parse_voice_list(args.voices_en, DEFAULT_VOICES["en"]),
    }

    print(f"voices: zh={[v['id'] for v in voices['zh']]}")
    print(f"        en={[v['id'] for v in voices['en']]}\n")

    for html_path in html_paths:
        if not html_path.exists():
            print(f"skipping (not found): {html_path}", file=sys.stderr)
            continue
        slug = slugify(html_path)
        print(f"== {html_path.name}  ->  /assets/audio/{slug}/")
        try:
            segments = extract_segments(html_path.read_text(encoding="utf-8-sig"))
        except ValueError as e:
            print(f"   skipping: {e}", file=sys.stderr)
            continue
        print(f"   {len(segments)} segments x {len(voices['zh']) + len(voices['en'])} voices")
        asyncio.run(render_article(slug, segments, voices, args.force, args.with_timings))


if __name__ == "__main__":
    main()
