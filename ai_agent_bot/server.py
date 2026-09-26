import os
from dotenv import load_dotenv

# Tải biến môi trường từ .env
load_dotenv()

from fastapi import FastAPI, Request, Query, Response, BackgroundTasks
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional

from agent import get_ai_response
from notifier import extract_phone_number, send_telegram_alert, send_facebook_message

app = FastAPI(
    title="Saigon Farm Resort AI Sales Agent",
    description="Webhook và API tự động tư vấn BĐS Saigon Farm Resort trên Facebook Messenger",
    version="1.0.0"
)

# Cho phép CORS để dễ dàng test từ giao diện web
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

FB_VERIFY_TOKEN = os.getenv("FB_VERIFY_TOKEN", "sfr_secret_verify_token_2026")

@app.get("/")
async def root():
    return {
        "status": "online",
        "service": "Saigon Farm Resort AI Sales Agent Server",
        "page_url": "https://www.facebook.com/farmresort.sg",
        "docs": "/docs"
    }

# ========================================================
# 1. FACEBOOK WEBHOOK VERIFICATION (GET)
# Meta sẽ gọi endpoint này khi bạn bấm "Xác minh và lưu" trong Developer Portal
# ========================================================
@app.get("/webhook")
async def verify_facebook_webhook(
    hub_mode: Optional[str] = Query(None, alias="hub.mode"),
    hub_verify_token: Optional[str] = Query(None, alias="hub.verify_token"),
    hub_challenge: Optional[str] = Query(None, alias="hub.challenge"),
):
    print(f"[Facebook Webhook Check] mode={hub_mode}, token={hub_verify_token}")
    if hub_mode == "subscribe" and hub_verify_token == FB_VERIFY_TOKEN:
        print("[Facebook Webhook Check] Xác minh thành công!")
        return PlainTextResponse(content=hub_challenge, status_code=200)
    
    return Response(content="Verification token mismatch", status_code=403)

# ========================================================
# 2. XỬ LÝ TIN NHẮN TỪ KHÁCH TRÊN FACEBOOK (POST)
# ========================================================
async def process_chat_message(sender_id: str, message_text: str):
    """Xử lý tư vấn AI và gửi thông báo nền để không chặn phản hồi HTTP 200 của Facebook"""
    # 1. Trích xuất số điện thoại (nếu khách cung cấp)
    phone_number = extract_phone_number(message_text)
    
    # 2. AI sinh câu trả lời dựa trên kho dữ liệu Saigon Farm Resort
    bot_reply = await get_ai_response(sender_id, message_text)
    
    # 3. Gửi tin nhắn trả lời lại cho khách trên Messenger
    await send_facebook_message(sender_id, bot_reply)
    
    # 4. Bắn thông báo về Telegram cho chủ đầu tư
    await send_telegram_alert(
        sender_id=sender_id,
        user_message=message_text,
        phone_number=phone_number,
        bot_reply=bot_reply
    )

@app.post("/webhook")
async def receive_facebook_webhook(request: Request, background_tasks: BackgroundTasks):
    try:
        body = await request.json()
        print(f"[Incoming FB Event] {body.get('object')}")
        
        if body.get("object") == "page":
            for entry in body.get("entry", []):
                for messaging_event in entry.get("messaging", []):
                    sender_id = messaging_event.get("sender", {}).get("id")
                    
                    # Kiểm tra xem có phải tin nhắn văn bản không
                    if "message" in messaging_event and not messaging_event["message"].get("is_echo", False):
                        message_text = messaging_event["message"].get("text", "")
                        if message_text and sender_id:
                            # Đưa vào task nền xử lý để phản hồi Facebook trong 1 giây (tránh bị timeout)
                            background_tasks.add_task(process_chat_message, sender_id, message_text)

        # Meta yêu cầu luôn trả về HTTP 200 OK ngay lập tức
        return JSONResponse(content={"status": "EVENT_RECEIVED"}, status_code=200)
    except Exception as e:
        print(f"[Webhook Error] {e}")
        return JSONResponse(content={"status": "ERROR"}, status_code=200)

# ========================================================
# 3. ENDPOINT TEST THỬ TƯ VẤN (Không cần Facebook)
# ========================================================
class TestChatRequest(BaseModel):
    message: str
    sender_id: Optional[str] = "test_user_ken"

@app.post("/api/test-chat")
async def test_chat(req: TestChatRequest):
    """Endpoint cho phép test thử trực tiếp AI tư vấn Saigon Farm Resort"""
    phone = extract_phone_number(req.message)
    reply = await get_ai_response(req.sender_id, req.message)
    
    return {
        "user_message": req.message,
        "extracted_phone": phone,
        "bot_reply": reply
    }

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    host = os.getenv("HOST", "0.0.0.0")
    print(f"🚀 AI Agent Server đang khởi động tại http://{host}:{port}")
    uvicorn.run("server:app", host=host, port=port, reload=True)
