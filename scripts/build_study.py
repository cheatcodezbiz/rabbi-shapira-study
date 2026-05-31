"""Build a bilingual study-guide HTML from a Python content module.

Mirrors build_article.py: the existing study-jewish-messiah.html is the
structural template (CSS, nav, footer, settings panel, TTS player — all the
chrome that is identical across every study guide). This script swaps in only
the parts that change per guide:

    * <title> + meta description + og:title/og:description + audio-slug
    * Hero cover (chip line, bilingual headline, deck, byline)
    * Meta strip (lesson count, read time, "Get the Book" link)
    * Article body (lead + intro rhythm + 8 lesson blocks + closing quote + CTA)

Content lives in scripts/studies/<slug>.py as a module attribute `study`.

Usage:
    python scripts/build_study.py study-divided-lives
    python scripts/build_study.py study-divided-lives study-gods-body study-medieval-preaching

Reads:  scripts/studies/<slug>.py  ->  module attribute `study`
Writes: <slug>.html  in repo root
"""

from __future__ import annotations

import importlib.util
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
TEMPLATE  = REPO_ROOT / "study-jewish-messiah.html"


def load_study_module(slug: str):
    p = REPO_ROOT / "scripts" / "studies" / f"{slug}.py"
    if not p.exists():
        sys.exit(f"missing content file: {p.relative_to(REPO_ROOT)}")
    spec = importlib.util.spec_from_file_location(f"study_{slug.replace('-', '_')}", p)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    if not hasattr(mod, "study"):
        sys.exit(f"{p} must define `study = {{...}}`")
    return mod.study


# ── Body block renderers ──────────────────────────────────────────────

def render_body_block(b: dict) -> str:
    t = b["type"]
    if t == "p":
        return (
            f'      <p>\n'
            f'        <span class="zh">{b["zh"]}</span>\n'
            f'        <span class="en">{b["en"]}</span>\n'
            f'      </p>\n'
        )
    if t == "blockquote":
        cls = ' class="' + b["class"] + '"' if b.get("class") else ""
        cite = ""
        if b.get("cite"):
            cite = f'\n        <cite>{b["cite"]}</cite>'
        return (
            f'      <blockquote{cls}>\n'
            f'        <span class="zh">{b["zh"]}</span>\n'
            f'        <span class="en">{b["en"]}</span>{cite}\n'
            f'      </blockquote>\n'
        )
    if t == "ul":
        items = "".join(
            f'        <li><span class="zh">{it["zh"]}</span><span class="en">{it["en"]}</span></li>\n'
            for it in b["items"]
        )
        return f'      <ul class="lesson-questions">\n{items}      </ul>\n'
    raise ValueError(f"unknown body block type: {t}")


def render_step(step: dict) -> str:
    out = [
        f'      <h3 class="lesson-step">\n'
        f'        <span class="zh">{step["label_zh"]}</span>\n'
        f'        <span class="en">{step["label_en"]}</span>\n'
        f'      </h3>\n'
    ]
    for b in step["body"]:
        out.append(render_body_block(b))
    return "".join(out)


def render_lesson(les: dict) -> str:
    out = [
        f'    <!-- ─────────────  LESSON {les["num"]}  ───────────── -->\n',
        f'    <div class="lesson-block">\n',
        f'      <div class="lesson-num">{les["heb"]} &nbsp;·&nbsp; {les["num"]}</div>\n',
        f'      <h2 class="lesson-title">\n',
        f'        <span class="zh">{les["title_zh"]}</span>\n',
        f'        <span class="en">{les["title_en"]}</span>\n',
        f'      </h2>\n\n',
    ]
    for step in les["steps"]:
        out.append(render_step(step))
        out.append("\n")
    out.append("    </div>\n\n")
    return "".join(out)


def render_intro_block(b: dict) -> str:
    if b["type"] == "p":
        cls = ' class="' + b["class"] + '"' if b.get("class") else ""
        return (
            f'    <p{cls}>\n'
            f'      <span class="zh">{b["zh"]}</span>\n'
            f'      <span class="en">{b["en"]}</span>\n'
            f'    </p>\n\n'
        )
    if b["type"] == "blockquote":
        return (
            f'    <blockquote>\n'
            f'      <span class="zh">\n{b["zh"]}\n      </span>\n'
            f'      <span class="en">\n{b["en"]}\n      </span>\n'
            f'    </blockquote>\n\n'
        )
    raise ValueError(f"unknown intro block type: {b['type']}")


