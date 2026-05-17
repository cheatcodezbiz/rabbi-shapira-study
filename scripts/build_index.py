"""Build the RAG knowledge index for the study-partner chatbot.

Walks every *.html page in the site, extracts the readable article body
(everything inside `.article-prose`, `.rabbi-bio`, or `.book-body`),
splits the bilingual spans (.zh / .en) so each language is searchable on
its own, chunks the prose, embeds it with Voyage AI, and upserts the
vectors into Pinecone.

Idempotent: each chunk is hashed; if the hash is unchanged we skip the
embedding call (saves money on re-runs).

Env vars required:
  PINECONE_API_KEY        — Pinecone account key
  PINECONE_INDEX_NAME     — Pinecone serverless index name (must already exist)
  VOYAGE_API_KEY          — Voyage AI key for embeddings

Optional:
  EMBED_MODEL             — default: voyage-3-lite  (512 dims)
  EMBED_DIM               — default: 512  (must match the Pinecone index)
  CHUNK_TOKENS            — soft target tokens per chunk (default 450)
  CHUNK_OVERLAP_TOKENS    — overlap between consecutive chunks (default 60)
  SITE_ROOT               — repo root to scan (default: parent of this script)
  DRY_RUN=1               — print plan, don't call Pinecone

Run from the repo root:
    pip install -r scripts/requirements.txt
    python scripts/build_index.py
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import sys
import time
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Iterable

# Third-party — see scripts/requirements.txt
from bs4 import BeautifulSoup, NavigableString
from pinecone import Pinecone
import requests


# ─── Configuration ──────────────────────────────────────────────────────────

SITE_ROOT = Path(os.environ.get("SITE_ROOT") or Path(__file__).resolve().parent.parent)
STATE_DIR = SITE_ROOT / ".rag-state"
STATE_DIR.mkdir(exist_ok=True)
HASH_LEDGER = STATE_DIR / "chunk_hashes.json"

EMBED_MODEL = os.environ.get("EMBED_MODEL", "voyage-3-lite")
EMBED_DIM = int(os.environ.get("EMBED_DIM", "512"))
CHUNK_TOKENS = int(os.environ.get("CHUNK_TOKENS", "450"))
CHUNK_OVERLAP_TOKENS = int(os.environ.get("CHUNK_OVERLAP_TOKENS", "60"))

DRY_RUN = bool(os.environ.get("DRY_RUN"))

# Files we never index (nav-only, footers, etc.) — everything else gets walked.
SKIP_FILES = {"404.html"}


# ─── HTML extraction ────────────────────────────────────────────────────────

# A "chunk container" is any element whose text should be grouped as one
# semantic block. Study guides have `.lesson-block`; articles have
# `.article-prose`; the home page has `.rabbi-bio` and `.book-body`.
CHUNK_CONTAINER_SELECTORS = [
    ".lesson-block",      # study-guide lessons (perfect natural chunks)
    ".article-prose",     # blog articles
    ".rabbi-bio",         # rabbi bio on home page
    ".book-body",         # book card descriptions
    ".featured .feat-body",
]

# Elements to strip inside a container before reading text.
STRIP_INSIDE_CONTAINER = ["script", "style", "noscript", "button", "audio", "video", "svg"]


@dataclass
class Chunk:
    chunk_id: str
    slug: str          # e.g. "study-romans11-jewish-dna"
    url: str           # e.g. "/study-romans11-jewish-dna"
    title_zh: str
    title_en: str
    section: str       # e.g. "Lesson 4 · ד 04 ·  ..." or "§Article"
    anchor: str        # in-page anchor if any, else ""
    lang: str          # "zh" | "en"  (one chunk per lang)
    text: str          # the actual chunk text


def _strip_inside(el):
    """Remove non-content elements that pollute the text."""
    for sel in STRIP_INSIDE_CONTAINER:
        for tag in el.find_all(sel):
            tag.decompose()


def _lang_text(node) -> tuple[str, str]:
    """Walk an HTML subtree and return (zh_text, en_text) by following
    the site's bilingual convention: <span class="zh">…</span> /
    <span class="en">…</span>. Text outside those spans is shared (added
    to both languages).
    """
    zh, en, shared = [], [], []
    for el in node.descendants:
        if isinstance(el, NavigableString):
            # Skip if any ancestor in this node is a .zh or .en span — handled below.
            parent_classes = []
            p = el.parent
            while p and p is not node:
                if p.has_attr("class"):
                    parent_classes.extend(p["class"])
                p = p.parent
            if "zh" in parent_classes and "en" not in parent_classes:
                zh.append(str(el))
            elif "en" in parent_classes and "zh" not in parent_classes:
                en.append(str(el))
            else:
                shared.append(str(el))
    zh_text = re.sub(r"\s+", " ", " ".join(shared + zh)).strip()
    en_text = re.sub(r"\s+", " ", " ".join(shared + en)).strip()
    return zh_text, en_text


def _page_title(soup: BeautifulSoup) -> tuple[str, str]:
    """Return (zh_title, en_title) for a page. Falls back to <title>."""
    h = soup.select_one(".article-headline") or soup.select_one("h1") or soup.select_one(".hero-title")
    if h:
        zh, en = _lang_text(h)
        if zh or en:
            return zh or en, en or zh
    if soup.title and soup.title.string:
        return soup.title.string.strip(), soup.title.string.strip()
    return "", ""


def _section_label(container) -> str:
    """Best-effort label for the chunk: lesson title, h2, or 'Article'."""
    if "lesson-block" in (container.get("class") or []):
        lt = container.select_one(".lesson-title")
        if lt:
            zh, en = _lang_text(lt)
            return (zh or en) or "Lesson"
        return "Lesson"
    h2 = container.find("h2")
    if h2:
        zh, en = _lang_text(h2)
        return (zh or en) or "Section"
    return "Section"


def _anchor_for(container) -> str:
    """The container's id, or the nearest ancestor's id."""
    el = container
    while el is not None:
        if el.has_attr("id"):
            return el["id"]
        el = el.parent
    return ""


# ─── Chunking ───────────────────────────────────────────────────────────────

# Quick & cheap token estimator. We don't need perfect — Voyage caps at
# 32k tokens per text. ~4 chars per English token, ~1.6 chars per CJK char.
def _est_tokens(s: str) -> int:
    cjk = sum(1 for c in s if 0x4E00 <= ord(c) <= 0x9FFF)
    other = len(s) - cjk
    return int(cjk / 1.6 + other / 4)


def _split_paragraphs(text: str) -> list[str]:
    """Split a chunk's raw text on sentence boundaries — works for both
    Chinese (。！？) and English (. ! ?)."""
    # Normalise whitespace then split on sentence enders, keeping them.
    text = re.sub(r"\s+", " ", text).strip()
    parts = re.split(r"(?<=[。！？\.\!\?])\s+", text)
    return [p for p in parts if p]


def _pack_chunks(sentences: list[str], target: int, overlap: int) -> list[str]:
    """Greedy pack sentences into ~target-token chunks with overlap."""
    chunks, cur, cur_tokens = [], [], 0
    for s in sentences:
        t = _est_tokens(s)
        if cur and cur_tokens + t > target:
            chunks.append(" ".join(cur))
            # carry over `overlap` tokens worth of trailing sentences
            carry, carried = [], 0
            for sent in reversed(cur):
                if carried >= overlap:
                    break
                carry.insert(0, sent)
                carried += _est_tokens(sent)
            cur = carry
            cur_tokens = carried
        cur.append(s)
        cur_tokens += t
    if cur:
        chunks.append(" ".join(cur))
    return chunks


# ─── Page → chunks ──────────────────────────────────────────────────────────

def extract_chunks_from_html(html: str, slug: str, url: str) -> Iterable[Chunk]:
    soup = BeautifulSoup(html, "html.parser")
    # Strip global navigation/footer noise at the page level too.
    for sel in ["nav", "footer", "header", ".topbar"]:
        for el in soup.select(sel):
            el.decompose()

    title_zh, title_en = _page_title(soup)

    containers = []
    for sel in CHUNK_CONTAINER_SELECTORS:
        containers.extend(soup.select(sel))
    # De-duplicate while preserving order.
    seen = set()
    unique = []
    for c in containers:
        if id(c) in seen:
            continue
        seen.add(id(c))
        unique.append(c)
    containers = unique

    if not containers:
        return

    for cidx, container in enumerate(containers):
        _strip_inside(container)
        section = _section_label(container)
        anchor = _anchor_for(container)
        zh_full, en_full = _lang_text(container)

        for lang, text in (("zh", zh_full), ("en", en_full)):
            text = text.strip()
            if not text or len(text) < 40:
                continue
            sentences = _split_paragraphs(text)
            chunks = _pack_chunks(sentences, CHUNK_TOKENS, CHUNK_OVERLAP_TOKENS)
            for i, body in enumerate(chunks):
                chunk_id = f"{slug}::{cidx:02d}::{lang}::{i:02d}"
                yield Chunk(
                    chunk_id=chunk_id,
                    slug=slug,
                    url=url,
                    title_zh=title_zh,
                    title_en=title_en,
                    section=section,
                    anchor=anchor,
                    lang=lang,
                    text=body,
                )


# ─── Embeddings (Voyage AI) ─────────────────────────────────────────────────

VOYAGE_URL = "https://api.voyageai.com/v1/embeddings"


def voyage_embed(texts: list[str], input_type: str = "document") -> list[list[float]]:
    """Batch embed via Voyage AI. Voyage supports up to 128 texts per call."""
    api_key = os.environ.get("VOYAGE_API_KEY")
    if not api_key:
        raise RuntimeError("VOYAGE_API_KEY not set")
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    out: list[list[float]] = []
    for i in range(0, len(texts), 64):
        batch = texts[i : i + 64]
        body = {
            "model": EMBED_MODEL,
            "input": batch,
            "input_type": input_type,
            "output_dimension": EMBED_DIM,
        }
        for attempt in range(4):
            r = requests.post(VOYAGE_URL, headers=headers, json=body, timeout=60)
            if r.status_code == 200:
                break
            if r.status_code in (429, 500, 502, 503, 504):
                time.sleep(2 ** attempt)
                continue
            raise RuntimeError(f"Voyage error {r.status_code}: {r.text[:300]}")
        else:
            raise RuntimeError(f"Voyage retries exhausted: {r.text[:300]}")
        data = r.json()["data"]
        # Voyage returns objects with index + embedding; preserve order.
        data.sort(key=lambda d: d["index"])
        out.extend(d["embedding"] for d in data)
    return out


# ─── Pinecone upsert ────────────────────────────────────────────────────────

def _pinecone_index():
    api_key = os.environ.get("PINECONE_API_KEY")
    index_name = os.environ.get("PINECONE_INDEX_NAME")
    if not (api_key and index_name):
        raise RuntimeError("PINECONE_API_KEY and PINECONE_INDEX_NAME must be set")
    pc = Pinecone(api_key=api_key)
    return pc.Index(index_name)


# ─── Hash ledger (skip unchanged chunks) ────────────────────────────────────

def _load_ledger() -> dict:
    if HASH_LEDGER.exists():
        try:
            return json.loads(HASH_LEDGER.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return {}
    return {}


def _save_ledger(ledger: dict) -> None:
    HASH_LEDGER.write_text(
        json.dumps(ledger, ensure_ascii=False, indent=2, sort_keys=True),
        encoding="utf-8",
    )


def _chunk_hash(c: Chunk) -> str:
    h = hashlib.sha256()
    h.update(c.text.encode("utf-8"))
    h.update(EMBED_MODEL.encode("utf-8"))
    h.update(str(EMBED_DIM).encode("utf-8"))
    return h.hexdigest()[:16]


# ─── Main ───────────────────────────────────────────────────────────────────

def discover_pages(root: Path) -> list[Path]:
    pages = []
    for p in sorted(root.glob("*.html")):
        if p.name in SKIP_FILES:
            continue
        pages.append(p)
    return pages


def main() -> int:
    pages = discover_pages(SITE_ROOT)
    if not pages:
        print(f"No HTML pages found under {SITE_ROOT}")
        return 1

    print(f"[index] scanning {len(pages)} pages under {SITE_ROOT}")
    all_chunks: list[Chunk] = []
    for p in pages:
        slug = p.stem
        url = "/" + slug
        html = p.read_text(encoding="utf-8")
        chunks = list(extract_chunks_from_html(html, slug, url))
        all_chunks.extend(chunks)
        print(f"  • {p.name:<40s} → {len(chunks):3d} chunks")
    print(f"[index] total chunks: {len(all_chunks)}")

    if not all_chunks:
        print("Nothing to embed.")
        return 0

    # Decide which chunks need re-embedding.
    ledger = _load_ledger()
    to_embed: list[Chunk] = []
    fresh_ledger: dict[str, str] = {}
    for c in all_chunks:
        h = _chunk_hash(c)
        fresh_ledger[c.chunk_id] = h
        if ledger.get(c.chunk_id) != h:
            to_embed.append(c)

    # Find chunks that disappeared since last build → delete from Pinecone.
    deleted_ids = [cid for cid in ledger if cid not in fresh_ledger]

    print(f"[index] chunks to (re)embed: {len(to_embed)}")
    print(f"[index] chunks to delete:    {len(deleted_ids)}")

    if DRY_RUN:
        print("[index] DRY_RUN — not contacting Voyage or Pinecone.")
        _save_ledger(fresh_ledger)
        return 0

    if to_embed:
        embeds = voyage_embed([c.text for c in to_embed], input_type="document")
        index = _pinecone_index()
        # Pinecone v3 accepts up to 100 vectors per upsert; chunk it.
        BATCH = 100
        for i in range(0, len(to_embed), BATCH):
            batch_chunks = to_embed[i : i + BATCH]
            batch_vecs = embeds[i : i + BATCH]
            payload = []
            for c, v in zip(batch_chunks, batch_vecs):
                payload.append({
                    "id": c.chunk_id,
                    "values": v,
                    "metadata": {
                        "slug": c.slug,
                        "url": c.url,
                        "title_zh": c.title_zh,
                        "title_en": c.title_en,
                        "section": c.section,
                        "anchor": c.anchor,
                        "lang": c.lang,
                        "text": c.text,
                    },
                })
            index.upsert(vectors=payload)
            print(f"[index] upserted {i + len(batch_chunks)}/{len(to_embed)}")

    if deleted_ids:
        index = _pinecone_index()
        # Pinecone delete by ID, batched.
        for i in range(0, len(deleted_ids), 1000):
            index.delete(ids=deleted_ids[i : i + 1000])
        print(f"[index] deleted {len(deleted_ids)} stale vectors")

    _save_ledger(fresh_ledger)
    print(f"[index] done. ledger saved to {HASH_LEDGER}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
