/**
 * Cloudflare Pages Function: /api/track
 * Receives real-time visitor tracking beacons, updates session state in KV,
 * and maintains the Telegram live visitor message lifecycle.
 */

// In-memory fallback for local dev if KV is temporarily unbound
const memoryStore = new Map();

function getVNTime(timestamp) {
  const d = new Date(timestamp || Date.now());
  const formatter = new Intl.DateTimeFormat('en-GB', {
    timeZone: 'Asia/Ho_Chi_Minh',
    hour12: false,
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit',
    second: '2-digit'
  });
  const parts = formatter.formatToParts(d);
  const p = {};
  for (const part of parts) {
    p[part.type] = part.value;
  }
  return {
    time: `${p.hour}:${p.minute}:${p.second}`,
    shortTime: `${p.hour}:${p.minute}`,
    date: `${p.year}-${p.month}-${p.day}`,
    hour: p.hour,
    hourKey: `${p.year}-${p.month}-${p.day}:${p.hour}`,
    hourDisplay: `${p.hour}:00`
  };
}

function formatDuration(seconds) {
  const s = Math.max(0, Math.floor(seconds || 0));
  const mins = Math.floor(s / 60);
  const secs = s % 60;
  return `${mins.toString().padStart(2, '0')}m ${secs.toString().padStart(2, '0')}s`;
}

// Telegram message formatters matching requirements
function formatLiveTelegramMessage(session) {
  const visitorCode = session.visitor_code || session.session_id.replace('SFR-', '#');
  const statusEmoji = session.status === 'IDLE' ? '🟡 IDLE' : '🟢 ONLINE';

  const lines = [
    '🟢 SFR VISITOR LIVE',
    '',
    `Visitor: ${visitorCode}`,
    `Started: ${session.started_time_str || 'Recently'}`,
    '',
    '📍 CURRENT PAGE',
    session.current_page || '/',
    '',
    '⏱ Active',
    formatDuration(session.active_time_seconds),
    '',
    '📜 Scroll',
    `${session.scroll_depth || 0}%`,
    '',
    '📣 SOURCE',
    session.traffic_source || 'Direct'
  ];

  if (session.utm_campaign) {
    lines.push('', 'Campaign:', session.utm_campaign);
  }

  lines.push('', '📱 DEVICE', session.device_category || 'Mobile');

  if (session.journey && session.journey.length > 0) {
    lines.push('', '🧭 JOURNEY');
    session.journey.slice(-5).forEach(j => {
      lines.push(`${j.time}  ${j.page}`);
    });
  }

  lines.push('', '🎯 CTA');
  if (session.ctas && session.ctas.length > 0) {
    session.ctas.slice(-3).forEach(c => {
      lines.push(`• ${c.label} (${c.time})`);
    });
  } else {
    lines.push('None');
  }

  lines.push('', 'Status:', statusEmoji);

  return lines.join('\n');
}

function formatEndedTelegramMessage(session) {
  const visitorCode = session.visitor_code || session.session_id.replace('SFR-', '#');

  const lines = [
    '⚫ SESSION ENDED',
    '',
    `Visitor: ${visitorCode}`,
    '',
    'Duration:',
    formatDuration(session.active_time_seconds),
    '',
    'Pages:',
    `${(session.pages_visited || [session.current_page || '/']).length}`,
    '',
    'Journey:'
  ];

  const pages = session.pages_visited || [session.current_page || '/'];
  pages.slice(-6).forEach(p => {
    lines.push(p);
  });

  lines.push(
    '',
    'Max Scroll:',
    `${session.scroll_depth || 0}%`,
    '',
    'CTA:'
  );

  if (session.ctas && session.ctas.length > 0) {
    session.ctas.forEach(c => {
      lines.push(`• ${c.label} (${c.time})`);
    });
  } else {
    lines.push('None');
  }

  lines.push(
    '',
    'Source:',
    session.traffic_source || 'Direct'
  );

  if (session.utm_campaign) {
    lines.push('', 'Campaign:', session.utm_campaign);
  }

  return lines.join('\n');
}

// Telegram API Helper Functions
async function sendTelegramMessage(botToken, chatId, text) {
  if (!botToken || !chatId) return null;
  try {
    const url = `https://api.telegram.org/bot${botToken}/sendMessage`;
    const res = await fetch(url, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        chat_id: chatId,
        text: text,
        disable_web_page_preview: true
      })
    });
    const json = await res.json();
    return json.ok ? json.result.message_id : null;
  } catch (e) {
    console.error('Telegram sendMessage error:', e);
    return null;
  }
}

