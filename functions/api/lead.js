/**
 * Cloudflare Pages Function: /api/lead
 * Receives consultation requests from the Saigon Farm Resort mobile app,
 * stores them in KV and notifies the sales Telegram chat.
 */

const CORS = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Methods': 'POST, OPTIONS',
  'Access-Control-Allow-Headers': 'Content-Type',
};

const json = (body, status = 200) =>
  new Response(JSON.stringify(body), { status, headers: { 'Content-Type': 'application/json', ...CORS } });

const clean = (v, max) => String(v ?? '').replace(/[\u0000-\u001f]/g, ' ').trim().slice(0, max);

export async function onRequestOptions() {
  return new Response(null, { status: 204, headers: CORS });
}

export async function onRequestPost({ request, env }) {
  let data;
  try {
    data = await request.json();
  } catch {
    return json({ ok: false, error: 'invalid_json' }, 400);
  }

  const name = clean(data.name, 80);
  const phone = clean(data.phone, 20).replace(/[\s.-]/g, '');
  const note = clean(data.note, 500);
  const lot = clean(data.lot, 10);
  const source = clean(data.source, 30) || 'app';

  if (name.length < 2 || !/^(\+?84|0)\d{9,10}$/.test(phone)) {
    return json({ ok: false, error: 'invalid_input' }, 400);
  }

  const now = new Date();
  const vnTime = now.toLocaleString('vi-VN', { timeZone: 'Asia/Ho_Chi_Minh' });
  const lead = { name, phone, note, lot, source, created_at: now.toISOString() };

  if (env.SFR_ANALYTICS) {
    try {
      await env.SFR_ANALYTICS.put(`lead:${now.getTime()}:${phone}`, JSON.stringify(lead), { expirationTtl: 60 * 60 * 24 * 365 });
    } catch (e) {}
  }

  if (env.TELEGRAM_BOT_TOKEN && env.TELEGRAM_CHAT_ID) {
    const text = [
      '📲 KHÁCH ĐĂNG KÝ TƯ VẤN (APP)',
      '',
      `Họ tên: ${name}`,
      `SĐT: ${phone}`,
      lot ? `Lô quan tâm: ${lot}` : null,
      note ? `Nhu cầu: ${note}` : null,
      `Nguồn: ${source}`,
      `Thời gian: ${vnTime}`,
    ].filter(Boolean).join('\n');
    try {
      await fetch(`https://api.telegram.org/bot${env.TELEGRAM_BOT_TOKEN}/sendMessage`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ chat_id: env.TELEGRAM_CHAT_ID, text }),
      });
    } catch (e) {}
  }

  return json({ ok: true });
}
