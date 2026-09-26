import os
import re
import httpx
from typing import Optional, Dict, Any

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "")
FB_PAGE_ACCESS_TOKEN = os.getenv("FB_PAGE_ACCESS_TOKEN", "")

def extract_phone_number(text: str) -> Optional[str]:
    """Tìm số điện thoại Việt Nam trong nội dung tin nhắn"""
    # Khớp các dạng 09xxxxxxxx, +849xxxxxxxx, 03x, 07x, 08x, 05x, có thể có dấu cách hoặc dấu chấm
    pattern = r'(?:\+?84|0)(?:[\.\s]?[3|5|7|8|9])(?:[\.\s]?\d){8}\b'
    match = re.search(pattern, text)
    if match:
        # Chuẩn hóa về chuỗi số
        cleaned = re.sub(r'[\.\s]', '', match.group(0))
        return cleaned
    return None

async def send_telegram_alert(
    sender_id: str,
    user_message: str,
    phone_number: Optional[str] = None,
    bot_reply: Optional[str] = None
):
    """Gửi cảnh báo có khách hàng tiềm năng về Telegram của chủ đầu tư/sales"""
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID or TELEGRAM_BOT_TOKEN == "your_telegram_bot_token_here":
        print("[Telegram] Chưa cấu hình TELEGRAM_BOT_TOKEN hoặc TELEGRAM_CHAT_ID, bỏ qua thông báo.")
        return

    icon = "🔥 CÓ SỐ ĐIỆN THOẠI MỚI 🔥" if phone_number else "💬 TIN NHẮN TỪ KHÁCH MỚI"
    
    msg_lines = [
        f"<b>{icon}</b>",
        f"<b>Dự án:</b> Saigon Farm Resort (MDS Living)",
        f"<b>Facebook ID khách:</b> <code>{sender_id}</code>",
    ]

    if phone_number:
        msg_lines.append(f"📞 <b>SỐ ĐIỆN THOẠI / ZALO:</b> <b><u>{phone_number}</u></b>")
    
    msg_lines.append(f"\n<b>Nội dung khách nhắn:</b>\n<i>{user_message}</i>")

    if bot_reply:
        # Rút gọn câu trả lời của bot nếu quá dài
        short_reply = (bot_reply[:250] + "...") if len(bot_reply) > 250 else bot_reply
        msg_lines.append(f"\n<b>Bot đã phản hồi:</b>\n<i>{short_reply}</i>")

    text_to_send = "\n".join(msg_lines)
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": text_to_send,
        "parse_mode": "HTML"
    }

    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            resp = await client.post(url, json=payload)
            if resp.status_code == 200:
                print(f"[Telegram] Gửi thông báo thành công cho Sender {sender_id}")
            else:
                print(f"[Telegram Error] {resp.status_code}: {resp.text}")
    except Exception as e:
        print(f"[Telegram Exception] {e}")

async def send_typing_indicator(recipient_id: str):
    """Bật hiệu ứng 'Đang soạn tin nhắn...' trên Messenger ngay tức thì"""
    if not FB_PAGE_ACCESS_TOKEN or FB_PAGE_ACCESS_TOKEN == "your_facebook_page_access_token_here":
        return
    url = f"https://graph.facebook.com/v21.0/me/messages?access_token={FB_PAGE_ACCESS_TOKEN}"
    payload = {
        "recipient": {"id": recipient_id},
        "sender_action": "typing_on"
    }
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            await client.post(url, json=payload)
    except Exception:
        pass

async def send_facebook_message(recipient_id: str, message_text: str) -> bool:
    """Gửi tin nhắn phản hồi qua Meta Messenger Send API"""
    if not FB_PAGE_ACCESS_TOKEN or FB_PAGE_ACCESS_TOKEN == "your_facebook_page_access_token_here":
        print(f"[Facebook Mock Reply] To {recipient_id}: {message_text}")
        return True

    url = f"https://graph.facebook.com/v21.0/me/messages?access_token={FB_PAGE_ACCESS_TOKEN}"
    payload = {
        "recipient": {"id": recipient_id},
        "message": {"text": message_text},
        "messaging_type": "RESPONSE"
    }

    try:
        async with httpx.AsyncClient(timeout=15.0) as client:
            resp = await client.post(url, json=payload)
            if resp.status_code == 200:
                print(f"[Facebook API] Đã gửi tin nhắn thành công tới {recipient_id}")
                return True
            else:
                print(f"[Facebook API Error] {resp.status_code}: {resp.text}")
                return False
    except Exception as e:
        print(f"[Facebook API Exception] {e}")
        return False
