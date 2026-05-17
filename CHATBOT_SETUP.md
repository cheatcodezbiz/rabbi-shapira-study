# Study-Partner Chatbot — Setup

A floating RAG chat widget grounded in this site's own articles and
study guides. Built on:

| Layer        | Service                                              |
| ------------ | ---------------------------------------------------- |
| Vector store | **Pinecone** (serverless index)                      |
| Embeddings   | **Voyage AI** — `voyage-3-lite` (512-dim, multilingual) |
| Chat LLM     | **OpenRouter** — default `deepseek/deepseek-chat`     |
| Frontend     | Vanilla JS floating bubble (`/assets/chat.js`)        |
| API          | Vercel Python function (`/api/chat.py`)               |

## 1. Provision external services

### 1a. Pinecone

1. Sign in at <https://app.pinecone.io>.
2. Create a **Serverless index** with these settings:
   - **Name**: anything — e.g. `rabbi-shapira-rag`
   - **Dimensions**: **`512`** (must match `voyage-3-lite`)
   - **Metric**: `cosine`
   - **Cloud**: AWS, `us-east-1` (cheapest serverless region)
3. From the dashboard, copy the **API key** (`PINECONE_API_KEY`) and the
   **index name** (`PINECONE_INDEX_NAME`).

### 1b. Voyage AI

1. Sign up at <https://www.voyageai.com>.
2. Create an API key (`VOYAGE_API_KEY`). The free tier gives you 50M
   tokens — more than enough to embed this whole site many times over.

### 1c. OpenRouter

1. Sign up at <https://openrouter.ai>.
2. Add ~$5 of credits (will last thousands of chat turns with DeepSeek).
3. Copy your API key (`OPENROUTER_API_KEY`).

## 2. Add environment variables to Vercel

In the Vercel project settings → **Environment Variables**, add:

```text
PINECONE_API_KEY            <from Pinecone>
PINECONE_INDEX_NAME         <your index name>
VOYAGE_API_KEY              <from Voyage>
OPENROUTER_API_KEY          <from OpenRouter>

# Optional — override defaults
OPENROUTER_MODEL            deepseek/deepseek-chat
EMBED_MODEL                 voyage-3-lite
EMBED_DIM                   512
TOP_K                       8
SITE_URL                    https://rabbi-shapira-study.vercel.app
SITE_NAME                   Light of Torah — Rabbi Shapira Study
```

Mark all of them for **Production** + **Preview** + **Development**.

## 3. Build the index (one-time, plus after content changes)

The indexer is a local dev script. It walks every `*.html`, splits the
bilingual spans, chunks the prose, embeds with Voyage, and upserts into
Pinecone. Re-running is **idempotent** — only changed chunks get
re-embedded (it keeps a hash ledger at `.rag-state/chunk_hashes.json`).

```bash
# One-time:
pip install -r scripts/requirements.txt

# Locally export the same env vars Vercel has:
export PINECONE_API_KEY=…
export PINECONE_INDEX_NAME=…
export VOYAGE_API_KEY=…

# Build (dry-run first to check what would happen):
DRY_RUN=1 python scripts/build_index.py
python scripts/build_index.py
```

Expected output on a clean run with the current ~9 pages:

```text
[index] scanning 9 pages
  • index.html                              →   ~6 chunks
  • article-499-mashiach-ben-yosef.html      →  ~14 chunks
  • article-epic-fury-isaiah26.html          →  ~14 chunks
  • article-messiah-birthing-iran.html       →  ~26 chunks
  • article-pesach-hormuz-yitro.html         →  ~14 chunks
  • article-vayikra-call-grafted-in.html     →  ~14 chunks
  • article-zion-birth-pangs.html            →  ~14 chunks
  • study-rivkah-remnant.html                →  ~22 chunks
  • study-romans11-jewish-dna.html           →  ~22 chunks
[index] total chunks: ~146
```

Each page produces chunks in both `zh` and `en` so retrieval works in
either language.

**Re-run the indexer any time you add or edit a page.** Add a hook to
your normal publish workflow, or just run it manually.

## 4. Test locally (optional)

```bash
# In one terminal, run a static server pointing at the repo:
python -m http.server 8000

# In another, run Vercel CLI dev to expose /api/chat:
vercel dev
```

Visit any page, click the gold chat bubble bottom-right, ask a question.

## 5. How the chatbot decides what to say

1. **Embed** the user's question with Voyage (`voyage-3-lite`, `input_type=query`).
2. **Retrieve** top-K (default 8) chunks from Pinecone, filtered to the
   user's UI language. If the preferred-language pool comes back thin,
   it tops up with the other language so cross-language questions work.
3. **Build prompt** with a "chavruta" (study partner) system prompt
   + a `SOURCES [S1]…[Sn]` block of retrieved chunk text.
4. **Stream** OpenRouter's chat completion back to the browser as SSE.
5. **Frontend** renders `[Sn]` tags as clickable pills that deep-link
   to the source article (URL + in-page `#anchor` when available).

## 6. Costs (back-of-envelope)

| Item               | Unit price                       | Notes                                |
| ------------------ | -------------------------------- | ------------------------------------ |
| Voyage embeddings  | $0.02 / 1M tokens                | Whole site ~ <$0.01 to (re)embed     |
| Pinecone           | Free up to 100k vectors          | Current corpus: ~150 vectors         |
| OpenRouter / DeepSeek | $0.27 in / $1.10 out / 1M tokens | ~$0.002 per chat turn             |
| Vercel function    | included in your plan            | One streaming POST per turn          |

So at 1,000 chat turns/month you're looking at about **$2/month** total.

## 7. Maintenance

- **After adding an article**: run `python scripts/build_index.py`.
- **After deleting an article**: same script — it detects removed
  chunks via the ledger and `DELETE`s them from Pinecone.
- **To change the LLM**: just update the `OPENROUTER_MODEL` env var in
  Vercel and redeploy. No code change needed.
- **To swap embedding model**: update `EMBED_MODEL` + `EMBED_DIM` in
  env, **destroy & recreate the Pinecone index** at the new dimension,
  then re-run `build_index.py`.

## 8. Files in this feature

```
scripts/
  build_index.py            ← extractor + chunker + upserter
  requirements.txt          ← bs4 + pinecone + requests
api/
  chat.py                   ← Vercel function: embed → retrieve → stream
  requirements.txt          ← + pinecone + requests
assets/
  chat.js                   ← single-file widget (CSS injected)
.rag-state/                 ← local-only hash ledger (gitignore'd)
  chunk_hashes.json
```

`.rag-state/` is local-only. **Add it to `.gitignore`** if it isn't
already (the project root file). It's not secret, just noise.
