/**
 * Cloudflare Pages Function: /api/cron
 * Generates the hourly summary report, executes server-side session timeouts,
 * and posts the report to Telegram.
 */

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
    hourDisplay: `${p.hour}:00`,
    dateObj: d
  };
}

function formatDuration(seconds) {
  const s = Math.max(0, Math.floor(seconds || 0));
  const mins = Math.floor(s / 60);
  const secs = s % 60;
  return `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
}

function calcPercentChange(curr, prev) {
  if (!prev || prev <= 0) return '';
  const diff = ((curr - prev) / prev) * 100;
  const rounded = Math.abs(Math.round(diff));
  if (diff > 0) return ` ↑ ${rounded}%`;
  if (diff < 0) return ` ↓ ${rounded}%`;
  return ' → 0%';
}

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

export async function onRequest(context) {
  const { request, env } = context;

  const botToken = env.TELEGRAM_BOT_TOKEN;
  const chatId = env.TELEGRAM_CHAT_ID;

  // Optional security check if CRON_SECRET is configured
  const url = new URL(request.url);
  const providedSecret = url.searchParams.get('secret') || request.headers.get('x-cron-secret');
  if (env.CRON_SECRET && providedSecret !== env.CRON_SECRET) {
    return new Response(JSON.stringify({ ok: false, error: 'Unauthorized cron trigger' }), {
      status: 401,
      headers: { 'Content-Type': 'application/json' }
    });
  }

  const now = Date.now();
  const currentVN = getVNTime(now);

  // Determine previous hour to summarize (e.g. at 18:00, summarize 17:00 -> 18:00)
  const oneHourAgo = now - 3600000;
  const prevHourVN = getVNTime(oneHourAgo);
  const twoHoursAgo = now - 7200000;
  const priorHourVN = getVNTime(twoHoursAgo);

  // 1. Clean up Stale Sessions & Server-Side Timeout (90-120s)
  let activeIndex = [];
  if (env.SFR_ANALYTICS) {
    try {
      activeIndex = (await env.SFR_ANALYTICS.get('active_sessions_index', 'json')) || [];
    } catch (e) {}
  }

  let stillActive = [];
  let timedOutCount = 0;

  for (const sid of activeIndex) {
    if (!env.SFR_ANALYTICS) continue;
    const sessionKey = `session:${sid}`;
    const sess = await env.SFR_ANALYTICS.get(sessionKey, 'json');

    if (!sess) continue;

    const timeSinceHeartbeat = now - (sess.last_heartbeat || 0);
    // If no heartbeat for > 100 seconds, close session
    if (!sess.ended && timeSinceHeartbeat > 100000) {
      sess.ended = true;
      sess.status = 'SESSION ENDED';
      timedOutCount++;

      if (sess.telegram_message_id) {
        const endedText = formatEndedTelegramMessage(sess);
        await editTelegramMessage(botToken, chatId, sess.telegram_message_id, endedText);
      }

      await env.SFR_ANALYTICS.put(sessionKey, JSON.stringify(sess), { expirationTtl: 3600 });
    } else if (!sess.ended) {
      stillActive.push(sid);
    }
  }

  if (env.SFR_ANALYTICS) {
    await env.SFR_ANALYTICS.put('active_sessions_index', JSON.stringify(stillActive), { expirationTtl: 86400 });
  }

  // 2. Fetch Stats for Previous Hour
  let hourlyStats = null;
  let priorStats = null;

  if (env.SFR_ANALYTICS) {
    hourlyStats = await env.SFR_ANALYTICS.get(`hourly:${prevHourVN.hourKey}`, 'json');
    priorStats = await env.SFR_ANALYTICS.get(`hourly:${priorHourVN.hourKey}`, 'json');
  }

  // Fallback if testing without prior hour data
  if (!hourlyStats) {
    hourlyStats = {
      hour: prevHourVN.hourDisplay,
      date: prevHourVN.date,
      visitors: {},
      sessions_count: 0,
      page_views: 0,
      pages: {},
      sources: {},
      devices: {},
      ctas: {},
      peak_concurrency: stillActive.length,
      peak_time: prevHourVN.shortTime
    };
  }

  const totalVisitors = Object.keys(hourlyStats.visitors || {}).length;
  const totalSessions = hourlyStats.sessions_count || totalVisitors;
  const totalViews = hourlyStats.page_views || 0;
  const currentlyOnline = stillActive.length;

  // Format Top Pages
  const pageEntries = Object.entries(hourlyStats.pages || {}).map(([path, data]) => {
    const pVisitors = Object.keys(data.visitors || {}).length;
    const avgSecs = pVisitors > 0 ? Math.round((data.active_time || 0) / pVisitors) : 0;
    return {
      path,
      visitors: pVisitors,
      views: data.views || 0,
      avgActive: formatDuration(avgSecs),
      ctas: data.ctas || 0
    };
  });

  pageEntries.sort((a, b) => b.views - a.views);

  // Format Sources
  const sourceEntries = Object.entries(hourlyStats.sources || {});
  sourceEntries.sort((a, b) => b[1] - a[1]);

  // Format CTAs
  const ctaEntries = Object.entries(hourlyStats.ctas || {});
  ctaEntries.sort((a, b) => b[1] - a[1]);
  const totalCTA = ctaEntries.reduce((acc, curr) => acc + curr[1], 0);

  // Format Device Percentages
  const totalDevices = Object.values(hourlyStats.devices || {}).reduce((a, b) => a + b, 0) || 1;
  const mobilePct = Math.round(((hourlyStats.devices['Mobile'] || 0) / totalDevices) * 100);
  const desktopPct = Math.round(((hourlyStats.devices['Desktop'] || 0) / totalDevices) * 100);
  const tabletPct = 100 - mobilePct - desktopPct;

  // Build Telegram Report Message
  const reportLines = [
    '📊 SFR — HOURLY REPORT',
    `${prevHourVN.hourDisplay} → ${currentVN.hourDisplay}`,
    '',
    '👥 TRAFFIC',
    ''
  ];

  // Comparisons with prior hour if applicable
  const priorVisitors = priorStats ? Object.keys(priorStats.visitors || {}).length : 0;
  const visitorDiff = priorVisitors > 5 ? calcPercentChange(totalVisitors, priorVisitors) : '';

  reportLines.push(`Visitors: ${totalVisitors}${visitorDiff}`);
  reportLines.push(`Sessions: ${totalSessions}`);
  reportLines.push(`Page Views: ${totalViews}`);
  reportLines.push(`Currently Online: ${currentlyOnline}`);

  if (pageEntries.length > 0) {
    reportLines.push('', '🔥 TOP PAGES');
    pageEntries.slice(0, 5).forEach((p, idx) => {
      reportLines.push('');
      reportLines.push(`${idx + 1}. ${p.path}`);
      reportLines.push(`${p.visitors} visitors`);
      reportLines.push(`${p.views} views`);
      reportLines.push(`Avg Active: ${p.avgActive}`);
      if (p.ctas > 0) {
        reportLines.push(`CTA: ${p.ctas}`);
      }
    });
  }

  if (sourceEntries.length > 0) {
    reportLines.push('', '📣 SOURCE', '');
    sourceEntries.slice(0, 6).forEach(([src, count]) => {
      reportLines.push(`${src}: ${count}`);
    });
  }

  if (ctaEntries.length > 0) {
    reportLines.push('', '🎯 CTA', '');
    ctaEntries.forEach(([type, count]) => {
      const displayType = type.charAt(0).toUpperCase() + type.slice(1);
      reportLines.push(`${displayType}: ${count}`);
    });
    reportLines.push('', `Total CTA: ${totalCTA}`);
  }

  reportLines.push(
    '',
    '📱 DEVICE',
    '',
    `Mobile: ${mobilePct}%`,
    `Desktop: ${desktopPct}%`,
    `Tablet: ${Math.max(0, tabletPct)}%`
  );

  reportLines.push(
    '',
    '👀 PEAK CONCURRENCY',
    '',
    'Maximum simultaneous visitors:',
    `${Math.max(currentlyOnline, hourlyStats.peak_concurrency || 0)}`,
    '',
    'Peak time:',
    hourlyStats.peak_time || prevHourVN.shortTime
  );

  const reportText = reportLines.join('\n');

  // Send Report to Telegram (only if there was traffic or at scheduled hour)
  let sentMsgId = null;
  if (totalViews > 0 || totalVisitors > 0 || url.searchParams.get('force') === '1') {
    sentMsgId = await sendTelegramMessage(botToken, chatId, reportText);
  }

  return new Response(JSON.stringify({
    ok: true,
    hour: `${prevHourVN.hourDisplay} -> ${currentVN.hourDisplay}`,
    visitors: totalVisitors,
    views: totalViews,
    online_now: currentlyOnline,
    timed_out_sessions: timedOutCount,
    telegram_message_id: sentMsgId,
    preview: reportText
  }), {
    status: 200,
    headers: { 'Content-Type': 'application/json' }
  });
}
