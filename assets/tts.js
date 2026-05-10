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
        '<button id="tts-hd" class="tts-btn-icon tts-btn-hd" aria-label="Toggle HD voice" title="HD voice (Google Gemini · 中文 + English)">HD</button>' +
        '<button id="tts-stop" class="tts-btn-icon tts-stop" aria-label="Stop">✕</button>';
      document.body.appendChild(player);
    } else {
      // Existing player — make sure HD button is present (insert before stop)
      if (!document.getElementById('tts-hd')) {
        var stop = document.getElementById('tts-stop');
        var hd = document.createElement('button');
        hd.id = 'tts-hd';
        hd.className = 'tts-btn-icon tts-btn-hd';
        hd.setAttribute('aria-label', 'Toggle HD voice');
        hd.title = 'HD voice (Google Gemini · 中文 + English)';
        hd.textContent = 'HD';
        if (stop) stop.parentNode.insertBefore(hd, stop);
        else player.appendChild(hd);
      }
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
      popup.innerHTML = '<button id="tts-selection-play" class="tts-popup-btn">▶ <span class="zh">從這裡朗讀</span><span class="en">Read from here</span></button>';
      document.body.appendChild(popup);
    }
  }
  injectMarkup();

  // ══════════════════════════════════════════════════════
  // Behaviour
  // ══════════════════════════════════════════════════════
  var synth = window.speechSynthesis;
  var SEGMENT_SELECTOR = ':scope > p, :scope > h2, :scope > h3, :scope > blockquote';
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
  var audioUnlocked = false;     // iOS audio is locked until first user-gesture play()

  // 1-byte silent WAV — the smallest valid file we can use to "warm up"
  // the <audio> element inside a user-gesture callback so iOS Safari will
  // let us call .play() later from an async callback.
  var SILENT_WAV_DATA_URL =
    'data:audio/wav;base64,UklGRkQAAABXQVZFZm10IBAAAAABAAEARKwAAIhYAQACABAAZGF0YSAAAAAAAA' +
    'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA';

  function getLang() { return document.documentElement.getAttribute('data-lang') || 'zh'; }

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

  // ── Speaker dispatch ──────────────────────────────────
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
    if (shouldUseHD()) speakViaHD(index, text, lang);
    else speakViaWebSpeech(index, text, lang);
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
    utter.rate = 1.0; utter.pitch = 1.0; utter.volume = 1.0;
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
    isPlaying = false; isPaused = false;
    currentUtterance = null; currentIndex = -1; activeBackend = null;
    clearHighlight(); updateStatus(); setPlayPauseIcon(true); hidePlayer();
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
  function hidePopup() {
    if (popup) popup.classList.remove('tts-popup-visible');
    pendingSelIndex = -1;
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
  function handleSelection() {
    var sel = window.getSelection();
    if (!sel || sel.isCollapsed || sel.rangeCount === 0) { hidePopup(); return; }
    if (!sel.toString().trim()) { hidePopup(); return; }
    var range = sel.getRangeAt(0);
    var segIndex = findSegmentForNode(sel.anchorNode);
    if (segIndex < 0) segIndex = findSegmentForNode(sel.focusNode);
    if (segIndex < 0) { hidePopup(); return; }
    var rect = range.getBoundingClientRect();
    if (rect.width === 0 && rect.height === 0) { hidePopup(); return; }
    positionPopup(rect, segIndex);
  }
  document.addEventListener('mouseup', function () { setTimeout(handleSelection, 10); });
  document.addEventListener('keyup', function (e) {
    if (e.shiftKey || /^Arrow|Home|End/.test(e.key)) setTimeout(handleSelection, 10);
  });
  document.addEventListener('selectionchange', function () {
    var sel = window.getSelection();
    if (!sel || sel.isCollapsed) hidePopup();
  });
  document.addEventListener('mousedown', function (e) {
    if (popup && !popup.contains(e.target)) hidePopup();
  });
  window.addEventListener('scroll', hidePopup, { passive: true });
  window.addEventListener('resize', hidePopup);
  if (btnSelPlay) {
    btnSelPlay.addEventListener('click', function (e) {
      e.preventDefault(); e.stopPropagation();
      var idx = pendingSelIndex;
      hidePopup();
      var sel = window.getSelection();
      if (sel && sel.removeAllRanges) sel.removeAllRanges();
      if (idx >= 0) { stop(); setTimeout(function () { speakSegment(idx); }, 80); }
    });
  }

  updateStatus();
})();
