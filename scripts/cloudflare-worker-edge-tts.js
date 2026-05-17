/**
 * Cloudflare Worker: Microsoft Edge Read-Aloud TTS proxy.
 *
 * Why this exists:
 *   Microsoft IP-fingerprints the free Read Aloud WebSocket and drops
 *   connections from Vercel / AWS / GCP datacenter ranges, returning
 *   "No audio was received". Cloudflare Workers run on a Cloudflare IP
 *   space that Microsoft still trusts, so we proxy through here and get
 *   pristine MP3s of voices like zh-TW-YunJheNeural for free.
 *
 * Endpoint contract (same as our old /api/edge-tts.py):
 *   POST  /
 *   Body:  { "text": "…", "voice": "zh-TW-YunJheNeural", "rate": "+0%" }
 *   200:   audio/mpeg  (the synthesised MP3)
 *   4xx/5xx: { "error": "...", "detail": "..." } as JSON
 *
 * CORS is wide-open by design — only the rabbi-shapira-study site calls it.
 *
 * Deploy: paste this file into dash.cloudflare.com → Workers → Create →
 * Hello World → replace the default code → Deploy.
 */

const TRUSTED_CLIENT_TOKEN = '6A5AA1D4EAFF4E9FB37E23D68491D6F4';
const WSS_HOST = 'speech.platform.bing.com';
const WSS_PATH = `/consumer/speech/synthesize/readaloud/edge/v1?TrustedClientToken=${TRUSTED_CLIENT_TOKEN}`;

const MAX_CHARS = 4000;
const TIMEOUT_MS = 25000;

const CORS = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Methods': 'POST, OPTIONS, GET',
  'Access-Control-Allow-Headers': 'Content-Type',
  'Access-Control-Max-Age': '86400',
};

export default {
  async fetch(request) {
    if (request.method === 'OPTIONS') {
      return new Response(null, { status: 204, headers: CORS });
    }
    if (request.method === 'GET') {
      return jsonResp({ ok: true, service: 'edge-tts-worker', voice_default: 'zh-TW-YunJheNeural' }, 200);
    }
    if (request.method !== 'POST') {
      return jsonResp({ error: 'POST required' }, 405);
    }

    let body;
    try {
      body = await request.json();
    } catch (err) {
      return jsonResp({ error: 'invalid JSON', detail: String(err) }, 400);
    }

    const text = String(body?.text || '').trim();
    const voice = String(body?.voice || 'zh-TW-YunJheNeural').trim();
    const rate = String(body?.rate || '+0%').trim();

    if (!text) return jsonResp({ error: 'text required' }, 400);
    if (text.length > MAX_CHARS) return jsonResp({ error: `text too long (max ${MAX_CHARS})` }, 400);
    if (!/^[a-zA-Z]{2,3}-[A-Za-z]{2,4}-[A-Za-z]+Neural$/.test(voice)) {
      return jsonResp({ error: 'invalid voice — expect e.g. zh-TW-YunJheNeural' }, 400);
    }
    if (!/^[+-]?\d{1,3}%$/.test(rate)) {
      return jsonResp({ error: 'rate must look like "+25%" or "-10%"' }, 400);
    }

    try {
      const mp3 = await synthesize(text, voice, rate);
      return new Response(mp3, {
        status: 200,
        headers: {
          ...CORS,
          'Content-Type': 'audio/mpeg',
          'Cache-Control': 'public, max-age=86400, immutable',
        },
      });
    } catch (err) {
      return jsonResp({ error: 'tts failed', detail: String(err?.message || err).slice(0, 400) }, 502);
    }
  },
};

function jsonResp(obj, status) {
  return new Response(JSON.stringify(obj), {
    status,
    headers: { ...CORS, 'Content-Type': 'application/json; charset=utf-8' },
  });
}

// ── Microsoft "Sec-MS-GEC" auth token ─────────────────────────────────────
// Mimics Python edge-tts's generate_sec_ms_gec(). The hash uses a Windows-
// epoch tick count, snapped to 5-minute boundaries, concatenated with the
// known TrustedClientToken, then SHA-256'd and upper-cased.
async function generateSecMsGec() {
  const winEpochSeconds = 11644473600;            // seconds between 1601 and 1970
  const ticksPerSecond = 10_000_000;              // 100-ns ticks
  const snap = 3_000_000_000;                     // 5 min in ticks (5*60*1e7)
  let ticks = Math.floor(((Date.now() / 1000) + winEpochSeconds) * ticksPerSecond);
  ticks = ticks - (ticks % snap);
  const buf = new TextEncoder().encode(`${ticks}${TRUSTED_CLIENT_TOKEN}`);
  const hash = await crypto.subtle.digest('SHA-256', buf);
  return [...new Uint8Array(hash)].map(b => b.toString(16).padStart(2, '0')).join('').toUpperCase();
}

