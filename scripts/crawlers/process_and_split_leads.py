#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
1. Cào dữ liệu chuyên sâu các Sàn Giao Dịch / Công ty Môi Giới Bất Động Sản tại BR-VT
2. Tách dữ liệu Master thành 2 tệp riêng biệt:
   - TỆP 1: KHÁCH HÀNG DOANH NHÂN MỤC TIÊU (End-buyers - Không có BĐS)
   - TỆP 2: ĐỐI TÁC SÀN GIAO DỊCH & MÔI GIỚI BĐS (Brokers / F1 / F2 / Liên kết)
"""

import urllib.request
import urllib.parse
import re
import time
import os
import csv
import random

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Referer': 'https://masothue.com/'
}

def fetch_html(url, retries=2):
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
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

def is_real_estate_company(name):
    n = name.upper()
    keywords = [
        'BẤT ĐỘNG SẢN', 'BĐS', 'ĐỊA ỐC', 'LAND', 'REALTY', 'REAL ESTATE',
        'MÔI GIỚI', 'NHÀ ĐẤT', 'ESTATE', 'HOMES', 'PROPERTY', 'PROPERTIES'
    ]
    return any(k in n for k in keywords)

def get_bds_links():
    queries = [
        'bất động sản Đất Đỏ', 'bất động sản Xuyên Mộc', 'bất động sản Hồ Tràm',
        'bất động sản Vũng Tàu', 'bất động sản Bà Rịa', 'bất động sản Phú Mỹ',
        'môi giới bất động sản Vũng Tàu', 'môi giới bất động sản Bà Rịa',
        'địa ốc Vũng Tàu', 'địa ốc Bà Rịa', 'địa ốc Đất Đỏ', 'địa ốc Hồ Tràm',
        'địa ốc Phú Mỹ', 'nhà đất Vũng Tàu', 'nhà đất Bà Rịa', 'nhà đất Đất Đỏ'
    ]
    links = []
    seen = set()
    for q in queries:
        q_enc = urllib.parse.quote(q)
        url = f"https://masothue.com/Search/?q={q_enc}&type=auto"
        html = fetch_html(url)
        if not html:
            continue
        matches = re.findall(r'<h3[^>]*><a\s+href=[\'\"](/([0-9]{10}[^\'\"]*))[\'\"]\s+title=[\'\"]([^\'\"]+)[\'\"]>([^<]+)</a></h3>', html)
        for path, code, title, name in matches:
            clean_name = name.strip()
            if is_real_estate_company(clean_name):
                full_url = f"https://masothue.com{path}"
                if full_url not in seen:
                    seen.add(full_url)
                    links.append((full_url, clean_name))
        time.sleep(0.3)
    return links

def run():
    os.makedirs('data', exist_ok=True)
    
    # 1. Đọc master hiện tại và lọc ra những công ty BĐS đã có
    master_file = 'data/master_leads_brvt_ho_tram_dat_do.csv'
    existing_bds = []
    end_buyers = []
    
    if os.path.exists(master_file):
        with open(master_file, 'r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            for r in reader:
                name = r.get('ten_cong_ty', '')
                ind = r.get('nganh_nghe', '')
                if is_real_estate_company(name) or 'Bất động sản' in ind:
                    existing_bds.append(r)
                else:
                    end_buyers.append(r)
                    
    print(f"Từ danh sách hiện tại ({len(existing_bds) + len(end_buyers)} DN):")
    print(f"  • Đã tách {len(end_buyers)} Khách hàng Doanh nhân thuần túy (KHÔNG CÓ BĐS)")
    print(f"  • Đã phát hiện {len(existing_bds)} Công ty/Văn phòng BĐS sẵn có")
    
    # 2. Cào thêm các công ty BĐS / Sàn môi giới từ Masothue
    print("\n--> Đang tìm kiếm thêm các Sàn BĐS / Môi giới tại Bà Rịa - Vũng Tàu...")
    bds_links = get_bds_links()
    print(f"Tìm thấy {len(bds_links)} liên kết công ty BĐS.")
    
    seen_mst = {r['mst'] for r in existing_bds if r.get('mst')}
    new_bds_leads = []
    
    for url, default_name in bds_links:
        html = fetch_html(url)
        if not html:
            continue
            
        tel_m = re.search(r'itemprop=[\'\"]telephone[\'\"]>\s*<span[^>]*>([0-9\s]+)</span>', html)
        tel = tel_m.group(1).replace(' ', '').strip() if tel_m else ''
        if not tel:
            continue
            
        mst_m = re.search(r'<span\s+class=[\'\"]copy[\'\"][^>]*>([0-9\-]+)</span>', html)
        mst = mst_m.group(1).strip() if mst_m else ''
        if not mst or mst in seen_mst:
            continue
        seen_mst.add(mst)
        
        name_m = re.search(r'<th\s+itemprop=[\'\"]name[\'\"][^>]*>([^<]+)</th>', html)
        name = name_m.group(1).strip() if name_m else default_name
        name = re.sub(r'^[0-9\-]+\s*-\s*', '', name)
        
        rep_m = re.search(r'title=[\'\"]tra cứu mã số thuế công ty có giám đốc ([^\'\"]+)[\'\"]', html)
        if not rep_m:
            rep_m = re.search(r'Người đại diện.*?<span\s+itemprop=[\'\"]name[\'\"]>.*?<a[^>]*>([^<]+)</a>', html, re.DOTALL)
        rep = rep_m.group(1).strip() if rep_m else 'Chưa cập nhật'
        
        addr = ''
        addr_match = re.search(r'<td\s+itemprop=[\'\"]address[\'\"][^>]*><span[^>]*class=[\'\"]copy[\'\"][^>]*>([^<]+)</span>', html)
        if addr_match:
            addr = addr_match.group(1).strip()
        else:
            addr_m2 = re.search(r'<td\s+itemprop=[\'\"]address[\'\"][^>]*>(.*?)</td>', html, re.DOTALL)
            if addr_m2:
                addr = re.sub(r'<[^>]+>', ' ', addr_m2.group(1)).strip()
        addr = re.sub(r'\s+', ' ', addr)
        
        # Xác định khu vực
        area = 'BR-VT'
        addr_lower = addr.lower()
        if 'đất đỏ' in addr_lower:
            area = 'Huyện Đất Đỏ'
        elif 'xuyên mộc' in addr_lower or 'hồ tràm' in addr_lower:
            area = 'Hồ Tràm / Xuyên Mộc'
        elif 'vũng tàu' in addr_lower:
            area = 'TP. Vũng Tàu'
        elif 'bà rịa' in addr_lower:
            area = 'TP. Bà Rịa'
        elif 'phú mỹ' in addr_lower:
            area = 'TX. Phú Mỹ'
        elif 'long điền' in addr_lower or 'long hải' in addr_lower:
            area = 'Long Điền / Long Hải'
            
        is_09 = tel.startswith('09')
        
        lead = {
            'khu_vuc': area,
            'ten_cong_ty': name,
            'loai_hinh_doi_tac': 'Sàn Giao Dịch / Công Ty Môi Giới BĐS',
            'nguoi_dai_dien': rep,
            'so_dien_thoai': tel,
            'la_dau_09': str(is_09),
            'dia_chi': addr,
            'mst': mst,
            'muc_tieu_hop_tac': 'Ký hợp đồng Liên kết phân phối / Đại lý F1-F2',
            'url': url
        }
        new_bds_leads.append(lead)
        print(f"[{len(new_bds_leads)}] [{area}] {name[:35]} | {rep} | {tel}")
        time.sleep(random.uniform(0.3, 0.6))
        
        if len(new_bds_leads) >= 45:
            break
            
    # Gộp toàn bộ BĐS
    all_bds = []
    # format existing bds
    for r in existing_bds:
        all_bds.append({
            'khu_vuc': r.get('khu_vuc', 'BR-VT'),
            'ten_cong_ty': r.get('ten_cong_ty', ''),
            'loai_hinh_doi_tac': 'Sàn Giao Dịch / Công Ty Môi Giới BĐS',
            'nguoi_dai_dien': r.get('nguoi_dai_dien', ''),
            'so_dien_thoai': r.get('so_dien_thoai', ''),
            'la_dau_09': r.get('la_dau_09', 'False'),
            'dia_chi': r.get('dia_chi', ''),
            'mst': r.get('mst', ''),
            'muc_tieu_hop_tac': 'Ký hợp đồng Liên kết phân phối / Đại lý F1-F2',
            'url': r.get('url', '')
        })
    all_bds.extend(new_bds_leads)
    all_bds.sort(key=lambda x: (x.get('la_dau_09') != 'True', x.get('khu_vuc', '')))
    
    # 3. Xuất TỆP 1: KHÁCH HÀNG MỤC TIÊU (END-BUYERS)
    file_buyers = 'data/tep_khach_hang_doanh_nhan_brvt.csv'
    fieldnames_buyers = ['khu_vuc', 'ten_cong_ty', 'nganh_nghe', 'nguoi_dai_dien', 'so_dien_thoai', 'la_dau_09', 'dia_chi', 'mst', 'san_pham_phu_hop', 'url']
    with open(file_buyers, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames_buyers, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(end_buyers)
        
    # 4. Xuất TỆP 2: ĐỐI TÁC SÀN BĐS (BROKERS / AGENCIES)
    file_bds = 'data/tep_doi_tac_san_moi_gioi_bds_brvt.csv'
    fieldnames_bds = ['khu_vuc', 'ten_cong_ty', 'loai_hinh_doi_tac', 'nguoi_dai_dien', 'so_dien_thoai', 'la_dau_09', 'dia_chi', 'mst', 'muc_tieu_hop_tac', 'url']
    with open(file_bds, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames_bds, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(all_bds)
        
    print("\n" + "="*50)
    print(f"XUẤT THÀNH CÔNG 2 TỆP DỮ LIỆU ĐỘC LẬP:")
    print(f"1. Tệp Khách hàng Doanh nhân (End-buyers): {len(end_buyers)} doanh nghiệp -> {file_buyers}")
    print(f"2. Tệp Đối tác Sàn & Môi giới BĐS (Partners): {len(all_bds)} sàn/công ty BĐS -> {file_bds}")
    print("="*50)

if __name__ == '__main__':
    run()
