"""Build a new bilingual article HTML from a YAML-style content file.

Takes the existing article-messiah-birthing-iran.html as the structural
template (CSS, nav, footer, settings panel — everything that's the same
across articles) and replaces just the parts that change per article:

    * <title> + meta description
    * Article cover image + chip + bilingual title + subtitle + byline date
    * Meta strip (date, read time, "Watch Original" YouTube URL + duration)
    * Article body (lead paragraph + numbered sections + closing quote)

Content is supplied via a Python dict written to scripts/articles/<slug>.py
which we import. This way per-article content is plain Python (easy to
write paragraph by paragraph) instead of escaped JSON or YAML.

Usage:
    python scripts/build_article.py article-zion-birth-pangs

Reads:  scripts/articles/<slug>.py  →  module attribute `article`
Writes: <slug>.html  in repo root
"""

from __future__ import annotations

import argparse
import importlib.util
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
TEMPLATE  = REPO_ROOT / "article-messiah-birthing-iran.html"


def load_article_module(slug: str):
    p = REPO_ROOT / "scripts" / "articles" / f"{slug}.py"
    if not p.exists():
        sys.exit(f"missing content file: {p.relative_to(REPO_ROOT)}")
    spec = importlib.util.spec_from_file_location(f"article_{slug}", p)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    if not hasattr(mod, "article"):
        sys.exit(f"{p} must define `article = {{...}}`")
    return mod.article


def render_section(s: dict) -> str:
    """One <h2> + N <p>/<blockquote>/<h3> children. `s` is {heading_zh, heading_en, body[]}."""
    out = [f'    <h2><span class="zh">{s["heading_zh"]}</span><span class="en">{s["heading_en"]}</span></h2>\n']
    for b in s["body"]:
        if b["type"] == "p":
            out.append(f'    <p>\n      <span class="zh">{b["zh"]}</span>\n      <span class="en">{b["en"]}</span>\n    </p>\n\n')
        elif b["type"] == "blockquote":
            cls = ' class="' + b["class"] + '"' if b.get("class") else ""
            cite_zh = f'<cite>——{b["cite_zh"]}</cite>' if b.get("cite_zh") else ""
            cite_en = f'<cite>— {b["cite_en"]}</cite>' if b.get("cite_en") else ""
            out.append(
                f'    <blockquote{cls}>\n'
                f'      <span class="zh">{b["zh"]}{cite_zh}</span>\n'
                f'      <span class="en">{b["en"]}{cite_en}</span>\n'
                f'    </blockquote>\n\n'
            )
        elif b["type"] == "h3":
            out.append(f'    <h3><span class="zh">{b["zh"]}</span><span class="en">{b["en"]}</span></h3>\n')
        else:
            raise ValueError(f"unknown body block type: {b['type']}")
    return "".join(out)


def render_prose(article: dict) -> str:
    parts = [
        '  <div class="article-prose">\n\n',
        f'    <p class="article-lead">\n      <span class="zh">{article["lead_zh"]}</span>\n      <span class="en">{article["lead_en"]}</span>\n    </p>\n\n',
    ]
    for s in article["sections"]:
        parts.append(render_section(s))
    parts.append("  </div>\n")
    return "".join(parts)


