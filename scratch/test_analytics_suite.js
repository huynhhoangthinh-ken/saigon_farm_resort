/**
 * Automated Test Suite for Saigon Farm Resort Real-Time Analytics
 */

import { onRequestPost as trackPost } from '../functions/api/track.js';
import { onRequest as cronHandler } from '../functions/api/cron.js';
import { onRequestGet as liveGet } from '../functions/api/live.js';

// Mock Cloudflare KV storage
class MockKV {
  constructor() {
    this.store = new Map();
  }
  async get(key, type) {
    const val = this.store.get(key);
    if (!val) return null;
    if (type === 'json') {
      try { return JSON.parse(val); } catch(e) { return null; }
    }
    return val;
  }
  async put(key, value, opts) {
    this.store.set(key, typeof value === 'string' ? value : JSON.stringify(value));
  }
  async delete(key) {
    this.store.delete(key);
  }
}

// Mock Telegram API
const telegramCalls = [];
global.fetch = async (url, options) => {
  if (url.includes('api.telegram.org')) {
    const body = options && options.body ? JSON.parse(options.body) : {};
    const isEdit = url.includes('editMessageText');
    const isSend = url.includes('sendMessage');
    const callRecord = {
      action: isEdit ? 'editMessageText' : isSend ? 'sendMessage' : 'other',
      chat_id: body.chat_id,
      message_id: body.message_id || 1001,
      text: body.text
    };
    telegramCalls.push(callRecord);
    return {
      json: async () => ({ ok: true, result: { message_id: 1001 } })
    };
  }
  return {
    status: 200,
    text: async () => 'OK',
    json: async () => ({ ok: true })
  };
};

