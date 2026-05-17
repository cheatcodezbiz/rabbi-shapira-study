"""Study-partner RAG chat endpoint.

POST JSON:
    {
      "message": "user question",
      "history": [{"role": "user"|"assistant", "content": "..."}],
      "lang":    "zh" | "en"          // optional; auto-detected if absent
    }

Streams Server-Sent Events back:
    event: sources           (one event with the retrieved citations)
    event: token             (many — each is a streamed LLM token)
    event: done              (terminal)
    event: error             (on failure)

The lambda is intentionally tiny: it embeds the question with Voyage AI,
queries Pinecone, builds a context-stuffed prompt, and proxies the
OpenRouter chat completion stream straight back to the browser as SSE.

Env vars:
    PINECONE_API_KEY, PINECONE_INDEX_NAME
    VOYAGE_API_KEY
    OPENROUTER_API_KEY
    OPENROUTER_MODEL          (default: deepseek/deepseek-chat)
    EMBED_MODEL               (default: voyage-3-lite)
    EMBED_DIM                 (default: 512)
    TOP_K                     (default: 8)
    SITE_URL                  (sent to OpenRouter as HTTP-Referer)
    SITE_NAME                 (sent to OpenRouter as X-Title)
"""
from http.server import BaseHTTPRequestHandler
import json
import os
import re
import time

import requests
from pinecone import Pinecone


# ─── Config ─────────────────────────────────────────────────────────────────

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
OPENROUTER_MODEL = os.environ.get("OPENROUTER_MODEL", "deepseek/deepseek-chat")

VOYAGE_URL = "https://api.voyageai.com/v1/embeddings"
EMBED_MODEL = os.environ.get("EMBED_MODEL", "voyage-3-lite")
EMBED_DIM = int(os.environ.get("EMBED_DIM", "512"))

TOP_K = int(os.environ.get("TOP_K", "8"))
MAX_CONTEXT_CHUNKS = 6   # how many retrieved chunks we put into the prompt
MAX_HISTORY_TURNS = 6    # rolling window of prior turns kept

SITE_URL = os.environ.get("SITE_URL", "https://rabbi-shapira-study.vercel.app")
SITE_NAME = os.environ.get("SITE_NAME", "Light of Torah · Rabbi Shapira Study")


# ─── Embedding ──────────────────────────────────────────────────────────────

def embed_query(text: str) -> list[float]:
    api_key = os.environ.get("VOYAGE_API_KEY")
    if not api_key:
        raise RuntimeError("VOYAGE_API_KEY not set")
    r = requests.post(
        VOYAGE_URL,
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        json={
            "model": EMBED_MODEL,
            "input": [text],
            "input_type": "query",
            "output_dimension": EMBED_DIM,
        },
        timeout=15,
    )
    r.raise_for_status()
    return r.json()["data"][0]["embedding"]


# ─── Retrieval ──────────────────────────────────────────────────────────────

_pc_index = None


def _index():
    global _pc_index
    if _pc_index is None:
        pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])
        _pc_index = pc.Index(os.environ["PINECONE_INDEX_NAME"])
    return _pc_index


def retrieve(query_vec: list[float], lang: str, k: int = TOP_K) -> list[dict]:
    """Pull top-K chunks from Pinecone, preferring the user's language but
    falling back to the other if too few matches survive the score floor."""
    idx = _index()
    pref = idx.query(
        vector=query_vec, top_k=k, include_metadata=True,
        filter={"lang": {"$eq": lang}},
    )
    matches = list(getattr(pref, "matches", []) or [])
    # If the preferred-language pool is thin, top up with the other language.
    if len(matches) < 3:
        other = "en" if lang == "zh" else "zh"
        topup = idx.query(
            vector=query_vec, top_k=k, include_metadata=True,
            filter={"lang": {"$eq": other}},
        )
        seen_ids = {m.id for m in matches}
        for m in (getattr(topup, "matches", []) or []):
            if m.id not in seen_ids:
                matches.append(m)
        matches = matches[:k]
    return [
        {
            "id": m.id,
            "score": float(getattr(m, "score", 0.0) or 0.0),
            **(m.metadata or {}),
        }
        for m in matches
    ]


# ─── Prompt assembly ────────────────────────────────────────────────────────

