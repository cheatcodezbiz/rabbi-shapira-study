"""Multi-speaker YouTube event → per-speaker bilingual articles.

Downloads a long conference video, transcribes the full audio with
faster-whisper (GPU, no rate limits), asks Ollama to identify speaker
transitions and segment the transcript, then for each speaker:
  - extracts a frame thumbnail from the video
  - generates bilingual Chinese/English content via Ollama
  - writes a build script for build_article.py

Usage
-----
    python scripts/yt_to_multispeaker.py OlTpoHwveIM
    python scripts/yt_to_multispeaker.py https://www.youtube.com/watch?v=OlTpoHwveIM

Output structure
----------------
    sources/<videoId>/
        meta.json
        thumb.jpg
        audio.m4a          (or .webm)
        video.mp4          (moderate quality, for frame extraction)
        transcript.raw.txt (full faster-whisper output with timestamps)
        speakers.json      (Ollama-identified speaker segments)
        speakers/
            01_<name>/
                transcript.zh.txt
                transcript.en.txt
                analysis.md
                frame.jpg      (video frame at speaker midpoint)
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import time
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

WHISPER_MODEL   = os.environ.get("WHISPER_MODEL", "large-v3")
WHISPER_DEVICE  = os.environ.get("WHISPER_DEVICE", "cuda")
WHISPER_COMPUTE = os.environ.get("WHISPER_COMPUTE", "float16")

# Minimum speaker segment duration (seconds). Shorter segments are merged
# into the previous speaker or dropped.
MIN_SEGMENT_SEC = 120


def shell(cmd: list[str], cwd: Path | None = None, capture: bool = False) -> subprocess.CompletedProcess:
    print(f"$ {' '.join(str(c) for c in cmd)}")
    return subprocess.run(cmd, cwd=str(cwd) if cwd else None, capture_output=capture, text=True, encoding="utf-8")


def normalize_video_url(url_or_id: str) -> str:
    if url_or_id.startswith("http"): return url_or_id
    if re.match(r"^[\w-]{11}$", url_or_id): return f"https://www.youtube.com/watch?v={url_or_id}"
    return url_or_id


def yt_metadata(url: str) -> dict:
    r = shell([sys.executable, "-m", "yt_dlp", "--no-warnings", "--skip-download", "-j", url], capture=True)
    if r.returncode != 0:
        raise RuntimeError(f"yt-dlp metadata failed: {r.stderr[:400]}")
    return json.loads(r.stdout)


def yt_download_video(url: str, out_dir: Path) -> Path:
    """Download video at 720p (for frame extraction). Returns path to video file."""
    out_dir.mkdir(parents=True, exist_ok=True)
    video_path = out_dir / "video.mp4"
    if video_path.exists():
        print(f"  video already downloaded: {video_path.name}")
        return video_path

    print("  downloading video (720p for frame extraction)…")
    shell([
        sys.executable, "-m", "yt_dlp",
        "--no-warnings",
        "-f", "bestvideo[height<=720][ext=mp4]+bestaudio[ext=m4a]/best[height<=720][ext=mp4]/best[height<=720]",
        "--merge-output-format", "mp4",
        "-o", str(video_path),
        url,
    ])
    if not video_path.exists():
        # fallback: any mp4
        for f in out_dir.glob("video.*"):
            return f
        raise RuntimeError("yt-dlp produced no video file")
    return video_path


def yt_download_audio(url: str, out_dir: Path) -> Path:
    """Download audio-only m4a. Returns path."""
    out_dir.mkdir(parents=True, exist_ok=True)
    existing = next(out_dir.glob("audio.*"), None)
    if existing:
        print(f"  audio already downloaded: {existing.name}")
        return existing

    print("  downloading audio…")
    shell([
        sys.executable, "-m", "yt_dlp",
        "--no-warnings",
        "-f", "bestaudio[ext=m4a]/bestaudio",
        "-o", str(out_dir / "audio.%(ext)s"),
        "--write-thumbnail", "--convert-thumbnails", "jpg",
        url,
    ])
    for f in out_dir.glob("audio.jpg"): f.rename(out_dir / "thumb.jpg")
    for f in out_dir.glob("audio.webp"): f.rename(out_dir / "thumb.jpg")
    audio = next(out_dir.glob("audio.*"), None)
    if not audio:
        raise RuntimeError("no audio file after download")
    return audio


# ── faster-whisper ────────────────────────────────────────────────────────────

_whisper_cache = None

def get_whisper():
    global _whisper_cache
    if _whisper_cache is None:
        from faster_whisper import WhisperModel
        import ctranslate2
        device, compute = WHISPER_DEVICE, WHISPER_COMPUTE
        try:
            if ctranslate2.get_cuda_device_count() == 0:
                device, compute = "cpu", "int8"
        except Exception:
            device, compute = "cpu", "int8"
        print(f"  [whisper] loading {WHISPER_MODEL} on {device}/{compute}…")
        _whisper_cache = WhisperModel(WHISPER_MODEL, device=device, compute_type=compute)
    return _whisper_cache


def transcribe_full(audio_path: Path, transcript_path: Path) -> list[dict]:
    """Transcribe audio → list of segments with timestamps.

    Each segment: {"start": float, "end": float, "text": str}
    Saved to transcript_path as JSON (for resuming).
    Also writes a human-readable .txt version.
    """
    if transcript_path.exists():
        print(f"  [whisper] loading cached transcript {transcript_path.name}")
        return json.loads(transcript_path.read_text(encoding="utf-8"))

    model = get_whisper()
    print(f"  [whisper] transcribing {audio_path.name} (this may take 30-60 min)…")
    t0 = time.time()

    raw_segments, info = model.transcribe(
        str(audio_path),
        beam_size=5,
        vad_filter=True,
        # Don't force language — the event has English, Mandarin, Spanish
        # Let whisper auto-detect per-segment
    )

    segments: list[dict] = []
    for seg in raw_segments:
        segments.append({"start": seg.start, "end": seg.end, "text": seg.text.strip()})
        # Print progress every ~15 minutes of audio
        if seg.end % 900 < 5:
            elapsed = time.time() - t0
            print(f"    …{seg.end/3600:.1f}h transcribed in {elapsed/60:.0f}m")

    elapsed = time.time() - t0
    print(f"  [whisper] done: {len(segments)} segments in {elapsed/60:.1f} min")

    transcript_path.write_text(json.dumps(segments, ensure_ascii=False, indent=2), encoding="utf-8")

    # Human-readable version
    txt_path = transcript_path.with_suffix(".txt")
    lines = []
    for s in segments:
        ts = f"[{s['start']/3600:.0f}:{(s['start']%3600)/60:02.0f}:{s['start']%60:02.0f}]"
        lines.append(f"{ts} {s['text']}")
    txt_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"  wrote {txt_path.name}")

    return segments


# ── Ollama helpers ────────────────────────────────────────────────────────────

def ollama_generate(prompt: str, timeout: int = 900) -> str:
    import urllib.request
    url = f"{OLLAMA_HOST}/api/generate"
    body = json.dumps({
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False,
        "options": {"temperature": 0.2, "num_predict": 8192},
    }).encode("utf-8")
    req = urllib.request.Request(url, data=body, method="POST",
                                  headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8")).get("response", "").strip()


def identify_speakers(segments: list[dict], out_path: Path) -> list[dict]:
    """Ask Ollama to identify speaker transitions in the transcript.

    Returns list of dicts:
    [
      {"speaker": "Rabbi Shapira", "start": 0.0, "end": 1234.5,
       "topic": "Opening blessing and introduction",
       "language": "en"},
      ...
    ]
    """
    if out_path.exists():
        print("  [ollama] loading cached speaker segments")
        return json.loads(out_path.read_text(encoding="utf-8"))

    # Build a condensed transcript (first 200 chars per minute) for context
    print("  [ollama] building condensed transcript for speaker ID…")
    condensed_lines: list[str] = []
    last_min = -1
    for seg in segments:
        minute = int(seg["start"] / 60)
        if minute > last_min:
            ts = f"[{seg['start']/3600:.0f}h{(seg['start']%3600)/60:02.0f}m]"
            condensed_lines.append(f"{ts} {seg['text'][:200]}")
            last_min = minute

    condensed = "\n".join(condensed_lines)

    print("  [ollama] identifying speakers (may take 5-10 min)…")
    prompt = f"""You are analyzing a transcript of a multi-speaker Messianic Jewish conference event called "The Night of the Bride 5786" (Milchemet HaChatunah - The War for the Wedding).

