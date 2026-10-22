#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cào dữ liệu doanh nghiệp đa dạng ngành nghề tại Bà Rịa - Vũng Tàu & Hồ Tràm
Lấy Tên công ty, Đại diện, SĐT di động (09, 08, 07, 03), Địa chỉ, Ngành nghề, MST
"""

import urllib.request
import re
import time
import os
import csv
import random

DISTRICT_MAPPING = [
    ('Hồ Tràm / Xuyên Mộc', 'huyen-xuyen-moc-255', 4),
    ('Đất Đỏ', 'huyen-dat-do-55', 4),
    ('TP. Vũng Tàu', 'thanh-pho-vung-tau-38', 4),
    ('TX. Phú Mỹ (Cảng & KCN)', 'thi-xa-phu-my-33', 3),
    ('TP. Bà Rịa', 'thanh-pho-ba-ria-52', 3),
    ('Long Điền / Long Hải', 'huyen-long-dien-453', 3)
]

def classify_industry(name):
    n = name.upper()
    if any(k in n for k in ['RESORT', 'HOTEL', 'KHÁCH SẠN', 'DU LỊCH', 'HOMESTAY', 'LODGE', 'TOUR', 'LỮ HÀNH', 'NGHỈ DƯỠNG']):
        return 'Du lịch, Khách sạn & Nghỉ dưỡng'
    if any(k in n for k in ['BẤT ĐỘNG SẢN', 'ĐỊA ỐC', 'LAND', 'REALTY', 'HOMES', 'ESTATE', 'NHÀ ĐẤT', 'BĐS']):
        return 'Bất động sản & Phát triển Dự án'
    if any(k in n for k in ['XÂY DỰNG', 'CONSTRUCTION', 'KIẾN TRÚC', 'NỘI THẤT', 'XÂY LẮP', 'THIẾT KẾ', 'CƠ ĐIỆN', 'BÊ TÔNG', 'VẬT LIỆU']):
        return 'Xây dựng, Kiến trúc & Vật liệu'
    if any(k in n for k in ['THỦY SẢN', 'HẢI SẢN', 'SEAFOOD', 'FISH', 'TÔM', 'CÁ', 'CÁ LƯỚI', 'CHẾ BIẾN THỦY SẢN']):
        return 'Thủy hải sản & Khai thác biển'
    if any(k in n for k in ['DẦU KHÍ', 'HÀNG HẢI', 'TÀU', 'CẢNG', 'PETRO', 'GAS', 'MARITIME', 'SHIP', 'HÓA CHẤT']):
        return 'Dầu khí, Cảng biển & Hàng hải'
    if any(k in n for k in ['LOGISTICS', 'VẬN TẢI', 'GIAO NHẬN', 'KHO BÃI', 'TRANSPORT', 'EXPRESS', 'XE KHÁCH']):
        return 'Vận tải & Logistics'
    if any(k in n for k in ['CÔNG NGHIỆP', 'SẢN XUẤT', 'CƠ KHÍ', 'CHẾ TẠO', 'THÉP', 'KIM LOẠI', 'NHỰA', 'FORGING', 'VALVE', 'TECHNOLOGIES', 'FABRICATION']):
        return 'Sản xuất công nghiệp & Cơ khí'
    if any(k in n for k in ['NÔNG NGHIỆP', 'FARM', 'NÔNG TRẠI', 'CHĂN NUÔI', 'CÂY KIỂNG', 'SINH HỌC', 'THẢO DƯỢC', 'THỰC PHẨM']):
        return 'Nông nghiệp, Nông trại & Thực phẩm sạch'
    if any(k in n for k in ['CÔNG NGHỆ', 'PHẦN MỀM', 'DIGI', 'TECH', 'MEDIA', 'TRUYỀN THÔNG', 'QUẢNG CÁO', 'GIẢI TRÍ', 'GAME']):
        return 'Công nghệ thông tin & Truyền thông'
    if any(k in n for k in ['ĐẦU TƯ', 'TÀI CHÍNH', 'HOLDINGS', 'GROUP', 'TƯ VẤN', 'QUẢN LÝ']):
        return 'Đầu tư & Quản lý doanh nghiệp'
    if any(k in n for k in ['F&B', 'ẨM THỰC', 'NHÀ HÀNG', 'QUÁN ĂN', 'CATERING', 'BEER', 'COFFEE', 'CÀ PHÊ']):
        return 'Nhà hàng, F&B & Dịch vụ ăn uống'
    if any(k in n for k in ['Y TẾ', 'DƯỢC', 'NHA KHOA', 'PHÒNG KHÁM', 'THẨM MỸ', 'SPA', 'WELLNESS']):
        return 'Y tế, Dược phẩm & Chăm sóc sức khỏe'
    if any(k in n for k in ['THƯƠNG MẠI', 'XUẤT NHẬP KHẨU', 'PHÂN PHỐI', 'TM DV', 'DỊCH VỤ', 'TRADING']):
        return 'Thương mại, Xuất nhập khẩu & Dịch vụ'
    return 'Thương mại & Dịch vụ tổng hợp'

def suggest_product(industry, name):
    ind = industry.lower()
    nm = name.lower()
    if 'khách sạn' in ind or 'nghỉ dưỡng' in ind or 'sản xuất' in ind or 'công nghiệp' in ind:
        return 'Điền An (Khu lưu trú chuyên gia 20-30p) / Điền Sản'
    if 'bất động sản' in ind or 'đầu tư' in ind or 'xây dựng' in ind:
        return 'Điền Sản Founders (Vốn 5,3 tỷ, lời 3,2-4,4 tỷ)'
    if 'dầu khí' in ind or 'cảng biển' in ind or 'thủy hải sản' in ind or 'y tế' in ind:
        return 'Biệt Phủ VIP 1.000m² - 1.452m² (Nghỉ dưỡng thượng lưu)'
    return 'Điền Sản Founders / Biệt Phủ Điền Trang'

def fetch_html(url, retries=2):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Referer': 'https://masothue.com/'
    }
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=10) as resp:
                return resp.read().decode('utf-8')
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(3)
            else:
                break
        except Exception:
            time.sleep(1)
    return ""

def run():
    print("=== BẮT ĐẦU CÀO TOÀN DIỆN DOANH NGHIỆP BR-VT & HỒ TRÀM ===")
    
    # 1. Thu thập danh sách URL công ty
    targets = []
    seen_urls = set()
    
    for area_label, slug, max_p in DISTRICT_MAPPING:
        print(f"--> Đang quét khu vực: {area_label} ({max_p} trang)...")
        for p in range(1, max_p + 1):
            list_url = f"https://masothue.com/tra-cuu-ma-so-thue-theo-tinh/{slug}?page={p}"
            html = fetch_html(list_url)
            if not html:
                continue
            matches = re.findall(r'<h3[^>]*><a\s+href=[\'\"](/([0-9]{10}[^\'\"]*))[\'\"]\s+title=[\'\"]([^\'\"]+)[\'\"]>([^<]+)</a></h3>', html)
            for path, code, title, name in matches:
                full_url = f"https://masothue.com{path}"
                if full_url not in seen_urls:
                    seen_urls.add(full_url)
                    targets.append((area_label, full_url, name.strip()))
            time.sleep(random.uniform(0.3, 0.6))
            
    print(f"Đã thu thập tổng cộng {len(targets)} liên kết doanh nghiệp từ các khu vực trọng điểm.")
    
    # 2. Quét chi tiết và trích xuất thông tin
    leads = []
    seen_mst = set()
    
    for i, (area_label, url, default_name) in enumerate(targets):
        html = fetch_html(url)
        if not html:
            continue
            
        # SĐT
        tel_m = re.search(r'itemprop=[\'\"]telephone[\'\"]>\s*<span[^>]*>([0-9\s]+)</span>', html)
        tel = tel_m.group(1).replace(' ', '').strip() if tel_m else ''
        if not tel:
            continue
            
        # Ưu tiên các số di động (09, 08, 07, 03, 05)
        is_mobile = any(tel.startswith(prefix) for prefix in ['09', '08', '07', '03', '05'])
        
        # Tên công ty
        name_m = re.search(r'<th\s+itemprop=[\'\"]name[\'\"][^>]*>([^<]+)</th>', html)
        name = name_m.group(1).strip() if name_m else default_name
        name = re.sub(r'^[0-9\-]+\s*-\s*', '', name)
        
        # MST
        mst_m = re.search(r'<span\s+class=[\'\"]copy[\'\"][^>]*>([0-9\-]+)</span>', html)
        mst = mst_m.group(1).strip() if mst_m else ''
        if mst in seen_mst:
            continue
        seen_mst.add(mst)
        
        # Người đại diện
        rep_m = re.search(r'title=[\'\"]tra cứu mã số thuế công ty có giám đốc ([^\'\"]+)[\'\"]', html)
        if not rep_m:
            rep_m = re.search(r'Người đại diện.*?<span\s+itemprop=[\'\"]name[\'\"]>.*?<a[^>]*>([^<]+)</a>', html, re.DOTALL)
        rep = rep_m.group(1).strip() if rep_m else 'Chưa cập nhật'
        
        # Địa chỉ (Lấy địa chỉ chuẩn)
        addr = ''
        addr_match = re.search(r'<td\s+itemprop=[\'\"]address[\'\"][^>]*><span[^>]*class=[\'\"]copy[\'\"][^>]*>([^<]+)</span>', html)
        if addr_match:
            addr = addr_match.group(1).strip()
        else:
            addr_m2 = re.search(r'<td\s+itemprop=[\'\"]address[\'\"][^>]*>(.*?)</td>', html, re.DOTALL)
            if addr_m2:
                addr = re.sub(r'<[^>]+>', ' ', addr_m2.group(1)).strip()
        addr = re.sub(r'\s+', ' ', addr)
        
        # Phân loại ngành nghề
        industry = classify_industry(name)
        product_fit = suggest_product(industry, name)
        
        lead = {
            'khu_vuc': area_label,
            'ten_cong_ty': name,
            'nganh_nghe': industry,
            'nguoi_dai_dien': rep,
            'so_dien_thoai': tel,
            'la_dau_09': tel.startswith('09'),
            'la_di_dong': is_mobile,
            'dia_chi': addr,
            'mst': mst,
            'san_pham_phu_hop': product_fit,
            'url': url
        }
        leads.append(lead)
        prefix_tag = "09 VIP" if tel.startswith('09') else ("Di động" if is_mobile else "Số bàn")
        print(f"[{len(leads)}] [{area_label}] [{prefix_tag}] {name[:35]} | {rep} | {tel} | {industry[:25]}")
        
        time.sleep(random.uniform(0.35, 0.75))
        
        # Lấy tối đa khoảng 90 leads chất lượng
        if len(leads) >= 80:
            print("Đạt mốc 80 doanh nghiệp đủ tiêu chuẩn! Đang hoàn tất xuất dữ liệu...")
            break
            
    # Sắp xếp: Ưu tiên đầu số 09 trước, sau đó là các đầu số di động khác
    leads.sort(key=lambda x: (not x['la_dau_09'], not x['la_di_dong'], x['khu_vuc']))
    
    # Ghi ra CSV
    out_csv = 'data/danh_sach_doanh_nghiep_brvt_ho_tram_toan_dien.csv'
    os.makedirs('data', exist_ok=True)
    with open(out_csv, 'w', encoding='utf-8-sig', newline='') as f:
        fieldnames = [
            'khu_vuc', 'ten_cong_ty', 'nganh_nghe', 'nguoi_dai_dien', 
            'so_dien_thoai', 'la_dau_09', 'dia_chi', 'mst', 'san_pham_phu_hop', 'url'
        ]
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(leads)
        
    print(f"HOÀN THÀNH XUẤT {len(leads)} DOANH NGHIỆP VÀO: {out_csv}")
    return leads

if __name__ == '__main__':
    run()
