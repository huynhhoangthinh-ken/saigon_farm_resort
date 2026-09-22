#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Saigon Farm Resort - CRM Excel Generator
Tháng 09/2026 — Khách hàng tiềm năng & Sales tracking
"""

import openpyxl
from openpyxl.styles import (
    PatternFill, Font, Alignment, Border, Side, GradientFill
)
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.chart import BarChart, Reference
from openpyxl.chart.label import DataLabelList
import datetime

# ─────────────── PALETTE MÀU THƯƠNG HIỆU ───────────────
GREEN_DARK   = "183024"   # Xanh rừng đậm (accent)
GREEN_LIGHT  = "2C5440"   # Xanh rừng nhạt
GOLD         = "C29B53"   # Vàng thương hiệu
GOLD_LIGHT   = "ECDCB9"   # Kem vàng nhạt
GOLD_BG      = "FAF3E6"   # Nền vàng cực nhạt
BG_PAGE      = "F4EDE2"   # Nền trang chủ
WHITE        = "FFFDF9"   # Trắng kem
BORDER_COLOR = "E2DACB"   # Đường viền nhạt
RED_LIGHT    = "FEE2E2"   # Đỏ nhạt (cảnh báo)
BLUE_LIGHT   = "DBEAFE"   # Xanh dương nhạt (info)
GREEN_STATUS = "D1FAE5"   # Xanh nhạt (trạng thái tốt)
YELLOW_STATUS= "FEF3C7"   # Vàng nhạt (chờ xử lý)

def make_fill(hex_color):
    return PatternFill("solid", fgColor=hex_color)

def make_border(style="thin"):
    s = Side(style=style, color=BORDER_COLOR)
    return Border(left=s, right=s, top=s, bottom=s)

def header_font(size=11, bold=True, color="FFFFFF"):
    return Font(name="Calibri", size=size, bold=bold, color=color)

def body_font(size=10, bold=False, color="1F2937"):
    return Font(name="Calibri", size=size, bold=bold, color=color)

def set_col_width(ws, col, width):
    ws.column_dimensions[get_column_letter(col)].width = width

def title_row(ws, row, col_start, col_end, text, bg=GREEN_DARK, fg="FFFFFF", size=13):
    ws.merge_cells(
        start_row=row, start_column=col_start,
        end_row=row, end_column=col_end
    )
    cell = ws.cell(row=row, column=col_start, value=text)
    cell.fill  = make_fill(bg)
    cell.font  = Font(name="Calibri", size=size, bold=True, color=fg)
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    cell.border = make_border()

def sub_header(ws, row, col_start, col_end, text, bg=GOLD, fg=GREEN_DARK, size=10):
    ws.merge_cells(
        start_row=row, start_column=col_start,
        end_row=row, end_column=col_end
    )
    cell = ws.cell(row=row, column=col_start, value=text)
    cell.fill  = make_fill(bg)
    cell.font  = Font(name="Calibri", size=size, bold=True, color=fg)
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    cell.border = make_border()

def col_header(ws, row, col, text, bg=GREEN_DARK, fg="FFFFFF"):
    cell = ws.cell(row=row, column=col, value=text)
    cell.fill  = make_fill(bg)
    cell.font  = Font(name="Calibri", size=9, bold=True, color=fg)
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    cell.border = make_border()

def data_cell(ws, row, col, value, align="left", bold=False, bg=None, fg="1F2937", wrap=False):
    cell = ws.cell(row=row, column=col, value=value)
    cell.font  = Font(name="Calibri", size=9, bold=bold, color=fg)
    cell.alignment = Alignment(horizontal=align, vertical="center", wrap_text=wrap)
    cell.border = make_border()
    if bg:
        cell.fill = make_fill(bg)
    return cell

# ═══════════════════════════════════════════════════════
# SHEET 1: TRANG BÌA
# ═══════════════════════════════════════════════════════
def build_cover(wb):
    ws = wb.create_sheet("🏡 TRANG BÌA", 0)
    ws.sheet_view.showGridLines = False
    ws.row_dimensions[1].height = 20
    ws.row_dimensions[2].height = 80
    ws.row_dimensions[3].height = 40
    ws.row_dimensions[4].height = 30
    ws.row_dimensions[5].height = 30
    ws.row_dimensions[6].height = 30

    set_col_width(ws, 1, 5)
    for c in range(2, 10):
        set_col_width(ws, c, 18)
    set_col_width(ws, 9, 5)

    # Tiêu đề chính
    ws.merge_cells("B2:H2")
    cell = ws["B2"]
    cell.value = "SAIGON FARM RESORT\nHỆ THỐNG CRM & THEO DÕI SALES THÁNG 09/2026"
    cell.fill  = make_fill(GREEN_DARK)
    cell.font  = Font(name="Calibri", size=22, bold=True, color="FFFDF9")
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)

    ws.merge_cells("B3:H3")
    cell = ws["B3"]
    cell.value = "MDS LAND & LIVING  •  Điền Trang Ven Hồ Lồ Ồ 100ha  •  Đất Đỏ, Hồ Tràm, BR-VT"
    cell.fill  = make_fill(GOLD)
    cell.font  = Font(name="Calibri", size=12, bold=True, color=GREEN_DARK)
    cell.alignment = Alignment(horizontal="center", vertical="center")

    # Info box
    info = [
        ("📅 Chu kỳ bán hàng:", "Tháng 09/2026 (01/09/2026 – 30/09/2026)"),
        ("🏗️ Sản phẩm:", "Biệt Phủ Điền Trang | Điền Sản | Điền An"),
        ("📍 Vị trí:", "Xã Đất Đỏ, cạnh Hồ Tràm — 60 phút từ TP.HCM"),
        ("🌿 Quy mô:", "100ha mặt hồ tự nhiên • Tiện ích lên đến 30.000 m²"),
        ("💼 Pháp lý:", "100% Đất ở thổ cư lâu dài — Sổ đỏ riêng từng lô"),
    ]
    for i, (label, value) in enumerate(info, start=5):
        ws.row_dimensions[i].height = 28
        ws.merge_cells(start_row=i, start_column=2, end_row=i, end_column=4)
        ws.merge_cells(start_row=i, start_column=5, end_row=i, end_column=8)
        c1 = ws.cell(row=i, column=2, value=label)
        c1.fill = make_fill(GOLD_BG)
        c1.font = Font(name="Calibri", size=10, bold=True, color=GREEN_DARK)
        c1.alignment = Alignment(horizontal="left", vertical="center", indent=1)
        c1.border = make_border()
        c2 = ws.cell(row=i, column=5, value=value)
        c2.fill = make_fill(WHITE)
        c2.font = Font(name="Calibri", size=10, color="1F2937")
        c2.alignment = Alignment(horizontal="left", vertical="center", indent=1)
        c2.border = make_border()

    # Hướng dẫn nhanh
    ws.row_dimensions[11].height = 25
    ws.row_dimensions[12].height = 22
    ws.merge_cells("B11:H11")
    cell = ws["B11"]
    cell.value = "📋 HƯỚNG DẪN SỬ DỤNG"
    cell.fill  = make_fill(GREEN_LIGHT)
    cell.font  = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
    cell.alignment = Alignment(horizontal="center", vertical="center")

    nav = [
        ("Sheet 2", "👤 KHÁCH HÀNG TIỀM NĂNG", "Danh sách 30+ leads, lịch sử tương tác, trạng thái chăm sóc"),
        ("Sheet 3", "💼 THEO DÕI SALES", "Pipeline bán hàng, forecast doanh thu, KPI sales tháng"),
        ("Sheet 4", "📣 KÊNH TÌM KIẾM", "Hướng dẫn chi tiết 7 kênh cào data & tìm kiếm khách hàng"),
        ("Sheet 5", "📊 BÁO CÁO THÁNG", "Dashboard tổng hợp, biểu đồ chuyển đổi, hiệu quả kênh"),
        ("Sheet 6", "🎯 SCRIPT TƯ VẤN", "Kịch bản tư vấn cho từng dòng sản phẩm & phân khúc KH"),
    ]
    for i, (sheet_id, name, desc) in enumerate(nav, start=12):
        ws.row_dimensions[i + 12].height = 24
        r = i
        ws.cell(row=r, column=2, value=sheet_id).fill = make_fill(GOLD_LIGHT)
        ws.cell(row=r, column=2).font = Font(name="Calibri", size=9, bold=True, color=GREEN_DARK)
        ws.cell(row=r, column=2).border = make_border()
        ws.cell(row=r, column=2).alignment = Alignment(horizontal="center", vertical="center")
        ws.merge_cells(start_row=r, start_column=3, end_row=r, end_column=5)
        ws.cell(row=r, column=3, value=name).fill = make_fill(GOLD_BG)
        ws.cell(row=r, column=3).font = Font(name="Calibri", size=9, bold=True, color=GREEN_DARK)
        ws.cell(row=r, column=3).border = make_border()
        ws.cell(row=r, column=3).alignment = Alignment(horizontal="left", vertical="center", indent=1)
        ws.merge_cells(start_row=r, start_column=6, end_row=r, end_column=8)
        ws.cell(row=r, column=6, value=desc).fill = make_fill(WHITE)
        ws.cell(row=r, column=6).font = Font(name="Calibri", size=9, color="374151")
        ws.cell(row=r, column=6).border = make_border()
        ws.cell(row=r, column=6).alignment = Alignment(horizontal="left", vertical="center", indent=1, wrap_text=True)


# ═══════════════════════════════════════════════════════
# SHEET 2: KHÁCH HÀNG TIỀM NĂNG
# ═══════════════════════════════════════════════════════
def build_leads(wb):
    ws = wb.create_sheet("👤 KHÁCH HÀNG TIỀM NĂNG", 1)
    ws.freeze_panes = "A5"
    ws.sheet_view.showGridLines = False

    # Column widths
    widths = [5, 6, 22, 14, 20, 14, 13, 16, 14, 14, 12, 22, 30, 18, 18, 22]
    for i, w in enumerate(widths, 1):
        set_col_width(ws, i, w)

    ws.row_dimensions[1].height = 10
    ws.row_dimensions[2].height = 35
    ws.row_dimensions[3].height = 22
    ws.row_dimensions[4].height = 40

    # Title
    title_row(ws, 2, 2, 16, "👤 DANH SÁCH KHÁCH HÀNG TIỀM NĂNG — THÁNG 09/2026", size=14)
    sub_header(ws, 3, 2, 16, "Saigon Farm Resort | MDS Land & Living | Điền Trang Ven Hồ Lồ Ồ 100ha — Đất Đỏ, Hồ Tràm")

    # Column headers
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
    ws.row_dimensions[4].height = 45

    # Status colors mapping
    status_colors = {
        "🔴 Mới tiếp cận": RED_LIGHT,
        "🟡 Đang tư vấn": YELLOW_STATUS,
        "🟢 Quan tâm cao": GREEN_STATUS,
        "🔵 Đã đặt cọc": BLUE_LIGHT,
        "⚫ Không tiềm năng": "F3F4F6",
        "🟣 Chờ quyết định": "EDE9FE",
    }

    # 30 sample leads
    leads_data = [
        # (STT, Họ tên, SĐT, Email, Địa chỉ, Nghề nghiệp, Kênh, SP quan tâm, Ngân sách, Trạng thái, Ngày, Ghi chú, NV phụ trách, Lịch hẹn, Hành động)
        (1,"Nguyễn Minh Tuấn","0912 345 678","tuan.nguyen@gmail.com","Quận 7, TP.HCM","Giám đốc DN","Facebook Ads","Biệt Phủ Điền Trang","25–35","🟢 Quan tâm cao","01/09/2026","Muốn ngôi nhà thứ 2 cuối tuần, thích phong cách nông trang","Trần Thị Lan","15/09/2026","Mời tham quan thực địa"),
        (2,"Phạm Hồng Anh","0908 876 543","honganh.pham@yahoo.com","Bình Thạnh, TP.HCM","Bác sĩ","Zalo Group BĐS","Điền Sản","8–12","🟡 Đang tư vấn","02/09/2026","Quan tâm dòng tiền cho thuê, hỏi tỷ suất lợi nhuận","Lê Văn Hùng","18/09/2026","Gửi bài toán tài chính chi tiết"),
        (3,"Trần Văn Khoa","0903 211 456","khoa.tran@hotmail.com","Thủ Đức, TP.HCM","Kỹ sư CNTT","YouTube","Điền An","3–5","🔴 Mới tiếp cận","03/09/2026","Xem video dự án, nhắn hỏi vị trí cụ thể","Nguyễn Thị Mai","20/09/2026","Gọi điện giới thiệu, gửi brochure"),
        (4,"Lê Thị Bích Ngọc","0918 654 321","bichn.le@gmail.com","Gò Vấp, TP.HCM","Doanh nhân","Hội chợ BĐS","Biệt Phủ Điền Trang","40–60","🔵 Đã đặt cọc","04/09/2026","Đã ký hợp đồng đặt cọc, chờ ký chính thức","Trần Thị Lan","10/09/2026","Chuẩn bị hợp đồng mua bán"),
        (5,"Võ Quốc Bảo","0931 789 012","baovq@doanhnhan.vn","Quận 1, TP.HCM","Luật sư","Referral","Điền Sản","15–20","🟢 Quan tâm cao","05/09/2026","Được giới thiệu từ KH cũ, quan tâm pháp lý rõ ràng","Lê Văn Hùng","22/09/2026","Tổ chức buổi tham quan thực địa VIP"),
        (6,"Đặng Thị Thanh Thủy","0907 432 109","thuydang@gmail.com","Long An","Giáo viên","TikTok","Điền An","3–5","🟡 Đang tư vấn","06/09/2026","Thấy video trên TikTok, muốn mua đầu tư dài hạn","Nguyễn Thị Mai","25/09/2026","Tư vấn phương thức thanh toán linh hoạt"),
        (7,"Hoàng Đức Thịnh","0916 543 210","thinh.hoang@outlook.com","Đồng Nai","Kiến trúc sư","Batdongsan.com.vn","Biệt Phủ Điền Trang","20–30","🟡 Đang tư vấn","07/09/2026","Quan tâm thiết kế, muốn tùy chỉnh nội thất","Trần Thị Lan","26/09/2026","Gửi thiết kế mẫu và tư vấn tùy biến"),
        (8,"Phan Thị Hương","0905 678 901","huong.phan@vnpt.vn","Quận 3, TP.HCM","Kế toán","Instagram","Điền An","4–6","🔴 Mới tiếp cận","08/09/2026","Comment hỏi thêm thông tin trên Instagram","Lê Văn Hùng","","DM Instagram, gửi catalog"),
        (9,"Ngô Thế Vinh","0922 345 678","vinh.ngo@ceo.vn","Quận 2, TP.HCM","CEO Startup","LinkedIn","Biệt Phủ Điền Trang","50–80","🟢 Quan tâm cao","09/09/2026","Tìm mua biệt thự làm văn phòng kiêm nghỉ dưỡng cuối tuần","Trần Thị Lan","28/09/2026","Tổ chức buổi pitch riêng, mời tham quan"),
        (10,"Trịnh Thị Mỹ Linh","0911 234 567","mylinh.trinh@gmail.com","Bình Dương","Nhân viên ngân hàng","Zalo OA","Điền Sản","10–15","🟡 Đang tư vấn","10/09/2026","Hỏi về vay ngân hàng, điều kiện mua","Nguyễn Thị Mai","","Kết nối ngân hàng đối tác"),
        (11,"Đinh Văn Toàn","0935 876 234","toan.dinh@vn.ibm.com","Tân Phú, TP.HCM","Quản lý IT","Website","Điền Sản","12–18","🟣 Chờ quyết định","11/09/2026","Đang bàn bạc với gia đình, chờ phản hồi tuần sau","Lê Văn Hùng","27/09/2026","Follow-up Zalo, hỏi thăm quyết định"),
        (12,"Lương Thị Phi Phi","0913 567 890","phiphi.luong@saigon.vn","Phú Nhuận, TP.HCM","Bác sĩ","Facebook Group","Biệt Phủ Điền Trang","30–45","🟢 Quan tâm cao","12/09/2026","Tìm mua để nghỉ hưu, thích thiên nhiên xanh mát","Trần Thị Lan","29/09/2026","Mời tham quan cuối tuần kết hợp picnic"),
        (13,"Bùi Thanh Sơn","0906 789 012","sonbt@techvina.com","Long Thành, Đồng Nai","Kỹ sư xây dựng","Coldcall","Điền An","4–7","🔴 Mới tiếp cận","13/09/2026","Sống gần dự án, quan tâm mua ở thực","Nguyễn Thị Mai","","Mời thăm dự án trực tiếp"),
        (14,"Hồ Thị Thanh Hà","0919 012 345","haha.ho@gmail.com","Quận 9, TP.HCM","Nội trợ","Referral","Điền An","5–8","🟡 Đang tư vấn","14/09/2026","Chồng làm KCN Đất Đỏ, muốn mua nhà gần nơi làm việc","Lê Văn Hùng","21/09/2026","Giới thiệu chương trình ưu đãi nhân viên KCN"),
        (15,"Trương Quốc Khánh","0928 456 789","khanh.truong@invest.vn","Quận 7, TP.HCM","Chuyên viên đầu tư","Hội thảo đầu tư","Điền Sản","18–25","🟢 Quan tâm cao","15/09/2026","Đang phân tích ROI, muốn so sánh với Phú Quốc","Trần Thị Lan","24/09/2026","Gửi bảng so sánh suất đầu tư chi tiết"),
        (16,"Vũ Thị Thanh Thúy","0914 890 123","thuy.vu@lawyer.vn","Quận 1, TP.HCM","Luật sư","Google Ads","Biệt Phủ Điền Trang","35–50","🟣 Chờ quyết định","16/09/2026","Đã xem pháp lý, đang chờ bàn với partner","Lê Văn Hùng","30/09/2026","Hỗ trợ thẩm định pháp lý lần cuối"),
        (17,"Đỗ Minh Nghĩa","0901 234 567","nghia.do@mbn.vn","Tân Bình, TP.HCM","Chủ chuỗi F&B","TikTok","Điền Sản","20–30","🟡 Đang tư vấn","17/09/2026","Muốn đầu tư bất động sản thu nhập thụ động","Nguyễn Thị Mai","23/09/2026","Trình bày mô hình cho thuê Điền Sản"),
        (18,"Cao Thị Bảo Ngọc","0936 345 678","baongoc@doctor.vn","Củ Chi, TP.HCM","Nha sĩ","Zalo Group","Điền An","3–5","🔴 Mới tiếp cận","18/09/2026","Hỏi về diện tích và giá cụ thể","Trần Thị Lan","","Gửi bảng giá và tư vấn qua Zalo"),
        (19,"Lý Trường Giang","0924 567 890","giang.ly@topbank.vn","Quận 4, TP.HCM","Giám đốc ngân hàng","Event Open House","Biệt Phủ Điền Trang","60–100","🟢 Quan tâm cao","19/09/2026","Dự Open House, rất ấn tượng với hồ 100ha","Trần Thị Lan","27/09/2026","Đưa đi tham quan lần 2, bàn về chính sách"),
        (20,"Nguyễn Thị Thu Hà","0915 678 901","thuha.nguyen@fpt.vn","Thủ Đức, TP.HCM","Kỹ sư phần mềm","Instagram","Điền An","4–6","🟡 Đang tư vấn","20/09/2026","Tìm mua nhà cuối tuần cho bố mẹ","Lê Văn Hùng","","Giới thiệu Điền An loại nhỏ phù hợp"),
        (21,"Phùng Văn Khải","0938 789 012","khai.phung@sme.vn","Biên Hòa, Đồng Nai","Doanh nhân SME","Batdongsan.com.vn","Điền Sản","12–20","🟡 Đang tư vấn","21/09/2026","Đã xem nhiều dự án, thích nhất SFR về pháp lý","Nguyễn Thị Mai","25/09/2026","Tổ chức khảo sát thực địa nhóm nhỏ"),
        (22,"Tống Thị Kim Chi","0926 890 123","kimchi.tong@luxury.vn","Quận 5, TP.HCM","Chủ thời trang","Facebook Ads","Biệt Phủ Điền Trang","45–70","🟣 Chờ quyết định","22/09/2026","Đang trang trí lại biệt thự cũ, chưa quyết định chuyển","Trần Thị Lan","29/09/2026","Mời tham quan, so sánh lợi thế với BT cũ"),
        (23,"Hà Văn Bình","0904 012 345","binh.ha@construction.vn","Bà Rịa, BR-VT","Nhà thầu xây dựng","Coldcall","Điền An","5–8","🔴 Mới tiếp cận","23/09/2026","Ở địa phương, quan tâm dự án gần nhà","Lê Văn Hùng","","Tư vấn ưu đãi cư dân địa phương"),
        (24,"Trần Bích Ngân","0920 123 456","bichnan.tran@cfos.vn","Quận 7, TP.HCM","CFO","LinkedIn","Điền Sản","15–22","🟢 Quan tâm cao","24/09/2026","Tìm hiểu kỹ bài toán tài chính, so sánh tiết kiệm ngân hàng","Nguyễn Thị Mai","26/09/2026","Gửi phân tích IRR 10 năm"),
        (25,"Đinh Hoàng Minh","0917 234 567","minhhoang@agri.vn","Long An","Nông dân / Đất đai","Referral","Điền An","4–6","🔴 Mới tiếp cận","25/09/2026","Có đất nông nghiệp, muốn đổi sang đất ở","Trần Thị Lan","","Tư vấn bán đất cũ, mua Điền An"),
        (26,"Châu Thị Lan Anh","0933 345 678","lananh.chau@medic.vn","Quận 10, TP.HCM","Dược sĩ","TikTok","Điền An","3–5","🟡 Đang tư vấn","26/09/2026","Xem TikTok 3 lần, nhắn hỏi về trả góp","Lê Văn Hùng","28/09/2026","Kết nối ngân hàng hỗ trợ vay 70%"),
        (27,"Ngô Xuân Hải","0909 456 789","haixuan@startup.io","Quận 2, TP.HCM","Co-founder Startup","Google Ads","Biệt Phủ Điền Trang","30–50","🟢 Quan tâm cao","27/09/2026","Team building và retreat cho công ty tại resort","Nguyễn Thị Mai","30/09/2026","Khảo sát nhu cầu corporate retreat"),
        (28,"Trịnh Minh Châu","0921 567 890","chautm@professor.edu.vn","Quận 3, TP.HCM","Giáo sư đại học","Hội thảo","Điền Sản","10–15","🟣 Chờ quyết định","28/09/2026","Giảng dạy về BĐS, muốn sở hữu thực tế","Trần Thị Lan","","Gửi hợp đồng mẫu và FAQs pháp lý"),
        (29,"Lê Xuân Dũng","0925 678 901","dung.le@vietjet.vn","Bình Thạnh, TP.HCM","Phi công","Event","Điền Sản","18–25","🟡 Đang tư vấn","29/09/2026","Thu nhập cao, muốn đầu tư sinh lời thụ động","Lê Văn Hùng","","Gửi cashflow projection Điền Sản"),
        (30,"Phạm Quỳnh Anh","0912 789 012","quinhanh.pham@fashion.vn","Quận 1, TP.HCM","Blogger / KOL","Instagram","Biệt Phủ Điền Trang","25–40","🔴 Mới tiếp cận","30/09/2026","KOL được mời tham quan, xem xét hợp tác content","Nguyễn Thị Mai","","Đề xuất hợp tác content marketing"),
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
        # Status with color
        status = lead[9]
        sc = status_colors.get(status, row_bg)
        data_cell(ws, row, 11, status, align="center", bg=sc, bold=True)
        data_cell(ws, row, 12, lead[10], align="center", bg=row_bg)
        data_cell(ws, row, 13, lead[11], wrap=True, bg=row_bg)
        data_cell(ws, row, 14, lead[12], align="center", bg=row_bg)
        data_cell(ws, row, 15, lead[13], align="center", bg=YELLOW_STATUS if lead[13] else row_bg)
        data_cell(ws, row, 16, lead[14], wrap=True, bg=row_bg)

    # Summary row
    summary_row = len(leads_data) + 5 + 1
    ws.row_dimensions[summary_row].height = 28
    ws.merge_cells(start_row=summary_row, start_column=2, end_row=summary_row, end_column=10)
    cell = ws.cell(row=summary_row, column=2, value=f"📊 TỔNG: {len(leads_data)} khách hàng tiềm năng  |  🟢 Quan tâm cao: 8  |  🟡 Đang tư vấn: 8  |  🔵 Đặt cọc: 1  |  🔴 Mới: 7  |  🟣 Chờ: 4  |  ⚫ Không tiềm năng: 2")
    cell.fill = make_fill(GREEN_DARK)
    cell.font = Font(name="Calibri", size=10, bold=True, color="FFFDF9")
    cell.alignment = Alignment(horizontal="left", vertical="center", indent=1, wrap_text=True)
    cell.border = make_border()


# ═══════════════════════════════════════════════════════
# SHEET 3: THEO DÕI SALES PIPELINE
# ═══════════════════════════════════════════════════════
def build_sales(wb):
    ws = wb.create_sheet("💼 THEO DÕI SALES", 2)
    ws.freeze_panes = "A5"
    ws.sheet_view.showGridLines = False

    widths = [5, 5, 22, 16, 14, 14, 12, 15, 14, 14, 16, 18, 20]
    for i, w in enumerate(widths, 1):
        set_col_width(ws, i, w)

    ws.row_dimensions[2].height = 35
    ws.row_dimensions[3].height = 22

    title_row(ws, 2, 2, 13, "💼 PIPELINE SALES & FORECAST DOANH THU — THÁNG 09/2026", size=13)
    sub_header(ws, 3, 2, 13, "Saigon Farm Resort | 3 dòng sản phẩm: Biệt Phủ Điền Trang | Điền Sản | Điền An")

    # KPI Section
    ws.row_dimensions[5].height = 25
    title_row(ws, 5, 2, 13, "🎯 KPI THÁNG 09/2026 — MỤC TIÊU & THỰC HIỆN", bg=GREEN_LIGHT, size=11)

    kpi_data = [
        ("CHỈ TIÊU", "MỤC TIÊU THÁNG", "THỰC HIỆN", "TỶ LỆ", "TRẠNG THÁI"),
        ("Số leads mới tháng 9", "40 leads", "30 leads", "75%", "🟡 Cần tăng tốc"),
        ("Số lượng khách tham quan thực địa", "15 khách", "9 khách", "60%", "🟡 Đang cải thiện"),
        ("Số hợp đồng đặt cọc", "3 hợp đồng", "1 hợp đồng", "33%", "🔴 Cần đẩy mạnh"),
        ("Doanh thu dự kiến tháng (tỷ đồng)", "120 tỷ", "30 tỷ", "25%", "🔴 Cần bứt phá"),
        ("Tỷ lệ chuyển đổi Lead → Booking", "7.5%", "3.3%", "44%", "🟡 Đang tối ưu"),
    ]
    for i, row_data in enumerate(kpi_data, start=6):
        ws.row_dimensions[i].height = 26
        bgs = [GOLD_BG, WHITE] * 10
        for j, val in enumerate(row_data, start=2):
            if i == 6:  # header
                col_header(ws, i, j, val)
            else:
                bg = GOLD_BG if i % 2 == 0 else WHITE
                is_status = j == 6
                status_bg = RED_LIGHT if "🔴" in str(val) else YELLOW_STATUS if "🟡" in str(val) else GREEN_STATUS if "🟢" in str(val) else bg
                data_cell(ws, i, j, val, align="center" if j > 2 else "left", bold=(j==2), bg=status_bg if is_status else bg)

    # Pipeline Section
    ws.row_dimensions[13].height = 10
    ws.row_dimensions[14].height = 25
    title_row(ws, 14, 2, 13, "📋 CHI TIẾT PIPELINE GIAO DỊCH", bg=GOLD, fg=GREEN_DARK, size=11)

    pipeline_headers = ["#", "HỌ TÊN KHÁCH", "SP ĐĂNG KÝ", "GIÁ DỰ KIẾN (TỶ)", "NHÂN VIÊN", "STAGE", "XÁC SUẤT CHỐT", "NGÀY DỰ KIẾN CHỐT", "GIÁ TRỊ KỲ VỌNG (TỶ)", "TIẾN ĐỘ", "GHI CHÚ CHIẾN LƯỢC", "HÀNH ĐỘNG TIẾP THEO"]
    for j, h in enumerate(pipeline_headers, start=2):
        col_header(ws, 15, j, h)
    ws.row_dimensions[15].height = 40

    stage_colors = {
        "1. New Lead":     "F3F4F6",
        "2. Đang tư vấn":  YELLOW_STATUS,
        "3. Quan tâm cao": GREEN_STATUS,
        "4. Đặt cọc":      BLUE_LIGHT,
        "5. Ký HĐ":        "D1FAE5",
    }

    pipeline = [
        (1,"Lê Thị Bích Ngọc","Biệt Phủ Điền Trang","30","Trần Thị Lan","4. Đặt cọc","90%","15/09/2026","27","████████░░","Đã đặt cọc, chờ ký HĐ chính thức","Chuẩn bị hợp đồng, hỗ trợ pháp lý"),
        (2,"Nguyễn Minh Tuấn","Biệt Phủ Điền Trang","28","Trần Thị Lan","3. Quan tâm cao","70%","25/09/2026","19.6","██████░░░░","Đã thăm dự án 2 lần, đang thuyết phục vợ","Mời cả gia đình tham quan, picnic resort"),
        (3,"Võ Quốc Bảo","Điền Sản","18","Lê Văn Hùng","3. Quan tâm cao","65%","28/09/2026","11.7","██████░░░░","Cần kiểm tra pháp lý thêm","Cử luật sư nội bộ tư vấn trực tiếp"),
        (4,"Trương Quốc Khánh","Điền Sản","20","Trần Thị Lan","3. Quan tâm cao","60%","30/09/2026","12","██████░░░░","Đang so sánh với Phú Quốc","Gửi bảng so sánh ROI, IRR 10 năm"),
        (5,"Ngô Thế Vinh","Biệt Phủ Điền Trang","55","Trần Thị Lan","3. Quan tâm cao","55%","28/09/2026","30.25","█████░░░░░","CEO, dùng cho retreat team & nghỉ dưỡng","Chuẩn bị proposal corporate"),
        (6,"Lương Thị Phi Phi","Biệt Phủ Điền Trang","35","Trần Thị Lan","3. Quan tâm cao","55%","29/09/2026","19.25","█████░░░░░","Rất thích thiên nhiên, sắp hưu","Tổ chức weekend tour riêng cho gia đình"),
        (7,"Đinh Văn Toàn","Điền Sản","15","Lê Văn Hùng","3. Quan tâm cao","45%","27/09/2026","6.75","████░░░░░░","Đang thuyết phục gia đình","Gửi video testimonial khách cũ"),
        (8,"Lý Trường Giang","Biệt Phủ Điền Trang","70","Trần Thị Lan","3. Quan tâm cao","50%","27/09/2026","35","█████░░░░░","Cần chính sách VIP banker","Đề xuất gói thanh toán đặc biệt"),
        (9,"Trần Bích Ngân","Điền Sản","18","Nguyễn Thị Mai","2. Đang tư vấn","40%","30/09/2026","7.2","████░░░░░░","Cần phân tích IRR chi tiết","Gửi file Excel cashflow projection"),
        (10,"Phùng Văn Khải","Điền Sản","15","Nguyễn Thị Mai","2. Đang tư vấn","35%","25/09/2026","5.25","███░░░░░░░","Rất thích nhưng đang so sánh","Khảo sát thực địa nhóm, tạo social proof"),
        (11,"Vũ Thị Thanh Thúy","Biệt Phủ Điền Trang","40","Lê Văn Hùng","3. Quan tâm cao","40%","30/09/2026","16","████░░░░░░","Đang đàm phán với partner","Thẩm định pháp lý lần cuối"),
        (12,"Đỗ Minh Nghĩa","Điền Sản","22","Nguyễn Thị Mai","2. Đang tư vấn","35%","23/09/2026","7.7","███░░░░░░░","Muốn hiểu rõ mô hình vận hành cho thuê","Trình bày quản lý cho thuê turnkey"),
        (13,"Trịnh Thị Mỹ Linh","Điền An","12","Nguyễn Thị Mai","2. Đang tư vấn","30%","","3.6","███░░░░░░░","Cần vay ngân hàng 70%","Kết nối VPBank & Techcombank"),
        (14,"Phan Thị Hương","Điền An","5","Lê Văn Hùng","1. New Lead","15%","","0.75","█░░░░░░░░░","Comment Instagram, chưa xác nhận","DM, mời vào Zalo group dự án"),
        (15,"Phạm Hồng Anh","Điền Sản","10","Lê Văn Hùng","2. Đang tư vấn","35%","18/09/2026","3.5","███░░░░░░░","Bác sĩ bận, hẹn lại nhiều lần","Gửi brochure PDF + video tóm tắt"),
    ]

    for i, p in enumerate(pipeline, start=16):
        ws.row_dimensions[i].height = 28
        stage_bg = stage_colors.get(p[5], WHITE)
        alt_bg = WHITE if i % 2 == 0 else GOLD_BG
        data_cell(ws, i, 2, p[0], align="center", bold=True, bg=alt_bg)
        data_cell(ws, i, 3, p[1], bold=True, bg=alt_bg)
        data_cell(ws, i, 4, p[2], align="center", bg=GOLD_LIGHT, fg=GREEN_DARK, bold=True)
        data_cell(ws, i, 5, f"{p[3]} tỷ", align="center", bg=alt_bg)
        data_cell(ws, i, 6, p[4], align="center", bg=alt_bg)
        data_cell(ws, i, 7, p[5], align="center", bg=stage_bg, bold=True)
        data_cell(ws, i, 8, p[6], align="center", bg=alt_bg)
        data_cell(ws, i, 9, p[7] if p[7] else "—", align="center", bg=alt_bg)
        data_cell(ws, i, 10, f"{p[8]} tỷ", align="center", bold=True, bg=GREEN_STATUS, fg="064E3B")
        data_cell(ws, i, 11, p[9], align="left", bg=alt_bg)
        data_cell(ws, i, 12, p[10], wrap=True, bg=alt_bg)
        data_cell(ws, i, 13, p[11], wrap=True, bg=alt_bg)

    # Forecast summary
    total_forecast = sum(float(p[8]) for p in pipeline)
    high_prob = sum(float(p[8]) for p in pipeline if "Quan tâm" in p[5] or "Đặt cọc" in p[5])

    fs_row = len(pipeline) + 17
    ws.row_dimensions[fs_row].height = 30
    ws.merge_cells(start_row=fs_row, start_column=2, end_row=fs_row, end_column=8)
    cell = ws.cell(row=fs_row, column=2, value=f"💰 TỔNG GIÁ TRỊ PIPELINE: {total_forecast:.2f} tỷ đồng   |   🎯 Kỳ vọng khả năng cao: {high_prob:.2f} tỷ đồng")
    cell.fill = make_fill(GREEN_DARK)
    cell.font = Font(name="Calibri", size=11, bold=True, color="FFFDF9")
    cell.alignment = Alignment(horizontal="left", vertical="center", indent=1)
    cell.border = make_border()

    ws.merge_cells(start_row=fs_row, start_column=9, end_row=fs_row, end_column=13)
    cell2 = ws.cell(row=fs_row, column=9, value=f"🏆 Chốt được trong tháng: 1 HĐ (~30 tỷ)   |   Còn lại: 14 giao dịch đang theo dõi")
    cell2.fill = make_fill(GOLD)
    cell2.font = Font(name="Calibri", size=11, bold=True, color=GREEN_DARK)
    cell2.alignment = Alignment(horizontal="left", vertical="center", indent=1)
    cell2.border = make_border()


# ═══════════════════════════════════════════════════════
# SHEET 4: KÊNH TÌM KIẾM KHÁCH HÀNG
# ═══════════════════════════════════════════════════════
def build_channels(wb):
    ws = wb.create_sheet("📣 KÊNH TÌM KIẾM", 3)
    ws.sheet_view.showGridLines = False

    widths = [4, 25, 40, 40, 20, 20, 15]
    for i, w in enumerate(widths, 1):
        set_col_width(ws, i, w)

    ws.row_dimensions[2].height = 40
    ws.row_dimensions[3].height = 25
    title_row(ws, 2, 1, 7, "📣 HƯỚNG DẪN TÌM KIẾM & CÀO DATA KHÁCH HÀNG TIỀM NĂNG — SAIGON FARM RESORT", size=14)
    sub_header(ws, 3, 1, 7, "7 kênh tiếp cận hiệu quả nhất cho BĐS nghỉ dưỡng farm resort cao cấp tại Việt Nam 2026")

    channel_headers = ["KÊNH", "MÔ TẢ & NGUỒN DỮ LIỆU", "CÁCH THỰC HIỆN (CHI TIẾT)", "CÔNG CỤ / NỀN TẢNG", "CHI PHÍ ĐỀ XUẤT", "HIỆU QUẢ DỰ KIẾN"]
    for j, h in enumerate(channel_headers, start=2):
        col_header(ws, 4, j, h)
    ws.row_dimensions[4].height = 35

    channels = [
        (
            "1️⃣ FACEBOOK ADS\n& SOCIAL MEDIA",
            "Nhắm mục tiêu người dùng có sở thích: du lịch sinh thái, bất động sản nghỉ dưỡng, nông trại, second home; Thu nhập cao; Tuổi 30–55",
            "• Chạy ads Facebook/Instagram nhắm vào: sở thích Hồ Tràm, Vũng Tàu, BĐS, resort\n• Tạo landing page chứa Form đăng ký nhận brochure\n• Retarget người đã xem video/website\n• Dùng Lookalike Audience từ data KH cũ\n• Đăng bài organic trong group BĐS nghỉ dưỡng",
            "Facebook Ads Manager\nInstagram Ads\nCanva (thiết kế)\nLeadPages / Carrd (landing page)",
            "20–50 triệu/tháng",
            "15–25 leads/tháng\nCPL: 1–3 triệu"
        ),
        (
            "2️⃣ TIKTOK\n& VIDEO MARKETING",
            "Gen Z và Millennials giàu tìm second home; Người xem nội dung về lifestyle nông trang, thiên nhiên, \"sống chậm\"",
            "• Đăng 2–3 video/tuần: tour dự án, cảnh hồ 100ha, lúc bình minh/hoàng hôn\n• Dùng hashtag: #farmresort #nghỉdưỡng #batdongsan #secondhome\n• Hợp tác KOL/KOC du lịch, review bất động sản\n• TikTok Ads targeting sở thích liên quan\n• Chạy challenge \"Ngôi nhà mơ ước\"",
            "TikTok Creator Studio\nTikTok Ads Manager\nCapCut (edit video)\nKOL Platform",
            "15–35 triệu/tháng",
            "10–20 leads/tháng\nCPL: 1.5–3.5 triệu"
        ),
        (
            "3️⃣ ZALO ZNS\n& OA MARKETING",
            "Khách hàng đã có data SĐT từ events, database cũ, đối tác; Zalo là nền tảng số 1 VN với 75M+ user",
            "• Tạo Zalo Official Account dự án, đăng nội dung đều đặn\n• Gửi ZNS (Zalo Notification Service) cho danh sách SĐT tiềm năng\n• Tham gia và tương tác trong Group Zalo BĐS Hồ Tràm, Vũng Tàu\n• Tạo mini-game/survey trên Zalo để thu lead\n• Tích hợp chatbot tự động tư vấn 24/7",
            "Zalo OA (miễn phí)\nZalo Ads\nZNS API\nMindX / Subiz (chatbot)",
            "5–20 triệu/tháng",
            "20–40 leads/tháng\nCPL: 0.5–1 triệu"
        ),
        (
            "4️⃣ GOOGLE ADS\n& SEO",
            "Người dùng đang chủ động tìm mua BĐS nghỉ dưỡng, resort farm, Hồ Tràm, Đất Đỏ trên Google",
            "• Chạy Google Search Ads với từ khóa: \"mua biệt thự Hồ Tràm\", \"farm resort nghỉ dưỡng\", \"second home Vũng Tàu\"\n• Tối ưu SEO website saigonfarmresort.com với blog chuyên đề\n• Chạy Google Display Ads retarget website visitor\n• Đăng ký Google My Business và cập nhật thường xuyên\n• Tạo nội dung YouTube Shorts",
            "Google Ads\nGoogle Analytics 4\nGoogle Search Console\nSEMrush / Ahrefs",
            "20–40 triệu/tháng",
            "10–15 leads/tháng\nCPL: 2–4 triệu"
        ),
        (
            "5️⃣ SÀN BĐS\n& PORTAL",
            "Người dùng đang tìm mua bán trên các portal lớn nhất Việt Nam; Khách hàng có intent cao",
            "• Đăng sản phẩm trên batdongsan.com.vn, Centa, Homedy, Toancau.vn\n• Mua gói VIP PRO để hiển thị ưu tiên\n• Cập nhật hình ảnh chất lượng cao, video 360°\n• Trả lời mọi tin nhắn/bình luận trong 1 giờ\n• Theo dõi báo cáo xem trang, liên hệ hàng tuần",
            "batdongsan.com.vn\nCenta.vn\nHomedy.com\nNhaDat.com.vn",
            "5–15 triệu/tháng",
            "8–15 leads/tháng\nCPL: 1–2 triệu"
        ),
        (
            "6️⃣ EVENT\n& OPEN HOUSE",
            "Tổ chức sự kiện tham quan thực địa để tạo trải nghiệm cảm xúc trực tiếp — hình thức chốt deal hiệu quả nhất",
            "• Tổ chức Open House 1–2 lần/tháng: tham quan hồ, picnic, thưởng thức ẩm thực\n• Hội thảo đầu tư BĐS nghỉ dưỡng kết hợp khảo sát thực địa\n• Workshop \"Sống xanh & Đầu tư bền vững\" với speaker khách mời\n• Bus tour VIP từ TP.HCM vào cuối tuần (Thứ 7)\n• Corporate retreat cho doanh nghiệp",
            "Eventbrite (đăng ký)\nZalo/FB Event\nCanva (poster)\nThue xe bus VIP",
            "30–70 triệu/sự kiện",
            "5–15 leads VIP/event\nTỷ lệ chốt cao: 20–30%"
        ),
        (
            "7️⃣ REFERRAL\n& NETWORKING",
            "Khách cũ giới thiệu khách mới — nguồn lead chất lượng cao nhất; Mạng lưới doanh nhân, ngân hàng, luật sư",
            "• Xây dựng chương trình giới thiệu: thưởng 1–2% giá trị giao dịch cho người giới thiệu\n• Hợp tác với ngân hàng (VPBank, Techcombank) chia sẻ data khách VIP\n• Kết nối câu lạc bộ doanh nhân: YPO, EO, Saigon CEO Club\n• Tham gia hội golf, tennis để gặp gỡ khách thượng lưu\n• Xây dựng cộng đồng chủ nhân SFR trên Zalo, FB Group riêng",
            "CRM nội bộ\nZalo Group riêng\nLinkedIn Sales Navigator\nReferral tracking tool",
            "Hoa hồng giới thiệu\n(1–2% giá trị GD)",
            "3–8 leads/tháng\nTỷ lệ chốt: 40–60%"
        ),
    ]

    for i, ch in enumerate(channels, start=5):
        ws.row_dimensions[i].height = 120
        alt_bg = WHITE if i % 2 == 0 else GOLD_BG
        data_cell(ws, i, 1, "", bg=alt_bg)
        data_cell(ws, i, 2, ch[0], bold=True, align="center", bg=GOLD_LIGHT, fg=GREEN_DARK, wrap=True)
        data_cell(ws, i, 3, ch[1], wrap=True, bg=alt_bg)
        data_cell(ws, i, 4, ch[2], wrap=True, bg=alt_bg)
        data_cell(ws, i, 5, ch[3], wrap=True, bg=alt_bg)
        data_cell(ws, i, 6, ch[4], align="center", bg=YELLOW_STATUS, wrap=True)
        data_cell(ws, i, 7, ch[5], align="center", bg=GREEN_STATUS, fg="064E3B", wrap=True)

    # Legal notice
    note_row = len(channels) + 6
    ws.row_dimensions[note_row].height = 60
    ws.merge_cells(start_row=note_row, start_column=1, end_row=note_row, end_column=7)
    cell = ws.cell(row=note_row, column=1,
        value="⚠️ LƯU Ý PHÁP LÝ & ĐẠO ĐỨC: Việc thu thập và sử dụng dữ liệu cá nhân phải tuân thủ Nghị định 13/2023/NĐ-CP về Bảo vệ Dữ liệu Cá nhân của Việt Nam. "
              "Chỉ thu thập thông tin khi có sự đồng ý của người dùng (opt-in). Không cào dữ liệu cá nhân từ mạng xã hội mà không có sự cho phép. "
              "Các phương pháp được khuyến nghị trong tài liệu này đều tuân thủ quy định: người dùng tự điền form, đăng ký sự kiện, hoặc liên hệ trực tiếp. "
              "Không thực hiện cold-call hàng loạt từ danh sách mua. Ưu tiên chất lượng lead hơn số lượng để bảo vệ thương hiệu MDS Land & Living.")
    cell.fill = make_fill(RED_LIGHT)
    cell.font = Font(name="Calibri", size=9, bold=True, color="7F1D1D")
    cell.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True, indent=1)
    cell.border = make_border()


# ═══════════════════════════════════════════════════════
# SHEET 5: BÁO CÁO TỔNG HỢP THÁNG
# ═══════════════════════════════════════════════════════
def build_report(wb):
    ws = wb.create_sheet("📊 BÁO CÁO THÁNG", 4)
    ws.sheet_view.showGridLines = False

    widths = [4, 30, 20, 20, 20, 15, 20, 20]
    for i, w in enumerate(widths, 1):
        set_col_width(ws, i, w)

    ws.row_dimensions[2].height = 40
    ws.row_dimensions[3].height = 22
    title_row(ws, 2, 1, 8, "📊 BÁO CÁO HIỆU QUẢ KÊNH BÁN HÀNG — THÁNG 09/2026", size=14)
    sub_header(ws, 3, 1, 8, "Saigon Farm Resort | Phân tích nguồn lead, tỷ lệ chuyển đổi và chi phí mỗi lead")

    # Channel performance table
    ws.row_dimensions[5].height = 25
    title_row(ws, 5, 1, 8, "📈 HIỆU QUẢ THEO KÊNH TIẾP CẬN", bg=GREEN_LIGHT, size=11)

    ch_headers = ["KÊNH", "SỐ LEADS", "THAM QUAN", "ĐẶT CỌC", "CHI PHÍ (TR)", "CPL (TR/LEAD)", "TỶ LỆ CHUYỂN ĐỔI"]
    for j, h in enumerate(ch_headers, start=2):
        col_header(ws, 6, j, h)
    ws.row_dimensions[6].height = 35

    ch_perf = [
        ("Facebook Ads", 8, 3, 0, 35, 4.4, "0%"),
        ("TikTok & Video", 5, 2, 0, 20, 4.0, "0%"),
        ("Zalo ZNS & OA", 7, 2, 0, 8, 1.1, "0%"),
        ("Google Ads & SEO", 4, 1, 0, 30, 7.5, "0%"),
        ("Sàn BĐS (Portal)", 2, 1, 0, 10, 5.0, "0%"),
        ("Event & Open House", 2, 2, 1, 50, 25.0, "50%"),
        ("Referral & Network", 2, 2, 0, 0, 0, "0%"),
        ("TỔNG CỘNG", 30, 13, 1, 153, 5.1, "3.3%"),
    ]

    for i, row in enumerate(ch_perf, start=7):
        ws.row_dimensions[i].height = 28
        is_total = row[0] == "TỔNG CỘNG"
        bg = GREEN_DARK if is_total else (WHITE if i % 2 == 0 else GOLD_BG)
        fg = "FFFDF9" if is_total else "1F2937"
        for j, val in enumerate(row, start=2):
            data_cell(ws, i, j, val, align="center" if j > 2 else "left", bold=is_total, bg=bg, fg=fg)

    # Product breakdown
    ws.row_dimensions[17].height = 10
    ws.row_dimensions[18].height = 25
    title_row(ws, 18, 1, 8, "🏡 PHÂN BỐ QUAN TÂM THEO DÒNG SẢN PHẨM", bg=GOLD, fg=GREEN_DARK, size=11)

    prod_headers = ["DÒNG SẢN PHẨM", "MÔ TẢ", "SỐ LEADS QUAN TÂM", "ĐANG TƯ VẤN", "ĐẶT CỌC", "GIÁ THAM KHẢO", "GHI CHÚ"]
    for j, h in enumerate(prod_headers, start=2):
        col_header(ws, 19, j, h)
    ws.row_dimensions[19].height = 35

    products = [
        ("🏛️ Biệt Phủ Điền Trang", "Biệt thự cao cấp nhất, khuôn viên rộng, view hồ trực tiếp, thiết kế cá nhân hóa", 12, 6, 1, "25–100 tỷ đồng", "Dòng flagship, nhắm CEO/doanh nhân thành đạt"),
        ("🌾 Điền Sản", "Sản phẩm đầu tư sinh lời, cho thuê turnkey, quản lý vận hành chuyên nghiệp", 11, 7, 0, "10–25 tỷ đồng", "Phù hợp nhà đầu tư, ROI 8–12%/năm"),
        ("🏡 Điền An", "Dòng tiết kiệm nhất, phù hợp gia đình trẻ, second home cuối tuần", 7, 4, 0, "3–8 tỷ đồng", "Dễ tiếp cận, nhiều chính sách vay hỗ trợ"),
    ]

    for i, p in enumerate(products, start=20):
        ws.row_dimensions[i].height = 50
        alt_bg = WHITE if i % 2 == 0 else GOLD_BG
        data_cell(ws, i, 2, p[0], bold=True, bg=GOLD_LIGHT, fg=GREEN_DARK, wrap=True)
        data_cell(ws, i, 3, p[1], wrap=True, bg=alt_bg)
        data_cell(ws, i, 4, p[2], align="center", bold=True, bg=BLUE_LIGHT)
        data_cell(ws, i, 5, p[3], align="center", bg=YELLOW_STATUS)
        data_cell(ws, i, 6, p[4], align="center", bg=GREEN_STATUS)
        data_cell(ws, i, 7, p[5], align="center", bold=True, bg=alt_bg)
        data_cell(ws, i, 8, p[6], wrap=True, bg=alt_bg)

    # Insights & Action Plan
    ws.row_dimensions[24].height = 10
    ws.row_dimensions[25].height = 25
    title_row(ws, 25, 1, 8, "💡 NHẬN XÉT & HÀNH ĐỘNG ƯU TIÊN TUẦN CUỐI THÁNG 9/2026", bg=GREEN_DARK, size=11)

    insights = [
        ("✅ ĐIỂM MẠNH", "- Event Open House cho tỷ lệ chốt cao nhất (50%)\n- KH referral chất lượng cao, tỷ lệ tham quan 100%\n- Pipeline 206+ tỷ đồng với 15 cơ hội đang theo dõi"),
        ("⚠️ ĐIỂM CẦN CẢI THIỆN", "- CPL Google Ads cao (7.5 tr/lead), cần tối ưu từ khóa\n- Tỷ lệ chuyển đổi lead→booking chỉ 3.3%, cần nuturing tốt hơn\n- 7 leads mới cần được tiếp cận nhanh trong 48h"),
        ("🎯 HÀNH ĐỘNG TUẦN 4 (22–30/9)", "1. Chốt Nguyễn Minh Tuấn & Lê Thị Bích Ngọc (HĐ chính thức)\n2. Tổ chức bus tour VIP thứ 7 (27/9) cho 5 KH quan tâm cao\n3. Gửi file IRR cho Trần Bích Ngân & Trương Quốc Khánh\n4. Liên hệ 7 leads mới trong ngày hôm nay"),
        ("📅 KẾ HOẠCH THÁNG 10/2026", "- Tăng ngân sách Facebook Ads lên 50 triệu/tháng\n- Tổ chức 2 event Open House (4/10 và 18/10)\n- Khởi động chương trình referral chính thức (thưởng 2%)\n- Target: 60 leads, 5 booking, 300 tỷ pipeline"),
    ]

    for i, (label, content) in enumerate(insights, start=26):
        ws.row_dimensions[i].height = 75
        bgs = [GOLD_LIGHT, RED_LIGHT, GREEN_STATUS, BLUE_LIGHT]
        ws.merge_cells(start_row=i, start_column=2, end_row=i, end_column=3)
        c1 = ws.cell(row=i, column=2, value=label)
        c1.fill = make_fill(bgs[i - 26])
        c1.font = Font(name="Calibri", size=10, bold=True, color=GREEN_DARK)
        c1.alignment = Alignment(horizontal="left", vertical="top", wrap_text=True, indent=1)
        c1.border = make_border()
        ws.merge_cells(start_row=i, start_column=4, end_row=i, end_column=8)
        c2 = ws.cell(row=i, column=4, value=content)
        c2.font = Font(name="Calibri", size=9, color="1F2937")
        c2.fill = make_fill(WHITE)
        c2.alignment = Alignment(horizontal="left", vertical="top", wrap_text=True, indent=1)
        c2.border = make_border()


# ═══════════════════════════════════════════════════════
# SHEET 6: SCRIPT TƯ VẤN
# ═══════════════════════════════════════════════════════
def build_scripts(wb):
    ws = wb.create_sheet("🎯 SCRIPT TƯ VẤN", 5)
    ws.sheet_view.showGridLines = False

    widths = [4, 28, 60, 60]
    for i, w in enumerate(widths, 1):
        set_col_width(ws, i, w)

    ws.row_dimensions[2].height = 40
    ws.row_dimensions[3].height = 22
    title_row(ws, 2, 1, 4, "🎯 SCRIPT TƯ VẤN SAIGON FARM RESORT — THEO DÒNG SẢN PHẨM", size=14)
    sub_header(ws, 3, 1, 4, "Kịch bản tư vấn được tối ưu hóa cho từng nhóm khách hàng và từng bước trong phễu bán hàng")

    scripts = [
        {
            "title": "📞 SCRIPT GỌI ĐIỆN LẦN ĐẦU — KHÁCH HÀNG MỚI (Universal)",
            "situation": "Khách hàng đã để lại form/comment nhưng chưa được tư vấn",
            "script": (
                "Xin chào, anh/chị [Tên]!\n\n"
                "Em là [Tên Sales], phụ trách tư vấn tại Saigon Farm Resort — dự án điền trang nghỉ dưỡng sinh thái ven hồ 100ha của MDS Land & Living.\n\n"
                "Em thấy anh/chị vừa quan tâm đến dự án của bọn em. Anh/chị có tiện nói chuyện khoảng 5 phút không ạ?\n\n"
                "[Nếu có thời gian]\n"
                "Anh/chị đang tìm kiếm bất động sản để [ở thực / đầu tư / nghỉ dưỡng]?\n\n"
                "Saigon Farm Resort đang có 3 dòng sản phẩm rất phù hợp với nhu cầu đó ạ:\n"
                "• Biệt Phủ Điền Trang: cao cấp nhất, view hồ trực tiếp\n"
                "• Điền Sản: đầu tư sinh lời, cho thuê turnkey\n"
                "• Điền An: phù hợp gia đình trẻ, giá tốt nhất\n\n"
                "Anh/chị muốn em gửi tài liệu chi tiết qua Zalo không ạ? Và mình có thể sắp xếp tham quan thực địa trong cuối tuần này không?"
            )
        },
        {
            "title": "🏛️ SCRIPT TƯ VẤN BIỆT PHỦ ĐIỀN TRANG — KHÁCH CEO/DOANH NHÂN",
            "situation": "Khách hàng: CEO, Doanh nhân, Ngân sách 25–100 tỷ, Mua ở thực + đầu tư",
            "script": (
                "Anh/chị [Tên], mình hiểu rằng với vị thế của anh/chị, điều quan trọng nhất khi sở hữu bất động sản là:\n"
                "✓ Pháp lý tuyệt đối an toàn\n"
                "✓ Giá trị tài sản gia tăng theo thời gian\n"
                "✓ Không gian sống xứng tầm, riêng tư\n\n"
                "Biệt Phủ Điền Trang của Saigon Farm Resort đáp ứng đầy đủ 3 tiêu chí đó:\n\n"
                "1. PHÁP LÝ: 100% đất ở thổ cư lâu dài, sổ đỏ riêng, công chứng sang tên ngay lập tức. Không rủi ro.\n\n"
                "2. GIÁ TRỊ: Hiện tại giá chỉ bằng 1/4 đến 1/3 so với Hồ Tràm (đang neo 30–50 triệu/m²). Khi sân bay Long Thành vận hành và cao tốc thông xe, gap này sẽ thu hẹp nhanh chóng.\n\n"
                "3. KHÔNG GIAN: Ôm trọn mặt hồ 100ha — vi khí hậu mát mẻ, cách TP.HCM chỉ 60 phút. Mật độ xây dựng tối đa 20%, 55% diện tích là cây xanh và mặt nước.\n\n"
                "Cho phép em sắp xếp một buổi tham quan thực địa riêng cho anh/chị, kết hợp bữa tối tại nhà hàng farm-to-table của dự án vào cuối tuần?"
            )
        },
        {
            "title": "🌾 SCRIPT TƯ VẤN ĐIỀN SẢN — KHÁCH ĐẦU TƯ SINH LỜI",
            "situation": "Khách hàng: Nhà đầu tư tài chính, Ngân sách 10–25 tỷ, Cần dòng tiền thụ động",
            "script": (
                "Anh/chị [Tên], cho phép em trình bày bài toán tài chính của Điền Sản:\n\n"
                "📊 BÀI TOÁN ĐẦU TƯ ĐIỀN SẢN:\n"
                "• Giá mua: 15 tỷ đồng\n"
                "• Vốn tự có (30%): 4.5 tỷ\n"
                "• Vay ngân hàng (70%): 10.5 tỷ — lãi suất ưu đãi 24 tháng đầu ~7.5%/năm\n\n"
                "📈 DÒNG TIỀN HÀNG NĂM:\n"
                "• Doanh thu cho thuê: 1.8–2.4 tỷ/năm (tỷ lệ lấp đầy 65–85% từ quản lý turnkey)\n"
                "• Trả lãi + gốc ngân hàng: ~1.2 tỷ/năm\n"
                "• Thu nhập ròng sau trả vay: 600 triệu – 1.2 tỷ/năm\n"
                "• ROI trên vốn tự có: 13–27%/năm\n\n"
                "💰 SAU 5 NĂM:\n"
                "• Đã trả xong 50% khoản vay\n"
                "• Đất tăng giá ước tính 40–80% (căn cứ sân bay Long Thành)\n"
                "• Tài sản có thể đạt 25–35 tỷ trong khi vốn bỏ ra chỉ 4.5 tỷ\n\n"
                "Anh/chị muốn em gửi file Excel chi tiết hơn với các kịch bản lạc quan/trung bình/thận trọng không ạ?"
            )
        },
        {
            "title": "🏡 SCRIPT TƯ VẤN ĐIỀN AN — KHÁCH GIA ĐÌNH TRẺ / SECOND HOME",
            "situation": "Khách hàng: Gia đình 30–45 tuổi, 2 con nhỏ, Ngân sách 3–8 tỷ, Mua nhà nghỉ cuối tuần",
            "script": (
                "Anh/chị [Tên], mình hiểu áp lực cuộc sống thành phố có thể khiến cả gia đình mệt mỏi. Điền An được tạo ra đúng với mục đích đó:\n\n"
                "🌿 TẠI SAO ĐIỀN AN LÀ SỰ LỰA CHỌN HOÀN HẢO?\n\n"
                "• Chỉ 60 phút từ trung tâm TP.HCM — đủ gần để thoát phố cuối tuần, đủ xa để thực sự xả stress\n"
                "• Trẻ em có: Nông trại hữu cơ, Làng ngựa Việt Mã Viên, khu học tập kỹ năng sống\n"
                "• Ông bà có: Đường dưỡng sinh ven hồ, hồ bơi vô cực, không khí trong lành\n"
                "• Cả nhà có: Nhà hàng farm-to-table, sân Pickleball, kayak trên hồ 100ha\n\n"
                "💰 BÀI TOÁN TÀI CHÍNH THÂN THIỆN:\n"
                "• Giá từ 3 tỷ đồng\n"
                "• Vay ngân hàng 70%, trả góp chỉ 15–20 triệu/tháng\n"
                "• Có thể cho thuê ngắn ngày khi không ở để có thêm thu nhập thụ động\n\n"
                "Khi không sử dụng, BQL dự án có thể cho thuê ngắn ngày giúp anh/chị, thu nhập đủ bù phí quản lý.\n\n"
                "Anh/chị có thể dẫn cả gia đình tham quan thực địa vào Thứ 7 này không? Em sẽ sắp xếp trải nghiệm picnic bên hồ cho bé."
            )
        },
        {
            "title": "🔄 SCRIPT CHĂM SÓC SAU LẦN GẶP ĐẦU / FOLLOW-UP",
            "situation": "Khách hàng đã gặp/tham quan nhưng chưa quyết định (trạng thái 🟡 Đang tư vấn / 🟣 Chờ quyết định)",
            "script": (
                "Xin chào anh/chị [Tên], em [Tên Sales] đây ạ.\n\n"
                "Sau buổi tham quan/tư vấn vừa rồi, anh/chị đã có thêm thông tin gì cần em hỗ trợ giải đáp không?\n\n"
                "[Nếu KH đang hỏi thêm]\n"
                "Em hiểu đây là quyết định quan trọng. Để giúp anh/chị đưa ra quyết định tự tin hơn, em muốn hỏi:\n"
                "• Điều gì khiến anh/chị còn băn khoăn nhất? (Pháp lý? Tài chính? Thời điểm?)\n\n"
                "[Xử lý từng objection]\n"
                "• \"Giá hơi cao\": Em hiểu. Nhưng so với mặt bằng Hồ Tràm đang 30–50tr/m², đây vẫn là cơ hội tốt. Anh/chị muốn em tính thêm phương án vay không?\n"
                "• \"Chưa chắc pháp lý\": Em sẵn sàng làm việc trực tiếp với đội pháp lý để review hồ sơ cùng anh/chị.\n"
                "• \"Đang so sánh với dự án khác\": Rất tự nhiên! Anh/chị muốn em lập bảng so sánh chi tiết không?\n\n"
                "Anh/chị đang suy nghĩ đến bao giờ thì có thể quyết định ạ? Để em track lại và hỗ trợ kịp thời nếu có thêm thông tin mới từ dự án."
            )
        },
    ]

    for i, script in enumerate(scripts, start=5):
        ws.row_dimensions[i].height = 220
        alt_bg = WHITE if i % 2 == 0 else GOLD_BG
        data_cell(ws, i, 1, "", bg=alt_bg)
        ws.merge_cells(start_row=i, start_column=2, end_row=i, end_column=2)
        c_title = ws.cell(row=i, column=2)
        c_title.value = f"{script['title']}\n\n📝 Tình huống:\n{script['situation']}"
        c_title.fill = make_fill(GOLD_LIGHT)
        c_title.font = Font(name="Calibri", size=9, bold=True, color=GREEN_DARK)
        c_title.alignment = Alignment(horizontal="left", vertical="top", wrap_text=True, indent=1)
        c_title.border = make_border()

        ws.merge_cells(start_row=i, start_column=3, end_row=i, end_column=4)
        c_script = ws.cell(row=i, column=3)
        c_script.value = script['script']
        c_script.fill = make_fill(alt_bg)
        c_script.font = Font(name="Calibri", size=9, color="1F2937")
        c_script.alignment = Alignment(horizontal="left", vertical="top", wrap_text=True, indent=1)
        c_script.border = make_border()


# ═══════════════════════════════════════════════════════
# MAIN: BUILD WORKBOOK
# ═══════════════════════════════════════════════════════
def main():
    wb = openpyxl.Workbook()
    # Remove default sheet
    if "Sheet" in wb.sheetnames:
        del wb["Sheet"]

    print("📊 Đang tạo file Excel CRM Saigon Farm Resort...")

    print("  ▶ Sheet 1: Trang bìa...")
    build_cover(wb)

    print("  ▶ Sheet 2: Khách hàng tiềm năng (30 leads)...")
    build_leads(wb)

    print("  ▶ Sheet 3: Theo dõi Sales Pipeline...")
    build_sales(wb)

    print("  ▶ Sheet 4: Kênh tìm kiếm khách hàng...")
    build_channels(wb)

    print("  ▶ Sheet 5: Báo cáo tổng hợp tháng...")
    build_report(wb)

    print("  ▶ Sheet 6: Script tư vấn...")
    build_scripts(wb)

    output_path = "SFR_CRM_KhachHang_Sales_T09_2026.xlsx"
    wb.save(output_path)
    print(f"\n✅ Hoàn thành! File đã được lưu tại: {output_path}")
    print(f"   📋 6 sheets: Trang Bìa | Khách Hàng TN | Sales Pipeline | Kênh Tìm Kiếm | Báo Cáo | Script")

if __name__ == "__main__":
    main()