The event features multiple speakers including Rabbi Dr. Itzhak Shapira and others. Below is a condensed transcript with timestamps (one line per minute of audio).

Your task: Identify all distinct speaker segments. For each speaker:
1. Name (or describe if unknown, e.g. "Female Vocalist", "Male Speaker 2")
2. Start time (in seconds from the transcript timestamps)
3. End time
4. Main topic/content (1-2 sentences)
5. Language spoken (en/zh/es/he/other)

Output ONLY a valid JSON array. No markdown. No explanation. Format:
[
  {{"speaker": "Rabbi Itzhak Shapira", "start": 0, "end": 3600, "topic": "Opening blessing and priestly benediction", "language": "en"}},
  {{"speaker": "Name or description", "start": 3600, "end": 7200, "topic": "Topic summary", "language": "en"}}
]

Condensed transcript:
{condensed}
"""
    response = ollama_generate(prompt, timeout=900)

    # Extract JSON from response
    json_match = re.search(r'\[[\s\S]+\]', response)
    if not json_match:
        print(f"  [warn] Ollama did not return valid JSON; raw:\n{response[:500]}")
        # Create a single fallback segment
        total = segments[-1]["end"] if segments else 0
        speaker_data = [{"speaker": "Full Event", "start": 0, "end": total,
                          "topic": "Complete Night of the Bride event", "language": "en"}]
    else:
        try:
            speaker_data = json.loads(json_match.group())
        except json.JSONDecodeError as e:
            print(f"  [warn] JSON parse error: {e}; using fallback")
            total = segments[-1]["end"] if segments else 0
            speaker_data = [{"speaker": "Full Event", "start": 0, "end": total,
                              "topic": "Complete Night of the Bride event", "language": "en"}]

    # Filter out segments shorter than MIN_SEGMENT_SEC
    filtered = [s for s in speaker_data if s["end"] - s["start"] >= MIN_SEGMENT_SEC]
    print(f"  [ollama] identified {len(filtered)} speaker segments (from {len(speaker_data)})")

    out_path.write_text(json.dumps(filtered, ensure_ascii=False, indent=2), encoding="utf-8")
    return filtered


def extract_frame(video_path: Path, timestamp_sec: float, out_path: Path) -> None:
    """Extract a single frame from video at timestamp_sec using ffmpeg."""
    if out_path.exists():
        return
    out_path.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run([
        "ffmpeg", "-ss", str(timestamp_sec),
        "-i", str(video_path),
        "-vframes", "1",
        "-q:v", "2",   # high quality JPEG
        "-vf", "scale=1280:720:force_original_aspect_ratio=decrease",
        str(out_path), "-y",
    ], capture_output=True)
    if out_path.exists():
        print(f"  frame extracted: {out_path.name}")
    else:
        print(f"  [warn] frame extraction failed at {timestamp_sec:.0f}s")


def get_speaker_transcript(segments: list[dict], start: float, end: float) -> str:
    """Extract and join transcript segments within a speaker's time range."""
    lines = [s["text"] for s in segments if s["start"] >= start and s["end"] <= end + 5]
    return " ".join(lines).strip()