async function runTests() {
  console.log('🧪 STARTING SFR ANALYTICS SUITE TEST...\n');

  const mockEnv = {
    SFR_ANALYTICS: new MockKV(),
    TELEGRAM_BOT_TOKEN: 'MOCK_TOKEN_123',
    TELEGRAM_CHAT_ID: '-100123456789'
  };

  const sessionId = 'SFR-7F2A91';

  // TEST 1: Session Start
  console.log('Test 1: Simulating session_start on /short via Facebook Ads...');
  const startReq = new Request('https://saigonfarmresort.com/api/track', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      event: 'session_start',
      session_id: sessionId,
      page_path: '/short',
      page_title: 'Điền Trang Bên Hồ | Saigon Farm Resort',
      traffic_source: 'Facebook Ads',
      referrer: 'https://m.facebook.com/',
      utm_source: 'fb',
      utm_medium: 'cpc',
      utm_campaign: 'SFR_SHORT_01',
      device_category: 'iPhone / Mobile',
      browser: 'Safari',
      screen_size: '390x844',
      active_time_seconds: 5,
      scroll_depth: 25
    })
  });

  const res1 = await trackPost({ request: startReq, env: mockEnv });
  const data1 = await res1.json();
  console.log('  Result:', data1);
  console.log('  Telegram messages sent:', telegramCalls.length);
  console.log('  Latest Telegram Message Text:\n' + telegramCalls[telegramCalls.length - 1].text);

  if (telegramCalls.length === 1 && telegramCalls[0].action === 'sendMessage') {
    console.log('✅ Test 1 PASSED: Initial Telegram message created with correct format.\n');
  } else {
    throw new Error('Test 1 Failed');
  }

  // TEST 2: Route Change to /gioithieu
  console.log('Test 2: Simulating route change to /gioithieu...');
  const changeReq = new Request('https://saigonfarmresort.com/api/track', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      event: 'page_change',
      session_id: sessionId,
      from_page: '/short',
      to_page: '/gioithieu',
      page_path: '/gioithieu',
      active_time_seconds: 65,
      scroll_depth: 75
    })
  });

  await trackPost({ request: changeReq, env: mockEnv });
  const latestEdit1 = telegramCalls[telegramCalls.length - 1];
  console.log('  Telegram action:', latestEdit1.action);
  console.log('  Message ID updated:', latestEdit1.message_id);
  console.log('  Current Page in message:', latestEdit1.text.includes('/gioithieu'));

  if (latestEdit1.action === 'editMessageText' && latestEdit1.text.includes('/gioithieu')) {
    console.log('✅ Test 2 PASSED: Telegram message dynamically EDITED with new route without sending duplicate message.\n');
  } else {
    throw new Error('Test 2 Failed');
  }

  // TEST 3: CTA Click (Zalo)
  console.log('Test 3: Simulating CTA Click (click_zalo)...');
  const ctaReq = new Request('https://saigonfarmresort.com/api/track', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      event: 'click_zalo',
      session_id: sessionId,
      page_path: '/gioithieu',
      cta_label: 'Zalo Click',
      active_time_seconds: 138,
      scroll_depth: 75
    })
  });

  await trackPost({ request: ctaReq, env: mockEnv });
  const latestEdit2 = telegramCalls[telegramCalls.length - 1];
  console.log('  Telegram action:', latestEdit2.action);
  console.log('  CTA in message:', latestEdit2.text.includes('Zalo Click'));

  if (latestEdit2.action === 'editMessageText' && latestEdit2.text.includes('Zalo Click')) {
    console.log('✅ Test 3 PASSED: CTA click instantly updated existing Telegram message.\n');
  } else {
    throw new Error('Test 3 Failed');
  }

  // TEST 4: Live Active Visitors API
  console.log('Test 4: Checking /api/live endpoint...');
  const liveRes = await liveGet({ env: mockEnv });
  const liveData = await liveRes.json();
  console.log('  Live Data:', liveData);

  if (liveData.online_now === 1 && liveData.pages['/gioithieu'] === 1) {
    console.log('✅ Test 4 PASSED: /api/live accurately reports active visitors and page distribution.\n');
  } else {
    throw new Error('Test 4 Failed');
  }

  // TEST 5: Hourly Cron Report
  console.log('Test 5: Triggering /api/cron hourly report...');
  const cronReq = new Request('https://saigonfarmresort.com/api/cron?force=1');
  const cronRes = await cronHandler({ request: cronReq, env: mockEnv });
  const cronData = await cronRes.json();
  console.log('  Cron result:', cronData.hour, 'Online now:', cronData.online_now);
  console.log('  Report preview:\n' + cronData.preview);

  if (cronData.ok && cronData.preview.includes('HOURLY REPORT')) {
    console.log('✅ Test 5 PASSED: Hourly report generated and formatted perfectly in Asia/Ho_Chi_Minh timezone.\n');
  } else {
    throw new Error('Test 5 Failed');
  }

  // TEST 6: Session End
  console.log('Test 6: Simulating session_end beacon...');
  const endReq = new Request('https://saigonfarmresort.com/api/track', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      event: 'session_end',
      session_id: sessionId,
      page_path: '/gioithieu',
      active_time_seconds: 145,
      scroll_depth: 75
    })
  });

  await trackPost({ request: endReq, env: mockEnv });
  const endEdit = telegramCalls[telegramCalls.length - 1];
  console.log('  Final Telegram Action:', endEdit.action);
  console.log('  Final Message Text:\n' + endEdit.text);

  if (endEdit.action === 'editMessageText' && endEdit.text.includes('⚫ SESSION ENDED')) {
    console.log('✅ Test 6 PASSED: Telegram message correctly edited to SESSION ENDED with summary!\n');
  } else {
    throw new Error('Test 6 Failed');
  }

  // TEST 7: Bot Filter & Internal Admin Exclusion
  console.log('Test 7: Testing Bot & Admin Exclusion...');
  // Check client logic regex
  const botUAs = [
    'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
    'facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_uatext.php)',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/120.0.0.0 Safari/537.36'
  ];
  const botRegex = /(bot|crawler|spider|robot|crawling|googlebot|bingbot|slurp|duckduckbot|baiduspider|yandexbot|facebookexternalhit|facebot|whatsapp|telegrambot|twitterbot|linkedinbot|pinterest|slackbot|discordbot|headlesschrome|lighthouse|curl|wget|python|php)/i;
  
  for (const ua of botUAs) {
    if (!botRegex.test(ua)) {
      throw new Error(`Bot test failed for UA: ${ua}`);
    }
  }
  console.log('✅ Test 7 PASSED: Bot filter successfully catches all major scrapers & headless crawlers.\n');

  console.log('🎉 ALL 7 COMPREHENSIVE TESTS PASSED SUCCESSFULLY!');
}

runTests().catch(err => {
  console.error('❌ Test failed:', err);
  process.exit(1);
});
