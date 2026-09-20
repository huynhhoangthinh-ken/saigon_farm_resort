/**
 * Cloudflare Worker: saigonfarmresort-cron
 * 24/7 Serverless Cron Trigger (runs at minute 0 of every hour)
 * Triggers https://saigonfarmresort.com/api/cron to post hourly reports to Telegram.
 */

export default {
  async scheduled(event, env, ctx) {
    console.log(`[SFR-CRON] Triggered at ${new Date().toISOString()}`);
    try {
      const targetUrl = 'https://saigonfarmresort.com/api/cron';
      const res = await fetch(targetUrl, {
        headers: {
          'User-Agent': 'SFR-Cron-Trigger/1.0',
          'x-cron-secret': env.CRON_SECRET || ''
        }
      });
      const data = await res.text();
      console.log(`[SFR-CRON] Executed successfully (${res.status}): ${data.substring(0, 100)}`);
    } catch (err) {
      console.error('[SFR-CRON] Execution failed:', err);
    }
  },

  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    if (url.pathname === '/trigger') {
      // Manual trigger for testing
      const res = await fetch('https://saigonfarmresort.com/api/cron', {
        headers: { 'x-cron-secret': env.CRON_SECRET || '' }
      });
      return new Response(await res.text(), {
        status: res.status,
        headers: { 'Content-Type': 'application/json' }
      });
    }

    return new Response('Saigon Farm Resort 24/7 Hourly Cron Worker Active. Scheduled: 0 * * * * (Every hour).', {
      status: 200,
      headers: { 'Content-Type': 'text/plain; charset=utf-8' }
    });
  }
};
