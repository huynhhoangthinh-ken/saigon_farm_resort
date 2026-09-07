#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate listing.html and listing/index.html with verified images and fallback
"""

import json
import os

def update_listing():
    with open("data/listing_categories.json", "r", encoding="utf-8") as f:
        categories = json.load(f)

    # 17 Verified Villa Images
    villa_imgs = [
        "assets/Index_asset/villa_gallery/sunrise_1_ext_1.jpg",
        "assets/Index_asset/villa_gallery/sunrise_2_living_1.jpg",
        "assets/Index_asset/villa_gallery/sunset_1_courtyard.jpg",
        "assets/Index_asset/villa_gallery/sunset_2_ext_1.jpg",
        "assets/Index_asset/villa_gallery/sunrise_1_ext_2.jpg",
        "assets/Index_asset/villa_gallery/sunset_2_living.jpg",
        "assets/Index_asset/villa_gallery/sunset_1_lake_1.jpg",
        "assets/Index_asset/villa_gallery/sunset_1_lake_2.jpg",
        "assets/Index_asset/villa_gallery/sunrise_1_bed_1.jpg",
        "assets/Index_asset/villa_gallery/sunrise_1_living_1.jpg",
        "assets/Index_asset/villa_gallery/sunrise_2_shc_1.jpg",
        "assets/Index_asset/villa_gallery/sunset_1_kitchen.jpg",
        "assets/Index_asset/villa_gallery/sunset_2_master.jpg",
        "assets/Index_asset/villa_gallery/sunrise_2_bed_1.jpg",
        "assets/Index_asset/villa_gallery/sunset_1_master.jpg",
        "assets/Index_asset/villa_gallery/sunrise_1_bed_2.jpg",
        "assets/Index_asset/villa_gallery/sunrise_2_living_2.jpg"
    ]

    # 12 Verified Dien San Images
    dien_san_imgs = [
        "assets/Index_asset/editorial_photo/3_product_type/Dien_san_12.webp",
        "assets/Index_asset/editorial_photo/3_product_type/Dien_san_Phan_lo.webp",
        "assets/Index_asset/editorial_photo/Canh_dong_lua.png",
        "assets/Index_asset/Phoicanh_3D_Tien_ich/Tong_the/S01_Final_Fix.jpg",
        "assets/Index_asset/Phoicanh_3D_Tien_ich/Tong_the/NEW_S02.jpg",
        "assets/Index_asset/Phoicanh_3D_Tien_ich/Duong_noi_bo/SFR_1.webp",
        "assets/Index_asset/Phoicanh_3D_Tien_ich/Duong_noi_bo/SFR_2-2.webp",
        "assets/Index_asset/Phoicanh_3D_Tien_ich/Duong_noi_bo/SFR_3.webp",
        "assets/Index_asset/Phoicanh_3D_Tien_ich/Duong_noi_bo/SFR_4.webp",
        "assets/Index_asset/Phoicanh_3D_Tien_ich/Duong_noi_bo/SFR_6.webp",
        "assets/Index_asset/villa_gallery/sunrise_1_ext_1.jpg",
        "assets/Index_asset/villa_gallery/sunset_1_courtyard.jpg"
    ]

    # 7 Verified Dien An Images
    dien_an_imgs = [
        "assets/Index_asset/editorial_photo/3_product_type/Dien_an_7.webp",
        "assets/Index_asset/editorial_photo/3_product_type/Dien_an_Bat_dong_San_dong_tien.webp",
        "assets/Index_asset/editorial_photo/3_product_type/Dien_an_layout.webp",
        "assets/Index_asset/Phoicanh_3D_Tien_ich/Ven_ho_clubhouse/Lake_Clubhouse_1.jpg",
        "assets/Index_asset/Phoicanh_3D_Tien_ich/Ven_ho_clubhouse/Lake_Clubhouse_2.jpg",
        "assets/Index_asset/Phoicanh_3D_Tien_ich/Ven_ho_clubhouse/Lake_Clubhouse_3.jpg",
        "assets/Index_asset/Phoicanh_3D_Tien_ich/Ven_ho_clubhouse/Lake_Clubhouse_4.jpg"
    ]

    # Update data in memory
    for cat in categories:
        slug = cat.get("slug")
        if slug == "biet-phu-dien-trang":
            for i, item in enumerate(cat.get("items", [])):
                item["image"] = villa_imgs[i % len(villa_imgs)]
        elif slug == "dien-san":
            for i, item in enumerate(cat.get("items", [])):
                item["image"] = dien_san_imgs[i % len(dien_san_imgs)]
        elif slug == "dien-an":
            for i, item in enumerate(cat.get("items", [])):
                item["image"] = dien_an_imgs[i % len(dien_an_imgs)]

    # Save updated json
    with open("data/listing_categories.json", "w", encoding="utf-8") as f:
        json.dump(categories, f, ensure_ascii=False, indent=2)

    # Flatten items
    all_items = []
    for cat in categories:
        slug = cat.get("slug", "")
        cat_title = cat.get("title", "")
        cat_badge = cat.get("badge", "")
        for item in cat.get("items", []):
            item_copy = dict(item)
            item_copy["category_slug"] = slug
            item_copy["category_title"] = cat_title
            item_copy["category_badge"] = cat_badge
            all_items.append(item_copy)

    total_count = len(all_items)
    dien_san_count = sum(1 for i in all_items if i["category_slug"] == "dien-san")
    dien_an_count = sum(1 for i in all_items if i["category_slug"] == "dien-an")
    biet_phu_count = sum(1 for i in all_items if i["category_slug"] == "biet-phu-dien-trang")
    available_count = sum(1 for i in all_items if i.get("status_type") == "available")
    reserved_count = sum(1 for i in all_items if i.get("status_type") == "reserved")

    # Generate cards HTML
    cards_html = []
    fallback_img = "assets/Index_asset/Phoicanh_3D_Tien_ich/Tong_the/S01_Final_Fix.jpg"

    for item in all_items:
        code = item.get("code", "")
        area_str = item.get("area", "")
        try:
            area_clean = float(area_str.replace(".", "").replace(",", "."))
        except:
            area_clean = 1000.0
        
        area_type = "large" if area_clean >= 1000.0 else "compact"
        status_type = item.get("status_type", "available")
        status_text = item.get("status", "Còn hàng")
        features = item.get("features", "")
        suitable_for = item.get("suitable_for", "")
        img = item.get("image", fallback_img)
        cat_slug = item.get("category_slug", "")
        cat_title = item.get("category_title", "")

        status_badge_class = "status-available" if status_type == "available" else "status-reserved"
        status_icon = "fa-circle-check" if status_type == "available" else "fa-clock"

        if cat_slug == "dien-san":
            special_note = """
            <div class="card-policy-tag">
              <i class="fa-solid fa-gift"></i> CS Mở Bán: 12 Tr/m² • Giảm 6% TT nhanh • Giảm 800Tr • Giữ lại 30% CĐT hỗ trợ ra hàng
            </div>
            """
        elif cat_slug == "dien-an":
            special_note = """
            <div class="card-policy-tag" style="background:#e8f4fd; color:#125b96; border-color:#bcdcf5;">
              <i class="fa-solid fa-hand-holding-dollar"></i> Cụm 30 phòng lưu trú • Thuê khoán 5 năm: 120 Tr/tháng
            </div>
            """
        else:
            special_note = """
            <div class="card-policy-tag" style="background:#fef7e9; color:#8c6b32; border-color:#eed8b0;">
              <i class="fa-solid fa-crown"></i> Dinh thự đơn lập ven hồ • 150 đêm nghỉ dưỡng + 215 đêm chia sẻ 50% DT
            </div>
            """

        card = f"""
        <div class="listing-card" 
             data-code="{code.lower()}"
             data-category="{cat_slug}" 
             data-area-type="{area_type}" 
             data-area-val="{area_clean}" 
             data-status="{status_type}">
          <div class="card-thumb-wrap">
            <img src="{img}" 
                 alt="Phối cảnh {code}" 
                 loading="lazy" 
                 class="card-thumb" 
                 onerror="this.onerror=null; this.src='{fallback_img}'">
            <span class="card-badge-code">MÃ LÔ {code}</span>
            <span class="card-badge-cat">{cat_title}</span>
            <span class="card-badge-status {status_badge_class}">
              <i class="fa-solid {status_icon}"></i> {status_text}
            </span>
          </div>
          <div class="card-body">
            <div class="card-meta-top">
              <span class="card-area"><i class="fa-solid fa-ruler-combined"></i> <strong>{area_str}</strong> m²</span>
              <span class="card-legal"><i class="fa-solid fa-shield-halved"></i> 100% Thổ Cư · Sổ Riêng</span>
            </div>
            <h4 class="card-title">Mã Lô {code} · {cat_title}</h4>
            <p class="card-desc"><strong>Đặc tính:</strong> {features}</p>
            <div class="card-fit">
              <i class="fa-regular fa-compass" style="color: #2e7d32; margin-right: 4px;"></i>
              <span><strong>Phù hợp:</strong> {suitable_for}</span>
            </div>
            {special_note}
            <div class="card-footer-action">
              <div class="card-price-label">
                <span>Chính sách giá</span>
                <strong>Gốc Đợt 1 CĐT</strong>
              </div>
              <button type="button" class="btn-card-action" onclick="openBookingModal('{code}', '{area_str}', '{cat_title}')">
                <i class="fa-solid fa-file-invoice-dollar"></i> Nhận Báo Giá
              </button>
            </div>
          </div>
        </div>
        """
        cards_html.append(card)

    cards_rendered = "\n".join(cards_html)

    html_content = f"""<!DOCTYPE html>
