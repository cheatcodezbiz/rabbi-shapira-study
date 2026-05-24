"""Build per-speaker bilingual articles from yt_to_multispeaker.py output.

Reads sources/<videoId>/speakers_processed.json, and for each speaker segment:
  1. Generates a scripts/articles/<slug>.py content file via Ollama
  2. Runs build_article.py to compile the HTML
  3. Copies the speaker's frame.jpg to assets/images/<slug>.jpg
  4. Renders audio with render_audio.py (with timings for karaoke)
  5. Updates index.html with the new article card

Usage
-----
    python scripts/build_speaker_articles.py OlTpoHwveIM
    python scripts/build_speaker_articles.py OlTpoHwveIM --no-audio   # skip audio render
    python scripts/build_speaker_articles.py OlTpoHwveIM --dry-run    # preview only
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

REPO_ROOT   = Path(__file__).resolve().parent.parent
SOURCE_ROOT = REPO_ROOT / "sources"

OLLAMA_HOST  = os.environ.get("OLLAMA_HOST", "http://localhost:11434")
OLLAMA_MODEL = os.environ.get("OLLAMA_MODEL", "gemma4:e4b")

EVENT_SERIES_ZH = "天使長之夜 · 新婦之戰 5786"
EVENT_SERIES_EN = "Night of the Bride 5786 · Milchemet HaChatunah"


def ollama_generate(prompt: str, timeout: int = 900) -> str:
    import urllib.request
    url = f"{OLLAMA_HOST}/api/generate"
    body = json.dumps({
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False,
        "options": {"temperature": 0.25, "num_predict": 12000},
    }).encode("utf-8")
    req = urllib.request.Request(url, data=body, method="POST",
                                  headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8")).get("response", "").strip()


def escape_py_str(s: str) -> str:
    """Escape string for safe inclusion in a Python source file triple-quote."""
    return s.replace("\\", "\\\\").replace('"""', '\\"\\"\\"').replace("\r", "")


def generate_article_dict(speaker: dict, sp_dir: Path, event_meta: dict) -> str:
    """Ask Ollama to produce the Python article dict for one speaker."""
    zh_text = (sp_dir / "transcript.zh.txt").read_text(encoding="utf-8")[:6000]
    en_text = (sp_dir / "transcript.en.txt").read_text(encoding="utf-8")[:6000]
    analysis = (sp_dir / "analysis.md").read_text(encoding="utf-8")[:4000]

    name = speaker.get("speaker", "Speaker")
    topic = speaker.get("topic", "")
    slug  = f"article-notb-{speaker['slug'].replace(re.match(r'^\\d+-','').group() if re.match(r'^\\d+-', speaker['slug']) else '', '', 1)}"
    slug  = re.sub(r'[^a-z0-9-]', '', slug.lower())

    duration_sec = speaker.get("end", 0) - speaker.get("start", 0)
    duration_str = f"{int(duration_sec//60)}:{int(duration_sec%60):02d}"

    print(f"  [ollama] generating article dict for {name}…")
    prompt = f"""You are writing the content dict for a bilingual (Traditional Chinese / English) article about a speaker at "The Night of the Bride 5786" Shavuot event.

Speaker: {name}
Topic: {topic}
Duration: {duration_str}

Analysis:
{analysis}

Chinese transcript (excerpt):
{zh_text[:2000]}

English transcript (excerpt):
{en_text[:2000]}

Write a Python dict for this article. The format MUST match exactly:

article = {{
    "slug": "{slug}",
    "video_id": "{event_meta.get('id', 'OlTpoHwveIM')}",
    "video_duration": "{duration_str}",
    "date": "{event_meta.get('upload_date', '20260522')[:4]} · {event_meta.get('upload_date', '20260522')[4:6]} · {event_meta.get('upload_date', '20260522')[6:]}",
    "read_min": {max(5, int(duration_sec / 60 / 4))},
    "chip_zh": "新婦之夜 5786 · {name[:20]}",
    "chip_en": "Night of the Bride 5786 · {name[:30]}",
    "title_zh": "<BILINGUAL EVOCATIVE ZH TITLE>",
    "title_en": "<BILINGUAL EVOCATIVE EN TITLE>",
    "subtitle_zh": "<2-3 sentence zh subtitle with key themes and Hebrew terms>",
    "subtitle_en": "<2-3 sentence en subtitle with key themes and Hebrew terms>",
    "lead_zh": "<Opening paragraph in traditional Chinese, 150-200 chars, with bold/em HTML>",
    "lead_en": "<Opening paragraph in English, 150-200 words, with bold/em HTML>",
    "sections": [
        {{
            "heading_zh": "一、<section title in zh>",
            "heading_en": "I. <section title in en>",
            "body": [
                {{"type": "p", "zh": "<paragraph zh>", "en": "<paragraph en>"}},
                {{"type": "blockquote", "zh": "<quote zh>", "en": "<quote en>"}},
            ]
        }},
        # ... 4-7 more sections
    ],
    "closing_quote": {{
        "zh": "<final quote or blessing in zh>",
        "en": "<final quote or blessing in en>",
        "ref": "<source reference>"
    }},
    "youtube_url": "https://www.youtube.com/watch?v={event_meta.get('id', 'OlTpoHwveIM')}&t={int(speaker.get('start', 0))}s",
}}

Rules:
- Use Traditional Chinese (Taiwan standard) only
- Include Hebrew terms with transliteration where relevant
- 4-7 sections minimum
- Each section has 2-4 body items (p or blockquote)
- closing_quote should be the speaker's final blessing or key statement
- Output ONLY valid Python code (the article = {{...}} assignment), nothing else
"""
    response = ollama_generate(prompt)

    # Try to extract just the article dict
    m = re.search(r'article\s*=\s*\{', response)
    if m:
        response = response[m.start():]
    return response


