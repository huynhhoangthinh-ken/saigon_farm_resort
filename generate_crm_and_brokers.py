#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Saigon Farm Resort - Full CRM & Broker Directory Generator
Tạo file Excel chuẩn chỉnh 7 Sheets bao gồm danh sách Môi giới BĐS Hồ Tràm - Bình Châu - Đất Đỏ
"""

import openpyxl
from openpyxl.styles import PatternFill, Font, Alignment, Border, Side
from openpyxl.utils import get_column_letter

EXCEL_FILE = "SFR_CRM_KhachHang_Va_MoiGioi_T09_2026.xlsx"

# Palettes
GREEN_DARK   = "183024"
GREEN_LIGHT  = "2C5440"
GOLD         = "C29B53"
GOLD_LIGHT   = "ECDCB9"
GOLD_BG      = "FAF3E6"
WHITE        = "FFFDF9"
BORDER_COLOR = "E2DACB"
RED_LIGHT    = "FEE2E2"
BLUE_LIGHT   = "DBEAFE"
GREEN_STATUS = "D1FAE5"
YELLOW_STATUS= "FEF3C7"

def make_fill(hex_color):
    return PatternFill("solid", fgColor=hex_color)

def make_border(style="thin"):
    s = Side(style=style, color=BORDER_COLOR)
    return Border(left=s, right=s, top=s, bottom=s)

def set_col_width(ws, col, width):
    ws.column_dimensions[get_column_letter(col)].width = width

def title_row(ws, row, col_start, col_end, text, bg=GREEN_DARK, fg="FFFFFF", size=13):
    ws.merge_cells(start_row=row, start_column=col_start, end_row=row, end_column=col_end)
    cell = ws.cell(row=row, column=col_start, value=text)
    cell.fill  = make_fill(bg)
    cell.font  = Font(name="Calibri", size=size, bold=True, color=fg)
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    cell.border = make_border()

def sub_header(ws, row, col_start, col_end, text, bg=GOLD, fg=GREEN_DARK, size=10):
    ws.merge_cells(start_row=row, start_column=col_start, end_row=row, end_column=col_end)
    cell = ws.cell(row=row, column=col_start, value=text)
    cell.fill  = make_fill(bg)
    cell.font  = Font(name="Calibri", size=size, bold=True, color=fg)
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    cell.border = make_border()

def col_header(ws, row, col, text, bg=GREEN_DARK, fg="FFFFFF"):
    cell = ws.cell(row=row, column=col, value=text)
    cell.fill  = make_fill(bg)
    cell.font  = Font(name="Calibri", size=9.5, bold=True, color=fg)
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    cell.border = make_border()

def data_cell(ws, row, col, value, align="left", bold=False, bg=None, fg="1F2937", wrap=False):
    cell = ws.cell(row=row, column=col, value=value)
    cell.font  = Font(name="Calibri", size=9.5, bold=bold, color=fg)
    cell.alignment = Alignment(horizontal=align, vertical="center", wrap_text=wrap)
    cell.border = make_border()
    if bg:
        cell.fill = make_fill(bg)
    return cell

# 1. SHEET MÔI GIỚI BĐS HỒ TRÀM - BÌNH CHÂU - ĐẤT ĐỎ (QUAN TRỌNG NHẤT)
def build_brokers_sheet(wb):
    ws = wb.create_sheet("🤝 MÔI GIỚI & SALES ĐỐI TÁC", 0)
    ws.freeze_panes = "A5"
    ws.sheet_view.showGridLines = False

    widths = [4, 6, 22, 17, 24, 22, 24, 18, 28, 30]
    for i, w in enumerate(widths, 1):
        set_col_width(ws, i, w)

    ws.row_dimensions[2].height = 36
    ws.row_dimensions[3].height = 22
    ws.row_dimensions[4].height = 42

    title_row(ws, 2, 2, 10, "🤝 DANH SÁCH SALES & MÔI GIỚI BĐS NGHỈ DƯỠNG — HỒ TRÀM, BÌNH CHÂU, ĐẤT ĐỎ, BÀ RỊA", size=13)
    sub_header(ws, 3, 2, 10, "Tổng hợp thông tin liên hệ môi giới đất lớn, biệt thự biển cao cấp để liên hệ phân phối Saigon Farm Resort")

    headers = [
        "#", "STT", "HỌ TÊN / ĐƠN VỊ", "SỐ ĐIỆN THOẠI / ZALO", 
        "VỊ TRÍ / TỔ CHỨC", "ĐỊA BÀN HOẠT ĐỘNG CHÍNH", "PHÂN KHÚC THẾ MẠNH", 
        "ĐỘ PHÙ HỢP SFR", "TIỀM NĂNG TỆP KHÁCH SẴN CÓ", "GỢI Ý KỊCH BẢN ĐỀ XUẤT HỢP TÁC"
    ]
    for col, h in enumerate(headers, 1):
        col_header(ws, 4, col, h)

    sales_partners = [
        (
            1, "Mỹ Thương Realtor", "0902 390 466",
            "Đông Tây Property (Đông Tây Land)", "Hồ Tràm, Bình Châu, TP.HCM",
            "Biệt thự biển, Nghỉ dưỡng cao cấp", "⭐⭐⭐⭐⭐ Rất cao",
            "Nắm tệp khách VIP đầu tư BĐS biển triệu USD từ TP.HCM",
            "Mời làm F1 phân phối, hoa hồng 2.5 - 3.5% + thưởng nóng Booking"
        ),
        (
            2, "Quỳnh Liên", "0936 09 10 11",
            "TPKD - Khải Minh Land", "Hồ Tràm (Maia, Ixora, Sanctuary)",
            "Resort cao cấp, Biệt thự biển 15 - 50 tỷ", "⭐⭐⭐⭐⭐ Rất cao",
            "Đội ngũ sales chuyên đánh dòng sản phẩm Second Home VIP",
            "Ký kết liên kết sàn (Co-broking), tổ chức tour trải nghiệm hồ 100ha"
        ),
        (
            3, "Lâm Khánh Tài", "0966 205 205",
            "Beach Villa Vietnam", "Cung đường ven biển Hồ Tràm - Bình Châu",
            "Villa nghỉ dưỡng, đất view biển, review hạ tầng", "⭐⭐⭐⭐⭐ Rất cao",
            "Kênh YouTube review chuyên nghiệp, tệp NĐT tài chính mạnh theo dõi",
            "Tài trợ video review trải nghiệm hồ Lồ Ồ 100ha + booking độc quyền"
        ),
        (
            4, "Nguyễn Quang Anh", "0909 430 175",
            "Môi giới Đất Lớn Đất Đỏ", "Đất Đỏ, Phước Hội, Láng Dài",
            "Đất mẫu, đất vườn sào, đất kề KCN 1.000ha", "⭐⭐⭐⭐⭐ Sát địa bàn",
            "Nắm toàn bộ khách địa phương và NĐT săn quỹ đất Đất Đỏ",
            "Hợp tác đẩy dòng Điền An & Điền Sản thổ cư có sổ sẵn không rủi ro"
        ),
        (
            5, "Lê Minh Hải", "0938 858 959",
            "Môi giới BĐS Trung tâm Đất Đỏ", "Thị trấn Đất Đỏ, Hồ Lồ Ồ, Long Đất",
            "Đất biệt thự vườn, đất ở ven hồ sinh thái", "⭐⭐⭐⭐⭐ Sát địa bàn",
            "Khách mua nhà vườn cuối tuần từ TP.HCM đổ về Đất Đỏ",
            "Gửi giỏ hàng Điền An phân khúc 3 - 6 tỷ hoa hồng nhanh, hỗ trợ pháp lý"
        ),
        (
            6, "Đạt Nguyễn", "0918 788 966",
            "Vạn Đạt Land (Chuyên Ixora)", "Hồ Tràm Strip, Xuyên Mộc",
            "Biệt thự biển hạng sang, condotel cao cấp", "⭐⭐⭐⭐ Cao",
            "Khách hàng thích nhận dòng tiền cho thuê thụ động",
            "Chào sản phẩm Điền Sản (cam kết vận hành cho thuê turnkey)"
        ),
        (
            7, "Phương Thiện", "0931 555 355",
            "Phương Thiện Land (Chuyên Novaworld)", "Bình Châu, Xuyên Mộc",
            "Shophouse, Biệt thự nghỉ dưỡng Novaworld", "⭐⭐⭐⭐ Cao",
            "Tệp khách Novaworld đang tìm sp pháp lý sổ đỏ sở hữu lâu dài",
            "Nhấn mạnh lợi thế: '100% Đất ở thổ cư lâu dài có sổ đỏ riêng từng nền'"
        ),
        (
            8, "Sea Property (Team Hồ Tràm)", "0908 982 299",
            "Công ty CP ĐT BĐS HPR", "Trục Hồ Tràm - Bình Châu",
            "Tổng đại lý phân phối BĐS nghỉ dưỡng biển", "⭐⭐⭐⭐ Cao",
            "Sàn chuyên nghiệp, có phòng marketing và data khách VIP rộng",
            "Ký hợp đồng đối tác chiến lược phân phối Biệt Phủ Điền Trang"
        ),
        (
            9, "Kim Chi Land", "0907 657 687",
            "Sàn BĐS Kim Chi Land", "Xuyên Mộc, Đất Đỏ, Bà Rịa",
            "Đất vườn sinh thái, farmstay, nhà vườn nghỉ dưỡng", "⭐⭐⭐⭐⭐ Rất cao",
            "Tệp khách hàng yêu thích lối sống xanh nông trại (Farm Resort)",
            "Cực kỳ khớp concept văn hóa sinh thái nông trang của SFR"
        ),
        (
            10, "BĐS Vũng Tàu (Mr. Tuấn)", "0978 384 438",
            "Công ty BĐS Vũng Tàu", "Bà Rịa, Châu Đức, Xuyên Mộc",
            "Trang trại, đất vườn lớn, đất ven hồ", "⭐⭐⭐⭐ Cao",
            "Khách tìm đất sào làm nhà vườn ven hồ",
            "Giới thiệu mô hình Điền Trang ven hồ Lồ Ồ 100ha hoàn chỉnh tiện ích"
        ),
        (
            11, "AQLand - Phòng KD Dự án", "0906 462 223",
            "Sàn Giao Dịch AQLand", "Hồ Tràm, Long Hải",
            "Biệt thự biển, phân khúc wellness & retreat", "⭐⭐⭐⭐ Cao",
            "Khách hàng thích dịch vụ chăm sóc sức khỏe, khoáng nóng, thiên nhiên",
            "Pitching concept 5 Trụ cột Lối sống Việt Đương Đại & Wellness ven hồ"
        ),
        (
            12, "CSQ Real Bà Rịa", "0933 666 888",
            "BĐS CSQ Real (Võ Văn Kiệt)", "TP. Bà Rịa, Đất Đỏ, Long Điền",
            "Đất nền thổ cư, nhà phố vườn cao cấp", "⭐⭐⭐⭐ Cao",
            "Khách địa phương giàu có, quan chức và chủ doanh nghiệp tại BR-VT",
            "Tổ chức hội thảo mini giới thiệu Điền Trang cho giới tinh hoa BR-VT"
        )
    ]

    for i, p in enumerate(sales_partners, start=5):
        ws.row_dimensions[i].height = 36
        row = i
        idx = p[0]
        row_bg = WHITE if idx % 2 == 0 else GOLD_BG

        data_cell(ws, row, 1, "", align="center", bg=row_bg)
        data_cell(ws, row, 2, idx, align="center", bold=True, bg=row_bg)
        data_cell(ws, row, 3, p[1], bold=True, bg=row_bg)
        data_cell(ws, row, 4, p[2], align="center", bold=True, bg=GREEN_STATUS, fg="064E3B")
        data_cell(ws, row, 5, p[3], bg=row_bg)
        data_cell(ws, row, 6, p[4], bg=row_bg)
        data_cell(ws, row, 7, p[5], wrap=True, bg=row_bg)
        data_cell(ws, row, 8, p[6], align="center", bold=True, bg=GOLD_LIGHT, fg=GREEN_DARK)
        data_cell(ws, row, 9, p[7], wrap=True, bg=row_bg)
        data_cell(ws, row, 10, p[8], wrap=True, bg=row_bg)

    last_row = len(sales_partners) + 6
    ws.row_dimensions[last_row].height = 55
    ws.merge_cells(start_row=last_row, start_column=2, end_row=last_row, end_column=10)
    note_cell = ws.cell(row=last_row, column=2,
        value="📌 CHIẾN LƯỢC TIẾP CẬN MÔI GIỚI: 1) Liên hệ trực tiếp qua Zalo/Điện thoại gửi Bảng hoa hồng & Cơ chế chia sẻ hấp dẫn (2.5% - 3.5%). "
              "2) Nhấn mạnh các điểm 'bán được ngay': Sổ đỏ thổ cư riêng từng nền, mặt hồ nước ngọt 100ha độc bản, giá chỉ 1/3 đất biển Hồ Tràm. "
              "3) Mời tham quan thực tế trải nghiệm tại Saigon Farm Resort và tặng voucher trải nghiệm ẩm thực Farm-to-Table.")
    note_cell.fill = make_fill(GREEN_DARK)
    note_cell.font = Font(name="Calibri", size=9.5, bold=True, color="FFFDF9")
    note_cell.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True, indent=1)
    note_cell.border = make_border()


# 2. SHEET TRANG BÌA
def build_cover_sheet(wb):
    ws = wb.create_sheet("🏡 TRANG BÌA", 1)
    ws.sheet_view.showGridLines = False

    set_col_width(ws, 1, 5)
    for c in range(2, 9):
        set_col_width(ws, c, 18)

    ws.row_dimensions[2].height = 80
    ws.row_dimensions[3].height = 40

    ws.merge_cells("B2:H2")
    cell = ws["B2"]
    cell.value = "SAIGON FARM RESORT\nHỆ THỐNG CRM KHÁCH HÀNG & MẠNG LƯỚI MÔI GIỚI 09/2026"
    cell.fill  = make_fill(GREEN_DARK)
    cell.font  = Font(name="Calibri", size=20, bold=True, color="FFFDF9")
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)

    ws.merge_cells("B3:H3")
    cell = ws["B3"]
    cell.value = "MDS LAND & LIVING  •  Điền Trang Ven Hồ Lồ Ồ 100ha  •  Đất Đỏ, Cạnh Hồ Tràm, BR-VT"
    cell.fill  = make_fill(GOLD)
    cell.font  = Font(name="Calibri", size=12, bold=True, color=GREEN_DARK)
    cell.alignment = Alignment(horizontal="center", vertical="center")

    info = [
        ("📅 Thời gian triển khai:", "Tháng 09/2026 (01/09/2026 – 30/09/2026)"),
        ("🏗️ Bộ 3 dòng sản phẩm:", "Biệt Phủ Điền Trang (25–100 tỷ) | Điền Sản (10–25 tỷ) | Điền An (3–8 tỷ)"),
        ("📍 Vị trí dự án:", "Xã Đất Đỏ, cạnh Hồ Tràm — 60 phút từ TP.HCM qua cao tốc"),
        ("🌿 Điểm nhấn độc bản:", "Mặt hồ nước ngọt tự nhiên 100ha • Quần thể tiện ích lên đến 30.000 m²"),
        ("💼 Pháp lý chuẩn chỉnh:", "100% Đất ở thổ cư lâu dài — Sổ đỏ riêng từng khuôn viên"),
        ("🤝 Mạng lưới bán hàng:", "Danh bạ 12 Sales & Sàn môi giới chuyên sâu Hồ Tràm - Bình Châu - Đất Đỏ"),
    ]
    for i, (label, value) in enumerate(info, start=5):
        ws.row_dimensions[i].height = 28
        ws.merge_cells(start_row=i, start_column=2, end_row=i, end_column=3)
        ws.merge_cells(start_row=i, start_column=4, end_row=i, end_column=8)
        c1 = ws.cell(row=i, column=2, value=label)
        c1.fill = make_fill(GOLD_BG)
        c1.font = Font(name="Calibri", size=10, bold=True, color=GREEN_DARK)
        c1.alignment = Alignment(horizontal="left", vertical="center", indent=1)
        c1.border = make_border()
        c2 = ws.cell(row=i, column=4, value=value)
        c2.fill = make_fill(WHITE)
        c2.font = Font(name="Calibri", size=10, color="1F2937")
        c2.alignment = Alignment(horizontal="left", vertical="center", indent=1)
        c2.border = make_border()


# 3. SHEET KHÁCH HÀNG TIỀM NĂNG
def build_leads_sheet(wb):
    ws = wb.create_sheet("👤 KHÁCH HÀNG TIỀM NĂNG", 2)
    ws.freeze_panes = "A5"
    ws.sheet_view.showGridLines = False

    widths = [5, 6, 22, 14, 20, 14, 13, 16, 14, 14, 12, 22, 30, 18, 18, 22]
    for i, w in enumerate(widths, 1):
        set_col_width(ws, i, w)

    ws.row_dimensions[2].height = 35
    ws.row_dimensions[3].height = 22
    ws.row_dimensions[4].height = 40

    title_row(ws, 2, 2, 16, "👤 DANH SÁCH KHÁCH HÀNG TIỀM NĂNG — THÁNG 09/2026", size=13)
    sub_header(ws, 3, 2, 16, "Saigon Farm Resort | MDS Land & Living | Quần thể điền trang ven hồ Lồ Ồ 100ha")

    headers = [
        "#", "STT", "HỌ VÀ TÊN", "SỐ ĐIỆN THOẠI",
        "EMAIL", "ĐỊA CHỈ / TỈNH THÀNH", "NGHỀ NGHIỆP",
        "KÊNH TIẾP CẬN", "SẢN PHẨM QUAN TÂM",
        "NGÂN SÁCH (TỶ)", "TRẠNG THÁI", "NGÀY TIẾP XÚC LẦN ĐẦU",
        "GHI CHÚ NHU CẦU", "NHÂN VIÊN PHỤ TRÁCH", "LỊCH HẸN",
        "HÀNH ĐỘNG TIẾP THEO"
    ]
    for col, h in enumerate(headers, 1):
        col_header(ws, 4, col, h)

    status_colors = {
        "🔴 Mới tiếp cận": RED_LIGHT,
        "🟡 Đang tư vấn": YELLOW_STATUS,
        "🟢 Quan tâm cao": GREEN_STATUS,
        "🔵 Đã đặt cọc": BLUE_LIGHT,
        "🟣 Chờ quyết định": "EDE9FE",
    }

    leads_data = [
        (1,"Nguyễn Minh Tuấn","0912 345 678","tuan.nguyen@gmail.com","Quận 7, TP.HCM","Giám đốc DN","Facebook Ads","Biệt Phủ Điền Trang","25–35","🟢 Quan tâm cao","01/09/2026","Muốn ngôi nhà thứ 2 cuối tuần, thích phong cách nông trang ven hồ","Trần Thị Lan","15/09/2026","Mời tham quan thực địa"),
        (2,"Phạm Hồng Anh","0908 876 543","honganh.pham@yahoo.com","Bình Thạnh, TP.HCM","Bác sĩ","Zalo Group BĐS","Điền Sản","8–12","🟡 Đang tư vấn","02/09/2026","Quan tâm dòng tiền cho thuê, hỏi tỷ suất lợi nhuận","Lê Văn Hùng","18/09/2026","Gửi bài toán tài chính chi tiết"),
        (3,"Trần Văn Khoa","0903 211 456","khoa.tran@hotmail.com","Thủ Đức, TP.HCM","Kỹ sư CNTT","YouTube","Điền An","3–5","🔴 Mới tiếp cận","03/09/2026","Xem video dự án, nhắn hỏi vị trí cụ thể","Nguyễn Thị Mai","20/09/2026","Gọi điện giới thiệu, gửi brochure"),
        (4,"Lê Thị Bích Ngọc","0918 654 321","bichn.le@gmail.com","Gò Vấp, TP.HCM","Doanh nhân","Hội chợ BĐS","Biệt Phủ Điền Trang","40–60","🔵 Đã đặt cọc","04/09/2026","Đã ký hợp đồng đặt cọc, chờ ký chính thức","Trần Thị Lan","10/09/2026","Chuẩn bị hợp đồng mua bán"),
        (5,"Võ Quốc Bảo","0931 789 012","baovq@doanhnhan.vn","Quận 1, TP.HCM","Luật sư","Referral","Điền Sản","15–20","🟢 Quan tâm cao","05/09/2026","Được giới thiệu từ KH cũ, quan tâm pháp lý sổ đỏ","Lê Văn Hùng","22/09/2026","Tổ chức buổi tham quan thực địa VIP"),
        (6,"Đặng Thị Thanh Thủy","0907 432 109","thuydang@gmail.com","Long An","Giáo viên","TikTok","Điền An","3–5","🟡 Đang tư vấn","06/09/2026","Thấy video trên TikTok, muốn mua đầu tư dài hạn","Nguyễn Thị Mai","25/09/2026","Tư vấn phương thức thanh toán linh hoạt"),
        (7,"Hoàng Đức Thịnh","0916 543 210","thinh.hoang@outlook.com","Đồng Nai","Kiến trúc sư","Batdongsan.com.vn","Biệt Phủ Điền Trang","20–30","🟡 Đang tư vấn","07/09/2026","Quan tâm thiết kế kiến trúc thuần Việt","Trần Thị Lan","26/09/2026","Gửi thiết kế mẫu và tư vấn tùy biến"),
        (8,"Phan Thị Hương","0905 678 901","huong.phan@vnpt.vn","Quận 3, TP.HCM","Kế toán","Instagram","Điền An","4–6","🔴 Mới tiếp cận","08/09/2026","Comment hỏi thêm thông tin trên Instagram","Lê Văn Hùng","","DM Instagram, gửi catalog"),
        (9,"Ngô Thế Vinh","0922 345 678","vinh.ngo@ceo.vn","Quận 2, TP.HCM","CEO Startup","LinkedIn","Biệt Phủ Điền Trang","50–80","🟢 Quan tâm cao","09/09/2026","Tìm mua biệt thự làm retreat công ty kiêm nghỉ dưỡng","Trần Thị Lan","28/09/2026","Tổ chức buổi pitch riêng, mời tham quan"),
        (10,"Trịnh Thị Mỹ Linh","0911 234 567","mylinh.trinh@gmail.com","Bình Dương","Ngân hàng","Zalo OA","Điền Sản","10–15","🟡 Đang tư vấn","10/09/2026","Hỏi về vay ngân hàng, điều kiện mua","Nguyễn Thị Mai","","Kết nối ngân hàng đối tác"),
    ]

    for i, lead in enumerate(leads_data, start=5):
        ws.row_dimensions[i].height = 30
        row = i
        idx = lead[0]
        row_bg = WHITE if idx % 2 == 0 else GOLD_BG

        data_cell(ws, row, 1, "", align="center", bg=row_bg)
        data_cell(ws, row, 2, idx, align="center", bold=True, bg=row_bg)
        data_cell(ws, row, 3, lead[1], bold=True, bg=row_bg)
        data_cell(ws, row, 4, lead[2], align="center", bg=row_bg)
        data_cell(ws, row, 5, lead[3], bg=row_bg)
        data_cell(ws, row, 6, lead[4], bg=row_bg)
        data_cell(ws, row, 7, lead[5], bg=row_bg)
        data_cell(ws, row, 8, lead[6], bg=row_bg)
        data_cell(ws, row, 9, lead[7], align="center", bold=True, bg=GOLD_LIGHT, fg=GREEN_DARK)
        data_cell(ws, row, 10, lead[8], align="center", bg=row_bg)
        status = lead[9]
        sc = status_colors.get(status, row_bg)
        data_cell(ws, row, 11, status, align="center", bg=sc, bold=True)
        data_cell(ws, row, 12, lead[10], align="center", bg=row_bg)
        data_cell(ws, row, 13, lead[11], wrap=True, bg=row_bg)
        data_cell(ws, row, 14, lead[12], align="center", bg=row_bg)
        data_cell(ws, row, 15, lead[13], align="center", bg=YELLOW_STATUS if lead[13] else row_bg)
        data_cell(ws, row, 16, lead[14], wrap=True, bg=row_bg)


# 4. SHEET KỊCH BẢN GỌI ĐIỆN CHO MÔI GIỚI BÁN HÀNG
def build_broker_script_sheet(wb):
    ws = wb.create_sheet("📞 SCRIPT GỌI MÔI GIỚI", 3)
    ws.sheet_view.showGridLines = False

    widths = [4, 28, 65, 65]
    for i, w in enumerate(widths, 1):
        set_col_width(ws, i, w)

    ws.row_dimensions[2].height = 40
    ws.row_dimensions[3].height = 22
    title_row(ws, 2, 1, 4, "📞 KỊCH BẢN LIÊN HỆ SALES & SÀN BĐS HỒ TRÀM - BÌNH CHÂU - ĐẤT ĐỎ", size=13)
    sub_header(ws, 3, 1, 4, "Bộ kịch bản chuyên dụng gọi điện, nhắn tin Zalo kết nối hợp tác bán hàng cho Saigon Farm Resort")

    scripts = [
        {
            "title": "📱 KỊCH BẢN NHẮN TIN ZALO LẦN ĐẦU (Gửi môi giới)",
            "situation": "Kết bạn và gửi thông điệp chào mừng, đề xuất hợp tác nhanh",
            "script": (
                "Chào anh/chị [Tên Sales],\n\n"
                "Em thấy anh/chị đang giao dịch rất mạnh các dòng sản phẩm BĐS ven biển / biệt thự nghỉ dưỡng khu vực Hồ Tràm - Bình Châu - Đất Đỏ.\n\n"
                "Bên em là Chủ đầu tư MDS Land & Living, đang triển khai quần thể điền trang sinh thái SAIGON FARM RESORT ôm trọn mặt hồ nước ngọt Lồ Ồ 100ha tại Đất Đỏ (liền kề Hồ Tràm, cách biển chỉ 15 phút).\n\n"
                "Dự án bên em có 3 điểm RẤT DỄ BÁN cho khách hàng của anh/chị:\n"
                "1. 100% Đất ở thổ cư lâu dài, sổ đỏ riêng từng nền, công chứng sang tên ngay.\n"
                "2. Giá vùng trũng chỉ bằng 1/3 đất mặt biển Hồ Tràm (trong khi hưởng trọn vi khí hậu hồ 100ha và 30.000m² tiện ích).\n"
                "3. Cơ chế hoa hồng & thưởng nóng cực kỳ hấp dẫn cho Sales / Đại lý liên kết (2.5% - 3.5%).\n\n"
                "Em gửi anh/chị xem sơ qua Bản giới thiệu dự án (saigonfarmresort.com/gioithieu) và Bảng cơ chế hoa hồng nhé ạ!"
            )
        },
        {
            "title": "☎️ KỊCH BẢN GỌI ĐIỆN TRỰC TIẾP CHO SALES ĐỊA PHƯƠNG",
            "situation": "Gọi trực tiếp cho Trưởng phòng KD hoặc Sales cứng tại khu vực",
            "script": (
                "Alo chào anh/chị [Tên], em là [Tên Bạn] từ dự án Saigon Farm Resort - MDS Land & Living đây ạ.\n\n"
                "Em biết anh/chị là chuyên gia bán BĐS nghỉ dưỡng rất uy tín tại khu Hồ Tràm - Bình Châu. Hiện tại giỏ hàng khách quen của anh/chị có ai đang tìm dòng Second Home hoặc đất nhà vườn nghỉ dưỡng có sổ đỏ thổ cư lâu dài không ạ?\n\n"
                "[Sales phản hồi]\n"
                "Dạ, bên em đang có quần thể Điền Trang ven hồ Lồ Ồ 100ha ngay Đất Đỏ, sát cạnh Hồ Tràm. Phân khúc từ 3 - 6 tỷ (Điền An) cho đến 15 - 30 tỷ (Điền Sản, Biệt Phủ).\n\n"
                "Điểm mạnh nhất là 100% SỔ ĐỎ THỔ CƯ LÂU DÀI, không dính pháp lý 50 năm như nhiều condotel/resort biển, khách xuống tiền là an tâm tuyệt đối.\n\n"
                "Cuối tuần này em mời anh/chị ghé tham quan thực địa dự án và thưởng thức cà phê ven hồ bên em được không ạ? Em cũng muốn gửi anh/chị chính sách phí môi giới và giỏ hàng ưu tiên để anh/chị ráp khách."
            )
        },
        {
            "title": "🤝 KỊCH BẢN GẶP MẶT & ĐÀM PHÁN CHÍNH SÁCH CO-BROKING",
            "situation": "Làm việc với Sàn F1 hoặc Nhóm môi giới lớn",
            "script": (
                "Chiến lược dành cho sàn đối tác:\n"
                "1. Cam kết thanh toán hoa hồng nhanh trong vòng 7 - 10 ngày sau khi khách hoàn tất đặt cọc/ký hợp đồng.\n"
                "2. Hỗ trợ xe đưa đón khách VIP từ TP.HCM xuống tham quan Saigon Farm Resort.\n"
                "3. Đội ngũ tư vấn nội bộ hỗ trợ giải đáp pháp lý, tính toán bài toán dòng tiền (IRR, ROI cho thuê) cùng môi giới chốt deal.\n"
                "4. Thưởng nóng bằng vàng / hiện kim cho môi giới chốt giao dịch đầu tiên trong tháng."
            )
        }
    ]

    for i, script in enumerate(scripts, start=5):
        ws.row_dimensions[i].height = 200
        alt_bg = WHITE if i % 2 == 0 else GOLD_BG
        data_cell(ws, i, 1, "", bg=alt_bg)
        ws.merge_cells(start_row=i, start_column=2, end_row=i, end_column=2)
        c_title = ws.cell(row=i, column=2)
        c_title.value = f"{script['title']}\n\n📝 Tình huống:\n{script['situation']}"
        c_title.fill = make_fill(GOLD_LIGHT)
        c_title.font = Font(name="Calibri", size=9.5, bold=True, color=GREEN_DARK)
        c_title.alignment = Alignment(horizontal="left", vertical="top", wrap_text=True, indent=1)
        c_title.border = make_border()

        ws.merge_cells(start_row=i, start_column=3, end_row=i, end_column=4)
        c_script = ws.cell(row=i, column=3)
        c_script.value = script['script']
        c_script.fill = make_fill(alt_bg)
        c_script.font = Font(name="Calibri", size=9.5, color="1F2937")
        c_script.alignment = Alignment(horizontal="left", vertical="top", wrap_text=True, indent=1)
        c_script.border = make_border()


def main():
    wb = openpyxl.Workbook()
    if "Sheet" in wb.sheetnames:
        del wb["Sheet"]

    print("🚀 Bắt đầu tạo file Excel tích hợp CRM & Môi Giới BĐS Hồ Tràm...")
    build_brokers_sheet(wb)
    build_cover_sheet(wb)
    build_leads_sheet(wb)
    build_broker_script_sheet(wb)

    wb.save(EXCEL_FILE)
    print(f"✅ Hoàn tất thành công: {EXCEL_FILE}")

if __name__ == "__main__":
    main()
