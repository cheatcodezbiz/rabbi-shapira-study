"""Text-to-speech endpoint (Google Gemini Native TTS).

Why not Edge TTS:
    Microsoft IP-fingerprints free Read-Aloud and drops Vercel/AWS/GCP
    datacenters with an empty response. Gemini TTS works fine from any
    cloud and the existing GEMINI_API_KEY in this project already has
    access to it.

Contract — same JSON in, audio/wav out so the chat widget can swap us
in without touching its calling code:

    POST  /api/tts
    Body: { "text": "…", "voice": "Charon", "rate": "+0%" }
    200 : audio/wav  (24 kHz, mono, 16-bit PCM, framed in a WAV header)
    4xx : { "error": "...", "detail": "..." }

The `rate` parameter is accepted for backward compatibility but not yet
applied — Gemini's prebuilt voices don't currently expose a rate knob.

Env: GEMINI_API_KEY (already provisioned in Vercel for this project).
"""
from http.server import BaseHTTPRequestHandler
import base64
import json
import os
import struct

import requests


GEMINI_TTS_URL = (
    "https://generativelanguage.googleapis.com/v1beta/models/"
    "{model}:generateContent?key={key}"
)
GEMINI_MODEL = os.environ.get("GEMINI_TTS_MODEL", "gemini-2.5-flash-preview-tts")

# Hard ceiling on input size — keeps latency / cost bounded.
MAX_CHARS = 4000

# Valid Gemini prebuilt voice names (Sep 2025 vintage). The chat widget's
# default for both languages is "Charon" — a mature/informative male voice
# that handles both Mandarin and English well.
VALID_VOICES = {
    "Achernar", "Achird", "Algenib", "Algieba", "Alnilam", "Aoede",
    "Autonoe", "Callirrhoe", "Charon", "Despina", "Enceladus", "Erinome",
    "Fenrir", "Gacrux", "Iapetus", "Kore", "Laomedeia", "Leda",
    "Orus", "Puck", "Pulcherrima", "Rasalgethi", "Sadachbia", "Sadaltager",
    "Schedar", "Sulafat", "Umbriel", "Vindemiatrix", "Zephyr", "Zubenelgenubi",
}
DEFAULT_VOICE = "Charon"


# ─── WAV framing ────────────────────────────────────────────────────────────

def pcm16_to_wav(pcm: bytes, sample_rate: int = 24_000, channels: int = 1) -> bytes:
    """Wrap raw little-endian 16-bit PCM in a minimal WAV header so any
    HTMLAudioElement / ffmpeg / VLC can play it without a decoder."""
    bits_per_sample = 16
    block_align = channels * bits_per_sample // 8
    byte_rate = sample_rate * block_align
    data_size = len(pcm)
    riff_size = 4 + (8 + 16) + (8 + data_size)  # "WAVE" + fmt chunk + data chunk

    header = b"RIFF"
    header += struct.pack("<I", riff_size)
    header += b"WAVE"
    # fmt chunk
    header += b"fmt "
    header += struct.pack("<I", 16)        # PCM fmt chunk size
    header += struct.pack("<H", 1)         # AudioFormat = 1 (PCM)
    header += struct.pack("<H", channels)
    header += struct.pack("<I", sample_rate)
    header += struct.pack("<I", byte_rate)
    header += struct.pack("<H", block_align)
    header += struct.pack("<H", bits_per_sample)
    # data chunk
    header += b"data"
    header += struct.pack("<I", data_size)
    return header + pcm


# ─── Gemini call ───────────────────────────────────────────────────────────

