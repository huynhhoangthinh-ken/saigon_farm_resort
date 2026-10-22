#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Công cụ cào danh bạ Doanh nghiệp / Chủ doanh nghiệp từ Masothue.com
Tối ưu hóa tìm số điện thoại di động (đầu số 09, 08, 07, 03) tại Bà Rịa - Vũng Tàu, Đồng Nai
Dự án: Saigon Farm Resort
"""

import urllib.request
import urllib.parse
import re
import time
import os
import csv
import argparse
import random

DISTRICT_CODES = {
    "dat_do": "huyen-dat-do-55",
    "xuyen_moc": "huyen-xuyen-moc-255",
    "vung_tau": "thanh-pho-vung-tau-38",
    "ba_ria": "thanh-pho-ba-ria-52",
    "phu_my": "thanh-pho-phu-my-16292",
    "chau_duc": "huyen-chau-duc-768",
    "long_dien": "huyen-long-dien-453",
    "dong_nai": "dong-nai-57"
}

def fetch_html(url, retries=3):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'Referer': 'https://masothue.com/'
    }
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=12) as response:
                return response.read().decode('utf-8')
        except urllib.error.HTTPError as e:
            if e.code == 429:
                wait_time = (attempt + 1) * 3
                print(f"[Rate Limit 429] Đang tạm dừng {wait_time}s rồi thử lại...")
                time.sleep(wait_time)
            else:
                print(f"Lỗi HTTP {e.code} khi tải {url}")
                break
        except Exception as e:
            print(f"Lỗi kết nối ({e}) khi tải {url}")
            time.sleep(1)
    return ""

def scrape_masothue(area_code="huyen-dat-do-55", max_pages=3, only_09=False, max_leads=50, output_csv="data/leads.csv"):
    os.makedirs(os.path.dirname(output_csv) if os.path.dirname(output_csv) else '.', exist_ok=True)
    
    print(f"=== BẮT ĐẦU CÀO DỮ LIỆU MASOTHUE ===")
    print(f"Khu vực mã: {area_code}")
    print(f"Số trang quét danh sách: {max_pages}")
    print(f"Chỉ lấy đầu số 09: {only_09}")
    print(f"Mục tiêu số lượng: {max_leads}")
    print("=" * 40)
    
    company_urls = []
    for page in range(1, max_pages + 1):
        list_url = f"https://masothue.com/tra-cuu-ma-so-thue-theo-tinh/{area_code}?page={page}"
        print(f"--> Đang quét trang danh sách {page}: {list_url}")
        html = fetch_html(list_url)
        if not html:
            continue
        
        matches = re.findall(r'<h3[^>]*><a\s+href=[\'\"](/([0-9]{10}[^\'\"]*))[\'\"]\s+title=[\'\"]([^\'\"]+)[\'\"]>([^<]+)</a></h3>', html)
        for path, slug, title, name in matches:
            full_url = f"https://masothue.com{path}"
            if full_url not in company_urls:
                company_urls.append((full_url, name.strip()))
        
        time.sleep(random.uniform(0.6, 1.2))
        
    print(f"Tìm thấy tổng cộng {len(company_urls)} hồ sơ doanh nghiệp.")
    
    collected_leads = []
    count_09 = 0
    
    for i, (detail_url, default_name) in enumerate(company_urls):
        html = fetch_html(detail_url)
        if not html:
            continue
            
        # Trích xuất số điện thoại
        tel_m = re.search(r'itemprop=[\'\"]telephone[\'\"]>\s*<span[^>]*>([0-9\s]+)</span>', html)
        tel = tel_m.group(1).replace(' ', '').strip() if tel_m else ''
        
        # Bỏ qua nếu không có số điện thoại
        if not tel:
            continue
            
        is_09 = tel.startswith('09')
        if only_09 and not is_09:
            continue
            
        # Trích xuất tên công ty
        name_m = re.search(r'<th\s+itemprop=[\'\"]name[\'\"][^>]*>([^<]+)</th>', html)
        name = name_m.group(1).strip() if name_m else default_name
        name = re.sub(r'^[0-9\-]+\s*-\s*', '', name)
        
        # Trích xuất Mã số thuế
        mst_m = re.search(r'<span\s+class=[\'\"]copy[\'\"][^>]*>([0-9\-]+)</span>', html)
        mst = mst_m.group(1).strip() if mst_m else ''
        
        # Trích xuất Người đại diện / Giám đốc
        rep_m = re.search(r'title=[\'\"]tra cứu mã số thuế công ty có giám đốc ([^\'\"]+)[\'\"]', html)
        if not rep_m:
            rep_m = re.search(r'Người đại diện.*?<span\s+itemprop=[\'\"]name[\'\"]>.*?<a[^>]*>([^<]+)</a>', html, re.DOTALL)
        rep = rep_m.group(1).strip() if rep_m else 'Chưa công bố'
        
        # Trích xuất Địa chỉ
        addr_m = re.search(r'<td\s+itemprop=[\'\"]address[\'\"][^>]*>.*?<span[^>]*>([^<]+)</span>', html, re.DOTALL)
        if not addr_m:
            addr_m = re.search(r'itemprop=[\'\"]address[\'\"][^>]*>([^<]+)</td>', html)
        addr = addr_m.group(1).strip() if addr_m else ''
        addr = re.sub(r'\s+', ' ', addr)
        
        # Tình trạng hoạt động
        status_m = re.search(r'Tình trạng.*?<td>([^<]+)</td>', html, re.DOTALL)
        status = status_m.group(1).strip() if status_m else 'Đang hoạt động'
        
        lead = {
            'ten_cong_ty': name,
            'nguoi_dai_dien': rep,
            'so_dien_thoai': tel,
            'la_dau_09': is_09,
            'mst': mst,
            'dia_chi': addr,
            'tinh_trang': status,
            'url': detail_url
        }
        collected_leads.append(lead)
        
        if is_09:
            count_09 += 1
            print(f"[VIP 09 #{count_09}] {name[:40]} | ĐD: {rep} | SĐT: {tel}")
        else:
            print(f"[Lead #{len(collected_leads)}] {name[:40]} | ĐD: {rep} | SĐT: {tel}")
            
        time.sleep(random.uniform(0.7, 1.3))
        
        if len(collected_leads) >= max_leads:
            print(f"Đã đạt số lượng tối đa yêu cầu ({max_leads} leads). Dừng cào.")
            break
            
    # Sắp xếp ưu tiên đầu số 09 lên trên cùng
    collected_leads.sort(key=lambda x: (not x['la_dau_09']))
    
    # Xuất ra file CSV UTF-8 với BOM để mở trực tiếp trong Microsoft Excel tiếng Việt không bị lỗi font
    with open(output_csv, 'w', encoding='utf-8-sig', newline='') as f:
        fieldnames = ['ten_cong_ty', 'nguoi_dai_dien', 'so_dien_thoai', 'la_dau_09', 'mst', 'dia_chi', 'tinh_trang', 'url']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(collected_leads)
        
    print("=" * 40)
    print(f"HOÀN THÀNH! Đã lưu {len(collected_leads)} khách hàng ({count_09} số di động đầu 09) vào: {output_csv}")
    return collected_leads

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scraper danh bạ doanh nghiệp Masothue")
    parser.add_argument("--area", default="dat_do", help=f"Khu vực: {list(DISTRICT_CODES.keys())} hoặc mã URL")
    parser.add_argument("--pages", type=int, default=3, help="Số trang danh sách cần quét")
    parser.add_argument("--only09", action="store_true", help="Chỉ lưu các số bắt đầu bằng 09")
    parser.add_argument("--max", type=int, default=30, help="Số lead tối đa cần lấy")
    parser.add_argument("--out", default="data/leads_masothue.csv", help="Đường dẫn file CSV xuất ra")
    
    args = parser.parse_args()
    area_slug = DISTRICT_CODES.get(args.area, args.area)
    scrape_masothue(area_code=area_slug, max_pages=args.pages, only_09=args.only09, max_leads=args.max, output_csv=args.out)