def ollama_process_speaker(raw_text: str, speaker: dict, event_title: str) -> tuple[str, str, str]:
    """Generate zh transcript, en translation, and analysis for one speaker."""
    lang = speaker.get("language", "en")
    name = speaker.get("speaker", "Speaker")
    topic = speaker.get("topic", "")

    print(f"  [ollama] processing {name}…")

    # Step 1: clean up / translate to Chinese
    if lang in ("zh", "zh-TW", "zh-CN"):
        zh_prompt = (
            f"以下是「{event_title}」活動中 {name} 的演講轉錄。\n"
            "請轉換為流暢的繁體中文（台灣標準），修正語音辨識錯誤，保留所有聖經引用和希伯來文詞彙。\n"
            "只輸出轉換後的繁體中文全文。\n\n"
            f"原文：\n{raw_text}"
        )
    else:
        zh_prompt = (
            f"以下是「{event_title}」活動中 {name} 的演講轉錄（英文/西班牙文）。\n"
            "請將全文翻譯成流暢的繁體中文（台灣標準），保留所有聖經引用和希伯來文詞彙。\n"
            "只輸出繁體中文翻譯全文。\n\n"
            f"原文：\n{raw_text[:8000]}"  # limit input size
        )
    zh = ollama_generate(zh_prompt)

    # Step 2: English translation (if not already English)
    if lang in ("en",):
        en = raw_text[:8000]  # already English
    else:
        en_prompt = (
            f"Translate the following transcript by {name} from '{event_title}' into "
            "clear, natural English. Preserve all biblical references and Hebrew terms.\n\n"
            f"Transcript:\n{raw_text[:8000]}"
        )
        en = ollama_generate(en_prompt)

    # Step 3: theological analysis
    analysis_prompt = (
        f"You are analyzing a teaching by {name} at the '{event_title}' Messianic Jewish conference.\n"
        f"Topic: {topic}\n\n"
        "Produce a structured analysis for a bilingual Chinese-English study article:\n\n"
        "1. **Bilingual Title** — evocative zh-TW / English title for this segment\n"
        "2. **One-sentence thesis** — what is the speaker claiming?\n"
        "3. **Key points** — numbered list of main arguments\n"
        "4. **Scriptural references** — verses cited, with Hebrew/Aramaic terms\n"
        "5. **Key Hebrew terms** — transliteration + gloss\n"
        "6. **Best quote** — strongest verbatim quote (original + zh translation)\n"
        "7. **Application** — what this means for Chinese believers\n"
        "8. **Closing** — how this teaching ends / the call to action\n\n"
        f"English transcript:\n{en[:6000]}"
    )
    analysis = ollama_generate(analysis_prompt)

    return zh, en, analysis