def render_article(s: dict, slug: str) -> str:
    cover_img = s.get("cover_img", "assets/remnant.jpg")
    parts = [
        '<!-- ── Featured Article (Editorial) ─────────────────── -->\n',
        '<article class="article-feature" id="featured-article">\n\n',
        '  <div class="article-cover">\n',
        f'    <img src="{cover_img}" alt="{s["cover_alt"]}" class="article-cover-img" />\n',
        '    <div class="article-cover-overlay"></div>\n',
        '    <div class="article-cover-text">\n',
        '      <div class="article-tag-line">\n',
        f'        <span class="zh">{s["tagline_zh"]}</span>\n',
        f'        <span class="en">{s["tagline_en"]}</span>\n',
        '      </div>\n',
        '      <h1 class="article-headline">\n',
        f'        <span class="zh">{s["headline_zh"]}</span>\n',
        f'        <span class="en">{s["headline_en"]}</span>\n',
        '      </h1>\n',
        '      <p class="article-deck">\n',
        f'        <span class="zh">{s["deck_zh"]}</span>\n',
        f'        <span class="en">{s["deck_en"]}</span>\n',
        '      </p>\n',
        '      <div class="article-byline">\n',
        f'        <span class="zh">{s["byline_zh"]}</span>\n',
        f'        <span class="en">{s["byline_en"]}</span>\n',
        '      </div>\n',
        '    </div>\n',
        '  </div>\n\n',
        '  <div class="article-meta-strip">\n',
        '    <span><span class="zh">8 堂课程</span><span class="en">8 Lessons</span></span>\n',
        '    <span class="meta-dot">·</span>\n',
        f'    <span><span class="zh">{s["readtime_zh"]}</span><span class="en">{s["readtime_en"]}</span></span>\n',
        '    <span class="meta-dot">·</span>\n',
        '    <span><span class="zh">自助 / 小组皆宜</span><span class="en">Self-paced or small group</span></span>\n',
        '    <span class="meta-dot">·</span>\n',
        f'    <a href="{s["book_url"]}" target="_blank" rel="noopener" class="meta-watch">\n',
        f'      📖 <span class="zh">{s["book_link_zh"]}</span><span class="en">{s["book_link_en"]}</span>\n',
        '    </a>\n',
        '    <span class="meta-dot">·</span>\n',
        '    <button id="tts-launch" class="tts-launch" aria-label="Listen to study guide">\n',
        '      <span class="tts-ico">🔊</span>\n',
        '      <span class="zh">聆听全文</span>\n',
        '      <span class="en">Listen</span>\n',
        '    </button>\n',
        '  </div>\n\n',
        '  <div class="article-prose">\n',
        '    <p class="article-lead">\n',
        f'      <span class="zh">{s["lead_zh"]}</span>\n',
        f'      <span class="en">{s["lead_en"]}</span>\n',
        '    </p>\n\n',
    ]
    for b in s["intro"]:
        parts.append(render_intro_block(b))
    parts.append('    <hr class="article-rule" />\n\n')
    for les in s["lessons"]:
        parts.append(render_lesson(les))
    # Closing
    parts.append('    <h2 class="lesson-title" style="text-align:center;border:none;">\n')
    parts.append(f'      <span class="zh">{s["closing_title_zh"]}</span>\n')
    parts.append(f'      <span class="en">{s["closing_title_en"]}</span>\n')
    parts.append('    </h2>\n\n')
    parts.append('    <blockquote class="closing-quote">\n')
    parts.append(f'      <span class="zh">{s["closing_zh"]}</span>\n')
    parts.append(f'      <span class="en">{s["closing_en"]}</span>\n')
    parts.append('    </blockquote>\n\n')
    parts.append('    <div class="article-cta-block">\n')
    parts.append(f'      <a href="{s["cta_url"]}" target="_blank" rel="noopener" class="cta-watch-video" style="background: var(--gold);">\n')
    parts.append(f'        📖 <span class="zh">{s["cta_zh"]}</span><span class="en">{s["cta_en"]}</span>\n')
    parts.append('      </a>\n')
    parts.append('    </div>\n\n')
    parts.append('  </div>\n')
    parts.append('</article>')
    return "".join(parts)


def sub_once(pattern: str, repl: str, text: str) -> str:
    # Use a function replacement so backslashes / group refs in `repl` are literal.
    new, n = re.subn(pattern, lambda m: repl, text, count=1, flags=re.S)
    if n != 1:
        raise RuntimeError(f"pattern not found exactly once: {pattern!r} (matched {n})")
    return new


def build(slug: str) -> None:
    s = load_study_module(slug)
    html = TEMPLATE.read_text(encoding="utf-8")

    html = sub_once(r"<title>.*?</title>", f'<title>{s["title_tag"]}</title>', html)
    html = sub_once(r'<meta name="description" content="[^"]*"',
                    f'<meta name="description" content="{s["meta_desc"]}"', html)
    html = sub_once(r'<meta name="audio-slug" content="[^"]*"',
                    f'<meta name="audio-slug" content="{slug}"', html)
    html = sub_once(r'<meta property="og:title" content="[^"]*"',
                    f'<meta property="og:title" content="{s["og_title"]}"', html)
    html = sub_once(r'<meta property="og:description" content="[^"]*"',
                    f'<meta property="og:description" content="{s["og_desc"]}"', html)

    new_article = render_article(s, slug)
    html = sub_once(r'<!-- ── Featured Article \(Editorial\).*?</article>', new_article, html)

    out = REPO_ROOT / f"{slug}.html"
    out.write_text(html, encoding="utf-8")
    # quick sanity: count lessons rendered
    n_lessons = html.count('class="lesson-block"')
    print(f"  wrote {out.name}  ({n_lessons} lessons, {len(html):,} bytes)")


def main() -> None:
    slugs = sys.argv[1:]
    if not slugs:
        sys.exit("usage: python scripts/build_study.py <slug> [<slug> ...]")
    for slug in slugs:
        print(f"== building {slug}")
        build(slug)


if __name__ == "__main__":
    main()
