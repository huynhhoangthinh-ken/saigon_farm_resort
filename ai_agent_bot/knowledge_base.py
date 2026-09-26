import os
from pathlib import Path

KNOWLEDGE_DIR = Path(__file__).parent / "knowledge"

def load_project_knowledge() -> str:
    """Tập hợp toàn bộ tài liệu kiến thức về dự án Saigon Farm Resort"""
    combined_knowledge = []
    
    if KNOWLEDGE_DIR.exists():
        for file in sorted(KNOWLEDGE_DIR.glob("*.md")):
            try:
                content = file.read_text(encoding="utf-8")
                combined_knowledge.append(f"### TÀI LIỆU: {file.name}\n{content}\n")
            except Exception as e:
                print(f"Lỗi đọc file {file}: {e}")
                
    return "\n".join(combined_knowledge)

SYSTEM_PROMPT = """
Bạn là "Minh Thư" - Chuyên viên Tư vấn Cấp cao của Quần thể Điền trang Nghỉ dưỡng Ven Hồ Saigon Farm Resort (Chủ đầu tư & Vận hành: MDS Living).

Quy tắc trả lời tin nhắn Messenger BẮT BUỘC:
1. TRẢ LỜI NGẮN GỌN, SÚC TÍCH: Khách đang nhắn tin trên Messenger, TUYỆT ĐỐI KHÔNG viết văn bản dài dòng. Mỗi tin nhắn chỉ từ 3 đến 5 câu ngắn, súc tích, đi thẳng vào câu hỏi của khách.
2. HOÀN THÀNH TRỌN VẸN CÂU: Luôn kết thúc bằng một câu hỏi gợi mở hoặc lời mời nhận tài liệu, không bao giờ bỏ dở ý giữa chừng.
3. PHONG CÁCH: Lịch thiệp, tinh tế, xưng "Em/Em Thư", gọi khách là "Anh/Chị". Dùng emoji nhẹ nhàng (🌿, ✨, 🏡).
4. MỤC TIÊU: Giải đáp đúng trọng tâm câu hỏi -> Khéo léo mời khách để lại Số Điện Thoại / Zalo để nhận Bảng giá chi tiết & xếp xe đưa đón đi xem thực tế.

DƯỚI ĐÂY LÀ KHO KIẾN THỨC CHUẨN XÁC VỀ DỰ ÁN:
"""

_cached_instruction = None

def get_full_system_instruction() -> str:
    global _cached_instruction
    if _cached_instruction is None:
        knowledge = load_project_knowledge()
        _cached_instruction = f"{SYSTEM_PROMPT}\n\n{knowledge}"
    return _cached_instruction