def slugify_speaker(name: str, idx: int) -> str:
    """Create a URL-safe slug for a speaker segment."""
    clean = re.sub(r'[^a-zA-Z0-9\s]', '', name.lower())
    clean = re.sub(r'\s+', '-', clean.strip())[:30]
    return f"{idx:02d}-{clean}"


def process_video(video_id: str, download_video: bool = True) -> Path:
    url = normalize_video_url(video_id)
    out = SOURCE_ROOT / video_id
    out.mkdir(parents=True, exist_ok=True)

    # 1. Metadata
    meta_path = out / "meta.json"
    if not meta_path.exists():
        meta_full = yt_metadata(url)
        meta = {k: meta_full.get(k) for k in (
            "id", "title", "description", "duration", "upload_date",
            "uploader", "channel", "channel_url", "webpage_url", "thumbnail",
        )}
        meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    else:
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
    title = meta.get("title", video_id)
    print(f"  title: {title[:80]}")
    print(f"  duration: {meta.get('duration', 0) // 3600}h {(meta.get('duration', 0) % 3600) // 60}m")

    # 2. Download audio (always needed) + video (for frames)
    audio = yt_download_audio(url, out)
    video_path = None
    if download_video:
        video_path = yt_download_video(url, out)

    # 3. Full transcription
    transcript_json = out / "transcript.raw.json"
    segments = transcribe_full(audio, transcript_json)

    # 4. Speaker identification
    speakers_path = out / "speakers.json"
    speakers = identify_speakers(segments, speakers_path)
    print(f"\n  Speaker breakdown:")
    for i, sp in enumerate(speakers):
        dur = sp["end"] - sp["start"]
        print(f"    {i+1:2}. {sp['speaker'][:40]:<40} {dur/60:.0f}m  {sp.get('language','?')}  {sp['topic'][:60]}")

    # 5. Per-speaker processing
    spk_dir = out / "speakers"
    spk_dir.mkdir(exist_ok=True)

    results: list[dict] = []
    for i, sp in enumerate(speakers):
        slug = slugify_speaker(sp["speaker"], i + 1)
        sp_out = spk_dir / slug
        sp_out.mkdir(exist_ok=True)

        print(f"\n  [{i+1}/{len(speakers)}] {sp['speaker']} ({slug})")

        # Extract transcript for this speaker
        raw = get_speaker_transcript(segments, sp["start"], sp["end"])
        if not raw:
            print("    [skip] empty transcript")
            continue

        # Save raw transcript
        (sp_out / "transcript.raw.txt").write_text(raw, encoding="utf-8")

        # Extract frame thumbnail (midpoint of segment)
        frame_path = sp_out / "frame.jpg"
        if video_path and video_path.exists():
            mid = (sp["start"] + sp["end"]) / 2
            extract_frame(video_path, mid, frame_path)
        else:
            # Fall back to copying the video thumbnail
            thumb = out / "thumb.jpg"
            if thumb.exists() and not frame_path.exists():
                import shutil
                shutil.copy(thumb, frame_path)

        # Generate bilingual content
        zh_path = sp_out / "transcript.zh.txt"
        en_path = sp_out / "transcript.en.txt"
        analysis_path = sp_out / "analysis.md"

        if not (zh_path.exists() and en_path.exists() and analysis_path.exists()):
            zh, en, analysis = ollama_process_speaker(raw, sp, title)
            zh_path.write_text(zh + "\n", encoding="utf-8")
            en_path.write_text(en + "\n", encoding="utf-8")
            analysis_path.write_text(analysis + "\n", encoding="utf-8")
        else:
            print("    [cached] transcripts and analysis already exist")

        results.append({
            **sp,
            "slug": slug,
            "frame": str(frame_path.relative_to(REPO_ROOT)) if frame_path.exists() else None,
        })

    # Save final summary
    summary_path = out / "speakers_processed.json"
    summary_path.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n  ✓ processed {len(results)} speakers → {summary_path.relative_to(REPO_ROOT)}")
    return out


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("inputs", nargs="+", help="YouTube URLs or 11-char video IDs")
    p.add_argument("--no-video", action="store_true", help="skip video download (no frame extraction)")
    p.add_argument("--whisper-model", default=None)
    p.add_argument("--ollama-model", default=None)
    args = p.parse_args()

    global WHISPER_MODEL, OLLAMA_MODEL
    if args.whisper_model: WHISPER_MODEL = args.whisper_model
    if args.ollama_model: OLLAMA_MODEL = args.ollama_model

    print(f"== multi-speaker pipeline: whisper/{WHISPER_MODEL} + ollama/{OLLAMA_MODEL}")

    for t in args.inputs:
        vid = t
        if t.startswith("http"):
            m = re.search(r"(?:v=|/shorts/|youtu\.be/)([\w-]{11})", t)
            if m: vid = m.group(1)
        print(f"\n[video] {vid}")
        try:
            process_video(vid, download_video=not args.no_video)
        except Exception as e:
            import traceback
            print(f"  ✗ failed: {e}", file=sys.stderr)
            traceback.print_exc()


if __name__ == "__main__":
    main()
