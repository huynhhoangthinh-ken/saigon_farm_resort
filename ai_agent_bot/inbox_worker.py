import asyncio
import os
import httpx
from dotenv import load_dotenv

# Tải cấu hình
load_dotenv()

from agent import get_ai_response
from notifier import extract_phone_number, send_telegram_alert, send_facebook_message, send_typing_indicator

PAGE_ID = "1206949772510945"
PAGE_ACCESS_TOKEN = os.getenv("FB_PAGE_ACCESS_TOKEN", "")

# Tập hợp lưu các tin nhắn đã trả lời để không trả lời trùng lặp
processed_message_ids = set()

async def init_processed_messages():
    """Nạp các ID tin nhắn cũ để không trả lời lại quá khứ khi vừa khởi động bot"""
    global processed_message_ids
    if not PAGE_ACCESS_TOKEN:
        return
    
    url = f"https://graph.facebook.com/v21.0/{PAGE_ID}/conversations?fields=messages.limit(20){{id,from}}&access_token={PAGE_ACCESS_TOKEN}"
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            resp = await client.get(url)
            if resp.status_code == 200:
                data = resp.json()
                for conv in data.get("data", []):
                    for msg in conv.get("messages", {}).get("data", []):
                        processed_message_ids.add(msg["id"])
                print(f"🤖 [Auto-Pilot] Đã ghi nhớ {len(processed_message_ids)} tin nhắn cũ. Sẵn sàng đón khách mới!")
    except Exception as e:
        print(f"[Init Error] {e}")

async def run_autopilot_inbox_worker():
    """Vòng lặp tự động online 24/7 kiểm tra hộp thư mỗi 2 giây"""
    await init_processed_messages()
    print("🚀 [Auto-Pilot Online] Bot AI Minh Thư đang trực chiến hộp thư Fanpage 24/7...")

    while True:
        try:
            url = f"https://graph.facebook.com/v21.0/{PAGE_ID}/conversations?fields=messages.limit(5){{id,message,from,created_time}}&access_token={PAGE_ACCESS_TOKEN}"
            async with httpx.AsyncClient(timeout=8.0) as client:
                resp = await client.get(url)
                if resp.status_code == 200:
                    data = resp.json()
                    for conv in data.get("data", []):
                        messages = conv.get("messages", {}).get("data", [])
                        if not messages:
                            continue
                        
                        latest_msg = messages[0]
                        msg_id = latest_msg.get("id")
                        sender_id = latest_msg.get("from", {}).get("id")
                        sender_name = latest_msg.get("from", {}).get("name", "Khách hàng")
                        msg_text = latest_msg.get("message", "")

                        # Nếu tin nhắn này là của KHÁCH HÀNG (không phải Page tự nói) và CHƯA xử lý
                        if sender_id and sender_id != PAGE_ID and msg_id not in processed_message_ids:
                            processed_message_ids.add(msg_id)
                            print(f"\n📩 [CÓ KHÁCH NHẮN] Từ: {sender_name} ({sender_id})")
                            print(f"   Nội dung: \"{msg_text}\"")

                            # 1. Bật ngay hiệu ứng "Đang soạn tin nhắn..." để khách thấy phản hồi lập tức
                            asyncio.create_task(send_typing_indicator(sender_id))

                            # 2. Trích xuất số điện thoại nếu khách gửi
                            phone = extract_phone_number(msg_text)
                            if phone:
                                print(f"🔥 [TÌM THẤY SĐT] {phone}")

                            # 3. Gọi AI Minh Thư sinh câu trả lời theo kho dữ liệu
                            print("🤖 [AI Minh Thư] Đang suy nghĩ câu trả lời...")
                            reply_text = await get_ai_response(sender_id, msg_text)

                            # 4. Gửi câu trả lời cho khách trên Messenger
                            sent = await send_facebook_message(sender_id, reply_text)
                            if sent:
                                print(f"✅ [Đã trả lời khách]: \"{reply_text[:60]}...\"")

                            # 5. Rung chuông báo về Telegram cho chủ nhân
                            await send_telegram_alert(
                                sender_id=f"{sender_name} ({sender_id})",
                                user_message=msg_text,
                                phone_number=phone,
                                bot_reply=reply_text
                            )
                else:
                    if resp.status_code == 400:
                        print(f"[Inbox Polling Token Error] {resp.text}")
                        await asyncio.sleep(4)
        except Exception as e:
            pass

        # Quét siêu nhanh mỗi 1.2 giây
        await asyncio.sleep(1.2)

if __name__ == "__main__":
    asyncio.run(run_autopilot_inbox_worker())
