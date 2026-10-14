#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Update data/listing_categories.json from the latest Excel price list:
listing/20261013_SFR_PA GIÁ_ có nhà_V3.xlsx
"""

import json
import datetime
import openpyxl

EXCEL_PATH = "listing/20261013_SFR_PA GIÁ_ có nhà_V3.xlsx"
JSON_PATH = "data/listing_categories.json"

LOT_COORDINATES = {
    'A04': (54.75, 42.00),
    'A06': (53.86, 49.97),
    'A08': (49.61, 48.26),
    'A09': (47.39, 46.97),
    'A11': (42.79, 44.83),
    'A12': (40.52, 43.75),
    'A13': (38.55, 42.62),
    'A14': (36.31, 41.44),
    'A15': (34.11, 40.46),
    'A16': (52.60, 56.83),
    'A17': (50.40, 55.70),
    'A18': (48.34, 54.84),
    'A19': (46.49, 53.97),
    'A20': (44.60, 53.36),
    'A21': (42.49, 52.45),
    'A22': (40.10, 50.34),
    'A23': (37.44, 48.40),
    'A24': (51.32, 60.32),
    'B04': (60.93, 39.50),
    'B05': (58.90, 44.44),
    'B06': (59.00, 47.66),
    'B07': (57.02, 51.34),
    'B08': (58.41, 52.40),
    'B09': (60.78, 53.39),
    'B10': (63.31, 55.15),
    'B12': (57.41, 58.77),
    'B13': (59.22, 59.19),
    'B14': (56.56, 61.65),
    'B15': (54.54, 64.59),
    'B17': (63.03, 59.52),
    'B18': (62.82, 62.59),
    'B19': (62.35, 64.91),
    'B20': (62.13, 67.24),
    'B22': (59.75, 74.23),
    'B23': (62.33, 75.49),
    'B24': (64.91, 76.48)
}

def format_vnd_str(val):
    if val is None: return ""
    return f"{int(round(val)):,} đ".replace(',', '.')

def format_billion_str(val):
    if val is None: return ""
    b = val / 1_000_000_000
    return f"{b:.2f}".replace('.', ',') + " Tỷ"

def format_unit_million_str(val):
    if val is None: return ""
    m = val / 1_000_000
    return f"{m:.2f}".replace('.', ',') + " Tr/m²"

def format_unit_str(val):
    if val is None: return ""
    return f"{int(round(val)):,} đ/m²".replace(',', '.')

def main():
    wb = openpyxl.load_workbook(EXCEL_PATH, data_only=True)
    ws = wb['Bảng giá đất Farm Resort']

    # Read existing JSON
    with open(JSON_PATH, 'r', encoding='utf-8') as f:
        categories = json.load(f)

    existing_items_map = {}
    for cat in categories:
        for item in cat.get('items', []):
            existing_items_map[item['code']] = item

    # Category items containers
    cat_items = {
        'biet-phu-dien-trang': [],
        'dien-san': [],
        'dien-an': []
    }

    for r in range(6, ws.max_row + 1):
        stt = ws.cell(r, 1).value
        if stt is None: continue
        block = str(ws.cell(r, 2).value or '').strip()
        num_val = ws.cell(r, 3).value
        code_raw = str(ws.cell(r, 4).value or '').strip()
        code_norm = code_raw.replace('.', '')
        letter = code_norm[0].upper()
        num = int(code_norm[1:])
        code = f"{letter}{num:02d}"

        so_gcn = str(ws.cell(r, 5).value or '').strip()
        so_thua = ws.cell(r, 6).value
        so_to = ws.cell(r, 7).value
        so_vao_so = str(ws.cell(r, 8).value or '').strip()
        ngay_cap_val = ws.cell(r, 9).value
        ngay_cap = ngay_cap_val.strftime('%d/%m/%Y') if isinstance(ngay_cap_val, (datetime.date, datetime.datetime)) else str(ngay_cap_val or '')

        dt_so = float(ws.cell(r, 10).value or 0)
        dt_gt = float(ws.cell(r, 11).value or 0)
        dt_ban = float(ws.cell(r, 12).value or 0)
        dt_o = float(ws.cell(r, 13).value or 0)

        pos_raw = str(ws.cell(r, 14).value or '').strip()
        # Normalize position string for UI filter
        if 'góc' in pos_raw.lower():
            pos = 'Lô góc'
        elif 'mặt tiền' in pos_raw.lower() or '2 mt' in pos_raw.lower():
            pos = '2 MT'
        else:
            pos = 'Lô thường'

        view_raw = str(ws.cell(r, 15).value or '').strip()
        view = 'Lúa' if 'lúa' in view_raw.lower() else 'Garden'

        road_raw = str(ws.cell(r, 16).value or '').strip()
        road = 'Đường trục chính' if 'trục' in road_raw.lower() else 'Đường nội bộ'

        direction = str(ws.cell(r, 17).value or '').strip()
        loai_sp = str(ws.cell(r, 18).value or '').strip()

        # Slug classification
        if 'biệt phủ' in loai_sp.lower():
            cat_slug = 'biet-phu-dien-trang'
            cat_title = 'Biệt Phủ Điền Trang'
        elif 'điền sản' in loai_sp.lower():
            cat_slug = 'dien-san'
            cat_title = 'Điền Sản'
        else:
            cat_slug = 'dien-an'
            cat_title = 'Điền An'

        dg_dat = ws.cell(r, 19).value
        tt_dat = ws.cell(r, 20).value
        dg_nha_novat = ws.cell(r, 21).value
        tt_nha_novat = ws.cell(r, 22).value
        dg_nha_vat = ws.cell(r, 23).value
        tt_nha_vat = ws.cell(r, 24).value
        quy_sp = str(ws.cell(r, 25).value or 'GĐ1').strip()

        # CSBH
        csbh_dg_dat_std = ws.cell(r, 27).value
        csbh_tt_dat_std = ws.cell(r, 28).value
        csbh_dg_nha_novat_std = ws.cell(r, 29).value
        csbh_tt_nha_novat_std = ws.cell(r, 30).value
        csbh_dg_nha_vat_std = ws.cell(r, 31).value
        csbh_tt_nha_vat_std = ws.cell(r, 32).value

        # Existing metadata preservation
        old_it = existing_items_map.get(code, {})

        area_val = round(dt_ban, 2)
        area_str = f"{area_val:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')

        # Handle Phase 2 (GĐ2)
        if quy_sp == 'GĐ2' or tt_dat is None:
            unit_price = 0
            unit_price_str = "Chưa mở bán"
            unit_price_million = "Chưa công bố"
            price = 0
            price_str = "Dự kiến mở bán Giai đoạn 2"
            price_billion = "Quỹ GĐ2"
            status = "Quỹ Giai Đoạn 2"
            status_type = "reserved"
            land_price = None
            land_price_str = None
            land_price_billion = None
            land_unit_price = None
            land_unit_price_str = None
            land_unit_price_million = None
            house_price_novat = None
            house_price_novat_str = None
            house_price_novat_billion = None
            house_price_vat = None
            house_price_vat_str = None
            house_price_vat_billion = None
        else:
            unit_price = int(round(dg_dat))
            unit_price_str = format_unit_str(dg_dat)
            unit_price_million = format_unit_million_str(dg_dat)

            price = int(round(tt_dat))
            price_str = format_vnd_str(tt_dat)
            price_billion = format_billion_str(tt_dat)

            status = old_it.get('status', 'Còn hàng')
            status_type = old_it.get('status_type', 'available')

            land_price = price
            land_price_str = price_str
            land_price_billion = price_billion
            land_unit_price = unit_price
            land_unit_price_str = unit_price_str
            land_unit_price_million = unit_price_million

            if tt_nha_novat:
                house_price_novat = int(round(tt_nha_novat))
                house_price_novat_str = format_vnd_str(tt_nha_novat)
                house_price_novat_billion = format_billion_str(tt_nha_novat)
                house_unit_price_novat = int(round(dg_nha_novat)) if dg_nha_novat else None
                house_unit_price_novat_million = format_unit_million_str(dg_nha_novat) if dg_nha_novat else None
            else:
                house_price_novat = None
                house_price_novat_str = None
                house_price_novat_billion = None
                house_unit_price_novat = None
                house_unit_price_novat_million = None

            if tt_nha_vat:
                house_price_vat = int(round(tt_nha_vat))
                house_price_vat_str = format_vnd_str(tt_nha_vat)
                house_price_vat_billion = format_billion_str(tt_nha_vat)
                house_unit_price_vat = int(round(dg_nha_vat)) if dg_nha_vat else None
                house_unit_price_vat_million = format_unit_million_str(dg_nha_vat) if dg_nha_vat else None
            else:
                house_price_vat = None
                house_price_vat_str = None
                house_price_vat_billion = None
                house_unit_price_vat = None
                house_unit_price_vat_million = None

        # Build feature descriptions
        if code == 'A19':
            features = "TẦM NHÌN TRỰC DIỆN ĐỒNG LÚA THANH BÌNH. Hướng Đông Bắc đón gió sinh thái mát mẻ quanh năm, không gian tĩnh lặng tuyệt đối bên thềm đồng lúa."
            suitable_for = "Gia chủ tìm kiếm tư dinh dưỡng sinh, tái tạo năng lượng với không gian mở khoáng đạt và dịch vụ MDS Living chuẩn 5 sao."
            amenity = "Bình thường"
            image = "assets/Index_asset/villa_gallery/sunset_2_ext_2.jpg"
        elif code == 'A20':
            features = "KHUÔN VIÊN GẦN 950 M² VIEW ĐỒNG LÚA. Thế đất vuông vức bề thế, hướng Đông Bắc đón gió lành, liền kề dải cảnh quan sinh thái và trục nội bộ yên tĩnh."
            suitable_for = "Gia đình đa thế hệ ưu tiên không gian sống biệt lập, diện tích lớn để thiết kế cảnh quan vườn và hồ bơi khoáng muối riêng biệt."
            amenity = "Bình thường"
            image = "assets/Index_asset/villa_gallery/sunrise_1_ext_3.jpg"
        else:
            features = old_it.get('features', '')
            suitable_for = old_it.get('suitable_for', '')
            amenity = old_it.get('amenity', 'Bình thường')
            image = old_it.get('image', 'assets/Index_asset/Phoicanh_3D_Tien_ich/Tong_the/S01_Final_Fix.jpg')

        map_x, map_y = LOT_COORDINATES.get(code, (50.0, 50.0))

        item_dict = {
            "stt": int(stt),
            "block": block,
            "code": code,
            "area": area_str,
            "area_val": area_val,
            "position": pos,
            "raw_position": pos_raw,
            "view": view,
            "amenity": amenity,
            "road": road,
            "direction": direction,
            "unit_price": unit_price,
            "unit_price_str": unit_price_str,
            "unit_price_million": unit_price_million,
            "price": price,
            "price_str": price_str,
            "price_billion": price_billion,
            "price_label": "Giá Niêm Yết Gốc (Original Price Listing - Trước CSBH)",
            "land_price": land_price,
            "land_price_str": land_price_str,
            "land_price_billion": land_price_billion,
            "land_unit_price": land_unit_price,
            "land_unit_price_str": land_unit_price_str,
            "land_unit_price_million": land_unit_price_million,
            "house_price_novat": house_price_novat,
            "house_price_novat_str": house_price_novat_str,
            "house_price_novat_billion": house_price_novat_billion,
            "house_price_vat": house_price_vat,
            "house_price_vat_str": house_price_vat_str,
            "house_price_vat_billion": house_price_vat_billion,
            "phase": quy_sp,
            "so_gcn": so_gcn,
            "so_thua": so_thua,
            "so_to": so_to,
            "so_vao_so": so_vao_so,
            "ngay_cap": ngay_cap,
            "dt_so": dt_so,
            "dt_gt": dt_gt,
            "dt_o": dt_o,
            "features": features,
            "suitable_for": suitable_for,
            "status": status,
            "status_type": status_type,
            "image": image,
            "category_slug": cat_slug,
            "category_title": cat_title,
            "map_x": map_x,
            "map_y": map_y
        }

        cat_items[cat_slug].append(item_dict)

    # Reassemble categories preserving metadata
    new_categories = []
    for cat in categories:
        slug = cat['slug']
        c_copy = dict(cat)
        c_copy['items'] = cat_items.get(slug, [])
        new_categories.append(c_copy)

    with open(JSON_PATH, 'w', encoding='utf-8') as f:
        json.dump(new_categories, f, ensure_ascii=False, indent=2)

    print(f"✅ Successfully updated {JSON_PATH} with 36 verified lots!")
    for c in new_categories:
        print(f"  - {c['title']}: {len(c['items'])} items")

if __name__ == "__main__":
    main()