<html lang="vi">
<head>
  <!-- Google Tag (gtag.js) - Google Analytics -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-8L9EZXY66G"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', 'G-8L9EZXY66G');
  </script>
  <meta charset="utf-8"/>
  <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
  <title>Giỏ Hàng Sản Phẩm Saigon Farm Resort | Bảng Hàng Nội Bộ Đợt 1</title>
  <meta content="Tổng hợp danh sách các mã căn, mã lô mở bán đợt 1 tại Quần thể Saigon Farm Resort: Điền Sản (12 nền độc bản), Điền An (7 cụm lưu trú) và Biệt Phủ Điền Trang (17 dinh thự). Cập nhật quỹ hàng trực tiếp từ Chủ đầu tư MDS Living." name="description"/>
  <!-- Google Fonts & FontAwesome -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Playfair+Display:ital,wght@0,500;0,600;0,700;1,400&display=swap" rel="stylesheet">
  <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet"/>
  
  <style>
    :root {{
      --primary: #183024;
      --primary-dark: #0f1f17;
      --primary-light: #2b523f;
      --gold: #c9a96e;
      --gold-dark: #8c6b32;
      --gold-light: #f5eedf;
      --bg-cream: #faf6ef;
      --text-main: #2b2b2b;
      --text-muted: #666666;
      --border-color: #e6decb;
      --font-sans: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      --font-serif: 'Playfair Display', Georgia, serif;
    }}

    * {{
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }}

    body {{
      font-family: var(--font-sans);
      background-color: var(--bg-cream);
      color: var(--text-main);
      line-height: 1.6;
      overflow-x: hidden;
    }}

    .container {{
      max-width: 1280px;
      margin: 0 auto;
      padding: 0 20px;
    }}

    /* Top Utility Bar */
    .topbar {{
      background: #fdfaf4;
      color: #5c472d;
      font-size: 0.82rem;
      padding: 8px 0;
      border-bottom: 1px solid #ebdcc5;
    }}
    .topbar-container {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 10px;
    }}
    .topbar a {{
      color: #5c472d;
      text-decoration: none;
      transition: color 0.2s;
    }}
    .topbar a:hover {{
      color: var(--gold-dark);
    }}

    /* Navbar */
    .navbar {{
      position: sticky;
      top: 0;
      z-index: 100;
      background: rgba(255,255,255,0.97);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border-color);
      box-shadow: 0 4px 20px rgba(0,0,0,0.03);
    }}
    .nav-container {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 14px 20px;
      max-width: 1280px;
      margin: 0 auto;
    }}
    .nav-brand {{
      display: flex;
      align-items: center;
      gap: 12px;
      text-decoration: none;
    }}
    .nav-brand img {{
      height: 42px;
      width: auto;
      object-fit: contain;
    }}
    .nav-brand-text {{
      display: flex;
      flex-direction: column;
    }}
    .nav-brand-title {{
      font-family: var(--font-serif);
      font-size: 1.22rem;
      font-weight: 700;
      color: var(--primary);
      letter-spacing: 0.5px;
    }}
    .nav-brand-sub {{
      font-size: 0.75rem;
      color: var(--gold-dark);
      font-weight: 600;
      letter-spacing: 1px;
      text-transform: uppercase;
    }}
    .nav-menu {{
      display: flex;
      align-items: center;
      gap: 20px;
      list-style: none;
    }}
    .nav-menu a {{
      text-decoration: none;
      color: var(--text-main);
      font-size: 0.92rem;
      font-weight: 600;
      transition: color 0.2s;
    }}
    .nav-menu a:hover, .nav-menu a.active {{
      color: var(--gold-dark);
    }}
    .btn-cta-nav {{
      background: linear-gradient(135deg, var(--gold) 0%, var(--gold-dark) 100%);
      color: #fff !important;
      padding: 8px 18px;
      border-radius: 6px;
      font-weight: 700;
      box-shadow: 0 2px 8px rgba(140, 107, 50, 0.25);
    }}

    /* Hero Banner */
    .listing-hero {{
      background: linear-gradient(135deg, rgba(24, 48, 36, 0.95) 0%, rgba(15, 31, 23, 0.98) 100%), url('assets/Index_asset/Phoicanh_3D_Tien_ich/Tong_the/S01_Final_Fix.jpg');
      background-size: cover;
      background-position: center;
      color: #fff;
      padding: 55px 0 45px;
      border-bottom: 3px solid var(--gold);
    }}
    .hero-tag {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: rgba(201, 169, 110, 0.2);
      border: 1px solid var(--gold);
      color: var(--gold);
      padding: 4px 14px;
      border-radius: 30px;
      font-size: 0.78rem;
      font-weight: 700;
      letter-spacing: 1px;
      text-transform: uppercase;
      margin-bottom: 12px;
    }}
    .hero-title {{
      font-family: var(--font-serif);
      font-size: 2.35rem;
      color: #fff;
      line-height: 1.25;
      margin-bottom: 12px;
    }}
    .hero-subtitle {{
      font-size: 1.02rem;
      color: #dfd8cb;
      max-width: 860px;
      line-height: 1.6;
      margin-bottom: 24px;
    }}
    .hero-stats {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 14px;
      margin-top: 25px;
      border-top: 1px dashed rgba(201, 169, 110, 0.4);
      padding-top: 20px;
    }}
    .hero-stat-card {{
      background: rgba(255,255,255,0.06);
      border: 1px solid rgba(255,255,255,0.1);
      border-radius: 8px;
      padding: 12px 16px;
    }}
    .hero-stat-num {{
      font-size: 1.45rem;
      font-weight: 800;
      color: var(--gold);
    }}
    .hero-stat-label {{
      font-size: 0.78rem;
      color: #ddd;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}

    /* Disclaimer Notice */
    .disclaimer-box {{
      background: #ffffff;
      border-left: 4px solid var(--gold-dark);
      border-radius: 8px;
      padding: 16px 20px;
      margin: 28px 0 20px;
      box-shadow: 0 4px 14px rgba(0,0,0,0.04);
      font-size: 0.9rem;
      color: #555;
    }}

    /* Filter Controls */
    .controls-panel {{
      background: #ffffff;
      border: 1px solid var(--border-color);
      border-radius: 12px;
      padding: 22px 24px;
      margin-bottom: 30px;
      box-shadow: 0 4px 16px rgba(0,0,0,0.04);
    }}
    .category-pills {{
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin-bottom: 18px;
      border-bottom: 1px solid #f0e9dc;
      padding-bottom: 16px;
    }}
    .cat-btn {{
      background: #faf6ee;
      border: 1px solid var(--border-color);
      color: var(--text-main);
      padding: 8px 18px;
      border-radius: 30px;
      font-weight: 600;
      font-size: 0.88rem;
      cursor: pointer;
      transition: all 0.2s;
    }}
    .cat-btn:hover {{
      background: #f2e9d8;
    }}
    .cat-btn.active {{
      background: var(--primary);
      border-color: var(--primary);
      color: #fff;
    }}
    .cat-btn span.badge-num {{
      display: inline-block;
      background: rgba(201, 169, 110, 0.3);
      color: inherit;
      font-size: 0.72rem;
      padding: 2px 7px;
      border-radius: 12px;
      margin-left: 6px;
      font-weight: 700;
    }}
    .cat-btn.active span.badge-num {{
      background: var(--gold);
      color: #111;
    }}

    .sub-filters {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 16px;
    }}
    .filter-group {{
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
    }}
    .filter-label {{
      font-size: 0.84rem;
      font-weight: 700;
      color: #666;
      text-transform: uppercase;
    }}
    .sub-btn {{
      background: #fff;
      border: 1px solid #d8cfc0;
      color: #444;
      padding: 6px 14px;
      border-radius: 20px;
      font-size: 0.82rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s;
    }}
    .sub-btn:hover {{
      background: #faf6ef;
    }}
    .sub-btn.active {{
      background: var(--gold-dark);
      border-color: var(--gold-dark);
      color: #fff;
    }}
    .search-input-box {{
      position: relative;
      min-width: 240px;
    }}
    .search-input-box input {{
      width: 100%;
      padding: 8px 14px 8px 36px;
      border: 1px solid #d8cfc0;
      border-radius: 20px;
      font-size: 0.86rem;
      outline: none;
      font-family: inherit;
    }}
    .search-input-box i {{
      position: absolute;
      left: 12px;
      top: 50%;
      transform: translateY(-50%);
      color: #999;
      font-size: 0.85rem;
    }}

    /* Listings Grid */
    .listings-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
      gap: 24px;
      margin-bottom: 50px;
    }}
    .listing-card {{
      background: #ffffff;
      border: 1px solid var(--border-color);
      border-radius: 12px;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      box-shadow: 0 4px 16px rgba(0,0,0,0.04);
      transition: transform 0.25s, box-shadow 0.25s;
    }}
    .listing-card:hover {{
      transform: translateY(-4px);
      box-shadow: 0 10px 28px rgba(0,0,0,0.09);
      border-color: var(--gold);
    }}
    .card-thumb-wrap {{
      position: relative;
      height: 220px;
      overflow: hidden;
      background: #183024;
    }}
    .card-thumb {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.5s ease;
    }}
    .listing-card:hover .card-thumb {{
      transform: scale(1.05);
    }}
    .card-badge-code {{
      position: absolute;
      top: 12px;
      left: 12px;
      background: rgba(15, 31, 23, 0.92);
      color: #fff;
      font-size: 0.78rem;
      font-weight: 800;
      padding: 4px 10px;
      border-radius: 4px;
      letter-spacing: 0.5px;
      border: 1px solid rgba(201, 169, 110, 0.4);
    }}
    .card-badge-cat {{
      position: absolute;
      bottom: 12px;
      left: 12px;
      background: rgba(255,255,255,0.9);
      color: var(--primary);
      font-size: 0.72rem;
      font-weight: 700;
      padding: 3px 8px;
      border-radius: 4px;
    }}
    .card-badge-status {{
      position: absolute;
      top: 12px;
      right: 12px;
      font-size: 0.74rem;
      font-weight: 700;
      padding: 4px 10px;
      border-radius: 20px;
    }}
    .status-available {{
      background: #e8f5e9;
      color: #2e7d32;
      border: 1px solid #c8e6c9;
    }}
    .status-reserved {{
      background: #fff3e0;
      color: #e65100;
      border: 1px solid #ffe0b2;
    }}

    .card-body {{
      padding: 20px;
      display: flex;
      flex-direction: column;
      flex: 1;
    }}
    .card-meta-top {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 8px;
      font-size: 0.85rem;
    }}
    .card-area {{
      color: var(--gold-dark);
      font-weight: 700;
    }}
    .card-area strong {{
      font-size: 1.15rem;
      color: var(--primary);
    }}
    .card-legal {{
      font-size: 0.78rem;
      color: #2e7d32;
      font-weight: 600;
    }}
    .card-title {{
      font-family: var(--font-serif);
      font-size: 1.28rem;
      color: #1a1a1a;
      margin-bottom: 8px;
    }}
    .card-desc {{
      font-size: 0.86rem;
      color: #555;
      line-height: 1.5;
      margin-bottom: 10px;
      min-height: 42px;
    }}
    .card-fit {{
      font-size: 0.84rem;
      color: #333;
      background: #faf6ee;
      padding: 8px 12px;
      border-radius: 6px;
      margin-bottom: 12px;
      border: 1px dashed #ebdcc5;
    }}
    .card-policy-tag {{
      background: #faf4e8;
      border: 1px solid #ebd9b8;
      color: #8c6b32;
      font-size: 0.78rem;
      font-weight: 600;
      padding: 6px 10px;
      border-radius: 6px;
      margin-bottom: 16px;
      line-height: 1.4;
    }}
    .card-footer-action {{
      margin-top: auto;
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-top: 1px solid #f0e9dc;
      padding-top: 14px;
      gap: 10px;
    }}
    .card-price-label {{
      display: flex;
      flex-direction: column;
    }}
    .card-price-label span {{
      font-size: 0.72rem;
      color: #888;
      text-transform: uppercase;
    }}
    .card-price-label strong {{
      font-size: 0.96rem;
      color: var(--primary);
    }}
    .btn-card-action {{
      background: var(--primary);
      color: #fff;
      border: none;
      padding: 9px 16px;
      border-radius: 6px;
      font-size: 0.85rem;
      font-weight: 700;
      cursor: pointer;
      transition: background 0.2s;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }}
    .btn-card-action:hover {{
      background: var(--gold-dark);
    }}

    /* No results */
    .no-results {{
      grid-column: 1 / -1;
      text-align: center;
      padding: 60px 20px;
      background: #fff;
      border-radius: 12px;
      border: 1px dashed #d8cfc0;
    }}
    .no-results i {{
      font-size: 2.5rem;
      color: #bbb;
      margin-bottom: 12px;
    }}

    /* Modal Booking */
    .modal-backdrop {{
      display: none;
      position: fixed;
      inset: 0;
      background: rgba(0,0,0,0.6);
      backdrop-filter: blur(4px);
      z-index: 9999;
      align-items: center;
      justify-content: center;
      padding: 20px;
    }}
    .modal-box {{
      background: #ffffff;
      border-radius: 14px;
      max-width: 520px;
      width: 100%;
      padding: 30px 28px;
      box-shadow: 0 20px 50px rgba(0,0,0,0.25);
      position: relative;
      border: 1px solid var(--border-color);
    }}
    .modal-close {{
      position: absolute;
      top: 18px;
      right: 18px;
      background: #f0f0f0;
      border: none;
      width: 32px;
      height: 32px;
      border-radius: 50%;
      cursor: pointer;
      font-size: 1rem;
      color: #666;
    }}
    .modal-title {{
      font-family: var(--font-serif);
      font-size: 1.5rem;
      color: var(--primary);
      margin-bottom: 6px;
    }}
    .modal-sub {{
      font-size: 0.88rem;
      color: #666;
      margin-bottom: 20px;
    }}
    .form-group {{
      margin-bottom: 14px;
    }}
    .form-group label {{
      display: block;
      font-size: 0.82rem;
      font-weight: 700;
      color: #444;
      margin-bottom: 6px;
      text-transform: uppercase;
    }}
    .form-group input, .form-group select, .form-group textarea {{
      width: 100%;
      padding: 10px 14px;
      border: 1px solid #d8cfc0;
      border-radius: 6px;
      font-family: inherit;
      font-size: 0.9rem;
      outline: none;
    }}
    .form-group input:focus, .form-group select:focus, .form-group textarea:focus {{
      border-color: var(--gold-dark);
    }}
    .btn-submit-modal {{
      width: 100%;
      background: linear-gradient(135deg, var(--gold) 0%, var(--gold-dark) 100%);
      color: #fff;
      border: none;
      padding: 12px;
      border-radius: 6px;
      font-size: 0.96rem;
      font-weight: 700;
      cursor: pointer;
      margin-top: 8px;
    }}

    /* Footer */
    footer {{
      background: #0f1f17;
      color: #ddd;
      padding: 45px 0 25px;
      border-top: 2px solid var(--gold);
      font-size: 0.88rem;
    }}
    .footer-content {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 20px;
      margin-bottom: 25px;
    }}
    .footer-copy {{
      text-align: center;
      border-top: 1px solid rgba(255,255,255,0.1);
      padding-top: 20px;
      font-size: 0.8rem;
      color: #888;
    }}

    @media (max-width: 768px) {{
      .hero-title {{
        font-size: 1.85rem;
      }}
      .nav-menu {{
        display: none;
      }}
      .sub-filters {{
        flex-direction: column;
        align-items: stretch;
      }}
      .search-input-box {{
        width: 100%;
      }}
      .listings-grid {{
        grid-template-columns: 1fr;
      }}
    }}
  </style>
