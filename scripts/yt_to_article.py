"""YouTube → article-source pipeline.

Downloads a YouTube video's audio + thumbnail + metadata, then sends the
audio to Google Gemini for Mandarin transcription, English translation,
and a structured theological analysis. Output goes into a per-video
folder under sources/<videoId>/ which the article author (human or LLM)
reads to compose the bilingual article.

Usage
-----
    python scripts/yt_to_article.py <youtube_url_or_id>
    python scripts/yt_to_article.py --channel @AhavatAmmiCHI --limit 12
    python scripts/yt_to_article.py --video-list videos.txt

What it produces (per video):
    sources/<videoId>/
        meta.json           — title, description, duration, thumbnail URL, …
        thumb.jpg           — original YouTube thumbnail (highest available)
        audio.m4a           — audio-only download (small)
        transcript.zh.txt   — Mandarin transcript (verbatim, Gemini)
        transcript.en.txt   — English translation
        analysis.md         — theological analysis: theme, references, voice
"""

from __future__ import annotations

import argparse
import asyncio
import json
import os
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

# Windows console defaults to cp1252 — printing Chinese titles crashes the
# script. Force stdout/stderr to UTF-8 so progress logging survives.
try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

REPO_ROOT  = Path(__file__).resolve().parent.parent
SOURCE_ROOT = REPO_ROOT / "sources"


def load_env() -> dict[str, str]:
    """Read .env so GEMINI_API_KEY is available without setting it manually."""
    env: dict[str, str] = {}
    p = REPO_ROOT / ".env"
    if p.exists():
        for line in p.read_text(encoding="utf-8-sig").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, _, v = line.partition("=")
            env[k.strip()] = v.strip()
    return env


def shell(cmd: list[str], cwd: Path | None = None, capture: bool = False) -> subprocess.CompletedProcess:
    print(f"$ {' '.join(cmd)}")
    return subprocess.run(cmd, cwd=str(cwd) if cwd else None, capture_output=capture, text=True, encoding="utf-8")


def normalize_video_url(url_or_id: str) -> str:
    if url_or_id.startswith("http"): return url_or_id
    if re.match(r"^[\w-]{11}$", url_or_id): return f"https://www.youtube.com/watch?v={url_or_id}"
    return url_or_id


def yt_metadata(url: str) -> dict:
    """Run yt-dlp -j to get the full info dict (no download)."""
    p = shell(
        [sys.executable, "-m", "yt_dlp", "--no-warnings", "--skip-download", "-j", url],
        capture=True,
    )
    if p.returncode != 0:
        raise RuntimeError(f"yt-dlp metadata failed: {p.stderr[:400]}")
    return json.loads(p.stdout)


