// Vercel serverless function: Gemini 3.1 Flash TTS proxy.
// Receives { text, lang, voice } as JSON, calls Gemini, returns audio/wav.
// The API key lives in Vercel env (GEMINI_API_KEY) and never reaches the browser.

export const config = {
  runtime: 'nodejs',
  maxDuration: 60,
};

const GEMINI_MODEL = 'gemini-3.1-flash-tts-preview';

// Sensible defaults per language. Voices work cross-language; these were
// chosen for narrative reading: Kore is a firm female voice that handles
// Mandarin tone well, Aoede is breezy and easy to listen to in English.
const DEFAULT_VOICES = { zh: 'Kore', en: 'Aoede' };

// Most paragraphs in the article are well under this; cap to keep latency
// bounded and to match Gemini's per-call sweet spot.
const MAX_TEXT_LEN = 4000;

function pcmToWav(pcmBuffer, sampleRate, channels = 1, bitsPerSample = 16) {
  const byteRate   = (sampleRate * channels * bitsPerSample) / 8;
  const blockAlign = (channels * bitsPerSample) / 8;
  const dataLen    = pcmBuffer.length;
  const buf        = Buffer.alloc(44 + dataLen);

  buf.write('RIFF', 0);
  buf.writeUInt32LE(36 + dataLen, 4);
  buf.write('WAVE', 8);
  buf.write('fmt ', 12);
  buf.writeUInt32LE(16, 16);              // PCM fmt chunk size
  buf.writeUInt16LE(1, 20);               // audio format = PCM
  buf.writeUInt16LE(channels, 22);
  buf.writeUInt32LE(sampleRate, 24);
  buf.writeUInt32LE(byteRate, 28);
  buf.writeUInt16LE(blockAlign, 32);
  buf.writeUInt16LE(bitsPerSample, 34);
  buf.write('data', 36);
  buf.writeUInt32LE(dataLen, 40);
  pcmBuffer.copy(buf, 44);
  return buf;
}

function parseRate(mimeType) {
  // Gemini returns mime like "audio/l16; rate=24000; channels=1"
  const m = /rate=(\d+)/i.exec(mimeType || '');
  return m ? parseInt(m[1], 10) : 24000;
}

async function readJsonBody(req) {
  if (req.body && typeof req.body === 'object') return req.body;
  const chunks = [];
  for await (const c of req) chunks.push(c);
  const raw = Buffer.concat(chunks).toString('utf8');
  return raw ? JSON.parse(raw) : {};
}

export default async function handler(req, res) {
  // CORS: allow same-origin static page (and local dev) to call this.
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
  if (req.method === 'OPTIONS') return res.status(204).end();
  if (req.method !== 'POST')    return res.status(405).json({ error: 'POST only' });

  const apiKey = process.env.GEMINI_API_KEY;
  if (!apiKey) return res.status(500).json({ error: 'GEMINI_API_KEY not set on server' });

  let body;
  try { body = await readJsonBody(req); }
  catch (e) { return res.status(400).json({ error: 'Invalid JSON body' }); }

  const text = (body.text || '').toString().trim();
  if (!text) return res.status(400).json({ error: '`text` required' });
  if (text.length > MAX_TEXT_LEN) {
    return res.status(400).json({ error: `text too long (max ${MAX_TEXT_LEN} chars)` });
  }
  const lang  = body.lang === 'en' ? 'en' : 'zh';
  const voice = (body.voice || DEFAULT_VOICES[lang]).toString();

  try {
    const upstream = await fetch(
      `https://generativelanguage.googleapis.com/v1beta/models/${GEMINI_MODEL}:generateContent?key=${encodeURIComponent(apiKey)}`,
      {
        method:  'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          contents: [{ parts: [{ text }] }],
          generationConfig: {
            responseModalities: ['AUDIO'],
            speechConfig: {
              voiceConfig: { prebuiltVoiceConfig: { voiceName: voice } },
            },
          },
        }),
      }
    );

    if (!upstream.ok) {
      const detail = (await upstream.text()).slice(0, 800);
      console.error('[tts] upstream error', upstream.status, detail);
      return res.status(upstream.status).json({ error: 'Gemini API error', detail });
    }

    const data = await upstream.json();
    const part = data.candidates?.[0]?.content?.parts?.find((p) => p.inlineData);
    if (!part) {
      return res.status(502).json({ error: 'No audio in Gemini response' });
    }

    const pcm  = Buffer.from(part.inlineData.data, 'base64');
    const rate = parseRate(part.inlineData.mimeType);
    const wav  = pcmToWav(pcm, rate, 1, 16);

    res.setHeader('Content-Type', 'audio/wav');
    res.setHeader('Content-Length', String(wav.length));
    // Same text + voice → identical audio. Browser-cache aggressively.
    res.setHeader('Cache-Control', 'public, max-age=86400, immutable');
    return res.status(200).end(wav);
  } catch (err) {
    console.error('[tts] handler error', err);
    return res.status(500).json({ error: 'Internal error', detail: String(err).slice(0, 300) });
  }
}