</head>
<body>

  <!-- Top Utility Bar -->
  <div class="topbar">
    <div class="container topbar-container">
      <div>🌿 <strong>Saigon Farm Resort:</strong> Quần Thể Nghỉ Dưỡng Sinh Thái Ven Hồ 100ha • Liền Kề Biển Hồ Tràm</div>
      <div style="display: flex; gap: 16px; align-items: center;">
        <a href="index.html"><i class="fa-solid fa-house" style="font-size:0.75rem; color:#8c6b32;"></i> Trang Chủ</a>
        <a href="gioi-thieu.html"><i class="fa-solid fa-file-lines" style="font-size:0.75rem; color:#8c6b32;"></i> Bản Giới Thiệu</a>
        <a href="article.html?id=304" style="background: linear-gradient(135deg, #c9a96e 0%, #a88448 100%); color: #fff; padding: 4px 12px; border-radius: 4px; font-weight: 700; text-decoration: none; box-shadow: 0 2px 6px rgba(201, 169, 110, 0.3);"><i class="fa-solid fa-calendar-check" style="font-size:0.75rem; margin-right:4px;"></i> Đăng Ký Khảo Sát</a>
      </div>
    </div>
  </div>

  <!-- Navbar -->
  <header class="navbar">
    <div class="nav-container">
      <a href="index.html" class="nav-brand">
        <img src="assets/Index_asset/LOGO_PNG/LOGO_SGF_3_BROWN.png" alt="Saigon Farm Resort Logo">
        <div class="nav-brand-text">
          <span class="nav-brand-title">SAIGON FARM RESORT</span>
          <span class="nav-brand-sub">Quỹ Căn Nội Bộ Đợt 1</span>
        </div>
      </a>
      <ul class="nav-menu">
        <li><a href="index.html">Trang Chủ</a></li>
        <li><a href="gioi-thieu.html">Bản Giới Thiệu (Tư Vấn)</a></li>
        <li><a href="dien-san.html">Điền Sản</a></li>
        <li><a href="dien-an.html">Điền An</a></li>
        <li><a href="biet-phu-dien-trang.html">Biệt Phủ</a></li>
        <li>
          <a href="tel:0909000000" class="btn-cta-nav">
            <i class="fa-solid fa-phone"></i> Hotline BQL
          </a>
        </li>
      </ul>
    </div>
  </header>

  <!-- Hero Banner -->
  <section class="listing-hero">
    <div class="container">
      <span class="hero-tag"><i class="fa-solid fa-lock"></i> DANH SÁCH GIỎ HÀNG NỘI BỘ (FOUNDERS CLUB)</span>
      <h1 class="hero-title">Quỹ Sản Phẩm Mở Bán Giai Đoạn 1</h1>
      <p class="hero-subtitle">
        Bảng theo dõi thời gian thực 36 sản phẩm độc bản thuộc 3 phân khu cao cấp: <strong>Điền Sản</strong> (12 nền độc bản ven hồ), <strong>Điền An</strong> (07 cụm lưu trú chuyên gia) và <strong>Biệt Phủ Điền Trang</strong> (17 dinh thự thượng lưu).
      </p>

      <div class="hero-stats">
        <div class="hero-stat-card">
          <div class="hero-stat-num">{total_count}</div>
          <div class="hero-stat-label">Tổng Số Mã Căn/Lô</div>
        </div>
        <div class="hero-stat-card">
          <div class="hero-stat-num">{available_count}</div>
          <div class="hero-stat-label">Đang Nhận Booking</div>
        </div>
        <div class="hero-stat-card">
          <div class="hero-stat-num">{reserved_count}</div>
          <div class="hero-stat-label">Đã Giữ Chỗ Đợt 1</div>
        </div>
        <div class="hero-stat-card">
          <div class="hero-stat-num">100%</div>
          <div class="hero-stat-label">Thổ Cư · Sổ Hồng Riêng</div>
        </div>
      </div>
    </div>
  </section>

  <!-- Main Content -->
  <main class="container" style="padding-top: 25px;">
    
    <!-- Disclaimer -->
    <div class="disclaimer-box">
      <strong><i class="fa-solid fa-circle-info" style="color:var(--gold-dark); margin-right: 6px;"></i> Thông Báo Điều Phối Giỏ Hàng:</strong>
      Dự án Saigon Farm Resort hiện đang trong giai đoạn chuẩn bị mở bán chính thức. Nhằm đảm bảo quyền lợi độc quyền và tính công bằng cho các nhà đầu tư sáng lập (Founders), bảng giỏ hàng chỉ cung cấp qua liên kết nội bộ này. Để nhận bảng giá chiết tính chính xác theo từng mã lô và chính sách ưu đãi mở bán, quý khách vui lòng chọn mã căn và bấm "Nhận Báo Giá".
    </div>

    <!-- Controls Panel -->
    <div class="controls-panel">
      <!-- Category Filter Pills -->
      <div class="category-pills">
        <button class="cat-btn active" data-cat="all" onclick="selectCategory('all', this)">
          Tất Cả Sản Phẩm <span class="badge-num">{total_count}</span>
        </button>
        <button class="cat-btn" data-cat="dien-san" onclick="selectCategory('dien-san', this)">
          Điền Sản (1.000m² Ven Hồ) <span class="badge-num">{dien_san_count}</span>
        </button>
        <button class="cat-btn" data-cat="dien-an" onclick="selectCategory('dien-an', this)">
          Điền An (Cụm Lưu Trú Dòng Tiền) <span class="badge-num">{dien_an_count}</span>
        </button>
        <button class="cat-btn" data-cat="biet-phu-dien-trang" onclick="selectCategory('biet-phu-dien-trang', this)">
          Biệt Phủ Điền Trang (Dinh Thự Flagship) <span class="badge-num">{biet_phu_count}</span>
        </button>
      </div>

      <!-- Sub Filters -->
      <div class="sub-filters">
        <div class="filter-group">
          <span class="filter-label">Diện tích:</span>
          <button class="sub-btn active" data-filter="area" data-val="all" onclick="selectAreaFilter('all', this)">Tất Cả</button>
          <button class="sub-btn" data-filter="area" data-val="large" onclick="selectAreaFilter('large', this)">Trên 1.000 m²</button>
          <button class="sub-btn" data-filter="area" data-val="compact" onclick="selectAreaFilter('compact', this)">Dưới 1.000 m²</button>
        </div>

        <div class="filter-group">
          <span class="filter-label">Tình trạng:</span>
          <button class="sub-btn active" data-filter="status" data-val="all" onclick="selectStatusFilter('all', this)">Tất Cả</button>
          <button class="sub-btn" data-filter="status" data-val="available" onclick="selectStatusFilter('available', this)">Còn Hàng</button>
          <button class="sub-btn" data-filter="status" data-val="reserved" onclick="selectStatusFilter('reserved', this)">Đang Giữ Chỗ</button>
        </div>

        <div class="search-input-box">
          <i class="fa-solid fa-magnifying-glass"></i>
          <input type="text" id="searchInput" placeholder="Tìm theo mã lô (A6, A8, B5...)" onkeyup="filterCards()">
        </div>
      </div>
    </div>

    <!-- Active Filter Counter -->
    <div style="margin-bottom: 20px; display: flex; justify-content: space-between; align-items: center;">
      <div style="font-size: 0.92rem; color: #555;">
        Đang hiển thị: <strong id="visibleCount" style="color:var(--primary); font-size: 1.1rem;">{total_count}</strong> sản phẩm phù hợp
      </div>
      <div>
        <a href="gioi-thieu.html#buoc-6-dien-san" style="font-size: 0.88rem; color: var(--gold-dark); text-decoration: underline; font-weight: 700;">
          <i class="fa-solid fa-chart-line"></i> Xem Bài Toán Đầu Tư 1.000 m² Điền Sản (12 Tr/m² → 13,8 Tr/m²)
        </a>
      </div>
    </div>

    <!-- Listings Grid -->
    <div class="listings-grid" id="listingsGrid">
      {cards_rendered}
      
      <!-- No Results Placeholder -->
      <div class="no-results" id="noResults" style="display: none;">
        <i class="fa-solid fa-magnifying-glass"></i>
        <h3 style="font-family: var(--font-serif); margin-bottom: 8px;">Không tìm thấy mã sản phẩm phù hợp</h3>
        <p style="color: #777; font-size: 0.9rem;">Quý khách vui lòng thử tìm kiếm mã khác hoặc đặt lại bộ lọc.</p>
        <button type="button" class="sub-btn" style="margin-top: 14px; padding: 8px 18px;" onclick="resetFilters()">Đặt lại bộ lọc</button>
      </div>
    </div>

  </main>

  <!-- Modal Booking / Nhận Bảng Giá -->
  <div class="modal-backdrop" id="bookingModal">
    <div class="modal-box">
      <button type="button" class="modal-close" onclick="closeBookingModal()">&times;</button>
      <h3 class="modal-title" id="modalTitle">Đăng Ký Nhận Bảng Giá</h3>
      <p class="modal-sub" id="modalSub">Thông tin chiết tính và chính sách ưu đãi mở bán đợt 1 sẽ được gửi trực tiếp đến quý khách.</p>
      
      <form onsubmit="handleFormSubmit(event)">
        <div class="form-group">
          <label>Mã Căn Quan Tâm</label>
          <input type="text" id="formCode" readonly style="background: #faf6ee; font-weight: 700; color: var(--gold-dark);">
        </div>
        <div class="form-group">
          <label>Họ Và Tên</label>
          <input type="text" id="formName" placeholder="Nguyễn Văn A" required>
        </div>
        <div class="form-group">
          <label>Số Điện Thoại / Zalo</label>
          <input type="tel" id="formPhone" placeholder="0909 xxx xxx" required>
        </div>
        <div class="form-group">
          <label>Nhu Cầu Đầu Tư</label>
          <select id="formNeed">
            <option value="Tích sản an toàn ven hồ">Tích sản an toàn ven hồ (Điền Sản)</option>
            <option value="Dòng tiền khai thác lưu trú">Dòng tiền khai thác lưu trú (Điền An)</option>
            <option value="Nghỉ dưỡng gia đình đa thế hệ">Nghỉ dưỡng gia đình đa thế hệ (Biệt Phủ)</option>
            <option value="Cần tư vấn bài toán tài chính">Cần tư vấn bài toán tài chính</option>
          </select>
        </div>
        <button type="submit" class="btn-submit-modal">
          <i class="fa-solid fa-paper-plane" style="margin-right: 6px;"></i> GỬI YÊU CẦU NHẬN BẢNG GIÁ
        </button>
      </form>
    </div>
  </div>

  <!-- Footer -->
  <footer>
    <div class="container">
      <div class="footer-content">
        <div>
          <h4 style="font-family: var(--font-serif); font-size: 1.25rem; color: #fff; margin-bottom: 6px;">SAIGON FARM RESORT</h4>
          <p style="color: #aaa; font-size: 0.84rem;">Quần Thể Nghỉ Dưỡng Sinh Thái Ven Hồ 100ha • Liền Kề Biển Hồ Tràm</p>
          <p style="color: #888; font-size: 0.8rem; margin-top: 4px;">Chủ Đầu Tư: <strong>MDS Living</strong></p>
        </div>
        <div style="display: flex; gap: 20px;">
          <a href="index.html" style="color:#c9a96e; text-decoration:none;">Trang Chủ</a>
          <a href="gioi-thieu.html" style="color:#c9a96e; text-decoration:none;">Bản Giới Thiệu</a>
          <a href="article.html?id=304" style="color:#c9a96e; text-decoration:none;">Đăng Ký Khảo Sát</a>
        </div>
      </div>
      <div class="footer-copy">
        © 2026 Saigon Farm Resort. Bảng giỏ hàng nội bộ phục vụ tư vấn giai đoạn 1. Mọi quyền được bảo lưu.
      </div>
    </div>
  </footer>

  <script>
    let currentCategory = 'all';
    let currentArea = 'all';
    let currentStatus = 'all';

    function selectCategory(cat, btn) {{
      currentCategory = cat;
      document.querySelectorAll('.cat-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      filterCards();
    }}

    function selectAreaFilter(val, btn) {{
      currentArea = val;
      document.querySelectorAll('[data-filter="area"]').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      filterCards();
    }}

    function selectStatusFilter(val, btn) {{
      currentStatus = val;
      document.querySelectorAll('[data-filter="status"]').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      filterCards();
    }}

    function resetFilters() {{
      currentCategory = 'all';
      currentArea = 'all';
      currentStatus = 'all';
      document.getElementById('searchInput').value = '';
      document.querySelectorAll('.cat-btn').forEach((b, i) => b.classList.toggle('active', i === 0));
      document.querySelectorAll('[data-filter="area"]').forEach((b, i) => b.classList.toggle('active', i === 0));
      document.querySelectorAll('[data-filter="status"]').forEach((b, i) => b.classList.toggle('active', i === 0));
      filterCards();
    }}

    function filterCards() {{
      const query = document.getElementById('searchInput').value.trim().toLowerCase();
      const cards = document.querySelectorAll('.listing-card');
      let visibleCount = 0;

      cards.forEach(card => {{
        const cardCat = card.getAttribute('data-category');
        const cardArea = card.getAttribute('data-area-type');
        const cardStatus = card.getAttribute('data-status');
        const cardCode = card.getAttribute('data-code');

        let matchCat = (currentCategory === 'all' || cardCat === currentCategory);
        let matchArea = (currentArea === 'all' || cardArea === currentArea);
        let matchStatus = (currentStatus === 'all' || cardStatus === currentStatus);
        let matchQuery = (!query || cardCode.includes(query));

        if (matchCat && matchArea && matchStatus && matchQuery) {{
          card.style.display = 'flex';
          visibleCount++;
        }} else {{
          card.style.display = 'none';
        }}
      }});

      document.getElementById('visibleCount').textContent = visibleCount;
      const noRes = document.getElementById('noResults');
      if (visibleCount === 0) {{
        noRes.style.display = 'block';
      }} else {{
        noRes.style.display = 'none';
      }}
    }}

    // Modal
    function openBookingModal(code, area, cat) {{
      const modal = document.getElementById('bookingModal');
      document.getElementById('formCode').value = code ? `${{code}} (${{cat}} - ${{area}} m²)` : 'Toàn Bộ Giỏ Hàng Đợt 1';
      document.getElementById('modalTitle').textContent = code ? `Nhận Báo Giá Mã Lô ${{code}}` : 'Nhận Bảng Giá Giỏ Hàng';
      modal.style.display = 'flex';
    }}

    function closeBookingModal() {{
      document.getElementById('bookingModal').style.display = 'none';
    }}

    window.onclick = function(event) {{
      const modal = document.getElementById('bookingModal');
      if (event.target === modal) {{
        closeBookingModal();
      }}
    }}

    function handleFormSubmit(e) {{
      e.preventDefault();
      const name = document.getElementById('formName').value;
      const phone = document.getElementById('formPhone').value;
      const code = document.getElementById('formCode').value;
      const need = document.getElementById('formNeed').value;

      alert(`Cảm ơn Quý khách ${{name}}! Yêu cầu nhận thông tin mã ${{code}} đã được ghi nhận. Chuyên viên tư vấn sẽ liên hệ lại qua SĐT/Zalo: ${{phone}} trong ít phút.`);
      closeBookingModal();
    }}
  </script>
</body>
</html>
"""

    with open("listing.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    print("Generated listing.html successfully!")

    os.makedirs("listing", exist_ok=True)
    with open("listing/index.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    print("Generated listing/index.html successfully!")

if __name__ == "__main__":
    update_listing()
