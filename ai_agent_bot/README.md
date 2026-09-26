# HƯỚNG DẪN KÍCH HOẠT AI AGENT BOT CHO FANPAGE SAIGON FARM RESORT
> **Fanpage:** [https://www.facebook.com/farmresort.sg](https://www.facebook.com/farmresort.sg)  
> **Chủ đầu tư & Vận hành:** MDS Living

---

## 1. KIẾN TRÚC HỆ THỐNG ĐÃ XÂY DỰNG
Hệ thống AI Agent Bot nằm trong thư mục `ai_agent_bot/`:
* `server.py`: FastAPI Webhook chuẩn Meta Graph API, tiếp nhận tin nhắn từ Facebook Messenger.
* `agent.py`: Trợ lý AI (Minh Thư) tích hợp Google Gemini AI đa tầng, nhớ ngữ cảnh cuộc trò chuyện.
* `knowledge_base.py`: Nạp **gần 50.000 ký tự tài liệu chuẩn** của Saigon Farm Resort (Vị trí Hồ Lồ Ồ, Hồ Tràm, 3 dòng sản phẩm Biệt Phủ, Điền Sản, Điền An, cam kết thuê 80tr/tháng, 150 đêm nghỉ dưỡng, hồ bơi khoáng muối, pháp lý sổ hồng...).
* `notifier.py`: Tự động nhận diện số điện thoại/Zalo của khách và **bắn tin nhắn cảnh báo hỏa tốc về Telegram** của bạn.

---

## 2. CÁC BƯỚC ĐỂ CHO BOT CHẠY THẬT (MẤT KHOẢNG 5-10 PHÚT)

### Bước 2.1: Cấu hình file `.env`
Nhân bản file `.env.example` thành `.env`:
```bash
cp .env.example .env
```
Mở file `.env` và điền:
1. `GEMINI_API_KEY`: Lấy miễn phí tại [Google AI Studio](https://aistudio.google.com/).
2. `TELEGRAM_BOT_TOKEN`: Chat với `@BotFather` trên Telegram -> gõ `/newbot` để tạo 1 bot nhận thông báo.
3. `TELEGRAM_CHAT_ID`: Chat với `@userinfobot` trên Telegram để lấy số ID của bạn.
4. `FB_PAGE_ACCESS_TOKEN`: Lấy từ Facebook Developer (ở Bước 2.3).

---

### Bước 2.2: Chạy Server & Mở cổng Public (Webhook URL)
Trên máy tính hoặc VPS của bạn:
```bash
cd ai_agent_bot
pip install -r requirements.txt
python server.py
```
Để Facebook kết nối được vào máy của bạn khi test, bạn dùng Cloudflare Tunnel (hoặc ngrok):
```bash
# Ví dụ dùng Cloudflare tunnel miễn phí:
cloudflared tunnel --url http://localhost:8000
# Hoặc ngrok:
ngrok http 8000
```
Bạn sẽ nhận được 1 đường link HTTPS (ví dụ: `https://xyz.trycloudflare.com` hoặc `https://abc.ngrok-free.app`).  
URL Webhook của bạn sẽ là: `https://xyz.trycloudflare.com/webhook`

---

### Bước 2.3: Kết nối với Fanpage qua Facebook Developer
1. Truy cập [developers.facebook.com](https://developers.facebook.com/) -> Bấm **Tạo ứng dụng (Create App)**.
2. Chọn loại ứng dụng: **Khác (Other)** -> **Doanh nghiệp (Business)**.
3. Thêm sản phẩm **Messenger**:
   - Ở mục **Webhooks**: Bấm **Thiết lập (Configure)**.
   - **URL gọi lại (Callback URL):** Điền `https://xyz.trycloudflare.com/webhook`
   - **Mã xác minh (Verify Token):** Điền `sfr_secret_verify_token_2026` (giống trong file `.env`).
   - Bấm **Xác minh và lưu**.
   - Bấm **Đăng ký (Subscribe)** vào sự kiện: `messages`, `messaging_postbacks`.
4. Ở mục **Tạo mã truy cập trang (Page Access Token)**:
   - Chọn Fanpage: **Saigon Farm Resort** (`https://www.facebook.com/farmresort.sg`).
   - Bấm **Generate Token**, sau đó dán mã này vào biến `FB_PAGE_ACCESS_TOKEN` trong file `.env`.

---

## 3. KỊCH BẢN CHĂM SÓC KHÁCH & LẤY LEAD ĐÃ ĐƯỢC LẬP TRÌNH SẴN

1. **Khách hỏi dự án:** AI giới thiệu vị trí vàng cạnh hồ Lồ Ồ 100ha, cách Hồ Tràm 15 phút, tiện ích 5 sao, pháp lý sổ hồng riêng.
2. **Khách hỏi chính sách đầu tư:** AI giải thích dòng tiền Điền An cam kết thuê 80tr/tháng, hoặc Biệt Phủ 150 đêm nghỉ dưỡng/năm.
3. **Mục tiêu lấy liên hệ:** AI luôn khéo léo đề nghị:
   > *"Dạ em xin phép gửi bộ tài liệu bảng giá đợt 1 và video thực tế flycam qua Zalo cho anh/chị, anh/chị cho em xin số điện thoại/Zalo để tiện gửi nhé ạ!"*
4. **Bắn thông báo:** Khi khách vừa gõ số điện thoại, điện thoại bạn sẽ rung chuông Telegram báo ngay tên khách, SĐT và nội dung chat để bạn chỉ việc bấm gọi điện chốt khách!