SYSTEM_PROMPT_BASE = (
    "You are a Torah study partner ('chavruta') for users of the Light of "
    "Torah / Ahavat Ammi website by Rabbi Dr. Itzhak Shapira. Your purpose "
    "is to help readers go deeper into the rabbi's published teachings on "
    "his site — not to lecture, but to converse, question, clarify, and "
    "send them back into the text.\n\n"
    "Hard rules:\n"
    "1. Ground every claim in the CONTEXT below. If the context does not "
    "   cover the question, say so plainly and suggest what the user could "
    "   look up next. Do not invent rabbinic citations.\n"
    "2. When you use a passage, append a citation tag like [S1], [S2] that "
    "   refers to the SOURCES list in the context. The frontend will turn "
    "   these into clickable source pills.\n"
    "3. Match the user's language. If they wrote in Chinese, answer in "
    "   simplified Chinese (简中). If in English, answer in English.\n"
    "4. Honor the rabbi's hashkafah (worldview). He is a Messianic Jewish "
    "   rabbi who reads Yeshua/Jesus as the Messiah ben Yosef and ben "
    "   David. Do not flatten his arguments into either generic "
    "   Christianity or generic Orthodox Judaism — he stands deliberately "
    "   between the two.\n"
    "5. Preserve Hebrew terms when the source uses them (e.g. shuvu, "
    "   teshuvah, tikkun, mesirut nefesh, Mashiach ben Yosef, kavanah). "
    "   Briefly translate the first time each appears in your reply.\n"
    "6. Keep replies focused. Two to four short paragraphs is usually "
    "   right; a numbered list is fine when the rabbi himself uses one.\n"
    "7. End with one short follow-up question or invitation when natural — "
    "   you are a chavruta, not a search box.\n"
)


def _format_context(chunks: list[dict]) -> tuple[str, list[dict]]:
    """Build the SOURCES block for the system prompt, return (text, used)."""
    used = chunks[:MAX_CONTEXT_CHUNKS]
    lines = []
    for i, c in enumerate(used, start=1):
        title = c.get("title_en") or c.get("title_zh") or c.get("slug") or "Untitled"
        section = c.get("section") or ""
        body = c.get("text") or ""
        # Trim each chunk so we don't blow the context window.
        if len(body) > 1400:
            body = body[:1400].rstrip() + " …"
        header = f"[S{i}] {title}"
        if section:
            header += f" — {section}"
        lines.append(f"{header}\n{body}")
    return "\n\n---\n\n".join(lines), used


def _detect_lang(text: str) -> str:
    """Cheap CJK heuristic — used only if frontend didn't say."""
    cjk = sum(1 for c in text if 0x4E00 <= ord(c) <= 0x9FFF)
    return "zh" if cjk >= max(2, len(text) * 0.08) else "en"


def build_messages(question: str, history: list[dict], context_text: str, lang: str) -> list[dict]:
    system = SYSTEM_PROMPT_BASE + (
        "\n\nUser's preferred language: " +
        ("Simplified Chinese (简中)" if lang == "zh" else "English") +
        ".\n\nSOURCES (numbered [S1], [S2], ...):\n" + (context_text or "(no relevant passages retrieved)")
    )
    msgs = [{"role": "system", "content": system}]
    # Rolling history window.
    if history:
        msgs.extend(history[-MAX_HISTORY_TURNS * 2 :])
    msgs.append({"role": "user", "content": question})
    return msgs


# ─── OpenRouter streaming ───────────────────────────────────────────────────

def stream_openrouter(messages: list[dict]):
    """Yield content tokens from OpenRouter's SSE stream."""
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        raise RuntimeError("OPENROUTER_API_KEY not set")
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": SITE_URL,
        "X-Title": SITE_NAME,
    }
    body = {
        "model": OPENROUTER_MODEL,
        "messages": messages,
        "stream": True,
        "temperature": 0.4,
        "max_tokens": 900,
    }
    with requests.post(OPENROUTER_URL, headers=headers, json=body, stream=True, timeout=120) as r:
        r.raise_for_status()
        # OpenRouter's SSE stream sends `Content-Type: text/event-stream`
        # with no `charset=` parameter. Per RFC 2616 + RFC 7231, `requests`
        # falls back to ISO-8859-1 for text/* with no charset, which mangles
        # every CJK / Hebrew byte. Bypass requests' decoder entirely:
        # iterate raw bytes and decode each line as UTF-8 ourselves.
        for raw_bytes in r.iter_lines(decode_unicode=False):
            if not raw_bytes:
                continue
            try:
                raw = raw_bytes.decode("utf-8")
            except UnicodeDecodeError:
                # Last-resort fallback so a single bad byte can't kill the stream.
                raw = raw_bytes.decode("utf-8", errors="replace")
            if not raw.startswith("data:"):
                continue
            payload = raw[5:].strip()
            if payload == "[DONE]":
                break
            try:
                obj = json.loads(payload)
            except json.JSONDecodeError:
                continue
            try:
                delta = obj["choices"][0]["delta"].get("content")
            except (KeyError, IndexError):
                continue
            if delta:
                yield delta