function uuid() {
  return crypto.randomUUID().replace(/-/g, '');
}

function escapeXml(s) {
  return s
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&apos;');
}

function buildSsml(text, voice, rate) {
  // The lang attribute is a placeholder; the actual locale comes from the voice name.
  return `<speak version='1.0' xmlns='http://www.w3.org/2001/10/synthesis' xml:lang='en-US'>` +
         `<voice name='${voice}'>` +
         `<prosody pitch='+0Hz' rate='${rate}' volume='+0%'>` +
         `${escapeXml(text)}` +
         `</prosody></voice></speak>`;
}

// ── The WebSocket dance ───────────────────────────────────────────────────
async function synthesize(text, voice, rate) {
  const gec = await generateSecMsGec();
  const url =
    `https://${WSS_HOST}${WSS_PATH}` +
    `&Sec-MS-GEC=${gec}` +
    `&Sec-MS-GEC-Version=1-130.0.2849.68` +
    `&ConnectionId=${uuid()}`;

  // Cloudflare Workers do WebSocket clients via fetch() with Upgrade header.
  const upgradeResp = await fetch(url, {
    headers: {
      'Upgrade': 'websocket',
      'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ' +
        '(KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0',
      'Origin': 'chrome-extension://jdiccldimpdaibmpdkjnbmckianbfold',
    },
  });

  if (upgradeResp.status !== 101) {
    const body = await upgradeResp.text().catch(() => '');
    throw new Error(`upgrade failed: HTTP ${upgradeResp.status} ${body.slice(0, 160)}`);
  }
  const ws = upgradeResp.webSocket;
  if (!ws) throw new Error('no websocket on upgrade response');
  ws.accept();

  const requestId = uuid();
  const timestamp = new Date().toString().replace('GMT+0000 (Coordinated Universal Time)', 'GMT+0000 (Coordinated Universal Time)');

  // Frame 1: speech.config — bind audio format + metadata options.
  const configBody = {
    context: {
      synthesis: {
        audio: {
          metadataoptions: {
            sentenceBoundaryEnabled: 'false',
            wordBoundaryEnabled: 'false',
          },
          outputFormat: 'audio-24khz-48kbitrate-mono-mp3',
        },
      },
    },
  };
  const configMsg =
    `X-Timestamp:${timestamp}\r\n` +
    `Content-Type:application/json; charset=utf-8\r\n` +
    `Path:speech.config\r\n\r\n` +
    JSON.stringify(configBody);
  ws.send(configMsg);

  // Frame 2: SSML containing the text + voice.
  const ssmlMsg =
    `X-RequestId:${requestId}\r\n` +
    `Content-Type:application/ssml+xml\r\n` +
    `X-Timestamp:${timestamp}\r\n` +
    `Path:ssml\r\n\r\n` +
    buildSsml(text, voice, rate);
  ws.send(ssmlMsg);

  // Collect audio chunks until we see Path:turn.end or the socket closes.
  return new Promise((resolve, reject) => {
    const chunks = [];
    let done = false;

    const finish = () => {
      if (done) return;
      done = true;
      try { ws.close(1000, 'done'); } catch (_) {}
      if (!chunks.length) {
        reject(new Error('empty audio'));
      } else {
        const total = chunks.reduce((n, c) => n + c.byteLength, 0);
        const out = new Uint8Array(total);
        let off = 0;
        for (const c of chunks) { out.set(new Uint8Array(c), off); off += c.byteLength; }
        resolve(out.buffer);
      }
    };

    const timer = setTimeout(() => {
      if (done) return;
      done = true;
      try { ws.close(1001, 'timeout'); } catch (_) {}
      reject(new Error('synthesis timed out'));
    }, TIMEOUT_MS);

    ws.addEventListener('message', (event) => {
      const data = event.data;
      if (data instanceof ArrayBuffer || ArrayBuffer.isView(data)) {
        // Binary frame: 2-byte big-endian header length, then headers, then audio.
        const u8 = data instanceof ArrayBuffer ? new Uint8Array(data) : new Uint8Array(data.buffer);
        if (u8.byteLength < 2) return;
        const headerLen = (u8[0] << 8) | u8[1];
        if (u8.byteLength < 2 + headerLen) return;
        chunks.push(u8.slice(2 + headerLen).buffer);
      } else if (typeof data === 'string') {
        if (/Path:turn\.end/.test(data)) {
          clearTimeout(timer);
          finish();
        }
      }
    });
    ws.addEventListener('close', () => { clearTimeout(timer); finish(); });
    ws.addEventListener('error', (err) => {
      if (done) return;
      done = true;
      clearTimeout(timer);
      reject(new Error('websocket error'));
    });
  });
}
