/**
 * Cloudflare Pages Function: /api/telegram-webhook
 * Handles interactive Telegram commands: /live, /status, /hour
 */

export async function onRequestPost(context) {
  const { request, env } = context;

  const botToken = env.TELEGRAM_BOT_TOKEN;
  if (!botToken) {
    return new Response(JSON.stringify({ ok: true, ignored: true }), { status: 200 });
  }

  let update;
  try {
    update = await request.json();
  } catch (e) {
    return new Response('Invalid JSON', { status: 400 });
  }

  const message = update.message;
  if (!message || !message.text) {
    return new Response(JSON.stringify({ ok: true }), { status: 200 });
  }

  const text = message.text.trim().toLowerCase();
  const chatId = message.chat.id;

  async function reply(replyText) {
    try {
      await fetch(`https://api.telegram.org/bot${botToken}/sendMessage`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          chat_id: chatId,
          text: replyText,
          disable_web_page_preview: true
        })
      });
    } catch (e) {}
  }

  if (text.startsWith('/live')) {
    let activeIndex = [];
    if (env.SFR_ANALYTICS) {
      try {
        activeIndex = (await env.SFR_ANALYTICS.get('active_sessions_index', 'json')) || [];
      } catch (e) {}
    }

    const now = Date.now();
    const pageCounts = {};
    let onlineCount = 0;

    for (const sid of activeIndex) {
      if (!env.SFR_ANALYTICS) continue;
      const sess = await env.SFR_ANALYTICS.get(`session:${sid}`, 'json');
      if (sess && !sess.ended && (now - (sess.last_heartbeat || 0) < 120000)) {
        onlineCount++;
        const p = sess.current_page || '/';
        pageCounts[p] = (pageCounts[p] || 0) + 1;
      }
    }

    const lines = [`🟢 ONLINE NOW: ${onlineCount}`, ''];
    const pageEntries = Object.entries(pageCounts).sort((a, b) => b[1] - a[1]);
    if (pageEntries.length > 0) {
      pageEntries.forEach(([page, count]) => {
        lines.push(`${page} — ${count}`);
      });
    } else {
      lines.push('No active visitors at this moment.');
    }

    await reply(lines.join('\n'));
  } else if (text.startsWith('/status')) {
    const statusText = [
      '🟢 SFR ANALYTICS SYSTEM STATUS',
      '',
      '• Edge Network: Cloudflare Pages Functions (Global)',
      `• KV Storage: ${env.SFR_ANALYTICS ? 'Connected (SFR_ANALYTICS)' : 'Not Bound'}`,
      '• Real-time Tracking: Active',
      '• Heartbeat Interval: 25s',
      '• Session Timeout: 100s',
      '• Hourly Scheduler: 24/7 Enabled',
      '• Timezone: Asia/Ho_Chi_Minh (UTC+7)'
    ].join('\n');
    await reply(statusText);
  } else if (text.startsWith('/hour')) {
    // Forward to internal cron logic to produce on-demand hour report
    const cronUrl = new URL(request.url);
    cronUrl.pathname = '/api/cron';
    cronUrl.searchParams.set('force', '1');
    const cronRes = await fetch(cronUrl.toString());
    const cronData = await cronRes.json();
    if (cronData.preview) {
      await reply(cronData.preview);
    } else {
      await reply('Unable to generate hour summary at this time.');
    }
  }

  return new Response(JSON.stringify({ ok: true }), {
    status: 200,
    headers: { 'Content-Type': 'application/json' }
  });
}