def yt_download_audio_and_thumb(url: str, out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    # m4a is YouTube's native audio container — fast download, no transcoding.
    shell([
        sys.executable, "-m", "yt_dlp",
        "--no-warnings",
        "-f", "bestaudio[ext=m4a]/bestaudio",
        "-o", str(out_dir / "audio.%(ext)s"),
        "--write-thumbnail",
        "--convert-thumbnails", "jpg",
        url,
    ])
    # Normalize thumbnail filename
    for f in out_dir.glob("audio.jpg"):
        f.rename(out_dir / "thumb.jpg")
    for f in out_dir.glob("audio.webp"):
        f.rename(out_dir / "thumb.jpg")
    # Sometimes yt-dlp writes audio.m4a, sometimes audio.webm — leave whichever it picked.


def list_channel_videos(channel_handle: str, limit: int) -> list[str]:
    """Return the latest N video IDs from a channel handle (e.g. '@AhavatAmmiCHI')."""
    handle = channel_handle.strip()
    url = f"https://www.youtube.com/{handle}/videos" if handle.startswith("@") else handle
    p = shell([
        sys.executable, "-m", "yt_dlp",
        "--no-warnings", "--flat-playlist", "--playlist-end", str(limit), "-j", url,
    ], capture=True)
    if p.returncode != 0:
        raise RuntimeError(f"yt-dlp channel list failed: {p.stderr[:400]}")
    ids = []
    for line in p.stdout.splitlines():
        try:
            ids.append(json.loads(line)["id"])
        except Exception:
            continue
    return ids


# ── Gemini transcription / analysis ──────────────────────────────────────────

# Flash has ~30x the free-tier quota of Pro and handles Mandarin ASR well.
# Override with GEMINI_MODEL=gemini-2.5-pro for higher quality if you have paid quota.
GEMINI_MODEL_AUDIO = os.environ.get("GEMINI_MODEL_AUDIO", "gemini-2.5-flash")
GEMINI_MODEL_TEXT  = os.environ.get("GEMINI_MODEL_TEXT",  "gemini-2.5-flash")


def gemini_upload_file(api_key: str, path: Path) -> dict:
    """Upload via the Files API, return the file resource (with .uri)."""
    import urllib.request, urllib.parse, mimetypes
    mime = mimetypes.guess_type(str(path))[0] or "audio/mp4"
    size = path.stat().st_size

    # Step 1: start a resumable upload session
    init_url = f"https://generativelanguage.googleapis.com/upload/v1beta/files?key={urllib.parse.quote(api_key)}"
    init_body = json.dumps({"file": {"display_name": path.name}}).encode("utf-8")
    req = urllib.request.Request(init_url, data=init_body, method="POST", headers={
        "X-Goog-Upload-Protocol": "resumable",
        "X-Goog-Upload-Command": "start",
        "X-Goog-Upload-Header-Content-Length": str(size),
        "X-Goog-Upload-Header-Content-Type": mime,
        "Content-Type": "application/json",
    })
    with urllib.request.urlopen(req, timeout=60) as r:
        upload_url = r.headers["X-Goog-Upload-URL"]

    # Step 2: upload the bytes + finalize
    with open(path, "rb") as f:
        body = f.read()
    req = urllib.request.Request(upload_url, data=body, method="POST", headers={
        "Content-Length": str(size),
        "X-Goog-Upload-Offset": "0",
        "X-Goog-Upload-Command": "upload, finalize",
    })
    with urllib.request.urlopen(req, timeout=600) as r:
        result = json.loads(r.read().decode("utf-8"))
    return result["file"]


def gemini_wait_active(api_key: str, file_resource: dict, max_wait_sec: int = 180) -> dict:
    """Poll until file state == ACTIVE (audio takes a few seconds to process)."""
    import urllib.request, urllib.parse
    name = file_resource["name"]
    deadline = time.time() + max_wait_sec
    while time.time() < deadline:
        url = f"https://generativelanguage.googleapis.com/v1beta/{name}?key={urllib.parse.quote(api_key)}"
        with urllib.request.urlopen(url, timeout=30) as r:
            data = json.loads(r.read().decode("utf-8"))
        state = data.get("state")
        if state == "ACTIVE": return data
        if state == "FAILED": raise RuntimeError(f"Gemini file processing failed: {data}")
        time.sleep(2)
    raise TimeoutError(f"Gemini file did not become ACTIVE within {max_wait_sec}s")


def gemini_generate(api_key: str, model: str, contents: list, max_retries: int = 6) -> str:
    """Single-shot generateContent call. Returns first text part.

    Retries 6 times with progressive backoff. Critically, 429 / quota errors
    get a much longer sleep (60–300s) since Gemini's per-minute window only
    clears after roughly that long, and the API returns 429 with a
    `retryDelay` hint that we honor when present.
    """
    import urllib.request, urllib.parse
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={urllib.parse.quote(api_key)}"
    body = json.dumps({
        "contents": [{"role": "user", "parts": contents}],
        "generationConfig": {"temperature": 0.2, "maxOutputTokens": 32000},
    }).encode("utf-8")
    last_err = None
    for attempt in range(max_retries + 1):
        try:
            req = urllib.request.Request(url, data=body, method="POST", headers={"Content-Type": "application/json"})
            with urllib.request.urlopen(req, timeout=600) as r:
                d = json.loads(r.read().decode("utf-8"))
            parts = d.get("candidates", [{}])[0].get("content", {}).get("parts", [])
            for p in parts:
                if "text" in p: return p["text"]
            raise RuntimeError(f"no text in Gemini response: {json.dumps(d)[:400]}")
        except urllib.error.HTTPError as e:
            last_err = e
            if attempt >= max_retries:
                raise
            # Try to read the response body for a retryDelay hint.
            wait = 60 if e.code == 429 else 4
            try:
                err_body = e.read().decode("utf-8", errors="replace")
                m = re.search(r'"retryDelay"\s*:\s*"(\d+)s?"', err_body)
                if m:
                    wait = max(int(m.group(1)) + 5, wait)
                # If Gemini explicitly mentions per-minute quota, sleep through it
                if "GenerateRequestsPerMinute" in err_body or "PerMinute" in err_body:
                    wait = max(wait, 65)
            except Exception:
                pass
            # Progressive bump on repeated 429s — Gemini's daily quota errors
            # need much longer waits, so escalate.
            if e.code == 429:
                wait = max(wait, 30 * (attempt + 1))
            print(f"     gemini {e.code} (attempt {attempt + 1}/{max_retries + 1}); sleep {wait}s", file=sys.stderr)
            time.sleep(wait)
            continue
        except Exception as e:
            last_err = e
            if attempt >= max_retries:
                raise
            time.sleep(4 + 2 * attempt)
            continue
    raise last_err  # pragma: no cover


# ── Per-video pipeline ───────────────────────────────────────────────────────

def process_video(video_id: str, env: dict[str, str], skip_download: bool = False) -> Path:
    """Download + transcribe + analyse a single video. Returns the source dir."""
    url = normalize_video_url(video_id)
    out = SOURCE_ROOT / video_id
    out.mkdir(parents=True, exist_ok=True)

    # 1. Metadata + thumbnail + audio
    if not (out / "meta.json").exists() or not skip_download:
        meta_full = yt_metadata(url)
        meta = {k: meta_full.get(k) for k in (
            "id", "title", "description", "duration", "upload_date",
            "uploader", "channel", "channel_url", "webpage_url", "thumbnail",
        )}
        (out / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    else:
        meta = json.loads((out / "meta.json").read_text(encoding="utf-8"))
    print(f"  title: {meta.get('title','')[:80]}")

    audio = next(out.glob("audio.*"), None)
    if not audio:
        yt_download_audio_and_thumb(url, out)
        audio = next(out.glob("audio.*"), None)
    if not audio:
        raise RuntimeError("yt-dlp produced no audio file")
    print(f"  audio: {audio.name} ({audio.stat().st_size // 1024} KB)")

    # 2. Gemini upload + transcription
    if not (out / "transcript.zh.txt").exists():
        api_key = env.get("GEMINI_API_KEY") or os.environ.get("GEMINI_API_KEY")
        if not api_key:
            raise RuntimeError("GEMINI_API_KEY not set in .env or environment")
        print("  uploading audio to Gemini Files API…")
        f = gemini_upload_file(api_key, audio)
        print("  waiting for ACTIVE…")
        f = gemini_wait_active(api_key, f)
        file_uri = f["uri"]
        mime = f.get("mimeType", "audio/mp4")

        print(f"  transcribing with {GEMINI_MODEL_AUDIO}…")
        transcribe_prompt = (
            "請將這段普通話/中文音頻完整轉錄成繁體中文文字。\n"
            "規則：\n"
            "1. 逐字轉錄，不要總結。\n"
            "2. 使用繁體中文（台灣標準）。\n"
            "3. 保留說話人原本的句子結構。\n"
            "4. 引用聖經、塔木德或希伯來文時，盡量保留原文用字。\n"
            "5. 自然分段，每個論點或段落換一段。\n"
            "只輸出轉錄文字，不要加任何前言或後記。"
        )
        zh = gemini_generate(api_key, GEMINI_MODEL_AUDIO, [
            {"file_data": {"file_uri": file_uri, "mime_type": mime}},
            {"text": transcribe_prompt},
        ])
        (out / "transcript.zh.txt").write_text(zh.strip() + "\n", encoding="utf-8")
        print(f"  zh transcript: {len(zh)} chars")

    # 3. English translation
    if not (out / "transcript.en.txt").exists():
        api_key = env.get("GEMINI_API_KEY") or os.environ.get("GEMINI_API_KEY")
        zh = (out / "transcript.zh.txt").read_text(encoding="utf-8")
        print("  translating to English…")
        en = gemini_generate(api_key, GEMINI_MODEL_TEXT, [
            {"text":
                "Translate the following Mandarin transcript of a Messianic Jewish "
                "rabbi's teaching into clear, theologically-precise English. Preserve "
                "all biblical / Talmudic / Hebrew references verbatim (transliterate "
                "Hebrew where the original gives it). Match the rabbi's tone — "
                "scholarly but accessible. Return only the translation.\n\n"
                "Transcript:\n\n" + zh
            },
        ])
        (out / "transcript.en.txt").write_text(en.strip() + "\n", encoding="utf-8")
        print(f"  en translation: {len(en)} chars")

    # 4. Theological analysis (helps the article author)
    if not (out / "analysis.md").exists():
        api_key = env.get("GEMINI_API_KEY") or os.environ.get("GEMINI_API_KEY")
        zh = (out / "transcript.zh.txt").read_text(encoding="utf-8")
        en = (out / "transcript.en.txt").read_text(encoding="utf-8")
        print("  generating theological analysis…")
        analysis = gemini_generate(api_key, GEMINI_MODEL_TEXT, [
            {"text":
                "You are an expert in Jewish-Christian theology, Talmudic exegesis "
                "and Messianic Jewish thought. The text below is a transcript of "
                "Rabbi Dr. Itzhak Shapira (Ahavat Ammi Ministries) teaching in "
                "Mandarin (with English translation). Produce a rigorous structured "
                "analysis that an article author can use to write a long-form "
                "bilingual study piece for Chinese Christians.\n\n"
                "Sections to produce (in English, markdown):\n\n"
                "1. **Title** — 1 evocative bilingual title (zh-TW / English).\n"
                "2. **One-sentence thesis** — what is Rabbi Shapira actually claiming?\n"
                "3. **Argument map** — numbered, the rabbi's logical chain step by step.\n"
                "4. **All scriptural references** — verse / Talmud tractate, with the "
                "Hebrew or Aramaic terms he highlights and what they mean.\n"
                "5. **Key Hebrew terms** — terms with transliteration + gloss + why they matter.\n"
                "6. **Key gematria / numerical claims** — if any.\n"
                "7. **Strongest 3 verbatim quotes** for use as blockquotes (zh original + en translation).\n"
                "8. **What this means for Christians who love Israel** — the take-home, ~3 paragraphs.\n"
                "9. **A word on discernment** — note any claims that are *drash* (homiletical) "
                "rather than literal so the article can be intellectually honest.\n"
                "10. **Closing call** — Rabbi Shapira's final exhortation, exactly as he gave it (zh + en).\n\n"
                "Mandarin transcript:\n\n" + zh + "\n\n"
                "English translation:\n\n" + en
            },
        ])
        (out / "analysis.md").write_text(analysis.strip() + "\n", encoding="utf-8")
        print(f"  analysis: {len(analysis)} chars")

    print(f"  ✓ done → {out.relative_to(REPO_ROOT)}\n")
    return out


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("inputs", nargs="*", help="YouTube URLs or 11-char video IDs")
    p.add_argument("--channel", help="@handle to enumerate latest videos from")
    p.add_argument("--limit", type=int, default=12, help="number of videos when using --channel")
    p.add_argument("--video-list", help="text file with one URL/ID per line")
    args = p.parse_args()

    env = load_env()
    if not env.get("GEMINI_API_KEY"):
        env["GEMINI_API_KEY"] = os.environ.get("GEMINI_API_KEY", "")

    targets: list[str] = list(args.inputs)
    if args.channel:
        print(f"== listing latest {args.limit} videos from {args.channel}")
        targets += list_channel_videos(args.channel, args.limit)
    if args.video_list:
        targets += [line.strip() for line in Path(args.video_list).read_text(encoding="utf-8").splitlines() if line.strip()]

    if not targets:
        print("no videos given. pass URLs/IDs, or --channel @handle.", file=sys.stderr)
        sys.exit(1)

    for i, t in enumerate(targets):
        vid = t
        if t.startswith("http"):
            m = re.search(r"(?:v=|/shorts/|youtu\.be/)([\w-]{11})", t)
            if m: vid = m.group(1)
        print(f"\n[{i+1}/{len(targets)}] {vid}")
        try:
            process_video(vid, env)
        except Exception as e:
            print(f"  ✗ failed: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