def build_article_module(slug: str, content: str, out_path: Path) -> None:
    """Write a scripts/articles/<slug>.py file."""
    header = f"# Article — Night of the Bride 5786 speaker segment\n# Auto-generated by build_speaker_articles.py\n\n"
    out_path.write_text(header + content + "\n", encoding="utf-8")
    print(f"  wrote {out_path.relative_to(REPO_ROOT)}")


def build_html(slug: str) -> bool:
    """Run build_article.py for the given slug. Returns True if successful."""
    r = subprocess.run(
        [sys.executable, str(REPO_ROOT / "scripts" / "build_article.py"), slug],
        cwd=str(REPO_ROOT),
        capture_output=True, text=True, encoding="utf-8",
    )
    if r.returncode != 0:
        print(f"  [error] build_article.py failed:\n{r.stderr[:600]}")
        return False
    print(f"  built {slug}.html")
    return True


def copy_thumbnail(frame_path: Path, slug: str) -> Path:
    """Copy speaker frame to assets/images/<slug>.jpg."""
    dest = REPO_ROOT / "assets" / "images" / f"{slug}.jpg"
    if not dest.exists() and frame_path.exists():
        shutil.copy(frame_path, dest)
        print(f"  copied thumbnail → assets/images/{slug}.jpg")
    return dest


def add_to_index(slug: str, speaker: dict) -> None:
    """Prepend article card to index.html articles grid."""
    index_path = REPO_ROOT / "index.html"
    html = index_path.read_text(encoding="utf-8")

    # Check if already added
    if slug in html:
        print(f"  {slug} already in index.html")
        return

    name     = speaker.get("speaker", "Speaker")
    topic_zh = speaker.get("topic_zh", speaker.get("topic", ""))[:80]
    topic_en = speaker.get("topic", "")[:80]
    title_zh = speaker.get("title_zh", name)
    title_en = speaker.get("title_en", topic_en)
    date_str = speaker.get("date", "2026 · 5 · 22")

    card = f'''        <article class="card">
          <a href="{slug}.html" style="display:block;text-decoration:none;color:inherit;">
            <div class="card-img c1" style="background-image:url('assets/images/{slug}.jpg');background-size:cover;background-position:center;"></div>
            <div class="card-body">
              <div class="card-tag"><span class="zh">新婦之夜 5786 · {name[:30]}</span><span class="en">Night of the Bride 5786 · {name[:30]}</span></div>
              <h4><span class="zh">{title_zh[:80]}</span><span class="en">{title_en[:80]}</span></h4>
              <p><span class="zh">{topic_zh}⋯</span><span class="en">{topic_en}⋯</span></p>
              <div class="card-foot">
                <span>{date_str}</span>
                <span><span class="zh">阅读全文 →</span><span class="en">Read More →</span></span>
              </div>
            </div>
          </a>
        </article>

'''

    # Insert before the first article card
    marker = '        <article class="card">'
    pos = html.find(marker)
    if pos < 0:
        print(f"  [warn] could not find article grid in index.html")
        return
    new_html = html[:pos] + card + html[pos:]
    index_path.write_text(new_html, encoding="utf-8")
    print(f"  added {slug} card to index.html")