# ─── SSE helpers ────────────────────────────────────────────────────────────

def _sse(event: str, data) -> bytes:
    if not isinstance(data, str):
        data = json.dumps(data, ensure_ascii=False)
    # SSE requires every line of data: to be prefixed; multi-line payloads
    # are unusual here but split anyway for safety.
    lines = "".join(f"data: {ln}\n" for ln in data.splitlines() or [""])
    return f"event: {event}\n{lines}\n".encode("utf-8")


# ─── Vercel handler ─────────────────────────────────────────────────────────

class handler(BaseHTTPRequestHandler):
    def _send_sse_headers(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/event-stream; charset=utf-8")
        self.send_header("Cache-Control", "no-cache, no-transform")
        self.send_header("Connection", "keep-alive")
        self.send_header("X-Accel-Buffering", "no")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

    def _emit(self, event: str, data):
        try:
            self.wfile.write(_sse(event, data))
            self.wfile.flush()
        except (BrokenPipeError, ConnectionResetError):
            raise

    # Browser preflight.
    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_GET(self):
        # Health check.
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps({
            "ok": True,
            "model": OPENROUTER_MODEL,
            "embed_model": EMBED_MODEL,
        }).encode("utf-8"))

    def do_POST(self):
        try:
            length = int(self.headers.get("Content-Length") or "0")
            raw = self.rfile.read(length) if length else b"{}"
            body = json.loads(raw.decode("utf-8") or "{}")
        except Exception as exc:
            self.send_response(400)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": f"bad json: {exc}"}).encode("utf-8"))
            return

        message = (body.get("message") or "").strip()
        if not message:
            self.send_response(400)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": "message is required"}).encode("utf-8"))
            return
        if len(message) > 2000:
            message = message[:2000]

        history = body.get("history") or []
        # Sanitise history to the only fields we accept.
        clean_history = []
        for h in history if isinstance(history, list) else []:
            if not isinstance(h, dict):
                continue
            role = h.get("role")
            content = h.get("content")
            if role in ("user", "assistant") and isinstance(content, str) and content.strip():
                clean_history.append({"role": role, "content": content[:4000]})

        lang = (body.get("lang") or "").lower()
        if lang not in ("zh", "en"):
            lang = _detect_lang(message)

        self._send_sse_headers()

        try:
            # 1. Embed.
            qvec = embed_query(message)
            # 2. Retrieve.
            chunks = retrieve(qvec, lang)
            # 3. Build context + emit sources event up front so UI can render pills.
            context_text, used = _format_context(chunks)
            self._emit("sources", [{
                "n": i + 1,
                "id": c.get("id"),
                "slug": c.get("slug"),
                "url": c.get("url"),
                "anchor": c.get("anchor"),
                "title_zh": c.get("title_zh"),
                "title_en": c.get("title_en"),
                "section": c.get("section"),
                "snippet": (c.get("text") or "")[:240],
                "score": round(c.get("score") or 0.0, 4),
            } for i, c in enumerate(used)])

            # 4. Stream the LLM answer.
            messages = build_messages(message, clean_history, context_text, lang)
            t0 = time.time()
            wrote_any = False
            for tok in stream_openrouter(messages):
                wrote_any = True
                self._emit("token", tok)
            elapsed_ms = int((time.time() - t0) * 1000)

            self._emit("done", {"elapsed_ms": elapsed_ms, "had_tokens": wrote_any})

        except Exception as exc:
            try:
                self._emit("error", {"message": str(exc)[:500]})
            except Exception:
                pass
