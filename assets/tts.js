// Shared TTS module — bilingual Web Speech default + HD via Gemini proxy.
//
// Drop-in script tag for any article page:
//   <script src="/assets/tts.js" defer></script>
//
// The page must contain:
//   * <div class="article-prose"> with <p>/<h2>/<h3>/<blockquote> children
//     using inner <span class="zh">…</span><span class="en">…</span> for the
//     two languages.
//   * (Optional) a <button id="tts-launch"> the user clicks to start playback.
//   * <html data-lang="zh"|"en"> attribute (toggled by the page's setLang()).
//
// On load this script idempotently injects:
//   * <style id="tts-injected-styles"> with the player + HD + toast CSS
//   * #tts-player floating bar (prev / play-pause / next / status / HD / stop)
//   * #tts-toast status bubble + #tts-audio HD audio element
//   * #tts-selection-popup "read from here" tooltip
//
// HD playback proxies through /api/tts (Vercel function calling Google
// Gemini Flash TTS). The API key lives only on the server.

(function () {
  'use strict';

  if (!('speechSynthesis' in window)) return;
  var prose = document.querySelector('.article-prose');
  if (!prose) return; // not an article page — skip everything

  // ══════════════════════════════════════════════════════
  // CSS
  // ══════════════════════════════════════════════════════
  function injectStyles() {
    if (document.getElementById('tts-injected-styles')) return;
    var css = `
/* Highlighted segment while reading */
.tts-current-segment {
  background: linear-gradient(90deg, rgba(212,175,90,0.18) 0%, rgba(212,175,90,0.08) 100%);
  border-left: 3px solid #b8952a;
  padding-left: 0.9rem !important;
  margin-left: -1.1rem !important;
  transition: background 0.3s, border-color 0.3s;
  border-radius: 0 4px 4px 0;
}
.article-prose blockquote.tts-current-segment {
  background: linear-gradient(135deg, rgba(212,175,90,0.18), #f2ece0);
}
/* Floating player */
#tts-player {
  position: fixed; bottom: 1.5rem; right: 1.5rem;
  background: #1a2744; color: white;
  border: 1px solid rgba(212,175,90,0.45);
  border-radius: 50px;
  padding: 0.45rem 0.5rem 0.45rem 1.1rem;
  display: flex; align-items: center; gap: 0.45rem;
  box-shadow: 0 8px 28px rgba(0,0,0,0.32);
  z-index: 998;
  font-family: 'Noto Sans TC', 'Noto Sans SC', sans-serif;
  transform: translateY(120%); opacity: 0;
  transition: transform 0.3s ease, opacity 0.3s ease;
}
#tts-player.tts-visible { transform: translateY(0); opacity: 1; }
.tts-status {
  font-size: 0.74rem; letter-spacing: 0.06em;
  color: rgba(255,255,255,0.7);
  padding: 0 0.3rem; min-width: 60px; text-align: center;
}
.tts-btn-icon {
  background: rgba(255,255,255,0.08); border: none; color: white;
  width: 34px; height: 34px; border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  cursor: pointer; font-size: 0.95rem;
  transition: background 0.18s;
}
.tts-btn-icon:hover { background: #b8952a; color: white; }
.tts-btn-icon.tts-main {
  background: #b8952a; width: 38px; height: 38px; font-size: 1rem;
}
.tts-btn-icon.tts-main:hover { background: #d4af5a; }
.tts-btn-icon.tts-stop:hover { background: #b03030; }
/* HD voice toggle (Gemini Flash TTS) */
.tts-btn-hd {
  width: auto; min-width: 38px;
  padding: 0 0.55rem; border-radius: 14px;
  font-size: 0.66rem; font-weight: 700; letter-spacing: 0.08em;
  font-family: 'Inter', sans-serif;
}
.tts-btn-hd.tts-hd-on {
  background: linear-gradient(135deg, #b8952a, #e6c378);
  color: white; box-shadow: 0 0 0 1px rgba(212,175,90,0.6) inset;
}
.tts-btn-hd.tts-hd-loading { background: rgba(212,175,90,0.45); color: white; cursor: wait; }
.tts-btn-hd.tts-hd-disabled { opacity: 0.35; cursor: not-allowed; }
.tts-btn-hd.tts-hd-disabled:hover { background: rgba(255,255,255,0.08); color: white; }
/* Toast under the player */
.tts-toast {
  position: fixed; bottom: 5rem; right: 1.5rem;
  background: #1a2744; color: white;
  border: 1px solid rgba(212,175,90,0.45);
  padding: 0.55rem 0.95rem; border-radius: 8px;
  font-size: 0.78rem;
  font-family: 'Noto Sans TC', 'Noto Sans SC', sans-serif;
  box-shadow: 0 6px 20px rgba(0,0,0,0.28);
  z-index: 999; max-width: 280px;
  opacity: 0; transform: translateY(8px);
  transition: opacity 0.2s, transform 0.2s;
  pointer-events: none;
}
.tts-toast.tts-toast-visible { opacity: 1; transform: translateY(0); }
@media (max-width: 768px) {
  #tts-player { bottom: 0.8rem; right: 0.8rem; left: 0.8rem; justify-content: center; border-radius: 50px; }
  .tts-toast { left: 0.8rem; right: 0.8rem; bottom: 4.5rem; max-width: none; }
}
/* Selection popup */
#tts-selection-popup {
  position: absolute;
  background: #1a2744; color: white;
  border: 1px solid #b8952a;
  border-radius: 8px; padding: 0.35rem 0.4rem;
  display: flex; align-items: center; gap: 0.35rem;
  box-shadow: 0 6px 18px rgba(0,0,0,0.28);
  z-index: 999;
  font-family: 'Noto Sans TC', 'Noto Sans SC', sans-serif;
  transform: translateY(-4px); opacity: 0;
  transition: transform 0.18s, opacity 0.18s;
  pointer-events: none;
}
#tts-selection-popup.tts-popup-visible {
  opacity: 1; transform: translateY(0); pointer-events: auto;
}
#tts-selection-popup::before {
  content: ''; position: absolute; top: -6px; left: 50%; transform: translateX(-50%);
  width: 0; height: 0;
  border-left: 6px solid transparent; border-right: 6px solid transparent;
  border-bottom: 6px solid #b8952a;
}
.tts-popup-btn {
  background: #b8952a; color: white; border: none;
  padding: 0.35rem 0.85rem; border-radius: 5px; cursor: pointer;
  font-family: 'Noto Sans TC', 'Noto Sans SC', sans-serif;
  font-size: 0.76rem; letter-spacing: 0.05em;
  display: flex; align-items: center; gap: 0.3rem;
  transition: background 0.15s; white-space: nowrap;
}
.tts-popup-btn:hover { background: #9b7d20; }

/* Settings (⚙) button + panel */
.tts-btn-settings { font-size: 1rem; }
#tts-settings {
  position: fixed; bottom: 5rem; right: 1.5rem;
  background: #1a2744; color: white;
  border: 1px solid rgba(212,175,90,0.45);
  border-radius: 14px;
  padding: 1rem 1rem 0.85rem;
  box-shadow: 0 12px 36px rgba(0,0,0,0.4);
  z-index: 999;
  font-family: 'Noto Sans TC', 'Noto Sans SC', sans-serif;
  font-size: 0.78rem;
  width: 320px;
  max-height: 70vh;
  overflow-y: auto;
  transform: translateY(8px);
  opacity: 0;
  pointer-events: none;
  transition: transform 0.18s, opacity 0.18s;
}
#tts-settings.tts-settings-visible {
  transform: translateY(0); opacity: 1; pointer-events: auto;
}
#tts-settings h4 {
  font-size: 0.7rem; font-weight: 600; letter-spacing: 0.1em;
  text-transform: uppercase;
  color: rgba(255,255,255,0.55);
  margin: 0.6rem 0 0.4rem;
}
#tts-settings h4:first-child { margin-top: 0; }
.tts-speed-row {
  display: flex; gap: 0.3rem; flex-wrap: wrap;
}
.tts-speed-btn {
  background: rgba(255,255,255,0.08);
  border: 1px solid transparent;
  color: white;
  padding: 0.3rem 0.55rem;
  border-radius: 6px; cursor: pointer;
  font-family: inherit; font-size: 0.74rem; font-weight: 600;
  transition: background 0.15s, border-color 0.15s;
  flex: 1 1 0; min-width: 0;
}
.tts-speed-btn:hover { background: rgba(212,175,90,0.25); }
.tts-speed-btn.tts-active {
  background: #b8952a; border-color: #d4af5a; color: white;
}
.tts-voice-section { margin-top: 0.2rem; }
.tts-voice-locale-group { margin-bottom: 0.4rem; }
.tts-voice-locale-label {
  font-size: 0.66rem; color: rgba(255,255,255,0.45);
  padding: 0.3rem 0 0.15rem 0.2rem;
  letter-spacing: 0.04em;
}
.tts-voice-row {
  display: flex; align-items: center; gap: 0.5rem;
  padding: 0.45rem 0.55rem;
  border-radius: 6px; cursor: pointer;
  transition: background 0.12s;
}
.tts-voice-row:hover { background: rgba(255,255,255,0.06); }
.tts-voice-row.tts-active {
  background: rgba(212,175,90,0.18);
  outline: 1px solid rgba(212,175,90,0.45);
}
.tts-voice-radio {
  width: 12px; height: 12px; border-radius: 50%;
  border: 1.5px solid rgba(255,255,255,0.4);
  flex-shrink: 0; position: relative;
}
.tts-voice-row.tts-active .tts-voice-radio {
  border-color: #d4af5a;
}
.tts-voice-row.tts-active .tts-voice-radio::after {
  content: ''; position: absolute; inset: 2px;
  background: #d4af5a; border-radius: 50%;
}
.tts-voice-name { flex: 1; font-size: 0.78rem; }
.tts-voice-gender {
  font-size: 0.7rem; color: rgba(255,255,255,0.55);
}
@media (max-width: 768px) {
  #tts-settings { left: 0.8rem; right: 0.8rem; bottom: 4.5rem; width: auto; }
}
`;
    var style = document.createElement('style');
    style.id = 'tts-injected-styles';
    style.textContent = css;
    document.head.appendChild(style);
  }
  injectStyles();

  // ══════════════════════════════════════════════════════
  // UI markup (idempotent)
  // ══════════════════════════════════════════════════════
  function injectMarkup() {
    var player = document.getElementById('tts-player');
    if (!player) {
      player = document.createElement('div');
      player.id = 'tts-player';
      player.setAttribute('role', 'region');
      player.setAttribute('aria-label', 'Article audio player');
      player.innerHTML =
        '<button id="tts-prev" class="tts-btn-icon" aria-label="Previous section" title="上一段 / Previous">⏮</button>' +
        '<button id="tts-play-pause" class="tts-btn-icon tts-main" aria-label="Play / Pause">⏸</button>' +
        '<button id="tts-next" class="tts-btn-icon" aria-label="Next section" title="下一段 / Next">⏭</button>' +
        '<span class="tts-status" id="tts-status">— / —</span>' +
        '<button id="tts-settings-btn" class="tts-btn-icon tts-btn-settings" aria-label="Voice & speed settings" title="語音與速度 / Voice & speed">⚙</button>' +
        '<button id="tts-stop" class="tts-btn-icon tts-stop" aria-label="Stop">✕</button>';
      document.body.appendChild(player);
    } else {
      // Existing player — make sure settings button is present (insert before stop)
      if (!document.getElementById('tts-settings-btn')) {
        var stopBtn = document.getElementById('tts-stop');
        var settingsBtn = document.createElement('button');
        settingsBtn.id = 'tts-settings-btn';
        settingsBtn.className = 'tts-btn-icon tts-btn-settings';
        settingsBtn.setAttribute('aria-label', 'Voice & speed settings');
        settingsBtn.title = '語音與速度 / Voice & speed';
        settingsBtn.textContent = '⚙';
        if (stopBtn) stopBtn.parentNode.insertBefore(settingsBtn, stopBtn);
        else player.appendChild(settingsBtn);
      }
      // Hide the legacy HD button if it exists from older markup — settings panel supersedes it
      var legacyHD = document.getElementById('tts-hd');
      if (legacyHD) legacyHD.style.display = 'none';
    }
    if (!document.getElementById('tts-settings')) {
      var panel = document.createElement('div');
      panel.id = 'tts-settings';
      panel.setAttribute('role', 'dialog');
      panel.setAttribute('aria-label', 'Voice and speed settings');
      panel.innerHTML =
        '<h4>速度 / Speed</h4>' +
        '<div class="tts-speed-row" id="tts-speed-row"></div>' +
        '<h4>語音 — 中文 / Chinese voice</h4>' +
        '<div class="tts-voice-section" id="tts-voice-section-zh">Loading…</div>' +
        '<h4>語音 — English voice</h4>' +
        '<div class="tts-voice-section" id="tts-voice-section-en">Loading…</div>';
      document.body.appendChild(panel);
    }
    if (!document.getElementById('tts-toast')) {
      var toast = document.createElement('div');
      toast.id = 'tts-toast';
      toast.className = 'tts-toast';
      toast.setAttribute('role', 'status');
      toast.setAttribute('aria-live', 'polite');
      document.body.appendChild(toast);
    }
    if (!document.getElementById('tts-audio')) {
      var audio = document.createElement('audio');
      audio.id = 'tts-audio';
      audio.preload = 'auto';
      // iOS Safari refuses to play unless the element exists in the DOM
      // BEFORE the user gesture, has playsinline (else it tries fullscreen),
      // and uses crossorigin=anonymous so blob: URLs work.
      audio.setAttribute('playsinline', '');
      audio.setAttribute('webkit-playsinline', '');
      audio.crossOrigin = 'anonymous';
      audio.style.display = 'none';
      document.body.appendChild(audio);
    }
    if (!document.getElementById('tts-selection-popup')) {
      var popup = document.createElement('div');
      popup.id = 'tts-selection-popup';
      popup.setAttribute('role', 'tooltip');
      popup.innerHTML = '<button id="tts-selection-play" class="tts-popup-btn">▶ <span class="zh">从这里开始</span><span class="en">Start from here</span></button>';
      document.body.appendChild(popup);
    }
  }
  injectMarkup();

  // ══════════════════════════════════════════════════════
  // Behaviour
  // ══════════════════════════════════════════════════════
  var synth = window.speechSynthesis;
  // Descendant selector — matches segments at any depth, so wrappers like
  // <div class="lesson-block"> don't hide content from the narrator.
  var SEGMENT_SELECTOR = 'p, h2, h3, blockquote';
  function getSegments() { return Array.from(prose.querySelectorAll(SEGMENT_SELECTOR)); }
  var segments = getSegments();

  // UI handles
  var player       = document.getElementById('tts-player');
  var btnLaunch    = document.getElementById('tts-launch'); // optional, on the page
  var btnPlayPause = document.getElementById('tts-play-pause');
  var btnPrev      = document.getElementById('tts-prev');
  var btnNext      = document.getElementById('tts-next');
  var btnStop      = document.getElementById('tts-stop');
  var btnHD        = document.getElementById('tts-hd');
  var statusEl     = document.getElementById('tts-status');
  var popup        = document.getElementById('tts-selection-popup');
  var btnSelPlay   = document.getElementById('tts-selection-play');
  var toastEl      = document.getElementById('tts-toast');
  var audioEl      = document.getElementById('tts-audio');

  // Core playback state
  var currentIndex     = -1;
  var isPlaying        = false;
  var isPaused         = false;
  var currentUtterance = null;
  var keepAliveTimer   = null;
  var pendingSelIndex  = -1;
  var activeBackend    = null; // 'webspeech' | 'hd' | null
  var playToken        = 0;

  // HD (Gemini) state
  var hdEnabled    = false;
  var hdAvailable  = true;
  var hdProbing    = false;
  var hdReady      = false;
  var TTS_ENDPOINT = '/api/tts';
  var GEMINI_VOICE = { zh: 'Kore', en: 'Aoede' };
  var hdCache      = new Map(); // "lang:idx" -> { url, blob }
  var HD_CACHE_MAX = 8;
  var toastTimer   = null;

  // Pre-rendered static audio (Edge TTS, served from /assets/audio/<slug>/).
  // Loaded lazily once on first playback. If a manifest exists for this page
  // we use it as the *default* — much higher quality than Web Speech, no
  // network synthesis cost, instant on iPhone, fully offline-cacheable.
  var staticManifest = null;        // null until probed; false if no manifest
  var staticManifestPromise = null; // in-flight probe

  // ── User settings (persisted) ──────────────────────────
  // Voice + speed survive page navigation via localStorage.
  var EDGE_PROXY  = '/api/edge-tts';
  var DEFAULT_PLAYBACK_RATE = 1.0;
  var SPEEDS = [0.75, 1.0, 1.25, 1.5, 1.75, 2.0];

  var voicesCatalog = null;          // loaded from /assets/voices.json
  var voicesPromise = null;
  var settings = {
    speed:   DEFAULT_PLAYBACK_RATE,
    voiceZh: null,                   // null means "use catalog default"
    voiceEn: null,
  };
  try {
    var raw = localStorage.getItem('tts-settings');
    if (raw) {
      var parsed = JSON.parse(raw);
      if (typeof parsed.speed === 'number' && SPEEDS.indexOf(parsed.speed) >= 0) settings.speed = parsed.speed;
      if (typeof parsed.voiceZh === 'string') settings.voiceZh = parsed.voiceZh;
      if (typeof parsed.voiceEn === 'string') settings.voiceEn = parsed.voiceEn;
    }
  } catch (e) {}
  function persistSettings() {
    try { localStorage.setItem('tts-settings', JSON.stringify(settings)); } catch (e) {}
  }

  // Live edge-tts proxy cache: "voice:rate:lang:idx" -> blobUrl
  var edgeCache = new Map();
  var EDGE_CACHE_MAX = 8;
  var audioUnlocked = false;     // iOS audio is locked until first user-gesture play()

  // 1-byte silent WAV — the smallest valid file we can use to "warm up"
  // the <audio> element inside a user-gesture callback so iOS Safari will
  // let us call .play() later from an async callback.
  var SILENT_WAV_DATA_URL =
    'data:audio/wav;base64,UklGRkQAAABXQVZFZm10IBAAAAABAAEARKwAAIhYAQACABAAZGF0YSAAAAAAAA' +
    'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA';

  function getLang() { return document.documentElement.getAttribute('data-lang') || 'zh'; }

  // Derive an audio slug from the page URL.
  //   /article-messiah-birthing-iran        -> 'article-messiah-birthing-iran'
  //   /article-messiah-birthing-iran.html   -> 'article-messiah-birthing-iran'
  //   /                                     -> 'index'
  function getSlug() {
    var meta = document.querySelector('meta[name="audio-slug"]');
    if (meta && meta.content) return meta.content;
    var p = location.pathname.replace(/^\/+|\/+$/g, '').replace(/\.html?$/i, '');
    return p || 'index';
  }

  function loadStaticManifest() {
    if (staticManifest !== null) return Promise.resolve(staticManifest);
    if (staticManifestPromise) return staticManifestPromise;
    var url = '/assets/audio/' + getSlug() + '/manifest.json';
    staticManifestPromise = fetch(url, { cache: 'force-cache' })
      .then(function (r) { return r.ok ? r.json() : false; })
      .then(function (m) { staticManifest = m || false; return staticManifest; })
      .catch(function () { staticManifest = false; return false; });
    return staticManifestPromise;
  }
  // Per-voice URL: assets/audio/<slug>/<lang>/<voiceId>/<idx>.mp3.
  // Falls back to default voice in this language if voice id isn't pre-rendered.
  function staticUrlFor(index, lang, voiceId) {
    if (!staticManifest || !staticManifest[lang]) return null;
    if (index < 0 || index >= staticManifest[lang].count) return null;
    // New manifest (multi-voice): per-voice subfolders, listed in `voices`.
    var voices = staticManifest[lang].voices;
    if (Array.isArray(voices) && voices.length) {
      var match = voices.find(function (v) { return v.id === voiceId; });
      if (!match) match = voices.find(function (v) { return v.id === staticManifest[lang].default; });
      if (!match) match = voices[0];
      return '/assets/audio/' + getSlug() + '/' + lang + '/' + match.id + '/' + index + '.mp3';
    }
    // Old manifest (single voice, flat layout) — falls through gracefully so
    // any cached older HTML still gets audio without 404ing on a missing file.
    return '/assets/audio/' + getSlug() + '/' + lang + '/' + index + '.mp3';
  }
  function shouldUseStatic(lang) {
    return !!(staticManifest && staticManifest[lang] && staticManifest[lang].count > 0);
  }
  function manifestVoicesFor(lang) {
    if (!staticManifest || !staticManifest[lang] || !staticManifest[lang].voices) return [];
    return staticManifest[lang].voices;
  }
  function manifestDefault(lang) {
    return staticManifest && staticManifest[lang] && staticManifest[lang].default;
  }

  // Must be invoked synchronously inside a user-gesture handler.
  // After this runs successfully, audioEl.play() works from any async context
  // for the rest of the page session — that's how iOS Safari treats it.
  function unlockAudio() {
    if (audioUnlocked || !audioEl) return;
    try {
      audioEl.muted = true;            // play() succeeds even on locked iOS when muted
      audioEl.src   = SILENT_WAV_DATA_URL;
      var p = audioEl.play();
      if (p && typeof p.then === 'function') {
        p.then(function () {
          try { audioEl.pause(); } catch (e) {}
          try { audioEl.currentTime = 0; } catch (e) {}
          audioEl.muted = false;
          audioUnlocked = true;
        }).catch(function () {
          // Even if the silent prime failed, mark unlocked so we don't keep retrying
          audioEl.muted = false;
          audioUnlocked = true;
        });
      } else {
        audioEl.muted = false;
        audioUnlocked = true;
      }
    } catch (e) {
      audioEl.muted = false;
      audioUnlocked = true;
    }
  }

  function getVoiceForLang(lang) {
    var voices = synth.getVoices();
    if (!voices.length) return null;
    var prefer = lang === 'zh'
      ? ['zh-tw', 'zh-hk', 'cmn-hant-tw', 'zh-cn', 'cmn-hans-cn', 'zh']
      : ['en-us', 'en-gb', 'en-au', 'en'];
    for (var i = 0; i < prefer.length; i++) {
      var p = prefer[i];
      var exact = voices.find(function (v) { return v.lang.toLowerCase() === p; });
      if (exact) return exact;
      var prefix = voices.find(function (v) { return v.lang.toLowerCase().indexOf(p) === 0; });
      if (prefix) return prefix;
    }
    return voices[0] || null;
  }

  function getSegmentText(seg, lang) {
    var span = seg.querySelector('span.' + lang);
    var text = span ? span.textContent : seg.textContent;
    return text.replace(/\s+/g, ' ').trim();
  }

  // Length under the same whitespace-collapsing rule used by getSegmentText —
  // so an offset we compute here matches the offset inside the audio's text.
  function normalizedLen(s) { return s.replace(/\s+/g, ' ').replace(/^\s+/, '').length; }

  // Cross-browser caret-from-point. Safari & Chrome ship caretRangeFromPoint;
  // Firefox ships caretPositionFromPoint; we wrap whichever exists.
  function caretRangeAt(x, y) {
    if (document.caretRangeFromPoint) return document.caretRangeFromPoint(x, y);
    if (document.caretPositionFromPoint) {
      var p = document.caretPositionFromPoint(x, y);
      if (!p) return null;
      var r = document.createRange();
      r.setStart(p.offsetNode, p.offset);
      r.setEnd(p.offsetNode, p.offset);
      return r;
    }
    return null;
  }

  // Char offset within the segment's audio-text where a Range begins.
  // Works for both a tap (caret range, collapsed) and a real selection.
  function offsetFromRange(seg, lang, range) {
    if (!range) return 0;
    var span = seg.querySelector('span.' + lang) || seg;
    var startNode   = range.startContainer;
    var startOffset = range.startOffset;
    if (!span.contains(startNode)) {
      // Range starts outside the visible-language span; if the END is inside, use that.
      if (!span.contains(range.endContainer)) return 0;
      startNode = range.endContainer;
      startOffset = range.endOffset;
    }
    var prefix = document.createRange();
    prefix.setStart(span, 0);
    prefix.setEnd(startNode, startOffset);
    return normalizedLen(prefix.toString());
  }

  // Round a tap offset back to the start of the word it landed in.
  // - Whitespace boundary for Latin scripts (English, transliterated Hebrew, etc.)
  // - Exact char for CJK / Hebrew / Arabic where every char is its own "word"
  function roundToWordStart(text, offset) {
    if (offset <= 0) return 0;
    if (offset > text.length) offset = text.length;
    // Walk back to nearest whitespace.
    var i = offset;
    while (i > 0 && !/\s/.test(text.charAt(i - 1))) i--;
    if (i > 0) return i;
    // No whitespace before the offset — for CJK / Hebrew / Arabic / Japanese kana,
    // every character is a word, so use the tap offset directly. For Latin with
    // no leading whitespace, fall back to start of paragraph.
    var ch = text.charAt(offset > 0 ? offset - 1 : 0);
    if (/[㐀-鿿぀-ヿ֐-׿؀-ۿ]/.test(ch)) return offset;
    return 0;
  }

  function setStatus(t) { if (statusEl) statusEl.textContent = t; }
  function updateStatus() {
    var total = segments.length;
    setStatus(currentIndex < 0 ? '— / ' + total : (currentIndex + 1) + ' / ' + total);
  }
  function setPlayPauseIcon(playing) {
    if (!btnPlayPause) return;
    btnPlayPause.textContent = playing ? '⏸' : '▶';
    btnPlayPause.setAttribute('aria-label', playing ? 'Pause' : 'Play');
  }
  function clearHighlight() {
    var prev = prose.querySelector('.tts-current-segment');
    if (prev) prev.classList.remove('tts-current-segment');
  }
  function highlight(index) {
    clearHighlight();
    if (index < 0 || index >= segments.length) return;
    var el = segments[index];
    el.classList.add('tts-current-segment');
    var rect = el.getBoundingClientRect();
    var winH = window.innerHeight || document.documentElement.clientHeight;
    if (rect.top < 80 || rect.bottom > winH - 120) {
      el.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }
  }
  function showPlayer() { if (player) player.classList.add('tts-visible'); }
  function hidePlayer() { if (player) player.classList.remove('tts-visible'); }

  function startKeepAlive() {
    stopKeepAlive();
    keepAliveTimer = setInterval(function () {
      if (synth.speaking && !synth.paused) { synth.pause(); synth.resume(); }
    }, 10000);
  }
  function stopKeepAlive() {
    if (keepAliveTimer) { clearInterval(keepAliveTimer); keepAliveTimer = null; }
  }

  // ── HD UI helpers + probe ─────────────────────────────
  function showToast(msg, ms) {
    if (!toastEl) return;
    toastEl.textContent = msg;
    toastEl.classList.add('tts-toast-visible');
    if (toastTimer) { clearTimeout(toastTimer); toastTimer = null; }
    if (ms) toastTimer = setTimeout(function () { toastEl.classList.remove('tts-toast-visible'); }, ms);
  }
  function setHDState(state, label) {
    if (!btnHD) return;
    btnHD.classList.remove('tts-hd-on', 'tts-hd-loading', 'tts-hd-disabled');
    btnHD.textContent = label || 'HD';
    if (state === 'on') btnHD.classList.add('tts-hd-on');
    else if (state === 'loading') btnHD.classList.add('tts-hd-loading');
    else if (state === 'disabled') btnHD.classList.add('tts-hd-disabled');
  }
  function refreshHDButtonForLang() {
    if (!btnHD) return;
    if (!hdAvailable) { setHDState('disabled'); btnHD.title = 'HD 語音無法使用 / HD voice unavailable'; return; }
    btnHD.title = 'HD voice — Google Gemini Flash TTS · 中文 + English';
    if (hdProbing) setHDState('loading');
    else if (hdEnabled && hdReady) setHDState('on');
    else setHDState('off');
  }
  function probeHD() {
    if (hdReady)   return Promise.resolve(true);
    if (hdProbing) return hdProbing;
    setHDState('loading');
    showToast('正在連線 HD 語音 (Gemini)... / Connecting HD voice (Gemini)...');

    // 12 s timeout — Gemini cold-start + free-tier 429 wait can take a while.
    var ctrl = (typeof AbortController !== 'undefined') ? new AbortController() : null;
    var timer = setTimeout(function () { if (ctrl) ctrl.abort(); }, 12000);

    hdProbing = fetch(TTS_ENDPOINT, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text: '你好', lang: 'zh', voice: GEMINI_VOICE.zh }),
      signal: ctrl ? ctrl.signal : undefined,
    }).then(function (r) {
      clearTimeout(timer);
      hdProbing = false;
      if (!r.ok) return r.text().then(function (t) { throw new Error('HTTP ' + r.status + ': ' + t.slice(0, 200)); });
      hdReady = true;
      setHDState(hdEnabled ? 'on' : 'off');
      showToast('✓ HD 語音已就緒 (Gemini Kore) / HD voice ready', 2400);
      return true;
    }).catch(function (err) {
      clearTimeout(timer);
      console.error('[HD] probe failed:', err);
      hdProbing = false; hdAvailable = false; hdEnabled = false;
      setHDState('disabled');
      var reason = String(err && err.message || err).slice(0, 90);
      // Common cases get friendlier messages
      if (/abort|timeout/i.test(reason))           reason = 'timeout (12s)';
      else if (/429/.test(reason))                 reason = 'rate limit (free tier 10/min)';
      else if (/Failed to fetch|NetworkError/i.test(reason)) reason = 'network blocked';
      showToast('✕ HD 失敗 (' + reason + ') — 使用系統語音 / HD failed — using system voice', 4500);
      throw err;
    });
    return hdProbing;
  }
  function shouldUseHD() { return hdEnabled && hdReady && hdAvailable; }

  function hdCacheKey(i, lang) { return lang + ':' + i; }
  async function hdAudioFor(index, lang) {
    var key = hdCacheKey(index, lang);
    if (hdCache.has(key)) return hdCache.get(key).url;
    segments = getSegments();
    if (index < 0 || index >= segments.length) return null;
    var text = getSegmentText(segments[index], lang);
    if (!text) return null;
    var resp = await fetch(TTS_ENDPOINT, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text: text, lang: lang, voice: GEMINI_VOICE[lang] })
    });
    if (!resp.ok) {
      var detail = await resp.text();
      throw new Error('tts ' + resp.status + ': ' + detail.slice(0, 200));
    }
    var blob = await resp.blob();
    var url  = URL.createObjectURL(blob);
    hdCache.set(key, { url: url, blob: blob });
    while (hdCache.size > HD_CACHE_MAX) {
      var oldestKey = hdCache.keys().next().value;
      var oldest = hdCache.get(oldestKey);
      try { URL.revokeObjectURL(oldest.url); } catch (e) {}
      hdCache.delete(oldestKey);
    }
    return url;
  }
  function clearHDCache() {
    hdCache.forEach(function (v) { try { URL.revokeObjectURL(v.url); } catch (e) {} });
    hdCache.clear();
  }

  // ── Voice + speed settings ────────────────────────────
  // The voice catalog now comes directly from the article's audio manifest
  // (so the picker only ever shows voices that are actually pre-rendered for
  // this page — no broken options). Loading a manifest is already handled by
  // loadStaticManifest() below.
  function getDefaultVoice(lang) { return manifestDefault(lang); }
  function getActiveVoice(lang) {
    var picked = lang === 'zh' ? settings.voiceZh : settings.voiceEn;
    var available = manifestVoicesFor(lang).map(function (v) { return v.id; });
    if (picked && available.indexOf(picked) >= 0) return picked;
    return getDefaultVoice(lang);
  }
  function rateAsPercent() {
    // edge-tts rate format: "+25%", "-10%". audio.playbackRate 1.5 ⇒ +50%.
    var pct = Math.round((settings.speed - 1) * 100);
    return (pct >= 0 ? '+' : '') + pct + '%';
  }

  function applySpeed() {
    if (audioEl) {
      try { audioEl.preservesPitch = true; } catch (e) {}
      try { audioEl.mozPreservesPitch = true; } catch (e) {}
      audioEl.playbackRate = settings.speed;
    }
    // Web Speech path doesn't run after switching mid-utterance, but keep current
    // utterance in sync where possible.
    if (currentUtterance) {
      try { currentUtterance.rate = Math.max(0.1, Math.min(10, settings.speed)); } catch (e) {}
    }
  }

  function renderSettingsPanel() {
    var speedRow = document.getElementById('tts-speed-row');
    if (speedRow) {
      speedRow.innerHTML = '';
      SPEEDS.forEach(function (s) {
        var btn = document.createElement('button');
        btn.type = 'button';
        btn.className = 'tts-speed-btn' + (s === settings.speed ? ' tts-active' : '');
        btn.textContent = (s === 1 ? '1×' : s + '×');
        btn.addEventListener('click', function () {
          settings.speed = s;
          persistSettings();
          renderSettingsPanel();
          applySpeed();
        });
        speedRow.appendChild(btn);
      });
    }

    if (!staticManifest) return;

    function renderVoiceList(containerId, langKey) {
      var container = document.getElementById(containerId);
      if (!container) return;
      container.innerHTML = '';
      var voicesList = manifestVoicesFor(langKey);
      if (!voicesList.length) {
        container.innerHTML = '<div class="tts-voice-locale-label">(no pre-rendered voices)</div>';
        return;
      }
      var defaultId = getDefaultVoice(langKey);
      var activeId  = getActiveVoice(langKey);

      // Sub-group by locale label so picker is scannable
      var byLocale = {};
      var localeOrder = [];
      voicesList.forEach(function (v) {
        if (!byLocale[v.locale]) { byLocale[v.locale] = { label: v.localeLabel, voices: [] }; localeOrder.push(v.locale); }
        byLocale[v.locale].voices.push(v);
      });

      localeOrder.forEach(function (loc) {
        var grp = document.createElement('div');
        grp.className = 'tts-voice-locale-group';
        var lbl = document.createElement('div');
        lbl.className = 'tts-voice-locale-label';
        lbl.textContent = byLocale[loc].label;
        grp.appendChild(lbl);
        byLocale[loc].voices.forEach(function (v) {
          var row = document.createElement('div');
          row.className = 'tts-voice-row' + (v.id === activeId ? ' tts-active' : '');
          row.setAttribute('role', 'radio');
          row.setAttribute('aria-checked', v.id === activeId ? 'true' : 'false');
          row.tabIndex = 0;
          row.innerHTML =
            '<span class="tts-voice-radio"></span>' +
            '<span class="tts-voice-name">' + v.name + (v.id === defaultId ? ' <span style="color:rgba(212,175,90,0.85);font-size:0.7rem">· default</span>' : '') + '</span>' +
            '<span class="tts-voice-gender">' + (v.gender === 'Female' ? '♀' : '♂') + '</span>';
          var pick = function () {
            if (langKey === 'zh') settings.voiceZh = v.id;
            else                  settings.voiceEn = v.id;
            persistSettings();
            renderSettingsPanel();
            // If we're currently playing in this language, restart current segment with the new voice.
            if (isPlaying && getLang() === langKey) {
              var idx = currentIndex;
              playToken++;
              synth.cancel(); if (audioEl) { try { audioEl.pause(); } catch (e) {} }
              setTimeout(function () { speakSegment(idx); }, 80);
            }
          };
          row.addEventListener('click', pick);
          row.addEventListener('keydown', function (e) {
            if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); pick(); }
          });
          grp.appendChild(row);
        });
        container.appendChild(grp);
      });
    }
    renderVoiceList('tts-voice-section-zh', 'zh');
    renderVoiceList('tts-voice-section-en', 'en');
  }

  function openSettings() {
    loadStaticManifest().then(renderSettingsPanel);
    var panel = document.getElementById('tts-settings');
    if (panel) panel.classList.add('tts-settings-visible');
  }
  function closeSettings() {
    var panel = document.getElementById('tts-settings');
    if (panel) panel.classList.remove('tts-settings-visible');
  }
  function toggleSettings() {
    var panel = document.getElementById('tts-settings');
    if (!panel) return;
    if (panel.classList.contains('tts-settings-visible')) closeSettings();
    else openSettings();
  }

  // ── Edge-TTS live proxy (for non-default voices) ──────
  function edgeCacheKey(voice, rate, lang, idx) { return voice + '|' + rate + '|' + lang + ':' + idx; }
  async function edgeAudioFor(index, lang, voice) {
    var rate = rateAsPercent();
    var key  = edgeCacheKey(voice, rate, lang, index);
    if (edgeCache.has(key)) return edgeCache.get(key);
    segments = getSegments();
    if (index < 0 || index >= segments.length) return null;
    var text = getSegmentText(segments[index], lang);
    if (!text) return null;
    var resp = await fetch(EDGE_PROXY, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text: text, voice: voice, rate: '+0%' }),  // speed is applied client-side via playbackRate
    });
    if (!resp.ok) {
      var detail = await resp.text();
      throw new Error('edge ' + resp.status + ': ' + detail.slice(0, 200));
    }
    var blob = await resp.blob();
    var url  = URL.createObjectURL(blob);
    edgeCache.set(key, url);
    while (edgeCache.size > EDGE_CACHE_MAX) {
      var oldKey = edgeCache.keys().next().value;
      try { URL.revokeObjectURL(edgeCache.get(oldKey)); } catch (e) {}
      edgeCache.delete(oldKey);
    }
    return url;
  }
  function clearEdgeCache() {
    edgeCache.forEach(function (u) { try { URL.revokeObjectURL(u); } catch (e) {} });
    edgeCache.clear();
  }

  function speakViaEdgeProxy(index, lang, voice) {
    activeBackend = 'hd';
    var token = ++playToken;
    synth.cancel(); stopKeepAlive();
    isPlaying = true; isPaused = false;
    setPlayPauseIcon(true); showPlayer();
    setStatus('… ' + (index + 1) + ' / ' + segments.length);
    edgeAudioFor(index, lang, voice).then(function (url) {
      if (token !== playToken) return;
      if (!url) { speakViaWebSpeech(index, getSegmentText(segments[index], lang), lang); return; }
      audioEl.src = url;
      applySpeed();
      var p = audioEl.play();
      if (p && p.catch) p.catch(function (e) { console.warn('[edge] play failed:', e); });
      updateStatus();
      if (index + 1 < segments.length) edgeAudioFor(index + 1, lang, voice).catch(function () {});
    }).catch(function (err) {
      if (token !== playToken) return;
      console.warn('[edge] failed:', err);
      showToast('語音合成失敗 — 切回系統語音 / Voice failed — fallback to system voice', 3000);
      speakViaWebSpeech(index, getSegmentText(segments[index], lang), lang);
    });
  }

  // ── Speaker dispatch ──────────────────────────────────
  // Priority:
  //   1. Pre-rendered static MP3 (Edge TTS) — best quality, instant, free
  //   2. HD button enabled? → live Gemini synthesis
  //   3. Web Speech (OS voice)
  function speakSegment(index) {
    segments = getSegments();
    if (index < 0 || index >= segments.length) { stop(); return; }
    var lang = getLang();
    var text = getSegmentText(segments[index], lang);
    if (!text) {
      currentIndex = index;
      if (index + 1 < segments.length) speakSegment(index + 1); else stop();
      return;
    }
    currentIndex = index;
    highlight(index);
    updateStatus();

    // Pre-rendered static MP3s for this article (multiple voices per language).
    // The picker only shows voices that are pre-rendered, so any choice the
    // user makes resolves to a valid static URL. Microsoft blocks Chinese
    // text from anonymous Vercel IPs, so live edge-tts is no longer wired
    // here — pre-rendering at build-time is the reliable path.
    loadStaticManifest().then(function () {
      var chosen = getActiveVoice(lang);
      if (chosen && shouldUseStatic(lang)) {
        var url = staticUrlFor(index, lang, chosen);
        if (url) { speakViaStatic(index, url, lang); return; }
      }
      // Last-resort fallbacks: legacy HD (Gemini), then OS Web Speech.
      if (shouldUseHD()) { speakViaHD(index, text, lang); return; }
      speakViaWebSpeech(index, text, lang);
    });
  }

  // Mid-paragraph entry point. The pre-rendered MP3 is paragraph-level (no
  // word-timestamps to seek into), so for a non-zero offset we synthesize the
  // truncated tail live. When this segment ends, the existing onend chain
  // moves to the next FULL segment normally — so only the first segment
  // after a tap loses the static-MP3 quality.
  function speakFromOffset(index, charOffset) {
    segments = getSegments();
    if (index < 0 || index >= segments.length) { stop(); return; }
    if (!charOffset || charOffset <= 0) { speakSegment(index); return; }
    var lang = getLang();
    var fullText = getSegmentText(segments[index], lang);
    if (!fullText) {
      if (index + 1 < segments.length) speakSegment(index + 1); else stop();
      return;
    }
    var tail = fullText.slice(charOffset).replace(/^\s+/, '');
    if (!tail) {
      if (index + 1 < segments.length) speakSegment(index + 1); else stop();
      return;
    }
    currentIndex = index;
    highlight(index);
    updateStatus();
    if (shouldUseHD()) { speakViaHD(index, tail, lang); return; }
    speakViaWebSpeech(index, tail, lang);
  }

  // Direct <audio src="…mp3"> playback. Same plumbing as HD (uses audioEl) but
  // no fetch round-trip — the URL is a static file Vercel serves with edge
  // caching, so playback starts in <50 ms even on iPhone.
  function speakViaStatic(index, url, lang) {
    activeBackend = 'hd';                    // reuse the audio-element backend state
    var token = ++playToken;
    synth.cancel(); stopKeepAlive();
    isPlaying = true; isPaused = false;
    setPlayPauseIcon(true); showPlayer();
    if (audioEl) {
      audioEl.src = url;
      applySpeed();                          // playbackRate must be set after src
      var p = audioEl.play();
      if (p && p.catch) p.catch(function (e) {
        console.warn('[static] play failed, falling back:', e);
        if (token === playToken) speakViaWebSpeech(index, getSegmentText(segments[index], lang), lang);
      });
    }
    updateStatus();
  }

  function speakViaWebSpeech(index, text, lang) {
    activeBackend = 'webspeech';
    var token = ++playToken;
    if (audioEl) { audioEl.pause(); }
    synth.cancel();
    if (synth.paused) synth.resume();
    var utter = new SpeechSynthesisUtterance(text);
    var voice = getVoiceForLang(lang);
    if (voice) { utter.voice = voice; utter.lang = voice.lang; }
    else utter.lang = lang === 'zh' ? 'zh-TW' : 'en-US';
    utter.rate = Math.max(0.1, Math.min(10, settings.speed));
    utter.pitch = 1.0; utter.volume = 1.0;
    utter.onend = function () {
      if (token !== playToken) return;
      if (currentUtterance !== utter) return;
      if (!isPlaying || isPaused) return;
      if (currentIndex + 1 < segments.length) speakSegment(currentIndex + 1); else stop();
    };
    utter.onerror = function (e) {
      if (e.error === 'interrupted' || e.error === 'canceled') return;
      console.warn('[TTS] webspeech error:', e.error);
    };
    currentUtterance = utter;
    isPlaying = true; isPaused = false;
    setPlayPauseIcon(true); showPlayer(); startKeepAlive();
    setTimeout(function () {
      if (token !== playToken) return;
      try { synth.speak(utter); } catch (err) { console.warn('[TTS] speak failed:', err); }
    }, 60);
  }

  function speakViaHD(index, text, lang) {
    activeBackend = 'hd';
    var token = ++playToken;
    synth.cancel(); stopKeepAlive();
    isPlaying = true; isPaused = false;
    setPlayPauseIcon(true); showPlayer();
    setStatus('… ' + (index + 1) + ' / ' + segments.length);
    hdAudioFor(index, lang).then(function (url) {
      if (token !== playToken) return;
      if (!url) { speakViaWebSpeech(index, text, lang); return; }
      audioEl.src = url;
      var p = audioEl.play();
      if (p && p.catch) p.catch(function (e) { console.warn('[audio] play failed:', e); });
      updateStatus();
      if (index + 1 < segments.length) hdAudioFor(index + 1, lang).catch(function () {});
    }).catch(function (err) {
      if (token !== playToken) return;
      console.warn('[HD] synth failed, falling back to system voice:', err);
      showToast('HD 語音失敗 — 切回系統語音 / HD failed — switched to system voice', 2800);
      hdEnabled = false; setHDState('off');
      speakViaWebSpeech(index, text, lang);
    });
  }

  // Audio element drives HD playback transitions
  if (audioEl) {
    audioEl.addEventListener('ended', function () {
      if (activeBackend !== 'hd') return;
      if (!isPlaying || isPaused) return;
      if (currentIndex + 1 < segments.length) speakSegment(currentIndex + 1); else stop();
    });
    audioEl.addEventListener('play', function () {
      if (activeBackend !== 'hd') return;
      isPaused = false; setPlayPauseIcon(true);
    });
    audioEl.addEventListener('pause', function () {
      if (activeBackend !== 'hd') return;
      if (audioEl.ended) return;
      if (isPlaying) { isPaused = true; setPlayPauseIcon(false); }
    });
    audioEl.addEventListener('error', function () {
      if (activeBackend !== 'hd') return;
      console.warn('[audio] element error', audioEl.error);
    });
  }

  function play() {
    if (isPaused) {
      if (activeBackend === 'webspeech') { synth.resume(); startKeepAlive(); }
      else if (activeBackend === 'hd' && audioEl) {
        var p = audioEl.play(); if (p && p.catch) p.catch(function () {});
      }
      isPaused = false; setPlayPauseIcon(true);
    } else if (!isPlaying) {
      var startAt = currentIndex < 0 ? 0 : currentIndex;
      speakSegment(startAt);
    }
  }
  function pause() {
    if (!isPlaying || isPaused) return;
    if (activeBackend === 'webspeech') { synth.pause(); stopKeepAlive(); }
    else if (activeBackend === 'hd' && audioEl) audioEl.pause();
    isPaused = true; setPlayPauseIcon(false);
  }
  function togglePlayPause() { if (isPlaying && !isPaused) pause(); else play(); }
  function next() { if (currentIndex + 1 < segments.length) speakSegment(currentIndex + 1); }
  function prev() { if (currentIndex > 0) speakSegment(currentIndex - 1); else if (segments.length) speakSegment(0); }
  function stop() {
    playToken++;
    synth.cancel(); stopKeepAlive();
    if (audioEl) {
      try { audioEl.pause(); } catch (e) {}
      try { audioEl.removeAttribute('src'); audioEl.load(); } catch (e) {}
    }
    clearHDCache();
    clearEdgeCache();
    isPlaying = false; isPaused = false;
    currentUtterance = null; currentIndex = -1; activeBackend = null;
    clearHighlight(); updateStatus(); setPlayPauseIcon(true); hidePlayer();
    closeSettings();
  }

  // HD button toggle
  function toggleHD() {
    // CRITICAL for iOS: must be called synchronously inside the user-gesture
    // handler so the audio element is "unlocked" for later async play().
    unlockAudio();

    if (!hdAvailable || hdProbing) return;
    if (!hdReady) {
      hdEnabled = true;
      setHDState('loading');                    // immediate visual feedback
      probeHD().then(function () {
        if (isPlaying) {
          var idx = currentIndex; playToken++;
          synth.cancel(); if (audioEl) { try { audioEl.pause(); } catch (e) {} }
          setTimeout(function () { speakSegment(idx); }, 80);
        }
      }).catch(function () {});
      return;
    }
    hdEnabled = !hdEnabled;
    setHDState(hdEnabled ? 'on' : 'off');
    showToast(hdEnabled ? 'HD ON (Gemini)' : 'HD OFF (system voice)', 1800);
    if (isPlaying) {
      var idx = currentIndex; playToken++;
      synth.cancel(); if (audioEl) { try { audioEl.pause(); } catch (e) {} }
      setTimeout(function () { speakSegment(idx); }, 80);
    }
  }
  if (btnHD) btnHD.addEventListener('click', toggleHD);

  // Settings (⚙) button + outside-click close
  var btnSettings = document.getElementById('tts-settings-btn');
  var settingsPanel = document.getElementById('tts-settings');
  if (btnSettings) {
    btnSettings.addEventListener('click', function (e) {
      e.stopPropagation();
      unlockAudio();          // priming the audio element while we have a user gesture
      toggleSettings();
    });
  }
  document.addEventListener('click', function (e) {
    if (!settingsPanel || !settingsPanel.classList.contains('tts-settings-visible')) return;
    if (settingsPanel.contains(e.target) || (btnSettings && btnSettings.contains(e.target))) return;
    closeSettings();
  });
  // Pre-fetch the audio manifest so the picker opens without a flash.
  loadStaticManifest();

  // React to <html data-lang> changes from setLang()
  new MutationObserver(refreshHDButtonForLang)
    .observe(document.documentElement, { attributes: true, attributeFilter: ['data-lang'] });
  refreshHDButtonForLang();

  // Expose stop for setLang()
  window.__ttsStop = stop;

  // Warm voice list
  synth.getVoices();
  if (typeof synth.addEventListener === 'function') {
    synth.addEventListener('voiceschanged', function () { /* voices ready */ });
  }

  // Wire controls
  if (btnLaunch) {
    btnLaunch.addEventListener('click', function () {
      // Unlock audio inside the user gesture so HD can later play() from async.
      unlockAudio();
      stop();
      setTimeout(function () { speakSegment(0); }, 80);
    });
  }
  if (btnPlayPause) btnPlayPause.addEventListener('click', togglePlayPause);
  if (btnPrev)      btnPrev.addEventListener('click', prev);
  if (btnNext)      btnNext.addEventListener('click', next);
  if (btnStop)      btnStop.addEventListener('click', stop);

  window.addEventListener('beforeunload', function () { try { synth.cancel(); } catch (e) {} });

  // ── Selection popup ───────────────────────────────────
  function findSegmentForNode(node) {
    if (!node) return -1;
    if (node.nodeType === 3) node = node.parentNode;
    if (!node || !node.closest) return -1;
    var seg = node.closest('p, h2, h3, blockquote');
    if (!seg || !prose.contains(seg)) return -1;
    segments = getSegments();
    return segments.indexOf(seg);
  }
  // Char offset (within the segment's normalized text) where playback
  // should start. Set by handleProseTap / handleSelection when the user
  // picks a word; reset to 0 by hidePopup. Lets "Start from here" begin
  // mid-paragraph at the actual tapped word, not at the paragraph head.
  var pendingCharOffset = 0;

  function hidePopup() {
    if (popup) popup.classList.remove('tts-popup-visible');
    pendingSelIndex = -1;
    pendingCharOffset = 0;
  }
  function positionPopup(rect, segIndex) {
    if (!popup) return;
    pendingSelIndex = segIndex;
    popup.classList.add('tts-popup-visible');
    var pw = popup.offsetWidth || 170;
    var x = rect.left + rect.width / 2 - pw / 2 + window.pageXOffset;
    var y = rect.bottom + window.pageYOffset + 10;
    var maxX = (document.documentElement.clientWidth || window.innerWidth) - pw - 8 + window.pageXOffset;
    if (x < 8 + window.pageXOffset) x = 8 + window.pageXOffset;
    if (x > maxX) x = maxX;
    popup.style.left = x + 'px';
    popup.style.top  = y + 'px';
  }
  // Set whenever the popup is shown via a paragraph tap (not a text-selection).
  // Used to suppress the selection handlers below — which otherwise fire on
  // the very next mouseup / selectionchange and would close the freshly-tapped
  // popup before the user can reach it.
  var tapShownAt = 0;

  function handleSelection() {
    var sel = window.getSelection();
    if (!sel || sel.isCollapsed || sel.rangeCount === 0) {
      if (Date.now() - tapShownAt > 200) hidePopup();
      return;
    }
    if (!sel.toString().trim()) {
      if (Date.now() - tapShownAt > 200) hidePopup();
      return;
    }
    var range = sel.getRangeAt(0);
    var segIndex = findSegmentForNode(sel.anchorNode);
    if (segIndex < 0) segIndex = findSegmentForNode(sel.focusNode);
    if (segIndex < 0) { hidePopup(); return; }
    var rect = range.getBoundingClientRect();
    if (rect.width === 0 && rect.height === 0) { hidePopup(); return; }
    // Use the selection's START offset so "Start from here" begins at the
    // first selected word, not at the head of the paragraph.
    var lang = getLang();
    var fullText = getSegmentText(segments[segIndex], lang);
    var rawOffset = offsetFromRange(segments[segIndex], lang, range);
    pendingCharOffset = roundToWordStart(fullText, rawOffset);
    positionPopup(rect, segIndex);
  }
  document.addEventListener('mouseup', function () { setTimeout(handleSelection, 10); });
  document.addEventListener('keyup', function (e) {
    if (e.shiftKey || /^Arrow|Home|End/.test(e.key)) setTimeout(handleSelection, 10);
  });
  document.addEventListener('selectionchange', function () {
    var sel = window.getSelection();
    if (!sel || sel.isCollapsed) {
      if (Date.now() - tapShownAt > 200) hidePopup();
    }
  });

  // ── Tap-to-narrate ────────────────────────────────────
  // On mobile and desktop, tapping inside a narratable segment shows the
  // popup near the tap so the user can start narration from that point —
  // no text selection required. The use case: a reader 20 minutes into a
  // long study guide leaves and comes back, scrolls to where they left
  // off, taps, and resumes from there.
  function handleProseTap(e) {
    // Defer to text-selection: if the user is highlighting, handleSelection() owns this.
    var sel = window.getSelection();
    if (sel && !sel.isCollapsed && sel.toString().trim()) return;
    // Let interactive children handle their own clicks.
    if (e.target.closest && e.target.closest('a, button, input, textarea, select, label, summary')) return;
    // Find the segment that was tapped.
    var seg = e.target.closest && e.target.closest('p, h2, h3, blockquote');
    if (!seg || !prose.contains(seg)) return;
    segments = getSegments();
    var segIndex = segments.indexOf(seg);
    if (segIndex < 0) return;
    // Resolve the tap to an exact character offset within the segment, then
    // round back to the start of that word. Falls back to 0 (paragraph start)
    // if the platform doesn't support caret-from-point.
    var lang = getLang();
    var caret = caretRangeAt(e.clientX, e.clientY);
    var offset = caret ? offsetFromRange(seg, lang, caret) : 0;
    var fullText = getSegmentText(seg, lang);
    pendingCharOffset = roundToWordStart(fullText, offset);
    // Show the popup at the tap point. positionPopup() centers horizontally
    // on rect.left + rect.width/2 and anchors the top to rect.bottom, so a
    // zero-width point at (clientX, clientY) gives us a tooltip exactly there.
    positionPopup({ left: e.clientX, width: 0, bottom: e.clientY }, segIndex);
    tapShownAt = Date.now();
  }
  prose.addEventListener('click', handleProseTap);
  document.addEventListener('mousedown', function (e) {
    if (popup && !popup.contains(e.target)) hidePopup();
  });
  window.addEventListener('scroll', hidePopup, { passive: true });
  window.addEventListener('resize', hidePopup);
  if (btnSelPlay) {
    btnSelPlay.addEventListener('click', function (e) {
      e.preventDefault(); e.stopPropagation();
      var idx = pendingSelIndex;
      var off = pendingCharOffset;
      hidePopup();
      var sel = window.getSelection();
      if (sel && sel.removeAllRanges) sel.removeAllRanges();
      if (idx >= 0) { stop(); setTimeout(function () { speakFromOffset(idx, off); }, 80); }
    });
  }

  updateStatus();
})();
