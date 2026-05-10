"""Vercel Python serverless function: live Microsoft Edge TTS synthesis.

Used when the user picks a voice that isn't pre-rendered. Takes a JSON
body { text, voice, rate? } and streams back an MP3 from Edge's free
Read-Aloud Neural voices via the edge-tts library.

The pre-rendered static MP3s in /assets/audio cover the *default* voice
for each article (HsiaoChen / Aria) — no proxy round-trip there. This
endpoint is only hit when someone changes voice in the settings panel.
"""
from http.server import BaseHTTPRequestHandler
import asyncio
import json

import edge_tts


# Hard ceilings to keep latency / cost bounded.
MAX_CHARS = 4000
ALLOWED_RATE = lambda s: bool(__import__('re').match(r'^[+-]?\d{1,3}%$', s or ''))


async def synthesize(text: str, voice: str, rate: str) -> bytes:
    com = edge_tts.Communicate(text, voice, rate=rate)
    chunks = []
    async for chunk in com.stream():
        if chunk['type'] == 'audio':
            chunks.append(chunk['data'])
    return b''.join(chunks)


def _send(self, status: int, ctype: str, body: bytes, *, cache: str | None = None) -> None:
    self.send_response(status)
    self.send_header('Content-Type', ctype)
    self.send_header('Content-Length', str(len(body)))
    if cache:
        self.send_header('Cache-Control', cache)
    self.send_header('Access-Control-Allow-Origin', '*')
    self.end_headers()
    self.wfile.write(body)


def _json(self, status: int, obj: dict) -> None:
    _send(self, status, 'application/json', json.dumps(obj).encode('utf-8'))


class handler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_GET(self):
        # Lightweight liveness probe for the frontend (used by the picker).
        _json(self, 200, {'ok': True, 'service': 'edge-tts'})

    def do_POST(self):
        try:
            length = int(self.headers.get('content-length', 0))
            body = json.loads(self.rfile.read(length) or b'{}')
        except Exception as e:
            return _json(self, 400, {'error': f'invalid JSON: {e}'})

        text = (body.get('text') or '').strip()
        voice = (body.get('voice') or '').strip()
        rate = (body.get('rate') or '+0%').strip()

        if not text:
            return _json(self, 400, {'error': '`text` required'})
        if len(text) > MAX_CHARS:
            return _json(self, 400, {'error': f'text too long (max {MAX_CHARS})'})
        if not voice or '-' not in voice:
            return _json(self, 400, {'error': '`voice` required (e.g. zh-TW-HsiaoChenNeural)'})
        if not ALLOWED_RATE(rate):
            return _json(self, 400, {'error': 'rate must look like "+25%" or "-10%"'})

        try:
            audio = asyncio.run(synthesize(text, voice, rate))
        except Exception as e:
            print(f'[edge-tts] synth failed: {e}', flush=True)
            return _json(self, 502, {'error': 'edge-tts failed', 'detail': str(e)[:200]})

        if not audio:
            return _json(self, 502, {'error': 'empty audio from edge-tts'})

        # Same (text, voice, rate) → identical bytes. Cache aggressively.
        _send(self, 200, 'audio/mpeg', audio,
              cache='public, max-age=86400, immutable')
