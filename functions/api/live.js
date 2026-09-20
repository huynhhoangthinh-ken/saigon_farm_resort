/**
 * Cloudflare Pages Function: /api/live
 * Returns real-time active visitor counts, active pages, and system status.
 */

export async function onRequestGet(context) {
  const { env } = context;

  if (!env.SFR_ANALYTICS) {
    return new Response(JSON.stringify({
      ok: true,
      online_now: 0,
      pages: {},
      message: 'KV storage connecting...'
    }), {
      status: 200,
      headers: { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*' }
    });
  }

  const now = Date.now();
  let activeIndex = [];
  try {
    activeIndex = (await env.SFR_ANALYTICS.get('active_sessions_index', 'json')) || [];
  } catch (e) {}

  const pageCounts = {};
  const activeSessions = [];

  for (const sid of activeIndex) {
    try {
      const sess = await env.SFR_ANALYTICS.get(`session:${sid}`, 'json');
      if (sess && !sess.ended && (now - (sess.last_heartbeat || 0) < 120000)) {
        const page = sess.current_page || '/';
        pageCounts[page] = (pageCounts[page] || 0) + 1;
        activeSessions.push({
          session_id: sess.session_id,
          visitor_code: sess.visitor_code,
          current_page: sess.current_page,
          active_time: sess.active_time_seconds,
          source: sess.traffic_source,
          campaign: sess.utm_campaign,
          status: sess.status
        });
      }
    } catch (e) {}
  }

  const totalOnline = activeSessions.length;

  // Format display string matching requirement #11
  const pageLines = Object.entries(pageCounts)
    .sort((a, b) => b[1] - a[1])
    .map(([path, count]) => `${path} — ${count}`);

  const displaySummary = [
    `ONLINE NOW: ${totalOnline}`,
    ...pageLines
  ].join('\n');

  return new Response(JSON.stringify({
    ok: true,
    online_now: totalOnline,
    pages: pageCounts,
    summary_text: displaySummary,
    active_visitors: activeSessions,
    timestamp: now
  }), {
    status: 200,
    headers: {
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*'
    }
  });
}