def gemini_tts(text: str, voice: str) -> tuple[bytes, str]:
    """Return (audio_bytes, mime). audio_bytes is raw bytes as returned
    by Gemini; mime is what Gemini said it is (typically
    `audio/L16;codec=pcm;rate=24000`)."""
    key = os.environ.get("GEMINI_API_KEY")
    if not key:
        raise RuntimeError("GEMINI_API_KEY not configured")

    url = GEMINI_TTS_URL.format(model=GEMINI_MODEL, key=key)
    payload = {
        "contents": [{"parts": [{"text": text}]}],
        "generationConfig": {
            "responseModalities": ["AUDIO"],
            "speechConfig": {
                "voiceConfig": {
                    "prebuiltVoiceConfig": {"voiceName": voice},
                },
            },
        },
    }
    r = requests.post(url, json=payload, timeout=30)
    if r.status_code != 200:
        # Surface enough of Gemini's reply for the frontend to log.
        raise RuntimeError(f"gemini HTTP {r.status_code}: {r.text[:400]}")
    data = r.json()
    try:
        parts = data["candidates"][0]["content"]["parts"]
    except (KeyError, IndexError) as e:
        raise RuntimeError(f"gemini response malformed: {e}: {json.dumps(data)[:300]}")
    for p in parts:
        inline = p.get("inlineData") or p.get("inline_data")
        if inline and inline.get("data"):
            return base64.b64decode(inline["data"]), inline.get("mimeType", "audio/L16;rate=24000")
    raise RuntimeError("no inlineData in gemini response")


# ─── HTTP helpers ──────────────────────────────────────────────────────────

CORS = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "POST, OPTIONS, GET",
    "Access-Control-Allow-Headers": "Content-Type",
}


def _write(self, status: int, ctype: str, body: bytes, *, cache: str | None = None):
    self.send_response(status)
    self.send_header("Content-Type", ctype)
    self.send_header("Content-Length", str(len(body)))
    for k, v in CORS.items():
        self.send_header(k, v)
    if cache:
        self.send_header("Cache-Control", cache)
    self.end_headers()
    self.wfile.write(body)


def _json(self, status: int, obj: dict):
    _write(self, status, "application/json; charset=utf-8",
           json.dumps(obj).encode("utf-8"))


# ─── Handler ───────────────────────────────────────────────────────────────

class handler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(204)
        for k, v in CORS.items():
            self.send_header(k, v)
        self.end_headers()

    def do_GET(self):
        _json(self, 200, {
            "ok": True,
            "service": "tts",
            "provider": "gemini",
            "model": GEMINI_MODEL,
            "default_voice": DEFAULT_VOICE,
        })

    def do_POST(self):
        try:
            length = int(self.headers.get("content-length") or 0)
            body = json.loads(self.rfile.read(length) or b"{}")
        except Exception as e:
            return _json(self, 400, {"error": "invalid JSON", "detail": str(e)})

        text = (body.get("text") or "").strip()
        voice = (body.get("voice") or DEFAULT_VOICE).strip()
        # `rate` is accepted but ignored — kept for back-compat with the old
        # edge-tts.py contract.
        _rate = body.get("rate", "+0%")  # noqa: F841

        if not text:
            return _json(self, 400, {"error": "text required"})
        if len(text) > MAX_CHARS:
            return _json(self, 400,
                         {"error": f"text too long (max {MAX_CHARS})"})
        if voice not in VALID_VOICES:
            return _json(self, 400, {
                "error": "invalid voice",
                "detail": f"unknown voice '{voice}'; pick one of "
                          + ", ".join(sorted(VALID_VOICES)),
            })

        try:
            audio_bytes, mime = gemini_tts(text, voice)
        except Exception as e:
            print(f"[tts] synth failed: {e}", flush=True)
            return _json(self, 502, {"error": "tts failed", "detail": str(e)[:400]})

        # Gemini returns audio/L16 PCM at 24kHz mono 16-bit. Wrap in WAV
        # so the browser can play it directly via HTMLAudioElement.
        if "L16" in mime or "pcm" in mime.lower():
            wav = pcm16_to_wav(audio_bytes, sample_rate=24_000, channels=1)
            _write(self, 200, "audio/wav", wav,
                   cache="public, max-age=86400, immutable")
        else:
            # Whatever Gemini gave us, pass it through unchanged.
            _write(self, 200, mime, audio_bytes,
                   cache="public, max-age=86400, immutable")