async function editTelegramMessage(botToken, chatId, messageId, text) {
  if (!botToken || !chatId || !messageId) return false;
  try {
    const url = `https://api.telegram.org/bot${botToken}/editMessageText`;
    const res = await fetch(url, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        chat_id: chatId,
        message_id: messageId,
        text: text,
        disable_web_page_preview: true
      })
    });
    const json = await res.json();
    return json.ok;
  } catch (e) {
    console.error('Telegram editMessage error:', e);
    return false;
  }
}

// KV Helper Functions (with memory fallback)
async function getKV(env, key) {
  if (env && env.SFR_ANALYTICS) {
    try {
      const val = await env.SFR_ANALYTICS.get(key, 'json');
      return val;
    } catch (e) {
      console.error('KV get error:', e);
    }
  }
  return memoryStore.get(key) || null;
}

async function putKV(env, key, value, ttlSeconds) {
  if (env && env.SFR_ANALYTICS) {
    try {
      const opts = ttlSeconds ? { expirationTtl: Math.max(60, ttlSeconds) } : undefined;
      await env.SFR_ANALYTICS.put(key, JSON.stringify(value), opts);
      return;
    } catch (e) {
      console.error('KV put error:', e);
    }
  }
  memoryStore.set(key, value);
}

// Main Pages Function Handler
export async function onRequestPost(context) {
  const { request, env } = context;

  // Telegram credentials from environment variables
  const botToken = env.TELEGRAM_BOT_TOKEN;
  const chatId = env.TELEGRAM_CHAT_ID;

  let payload;
  try {
    payload = await request.json();
  } catch (e) {
    return new Response(JSON.stringify({ ok: false, error: 'Invalid JSON' }), {
      status: 400,
      headers: { 'Content-Type': 'application/json' }
    });
  }

  const {
    event,
    session_id,
    page_path = '/',
    active_time_seconds = 0,
    scroll_depth = 0,
    cta_label,
    cta_type,
    from_page,
    to_page,
    visitor_status
  } = payload;

  if (!session_id) {
    return new Response(JSON.stringify({ ok: false, error: 'Missing session_id' }), {
      status: 400,
      headers: { 'Content-Type': 'application/json' }
    });
  }

  const now = Date.now();
  const vnTime = getVNTime(now);
  const sessionKey = `session:${session_id}`;

  // Retrieve existing session or initialize new one
  let session = await getKV(env, sessionKey);

  if (!session) {
    const visitorCode = '#' + session_id.replace('SFR-', '');
    session = {
      session_id,
      visitor_code: visitorCode,
      started_at: now,
      started_time_str: vnTime.time,
      started_date_str: vnTime.date,
      landing_page: payload.landing_page || page_path,
      current_page: page_path,
      traffic_source: payload.traffic_source || 'Direct',
      referrer: payload.referrer || '',
      utm_source: payload.utm_source || '',
      utm_medium: payload.utm_medium || '',
      utm_campaign: payload.utm_campaign || '',
      utm_content: payload.utm_content || '',
      utm_term: payload.utm_term || '',
      device_category: payload.device_category || 'Mobile',
      browser: payload.browser || 'Browser',
      screen_size: payload.screen_size || '',
      active_time_seconds: active_time_seconds,
      scroll_depth: scroll_depth,
      pages_visited: [page_path],
      journey: [{ time: vnTime.shortTime, page: page_path }],
      ctas: [],
      status: 'ONLINE',
      last_heartbeat: now,
      telegram_message_id: null,
      last_telegram_update: now,
      ended: false
    };

    // Send initial Telegram Live alert
    const messageText = formatLiveTelegramMessage(session);
    const msgId = await sendTelegramMessage(botToken, chatId, messageText);
    if (msgId) {
      session.telegram_message_id = msgId;
    }
  } else {
    // Update existing session state
    session.last_heartbeat = now;
    if (active_time_seconds > (session.active_time_seconds || 0)) {
      session.active_time_seconds = active_time_seconds;
    }
    if (scroll_depth > (session.scroll_depth || 0)) {
      session.scroll_depth = scroll_depth;
    }
    if (page_path && page_path !== session.current_page) {
      session.current_page = page_path;
      if (!session.pages_visited.includes(page_path)) {
        session.pages_visited.push(page_path);
      }
      session.journey.push({ time: vnTime.shortTime, page: page_path });
    }
  }

  // Handle Event Specific Actions
  let shouldUpdateTelegram = false;
  let isSessionEndEvent = false;

  if (event === 'page_change') {
    const targetPage = to_page || page_path;
    session.current_page = targetPage;
    if (!session.pages_visited.includes(targetPage)) {
      session.pages_visited.push(targetPage);
    }
    session.journey.push({ time: vnTime.shortTime, page: targetPage });
    session.status = 'ONLINE';
    shouldUpdateTelegram = true; // Immediate update on route change
  } else if (event.startsWith('click_') || event === 'cta_click' || event === 'form_submit') {
    const label = cta_label || (cta_type ? cta_type.replace('click_', '') : 'CTA Click');
    session.ctas.push({
      time: vnTime.shortTime,
      type: event,
      label: label
    });
    session.status = 'ONLINE';
    shouldUpdateTelegram = true; // Immediate update on CTA
  } else if (event === 'heartbeat') {
    const newStatus = visitor_status || 'ONLINE';
    const statusChanged = session.status !== newStatus;
    session.status = newStatus;

    // Telegram rate limit guard: update every ~60 seconds OR when status changes
    const timeSinceLastTelegram = (now - (session.last_telegram_update || 0)) / 1000;
    if (statusChanged || timeSinceLastTelegram >= 60) {
      shouldUpdateTelegram = true;
    }
  } else if (event === 'session_end') {
    session.ended = true;
    session.status = 'SESSION ENDED';
    isSessionEndEvent = true;
    shouldUpdateTelegram = true;
  }

  // Execute Telegram Message Edit if needed
  if (shouldUpdateTelegram && session.telegram_message_id) {
    const text = isSessionEndEvent
      ? formatEndedTelegramMessage(session)
      : formatLiveTelegramMessage(session);

    await editTelegramMessage(botToken, chatId, session.telegram_message_id, text);
    session.last_telegram_update = now;
  }

  // Persist session in KV (TTL: 300s / 5 mins, automatically renewed by active heartbeats)
  // When ended, retain for 1 hour for stats verification
  const sessionTTL = isSessionEndEvent ? 3600 : 300;
  await putKV(env, sessionKey, session, sessionTTL);

  // Update Active Sessions Index
  let activeIndex = await getKV(env, 'active_sessions_index');
  if (!Array.isArray(activeIndex)) activeIndex = [];

  if (isSessionEndEvent) {
    activeIndex = activeIndex.filter(id => id !== session_id);
  } else if (!activeIndex.includes(session_id)) {
    activeIndex.push(session_id);
  }
  await putKV(env, 'active_sessions_index', activeIndex, 86400);

  // Update Hourly Aggregated Metrics
  try {
    const hourKey = `hourly:${vnTime.hourKey}`;
    let hourlyStats = await getKV(env, hourKey);
    if (!hourlyStats) {
      hourlyStats = {
        hour: vnTime.hourDisplay,
        hourKey: vnTime.hourKey,
        date: vnTime.date,
        visitors: {},
        sessions_count: 0,
        page_views: 0,
        pages: {},
        sources: {},
        campaigns: {},
        devices: {},
        ctas: {},
        peak_concurrency: 0,
        peak_time: vnTime.shortTime
      };
    }

    // Register visitor & session
    hourlyStats.visitors[session_id] = 1;
    hourlyStats.page_views++;
    if (event === 'session_start') {
      hourlyStats.sessions_count++;
    }

    // Register Page view stats
    const p = session.current_page || '/';
    if (!hourlyStats.pages[p]) {
      hourlyStats.pages[p] = { views: 0, visitors: {}, active_time: 0, ctas: 0, scroll_90: 0 };
    }
    hourlyStats.pages[p].views++;
    hourlyStats.pages[p].visitors[session_id] = 1;
    hourlyStats.pages[p].active_time += Math.min(25, active_time_seconds);

    if (scroll_depth >= 90) hourlyStats.pages[p].scroll_90++;

    // Register Source
    const src = session.traffic_source || 'Direct';
    hourlyStats.sources[src] = (hourlyStats.sources[src] || 0) + 1;

    // Register Device
    const dev = session.device_category || 'Mobile';
    hourlyStats.devices[dev] = (hourlyStats.devices[dev] || 0) + 1;

    // Register CTA
    if (event.startsWith('click_') || event === 'cta_click' || event === 'form_submit') {
      const ctaTypeKey = (cta_type || event).replace('click_', '');
      hourlyStats.ctas[ctaTypeKey] = (hourlyStats.ctas[ctaTypeKey] || 0) + 1;
      hourlyStats.pages[p].ctas++;
    }

    // Check concurrency
    const currentOnline = activeIndex.length;
    if (currentOnline > (hourlyStats.peak_concurrency || 0)) {
      hourlyStats.peak_concurrency = currentOnline;
      hourlyStats.peak_time = vnTime.shortTime;
    }

    // Store hourly stats with 7 days TTL (604800s)
    await putKV(env, hourKey, hourlyStats, 604800);
  } catch (e) {
    console.error('Error updating hourly stats:', e);
  }

  return new Response(JSON.stringify({
    ok: true,
    session_id: session.session_id,
    status: session.status,
    active_time: session.active_time_seconds
  }), {
    status: 200,
    headers: {
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*'
    }
  });
}

// Handle CORS Preflight
export async function onRequestOptions() {
  return new Response(null, {
    status: 204,
    headers: {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'POST, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type',
      'Access-Control-Max-Age': '86400'
    }
  });
}
