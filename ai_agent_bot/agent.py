import os
import json
import httpx
from typing import Dict, List
from knowledge_base import get_full_system_instruction

# Quản lý lịch sử hội thoại trong bộ nhớ tạm thời theo Facebook PSID
conversation_histories: Dict[str, List[Dict[str, str]]] = {}

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-3.7-flash")

async def get_ai_response(sender_id: str, user_message: str) -> str:
    """Gọi Gemini REST API tương thích trực tiếp với khóa API xác thực"""
    api_key = os.getenv("GEMINI_API_KEY", "")
    
    if not api_key or api_key == "your_gemini_api_key_here":
        return (
            "Dạ em chào Anh/Chị! Em là Minh Thư - Trợ lý tư vấn Saigon Farm Resort. "
            "Anh/Chị vui lòng để lại Số điện thoại hoặc liên hệ trực tiếp Hotline MDS Living để em gửi bảng giá ngay nhé ạ! 🌿"
        )
    
    if sender_id not in conversation_histories:
        conversation_histories[sender_id] = []
        
    history = conversation_histories[sender_id]
    
    # Định dạng contents cho Gemini REST API
    contents = []
    for turn in history[-6:]:
        contents.append({
            "role": turn["role"],
            "parts": [{"text": turn["text"]}]
        })
        
    contents.append({
        "role": "user",
        "parts": [{"text": user_message}]
    })
    
    system_instruction = get_full_system_instruction()
    
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL_NAME}:generateContent?key={api_key}"
    payload = {
        "systemInstruction": {
            "parts": [{"text": system_instruction}]
        },
        "contents": contents,
        "generationConfig": {
            "temperature": 0.6,
            "maxOutputTokens": 1500
        }
    }
    
    try:
        async with httpx.AsyncClient(timeout=25.0) as client:
            resp = await client.post(url, json=payload, headers={"Content-Type": "application/json"})
            if resp.status_code == 200:
                data = resp.json()
                reply_text = data["candidates"][0]["content"]["parts"][0]["text"].strip()
                
                # Lưu lịch sử chat
                history.append({"role": "user", "text": user_message})
                history.append({"role": "model", "text": reply_text})
                
                if len(history) > 12:
                    conversation_histories[sender_id] = history[-12:]
                    
                return reply_text
            else:
                print(f"[Gemini REST Error] {resp.status_code}: {resp.text}")
                return (
                    "Dạ em cảm ơn Anh/Chị đã quan tâm Saigon Farm Resort. "
                    "Anh/Chị cho em xin số điện thoại/Zalo để em gửi trọn bộ thông tin bảng giá và hồ sơ pháp lý qua cho anh/chị ngay nhé ạ! 🏡"
                )
    except Exception as e:
        print(f"[Gemini Exception] {e}")
        return (
            "Dạ em cảm ơn Anh/Chị. Anh/Chị cho em xin số điện thoại/Zalo để em gửi bảng giá chi tiết qua cho anh/chị ngay nhé ạ! 🌿"
        )
