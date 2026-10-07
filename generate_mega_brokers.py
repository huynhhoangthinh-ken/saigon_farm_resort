#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Saigon Farm Resort - MEGA BROKER & SALES NETWORK DIRECTORY (30 ĐỐI TÁC CHIẾN LƯỢC)
Mở rộng theo 4 nhóm logic:
1. Nhóm 1: Địa phương Đất Đỏ - Xuyên Mộc - Bà Rịa (Đất lớn, am hiểu thổ địa)
2. Nhóm 2: Chuyên viên Biệt thự biển Hồ Tràm - Bình Châu (Khách VIP triệu USD)
3. Nhóm 3: Đại lý BĐS Nhà Vườn Sinh Thái & Ven Sông TP.Thủ Đức / Long Thành / Nhơn Trạch
4. Nhóm 4: Các Sàn Master Broker & Sàn phân phối F1 Nghỉ Dưỡng TP.HCM
"""

import openpyxl
from openpyxl.styles import PatternFill, Font, Alignment, Border, Side
from openpyxl.utils import get_column_letter

EXCEL_FILE = "SFR_CRM_KhachHang_Va_MoiGioi_T09_2026.xlsx"
DESKTOP_FILE = "/Users/kenhuynh/Desktop/SFR_CRM_KhachHang_Va_MoiGioi_T09_2026.xlsx"

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
PURPLE_LIGHT = "EDE9FE"

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

def group_header(ws, row, col_start, col_end, text, bg=GREEN_LIGHT, fg="FFFFFF"):
    ws.merge_cells(start_row=row, start_column=col_start, end_row=row, end_column=col_end)
    cell = ws.cell(row=row, column=col_start, value=text)
    cell.fill  = make_fill(bg)
    cell.font  = Font(name="Calibri", size=10.5, bold=True, color=fg)
    cell.alignment = Alignment(horizontal="left", vertical="center", indent=1)
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


def build_mega_brokers(wb):
    ws = wb.create_sheet("🤝 MÔI GIỚI & SALES ĐỐI TÁC", 0)
    ws.freeze_panes = "A5"
    ws.sheet_view.showGridLines = False

    widths = [4, 6, 22, 17, 24, 22, 24, 18, 28, 30]
    for i, w in enumerate(widths, 1):
        set_col_width(ws, i, w)

    ws.row_dimensions[2].height = 36
    ws.row_dimensions[3].height = 22
    ws.row_dimensions[4].height = 42

    title_row(ws, 2, 2, 10, "🤝 MẠNG LƯỚI 30 SALES & SÀN BĐS ĐỐI TÁC PHÂN PHỐI SAIGON FARM RESORT", size=13)
    sub_header(ws, 3, 2, 10, "Mở rộng 4 nhóm logic: Địa phương Đất Đỏ • Biệt thự biển Hồ Tràm • Nhà vườn sinh thái TP.HCM/Đồng Nai • Đại lý Master Broker")

    headers = [
        "#", "STT", "HỌ TÊN / ĐƠN VỊ", "SỐ ĐIỆN THOẠI / ZALO", 
        "VỊ TRÍ / TỔ CHỨC", "ĐỊA BÀN HOẠT ĐỘNG CHÍNH", "PHÂN KHÚC THẾ MẠNH", 
        "ĐỘ PHÙ HỢP SFR", "TIỀM NĂNG TỆP KHÁCH SẴN CÓ", "GỢI Ý KỊCH BẢN ĐỀ XUẤT HỢP TÁC"
    ]
    for col, h in enumerate(headers, 1):
        col_header(ws, 4, col, h)

    # 30 Brokers in 4 logical groups
    groups = [
        {
            "name": "📍 NHÓM 1: ĐỊA PHƯƠNG ĐẤT ĐỎ - BÀ RỊA - CHÂU ĐỨC (NẮM ĐẤT MẪU, ĐẤT VƯỜN & KHÁCH ĐỊA PHƯƠNG)",
            "partners": [
                (1, "Nguyễn Quang Anh", "0909 430 175", "Môi giới Đất Lớn Đất Đỏ", "Đất Đỏ, Phước Hội, Láng Dài", "Đất mẫu, đất sào, đất kề KCN 1.000ha", "⭐⭐⭐⭐⭐ Cực sát địa bàn", "Khách địa phương và NĐT săn quỹ đất Đất Đỏ", "Hợp tác giỏ hàng Điền An thổ cư có sổ sẵn, cam kết pháp lý sạch"),
                (2, "Lê Minh Hải", "0938 858 959", "BĐS Trung tâm Đất Đỏ", "Thị trấn Đất Đỏ, Hồ Lồ Ồ, Long Đất", "Đất biệt thự vườn, đất ở ven hồ", "⭐⭐⭐⭐⭐ Cực sát địa bàn", "Khách mua nhà vườn cuối tuần từ TP.HCM đổ về", "Gửi giỏ hàng Điền An phân khúc 3 - 6 tỷ hoa hồng nhanh"),
                (3, "CSQ Real Bà Rịa", "0933 666 888", "BĐS CSQ Real (Võ Văn Kiệt)", "TP. Bà Rịa, Đất Đỏ, Long Điền", "Đất nền thổ cư, nhà phố vườn cao cấp", "⭐⭐⭐⭐ Rất cao", "Giới tinh hoa, chủ doanh nghiệp tại tỉnh BR-VT", "Tổ chức hội thảo mini giới thiệu Điền Trang cho VIP BR-VT"),
                (4, "Kim Chi Land", "0907 657 687", "Sàn BĐS Kim Chi Land", "Xuyên Mộc, Đất Đỏ, Bà Rịa", "Đất vườn sinh thái, farmstay, nhà vườn", "⭐⭐⭐⭐⭐ Khớp 100% Concept", "Khách yêu thích lối sống xanh nông trại (Farm Resort)", "Cực kỳ khớp concept nông trang sinh thái ven hồ 100ha"),
                (5, "BĐS Vũng Tàu (Mr. Tuấn)", "0978 384 438", "Công ty BĐS Vũng Tàu", "Bà Rịa, Châu Đức, Xuyên Mộc", "Trang trại, đất vườn lớn, đất ven hồ", "⭐⭐⭐⭐ Cao", "Khách săn đất sào làm nhà vườn ven hồ", "Giới thiệu mô hình Điền Trang ven hồ Lồ Ồ hoàn chỉnh tiện ích"),
                (6, "BĐS Tiền Land Long Hải", "0908 123 789", "Tiền Land (Võ Thị Sáu, Long Hải)", "Long Hải, Phước Hải, Đất Đỏ", "Đất nghỉ dưỡng ven biển & ven hồ", "⭐⭐⭐⭐ Cao", "Khách chuộng nghỉ dưỡng sinh thái gần biển", "Liên kết Co-broking, chia sẻ hoa hồng 3%"),
                (7, "Nhà Đất Châu Đức (Mr. Hùng)", "0913 888 678", "Văn phòng BĐS Châu Đức", "Châu Đức, giáp ranh Đất Đỏ", "Đất vườn hồ Suối Rao, hồ Sông Ray", "⭐⭐⭐⭐ Cao", "Khách thích làm trang trại, homestay ven hồ", "Định vị SFR là phiên bản cao cấp chuẩn resort 5 sao"),
            ]
        },
        {
            "name": "🏖️ NHÓM 2: CHUYÊN VIÊN & SÀN BIỆT THỰ BIỂN HỒ TRÀM - BÌNH CHÂU (KHÁCH VIP TRIỆU USD)",
            "partners": [
                (8, "Mỹ Thương Realtor", "0902 390 466", "Đông Tây Property", "Hồ Tràm, Bình Châu, TP.HCM", "Biệt thự biển, Nghỉ dưỡng cao cấp", "⭐⭐⭐⭐⭐ Cực cao", "Tệp khách VIP đầu tư BĐS biển triệu USD từ TP.HCM", "Mời làm F1 phân phối, hoa hồng 2.5 - 3.5% + thưởng nóng"),
                (9, "Quỳnh Liên", "0936 09 10 11", "TPKD - Khải Minh Land", "Hồ Tràm (Maia, Ixora, Sanctuary)", "Resort cao cấp, Biệt thự biển 15 - 50 tỷ", "⭐⭐⭐⭐⭐ Cực cao", "Sales tinh nhuệ chuyên đánh dòng Second Home", "Ký kết liên kết sàn, tổ chức tour trải nghiệm hồ 100ha"),
                (10, "Lâm Khánh Tài", "0966 205 205", "Beach Villa Vietnam", "Cung đường biển Hồ Tràm - Bình Châu", "Villa nghỉ dưỡng, review hạ tầng", "⭐⭐⭐⭐⭐ Cực cao", "Kênh YouTube BĐS triệu view, tệp NĐT tài chính mạnh", "Tài trợ video review trải nghiệm hồ Lồ Ồ 100ha + booking độc quyền"),
                (11, "Đạt Nguyễn", "0918 788 966", "Vạn Đạt Land (Chuyên Ixora)", "Hồ Tràm Strip, Xuyên Mộc", "Biệt thự biển hạng sang, condotel", "⭐⭐⭐⭐ Cao", "Khách thích nhận dòng tiền cho thuê thụ động", "Chào sản phẩm Điền Sản (cam kết vận hành cho thuê turnkey)"),
                (12, "Phương Thiện", "0931 555 355", "Phương Thiện Land (Chuyên Novaworld)", "Bình Châu, Xuyên Mộc", "Shophouse, Biệt thự nghỉ dưỡng Novaworld", "⭐⭐⭐⭐ Cao", "Khách Novaworld tìm sp pháp lý sổ đỏ sở hữu lâu dài", "Nhấn mạnh: '100% Đất thổ cư lâu dài có sổ đỏ riêng từng nền'"),
                (13, "Sea Property (Team Hồ Tràm)", "0908 982 299", "Công ty CP ĐT BĐS HPR", "Trục Hồ Tràm - Bình Châu", "Tổng đại lý phân phối BĐS nghỉ dưỡng biển", "⭐⭐⭐⭐ Cao", "Sàn chuyên nghiệp, có phòng marketing & data VIP", "Ký hợp đồng đối tác chiến lược phân phối Biệt Phủ Điền Trang"),
                (14, "AQLand - Phòng Dự Án", "0906 462 223", "Sàn Giao Dịch AQLand", "Hồ Tràm, Long Hải", "Biệt thự biển, phân khúc wellness & retreat", "⭐⭐⭐⭐ Cao", "Khách thích chăm sóc sức khỏe, khoáng nóng, thiên nhiên", "Pitching concept 5 Trụ cột Lối sống Việt & Wellness ven hồ"),
                (15, "La Kim Mỹ Duyên", "0918 626 687", "IQI Vietnam (Chuyên Angsana)", "Hồ Tràm Strip, Xuyên Mộc", "BĐS nghỉ dưỡng hạng sang chuẩn quốc tế", "⭐⭐⭐⭐ Cao", "Khách hàng đầu tư BĐS thương hiệu 5 sao", "Chào giỏ hàng Biệt Phủ Điền Trang cho khách thượng lưu"),
                (16, "Đặng Duy", "0969 113 222", "Mister BĐS / IQI Vietnam", "Hồ Tràm, Phú Quốc, Phan Thiết", "Reviewer BĐS nghỉ dưỡng & Đầu tư", "⭐⭐⭐⭐ Cao", "Cộng đồng nhà đầu tư cá nhân có dòng vốn sẵn", "Mời review dự án và mở giỏ hàng độc quyền"),
            ]
        },
        {
            "name": "🌿 NHÓM 3: MÔI GIỚI BĐS NHÀ VƯỜN SINH THÁI & VEN SÔNG (TP.THỦ ĐỨC, LONG THÀNH, NHƠN TRẠCH)",
            "partners": [
                (17, "Mr. Đức Hùng (Nhà Vườn Long Phước)", "0903 123 456", "Long Phước Estate (Quận 9 cũ)", "Long Phước, Tam Đa, TP. Thủ Đức", "Biệt thự vườn ven sông 1.000m² - 5.000m²", "⭐⭐⭐⭐⭐ Khớp khách mua Second Home", "Khách đại gia TP.HCM thích làm nhà vườn sinh thái", "So sánh giá: Long Phước 30-50tr/m², SFR chỉ 1/4 mà có hồ 100ha"),
                (18, "Saigon Garden Team (Hưng Thịnh)", "0909 888 999", "Đại lý phân phối Saigon Garden", "Long Phước, TP. Thủ Đức", "Biệt thự sinh thái vườn ven sông cao cấp", "⭐⭐⭐⭐⭐ Tệp khách tương đồng 100%", "Tệp khách giàu thích thiên nhiên nhưng ngán giá Quận 9", "Gợi ý SFR: Chỉ 60 phút cao tốc là tới điền trang 100ha"),
                (19, "Mr. Lâm Long Thành", "0901 803 151", "BĐS Đất Vườn Sân Bay Long Thành", "An Phước, Long Phước, Bàu Cạn (Đồng Nai)", "Đất sào, đất trang trại đón đầu sân bay", "⭐⭐⭐⭐ Cao", "NĐT đón sóng hạ tầng Sân bay Long Thành", "SFR nằm ngay tam giác vàng Sân bay Long Thành - Hồ Tràm"),
                (20, "Ms. Thuỳ (Đất Vườn Long Thành)", "0328 193 938", "Chuyên Trang Trại Đồng Nai", "Long Thành, Cẩm Mỹ", "Đất nhà vườn, biệt thự vườn nghỉ dưỡng", "⭐⭐⭐⭐ Cao", "Gia đình TP.HCM tìm đất làm second home cuối tuần", "Tư vấn Điền An giá mềm chỉ từ 3 - 5 tỷ có sẵn hạ tầng tiện ích"),
                (21, "Mr. Huy (Nhơn Trạch Ven Sông)", "0976 776 960", "BĐS Sinh Thái Nhơn Trạch", "Đại Phước, Vĩnh Thanh, Phước An", "Đất ven sông, nhà vườn sinh thái", "⭐⭐⭐⭐ Cao", "Khách tìm kiếm không gian xanh thoát khỏi khói bụi", "Mời tham quan hồ Lồ Ồ 100ha - quy mô mặt nước gấp 10 lần sông rạch"),
                (22, "Tất Thành (Chuyên Khu Đông)", "0932 038 345", "Chuyên BĐS Đô Thị Sinh Thái", "TP. Thủ Đức, Biên Hòa, Long Thành", "Aqua City, Eco Village Saigon River", "⭐⭐⭐⭐ Cao", "Khách chuộng không gian sinh thái ven nước", "Chào dòng Điền Sản có pháp lý sổ đỏ sở hữu lâu dài"),
                (23, "Hunter Land (Eco Village)", "0911 378 737", "Sàn Hunter Land", "Khu Đông TP.HCM, Nhơn Trạch", "Bất động sản sinh thái trị liệu (Wellness)", "⭐⭐⭐⭐ Cao", "Khách quan tâm bất động sản chăm sóc sức khỏe", "Định vị SFR: Quần thể điền trang sinh thái hồ 100ha thuần tự nhiên"),
            ]
        },
        {
            "name": "🏢 NHÓM 4: CÁC SÀN MASTER BROKER & ĐẠI LÝ F1 BĐS NGHỈ DƯỠNG LỚN TẠI TP.HCM",
            "partners": [
                (24, "ERA Vietnam (Hotline Đại Lý)", "1800 6701", "Hệ thống ERA Real Estate VN", "Toàn quốc & TP.HCM (Trụ sở Q7)", "Sàn phân phối BĐS nghỉ dưỡng lớn nhất VN", "⭐⭐⭐⭐⭐ Quy mô cực lớn", "Mạng lưới hơn 4.000 môi giới chuyên nghiệp", "Ký kết phân phối F1 / Tổng đại lý bán hàng cho toàn dự án"),
                (25, "IQI Vietnam (Phòng Phát Triển DA)", "0764 155 155", "IQI Global Vietnam (City Gate Q2)", "TP. Thủ Đức, TP.HCM & Quốc tế", "BĐS cao cấp & Khách hàng nước ngoài/Việt kiều", "⭐⭐⭐⭐⭐ Khách quốc tế & Việt kiều", "Khách Việt kiều muốn mua điền trang bản sắc văn hóa Việt", "Pitching concept 5 Trụ cột Lối sống Việt Đương Đại"),
                (26, "Southern Homes Vietnam", "1900 2089", "Southern Homes (Phan Khiêm Ích, Q7)", "Quận 7, TP.HCM, Vũng Tàu, Hồ Tràm", "Chuyên phân phối F1 các dự án biển Hồ Tràm", "⭐⭐⭐⭐⭐ Rất mạnh Hồ Tràm", "Tệp khách Phú Mỹ Hưng & TP.HCM sở hữu BĐS thứ 2", "Tổ chức Roadshow giới thiệu dự án tại Quận 7"),
                (27, "Smartland (Team Nghỉ Dưỡng)", "0916 257 825", "Công ty TNHH BĐS Smartland", "TP.HCM (Nguyễn Hoàng, An Phú)", "Đại lý chiến lược các CĐT lớn", "⭐⭐⭐⭐ Cao", "Hơn 500 sales chuyên bán BĐS nghỉ dưỡng triệu USD", "Đàm phán cơ chế độc quyền giỏ hàng Biệt Phủ Điền Trang"),
                (28, "Đông Tây Land (Khối Nghỉ Dưỡng)", "0977 487 777", "Đông Tây Group", "TP. Thủ Đức, TP.HCM", "Top 1 sàn phân phối BĐS nghỉ dưỡng phía Nam", "⭐⭐⭐⭐⭐ Cực mạnh", "Data khách hàng ngàn tỷ mua BĐS khắp cả nước", "Hợp tác chiến lược, tài trợ chi phí tổ chức sự kiện mở bán"),
                (29, "Rever Vietnam", "028 7304 8899", "Công ty Công nghệ BĐS Rever", "TP.HCM, Đồng Nai, BR-VT", "Môi giới công nghệ, xác thực minh bạch", "⭐⭐⭐⭐ Cao", "Tệp khách công nghệ, trẻ tuổi, chuộng pháp lý chuẩn", "Đẩy tin xác thực sổ đỏ 100% thổ cư lên hệ thống Rever"),
                (30, "CBRE / Savills Residential", "0903 002 287", "Bộ phận Kinh doanh Nhà ở Cao cấp", "Quận 1, TP.HCM", "Biệt thự cao cấp, BĐS di sản truyền đời", "⭐⭐⭐⭐ Khách siêu giàu (UHNWI)", "Tệp khách gia tộc, chủ tập đoàn lớn tại Việt Nam", "Giới thiệu Biệt Phủ Điền Trang như một tài sản di sản truyền đời"),
            ]
        }
    ]

    current_row = 5
    for grp in groups:
        ws.row_dimensions[current_row].height = 28
        group_header(ws, current_row, 2, 10, grp["name"])
        current_row += 1

        for p in grp["partners"]:
            ws.row_dimensions[current_row].height = 36
            idx = p[0]
            row_bg = WHITE if idx % 2 == 0 else GOLD_BG

            data_cell(ws, current_row, 1, "", align="center", bg=row_bg)
            data_cell(ws, current_row, 2, idx, align="center", bold=True, bg=row_bg)
            data_cell(ws, current_row, 3, p[1], bold=True, bg=row_bg)
            data_cell(ws, current_row, 4, p[2], align="center", bold=True, bg=GREEN_STATUS, fg="064E3B")
            data_cell(ws, current_row, 5, p[3], bg=row_bg)
            data_cell(ws, current_row, 6, p[4], bg=row_bg)
            data_cell(ws, current_row, 7, p[5], wrap=True, bg=row_bg)
            data_cell(ws, current_row, 8, p[6], align="center", bold=True, bg=GOLD_LIGHT, fg=GREEN_DARK)
            data_cell(ws, current_row, 9, p[7], wrap=True, bg=row_bg)
            data_cell(ws, current_row, 10, p[8], wrap=True, bg=row_bg)
            current_row += 1

    # Bottom note
    ws.row_dimensions[current_row].height = 65
    ws.merge_cells(start_row=current_row, start_column=2, end_row=current_row, end_column=10)
    note_cell = ws.cell(row=current_row, column=2,
        value="📌 CHIẾN LƯỢC TIẾP CẬN THEO TỪNG NHÓM: \n"
              "• Nhóm 1 (Địa phương): Đẩy mạnh phân khúc Điền An & Điền Sản, tập trung vào điểm mạnh 'Sổ đỏ thổ cư riêng từng nền, không lo quy hoạch treo'.\n"
              "• Nhóm 2 (Biệt thự biển): Đánh vào yếu tố so sánh 'Sở hữu lâu dài vs 50 năm' và 'Vùng trũng giá 1/3 đất biển' để chuyển hướng khách của họ.\n"
              "• Nhóm 3 (Nhà vườn sinh thái): Nhấn mạnh vi khí hậu mát mẻ của hồ nước ngọt 100ha và chỉ mất 60 phút từ TP.HCM qua cao tốc.\n"
              "• Nhóm 4 (Master Broker): Ký hợp đồng Co-broking chính thức, áp dụng cơ chế thưởng nóng và hỗ trợ xe đưa đón khách VIP.")
    note_cell.fill = make_fill(GREEN_DARK)
    note_cell.font = Font(name="Calibri", size=9.5, bold=True, color="FFFDF9")
    note_cell.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True, indent=1)
    note_cell.border = make_border()


def build_cover(wb):
    ws = wb.create_sheet("🏡 TRANG BÌA", 1)
    ws.sheet_view.showGridLines = False

    set_col_width(ws, 1, 5)
    for c in range(2, 9):
        set_col_width(ws, c, 18)

    ws.row_dimensions[2].height = 80
    ws.row_dimensions[3].height = 40

    ws.merge_cells("B2:H2")
    cell = ws["B2"]
    cell.value = "SAIGON FARM RESORT\nMẠNG LƯỚI 30 ĐỐI TÁC MÔI GIỚI & SALES CHIẾN LƯỢC"
    cell.fill  = make_fill(GREEN_DARK)
    cell.font  = Font(name="Calibri", size=20, bold=True, color="FFFDF9")
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)

    ws.merge_cells("B3:H3")
    cell = ws["B3"]
    cell.value = "MDS LAND & LIVING  •  Quần Thể Điền Trang Ven Hồ Lồ Ồ 100ha  •  Đất Đỏ, Cạnh Hồ Tràm, BR-VT"
    cell.fill  = make_fill(GOLD)
    cell.font  = Font(name="Calibri", size=12, bold=True, color=GREEN_DARK)
    cell.alignment = Alignment(horizontal="center", vertical="center")

    info = [
        ("📅 Thời gian triển khai:", "Tháng 09/2026 — Phủ sóng mạng lưới bán hàng quý 3 & 4/2026"),
        ("🏗️ Bộ 3 dòng sản phẩm:", "Biệt Phủ Điền Trang (25–100 tỷ) | Điền Sản (10–25 tỷ) | Điền An (3–8 tỷ)"),
        ("📍 Tọa độ vàng kết nối:", "Xã Đất Đỏ, cạnh Hồ Tràm — 60 phút từ TP.HCM qua Cao tốc Long Thành / Bến Lức"),
        ("🌿 Điểm nhấn độc bản:", "Mặt hồ nước ngọt tự nhiên 100ha • Quần thể tiện ích lên đến 30.000 m² (Việt Mã Viên, Pickleball, Kayak)"),
        ("💼 Bảo chứng pháp lý:", "100% Đất ở thổ cư lâu dài — Sổ đỏ riêng từng khuôn viên — Công chứng sang tên ngay"),
        ("🤝 Quy mô danh bạ:", "30 Sales & Sàn BĐS đối tác phân chia 4 nhóm logic: Địa phương, Biệt thự biển, Nhà vườn, Master Broker"),
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


def build_leads(wb):
    ws = wb.create_sheet("👤 KHÁCH HÀNG TIỀM NĂNG", 2)
    ws.freeze_panes = "A5"
    ws.sheet_view.showGridLines = False

    widths = [5, 6, 22, 14, 20, 14, 13, 16, 14, 14, 12, 22, 30, 18, 18, 22]
    for i, w in enumerate(widths, 1):
        set_col_width(ws, i, w)

    ws.row_dimensions[2].height = 35
    ws.row_dimensions[3].height = 22
    ws.row_dimensions[4].height = 40

    title_row(ws, 2, 2, 16, "👤 THEO DÕI KHÁCH HÀNG TIỀM NĂNG TỪ CÁC SÀN ĐỐI TÁC", size=13)
    sub_header(ws, 3, 2, 16, "Saigon Farm Resort | MDS Land & Living | Quần thể điền trang ven hồ Lồ Ồ 100ha")

    headers = [
        "#", "STT", "HỌ VÀ TÊN", "SỐ ĐIỆN THOẠI",
        "EMAIL", "ĐỊA CHỈ / TỈNH THÀNH", "NGHỀ NGHIỆP",
        "NGUỒN / MÔI GIỚI GIỚI THIỆU", "SẢN PHẨM QUAN TÂM",
        "NGÂN SÁCH (TỶ)", "TRẠNG THÁI", "NGÀY TIẾP XÚC",
        "GHI CHÚ NHU CẦU", "SALES NỘI BỘ PHỤ TRÁCH", "LỊCH HẸN THỰC ĐỊA",
        "HÀNH ĐỘNG TIẾP THEO"
    ]
    for col, h in enumerate(headers, 1):
        col_header(ws, 4, col, h)

    sample_leads = [
        (1,"Nguyễn Minh Tuấn","0912 345 678","tuan.nguyen@gmail.com","Quận 7, TP.HCM","Giám đốc DN","Mỹ Thương Realtor (Đông Tây)","Biệt Phủ Điền Trang","25–35","🟢 Quan tâm cao","01/09/2026","Muốn second home cuối tuần, thích phong cách nông trang ven hồ","Trần Thị Lan","28/09/2026","Mời tham quan thực địa & trải nghiệm chèo thuyền Kayak"),
        (2,"Phạm Hồng Anh","0908 876 543","honganh.pham@yahoo.com","Bình Thạnh, TP.HCM","Bác sĩ","Quỳnh Liên (Khải Minh)","Điền Sản","8–12","🟡 Đang tư vấn","02/09/2026","Quan tâm dòng tiền cho thuê, hỏi tỷ suất lợi nhuận","Lê Văn Hùng","29/09/2026","Gửi bài toán tài chính & phương án cho thuê turnkey"),
        (3,"Lê Thị Bích Ngọc","0918 654 321","bichn.le@gmail.com","Gò Vấp, TP.HCM","Doanh nhân","Lâm Khánh Tài (Beach Villa)","Biệt Phủ Điền Trang","40–60","🔵 Đã đặt cọc","04/09/2026","Đã ký thỏa thuận đặt cọc, chuẩn bị ký HĐ chuyển nhượng","Trần Thị Lan","10/09/2026","Hỗ trợ thủ tục công chứng sang tên sổ đỏ"),
        (4,"Võ Quốc Bảo","0931 789 012","baovq@doanhnhan.vn","Quận 1, TP.HCM","Luật sư","Nguyễn Quang Anh (Đất Đỏ)","Điền Sản","15–20","🟢 Quan tâm cao","05/09/2026","Được giới thiệu, đã kiểm tra quy hoạch và ưng ý pháp lý sổ đỏ","Lê Văn Hùng","30/09/2026","Tổ chức buổi tham quan thực địa VIP cho gia đình"),
        (5,"Ngô Thế Vinh","0922 345 678","vinh.ngo@ceo.vn","Quận 2, TP.HCM","CEO Startup","Đức Hùng (Nhà Vườn Long Phước)","Biệt Phủ Điền Trang","50–80","🟢 Quan tâm cao","09/09/2026","Tìm mua biệt thự ven hồ làm retreat công ty kiêm nghỉ dưỡng","Trần Thị Lan","02/10/2026","Chuẩn bị proposal chi tiết & thực đơn tiệc ngoài trời ven hồ"),
    ]

    for i, lead in enumerate(sample_leads, start=5):
        ws.row_dimensions[i].height = 30
        idx = lead[0]
        row_bg = WHITE if idx % 2 == 0 else GOLD_BG

        data_cell(ws, i, 1, "", align="center", bg=row_bg)
        data_cell(ws, i, 2, idx, align="center", bold=True, bg=row_bg)
        data_cell(ws, i, 3, lead[1], bold=True, bg=row_bg)
        data_cell(ws, i, 4, lead[2], align="center", bg=row_bg)
        data_cell(ws, i, 5, lead[3], bg=row_bg)
        data_cell(ws, i, 6, lead[4], bg=row_bg)
        data_cell(ws, i, 7, lead[5], bg=row_bg)
        data_cell(ws, i, 8, lead[6], bold=True, bg=BLUE_LIGHT)
        data_cell(ws, i, 9, lead[7], align="center", bold=True, bg=GOLD_LIGHT, fg=GREEN_DARK)
        data_cell(ws, i, 10, lead[8], align="center", bg=row_bg)
        data_cell(ws, i, 11, lead[9], align="center", bg=GREEN_STATUS if "cao" in lead[9] else BLUE_LIGHT if "cọc" in lead[9] else YELLOW_STATUS, bold=True)
        data_cell(ws, i, 12, lead[10], align="center", bg=row_bg)
        data_cell(ws, i, 13, lead[11], wrap=True, bg=row_bg)
        data_cell(ws, i, 14, lead[12], align="center", bg=row_bg)
        data_cell(ws, i, 15, lead[13], align="center", bg=YELLOW_STATUS if lead[13] else row_bg)
        data_cell(ws, i, 16, lead[14], wrap=True, bg=row_bg)


def build_scripts(wb):
    ws = wb.create_sheet("📞 SCRIPT GỌI MÔI GIỚI", 3)
    ws.sheet_view.showGridLines = False

    widths = [4, 28, 65, 65]
    for i, w in enumerate(widths, 1):
        set_col_width(ws, i, w)

    ws.row_dimensions[2].height = 40
    ws.row_dimensions[3].height = 22
    title_row(ws, 2, 1, 4, "📞 KỊCH BẢN LIÊN HỆ SALES & SÀN BĐS (THEO 4 NHÓM ĐỐI TÁC)", size=13)
    sub_header(ws, 3, 1, 4, "Bộ kịch bản chuyên biệt cho nhân viên gọi điện hoặc nhắn tin Zalo kết nối hợp tác phân phối")

    scripts = [
        {
            "title": "📱 KỊCH BẢN CHUNG: NHẮN TIN ZALO KẾT BẠN ĐẦU TIÊN",
            "situation": "Gửi tin nhắn chào mừng, đề xuất hợp tác nhanh gọn qua Zalo",
            "script": (
                "Chào anh/chị [Tên],\n\n"
                "Em thấy anh/chị đang giao dịch rất mạnh phân khúc BĐS nghỉ dưỡng / biệt thự / nhà vườn khu vực phía Nam.\n\n"
                "Bên em là Chủ đầu tư MDS Land & Living, đang triển khai quần thể điền trang sinh thái SAIGON FARM RESORT ôm trọn mặt hồ nước ngọt Lồ Ồ 100ha tại Đất Đỏ (liền kề Hồ Tràm, chỉ 60 phút từ TP.HCM).\n\n"
                "Dự án bên em có 3 điểm CỰC KỲ DỄ BÁN cho khách hàng của anh/chị:\n"
                "1. 100% Đất ở thổ cư lâu dài, sổ đỏ riêng từng nền, công chứng sang tên ngay (không lo pháp lý 50 năm hay quy hoạch treo).\n"
                "2. Vùng trũng giá: Giá chỉ bằng 1/3 đến 1/4 đất biển Hồ Tràm trong khi sở hữu mặt nước hồ tự nhiên 100ha và 30.000m² tiện ích (Việt Mã Viên, Pickleball, Kayak).\n"
                "3. Cơ chế hoa hồng & thưởng nóng cực kỳ hấp dẫn cho Sales / Đại lý liên kết (2.5% - 3.5%).\n\n"
                "Em gửi anh/chị xem trước link giới thiệu: saigonfarmresort.com/gioithieu và Bảng cơ chế hoa hồng chi tiết nhé ạ!"
            )
        },
        {
            "title": "🏖️ KỊCH BẢN CHO NHÓM 2: SALES BIỆT THỰ BIỂN HỒ TRÀM",
            "situation": "Gọi điện cho Sales chuyên bán Maia, Ixora, Novaworld, Sanctuary",
            "script": (
                "Alo chào anh/chị [Tên], em là [Tên Bạn] từ dự án Saigon Farm Resort - MDS Land & Living.\n\n"
                "Em biết anh/chị đang có tệp khách VIP rất mạnh quan tâm biệt thự nghỉ dưỡng Hồ Tràm. Chắc anh/chị cũng gặp nhiều khách hàng hỏi câu: 'Có sản phẩm nào nghỉ dưỡng ven hồ, không khí mát mẻ mà PHÁP LÝ SỔ ĐỎ LÂU DÀI không?'\n\n"
                "Đúng điểm chạm đó, bên em có quần thể Điền Trang ven hồ Lồ Ồ 100ha ngay Đất Đỏ, cách biển Hồ Tràm chỉ 15 phút lái xe.\n\n"
                "Khách của anh/chị mua ở đây có 3 lợi thế vượt trội so với condotel/resort biển:\n"
                "• Sở hữu vĩnh viễn (sổ đỏ thổ cư riêng) thay vì hợp đồng thuê 50 năm.\n"
                "• Giá chỉ bằng 1/3 (phân khúc từ 3 - 6 tỷ cho Điền An, và 15 - 30 tỷ cho Biệt Phủ Điền Trang).\n"
                "• Có sẵn hồ tự nhiên 100ha và 30.000m² tiện ích độc bản.\n\n"
                "Cuối tuần này em mời anh/chị ghé tham quan thực địa dự án và uống cà phê ven hồ bên em được không ạ? Em sẽ gửi trước giỏ hàng ưu tiên để anh/chị ráp khách ngay."
            )
        },
        {
            "title": "🌿 KỊCH BẢN CHO NHÓM 3: SALES NHÀ VƯỜN LONG PHƯỚC / ĐỒNG NAI",
            "situation": "Gọi cho Sales chuyên bán đất vườn, nhà vườn sinh thái ven sông",
            "script": (
                "Chào anh/chị [Tên], em thấy anh/chị bán nhà vườn Long Phước Quận 9 và đất vườn Đồng Nai rất tốt.\n\n"
                "Hiện nay đất vườn Long Phước giá đã lên tới 30 - 50 triệu/m², nhiều khách muốn làm nhà vườn sinh thái nhưng ngân sách 5 - 10 tỷ chỉ mua được mảnh nhỏ hoặc đất nông nghiệp khó chuyển thổ cư.\n\n"
                "Bên em có dự án Saigon Farm Resort tại Đất Đỏ, đi cao tốc từ TP.HCM xuống đúng 60 phút.\n\n"
                "Với tài chính chỉ từ 3 - 6 tỷ, khách của anh/chị đã sở hữu ngay khuôn viên nhà vườn ĐIỀN AN có 100% thổ cư, hạ tầng đường sá hoàn chỉnh, lại nằm ngay mặt hồ nước ngọt 100ha.\n\n"
                "Anh/chị có tệp khách nào đang tìm nhà vườn cuối tuần mà chưa chốt được vì giá TP.HCM quá cao không? Em gửi anh/chị thông tin dự án để anh/chị giới thiệu thêm phương án này cho khách nhé!"
            )
        },
        {
            "title": "🏢 KỊCH BẢN CHO NHÓM 4: SÀN MASTER BROKER & ĐẠI LÝ F1",
            "situation": "Đàm phán hợp tác phân phối cấp Sàn / Đại lý lớn (ERA, IQI, Southern Homes...)",
            "script": (
                "Chính sách dành riêng cho Sàn đối tác chiến lược:\n"
                "1. Hoa hồng đại lý: 3.0% - 3.5% trên tổng giá trị giao dịch.\n"
                "2. Cam kết giải ngân hoa hồng nhanh: Chi trả 100% phí môi giới trong vòng 7 - 10 ngày làm việc sau khi khách ký HĐ.\n"
                "3. Hỗ trợ sự kiện bán hàng: Hỗ trợ xe đưa đón khách VIP từ TP.HCM xuống dự án, đài thọ tiệc trà/ẩm thực Farm-to-Table tại resort.\n"
                "4. Thưởng nóng đột phá: Tặng 1 lượng vàng SJC hoặc xe SH cho giao dịch đầu tiên của Sàn trong tháng.\n"
                "5. Cung cấp tài liệu bán hàng chuyên nghiệp: Bộ E-brochure, video flycam 4K, bản vẽ mặt bằng và bảng tính dòng tiền IRR cho thuê."
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

    print("🚀 Bắt đầu tạo file Excel mở rộng 30 đối tác môi giới...")
    build_mega_brokers(wb)
    build_cover(wb)
    build_leads(wb)
    build_scripts(wb)

    wb.save(EXCEL_FILE)
    wb.save(DESKTOP_FILE)
    print(f"✅ Hoàn tất thành công!")
    print(f"   📁 Lưu tại dự án: {EXCEL_FILE}")
    print(f"   📁 Lưu tại Desktop: {DESKTOP_FILE}")

if __name__ == "__main__":
    main()