def render_cover(article: dict) -> str:
    a = article
    chip_zh = a.get("chip_zh", "拉比沙皮拉教导")
    chip_en = a.get("chip_en", "Rabbi Shapira Teaching")
    img_path = f"assets/images/{a['slug']}.jpg"
    return (
        '  <div class="article-cover">\n'
        f'    <img src="{img_path}" alt="{a["title_en"]}" />\n'
        '    <div class="article-cover-overlay"></div>\n'
        '    <div class="article-cover-text">\n'
        f'      <span class="article-chip"><span class="zh">{chip_zh}</span><span class="en">{chip_en}</span></span>\n'
        '      <h1 class="article-title">\n'
        f'        <span class="zh">{a["title_zh"]}</span>\n'
        f'        <span class="en">{a["title_en"]}</span>\n'
        '      </h1>\n'
        '      <p class="article-subtitle">\n'
        f'        <span class="zh">{a["subtitle_zh"]}</span>\n'
        f'        <span class="en">{a["subtitle_en"]}</span>\n'
        '      </p>\n'
        '      <div class="article-byline">\n'
        f'        <span class="zh">沙皮拉拉比博士 · Ahavat Ammi 事工</span>\n'
        f'        <span class="en">Rabbi Dr. Itzhak Shapira · Ahavat Ammi Ministries</span>\n'
        '      </div>\n'
        '    </div>\n'
        '  </div>\n'
    )


def render_meta_strip(article: dict) -> str:
    a = article
    yt_url = f"https://www.youtube.com/watch?v={a['video_id']}"
    return (
        '  <div class="article-meta-strip">\n'
        f'    <span>{a["date"]}</span>\n'
        '    <span class="meta-dot">·</span>\n'
        f'    <span><span class="zh">约 {a["read_min"]} 分钟阅读</span><span class="en">~{a["read_min"]} min read</span></span>\n'
        '    <span class="meta-dot">·</span>\n'
        f'    <a href="{yt_url}" target="_blank" rel="noopener" class="meta-watch">\n'
        f'      ▶ <span class="zh">观看原始视频 ({a["video_duration"]})</span><span class="en">Watch Original ({a["video_duration"]})</span>\n'
        '    </a>\n'
        '    <span class="meta-dot">·</span>\n'
        '    <button id="tts-launch" class="tts-launch" aria-label="Listen to article">\n'
        '      <span class="tts-ico">🔊</span>\n'
        '      <span class="zh">聆听全文</span>\n'
        '      <span class="en">Listen</span>\n'
        '    </button>\n'
        '  </div>\n'
    )


def build(slug: str, article: dict) -> str:
    template = TEMPLATE.read_text(encoding="utf-8-sig")

    # 1. Title + meta description
    template = re.sub(
        r"<title>.*?</title>",
        f"<title>{article['title_zh']} — 妥拉之光</title>",
        template, count=1, flags=re.DOTALL,
    )
    template = re.sub(
        r'<meta name="description" content=".*?" />',
        f'<meta name="description" content="{article["title_en"]} — A teaching by Rabbi Dr. Itzhak Shapira (Ahavat Ammi Ministries)" />',
        template, count=1,
    )

    # 2. Article-cover (replace whole <div class="article-cover">…</div>)
    template = re.sub(
        r'  <div class="article-cover">.*?\n  </div>\n',
        render_cover(article),
        template, count=1, flags=re.DOTALL,
    )

    # 3. Meta strip
    template = re.sub(
        r'  <div class="article-meta-strip">.*?\n  </div>\n',
        render_meta_strip(article),
        template, count=1, flags=re.DOTALL,
    )

    # 4. Article-prose (everything between the opening tag and the closing </div>
    #    just before <footer>). The template has nothing between </article-prose>
    #    and </article>; we replace from <div class="article-prose"> through
    #    its closing </div> and append the closing </article> right after.
    template = re.sub(
        r'  <div class="article-prose">.*?\n  </div>\n',
        render_prose(article),
        template, count=1, flags=re.DOTALL,
    )

    return template


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("slug", help="article slug, e.g. article-zion-birth-pangs")
    args = p.parse_args()
    article = load_article_module(args.slug)
    if article["slug"] != args.slug:
        sys.exit(f"slug mismatch: arg={args.slug} but content says {article['slug']}")
    out = build(args.slug, article)
    out_path = REPO_ROOT / f"{args.slug}.html"
    out_path.write_text(out, encoding="utf-8")
    print(f"wrote {out_path.relative_to(REPO_ROOT)}  ({out_path.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
