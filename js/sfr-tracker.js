/**
 * SAIGON FARM RESORT — REAL-TIME VISITOR TRACKER CLIENT (SFR-TRACKER)
 * Lightweight, non-blocking real-time tracking client with Telegram live integration.
 * Preserves GA4 & Microsoft Clarity integrity.
 */

(function () {
  'use strict';

  // 1. Bot & Crawler Detection
  function isBot() {
    if (window.navigator.webdriver) return true;
    if (window._phantom || window.__nightmare || window.callPhantom) return true;
    var ua = (navigator.userAgent || '').toLowerCase();
    var botRegex = /(bot|crawler|spider|robot|crawling|googlebot|bingbot|slurp|duckduckbot|baiduspider|yandexbot|facebookexternalhit|facebot|whatsapp|telegrambot|twitterbot|linkedinbot|pinterest|slackbot|discordbot|headlesschrome|lighthouse|curl|wget|python|php)/i;
    return botRegex.test(ua);
  }

  if (isBot()) return;

  // 2. Internal / Admin Traffic Exclusion
  function checkAdminBypass() {
    try {
      var urlParams = new URLSearchParams(window.location.search);
      if (urlParams.get('sfr_admin') === '1' || urlParams.get('admin') === '1') {
        localStorage.setItem('sfr_admin_bypass', '1');
        document.cookie = 'sfr_admin_bypass=1; path=/; max-age=31536000; SameSite=Lax';
        console.info('[SFR Analytics] Internal admin bypass enabled.');
        return true;
      }
      if (urlParams.get('sfr_admin') === '0' || urlParams.get('admin') === '0') {
        localStorage.removeItem('sfr_admin_bypass');
        document.cookie = 'sfr_admin_bypass=; path=/; expires=Thu, 01 Jan 1970 00:00:00 GMT';
        console.info('[SFR Analytics] Internal admin bypass disabled.');
        return false;
      }
      if (localStorage.getItem('sfr_admin_bypass') === '1' || document.cookie.indexOf('sfr_admin_bypass=1') !== -1) {
        return true;
      }
      // Localhost check (unless explicitly testing with ?sfr_test=1)
      var host = window.location.hostname;
      if ((host === 'localhost' || host === '127.0.0.1') && urlParams.get('sfr_test') !== '1') {
        return true;
      }
    } catch (e) {}
    return false;
  }

  if (checkAdminBypass()) {
    return;
  }

  // 3. Anonymous Session Identifier (Format: SFR-A72F91)
  function getSessionId() {
    try {
      var sid = sessionStorage.getItem('sfr_session_id');
      if (!sid) {
        var hex = Math.floor(Math.random() * 0xFFFFFF).toString(16).toUpperCase().padStart(6, '0');
        sid = 'SFR-' + hex;
        sessionStorage.setItem('sfr_session_id', sid);
        sessionStorage.setItem('sfr_session_start_time', Date.now().toString());
      }
      return sid;
    } catch (e) {
      return 'SFR-' + Math.floor(Math.random() * 0xFFFFFF).toString(16).toUpperCase().padStart(6, '0');
    }
  }

  var sessionId = getSessionId();

  // 4. Device & Browser Parsing
  function getDeviceCategory() {
    var ua = navigator.userAgent;
    if (/(ipad|tablet|(android(?!.*mobile))|(windows(?!.*phone)(.*touch))|kindle|playbook|silk)/i.test(ua)) {
      return 'Tablet';
    }
    if (/(android|iphone|ipod|windows phone|blackberry|mobile)/i.test(ua)) {
      return 'Mobile';
    }
    return 'Desktop';
  }

  function getBrowserName() {
    var ua = navigator.userAgent;
    if (/zalo/i.test(ua)) return 'Zalo App';
    if (/fban|fbav/i.test(ua)) return 'Facebook App';
    if (/crios/i.test(ua)) return 'Chrome (iOS)';
    if (/fxios/i.test(ua)) return 'Firefox (iOS)';
    if (/edg/i.test(ua)) return 'Edge';
    if (/chrome|chromium/i.test(ua)) return 'Chrome';
    if (/safari/i.test(ua)) return 'Safari';
    if (/firefox/i.test(ua)) return 'Firefox';
    if (/opera|opr/i.test(ua)) return 'Opera';
    return 'Browser';
  }

  // 5. Traffic Source & Campaign Resolution
  function getTrafficSource() {
    var urlParams = new URLSearchParams(window.location.search);
    var utmSource = urlParams.get('utm_source');
    var utmMedium = urlParams.get('utm_medium');
    var utmCampaign = urlParams.get('utm_campaign');
    var ref = document.referrer || '';

    var sourceName = 'Direct';
    if (utmSource) {
      sourceName = utmSource;
      if (/fb|facebook/i.test(utmSource)) {
        sourceName = (utmMedium && /cpc|ads|paid/i.test(utmMedium)) ? 'Facebook Ads' : 'Facebook';
      } else if (/zalo/i.test(utmSource)) {
        sourceName = (utmMedium && /cpc|ads/i.test(utmMedium)) ? 'Zalo Ads' : 'Zalo';
      } else if (/google/i.test(utmSource)) {
        sourceName = (utmMedium && /cpc|ads/i.test(utmMedium)) ? 'Google Ads' : 'Google';
      }
    } else if (ref) {
      if (/facebook\.com|fb\.com/i.test(ref)) sourceName = 'Facebook Organic';
      else if (/zalo\.me/i.test(ref)) sourceName = 'Zalo';
      else if (/google\./i.test(ref)) sourceName = 'Google Organic';
      else if (/tiktok\.com/i.test(ref)) sourceName = 'TikTok';
      else if (/youtube\.com/i.test(ref)) sourceName = 'YouTube';
      else {
        try {
          sourceName = new URL(ref).hostname;
        } catch (e) {
          sourceName = 'Referral';
        }
      }
    }

    return {
      source: sourceName,
      referrer: ref,
      utm_source: utmSource || '',
      utm_medium: utmMedium || '',
      utm_campaign: utmCampaign || '',
      utm_content: urlParams.get('utm_content') || '',
      utm_term: urlParams.get('utm_term') || ''
    };
  }

  // 6. State Management
  var currentPath = window.location.pathname || '/';
  var maxScrollDepth = 0;
  var activeSeconds = 0;
  var lastUserActivity = Date.now();
  var isTabVisible = !document.hidden;
  var heartbeatTimer = null;
  var activeSecondTicker = null;
  var formStarted = false;
  var trackingEndpoint = '/api/track';

  // 7. Silent Transmission (Beacon with keepalive fetch fallback)
  function sendEvent(eventType, extraData) {
    try {
      var payload = Object.assign({
        event: eventType,
        session_id: sessionId,
        page_path: currentPath,
        page_title: document.title || '',
        active_time_seconds: activeSeconds,
        scroll_depth: maxScrollDepth,
        timestamp: Date.now()
      }, extraData || {});

      var dataStr = JSON.stringify(payload);

      if (navigator.sendBeacon) {
        var blob = new Blob([dataStr], { type: 'application/json' });
        var ok = navigator.sendBeacon(trackingEndpoint, blob);
        if (ok) return;
      }

      fetch(trackingEndpoint, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: dataStr,
        keepalive: true
      }).catch(function () {});
    } catch (err) {
      // Fail completely silently to prevent disrupting site functionality
    }
  }

  // 8. Active Time & Activity Watcher (No passive tab time)
  function recordUserActivity() {
    lastUserActivity = Date.now();
  }

  ['scroll', 'mousemove', 'touchstart', 'click', 'keydown'].forEach(function (evt) {
    window.addEventListener(evt, recordUserActivity, { passive: true });
  });

  document.addEventListener('visibilitychange', function () {
    isTabVisible = !document.hidden;
    if (isTabVisible) {
      recordUserActivity();
    }
  });

  activeSecondTicker = setInterval(function () {
    // Only increment when tab is visible AND active within the last 20 seconds
    if (isTabVisible && (Date.now() - lastUserActivity < 20000)) {
      activeSeconds++;
    }
  }, 1000);

  // 9. Scroll Tracking (25%, 50%, 75%, 90%)
  function calculateScroll() {
    try {
      var docEl = document.documentElement;
      var body = document.body;
      var scrollTop = window.pageYOffset || docEl.scrollTop || body.scrollTop || 0;
      var scrollHeight = Math.max(docEl.scrollHeight, body.scrollHeight, 1);
      var clientHeight = window.innerHeight || docEl.clientHeight || 1;

      var percent = Math.min(100, Math.round(((scrollTop + clientHeight) / scrollHeight) * 100));
      if (percent > maxScrollDepth) {
        maxScrollDepth = percent;
      }
    } catch (e) {}
  }

  window.addEventListener('scroll', calculateScroll, { passive: true });

  // 10. Route Change Tracking (SPA & Multi-page History)
  function handleRouteChange(newPath) {
    if (newPath === currentPath) return;
    var from = currentPath;
    currentPath = newPath;
    maxScrollDepth = 0; // reset scroll for new route

    sendEvent('page_change', {
      from_page: from,
      to_page: newPath
    });
  }

  var originalPushState = history.pushState;
  if (originalPushState) {
    history.pushState = function () {
      originalPushState.apply(this, arguments);
      handleRouteChange(window.location.pathname);
    };
  }

  var originalReplaceState = history.replaceState;
  if (originalReplaceState) {
    history.replaceState = function () {
      originalReplaceState.apply(this, arguments);
      handleRouteChange(window.location.pathname);
    };
  }

  window.addEventListener('popstate', function () {
    handleRouteChange(window.location.pathname);
  });

  // 11. CTA & Important Action Interception
  function identifyCTA(elem) {
    if (!elem || elem === document.body || elem === document.documentElement) return null;

    var href = (elem.getAttribute('href') || '').toLowerCase();
    var text = (elem.innerText || elem.textContent || '').trim().toLowerCase();
    var cls = (elem.className || '').toString().toLowerCase();
    var id = (elem.id || '').toLowerCase();

    // Direct channel matches
    if (href.indexOf('zalo.me') !== -1 || href.indexOf('zalo:') !== -1) {
      return { type: 'click_zalo', label: 'Zalo Click' };
    }
    if (href.startsWith('tel:')) {
      return { type: 'click_phone', label: 'Phone Call (' + href.replace('tel:', '').trim() + ')' };
    }
    if (href.indexOf('wa.me') !== -1 || href.indexOf('whatsapp') !== -1) {
      return { type: 'click_whatsapp', label: 'WhatsApp Click' };
    }
    if (href.indexOf('m.me') !== -1 || href.indexOf('messenger.com') !== -1) {
      return { type: 'click_messenger', label: 'Messenger Click' };
    }
    if (href.indexOf('maps.google') !== -1 || href.indexOf('goo.gl/maps') !== -1 || href.indexOf('/vitri') !== -1) {
      return { type: 'view_location', label: 'View Location Map' };
    }
    if (href.indexOf('.pdf') !== -1 || elem.hasAttribute('download')) {
      return { type: 'download', label: 'Download Brochure' };
    }

    // Button & CTA classes
    if (cls.indexOf('cta') !== -1 || cls.indexOf('btn-gold') !== -1 || elem.hasAttribute('data-cta') || id.indexOf('cta') !== -1) {
      var label = (elem.getAttribute('data-cta') || text.substring(0, 30) || 'CTA Button').trim();
      return { type: 'cta_click', label: label };
    }

    // Video play triggers
    if (cls.indexOf('video-play') !== -1 || cls.indexOf('play-btn') !== -1) {
      return { type: 'video_play', label: 'Play Video' };
    }

    return identifyCTA(elem.parentElement);
  }

  document.addEventListener('click', function (e) {
    try {
      var cta = identifyCTA(e.target);
      if (cta) {
        sendEvent(cta.type, {
          cta_label: cta.label,
          cta_type: cta.type
        });
      }
    } catch (err) {}
  }, true);

  // Form Interactions
  document.addEventListener('focusin', function (e) {
    try {
      var tag = (e.target.tagName || '').toLowerCase();
      if (!formStarted && (tag === 'input' || tag === 'textarea' || tag === 'select')) {
        formStarted = true;
        sendEvent('form_start', {
          form_id: (e.target.form ? e.target.form.id : '') || 'lead_form'
        });
      }
    } catch (err) {}
  }, true);

  document.addEventListener('submit', function (e) {
    try {
      var formId = (e.target.id || e.target.name || 'lead_form');
      sendEvent('form_submit', {
        form_id: formId,
        cta_label: 'Form Submitted (' + formId + ')'
      });
    } catch (err) {}
  }, true);

  // 12. Session Start Trigger
  var traffic = getTrafficSource();
  var isReturningSession = sessionStorage.getItem('sfr_session_sent') === '1';

  if (!isReturningSession) {
    sessionStorage.setItem('sfr_session_sent', '1');
    sendEvent('session_start', {
      landing_page: currentPath,
      traffic_source: traffic.source,
      referrer: traffic.referrer,
      utm_source: traffic.utm_source,
      utm_medium: traffic.utm_medium,
      utm_campaign: traffic.utm_campaign,
      utm_content: traffic.utm_content,
      utm_term: traffic.utm_term,
      device_category: getDeviceCategory(),
      browser: getBrowserName(),
      screen_size: (window.screen.width || 0) + 'x' + (window.screen.height || 0)
    });
  }

  // 13. Heartbeat (every 25 seconds)
  heartbeatTimer = setInterval(function () {
    var idleTime = Date.now() - lastUserActivity;
    var status = (idleTime > 50000) ? 'IDLE' : 'ONLINE';

    sendEvent('heartbeat', {
      current_page: currentPath,
      visibility_state: isTabVisible ? 'visible' : 'hidden',
      visitor_status: status
    });
  }, 25000);

  // 14. Session End (visibility & pagehide)
  function handleSessionEnd() {
    sendEvent('session_end', {
      current_page: currentPath
    });
  }

  window.addEventListener('pagehide', handleSessionEnd);
  window.addEventListener('beforeunload', handleSessionEnd);
})();
