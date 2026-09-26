import asyncio
import os
from knowledge_base import load_project_knowledge
from notifier import extract_phone_number

def test_system():
    print("=" * 60)
    print(" KIỂM TRA HỆ THỐNG KHO DỮ LIỆU SAIGON FARM RESORT")
    print("=" * 60)
    
    # 1. Kiểm tra nạp tài liệu
    knowledge = load_project_knowledge()
    print(f"✅ Đã nạp thành công {len(knowledge)} ký tự kiến thức dự án.")
    if "Hồ Lồ Ồ" in knowledge and "MDS Living" in knowledge:
        print("✅ Dữ liệu chứa đầy đủ thông tin: Vị trí Hồ Lồ Ồ, CĐT MDS Living, các dòng sản phẩm.")
    
    # 2. Kiểm tra bộ bóc tách số điện thoại
    sample_texts = [
        "Tôi muốn hỏi giá biệt phủ, số tôi là 0908123456 nhé",
        "Alo tư vấn giúp qua zalo +84 912 345 678",
        "Chỉ muốn xem thông tin thôi chưa có sđt",
        "Gọi lại cho anh 0987.654.321 chiều nay"
    ]
    
    print("\n" + "=" * 60)
    print(" KIỂM TRA TỰ ĐỘNG BÓC TÁCH SỐ ĐIỆN THOẠI KHÁCH")
    print("=" * 60)
    for text in sample_texts:
        phone = extract_phone_number(text)
        print(f"Tin nhắn: '{text}' -> Bắt được SĐT: {phone}")

if __name__ == "__main__":
    test_system()
