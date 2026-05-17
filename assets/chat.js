/* Light of Torah — RAG study-partner chat widget.
 *
 * Single-file vanilla JS widget that injects its own styles and mounts
 * a floating chat bubble. Designed to coexist with the existing TTS
 * player (which lives bottom-right too — we slot above it on pages that
 * have one, and reposition on mobile).
 *
 * Wire-up: just include
 *     <script defer src="/assets/chat.js?v=1"></script>
 * on any page. Reads the current language from <html data-lang>
 * exactly like the rest of the site.
 *
 * Talks to POST /api/chat which streams Server-Sent Events:
 *     event: sources  (one event with the retrieved citation array)
 *     event: token    (many; each is a string token)
 *     event: done     (terminal)
 *     event: error
 */
(function () {
  'use strict';

  if (window.__lotChatLoaded) return;
  window.__lotChatLoaded = true;

  // ─── Config ─────────────────────────────────────────────────────────
  var API_PATH = '/api/chat';
  var TTS_API_PATH = '/api/tts';
  var HISTORY_KEY = 'lot-chat-history-v1';
  var MAX_HISTORY_TURNS = 8;             // pairs of user+assistant kept

  // Gemini prebuilt voices used for the speak-aloud button on bot replies.
  // Charon = mature, informative male — handles Mandarin + English well.
  // Override via window.LOT_TTS_VOICES = { zh: '...', en: '...' } in a
  // <script> before chat.js if you want to change the defaults.
  // Other male options worth trying: Orus, Fenrir, Algenib, Iapetus.
  var TTS_VOICES = (window.LOT_TTS_VOICES) || {
    zh: 'Charon',
    en: 'Charon'
  };

  var I18N = {
    zh: {
      bubble:       '与拉比对话',
      title:        '学习伙伴 · Chavruta',
      subtitle:     '基于拉比沙皮拉的教导回答你的问题',
      placeholder:  '问一个问题（中文或英文）…',
      send:         '发送',
      stop:         '停止',
      typing:       '拉比正在思考…',
      sources:      '出处',
      clear:        '清空对话',
      speak:        '朗读',
      stopSpeak:    '停止朗读',
      empty: [
        '你好！我是基于沙皮拉拉比著作的学习伙伴。',
        '你可以问我任何关于网站文章、研习指南或拉比观点的问题。',
        '比如：',
        '· 「外邦人的丰满」是什么意思？',
        '· 利百加的「面纱」象征着什么？',
        '· 大卫之子弥赛亚和约瑟之子弥赛亚有什么区别？'
      ],
      errorPrefix:  '抱歉，出错了：'
    },
    en: {
      bubble:       'Ask the Rabbi',
      title:        'Study Partner · Chavruta',
      subtitle:     'Grounded in Rabbi Shapira\'s teachings on this site',
      placeholder:  'Ask a question (English or 中文)…',
      send:         'Send',
      stop:         'Stop',
      typing:       'Thinking…',
      sources:      'Sources',
      clear:        'Clear chat',
      speak:        'Read aloud',
      stopSpeak:    'Stop reading',
      empty: [
        'Shalom! I\'m a study partner grounded in Rabbi Shapira\'s teachings on this site.',
        'Ask me anything about the articles, study guides, or the rabbi\'s positions.',
        'For example:',
        '· What does "the fullness of the Gentiles" mean?',
        '· What does Rivkah\'s veil symbolize?',
        '· How does Mashiach ben Yosef differ from ben David?'
      ],
      errorPrefix:  'Sorry — something went wrong: '
    }
  };

  function lang() {
    return document.documentElement.getAttribute('data-lang') === 'en' ? 'en' : 'zh';
  }
  function t() { return I18N[lang()]; }

  // ─── Styles ─────────────────────────────────────────────────────────
  var STYLE = `
  #lot-chat-bubble {
    position: fixed;
    right: 1.5rem; bottom: 1.5rem;
    width: 60px; height: 60px;
    border-radius: 50%;
    background: linear-gradient(135deg, #b8952a 0%, #d4af5a 100%);
    color: white;
    border: 2px solid rgba(255,255,255,0.18);
    cursor: pointer;
    box-shadow: 0 8px 28px rgba(26,39,68,0.32), 0 0 0 0 rgba(184,149,42,0.45);
    display: flex; align-items: center; justify-content: center;
    z-index: 997;
    transition: transform 0.18s, box-shadow 0.18s;
    font-family: 'Noto Sans SC', sans-serif;
    animation: lot-chat-pulse 2.4s ease-out infinite;
  }
  #lot-chat-bubble:hover { transform: translateY(-2px) scale(1.04); box-shadow: 0 12px 36px rgba(26,39,68,0.42); }
  #lot-chat-bubble.lot-hidden { display: none; }
  #lot-chat-bubble svg { width: 28px; height: 28px; fill: white; }
  @keyframes lot-chat-pulse {
    0%   { box-shadow: 0 8px 28px rgba(26,39,68,0.32), 0 0 0 0 rgba(184,149,42,0.45); }
    70%  { box-shadow: 0 8px 28px rgba(26,39,68,0.32), 0 0 0 18px rgba(184,149,42,0); }
    100% { box-shadow: 0 8px 28px rgba(26,39,68,0.32), 0 0 0 0 rgba(184,149,42,0); }
  }

  /* Slot above the existing #tts-player on pages that have one */
  body:has(#tts-player.tts-visible) #lot-chat-bubble { bottom: 5.2rem; }

  #lot-chat-panel {
    position: fixed;
    right: 1.5rem; bottom: 1.5rem;
    width: 400px;
    max-width: calc(100vw - 1.5rem);
    height: min(620px, calc(100vh - 1.5rem - 3rem));
    background: #faf7f0;
    border: 1px solid #e0d8c8;
    border-radius: 14px;
    box-shadow: 0 24px 60px rgba(13,23,41,0.32);
    display: none;
    flex-direction: column;
    overflow: hidden;
    z-index: 998;
    font-family: 'Noto Serif SC', serif;
    color: #2a2218;
  }
  html[data-lang="en"] #lot-chat-panel { font-family: 'EB Garamond', 'Noto Serif SC', serif; }
  #lot-chat-panel.lot-open { display: flex; }

  .lot-chat-header {
    background: linear-gradient(135deg, #0d1729 0%, #1a2744 100%);
    color: white;
    padding: 0.85rem 1rem;
    display: flex; align-items: center; gap: 0.7rem;
    border-bottom: 2px solid #b8952a;
  }
  .lot-chat-header-mark {
    width: 32px; height: 32px;
    background: #b8952a; border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    color: white; font-weight: 700; font-size: 0.95rem;
    flex-shrink: 0;
    font-family: 'Noto Sans SC', sans-serif;
  }
  .lot-chat-header-text { flex: 1; min-width: 0; }
  .lot-chat-title {
    font-size: 0.92rem; font-weight: 600;
    letter-spacing: 0.04em;
    white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
  }
  .lot-chat-subtitle {
    font-family: 'Noto Sans SC', sans-serif;
    font-size: 0.68rem; color: #d4af5a;
    letter-spacing: 0.06em; opacity: 0.85;
    white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
  }
  .lot-chat-icon-btn {
    background: rgba(255,255,255,0.08);
    border: none; color: white;
    width: 30px; height: 30px;
    border-radius: 50%;
    cursor: pointer;
    display: flex; align-items: center; justify-content: center;
    font-size: 1rem; line-height: 1;
    transition: background 0.15s;
  }
  .lot-chat-icon-btn:hover { background: rgba(255,255,255,0.18); }
  .lot-chat-icon-btn[title]::after { content: attr(title); }

  .lot-chat-body {
    flex: 1; min-height: 0;
    overflow-y: auto;
    padding: 1rem 1rem 0.5rem;
    display: flex; flex-direction: column; gap: 0.85rem;
    scroll-behavior: smooth;
  }

  .lot-msg {
    display: flex; flex-direction: column;
    max-width: 92%;
    font-size: 0.92rem; line-height: 1.7;
  }
  .lot-msg-user { align-self: flex-end; }
  .lot-msg-asst { align-self: flex-start; }
  html[data-lang="en"] .lot-msg { font-size: 1rem; line-height: 1.6; }

  .lot-msg-bubble {
    padding: 0.7rem 0.95rem;
    border-radius: 14px;
    word-wrap: break-word;
    white-space: pre-wrap;
  }
  .lot-msg-user .lot-msg-bubble {
    background: #1a2744;
    color: white;
    border-bottom-right-radius: 4px;
  }
  .lot-msg-asst .lot-msg-bubble {
    background: white;
    color: #2a2218;
    border: 1px solid #e0d8c8;
    border-bottom-left-radius: 4px;
    position: relative;
  }
  .lot-msg-asst { position: relative; }
  .lot-speak-btn {
    background: rgba(184,149,42,0.12);
    color: #b8952a;
    border: 1px solid rgba(184,149,42,0.32);
    cursor: pointer;
    width: 28px; height: 28px;
    border-radius: 50%;
    display: inline-flex; align-items: center; justify-content: center;
    margin-top: 0.4rem;
    align-self: flex-start;
    transition: background 0.15s, color 0.15s, transform 0.12s;
    flex-shrink: 0;
    padding: 0;
    line-height: 1;
  }
  .lot-speak-btn:hover { background: #b8952a; color: white; transform: scale(1.05); }
  .lot-speak-btn svg { width: 14px; height: 14px; fill: currentColor; display: block; }
  .lot-speak-btn.lot-speaking {
    background: #b03030; color: white; border-color: #b03030;
    animation: lot-speak-pulse 1.5s ease-in-out infinite;
  }
  .lot-speak-btn.lot-loading {
    background: rgba(184,149,42,0.18);
    color: #b8952a;
    cursor: progress;
  }
  .lot-speak-btn .lot-spin { animation: lot-spin 0.9s linear infinite; transform-origin: 50% 50%; }
  @keyframes lot-spin { to { transform: rotate(360deg); } }
  @keyframes lot-speak-pulse {
    0%, 100% { box-shadow: 0 0 0 0 rgba(176,48,48,0.4); }
    50%      { box-shadow: 0 0 0 6px rgba(176,48,48,0); }
  }
  .lot-msg-bubble strong { color: #1a2744; font-weight: 600; }
  .lot-msg-bubble em { font-style: italic; }
  .lot-msg-bubble code {
    font-family: 'Courier New', monospace;
    background: rgba(184,149,42,0.12);
    padding: 0.05rem 0.3rem; border-radius: 3px;
    font-size: 0.88em;
  }
  .lot-msg-bubble p { margin: 0 0 0.55rem; }
  .lot-msg-bubble p:last-child { margin-bottom: 0; }

  .lot-cite {
    display: inline-flex; align-items: center;
    background: #b8952a; color: white;
    font-family: 'Noto Sans SC', sans-serif;
    font-size: 0.65rem;
    padding: 0 0.36rem;
    border-radius: 20px;
    margin: 0 0.12rem;
    text-decoration: none;
    cursor: pointer;
    letter-spacing: 0.04em;
    vertical-align: 1px;
    line-height: 1.5;
    transition: background 0.15s;
  }
  .lot-cite:hover { background: #0d1729; }

  .lot-sources {
    margin-top: 0.45rem;
    padding-top: 0.5rem;
    border-top: 1px dashed rgba(184,149,42,0.35);
    display: flex; flex-wrap: wrap; gap: 0.35rem;
  }
  .lot-source-pill {
    background: rgba(184,149,42,0.1);
    color: #1a2744;
    border: 1px solid rgba(184,149,42,0.32);
    font-family: 'Noto Sans SC', sans-serif;
    font-size: 0.7rem;
    padding: 0.22rem 0.55rem;
    border-radius: 14px;
    text-decoration: none;
    line-height: 1.4;
    transition: background 0.15s, color 0.15s;
  }
  .lot-source-pill:hover { background: #1a2744; color: white; }
  .lot-source-pill .lot-source-n {
    color: #b8952a; font-weight: 600;
    margin-right: 0.25rem;
  }
  .lot-source-pill:hover .lot-source-n { color: #d4af5a; }

  .lot-empty {
    color: #6b5f4e;
    font-size: 0.9rem;
    padding: 0.5rem 0.2rem;
  }
  .lot-empty p { margin: 0 0 0.4rem; line-height: 1.7; }
  .lot-empty p:first-child { color: #1a2744; font-weight: 600; }

  .lot-typing {
    color: #6b5f4e; font-size: 0.82rem; font-style: italic;
    padding: 0.4rem 0.2rem;
    display: flex; align-items: center; gap: 0.4rem;
    font-family: 'Noto Sans SC', sans-serif;
  }
  .lot-typing-dot {
    display: inline-block;
    width: 6px; height: 6px;
    border-radius: 50%;
    background: #b8952a;
    animation: lot-bounce 1.2s infinite ease-in-out;
  }
  .lot-typing-dot:nth-child(2) { animation-delay: 0.18s; }
  .lot-typing-dot:nth-child(3) { animation-delay: 0.36s; }
  @keyframes lot-bounce {
    0%, 80%, 100% { opacity: 0.25; transform: scale(0.85); }
    40%           { opacity: 1;    transform: scale(1.15); }
  }

  .lot-input-bar {
    border-top: 1px solid #e0d8c8;
    background: white;
    padding: 0.6rem 0.7rem 0.7rem;
    display: flex; gap: 0.45rem;
    align-items: flex-end;
  }
  .lot-input {
    flex: 1; min-width: 0;
    border: 1px solid #e0d8c8;
    border-radius: 18px;
    padding: 0.55rem 0.85rem;
    font-family: inherit;
    font-size: 0.92rem;
    color: #2a2218;
    background: #faf7f0;
    outline: none;
    resize: none;
    max-height: 120px;
    line-height: 1.5;
    transition: border-color 0.15s;
  }
  .lot-input:focus { border-color: #b8952a; }
  .lot-send-btn {
    background: #1a2744;
    color: white;
    border: none;
    border-radius: 50%;
    width: 38px; height: 38px;
    cursor: pointer;
    flex-shrink: 0;
    display: flex; align-items: center; justify-content: center;
    transition: background 0.15s, transform 0.1s;
  }
  .lot-send-btn:hover { background: #b8952a; }
  .lot-send-btn:disabled { opacity: 0.35; cursor: not-allowed; }
  .lot-send-btn.lot-stop { background: #b03030; }
  .lot-send-btn svg { width: 16px; height: 16px; fill: white; }

  .lot-disclaimer {
    text-align: center;
    font-family: 'Noto Sans SC', sans-serif;
    font-size: 0.6rem;
    color: #a39684;
    padding: 0.25rem 0.5rem 0.4rem;
    background: white;
    letter-spacing: 0.04em;
  }

  /* ── Mobile ── */
  @media (max-width: 640px) {
    #lot-chat-bubble { right: 0.9rem; bottom: 0.9rem; width: 54px; height: 54px; }
    body:has(#tts-player.tts-visible) #lot-chat-bubble { bottom: 4.7rem; }
    #lot-chat-panel {
      right: 0.5rem; left: 0.5rem; bottom: 0.5rem;
      width: auto;
      height: calc(100vh - 1rem);
      max-height: 92vh;
    }
  }
  `;

  // ─── DOM ────────────────────────────────────────────────────────────

  var bubble, panel, body, input, sendBtn, headerTitle, headerSub;
  var sourcesByMsg = {}; // msgId -> array of sources
  var currentController = null;
  var currentAssistantBubble = null;
  var currentSourcesEl = null;
  var currentSources = [];
  var streamingText = '';

  function mount() {
    var style = document.createElement('style');
    style.id = 'lot-chat-style';
    style.textContent = STYLE;
    document.head.appendChild(style);

    bubble = document.createElement('button');
    bubble.id = 'lot-chat-bubble';
    bubble.type = 'button';
    bubble.setAttribute('aria-label', t().bubble);
    bubble.title = t().bubble;
    bubble.innerHTML =
      '<svg viewBox="0 0 24 24" aria-hidden="true">' +
      '<path d="M20 2H4c-1.1 0-2 .9-2 2v18l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zm-2 12H7v-2h11v2zm0-3H7V9h11v2zm0-3H7V5h11v2z"/>' +
      '</svg>';
    bubble.addEventListener('click', openPanel);
    document.body.appendChild(bubble);

    panel = document.createElement('aside');
    panel.id = 'lot-chat-panel';
    panel.setAttribute('role', 'dialog');
    panel.setAttribute('aria-label', t().title);
    panel.innerHTML =
      '<header class="lot-chat-header">' +
        '<div class="lot-chat-header-mark">光</div>' +
        '<div class="lot-chat-header-text">' +
          '<div class="lot-chat-title"></div>' +
          '<div class="lot-chat-subtitle"></div>' +
        '</div>' +
        '<button class="lot-chat-icon-btn" id="lot-chat-clear" aria-label="Clear" title="">↻</button>' +
        '<button class="lot-chat-icon-btn" id="lot-chat-close" aria-label="Close" title="✕">✕</button>' +
      '</header>' +
      '<div class="lot-chat-body" id="lot-chat-body"></div>' +
      '<div class="lot-input-bar">' +
        '<textarea class="lot-input" id="lot-chat-input" rows="1"></textarea>' +
        '<button class="lot-send-btn" id="lot-chat-send" type="button" aria-label="Send">' +
          '<svg viewBox="0 0 24 24"><path d="M2.01 21L23 12 2.01 3 2 10l15 2-15 2z"/></svg>' +
        '</button>' +
      '</div>' +
      '<div class="lot-disclaimer">AI · ' + (lang() === 'zh' ? '请始终参照原文核对引用' : 'Always verify citations in the source') + '</div>';
    document.body.appendChild(panel);

    body         = panel.querySelector('#lot-chat-body');
    input        = panel.querySelector('#lot-chat-input');
    sendBtn      = panel.querySelector('#lot-chat-send');
    headerTitle  = panel.querySelector('.lot-chat-title');
    headerSub    = panel.querySelector('.lot-chat-subtitle');

    panel.querySelector('#lot-chat-close').addEventListener('click', closePanel);
    panel.querySelector('#lot-chat-clear').addEventListener('click', clearChat);
    sendBtn.addEventListener('click', onSendClick);
    input.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        onSendClick();
      }
    });
    input.addEventListener('input', autosize);

    refreshI18n();
    renderHistory();

    // Re-apply i18n when language toggles elsewhere.
    var lastLang = lang();
    new MutationObserver(function () {
      var L = lang();
      if (L !== lastLang) {
        lastLang = L;
        refreshI18n();
        renderHistory();
      }
    }).observe(document.documentElement, { attributes: true, attributeFilter: ['data-lang'] });
  }

  function refreshI18n() {
    var L = t();
    bubble.title = L.bubble;
    bubble.setAttribute('aria-label', L.bubble);
    headerTitle.textContent = L.title;
    headerSub.textContent = L.subtitle;
    input.placeholder = L.placeholder;
    panel.querySelector('#lot-chat-clear').title = L.clear;
  }

  function openPanel() {
    panel.classList.add('lot-open');
    bubble.classList.add('lot-hidden');
    setTimeout(function () { input.focus(); }, 80);
    scrollToBottom();
  }
  function closePanel() {
    panel.classList.remove('lot-open');
    bubble.classList.remove('lot-hidden');
    if (window.__lotChatStopSpeaking) window.__lotChatStopSpeaking();
  }
  function autosize() {
    input.style.height = 'auto';
    input.style.height = Math.min(120, input.scrollHeight) + 'px';
  }
  function scrollToBottom() {
    if (body) body.scrollTop = body.scrollHeight;
  }

  // ─── History ────────────────────────────────────────────────────────

  function loadHistory() {
    try {
      var raw = localStorage.getItem(HISTORY_KEY);
      var parsed = raw ? JSON.parse(raw) : [];
      return Array.isArray(parsed) ? parsed : [];
    } catch (_) { return []; }
  }
  function saveHistory(h) {
    var trimmed = h.slice(-MAX_HISTORY_TURNS * 2);
    try { localStorage.setItem(HISTORY_KEY, JSON.stringify(trimmed)); } catch (_) {}
  }
  function clearChat() {
    if (currentController) currentController.abort();
    if (window.__lotChatStopSpeaking) window.__lotChatStopSpeaking();
    localStorage.removeItem(HISTORY_KEY);
    sourcesByMsg = {};
    renderHistory();
  }

  // ─── Rendering ──────────────────────────────────────────────────────

  // Tiny safe markdown: bold/italic/code/paragraphs + [Sn] citation tags.
  function escapeHtml(s) {
    return s.replace(/[&<>"']/g, function (c) {
      return ({ '&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;' })[c];
    });
  }
  function renderInlineMarkdown(s, sources) {
    var html = escapeHtml(s);
    // Citation tags  [S1]  →  <a class="lot-cite" data-n="1">[S1]</a>
    html = html.replace(/\[S(\d{1,2})\]/g, function (_m, n) {
      var idx = parseInt(n, 10);
      var src = sources && sources[idx - 1];
      if (src && (src.url || src.anchor)) {
        var href = (src.url || '') + (src.anchor ? '#' + src.anchor : '');
        return '<a class="lot-cite" href="' + escapeHtml(href) + '">[S' + idx + ']</a>';
      }
      return '<span class="lot-cite" style="background:#a39684">[S' + idx + ']</span>';
    });
    // Bold **x**
    html = html.replace(/\*\*([^*\n]+)\*\*/g, '<strong>$1</strong>');
    // Italic *x*  (avoid eating bold's leftover)
    html = html.replace(/(^|[^*])\*([^*\n]+)\*/g, '$1<em>$2</em>');
    // Inline code `x`
    html = html.replace(/`([^`\n]+)`/g, '<code>$1</code>');
    return html;
  }
  function renderMessageHtml(text, sources) {
    var paras = text.split(/\n{2,}/).map(function (p) { return p.trim(); }).filter(Boolean);
    if (!paras.length) return '';
    return paras.map(function (p) {
      // Single newlines inside a paragraph → <br>
      var withBr = p.split('\n').map(function (line) { return renderInlineMarkdown(line, sources); }).join('<br>');
      return '<p>' + withBr + '</p>';
    }).join('');
  }

  function renderEmpty() {
    body.innerHTML = '';
    var div = document.createElement('div');
    div.className = 'lot-empty';
    div.innerHTML = t().empty.map(function (line) {
      return '<p>' + escapeHtml(line) + '</p>';
    }).join('');
    body.appendChild(div);
  }

  function renderHistory() {
    var h = loadHistory();
    body.innerHTML = '';
    if (!h.length) { renderEmpty(); return; }
    h.forEach(function (m, i) {
      addMessage(m.role, m.content, m.sources || (sourcesByMsg[i] || null), false);
    });
    scrollToBottom();
  }

  function addMessage(role, text, sources, scroll) {
    if (body.querySelector('.lot-empty')) body.innerHTML = '';
    var wrap = document.createElement('div');
    wrap.className = 'lot-msg ' + (role === 'user' ? 'lot-msg-user' : 'lot-msg-asst');
    var bubble = document.createElement('div');
    bubble.className = 'lot-msg-bubble';
    bubble.innerHTML = renderMessageHtml(text || '', sources);
    wrap.appendChild(bubble);
    var srcEl = null;
    var speakBtn = null;
    if (role === 'assistant') {
      // Attach a speaker button — wires into the Web Speech API.
      speakBtn = makeSpeakBtn(function () {
        return ttsTextFromBubble(bubble);
      }, speakBtn);
      // We store the ref so toggleSpeak can find it; also attach after sources.
      if (sources && sources.length) {
        srcEl = document.createElement('div');
        srcEl.className = 'lot-sources';
        srcEl.innerHTML = renderSources(sources);
        wrap.appendChild(srcEl);
      }
      wrap.appendChild(speakBtn);
    }
    body.appendChild(wrap);
    if (scroll !== false) scrollToBottom();
    return { wrap: wrap, bubble: bubble, sourcesEl: srcEl, speakBtn: speakBtn };
  }

  // ─── TTS — Edge TTS (server-side Microsoft Read Aloud voices) ───────

  var SPEAK_ICON =
    '<svg viewBox="0 0 24 24" aria-hidden="true">' +
      '<path d="M3 10v4h4l5 5V5L7 10H3zm13.5 2A4.5 4.5 0 0 0 14 7.97v8.05a4.5 4.5 0 0 0 2.5-4.02zM14 3.23v2.06a7 7 0 0 1 0 13.42v2.06A9 9 0 0 0 14 3.23z"/>' +
    '</svg>';
  var STOP_ICON =
    '<svg viewBox="0 0 24 24" aria-hidden="true">' +
      '<rect x="6" y="6" width="12" height="12" rx="2"/>' +
    '</svg>';
  // Spinning dotted ring shown while the server is synthesising the MP3.
  var LOADING_ICON =
    '<svg viewBox="0 0 24 24" aria-hidden="true" class="lot-spin">' +
      '<circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="2.4" stroke-dasharray="14 8"/>' +
    '</svg>';

  // One audio element + one in-flight request controller, shared across messages.
  var ttsAudio = null;
  var ttsController = null;
  var ttsCurrentUrl = null;
  var currentSpeakBtn = null;

  function ttsTextFromBubble(bubble) {
    // Strip citation tags and pull plain text for natural speech.
    var clone = bubble.cloneNode(true);
    clone.querySelectorAll('.lot-cite').forEach(function (c) { c.remove(); });
    return (clone.innerText || clone.textContent || '').replace(/\s+/g, ' ').trim();
  }

  function resetSpeakBtn(btn) {
    if (!btn) return;
    btn.classList.remove('lot-speaking', 'lot-loading');
    btn.innerHTML = SPEAK_ICON;
    btn.title = t().speak;
  }

  function stopSpeaking() {
    if (ttsController) {
      try { ttsController.abort(); } catch (_) {}
      ttsController = null;
    }
    if (ttsAudio) {
      try { ttsAudio.pause(); } catch (_) {}
      try { ttsAudio.src = ''; } catch (_) {}
      ttsAudio = null;
    }
    if (ttsCurrentUrl) {
      try { URL.revokeObjectURL(ttsCurrentUrl); } catch (_) {}
      ttsCurrentUrl = null;
    }
    resetSpeakBtn(currentSpeakBtn);
    currentSpeakBtn = null;
  }
  window.__lotChatStopSpeaking = stopSpeaking;

  function speak(text, btn) {
    if (!text) return;
    // Toggle: clicking the active button stops playback.
    if (currentSpeakBtn === btn && (ttsAudio || ttsController)) {
      stopSpeaking();
      return;
    }
    stopSpeaking();

    var L = lang();
    var voice = TTS_VOICES[L] || TTS_VOICES.zh;
    // Edge TTS caps a single request at ~4000 chars; we cap to 3800 for
    // safety. Replies are normally well under this.
    var clipped = text.length > 3800 ? text.slice(0, 3800) + '…' : text;

    currentSpeakBtn = btn;
    btn.classList.add('lot-loading');
    btn.innerHTML = LOADING_ICON;
    btn.title = t().speak + '…';

    var controller = new AbortController();
    ttsController = controller;

    fetch(TTS_API_PATH, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Accept': 'audio/wav' },
      body: JSON.stringify({ text: clipped, lang: L, voice: voice }),
      signal: controller.signal
    })
      .then(function (r) {
        if (!r.ok) throw new Error('TTS HTTP ' + r.status);
        return r.blob();
      })
      .then(function (blob) {
        // Bail out if the user clicked Stop while we were waiting.
        if (controller.signal.aborted) return;
        var url = URL.createObjectURL(blob);
        ttsCurrentUrl = url;
        var audio = new Audio(url);
        ttsAudio = audio;
        audio.onended = function () {
          if (currentSpeakBtn === btn) stopSpeaking();
        };
        audio.onerror = audio.onended;
        btn.classList.remove('lot-loading');
        btn.classList.add('lot-speaking');
        btn.innerHTML = STOP_ICON;
        btn.title = t().stopSpeak;
        audio.play().catch(function (err) {
          console.warn('[chat] audio play blocked:', err);
          stopSpeaking();
        });
      })
      .catch(function (err) {
        if (err && err.name === 'AbortError') return;
        console.warn('[chat] tts error:', err);
        stopSpeaking();
      });
  }

  function makeSpeakBtn(getText) {
    var btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'lot-speak-btn';
    btn.title = t().speak;
    btn.setAttribute('aria-label', t().speak);
    btn.innerHTML = SPEAK_ICON;
    btn.addEventListener('click', function () {
      var text = getText();
      speak(text, btn);
    });
    return btn;
  }

  // Stop speaking if the panel is closed or the page is hidden.
  document.addEventListener('visibilitychange', function () {
    if (document.hidden) stopSpeaking();
  });

  function renderSources(sources) {
    return sources.map(function (s, i) {
      var href = (s.url || '') + (s.anchor ? '#' + s.anchor : '');
      var label = (lang() === 'zh' ? (s.title_zh || s.title_en) : (s.title_en || s.title_zh)) || s.slug || 'source';
      var section = s.section ? (' · ' + s.section) : '';
      return '<a class="lot-source-pill" href="' + escapeHtml(href) + '" title="' + escapeHtml(s.snippet || '') + '">' +
               '<span class="lot-source-n">S' + (i + 1) + '</span>' + escapeHtml(label) + escapeHtml(section) +
             '</a>';
    }).join('');
  }

  // ─── Streaming send ─────────────────────────────────────────────────

  function setSending(isSending) {
    if (isSending) {
      sendBtn.classList.add('lot-stop');
      sendBtn.setAttribute('aria-label', t().stop);
      sendBtn.innerHTML = '<svg viewBox="0 0 24 24"><rect x="6" y="6" width="12" height="12" rx="2"/></svg>';
    } else {
      sendBtn.classList.remove('lot-stop');
      sendBtn.setAttribute('aria-label', t().send);
      sendBtn.innerHTML = '<svg viewBox="0 0 24 24"><path d="M2.01 21L23 12 2.01 3 2 10l15 2-15 2z"/></svg>';
    }
  }

  function onSendClick() {
    if (currentController) {
      currentController.abort();
      return;
    }
    var text = (input.value || '').trim();
    if (!text) return;
    input.value = '';
    autosize();
    send(text);
  }

  function send(question) {
    var history = loadHistory().map(function (m) {
      return { role: m.role, content: m.content };
    });
    addMessage('user', question, null);
    // Append optimistically; we'll patch the trailing assistant entry on completion.
    history.push({ role: 'user', content: question });

    var asst = addMessage('assistant', '', null);
    currentAssistantBubble = asst.bubble;
    currentSourcesEl = null;
    currentSources = [];
    streamingText = '';

    // Insert a typing indicator inside the empty bubble.
    asst.bubble.innerHTML =
      '<span class="lot-typing">' +
        '<span class="lot-typing-dot"></span>' +
        '<span class="lot-typing-dot"></span>' +
        '<span class="lot-typing-dot"></span>' +
        '<span style="margin-left:0.2rem;">' + escapeHtml(t().typing) + '</span>' +
      '</span>';
    scrollToBottom();
    setSending(true);

    var controller = new AbortController();
    currentController = controller;

    fetch(API_PATH, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Accept': 'text/event-stream' },
      body: JSON.stringify({ message: question, history: history.slice(0, -1), lang: lang() }),
      signal: controller.signal
    })
      .then(function (resp) {
        if (!resp.ok || !resp.body) throw new Error('HTTP ' + resp.status);
        return readSSE(resp.body, asst);
      })
      .then(function (final) {
        // Persist a full assistant turn (with its sources).
        var h = loadHistory();
        h.push({ role: 'user', content: question });
        h.push({ role: 'assistant', content: final.text, sources: final.sources });
        saveHistory(h);
      })
      .catch(function (err) {
        if (err && err.name === 'AbortError') {
          asst.bubble.innerHTML = renderMessageHtml('…', null);
        } else {
          console.error('[chat] error', err);
          asst.bubble.innerHTML = renderMessageHtml(t().errorPrefix + (err && err.message || 'unknown'), null);
        }
      })
      .finally(function () {
        currentController = null;
        setSending(false);
      });
  }

  function readSSE(stream, asst) {
    var reader = stream.getReader();
    var decoder = new TextDecoder('utf-8');
    var buffer = '';
    var firstToken = true;

    function processEvent(ev) {
      if (!ev) return;
      var lines = ev.split('\n');
      var name = 'message';
      var data = '';
      for (var i = 0; i < lines.length; i++) {
        var line = lines[i];
        if (line.indexOf('event:') === 0) name = line.slice(6).trim();
        else if (line.indexOf('data:') === 0) data += line.slice(5).replace(/^ /, '') + '\n';
      }
      data = data.replace(/\n$/, '');

      if (name === 'sources') {
        try { currentSources = JSON.parse(data) || []; }
        catch (_) { currentSources = []; }
        if (currentSources.length) {
          if (!currentSourcesEl) {
            currentSourcesEl = document.createElement('div');
            currentSourcesEl.className = 'lot-sources';
            asst.wrap.appendChild(currentSourcesEl);
          }
          currentSourcesEl.innerHTML = renderSources(currentSources);
        }
      } else if (name === 'token') {
        if (firstToken) {
          firstToken = false;
          asst.bubble.innerHTML = '';
        }
        streamingText += data;
        asst.bubble.innerHTML = renderMessageHtml(streamingText, currentSources);
        scrollToBottom();
      } else if (name === 'error') {
        try {
          var obj = JSON.parse(data);
          asst.bubble.innerHTML = renderMessageHtml(t().errorPrefix + (obj.message || 'unknown'), null);
        } catch (_) {
          asst.bubble.innerHTML = renderMessageHtml(t().errorPrefix + data, null);
        }
      } else if (name === 'done') {
        // Final flush — make sure markdown's fully rendered.
        asst.bubble.innerHTML = renderMessageHtml(streamingText, currentSources);
      }
    }

    return reader.read().then(function pump(result) {
      if (result.done) {
        if (buffer.trim()) processEvent(buffer.trim());
        return { text: streamingText, sources: currentSources };
      }
      buffer += decoder.decode(result.value, { stream: true });
      var parts = buffer.split(/\n\n+/);
      buffer = parts.pop();
      for (var i = 0; i < parts.length; i++) processEvent(parts[i].trim());
      return reader.read().then(pump);
    });
  }

  // ─── Boot ───────────────────────────────────────────────────────────

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', mount);
  } else {
    mount();
  }
})();
