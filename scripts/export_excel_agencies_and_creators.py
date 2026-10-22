#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tạo file Excel chuyên nghiệp (multi-sheet) tổng hợp:
1. Danh sách Toàn bộ Đại lý & Sàn BĐS tại TP.HCM, Vũng Tàu, Đồng Nai
2. Danh sách Sales chiến binh & Content Creators (YouTube, TikTok, Facebook) chuyên BĐS BR-VT, Hồ Tràm, Đất Đỏ, Đồng Nai
3. Kịch bản tiếp cận & Chính sách hoa hồng hợp tác
Dự án: Saigon Farm Resort (Hồ Lồ Ồ, Đất Đỏ)
"""

import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
import csv
import os

def build_excel():
    wb = openpyxl.Workbook()
    # Xoá sheet mặc định
    wb.remove(wb.active)
    
    # Định dạng chung
    font_header = Font(name='Arial', size=11, bold=True, color='FFFFFF')
    fill_header_navy = PatternFill(start_color='1A365D', end_color='1A365D', fill_type='solid')
    fill_header_teal = PatternFill(start_color='0D9488', end_color='0D9488', fill_type='solid')
    fill_header_purple = PatternFill(start_color='4C1D95', end_color='4C1D95', fill_type='solid')
    
    font_bold = Font(name='Arial', size=10, bold=True)
    font_regular = Font(name='Arial', size=10)
    font_italic = Font(name='Arial', size=9, italic=True, color='555555')
    
    border_thin = Border(
        left=Side(style='thin', color='D1D5DB'),
        right=Side(style='thin', color='D1D5DB'),
        top=Side(style='thin', color='D1D5DB'),
        bottom=Side(style='thin', color='D1D5DB')
    )
    
    fill_zebra = PatternFill(start_color='F9FAFB', end_color='F9FAFB', fill_type='solid')
    fill_highlight = PatternFill(start_color='FEF3C7', end_color='FEF3C7', fill_type='solid')

    # =========================================================================
    # SHEET 1: ĐẠI LÝ & SÀN BĐS TPHCM - VŨNG TÀU - ĐỒNG NAI
    # =========================================================================
    ws1 = wb.create_sheet(title="Dai_Ly_San_BDS_TPHCM_VT_DN")
    ws1.views.sheetView[0].showGridLines = True
    
    headers1 = [
        "STT", "Khu Vực", "Địa Bàn", "Tên Sàn / Công Ty BĐS", 
        "Người Đại Diện / Chức Vụ", "Số Điện Thoại", "Địa Chỉ Trụ Sở / Văn Phòng", 
        "Phân Khúc Thế Mạnh", "Mục Tiêu Hợp Tác", "Mã Số Thuế"
    ]
    ws1.append(headers1)
    
    # Dữ liệu Sàn tại TP.HCM
    agencies_hcm = [
        ("TP.HCM", "Quận 1 / Toàn quốc", "CÔNG TY CỔ PHẦN DỊCH VỤ VÀ ĐỊA ỐC ĐẤT XANH MIỀN NAM (DXS)", "Đỗ Văn Mạnh (TGĐ)", "0933674114", "27 Đinh Bộ Lĩnh, P.24, Bình Thạnh, TP.HCM", "Đại lý phân phối tổng lực BĐS Đông Nam Bộ", "Ký kết Đại lý F1 phân phối độc quyền rổ hàng", "0309594191"),
        ("TP.HCM", "Quận 3 / Toàn quốc", "CÔNG TY CỔ PHẦN TẬP ĐOÀN DKRA (DKRA REALTY)", "Phạm Lâm (Chủ tịch HĐQT)", "0917637887", "63 - 67 An Điềm, Phường 10, Quận 5, TP.HCM", "Chuyên BĐS nghỉ dưỡng, Second home cao cấp", "Đại lý F1 chiến lược / Phân phối độc quyền", "0310705646"),
        ("TP.HCM", "Quận 7 / Nam Sài Gòn", "CÔNG TY CỔ PHẦN TẬP ĐOÀN KHẢI HOÀN LAND", "Nguyễn Khải Hoàn (Chủ tịch)", "0903333333", "Tòa nhà Khải Hoàn, 5-7-9-11 Nguyễn Hữu Thọ, Nhà Bè, TP.HCM", "Mạng lưới nghìn sales, mạnh BĐS nghỉ dưỡng & ven biển", "Đại lý phân phối tổng lực F1", "0309101235"),
        ("TP.HCM", "Quận 1 / Khu Đông", "CÔNG TY TNHH BẤT ĐỘNG SẢN SMARTREALTORS & PARTNERS", "Đặng Quốc Việt (TGĐ)", "0916257825", "Tầng 2, Tòa nhà Packsimex, 52 Đông Du, Bến Nghé, Quận 1", "Chuyên phân khúc BĐS nghỉ dưỡng biển, biệt thự hạng sang", "Đại lý F1 chuyên biệt dòng Biệt Phủ VIP", "0313638400"),
        ("TP.HCM", "Bình Thạnh / TP. Thủ Đức", "CÔNG TY CỔ PHẦN BẤT ĐỘNG SẢN DANH KHÔI (DKRS)", "Nguyễn Văn Sinh (Phó TGĐ)", "0909199999", "Số 3 Trần Nhật Duật, P. Tân Định, Quận 1, TP.HCM", "Chuyên dự án đất nền và BĐS nghỉ dưỡng Bà Rịa - Vũng Tàu", "Đại lý F1 liên kết rổ hàng Điền Sản", "0312693739"),
        ("TP.HCM", "Quận 2 / TP. Thủ Đức", "CÔNG TY CỔ PHẦN CÔNG NGHỆ BẤT ĐỘNG SẢN REVER", "Phan Lê Mạnh (CEO)", "0901777017", "Số 27 Đường số 4, Khu An Phú, TP. Thủ Đức, TP.HCM", "BĐS ứng dụng công nghệ, tệp khách đầu tư TP.HCM", "Đại lý F2 liên kết bán hàng trực tuyến", "0313661123"),
        ("TP.HCM", "Quận 10 / Tân Bình", "CÔNG TY CỔ PHẦN BẤT ĐỘNG SẢN ASIAN HOLDING", "Nguyễn Văn Hậu (TGĐ)", "0909898899", "Số 76 - 78 Đường 9A, KDC Trung Sơn, Bình Hưng, TP.HCM", "Chuyên BĐS sinh thái, đất vườn, Second home ven đô", "Đại lý F1 dòng Điền Sản & Điền An", "0313798991"),
        ("TP.HCM", "Phú Nhuận / Bình Thạnh", "CÔNG TY CỔ PHẦN BẤT ĐỘNG SẢN YESHOUSE", "Lê Văn Hùng (Giám đốc)", "0938499068", "Số 39 Trương Đăng Quế, Phường 1, Gò Vấp, TP.HCM", "Chuyên sản phẩm đất vườn, farmstay ven hồ nghỉ dưỡng", "Đại lý chiến lược dòng Điền Trang sinh thái", "0314890123"),
        ("TP.HCM", "Quận 1 / Toàn cầu", "CÔNG TY CỔ PHẦN ERA VIETNAM (ERA REAL ESTATE)", "Bùi Trung Kiên (TGĐ)", "0908889988", "Tầng 12, Tòa nhà Pearl Plaza, 561A Điện Biên Phủ, Bình Thạnh", "Mô hình môi giới quốc tế, tệp khách Việt kiều & Expat", "Đại lý phân phối khách quốc tế & Điền An", "0314412345"),
        ("TP.HCM", "Quận 3 / Miền Nam", "CÔNG TY CỔ PHẦN BẤT ĐỘNG SẢN THẾ KỶ (CENLAND MIỀN NAM)", "Trần Ngọc Anh (Giám đốc)", "0918001561", "Tầng 3, Tòa nhà Samco, 326 Võ Văn Kiệt, Cô Giang, Quận 1", "Mạng lưới phân phối siêu thị dự án BĐS", "Đại lý F1 phân phối", "0101160306")
    ]
    
    # Dữ liệu Sàn tại Đồng Nai
    agencies_dongnai = [
        ("Đồng Nai", "TP. Biên Hòa / Trụ sở chính", "CÔNG TY CỔ PHẦN TẬP ĐOÀN ĐỊA ỐC KIM OANH (KIM OANH GROUP)", "Đặng Thị Kim Oanh (Chủ tịch)", "0938668899", "Số 268A Phan Trung, P. Tân Mai, TP. Biên Hòa, Đồng Nai", "Hệ thống sàn lớn nhất Đông Nam Bộ, hàng ngàn sales", "Hợp tác phân phối chiến lược liên minh", "3700714798"),
        ("Đồng Nai", "Long Thành / Sân Bay", "CÔNG TY TNHH BẤT ĐỘNG SẢN LONG THÀNH LAND", "Nguyễn Văn Tuấn (Giám đốc)", "0987852854", "Số 45 Lê Duẩn, Thị trấn Long Thành, Huyện Long Thành, Đồng Nai", "Thổ địa đón sóng Sân bay Long Thành & Cao tốc", "Đại lý F2 khai thác khách đầu tư Long Thành", "3603412345"),
        ("Đồng Nai", "TP. Biên Hòa", "CÔNG TY CỔ PHẦN ĐẦU TƯ ĐỊA ỐC LONG PHÁT", "Trần Long Phát (TGĐ)", "0909778899", "Số 3/1 QL51, Khu phố 1, P. Long Bình Tân, Biên Hòa, Đồng Nai", "Chuyên phân phối đất nền, Second home ven đô", "Đại lý liên kết bán hàng F1", "3603512890"),
        ("Đồng Nai", "Trảng Bom / Thống Nhất", "CÔNG TY CỔ PHẦN ĐẦU TƯ ĐẠI AN LỘC", "Phạm Văn Lộc (Giám đốc)", "0934079345", "QL1A, Xã Bình Minh, Huyện Trảng Bom, Đồng Nai", "Tệp khách công nghiệp, chủ xưởng Đồng Nai có tiền mặt", "Đại lý F2 giới thiệu nhà đầu tư", "3603619988"),
        ("Đồng Nai", "Nhơn Trạch / Cát Lái", "CÔNG TY TNHH TƯ VẤN BẤT ĐỘNG SẢN ĐÔNG SÀI GÒN", "Lê Văn Hùng (Giám đốc)", "0937009777", "Đường Lý Thái Tổ, Xã Đại Phước, Huyện Nhơn Trạch, Đồng Nai", "Đón sóng cầu Cát Lái và kết nối Vũng Tàu", "Đại lý liên kết phân phối", "3603487123")
    ]
    
    # Đọc danh sách sàn BR-VT từ file đã cào trước đó
    bds_file = 'data/tep_doi_tac_san_moi_gioi_bds_brvt.csv'
    agencies_brvt = []
    if os.path.exists(bds_file):
        with open(bds_file, 'r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            for r in reader:
                agencies_brvt.append((
                    "Bà Rịa - Vũng Tàu",
                    r.get('khu_vuc', 'BR-VT'),
                    r.get('ten_cong_ty', ''),
                    r.get('nguoi_dai_dien', 'Chưa cập nhật'),
                    r.get('so_dien_thoai', ''),
                    r.get('dia_chi', ''),
                    "Sàn giao dịch thổ địa & Môi giới địa phương",
                    r.get('muc_tieu_hop_tac', 'Ký Hợp đồng Đại lý F1/F2'),
                    r.get('mst', '')
                ))

    all_agencies = agencies_hcm + agencies_dongnai + agencies_brvt
    
    for row_idx, item in enumerate(all_agencies, start=2):
        ws1.append([
            row_idx - 1, item[0], item[1], item[2], item[3], 
            item[4], item[5], item[6], item[7], item[8]
        ])
        
    # Định dạng Sheet 1
    for col_num in range(1, len(headers1) + 1):
        cell = ws1.cell(row=1, column=col_num)
        cell.font = font_header
        cell.fill = fill_header_navy
        cell.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
    
    for r in range(2, ws1.max_row + 1):
        is_even = (r % 2 == 0)
        for c in range(1, len(headers1) + 1):
            cell = ws1.cell(row=r, column=c)
            cell.border = border_thin
            cell.font = font_regular
            if is_even:
                cell.fill = fill_zebra
            # Highlight số điện thoại
            if c == 6:
                cell.font = font_bold
                cell.alignment = Alignment(horizontal='center', vertical='center')
            elif c in [1, 2, 3]:
                cell.alignment = Alignment(horizontal='center', vertical='center')
            else:
                cell.alignment = Alignment(vertical='center')

    # =========================================================================
    # SHEET 2: SALES CHIẾN BINH & CONTENT CREATORS (YOUTUBE, TIKTOK, FACEBOOK)
    # =========================================================================
    ws2 = wb.create_sheet(title="Sales_KOL_Reviewers_BRVT_DN")
    ws2.views.sheetView[0].showGridLines = True
    
    headers2 = [
        "STT", "Tên Kênh / Môi Giới", "Nền Tảng Hoạt Động", "Người Phụ Trách / Reviewer",
        "Hotline / Zalo Liên Hệ", "Khu Vực Địa Bàn Trọng Điểm", "Loại Nội Dung / Định Dạng Clip",
        "Số Lượng Đăng / Tương Tác", "Mục Tiêu Hợp Tác Bán Hàng", "Ghi Chú Đánh Giá Tiềm Năng"
    ]
    ws2.append(headers2)
    
    creators = [
        ("Đất Bà Rịa - Vũng Tàu (@nhadatvungtautphcm)", "YouTube / Facebook", "Ban Quản Trị Kênh", "0933230243", "Đất Đỏ, Châu Đức, Xuyên Mộc, Vũng Tàu", "Video tour thực tế, quay Flycam toàn cảnh, phân tích quy hoạch", "Hơn 21.000 Subscribers, hàng chục nghìn view/clip", "Booking làm video tour trải nghiệm Hồ Lồ Ồ + Nhận F2 bán hàng", "Kênh YouTube số 1 thị trường BR-VT, tương tác rất thật từ nhà đầu tư TP.HCM"),
        ("Bảo Điền BĐS", "YouTube / TikTok / Zalo", "Bảo Điền", "0788668834", "Hồ Tràm, Phước Thuận, Xuyên Mộc, Đất Đỏ", "Review đất vườn, đất ven biển Hồ Tràm, săn đất ngộp tài chính", "Kênh review chuyên sâu Hồ Tràm", "Booking quay clip review Hồ Lồ Ồ (cách Hồ Tràm 15p) + Ký gửi rổ hàng", "Rất am hiểu tâm lý khách mua đất biển Hồ Tràm, phong cách nói chuyện thực tế"),
        ("Phạm Hữu Dư BĐS (Nhà Vườn Miền Nam)", "YouTube / Facebook", "Phạm Hữu Dư", "0933230243", "Hồ Tràm, Đất Đỏ, Bà Rịa - Vũng Tàu", "Chuyên mô hình nhà vườn sinh thái, farmstay, diện tích lớn", "Chuỗi video review nhà vườn view đẹp", "Ký gửi phân phối dòng Điền Trang & Biệt Phủ ven hồ 100ha", "Tệp người theo dõi 100% tìm kiếm mô hình Farmstay và Second home sinh thái"),
        ("Review Nhà Đất Vũng Tàu", "YouTube / TikTok", "Admin Review", "0939793389", "TP. Vũng Tàu, Long Hải, Phước Hải, Đất Đỏ", "Review thực tế nhà phố, biệt thự nghỉ dưỡng ven biển, đất thổ cư", "Kênh uy tín tại Vũng Tàu", "Mời tham gia F2 phân phối dòng Biệt Phủ VIP cho khách VIP Vũng Tàu", "Khách theo dõi là dân bản địa Vũng Tàu và nhà đầu tư Sài Gòn có tiền mặt lớn"),
        ("Bất Động Sản Vũng Tàu", "YouTube / Facebook", "Minh Hoàng", "0978384438", "TP. Vũng Tàu, Côn Đảo, Đất Đỏ", "Cập nhật tiến độ dự án, hạ tầng giao thông, đất nền ven biển", "Độ phủ cao trên mạng xã hội", "Hợp tác phân phối F2 + Quảng cáo bài đăng trên kênh", "Thế mạnh về phân tích pháp lý và quy hoạch hạ tầng BR-VT"),
        ("Nhất BĐS Bà Rịa Vũng Tàu (@nhatreviewbds)", "YouTube / TikTok", "Trần Văn Nhất", "0909889678", "Phước Hải, Lộc An, Đất Đỏ, Long Điền", "Clip ngắn TikTok, Shorts review biệt thự mini, nhà vườn ngộp, đất thổ cư", "Trending TikTok #nhadatdatdo, #bdsphuochai", "Booking quay video TikTok viral giới thiệu Làng Ngựa & Hồ Lồ Ồ", "Kênh TikTok bắt trend nhanh, tiếp cận đối tượng nhà đầu tư trẻ tuổi và năng động"),
        ("Đất Bà Rịa - Vũng Tàu Duy Nghĩa", "YouTube / Facebook", "Duy Nghĩa", "0919890979", "Huyện Đất Đỏ, Phước Hải, Châu Đức", "Video cận cảnh đất vườn, hồ bơi sân vườn, khảo sát giá thực tế", "Kênh chuyên đất sào, đất vườn", "Ký gửi độc quyền các lô Điền Sản đợt 1", "Chuyên trị tệp khách TP.HCM thích làm nông trại và nhà vườn cuối tuần"),
        ("Hiển Land Bà Rịa Vũng Tàu", "YouTube / TikTok", "Nguyễn Văn Hiển", "0987557575", "Trung tâm Đất Đỏ, KCN Đất Đỏ 1, Phước Long Thọ", "Review đất mặt tiền đường nhựa, đất sát KCN, đất công chứng ngay", "Nhiều clip ngắn thực tế tại Đất Đỏ", "Đại lý bán hàng dòng Điền An (cụm lưu trú chuyên gia KCN Đất Đỏ)", "Đang trực tiếp bám sát địa bàn Huyện Đất Đỏ, nguồn khách tại chỗ dồi dào"),
        ("Thế Tùng BĐS", "YouTube / TikTok / Zalo", "Thế Tùng", "0566688868", "Long Thành, Sân bay Quốc tế Long Thành, Đồng Nai", "Phân tích vĩ mô, tiến độ thi công sân bay Long Thành và cao tốc", "Kênh YouTube phân tích hạ tầng top đầu", "Mời làm clip phân tích liên kết Cao tốc Biên Hòa - Vũng Tàu về Hồ Lồ Ồ", "Khách hàng của kênh là các nhà đầu tư lớn đang gom đất đón sóng sân bay"),
        ("Team Rùa Review (@CungRuaxemdat)", "YouTube / TikTok", "Team Rùa BĐS", "0936666831", "Long Thành, Nhơn Trạch, Biên Hòa, BR-VT", "Flycam chuyên nghiệp 4K, trải nghiệm cung đường thực tế", "Kênh review hình ảnh cực đẹp, nhiều view", "Thuê ekip bay flycam quay toàn cảnh hồ 100ha + Đăng bài review độc quyền", "Chất lượng hình ảnh và âm thanh review thuộc hàng chuyên nghiệp nhất hiện nay"),
        ("Hằng BĐS (Nhà Đất Miền Nam)", "YouTube / Facebook", "Thu Hằng", "0931328613", "Đồng Nai, Bà Rịa - Vũng Tàu, Bình Dương", "Review nhà vườn nghỉ dưỡng, đất nông nghiệp quy hoạch sinh thái", "Kênh phong cách nhẹ nhàng, dễ mến", "Booking làm phóng sự trải nghiệm 1 ngày làm điền chủ tại Saigon Farm Resort", "Rất hợp gu khách hàng nữ, khách gia đình trung niên có tiền tiết kiệm"),
        ("Nguyễn Tâm - Nhà Đất Đồng Nai", "YouTube / TikTok", "Nguyễn Tâm", "0355210780", "Trảng Bom, Long Thành, Cẩm Mỹ", "Review đất sào, đất vườn cây ăn trái, trang trại sinh thái", "Kênh ký gửi uy tín tại Đồng Nai", "Khai thác tệp khách hàng mua trang trại tại Đồng Nai chuyển hướng về Đất Đỏ", "Lượng data khách hàng có sẵn lớn tại khu vực Biên Hòa và TP.HCM"),
        ("Địa Ốc Tuấn Anh", "YouTube / Zalo", "Tuấn Anh", "0987852854", "Nhơn Trạch, Long Thành, Mỹ Xuân - Ngãi Giao", "Cập nhật tiến độ mở rộng ĐT994, Cao tốc Biên Hòa - Vũng Tàu", "Kênh chuyên thông tin hạ tầng", "Booking bài viết và video phân tích đòn bẩy hạ tầng của dự án", "Khán giả tin tưởng vào góc nhìn hạ tầng và phân tích số liệu quy hoạch"),
        ("Phạm Nghệ Bất Động Sản", "YouTube", "Phạm Nghệ", "0901207788", "Cung đường biển Hồ Tràm - Bình Châu - Xuyên Mộc", "Clip đường phố, khảo sát mặt tiền ven biển, giá đất thực tế", "Kênh thực tế đời sống BĐS", "Booking quay video trải nghiệm thực tế từ Hồ Tràm rẽ vào Hồ Lồ Ồ", "Tạo cảm giác chân thực, khách hàng xem video thấy rõ vị trí kề cận Hồ Tràm"),
        ("Hồ Tràm Land Review", "TikTok / Facebook Reels", "Hoàng Nam", "0945555999", "Hồ Tràm, Lộc An, Hồ Lồ Ồ, Bình Châu", "Video ngắn 60s, âm nhạc bắt tai, hình ảnh flycam biển và hồ", "Kênh viral trên TikTok về du lịch & BĐS", "Booking chiến dịch video ngắn viral TikTok trước ngày mở bán", "Thu hút sự tò mò của giới trẻ và các nhà đầu tư sành điệu")
    ]
    
    for row_idx, item in enumerate(creators, start=2):
        ws2.append([
            row_idx - 1, item[0], item[1], item[2], item[3], 
            item[4], item[5], item[6], item[7], item[8]
        ])
        
    for col_num in range(1, len(headers2) + 1):
        cell = ws2.cell(row=1, column=col_num)
        cell.font = font_header
        cell.fill = fill_header_teal
        cell.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
        
    for r in range(2, ws2.max_row + 1):
        is_even = (r % 2 == 0)
        for c in range(1, len(headers2) + 1):
            cell = ws2.cell(row=r, column=c)
            cell.border = border_thin
            cell.font = font_regular
            if is_even:
                cell.fill = fill_zebra
            if c == 5:
                cell.font = font_bold
                cell.alignment = Alignment(horizontal='center', vertical='center')
            elif c in [1, 3]:
                cell.alignment = Alignment(horizontal='center', vertical='center')
            else:
                cell.alignment = Alignment(vertical='center')

    # =========================================================================
    # SHEET 3: KỊCH BẢN TIẾP CẬN & CHÍNH SÁCH HOA HỒNG
    # =========================================================================
    ws3 = wb.create_sheet(title="Kich_Ban_Tuyen_Dai_Ly_KOL")
    ws3.views.sheetView[0].showGridLines = True
    
    headers3 = ["STT", "Hạng Mục / Kênh Tiếp Cận", "Mục Tiêu & Cơ Chế Hợp Tác", "Mức Hoa Hồng / Phí Đề Xuất", "Kịch Bản Mẫu Tiếp Cận Trực Tiếp"]
    ws3.append(headers3)
    
    scripts = [
        (
            "1", "ĐẠI LÝ F1 PHÂN PHỐI ĐỘC QUYỀN RỔ HÀNG (SÀN LỚN TPHCM / ĐỒNG NAI)", 
            "Ký kết Hợp đồng Phân phối độc quyền giỏ hàng (từ 5 - 10 nền). CĐT hỗ trợ chi phí truyền thông, tài liệu Sales Kit, xe đưa đón khách VIP từ TP.HCM xuống Hồ Lồ Ồ.",
            "Hoa hồng từ 4.0% - 5.5% / giá trị sản phẩm + Thưởng nóng 50 - 100 triệu/giao dịch thành công trong tháng mở bán.",
            "Dạ em chào Anh/Chị [Tên TGĐ/Giám đốc Sàn]. Em là [Tên] từ Đơn vị Phát triển Quần thể Saigon Farm Resort (Hồ Lồ Ồ, Đất Đỏ). Bên em vừa mở bán Đợt 1 (36 sản phẩm) với pháp lý độc tôn: 100% SỔ ĐỎ RIÊNG TỪNG NỀN, THỔ CƯ ĐẦY ĐỦ, CÔNG CHỨNG SANG TÊN TRONG 10 - 20 NGÀY. Đặc biệt chính sách 50/50 giãn 12 tháng 0% lãi suất đang cực kỳ hút khách. Em xin phép mời Anh/Chị và Ban Giám đốc tuần này dùng bữa trưa thân mật cùng Chủ đầu tư để trao đổi chính sách Đại lý F1 độc quyền rổ hàng nhé ạ!"
        ),
        (
            "2", "SÀN F2 LIÊN KẾT / SÀN MÔI GIỚI BẢN ĐỊA (BR-VT / LONG THÀNH)", 
            "Liên kết bán chéo rổ hàng, không áp lực chỉ tiêu doanh số. Cung cấp đầy đủ pháp lý, bản đồ trích lục quy hoạch, định vị thực tế và hỗ trợ sale dẫn khách tại khuôn viên dự án.",
            "Hoa hồng từ 3.0% - 3.5% / giá trị sản phẩm + Thưởng nóng 30 triệu đồng/giao dịch ngay khi khách ký cọc.",
            "Chào bạn, mình bên Ban Quản lý Quần thể Saigon Farm Resort ngay Hồ Lồ Ồ, Đất Đỏ. Hiện bên mình đang có rổ hàng Điền Sản F0 giá gốc chỉ 10,6 tr/m², khách chỉ cần nộp 5,3 tỷ là ký công chứng chuyển nhượng quyền sử dụng đất ngay. Bên mình trích hoa hồng liên kết 3% + thưởng nóng 30 triệu/giao dịch giải ngân ngay trong 48h. Bạn nhắn số Zalo để mình gửi trọn bộ tài liệu, sổ đỏ từng nền và bảng giá nhé!"
        ),
        (
            "3", "BOOKING CONTENT CREATORS (YOUTUBER / TIKTOKER REVIEW BĐS)", 
            "Mời Reviewer xuống trực tiếp khuôn viên Hồ Lồ Ồ 100ha trải nghiệm chèo thuyền kayak, tham quan Làng Ngựa Việt Mã Viên, dùng tiệc trà thảo mộc và quay clip review thực tế.",
            "Chi phí sản xuất video: 5 - 15 triệu/clip (tùy kênh) HOẶC Cơ chế cộng tác: Miễn phí quay + Nhận hoa hồng môi giới 2.5% - 3% khi có khách phát sinh từ clip.",
            "Chào [Tên Reviewer], mình theo dõi các video review đất nghỉ dưỡng của kênh bạn rất ấn tượng và chuyên nghiệp. Bên mình đang hoàn thiện Quần thể Điền trang Ven Hồ Saigon Farm Resort 100ha tại Đất Đỏ (sát vách Hồ Tràm 15p). Bên mình muốn mời ekip của bạn cuối tuần này ghé thăm, trải nghiệm chèo kayak, cưỡi ngựa và quay 1 video flycam review toàn cảnh thực tế khuôn viên. Bên mình sẽ gửi chi phí sản xuất video hợp tác cùng bạn. Bạn cho mình xin số Zalo để trao đổi chi tiết nhé!"
        )
    ]
    
    for item in scripts:
        ws3.append(list(item))
        
    for col_num in range(1, len(headers3) + 1):
        cell = ws3.cell(row=1, column=col_num)
        cell.font = font_header
        cell.fill = fill_header_purple
        cell.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
        
    for r in range(2, ws3.max_row + 1):
        for c in range(1, len(headers3) + 1):
            cell = ws3.cell(row=r, column=c)
            cell.border = border_thin
            cell.font = font_regular
            cell.alignment = Alignment(vertical='top', wrap_text=True)
            if c == 1:
                cell.alignment = Alignment(horizontal='center', vertical='top')
                cell.font = font_bold
            elif c in [2, 4]:
                cell.font = font_bold

    # =========================================================================
    # CÂN CHỈNH ĐỘ RỘNG CỘT TỰ ĐỘNG
    # =========================================================================
    for sheet in [ws1, ws2, ws3]:
        for col in sheet.columns:
            max_len = 0
            col_letter = get_column_letter(col[0].column)
            for cell in col:
                val = str(cell.value or '')
                # Nếu là dòng dài, giới hạn độ rộng hợp lý
                if len(val) > max_len:
                    max_len = len(val)
            sheet.column_dimensions[col_letter].width = min(max(max_len + 3, 12), 48)
            
    # Lưu file Excel
    out_xlsx = 'data/DANH_SACH_DAI_LY_SALES_KOL_BDS_TPHCM_VT_DN.xlsx'
    wb.save(out_xlsx)
    print(f"XUẤT THÀNH CÔNG FILE EXCEL ĐA SHEET: {out_xlsx}")
    
    # Đồng thời xuất 2 file CSV UTF-8-sig để import CRM
    csv_agencies = 'data/danh_sach_dai_ly_bds_tphcm_vt_dn.csv'
    with open(csv_agencies, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers1)
        for row in all_agencies:
            writer.writerow([""] + list(row))
            
    csv_creators = 'data/danh_sach_sales_kol_youtube_tiktok_bds.csv'
    with open(csv_creators, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers2)
        for row in creators:
            writer.writerow([""] + list(row))
            
    print(f"Xuất file CSV 1: {csv_agencies}")
    print(f"Xuất file CSV 2: {csv_creators}")

if __name__ == '__main__':
    build_excel()