def render_audio(slug: str) -> None:
    """Run render_audio.py --with-timings for the given HTML file."""
    r = subprocess.run(
        [sys.executable, "scripts/render_audio.py", f"{slug}.html", "--with-timings"],
        cwd=str(REPO_ROOT),
        text=True, encoding="utf-8",
    )
    if r.returncode != 0:
        print(f"  [warn] render_audio.py returned {r.returncode}")
    else:
        print(f"  audio rendered for {slug}")


def process_speakers(video_id: str, dry_run: bool = False, no_audio: bool = False) -> None:
    src_dir = SOURCE_ROOT / video_id
    speakers_path = src_dir / "speakers_processed.json"

    if not speakers_path.exists():
        print(f"ERROR: {speakers_path} not found. Run yt_to_multispeaker.py first.", file=sys.stderr)
        sys.exit(1)

    speakers = json.loads(speakers_path.read_text(encoding="utf-8"))
    meta = json.loads((src_dir / "meta.json").read_text(encoding="utf-8"))
    spk_base = src_dir / "speakers"

    print(f"== building articles for {len(speakers)} speakers from {video_id}")
    print(f"   event: {meta.get('title', '')[:80]}\n")

    for i, sp in enumerate(speakers):
        name = sp.get("speaker", f"Speaker{i+1}")
        sp_dir = spk_base / sp["slug"]
        print(f"\n[{i+1}/{len(speakers)}] {name}")

        if not sp_dir.exists():
            print(f"  [skip] speaker dir not found: {sp_dir}")
            continue

        # Derive article slug from speaker slug + event prefix
        raw_slug = sp["slug"]  # e.g. "01-rabbi-itzhak-shapira"
        num_match = re.match(r'^(\d+)-', raw_slug)
        num = num_match.group(1) if num_match else str(i+1).zfill(2)
        name_slug = re.sub(r'[^a-z0-9]', '-', name.lower())[:25].strip('-')
        article_slug = f"article-notb-{num}-{name_slug}"

        html_path = REPO_ROOT / f"{article_slug}.html"
        article_py_path = REPO_ROOT / "scripts" / "articles" / f"{article_slug}.py"
        frame_path = sp_dir / "frame.jpg"

        if dry_run:
            print(f"  would build → {article_slug}.html")
            continue

        # 1. Generate article module (if not exists)
        if not article_py_path.exists():
            try:
                content = generate_article_dict(sp, sp_dir, meta)
                build_article_module(article_slug, content, article_py_path)
            except Exception as e:
                print(f"  [error] article dict generation failed: {e}")
                continue

        # 2. Build HTML
        if not html_path.exists():
            if not build_html(article_slug):
                print(f"  [warn] skipping {article_slug} due to build error")
                continue

        # 3. Copy thumbnail
        copy_thumbnail(frame_path, article_slug)

        # 4. Add to index.html
        sp["date"] = f"{meta.get('upload_date', '20260522')[:4]} · {meta.get('upload_date', '20260522')[4:6]} · {meta.get('upload_date', '20260522')[6:]}"
        add_to_index(article_slug, sp)

        # 5. Render audio (optional, slow)
        if not no_audio and html_path.exists():
            render_audio(article_slug)

    print("\n== done. Now commit + deploy:")
    print("   git add -A && git commit -m 'Add Night of the Bride speaker articles'")
    print("   vercel --prod")


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("video_id", help="YouTube video ID (e.g. OlTpoHwveIM)")
    p.add_argument("--dry-run", action="store_true", help="preview only, don't write files")
    p.add_argument("--no-audio", action="store_true", help="skip audio rendering")
    p.add_argument("--ollama-model", default=None)
    args = p.parse_args()

    global OLLAMA_MODEL
    if args.ollama_model: OLLAMA_MODEL = args.ollama_model

    process_speakers(args.video_id, dry_run=args.dry_run, no_audio=args.no_audio)


if __name__ == "__main__":
    main()
