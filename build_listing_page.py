#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate ultra-luxury listing.html and listing/index.html with:
1. Complete 34 verified products from Original Price Listing
2. Interactive Master Plan (Bản đồ phân lô tương tác) with zoom, pan, hover tooltips & click-to-highlight
3. Dual-view: Card Grid + 11-column Data Table
4. Real-time multi-facet filter & search
5. Interactive booking modal prefilled with lot data
"""

import json
import os

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

def update_listing():
    with open("data/listing_categories.json", "r", encoding="utf-8") as f:
        categories = json.load(f)

    # Flatten items
    all_items = []
    for cat in categories:
        slug = cat.get("slug", "")
        cat_title = cat.get("title", "")
        cat_badge = cat.get("badge", "")
        for item in cat.get("items", []):
            it = dict(item)
            it["category_slug"] = slug
            it["category_title"] = cat_title
            it["category_badge"] = cat_badge
            code = it.get("code", "")
            if code in LOT_COORDINATES:
                it["map_x"] = LOT_COORDINATES[code][0]
                it["map_y"] = LOT_COORDINATES[code][1]
            all_items.append(it)

    # Sort by STT
    all_items.sort(key=lambda x: x.get("stt", 0))

    total_count = len(all_items)
    manor_count = sum(1 for i in all_items if i["category_slug"] == "biet-phu-dien-trang")
    founders_count = sum(1 for i in all_items if i["category_slug"] == "dien-san")
    haven_count = sum(1 for i in all_items if i["category_slug"] == "dien-an")
    available_count = sum(1 for i in all_items if i.get("status_type") == "available")
    reserved_count = sum(1 for i in all_items if i.get("status_type") == "reserved")

    # Generate Map Hotspots
    map_hotspots_html = []
    for item in all_items:
        code = item.get("code", "")
        block = item.get("block", "")
        cat_slug = item.get("category_slug", "")
        cat_title = item.get("category_title", "")
        mx = item.get("map_x", 50.0)
        my = item.get("map_y", 50.0)
        area_str = item.get("area", "")
        pos = item.get("position", "Lô thường")
        direction = item.get("direction", "")
        view = item.get("view", "Garden")
        unit_price_mil = item.get("unit_price_million", "")
        unit_price_str = item.get("unit_price_str", "")
        price_bil = item.get("price_billion", "")
        price_str = item.get("price_str", "")
        status_type = item.get("status_type", "available")
        status_text = item.get("status", "Còn hàng")

        cat_color_class = f"pin-{cat_slug}"
        reserved_class = "pin-reserved" if status_type == "reserved" else ""

        hotspot = f"""
        <div class="map-hotspot {cat_color_class} {reserved_class}"
             id="hotspot-{code.lower()}"
             style="left: {mx}%; top: {my}%;"
             data-code="{code.lower()}"
             data-category="{cat_slug}"
             data-status="{status_type}"
             onclick="focusLot('{code}')">
          <div class="hotspot-pin">
            <span class="pin-code">{code}</span>
            <div class="pin-pulse"></div>
          </div>
          <div class="hotspot-tooltip">
            <div class="tooltip-header">
              <span class="tooltip-code">MÃ CĂN {code}</span>
              <span class="tooltip-status status-{status_type}">{status_text}</span>
            </div>
            <div class="tooltip-cat">{cat_title} · Dãy {block}</div>
            <div class="tooltip-area"><i class="fa-solid fa-ruler-combined"></i> <strong>{area_str}</strong> m² (100% Thổ cư)</div>
            <div class="tooltip-specs">
              <span>{pos}</span> · <span>Hướng {direction}</span> · <span>{view}</span>
            </div>
            <div class="tooltip-price-row">
              <div class="tooltip-price-val">{price_bil}</div>
              <div class="tooltip-unit-val">{unit_price_mil}</div>
            </div>
            <div class="tooltip-action-row">
              <button type="button" class="btn-tooltip-booking" onclick="event.stopPropagation(); openBookingModal('{code}', '{cat_title}', '{area_str}', '{unit_price_str}', '{price_str}', '{price_bil}')">
                <i class="fa-solid fa-file-invoice-dollar"></i> Nhận Báo Giá
              </button>
            </div>
          </div>
        </div>
        """
        map_hotspots_html.append(hotspot)

    map_hotspots_rendered = "\n".join(map_hotspots_html)

    # Generate Cards HTML
    cards_html = []
    for item in all_items:
        code = item.get("code", "")
        block = item.get("block", "")
        stt = item.get("stt", 0)
        area_str = item.get("area", "")
        area_val = item.get("area_val", 1000.0)
        pos = item.get("position", "Lô thường")
        view = item.get("view", "Garden")
        amenity = item.get("amenity", "Bình thường")
        road = item.get("road", "Đường nội bộ")
        direction = item.get("direction", "")
        unit_price = item.get("unit_price", 0)
        unit_price_str = item.get("unit_price_str", "")
        unit_price_mil = item.get("unit_price_million", "")
        price = item.get("price", 0)
        price_str = item.get("price_str", "")
        price_bil = item.get("price_billion", "")
        status_type = item.get("status_type", "available")
        status_text = item.get("status", "Còn hàng")
        features = item.get("features", "")
        suitable_for = item.get("suitable_for", "")
        img = item.get("image", "/assets/Index_asset/Phoicanh_3D_Tien_ich/Tong_the/S01_Final_Fix.jpg")
        if img and not img.startswith('/') and not img.startswith('http'):
            img = '/' + img
        cat_slug = item.get("category_slug", "")
        cat_title = item.get("category_title", "")

        status_class = "status-available" if status_type == "available" else "status-reserved"
        status_icon = "fa-circle-check" if status_type == "available" else "fa-clock"

        pos_badge = ""
        if pos == "Lô góc":
            pos_badge = '<span class="badge-chip badge-gold"><i class="fa-solid fa-gem"></i> Lô Góc</span>'
        elif pos == "2 MT":
            pos_badge = '<span class="badge-chip badge-purple"><i class="fa-solid fa-arrows-split-up-and-left"></i> 2 Mặt Tiền</span>'

        view_badge = ""
        if view == "Lúa":
            view_badge = '<span class="badge-chip badge-amber"><i class="fa-solid fa-wheat-awn"></i> View Đồng Lúa</span>'
        else:
            view_badge = '<span class="badge-chip badge-green"><i class="fa-solid fa-leaf"></i> View Garden</span>'

        amenity_badge = ""
        if amenity == "Clubhouse":
            amenity_badge = '<span class="badge-chip badge-blue"><i class="fa-solid fa-spa"></i> Kề Clubhouse</span>'
        elif amenity == "Công viên cảnh quan":
            amenity_badge = '<span class="badge-chip badge-blue"><i class="fa-solid fa-tree"></i> Kề Công Viên</span>'

        # Policy note per collection
        if cat_slug == "dien-san":
            policy_html = """
            <div class="card-policy-box policy-founders">
              <i class="fa-solid fa-gift"></i>
              <span><strong>CS Mở Bán:</strong> Ưu đãi TT sớm 70% giảm <strong>800Tr</strong> · TT sớm 100% giảm <strong>1 Tỷ</strong> · Giãn 30% tới cuối 2027 0% lãi</span>
            </div>
            """
        elif cat_slug == "dien-an":
            policy_html = """
            <div class="card-policy-box policy-haven">
              <i class="fa-solid fa-hand-holding-dollar"></i>
              <span><strong>Dòng Tiền:</strong> Cam kết thuê tối thiểu <strong>80 Tr/tháng</strong> (từ 20 phòng) · MDS Living vận hành phòng bổ sung</span>
            </div>
            """
        else:
            policy_html = """
            <div class="card-policy-box policy-manor">
              <i class="fa-solid fa-crown"></i>
              <span><strong>Đặc Quyền:</strong> Dinh thự ven hồ · 150 đêm nghỉ dưỡng + 215 đêm chia sẻ 50% doanh thu cùng MDS Living</span>
            </div>
            """

        card = f"""
        <div class="listing-card"
             id="card-{code.lower()}"
             onclick="openBookingModal('{code}', '{cat_title}', '{area_str}', '{unit_price_str}', '{price_str}', '{price_bil}')"
             data-stt="{stt}"
             data-code="{code.lower()}"
             data-block="{block.lower()}"
             data-category="{cat_slug}"
             data-area="{area_val}"
             data-pos="{pos}"
             data-view="{view}"
             data-amenity="{amenity}"
             data-road="{road}"
             data-direction="{direction}"
             data-unit-price="{unit_price}"
             data-price="{price}"
             data-status="{status_type}"
             onmouseenter="highlightHotspot('{code.lower()}')"
             onmouseleave="unhighlightHotspot('{code.lower()}')">
          <div class="card-thumb-wrap">
            <img src="{img}" 
                 alt="Mã căn {code} - {cat_title}" 
                 loading="lazy" 
                 class="card-thumb" 
                 onerror="this.onerror=null; this.src='/assets/Index_asset/Phoicanh_3D_Tien_ich/Tong_the/S01_Final_Fix.jpg'">
            <span class="card-badge-code">MÃ {code}</span>
            <span class="card-badge-cat">{cat_title}</span>
            <span class="card-badge-status {status_class}">
              <i class="fa-solid {status_icon}"></i> {status_text}
            </span>
          </div>
          <div class="card-body">
            <div class="card-top-info">
              <div class="card-area-box">
                <span class="area-label"><i class="fa-solid fa-ruler-combined"></i> Diện tích đất</span>
                <span class="area-val"><strong>{area_str}</strong> m²</span>
              </div>
              <div class="card-legal-pill">
                <i class="fa-solid fa-shield-halved"></i> 100% Sổ Riêng
              </div>
            </div>

            <h4 class="card-title">Căn {code} · Dãy {block} ({direction})</h4>
            <div class="card-mobile-meta"><span class="cm-tag">{pos}</span> • <span class="cm-tag">{road}</span></div>

            <!-- Specs Grid -->
            <div class="card-specs-grid">
              <div class="spec-item">
                <span class="spec-label">Vị trí</span>
                <span class="spec-val"><strong>{pos}</strong></span>
              </div>
              <div class="spec-item">
                <span class="spec-label">Hướng</span>
                <span class="spec-val"><strong>{direction}</strong></span>
              </div>
              <div class="spec-item">
                <span class="spec-label">Mặt đường</span>
                <span class="spec-val"><strong>{road}</strong></span>
              </div>
              <div class="spec-item">
                <span class="spec-label">Cảnh quan</span>
                <span class="spec-val"><strong>{view}</strong></span>
              </div>
            </div>

            <!-- Chips tags -->
            <div class="card-chips-row">
              {pos_badge}
              {view_badge}
              {amenity_badge}
            </div>

            <!-- Description -->
            <p class="card-features"><strong>Đặc tính:</strong> {features}</p>
            <div class="card-fit">
              <i class="fa-regular fa-compass"></i>
              <span><strong>Phù hợp:</strong> {suitable_for}</span>
            </div>

            {policy_html}

            <!-- Price Block -->
            <div class="card-price-section">
              <div class="price-header-row">
                <span class="price-type-tag">GIÁ GỐC NIÊM YẾT ĐỢT 1</span>
                <span class="unit-price-tag">Đơn giá: <strong>{unit_price_mil}</strong></span>
              </div>
              <div class="price-main-row">
                <div class="price-display">
                  <span class="price-billion">{price_bil}</span>
                  <span class="price-exact">({price_str})</span>
                </div>
                <span class="price-note-badge">Trước CSBH & Ưu Đãi</span>
              </div>
            </div>

            <!-- Footer Action -->
            <div class="card-actions">
              <button type="button" class="btn-primary-action" onclick="event.stopPropagation(); openBookingModal('{code}', '{cat_title}', '{area_str}', '{unit_price_str}', '{price_str}', '{price_bil}')">
                <i class="fa-solid fa-file-invoice-dollar"></i> Chi tiết
              </button>
              <button type="button" class="btn-view-map-action" onclick="event.stopPropagation(); locateOnMap('{code}')" title="Định vị lô {code} trên bản đồ">
                <i class="fa-solid fa-map-location-dot"></i>
              </button>
              <a href="tel:0909000712" onclick="event.stopPropagation()" class="btn-call-action" title="Gọi 0909 000 712 kiểm tra lô {code}">
                <i class="fa-solid fa-phone"></i>
              </a>
              <a href="https://zalo.me/0909000712" onclick="event.stopPropagation()" target="_blank" class="btn-zalo-action" title="Nhắn Zalo 0909 000 712 khóa cọc lô {code}">
                <i class="fa-solid fa-comment-dots"></i>
              </a>
            </div>
          </div>
        </div>
        """
        cards_html.append(card)

    cards_rendered = "\n".join(cards_html)

    # Generate Table Rows HTML
    table_rows_html = []
    for item in all_items:
        stt = item.get("stt", 0)
        code = item.get("code", "")
        block = item.get("block", "")
        cat_slug = item.get("category_slug", "")
        cat_title = item.get("category_title", "")
        area_str = item.get("area", "")
        area_val = item.get("area_val", 1000.0)
        pos = item.get("position", "Lô thường")
        view = item.get("view", "Garden")
        amenity = item.get("amenity", "Bình thường")
        road = item.get("road", "Đường nội bộ")
        direction = item.get("direction", "")
        unit_price = item.get("unit_price", 0)
        unit_price_str = item.get("unit_price_str", "")
        unit_price_mil = item.get("unit_price_million", "")
        price = item.get("price", 0)
        price_str = item.get("price_str", "")
        price_bil = item.get("price_billion", "")
        status_type = item.get("status_type", "available")
        status_text = item.get("status", "Còn hàng")

        status_class = "status-available" if status_type == "available" else "status-reserved"

        row = f"""
        <tr class="table-row-item"
            id="row-{code.lower()}"
            data-stt="{stt}"
            data-code="{code.lower()}"
            data-block="{block.lower()}"
            data-category="{cat_slug}"
            data-area="{area_val}"
            data-pos="{pos}"
            data-view="{view}"
            data-amenity="{amenity}"
            data-road="{road}"
            data-direction="{direction}"
            data-unit-price="{unit_price}"
            data-price="{price}"
            data-status="{status_type}"
            onmouseenter="highlightHotspot('{code.lower()}')"
            onmouseleave="unhighlightHotspot('{code.lower()}')">
          <td class="col-stt">{stt}</td>
          <td class="col-block"><strong>{block}</strong></td>
          <td class="col-code"><span class="table-code-badge" onclick="locateOnMap('{code}')" style="cursor:pointer;" title="Bấm để xem trên bản đồ">{code} <i class="fa-solid fa-location-crosshairs" style="font-size:0.7rem; margin-left:3px;"></i></span></td>
          <td class="col-cat"><span class="cat-pill cat-{cat_slug}">{cat_title}</span></td>
          <td class="col-area"><strong>{area_str}</strong> m²</td>
          <td class="col-pos">{pos}</td>
          <td class="col-dir">{direction}</td>
          <td class="col-view">{view}</td>
          <td class="col-amenity">{amenity}</td>
          <td class="col-road">{road}</td>
          <td class="col-unit-price"><span class="unit-p-text">{unit_price_str}</span></td>
          <td class="col-total-price">
            <strong class="price-bil-text">{price_bil}</strong>
            <span class="price-full-sub">{price_str}</span>
          </td>
          <td class="col-status"><span class="table-status-pill {status_class}">{status_text}</span></td>
          <td class="col-action">
            <div style="display:flex; gap:6px; align-items:center;">
              <button type="button" class="btn-table-action" onclick="openBookingModal('{code}', '{cat_title}', '{area_str}', '{unit_price_str}', '{price_str}', '{price_bil}')" title="Nhận bảng tính & CSBH">
                <i class="fa-solid fa-file-invoice-dollar"></i> Báo Giá
              </button>
              <a href="tel:0909000712" class="btn-table-call" title="Gọi 0909 000 712 check căn {code}">
                <i class="fa-solid fa-phone"></i>
              </a>
              <a href="https://zalo.me/0909000712" target="_blank" class="btn-table-zalo" title="Zalo 0909 000 712 khóa cọc {code}">
                <i class="fa-solid fa-comment-dots"></i>
              </a>
            </div>
          </td>
        </tr>
        """
        table_rows_html.append(row)

    table_rows_rendered = "\n".join(table_rows_html)

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
  <!-- SFR Real-Time Visitor Live Tracker -->
  <script defer src="/js/sfr-tracker.js"></script>

  <meta charset="utf-8"/>
  <base href="/">
  <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
  <title>Giỏ Hàng & Bảng Giá Mở Bán Đợt 1 | Saigon Farm Resort</title>
  <meta content="Bản đồ mặt bằng tương tác và giỏ hàng 34 sản phẩm mở bán Đợt 1 tại Saigon Farm Resort: Biệt Phủ Điền Trang, Điền Sản và Điền An. Xem vị trí thực địa, đơn giá và giá niêm yết gốc (Original Price Listing) trực tiếp từ Chủ đầu tư MDS Living." name="description"/>
  <meta name="keywords" content="mặt bằng saigon farm resort, sơ đồ phân lô saigon farm resort, giỏ hàng saigon farm resort, bảng giá saigon farm resort, biệt phủ điền trang, điền sản mds living, điền an lưu trú"/>
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1"/>
  <link rel="canonical" href="https://saigonfarmresort.com/giohang">
  <link rel="icon" type="image/x-icon" href="/assets/Index_asset/LOGO_PNG/LOGO_SGF_3_BROWN.png">

  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://saigonfarmresort.com/giohang">
  <meta property="og:title" content="Giỏ Hàng & Bảng Giá Mở Bán Đợt 1 | Saigon Farm Resort">
  <meta property="og:description" content="34 sản phẩm đất nền biệt phủ & điền trang sinh thái ven hồ 100ha. Bản đồ phân lô tương tác và bảng giá niêm yết gốc từ Chủ đầu tư MDS Living.">
  <meta property="og:image" content="https://saigonfarmresort.com/assets/Index_asset/masterplan_tmb_sales.webp">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Giỏ Hàng & Mặt Bằng Phân Lô Tương Tác | Saigon Farm Resort">
  <meta name="twitter:description" content="34 sản phẩm đất nền biệt phủ & điền trang sinh thái ven hồ 100ha.">
  <meta name="twitter:image" content="https://saigonfarmresort.com/assets/Index_asset/masterplan_tmb_sales.webp">

  <!-- Fonts & Icons -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;0,900;1,400&family=Montserrat:wght@300;400;500;600;700;800&family=Outfit:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css"/>

  <!-- Structured Data JSON-LD -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "CollectionPage",
        "@id": "https://saigonfarmresort.com/listing.html#webpage",
        "url": "https://saigonfarmresort.com/listing.html",
        "name": "Giỏ Hàng & Mặt Bằng Phân Lô Tương Tác Saigon Farm Resort",
        "description": "Bản đồ phân lô tương tác và bảng hàng nội bộ mở bán đợt 1 các dòng sản phẩm Biệt Phủ Điền Trang, Điền Sản và Điền An.",
        "breadcrumb": {{
          "@type": "BreadcrumbList",
          "itemListElement": [
            {{
              "@type": "ListItem",
              "position": 1,
              "name": "Trang Chủ",
              "item": "https://saigonfarmresort.com/"
            }},
            {{
              "@type": "ListItem",
              "position": 2,
              "name": "Giỏ Hàng & Mặt Bằng Tương Tác",
              "item": "https://saigonfarmresort.com/listing.html"
            }}
          ]
        }}
      }}
    ]
  }}
  </script>

  <style>
    :root {{
      --primary: #183024;
      --primary-dark: #0f1f17;
      --primary-light: #2c4d3b;
      --gold: #c9a96e;
      --gold-dark: #8c6b32;
      --gold-light: #f4ecdc;
      --cream: #fdfaf4;
      --bg-soft: #f8f6f0;
      --border-color: #ebdcc5;
      --text-dark: #1f2421;
      --text-muted: #666e68;
      --color-manor: #c9a96e;
      --color-founders: #10b981;
      --color-haven: #0284c7;
      --font-serif: 'Playfair Display', serif;
      --font-sans: 'Montserrat', sans-serif;
      --font-display: 'Outfit', sans-serif;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: var(--font-sans);
      color: var(--text-dark);
      background-color: var(--bg-soft);
      line-height: 1.6;
      -webkit-font-smoothing: antialiased;
    }}

    /* Top utility bar */
    .topbar {{
      background: var(--primary-dark);
      color: #dfd7cc;
      font-size: 0.8rem;
      padding: 8px 20px;
      border-bottom: 1px solid rgba(201,169,110,0.25);
    }}
    .topbar-container {{
      max-width: 1360px;
      margin: 0 auto;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 10px;
    }}
    .topbar-left {{
      display: flex;
      align-items: center;
      gap: 16px;
    }}
    .topbar-left span {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }}
    .topbar-right {{
      display: flex;
      align-items: center;
      gap: 18px;
    }}
    .topbar-right a {{
      color: #dfd7cc;
      text-decoration: none;
      transition: color 0.2s;
    }}
    .topbar-right a:hover {{
      color: var(--gold);
    }}

    /* Header Nav */
    .navbar {{
      position: sticky;
      top: 0;
      z-index: 100;
      background: rgba(255,255,255,0.98);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      border-bottom: 1px solid var(--border-color);
      box-shadow: 0 4px 20px rgba(0,0,0,0.03);
    }}
    .nav-container {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 12px 24px;
      max-width: 1360px;
      margin: 0 auto;
    }}
    .nav-brand {{
      display: flex;
      align-items: center;
      gap: 14px;
      text-decoration: none;
    }}
    .nav-brand img {{
      height: 44px;
      width: auto;
      object-fit: contain;
    }}
    .nav-brand-text {{
      display: flex;
      flex-direction: column;
    }}
    .nav-brand-title {{
      font-family: var(--font-serif);
      font-size: 1.25rem;
      font-weight: 700;
      color: var(--primary);
      letter-spacing: 0.5px;
    }}
    .nav-brand-sub {{
      font-size: 0.74rem;
      color: var(--gold-dark);
      font-weight: 600;
      letter-spacing: 1px;
      text-transform: uppercase;
    }}
    .nav-links {{
      display: flex;
      align-items: center;
      gap: 22px;
      list-style: none;
    }}
    .nav-links a {{
      color: var(--text-dark);
      text-decoration: none;
      font-size: 0.9rem;
      font-weight: 600;
      transition: all 0.2s ease;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }}
    .nav-links a:hover, .nav-links a.active {{
      color: var(--gold-dark);
    }}
    .nav-cta {{
      background: linear-gradient(135deg, var(--gold-dark), var(--gold));
      color: #ffffff !important;
      padding: 9px 18px;
      border-radius: 6px;
      font-weight: 700 !important;
      box-shadow: 0 3px 10px rgba(140,107,50,0.25);
    }}
    .nav-cta:hover {{
      opacity: 0.95;
      transform: translateY(-1px);
    }}

    /* Hero Section - Luxury Vietnamese Heritage Cream */
    .listing-hero {{
      background: linear-gradient(180deg, #fdfbf7 0%, #f7f2e9 50%, #f0e7db 100%);
      color: var(--text-dark);
      padding: 50px 24px 46px;
      position: relative;
      border-bottom: 1.5px solid #dfc89f;
      overflow: hidden;
    }}
    .hero-watermark-layer {{
      position: absolute;
      inset: 0;
      pointer-events: none;
      overflow: hidden;
      z-index: 0;
    }}
    .wm-hero-drum {{
      position: absolute;
      top: -100px;
      right: -60px;
      width: 460px;
      height: 460px;
      background: url('/assets/patterns/gold_dong_son_drum.png') no-repeat center;
      background-size: contain;
      opacity: 0.12;
      transform: rotate(-12deg);
    }}
    .wm-hero-lotus-left {{
      position: absolute;
      bottom: -30px;
      left: -30px;
      width: 250px;
      height: 250px;
      background: url('/assets/patterns/gold_lotus.webp') no-repeat left bottom;
      background-size: contain;
      opacity: 0.15;
    }}
    .wm-hero-pavilion-right {{
      position: absolute;
      bottom: -10px;
      right: 40px;
      width: 280px;
      height: 230px;
      background: url('/assets/patterns/gold_estate_pavilion.webp') no-repeat right bottom;
      background-size: contain;
      opacity: 0.12;
    }}
    .wm-hero-cloud {{
      position: absolute;
      top: 30px;
      left: 12%;
      width: 220px;
      height: 110px;
      background: url('/assets/patterns/gold_auspicious_cloud.png') no-repeat center;
      background-size: contain;
      opacity: 0.14;
    }}
    .hero-container {{
      max-width: 1360px;
      margin: 0 auto;
      position: relative;
      z-index: 1;
    }}
    .breadcrumbs {{
      font-size: 0.82rem;
      color: #7d6f5d;
      margin-bottom: 12px;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .breadcrumbs a {{
      color: var(--gold-dark);
      text-decoration: none;
      font-weight: 600;
    }}
    .breadcrumbs a:hover {{
      color: var(--primary);
      text-decoration: underline;
    }}
    .hero-title-wrap {{
      margin-bottom: 18px;
    }}
    .hero-tag-badge {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: #faf4e8;
      color: #8c6b32;
      border: 1px solid #dfc89f;
      padding: 6px 14px;
      border-radius: 30px;
      font-size: 0.78rem;
      font-weight: 700;
      letter-spacing: 0.6px;
      margin-bottom: 12px;
      text-transform: uppercase;
      box-shadow: 0 2px 8px rgba(140, 107, 50, 0.08);
    }}
    .hero-title {{
      font-family: var(--font-serif);
      font-size: 2.45rem;
      font-weight: 700;
      line-height: 1.25;
      color: var(--primary);
      margin-bottom: 12px;
      letter-spacing: -0.5px;
    }}
    .hero-sub {{
      font-size: 1.05rem;
      color: #3b4d42;
      max-width: 920px;
      line-height: 1.65;
    }}

    /* Notice Banner: Original Price Listing (Thư thông báo CĐT) */
    .notice-original-price {{
      background: #ffffff;
      border: 1.5px solid #dfc89f;
      border-left: 4px solid var(--gold-dark);
      border-radius: 12px;
      padding: 20px 24px;
      margin-top: 24px;
      box-shadow: 0 8px 24px rgba(140, 107, 50, 0.08);
      display: flex;
      gap: 18px;
      align-items: flex-start;
    }}
    .notice-icon {{
      font-size: 1.7rem;
      color: var(--gold-dark);
      flex-shrink: 0;
      margin-top: 2px;
    }}
    .notice-text {{
      font-size: 0.88rem;
      color: #2c3931;
      line-height: 1.65;
    }}
    .notice-text strong {{
      color: var(--primary);
    }}
    .notice-text p {{
      margin: 4px 0 8px;
    }}
    .notice-text ul {{
      margin-top: 6px;
      margin-left: 18px;
    }}
    .notice-text li {{
      margin-bottom: 5px;
    }}

    /* Stat Cards Row */
    .hero-stats-grid {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 16px;
      margin-top: 26px;
    }}
    .stat-pill {{
      background: #ffffff;
      border: 1.5px solid #e5dcce;
      border-radius: 12px;
      padding: 16px 20px;
      display: flex;
      flex-direction: column;
      gap: 4px;
      box-shadow: 0 4px 16px rgba(24, 48, 36, 0.04);
      transition: transform 0.25s, box-shadow 0.25s, border-color 0.25s;
    }}
    .stat-pill:hover {{
      transform: translateY(-3px);
      box-shadow: 0 10px 24px rgba(140, 107, 50, 0.12);
      border-color: var(--gold);
    }}
    .stat-pill-label {{
      font-size: 0.74rem;
      color: #7d6f5d;
      text-transform: uppercase;
      letter-spacing: 0.6px;
      font-weight: 700;
    }}
    .stat-pill-val {{
      font-family: var(--font-serif);
      font-size: 1.65rem;
      font-weight: 800;
      color: var(--primary);
    }}
    .stat-pill-sub {{
      font-size: 0.74rem;
      color: var(--gold-dark);
      font-weight: 600;
    }}

    /* Main Container */
    .main-content {{
      max-width: 1360px;
      margin: 0 auto;
      padding: 35px 20px 80px;
    }}

    /* ==============================================================
       INTERACTIVE MASTER PLAN SECTION
       ============================================================== */
    .masterplan-interactive-section {{
      background: #ffffff;
      border: 1px solid var(--border-color);
      border-radius: 14px;
      padding: 24px;
      margin-bottom: 40px;
      box-shadow: 0 6px 24px rgba(0,0,0,0.05);
    }}
    .map-header {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      flex-wrap: wrap;
      gap: 16px;
      margin-bottom: 18px;
      padding-bottom: 16px;
      border-bottom: 1px solid #f0e7d8;
    }}
    .map-title-group h2 {{
      font-family: var(--font-serif);
      font-size: 1.6rem;
      color: var(--primary);
      margin-bottom: 6px;
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    .map-title-group p {{
      font-size: 0.9rem;
      color: var(--text-muted);
    }}
    .map-legend-group {{
      display: flex;
      align-items: center;
      flex-wrap: wrap;
      gap: 12px;
    }}
    .legend-item {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-size: 0.8rem;
      font-weight: 600;
      padding: 5px 10px;
      border-radius: 4px;
    }}
    .legend-dot {{
      width: 12px;
      height: 12px;
      border-radius: 50%;
    }}
    .legend-manor {{ background: #fbf7ee; color: #8c6b32; border: 1px solid #edd9b5; }}
    .legend-manor .legend-dot {{ background: #c9a96e; }}
    .legend-founders {{ background: #ecfdf5; color: #047857; border: 1px solid #a7f3d0; }}
    .legend-founders .legend-dot {{ background: #10b981; }}
    .legend-haven {{ background: #eff6ff; color: #1d4ed8; border: 1px solid #bfdbfe; }}
    .legend-haven .legend-dot {{ background: #0284c7; }}
    .legend-reserved {{ background: #fff7ed; color: #c2410c; border: 1px solid #fed7aa; }}
    .legend-reserved .legend-dot {{ background: #f97316; }}

    /* Map Viewer Container with Pan/Zoom */
    .map-viewport {{
      position: relative;
      width: 100%;
      height: 720px;
      background: #08140e;
      border-radius: 12px;
      overflow: hidden;
      border: 1px solid #ded6c5;
      user-select: none;
      cursor: grab;
    }}
    .map-viewport:active {{
      cursor: grabbing;
    }}
    .map-canvas {{
      position: absolute;
      top: 0;
      left: 0;
      transform-origin: 0 0;
      will-change: transform;
      transition: none;
    }}
    .map-canvas.smooth-anim {{
      transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    .map-stage {{
      position: relative;
      width: 2560px;
      height: 1918px;
      display: block;
    }}
    .map-image {{
      width: 100%;
      height: 100%;
      display: block;
      pointer-events: none;
      user-select: none;
    }}

    /* Map Floating Controls */
    .map-controls-floating {{
      position: absolute;
      right: 18px;
      bottom: 18px;
      display: flex;
      flex-direction: column;
      gap: 6px;
      z-index: 20;
    }}
    .map-ctrl-btn {{
      width: 38px;
      height: 38px;
      background: rgba(255,255,255,0.95);
      border: 1px solid #ded6c5;
      border-radius: 6px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1rem;
      color: var(--primary);
      cursor: pointer;
      box-shadow: 0 4px 10px rgba(0,0,0,0.15);
      transition: all 0.2s;
    }}
    .map-ctrl-btn:hover {{
      background: var(--gold);
      color: #fff;
      border-color: var(--gold);
    }}
    .map-hint-badge {{
      position: absolute;
      left: 18px;
      bottom: 18px;
      background: rgba(15, 31, 23, 0.85);
      backdrop-filter: blur(4px);
      color: #dfd7cc;
      font-size: 0.78rem;
      padding: 6px 12px;
      border-radius: 20px;
      border: 1px solid rgba(201,169,110,0.3);
      z-index: 20;
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    /* Hotspot Marker / Pin */
    .map-hotspot {{
      position: absolute;
      transform: translate(-50%, -50%);
      cursor: pointer;
      z-index: 5;
      transition: transform 0.2s, z-index 0.2s;
    }}
    .map-hotspot:hover, .map-hotspot.highlighted {{
      z-index: 50;
      transform: translate(-50%, -50%) scale(1.25);
    }}
    .hotspot-pin {{
      position: relative;
      padding: 6px 12px;
      border-radius: 6px;
      font-family: var(--font-display);
      font-size: 15px;
      font-weight: 800;
      letter-spacing: 0.5px;
      color: #ffffff;
      box-shadow: 0 4px 12px rgba(0,0,0,0.4);
      white-space: nowrap;
      display: flex;
      align-items: center;
      justify-content: center;
      border: 1.5px solid rgba(255,255,255,0.85);
    }}
    .pin-biet-phu-dien-trang .hotspot-pin {{
      background: linear-gradient(135deg, #a88448, #c9a96e);
    }}
    .pin-dien-san .hotspot-pin {{
      background: linear-gradient(135deg, #059669, #10b981);
    }}
    .pin-dien-an .hotspot-pin {{
      background: linear-gradient(135deg, #0284c7, #38bdf8);
    }}
    .pin-reserved .hotspot-pin {{
      border: 2px solid #ea580c !important;
      box-shadow: 0 0 10px rgba(234, 88, 12, 0.8);
    }}
    .pin-pulse {{
      position: absolute;
      top: -4px;
      left: -4px;
      right: -4px;
      bottom: -4px;
      border-radius: 6px;
      border: 2px solid var(--gold);
      opacity: 0;
      pointer-events: none;
      animation: pinPulseAnim 2s infinite;
    }}
    .pin-reserved .pin-pulse {{
      border-color: #f97316;
    }}
    @keyframes pinPulseAnim {{
      0% {{ transform: scale(0.95); opacity: 0.8; }}
      70% {{ transform: scale(1.4); opacity: 0; }}
      100% {{ transform: scale(1.4); opacity: 0; }}
    }}

    /* Hotspot Tooltip Card */
    .hotspot-tooltip {{
      position: absolute;
      bottom: calc(100% + 14px);
      left: 50%;
      transform: translateX(-50%);
      width: 270px;
      background: #ffffff;
      border: 1px solid var(--border-color);
      border-radius: 10px;
      padding: 14px 16px;
      box-shadow: 0 12px 36px rgba(0,0,0,0.3);
      pointer-events: none;
      opacity: 0;
      visibility: hidden;
      transition: opacity 0.2s, visibility 0.2s, transform 0.2s;
      z-index: 100;
    }}
    .hotspot-tooltip::after {{
      content: '';
      position: absolute;
      top: 100%;
      left: 50%;
      transform: translateX(-50%);
      border-width: 6px;
      border-style: solid;
      border-color: #ffffff transparent transparent transparent;
    }}
    .map-hotspot:hover .hotspot-tooltip,
    .map-hotspot.highlighted .hotspot-tooltip {{
      opacity: 1;
      visibility: visible;
      pointer-events: auto;
      transform: translateX(-50%) translateY(-2px);
    }}
    .tooltip-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 4px;
    }}
    .tooltip-code {{
      font-family: var(--font-serif);
      font-weight: 800;
      color: var(--primary);
      font-size: 0.95rem;
    }}
    .tooltip-status {{
      font-size: 0.68rem;
      font-weight: 700;
      padding: 2px 6px;
      border-radius: 10px;
    }}
    .tooltip-cat {{
      font-size: 0.76rem;
      color: var(--gold-dark);
      font-weight: 700;
      margin-bottom: 6px;
    }}
    .tooltip-area {{
      font-size: 0.8rem;
      color: #333;
      margin-bottom: 4px;
    }}
    .tooltip-specs {{
      font-size: 0.72rem;
      color: #666;
      margin-bottom: 8px;
      padding-bottom: 6px;
      border-bottom: 1px dashed #eee;
    }}
    .tooltip-price-row {{
      display: flex;
      justify-content: space-between;
      align-items: baseline;
      margin-bottom: 8px;
    }}
    .tooltip-price-val {{
      font-family: var(--font-display);
      font-size: 1.1rem;
      font-weight: 800;
      color: #b91c1c;
    }}
    .tooltip-unit-val {{
      font-size: 0.72rem;
      color: #555;
    }}
    .btn-tooltip-booking {{
      width: 100%;
      background: var(--primary);
      color: #ffffff;
      border: none;
      padding: 6px 10px;
      border-radius: 4px;
      font-size: 0.76rem;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
    }}
    .btn-tooltip-booking:hover {{
      background: var(--gold-dark);
    }}

    /* Control Toolbar (Search, Filter, View Switch) */
    .control-toolbar {{
      background: #ffffff;
      border: 1px solid var(--border-color);
      border-radius: 12px;
      padding: 20px;
      margin-bottom: 30px;
      box-shadow: 0 4px 16px rgba(0,0,0,0.04);
    }}
    .toolbar-row-top {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 16px;
      margin-bottom: 18px;
      padding-bottom: 16px;
      border-bottom: 1px solid #f0e7d8;
    }}
    .search-box-wrap {{
      position: relative;
      flex: 1;
      min-width: 280px;
      max-width: 460px;
    }}
    .search-box-wrap i {{
      position: absolute;
      left: 14px;
      top: 50%;
      transform: translateY(-50%);
      color: #888;
      font-size: 0.9rem;
    }}
    .search-input {{
      width: 100%;
      padding: 10px 14px 10px 38px;
      border: 1px solid #dcd3c2;
      border-radius: 25px;
      font-size: 0.88rem;
      outline: none;
      font-family: inherit;
      transition: all 0.2s;
    }}
    .search-input:focus {{
      border-color: var(--gold-dark);
      box-shadow: 0 0 0 3px rgba(201,169,110,0.18);
    }}

    /* View Switcher */
    .view-switcher {{
      display: inline-flex;
      background: #f1ebd8;
      border-radius: 8px;
      padding: 4px;
      gap: 4px;
    }}
    .view-btn {{
      border: none;
      background: transparent;
      padding: 8px 16px;
      border-radius: 6px;
      font-size: 0.85rem;
      font-weight: 700;
      color: var(--text-dark);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s;
    }}
    .view-btn.active {{
      background: var(--primary);
      color: #ffffff;
      box-shadow: 0 2px 8px rgba(24,48,36,0.2);
    }}

    /* Category Filter Pills */
    .category-pills {{
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin-bottom: 16px;
    }}
    .cat-btn {{
      background: #f8f6f0;
      border: 1px solid #ded6c5;
      padding: 8px 18px;
      border-radius: 25px;
      font-size: 0.86rem;
      font-weight: 600;
      color: var(--text-dark);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s;
    }}
    .cat-btn:hover {{
      background: #f0e8d6;
      border-color: var(--gold);
    }}
    .cat-btn.active {{
      background: var(--primary);
      color: #fff;
      border-color: var(--primary);
    }}
    .cat-count-badge {{
      background: rgba(0,0,0,0.08);
      font-size: 0.72rem;
      padding: 2px 7px;
      border-radius: 12px;
      margin-left: 4px;
    }}
    .cat-btn.active .cat-count-badge {{
      background: rgba(255,255,255,0.22);
      color: #fff;
    }}

    /* Filters Row 2 */
    .filters-row-secondary {{
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 14px;
    }}
    .filter-dropdowns-group {{
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      align-items: center;
    }}
    .select-filter {{
      padding: 7px 12px;
      border: 1px solid #ded6c5;
      border-radius: 6px;
      background: #ffffff;
      font-size: 0.82rem;
      color: var(--text-dark);
      font-weight: 500;
      outline: none;
      cursor: pointer;
      font-family: inherit;
    }}
    .select-filter:focus {{
      border-color: var(--gold-dark);
    }}

    .sort-group {{
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .sort-label {{
      font-size: 0.82rem;
      color: var(--text-muted);
      font-weight: 600;
    }}

    /* Results summary */
    .results-summary-bar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 20px;
      font-size: 0.88rem;
      color: var(--text-muted);
    }}
    .results-count strong {{
      color: var(--primary);
    }}

    /* Card Grid View */
    .listings-grid {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 26px;
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
      transition: transform 0.25s, box-shadow 0.25s, border-color 0.25s;
    }}
    .listing-card:hover, .listing-card.card-highlighted {{
      transform: translateY(-4px);
      box-shadow: 0 12px 30px rgba(0,0,0,0.08);
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
      background: rgba(15, 31, 23, 0.94);
      color: #fff;
      font-size: 0.8rem;
      font-weight: 800;
      padding: 5px 12px;
      border-radius: 4px;
      letter-spacing: 0.5px;
      border: 1px solid rgba(201, 169, 110, 0.5);
    }}
    .card-badge-cat {{
      position: absolute;
      bottom: 12px;
      left: 12px;
      background: rgba(255,255,255,0.92);
      color: var(--primary);
      font-size: 0.74rem;
      font-weight: 700;
      padding: 4px 10px;
      border-radius: 4px;
      box-shadow: 0 2px 6px rgba(0,0,0,0.1);
    }}
    .card-badge-status {{
      position: absolute;
      top: 12px;
      right: 12px;
      font-size: 0.74rem;
      font-weight: 700;
      padding: 4px 11px;
      border-radius: 20px;
      display: inline-flex;
      align-items: center;
      gap: 5px;
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
    .card-top-info {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 10px;
    }}
    .card-area-box {{
      display: flex;
      flex-direction: column;
    }}
    .area-label {{
      font-size: 0.72rem;
      color: #777;
      text-transform: uppercase;
    }}
    .area-val {{
      font-size: 1.15rem;
      color: var(--primary);
    }}
    .area-val strong {{
      font-size: 1.3rem;
      font-weight: 800;
      color: var(--gold-dark);
    }}
    .card-legal-pill {{
      font-size: 0.76rem;
      background: #e8f5e9;
      color: #2e7d32;
      padding: 4px 8px;
      border-radius: 4px;
      font-weight: 600;
    }}

    .card-title {{
      font-family: var(--font-serif);
      font-size: 1.25rem;
      color: #1a1a1a;
      margin-bottom: 12px;
      font-weight: 700;
    }}

    /* Specs 4-cell Grid */
    .card-specs-grid {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 8px;
      background: #fdfbf7;
      border: 1px solid #ebdcc5;
      border-radius: 6px;
      padding: 10px;
      margin-bottom: 12px;
    }}
    .spec-item {{
      display: flex;
      flex-direction: column;
    }}
    .spec-label {{
      font-size: 0.7rem;
      color: #888;
      text-transform: uppercase;
    }}
    .spec-val {{
      font-size: 0.84rem;
      color: var(--primary);
    }}

    /* Chips row */
    .card-chips-row {{
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      margin-bottom: 12px;
    }}
    .badge-chip {{
      font-size: 0.72rem;
      font-weight: 600;
      padding: 3px 8px;
      border-radius: 4px;
      display: inline-flex;
      align-items: center;
      gap: 4px;
    }}
    .badge-gold {{
      background: #fbf4e6;
      color: #8c6b32;
      border: 1px solid #ecd8b4;
    }}
    .badge-purple {{
      background: #f3e8ff;
      color: #6b21a8;
      border: 1px solid #e9d5ff;
    }}
    .badge-green {{
      background: #ecfdf5;
      color: #047857;
      border: 1px solid #a7f3d0;
    }}
    .badge-amber {{
      background: #fffbeb;
      color: #b45309;
      border: 1px solid #fde68a;
    }}
    .badge-blue {{
      background: #eff6ff;
      color: #1d4ed8;
      border: 1px solid #bfdbfe;
    }}

    .card-features {{
      font-size: 0.84rem;
      color: #555;
      line-height: 1.5;
      margin-bottom: 10px;
      min-height: 42px;
    }}
    .card-fit {{
      font-size: 0.82rem;
      color: #333;
      background: #faf6ee;
      padding: 8px 12px;
      border-radius: 6px;
      margin-bottom: 12px;
      border: 1px dashed #ebdcc5;
      display: flex;
      align-items: flex-start;
      gap: 6px;
    }}
    .card-fit i {{
      color: var(--gold-dark);
      margin-top: 3px;
    }}

    /* Policy Box */
    .card-policy-box {{
      font-size: 0.78rem;
      padding: 8px 10px;
      border-radius: 6px;
      margin-bottom: 16px;
      display: flex;
      align-items: flex-start;
      gap: 8px;
      line-height: 1.45;
    }}
    .card-policy-box i {{
      margin-top: 2px;
      font-size: 0.85rem;
    }}
    .policy-founders {{
      background: #fdf5ea;
      color: #8c6b32;
      border: 1px solid #ebd8b5;
    }}
    .policy-haven {{
      background: #edf7ff;
      color: #155e75;
      border: 1px solid #bae6fd;
    }}
    .policy-manor {{
      background: #fbf7ee;
      color: #78350f;
      border: 1px solid #fde68a;
    }}

    /* Price Section on Card */
    .card-price-section {{
      margin-top: auto;
      background: #fdfaf4;
      border: 1px solid #e7dac5;
      border-radius: 8px;
      padding: 12px 14px;
      margin-bottom: 14px;
    }}
    .price-header-row {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 6px;
    }}
    .price-type-tag {{
      font-size: 0.68rem;
      font-weight: 700;
      color: #8c6b32;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}
    .unit-price-tag {{
      font-size: 0.78rem;
      color: #555;
    }}
    .unit-price-tag strong {{
      color: var(--primary);
    }}
    .price-main-row {{
      display: flex;
      justify-content: space-between;
      align-items: baseline;
      flex-wrap: wrap;
      gap: 6px;
    }}
    .price-display {{
      display: flex;
      align-items: baseline;
      gap: 6px;
    }}
    .price-billion {{
      font-family: var(--font-display);
      font-size: 1.45rem;
      font-weight: 800;
      color: #b91c1c;
      letter-spacing: -0.5px;
    }}
    .price-exact {{
      font-size: 0.78rem;
      color: #777;
    }}
    .price-note-badge {{
      font-size: 0.7rem;
      background: #fee2e2;
      color: #991b1b;
      padding: 2px 6px;
      border-radius: 4px;
      font-weight: 600;
    }}

    /* Card Actions */
    .card-actions {{
      display: flex;
      gap: 8px;
    }}
    .btn-primary-action {{
      flex: 1;
      background: var(--primary);
      color: #ffffff;
      border: none;
      padding: 11px 16px;
      border-radius: 6px;
      font-size: 0.88rem;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      transition: background 0.2s;
    }}
    .btn-primary-action:hover {{
      background: var(--gold-dark);
    }}
    .btn-view-map-action {{
      width: 44px;
      height: 44px;
      background: #fdfaf4;
      border: 1px solid #ded6c5;
      color: var(--primary);
      border-radius: 6px;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      font-size: 1.05rem;
      transition: all 0.2s;
    }}
    .btn-view-map-action:hover {{
      background: var(--primary);
      color: #fff;
      border-color: var(--primary);
    }}
    .btn-call-action {{
      width: 44px;
      height: 44px;
      background: #fdfaf4;
      border: 1px solid #ded6c5;
      color: var(--primary);
      border-radius: 6px;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      text-decoration: none;
      font-size: 1rem;
      transition: all 0.2s;
    }}
    .btn-call-action:hover {{
      background: var(--gold);
      color: #fff;
      border-color: var(--gold);
    }}

    /* Table View Styles */
    .table-view-container {{
      display: none;
      background: #ffffff;
      border: 1px solid var(--border-color);
      border-radius: 12px;
      overflow: hidden;
      box-shadow: 0 4px 16px rgba(0,0,0,0.04);
      margin-bottom: 50px;
    }}
    .table-responsive {{
      overflow-x: auto;
      max-width: 100%;
    }}
    .inventory-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.84rem;
      white-space: nowrap;
    }}
    .inventory-table th {{
      background: #183024;
      color: #ffffff;
      font-weight: 700;
      padding: 14px 12px;
      text-align: left;
      font-size: 0.78rem;
      letter-spacing: 0.5px;
      text-transform: uppercase;
      position: sticky;
      top: 0;
      z-index: 10;
    }}
    .inventory-table td {{
      padding: 12px 14px;
      border-bottom: 1px solid #f0e9dc;
      color: var(--text-dark);
    }}
    .inventory-table tbody tr:hover, .inventory-table tbody tr.row-highlighted {{
      background-color: #faf6ee;
    }}
    .table-code-badge {{
      background: #183024;
      color: #ffffff;
      font-weight: 800;
      padding: 3px 8px;
      border-radius: 4px;
      font-size: 0.8rem;
    }}
    .cat-pill {{
      font-size: 0.74rem;
      font-weight: 700;
      padding: 3px 8px;
      border-radius: 4px;
    }}
    .cat-biet-phu-dien-trang {{
      background: #fbf4e6;
      color: #8c6b32;
    }}
    .cat-dien-san {{
      background: #edf7ee;
      color: #2e7d32;
    }}
    .cat-dien-an {{
      background: #e8f4fd;
      color: #0284c7;
    }}
    .table-status-pill {{
      font-size: 0.72rem;
      font-weight: 700;
      padding: 3px 8px;
      border-radius: 12px;
      display: inline-block;
    }}
    .price-bil-text {{
      color: #b91c1c;
      font-size: 0.95rem;
      display: block;
    }}
    .price-full-sub {{
      font-size: 0.72rem;
      color: #777;
      display: block;
    }}
    .btn-table-action {{
      background: var(--primary);
      color: #ffffff;
      border: none;
      padding: 6px 12px;
      border-radius: 4px;
      font-size: 0.76rem;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 4px;
      transition: background 0.2s;
    }}
    .btn-table-action:hover {{
      background: var(--gold-dark);
    }}

    /* Empty state */
    .no-results-box {{
      display: none;
      text-align: center;
      padding: 60px 20px;
      background: #ffffff;
      border: 1px dashed var(--border-color);
      border-radius: 12px;
      margin-bottom: 50px;
    }}
    .no-results-box i {{
      font-size: 3rem;
      color: #ccc;
      margin-bottom: 14px;
    }}
    .no-results-box h3 {{
      font-family: var(--font-serif);
      font-size: 1.4rem;
      margin-bottom: 8px;
    }}

    /* Booking Modal */
    .modal-overlay {{
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: rgba(0,0,0,0.65);
      backdrop-filter: blur(4px);
      z-index: 1000;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 20px;
    }}
    .modal-card {{
      background: #ffffff;
      border-radius: 12px;
      max-width: 540px;
      width: 100%;
      overflow: hidden;
      box-shadow: 0 20px 50px rgba(0,0,0,0.3);
      animation: modalFadeIn 0.3s ease;
    }}
    @keyframes modalFadeIn {{
      from {{ opacity: 0; transform: scale(0.95); }}
      to {{ opacity: 1; transform: scale(1); }}
    }}
    .modal-header {{
      background: var(--primary);
      color: #ffffff;
      padding: 18px 22px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .modal-header h3 {{
      font-family: var(--font-serif);
      font-size: 1.25rem;
      color: #ffffff;
    }}
    .modal-close-btn {{
      background: transparent;
      border: none;
      color: #ffffff;
      font-size: 1.2rem;
      cursor: pointer;
    }}
    .modal-body {{
      padding: 22px;
    }}
    .modal-lot-preview {{
      background: #fdfaf4;
      border: 1px solid #eedec7;
      border-radius: 8px;
      padding: 12px 16px;
      margin-bottom: 18px;
    }}
    .mlp-title {{
      font-size: 0.88rem;
      font-weight: 700;
      color: var(--primary);
      margin-bottom: 4px;
    }}
    .mlp-details {{
      font-size: 0.8rem;
      color: #666;
    }}
    .mlp-price {{
      font-size: 1.15rem;
      font-weight: 800;
      color: #b91c1c;
      margin-top: 4px;
    }}

    .form-group {{
      margin-bottom: 14px;
    }}
    .form-group label {{
      display: block;
      font-size: 0.82rem;
      font-weight: 700;
      color: var(--text-dark);
      margin-bottom: 6px;
    }}
    .form-control {{
      width: 100%;
      padding: 10px 14px;
      border: 1px solid #dcd3c2;
      border-radius: 6px;
      font-size: 0.88rem;
      outline: none;
      font-family: inherit;
    }}
    .form-control:focus {{
      border-color: var(--gold-dark);
    }}
    .modal-submit-btn {{
      width: 100%;
      background: linear-gradient(135deg, var(--gold-dark), var(--gold));
      color: #ffffff;
      border: none;
      padding: 12px;
      border-radius: 6px;
      font-size: 0.95rem;
      font-weight: 700;
      cursor: pointer;
      margin-top: 10px;
    }}
    .modal-submit-btn:hover {{
      opacity: 0.95;
    }}

    /* Footer */
    .site-footer {{
      background: var(--primary-dark);
      color: #dfd7cc;
      padding: 50px 20px 25px;
      border-top: 3px solid var(--gold);
    }}
    .footer-container {{
      max-width: 1360px;
      margin: 0 auto;
      display: grid;
      grid-template-columns: 2fr 1fr 1fr 1fr;
      gap: 30px;
      margin-bottom: 40px;
    }}
    .footer-col h4 {{
      font-family: var(--font-serif);
      font-size: 1.1rem;
      color: var(--gold);
      margin-bottom: 14px;
    }}
    .footer-col ul {{
      list-style: none;
    }}
    .footer-col li {{
      margin-bottom: 8px;
    }}
    .footer-col a {{
      color: #dfd7cc;
      text-decoration: none;
      font-size: 0.85rem;
      transition: color 0.2s;
    }}
    .footer-col a:hover {{
      color: var(--gold);
    }}
    .footer-bottom {{
      max-width: 1360px;
      margin: 0 auto;
      border-top: 1px solid rgba(255,255,255,0.1);
      padding-top: 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 12px;
      font-size: 0.8rem;
      color: #999;
    }}

    /* View Switcher */
    .view-switcher {{
      display: inline-flex;
      background: #f1ebd8;
      border-radius: 8px;
      padding: 4px;
      gap: 4px;
    }}
    .view-btn {{
      border: none;
      background: transparent;
      padding: 7px 12px;
      border-radius: 6px;
      font-size: 0.82rem;
      font-weight: 700;
      color: var(--text-dark);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s;
    }}
    .view-btn.active {{
      background: var(--primary);
      color: #ffffff;
      box-shadow: 0 2px 8px rgba(24,48,36,0.2);
    }}
    .view-btn.active i {{
      color: var(--gold);
    }}

    /* List mode (Compact Rows) */
    .listings-grid.view-list-mode {{
      display: flex !important;
      flex-direction: column !important;
      gap: 12px !important;
    }}
    .listings-grid.view-list-mode .listing-card {{
      display: flex !important;
      flex-direction: row !important;
      align-items: stretch !important;
      border-radius: 10px;
      cursor: pointer;
    }}
    .listings-grid.view-list-mode .card-thumb-wrap {{
      width: 130px !important;
      min-width: 130px !important;
      height: auto !important;
      min-height: 110px !important;
    }}
    .listings-grid.view-list-mode .card-body {{
      padding: 10px 14px !important;
      flex: 1;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }}
    .listings-grid.view-list-mode .card-specs-grid,
    .listings-grid.view-list-mode .card-features,
    .listings-grid.view-list-mode .card-fit,
    .listings-grid.view-list-mode .card-policy-box,
    .listings-grid.view-list-mode .card-chips-row {{
      display: none !important;
    }}
    .listings-grid.view-list-mode .card-price-section {{
      padding: 4px 8px !important;
      margin: 4px 0 !important;
      background: transparent !important;
      border: none !important;
    }}
    .listings-grid.view-list-mode .card-actions {{
      display: flex !important;
      gap: 8px !important;
      align-items: center !important;
    }}
    .listings-grid.view-list-mode .btn-primary-action {{
      padding: 7px 12px !important;
      font-size: 0.78rem !important;
    }}

    .card-mobile-meta {{
      display: none;
    }}

    /* Mobile Fixed Bottom Dock */
    .mobile-bottom-dock {{
      display: none;
    }}

    /* Tablet Responsive */
    @media (max-width: 1100px) {{
      .listings-grid:not(.view-list-mode) {{
        grid-template-columns: repeat(2, 1fr);
      }}
      .hero-stats-grid {{
        grid-template-columns: repeat(2, 1fr);
      }}
      .footer-container {{
        grid-template-columns: 1fr 1fr;
      }}
      .map-viewport {{
        height: 520px;
      }}
    }}

    /* Mobile Responsive (Super Friendly & Square Grid) */
    @media (max-width: 768px) {{
      body {{
        padding-bottom: 75px !important;
      }}
      .nav-links {{
        display: none;
      }}
      .hero-title {{
        font-size: 1.6rem !important;
      }}
      .hero-stats-grid {{
        grid-template-columns: repeat(2, 1fr) !important;
        gap: 8px !important;
      }}
      .stat-pill {{
        padding: 10px 12px !important;
      }}
      .stat-pill-val {{
        font-size: 1.3rem !important;
      }}
      .footer-container {{
        grid-template-columns: 1fr;
      }}
      .toolbar-row-top {{
        flex-direction: column;
        align-items: stretch;
        gap: 10px;
      }}
      .search-box-wrap {{
        max-width: 100%;
      }}
      .map-viewport {{
        height: 380px;
      }}
      .map-header {{
        flex-direction: column;
        gap: 10px;
      }}
      .floating-sales-cta {{
        display: none !important;
      }}

      /* Fixed bottom dock */
      .mobile-bottom-dock {{
        display: flex !important;
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        background: rgba(15, 31, 23, 0.98);
        backdrop-filter: blur(14px);
        -webkit-backdrop-filter: blur(14px);
        padding: 8px 12px;
        gap: 8px;
        z-index: 9999;
        box-shadow: 0 -4px 20px rgba(0,0,0,0.3);
        border-top: 1px solid rgba(201,169,110,0.4);
        padding-bottom: max(8px, env(safe-area-inset-bottom));
      }}
      .dock-btn {{
        flex: 1;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        gap: 6px;
        padding: 11px 8px;
        border-radius: 8px;
        font-size: 0.84rem;
        font-weight: 700;
        text-decoration: none;
      }}
      .dock-btn-call {{
        background: linear-gradient(135deg, #c9a96e, #a88448);
        color: #183024;
      }}
      .dock-btn-zalo {{
        background: #0068FF;
        color: #ffffff;
      }}

      /* Category Pills Touch Carousel */
      .category-pills {{
        display: flex !important;
        flex-wrap: nowrap !important;
        overflow-x: auto !important;
        -webkit-overflow-scrolling: touch;
        gap: 8px !important;
        padding: 4px 0 8px !important;
        margin-bottom: 10px !important;
        scrollbar-width: none;
      }}
      .category-pills::-webkit-scrollbar {{
        display: none;
      }}
      .cat-btn {{
        flex-shrink: 0 !important;
        padding: 7px 14px !important;
        font-size: 0.8rem !important;
        white-space: nowrap !important;
      }}

      /* Filter Dropdowns Horizontal Strip */
      .filters-row-secondary {{
        flex-direction: column !important;
        align-items: stretch !important;
        gap: 8px !important;
      }}
      .filter-dropdowns-group {{
        display: flex !important;
        flex-wrap: nowrap !important;
        overflow-x: auto !important;
        -webkit-overflow-scrolling: touch;
        gap: 6px !important;
        padding-bottom: 6px !important;
        width: 100% !important;
        scrollbar-width: none;
      }}
      .filter-dropdowns-group::-webkit-scrollbar {{
        display: none;
      }}
      .select-filter {{
        flex-shrink: 0 !important;
        padding: 6px 10px !important;
        font-size: 0.78rem !important;
        background-color: #ffffff;
        border: 1px solid #dcd3c2;
      }}
      .sort-group {{
        justify-content: flex-end;
      }}
      .sort-group select {{
        font-size: 0.78rem;
        padding: 6px 10px;
      }}

      /* 2-Column Square Grid on Mobile ("Hàng ngang ô vuông") */
      .listings-grid:not(.view-list-mode) {{
        grid-template-columns: repeat(2, 1fr) !important;
        gap: 10px !important;
        margin-bottom: 25px !important;
      }}
      .listings-grid:not(.view-list-mode) .listing-card {{
        border-radius: 10px !important;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05) !important;
        display: flex !important;
        flex-direction: column !important;
        cursor: pointer;
        transition: transform 0.2s;
      }}
      .listings-grid:not(.view-list-mode) .listing-card:active {{
        transform: scale(0.98);
      }}
      .listings-grid:not(.view-list-mode) .card-thumb-wrap {{
        height: 120px !important;
        position: relative;
      }}
      .listings-grid:not(.view-list-mode) .card-badge-code {{
        top: 6px !important;
        left: 6px !important;
        font-size: 0.7rem !important;
        padding: 3px 6px !important;
        font-weight: 800;
        letter-spacing: 0;
      }}
      .listings-grid:not(.view-list-mode) .card-badge-cat {{
        bottom: 6px !important;
        left: 6px !important;
        font-size: 0.62rem !important;
        padding: 2px 6px !important;
      }}
      .listings-grid:not(.view-list-mode) .card-badge-status {{
        top: 6px !important;
        right: 6px !important;
        font-size: 0.62rem !important;
        padding: 2px 6px !important;
      }}
      .listings-grid:not(.view-list-mode) .card-body {{
        padding: 8px !important;
        display: flex;
        flex-direction: column;
        flex: 1;
      }}
      .listings-grid:not(.view-list-mode) .card-top-info {{
        margin-bottom: 4px !important;
      }}
      .listings-grid:not(.view-list-mode) .area-label {{
        display: none !important;
      }}
      .listings-grid:not(.view-list-mode) .area-val {{
        font-size: 0.95rem !important;
        font-weight: 800;
        color: var(--primary);
      }}
      .listings-grid:not(.view-list-mode) .area-val strong {{
        font-size: 1.05rem !important;
        color: var(--gold-dark);
      }}
      .listings-grid:not(.view-list-mode) .card-legal-pill {{
        display: none !important;
      }}
      .listings-grid:not(.view-list-mode) .card-title {{
        font-size: 0.84rem !important;
        font-weight: 700 !important;
        margin-bottom: 4px !important;
        line-height: 1.3 !important;
        white-space: nowrap !important;
        overflow: hidden !important;
        text-overflow: ellipsis !important;
      }}
      .card-mobile-meta {{
        display: flex !important;
        align-items: center;
        gap: 4px;
        font-size: 0.68rem;
        color: var(--text-muted);
        margin-bottom: 4px;
      }}
      .cm-tag {{
        background: #f4ecdc;
        padding: 1px 5px;
        border-radius: 3px;
        font-weight: 600;
        color: #7d6f5d;
      }}

      /* Hide dense text fields on 2-col mobile cards so they stay neat and square */
      .listings-grid:not(.view-list-mode) .card-specs-grid,
      .listings-grid:not(.view-list-mode) .card-features,
      .listings-grid:not(.view-list-mode) .card-fit,
      .listings-grid:not(.view-list-mode) .card-policy-box,
      .listings-grid:not(.view-list-mode) .card-chips-row {{
        display: none !important;
      }}
      /* Compact Price box */
      .listings-grid:not(.view-list-mode) .card-price-section {{
        padding: 6px 8px !important;
        margin-top: auto !important;
        margin-bottom: 6px !important;
        border-radius: 6px !important;
        background: #fdfaf4 !important;
      }}
      .listings-grid:not(.view-list-mode) .price-type-tag,
      .listings-grid:not(.view-list-mode) .price-exact,
      .listings-grid:not(.view-list-mode) .price-note-badge {{
        display: none !important;
      }}
      .listings-grid:not(.view-list-mode) .unit-price-tag {{
        font-size: 0.68rem !important;
        color: #777;
      }}
      .listings-grid:not(.view-list-mode) .price-billion {{
        font-size: 1.12rem !important;
        font-weight: 800 !important;
        color: #b91c1c !important;
      }}
      /* Dual Quick Action Buttons on 2-col card */
      .listings-grid:not(.view-list-mode) .card-actions {{
        display: grid !important;
        grid-template-columns: 1fr 1fr !important;
        gap: 6px !important;
      }}
      .listings-grid:not(.view-list-mode) .btn-primary-action,
      .listings-grid:not(.view-list-mode) .btn-view-map-action {{
        display: none !important;
      }}
      .listings-grid:not(.view-list-mode) .btn-call-action {{
        width: 100% !important;
        height: 32px !important;
        border-radius: 5px !important;
        background: #183024 !important;
        color: #ffffff !important;
        font-size: 0.74rem !important;
        font-weight: 700 !important;
        display: inline-flex !important;
        align-items: center !important;
        justify-content: center !important;
        gap: 4px !important;
        text-decoration: none !important;
        border: none !important;
      }}
      .listings-grid:not(.view-list-mode) .btn-call-action::after {{
        content: "Gọi";
      }}
      .listings-grid:not(.view-list-mode) .btn-zalo-action {{
        width: 100% !important;
        height: 32px !important;
        border-radius: 5px !important;
        background: #0068FF !important;
        color: #ffffff !important;
        font-size: 0.74rem !important;
        font-weight: 700 !important;
        display: inline-flex !important;
        align-items: center !important;
        justify-content: center !important;
        gap: 4px !important;
        text-decoration: none !important;
        border: none !important;
      }}
      .listings-grid:not(.view-list-mode) .btn-zalo-action::after {{
        content: "Zalo";
      }}

      /* Mobile Modal Polish */
      .modal-overlay {{
        padding: 10px;
        align-items: flex-end;
      }}
      .modal-card {{
        max-height: 88vh;
        overflow-y: auto;
        border-radius: 16px 16px 0 0;
      }}
      .modal-body {{
        padding: 16px;
      }}
      .form-group {{
        margin-bottom: 10px;
      }}
      .form-control {{
        padding: 8px 12px;
        font-size: 0.85rem;
      }}
    }}

    /* Lock Deposit Banner */
    .lock-deposit-banner {{
      background: linear-gradient(135deg, #183024 0%, #102219 100%);
      border: 1.5px solid var(--gold);
      border-radius: 12px;
      padding: 20px 24px;
      margin-bottom: 24px;
      box-shadow: 0 8px 24px rgba(24, 48, 36, 0.25);
      position: relative;
      overflow: hidden;
    }}
    .lock-deposit-banner::before {{
      content: "";
      position: absolute;
      top: -30px;
      right: -30px;
      width: 140px;
      height: 140px;
      border-radius: 50%;
      background: radial-gradient(circle, rgba(201,169,110,0.18) 0%, transparent 70%);
      pointer-events: none;
    }}
    .lock-deposit-badge {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: rgba(201, 169, 110, 0.2);
      color: var(--gold-light);
      border: 1px solid rgba(201, 169, 110, 0.4);
      padding: 4px 12px;
      border-radius: 20px;
      font-size: 0.74rem;
      font-weight: 800;
      letter-spacing: 0.5px;
      margin-bottom: 12px;
      text-transform: uppercase;
    }}
    .lock-deposit-grid {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 18px;
    }}
    .lock-deposit-text {{
      flex: 1;
      min-width: 280px;
    }}
    .lock-deposit-text h3 {{
      font-family: var(--font-serif);
      font-size: 1.3rem;
      color: #ffffff;
      margin: 0 0 6px;
      display: flex;
      align-items: center;
      flex-wrap: wrap;
      gap: 8px;
    }}
    .lock-deposit-text h3 span {{
      color: var(--gold-light);
      font-family: var(--font-display);
      font-weight: 800;
      letter-spacing: 0.5px;
    }}
    .lock-deposit-text p {{
      color: #dfd7cc;
      font-size: 0.88rem;
      line-height: 1.55;
      margin: 0;
    }}
    .lock-deposit-cta-group {{
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
    }}
    .btn-lock-phone {{
      background: var(--gold);
      color: #183024;
      font-weight: 700;
      font-size: 0.9rem;
      padding: 12px 22px;
      border-radius: 30px;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: all 0.25s ease;
      box-shadow: 0 4px 14px rgba(201, 169, 110, 0.35);
    }}
    .btn-lock-phone:hover {{
      background: var(--gold-light);
      transform: translateY(-2px);
      box-shadow: 0 6px 18px rgba(201, 169, 110, 0.45);
    }}
    .btn-lock-zalo {{
      background: #0068FF;
      color: #ffffff;
      font-weight: 700;
      font-size: 0.9rem;
      padding: 12px 22px;
      border-radius: 30px;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: all 0.25s ease;
      box-shadow: 0 4px 14px rgba(0, 104, 255, 0.35);
    }}
    .btn-lock-zalo:hover {{
      background: #0056d6;
      transform: translateY(-2px);
      box-shadow: 0 6px 18px rgba(0, 104, 255, 0.45);
    }}

    /* Card Zalo Action Button */
    .btn-zalo-action {{
      width: 44px;
      height: 44px;
      background: #eff6ff;
      border: 1px solid #bfdbfe;
      color: #0068FF;
      border-radius: 6px;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      text-decoration: none;
      font-size: 1.05rem;
      transition: all 0.2s;
    }}
    .btn-zalo-action:hover {{
      background: #0068FF;
      color: #ffffff;
      border-color: #0068FF;
    }}

    /* Table Quick Call/Zalo Buttons */
    .btn-table-call {{
      width: 32px;
      height: 32px;
      background: #fdfaf4;
      border: 1px solid #ded6c5;
      color: var(--primary);
      border-radius: 4px;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      text-decoration: none;
      font-size: 0.85rem;
      transition: all 0.2s;
    }}
    .btn-table-call:hover {{
      background: var(--gold);
      color: #fff;
    }}
    .btn-table-zalo {{
      width: 32px;
      height: 32px;
      background: #eff6ff;
      border: 1px solid #bfdbfe;
      color: #0068FF;
      border-radius: 4px;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      text-decoration: none;
      font-size: 0.9rem;
      transition: all 0.2s;
    }}
    .btn-table-zalo:hover {{
      background: #0068FF;
      color: #fff;
    }}

    /* Modal Direct Lock Callout */
    .modal-direct-lock {{
      background: #faf4e8;
      border: 1px solid #dfc89f;
      border-radius: 8px;
      padding: 12px 14px;
      margin-bottom: 16px;
    }}
    .mdl-title {{
      font-size: 0.82rem;
      font-weight: 700;
      color: #183024;
      margin-bottom: 8px;
    }}
    .mdl-actions {{
      display: flex;
      gap: 10px;
      flex-wrap: wrap;
    }}
    .btn-mdl-call {{
      flex: 1;
      background: #183024;
      color: #fff;
      font-weight: 700;
      font-size: 0.84rem;
      padding: 8px 12px;
      border-radius: 6px;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
    }}
    .btn-mdl-zalo {{
      flex: 1;
      background: #0068FF;
      color: #fff;
      font-weight: 700;
      font-size: 0.84rem;
      padding: 8px 12px;
      border-radius: 6px;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
    }}

    /* Floating Sales CTA */
    .floating-sales-cta {{
      position: fixed;
      bottom: 24px;
      right: 24px;
      z-index: 999;
      display: flex;
      flex-direction: column;
      gap: 10px;
    }}
    .float-sales-btn {{
      display: inline-flex;
      align-items: center;
      gap: 10px;
      padding: 11px 18px;
      border-radius: 30px;
      font-size: 0.86rem;
      font-weight: 700;
      text-decoration: none;
      box-shadow: 0 6px 20px rgba(0,0,0,0.22);
      transition: all 0.25s ease;
      border: 1.5px solid rgba(255,255,255,0.25);
    }}
    .float-sales-btn.float-call {{
      background: linear-gradient(135deg, #183024 0%, #102219 100%);
      color: #f7eedc;
      border-color: #c9a96e;
    }}
    .float-sales-btn.float-call i {{
      color: #c9a96e;
      font-size: 1.05rem;
    }}
    .float-sales-btn.float-call:hover {{
      transform: translateY(-2px);
      background: #c9a96e;
      color: #183024;
    }}
    .float-sales-btn.float-call:hover i {{
      color: #183024;
    }}
    .float-sales-btn.float-zalo {{
      background: #0068FF;
      color: #ffffff;
      border-color: #60a5fa;
    }}
    .float-sales-btn.float-zalo:hover {{
      transform: translateY(-2px);
      background: #0056d6;
    }}
    @media (max-width: 640px) {{
      .floating-sales-cta {{
        bottom: 16px;
        right: 14px;
      }}
      .float-sales-btn {{
        padding: 9px 14px;
        font-size: 0.8rem;
      }}
    }}

  </style>
</head>
<body>

  <!-- Top bar -->
  <div class="topbar">
    <div class="topbar-container">
      <div class="topbar-left">
        <span><i class="fa-solid fa-location-dot" style="color:var(--gold);"></i> Xã Đất Đỏ, TP. Hồ Chí Minh</span>
        <span><i class="fa-solid fa-shield-halved" style="color:#4ade80;"></i> Sổ đỏ thổ cư 100% từng nền</span>
      </div>
      <div class="topbar-right">
        <a href="tel:0909000712" style="font-weight:700; color:#fff; background:rgba(201,169,110,0.22); padding:3px 10px; border-radius:14px; border:1px solid rgba(201,169,110,0.5);"><i class="fa-solid fa-phone-volume" style="color:var(--gold);"></i> Check Căn: 0909 000 712</a>
        <a href="https://zalo.me/0909000712" target="_blank" style="font-weight:700; color:#0068FF; background:#fff; padding:3px 10px; border-radius:14px;"><i class="fa-solid fa-comment-dots"></i> Zalo Khóa Cọc</a>
        <a href="gioithieu"><i class="fa-solid fa-book-open"></i> Bản Giới Thiệu (Pitch Deck)</a>
      </div>
    </div>
  </div>

  <!-- Navbar -->
  <header class="navbar">
    <div class="nav-container">
      <a href="giohang.html" class="nav-brand">
        <img src="/assets/Index_asset/LOGO_PNG/LOGO_SGF_3_BROWN.png" alt="Saigon Farm Resort Logo">
        <div class="nav-brand-text">
          <span class="nav-brand-title">SAIGON FARM RESORT</span>
          <span class="nav-brand-sub">Quần Thể Điền Trang Sinh Thái Ven Hồ</span>
        </div>
      </a>
      <ul class="nav-links">
        <li><a href="#interactive-masterplan"><i class="fa-solid fa-map-location-dot"></i> Bản Đồ Phân Lô</a></li>
        <li><a href="biet-phu-dien-trang.html">Biệt Phủ Điền Trang</a></li>
        <li><a href="dien-san.html">Điền Sản</a></li>
        <li><a href="dien-an.html">Điền An</a></li>
        <li><a href="giohang.html" class="active"><i class="fa-solid fa-cart-shopping" style="color:var(--gold-dark);"></i> Giỏ Hàng Mở Bán</a></li>
        <li><a href="javascript:void(0)" onclick="openBookingModal('TƯ VẤN CHUNG', 'Đợt 1', '', '', '', '')" class="nav-cta"><i class="fa-solid fa-paper-plane"></i> Nhận Báo Giá Đợt 1</a></li>
      </ul>
    </div>
  </header>

  <!-- Hero Section -->
  <section class="listing-hero">
    <!-- Vietnamese Heritage Watermark Layer -->
    <div class="hero-watermark-layer">
      <div class="wm-hero-drum"></div>
      <div class="wm-hero-lotus-left"></div>
      <div class="wm-hero-pavilion-right"></div>
      <div class="wm-hero-cloud"></div>
    </div>

    <div class="hero-container">
      <div class="breadcrumbs">
        <span><i class="fa-solid fa-layer-group"></i> Quần Thể Saigon Farm Resort</span>
        <i class="fa-solid fa-chevron-right" style="font-size:0.7rem;"></i>
        <span style="color:var(--primary); font-weight:700;">Giỏ Hàng & Bảng Giá Mở Bán Đợt 1</span>
      </div>

      <div class="hero-title-wrap">
        <div class="hero-tag-badge">
          <i class="fa-solid fa-bullhorn"></i> Quỹ Hàng Trực Tiếp Từ Chủ Đầu Tư MDS Living
        </div>
        <h1 class="hero-title">BẢNG HÀNG & GIỎ HÀNG MỞ BÁN ĐỢT 1</h1>
        <p class="hero-sub">
          Cập nhật thông tin chi tiết mã căn, diện tích, vị trí, hướng, view, đơn giá và giá bán niêm yết của 34 sản phẩm đất nền nghỉ dưỡng ven hồ 100ha tại Saigon Farm Resort.
        </p>
      </div>

      <!-- Notice Banner for Original Price Listing -->
      <div class="notice-original-price">
        <i class="fa-solid fa-circle-exclamation notice-icon"></i>
        <div class="notice-text">
          <strong>LƯU Ý VỀ GIÁ NIÊM YẾT GỐC (ORIGINAL PRICE LISTING):</strong>
          <p>Bảng giá dưới đây là <strong>Giá Niêm Yết Công Bố Trước Chính Sách Bán Hàng</strong> của Chủ đầu tư. Khách hàng giao dịch trong Đợt 1 sẽ được áp dụng các chính sách ưu đãi đặc quyền:</p>
          <ul>
            <li><strong>Điền Sản (11 nền):</strong> Thanh toán sớm 70% giảm ngay <strong>800 Triệu</strong> · Thanh toán 100% giảm <strong>1 Tỷ đồng</strong> · Giữ lại 30% CĐT hỗ trợ ra hàng hoặc giãn thanh toán tới cuối 2027 với lãi suất 0%.</li>
            <li><strong>Điền An (7 cụm):</strong> Hợp đồng thuê dài hạn từ MDS Living, cam kết thuê tối thiểu <strong>80 Tr/tháng (960 Tr/năm)</strong> với cụm từ 20 phòng trở lên.</li>
            <li><strong>Biệt Phủ Điền Trang (16 dinh thự):</strong> MDS Living cam kết mua lại 90 - 150 đêm lưu trú/năm hoặc khai thác chia sẻ 50% doanh thu.</li>
          </ul>
        </div>
      </div>

      <!-- Sales Lock Deposit Callout Banner -->
      <div class="lock-deposit-banner">
        <div class="lock-deposit-badge">
          <i class="fa-solid fa-shield-halved"></i> QUY TRÌNH CHECK CĂN &amp; KHÓA CỌC TRỰC TIẾP
        </div>
        <div class="lock-deposit-grid">
          <div class="lock-deposit-text">
            <h3><i class="fa-solid fa-phone-volume" style="color: #c9a96e; margin-right: 8px;"></i>Hotline / Zalo Quản Lý Giỏ Hàng: <span>0909 000 712</span></h3>
            <p>Dành riêng cho Chuyên viên kinh doanh &amp; Quản lý bán hàng: Vui lòng gọi hoặc nhắn Zalo trực tiếp đến <strong>0909 000 712</strong> để kiểm tra tình trạng còn/hết của mã căn và khóa cọc ngay trong thời gian thực trước khi tiến hành nhận tiền khách hàng.</p>
          </div>
          <div class="lock-deposit-cta-group">
            <a href="tel:0909000712" class="btn-lock-phone">
              <i class="fa-solid fa-phone"></i> Gọi 0909 000 712
            </a>
            <a href="https://zalo.me/0909000712" target="_blank" class="btn-lock-zalo">
              <i class="fa-solid fa-comment-dots"></i> Nhắn Zalo Khóa Cọc
            </a>
          </div>
        </div>
      </div>

      <!-- Hero Stats -->
      <div class="hero-stats-grid">
        <div class="stat-pill">
          <span class="stat-pill-label">Tổng sản phẩm mở bán</span>
          <span class="stat-pill-val">{total_count} Căn</span>
          <span class="stat-pill-sub">16 Biệt Phủ • 11 Điền Sản • 7 Điền An</span>
        </div>
        <div class="stat-pill">
          <span class="stat-pill-label">Đơn giá đất chỉ từ</span>
          <span class="stat-pill-val">11,21 Tr/m²</span>
          <span class="stat-pill-sub">Giá gốc đợt 1 từ Chủ đầu tư</span>
        </div>
        <div class="stat-pill">
          <span class="stat-pill-label">Tổng giá niêm yết từ</span>
          <span class="stat-pill-val">7,96 Tỷ</span>
          <span class="stat-pill-sub">Lô A23 (543,61 m² view đồng lúa)</span>
        </div>
        <div class="stat-pill">
          <span class="stat-pill-label">Pháp lý dự án</span>
          <span class="stat-pill-val">100% Sổ Riêng</span>
          <span class="stat-pill-sub">Đất ở nông thôn (ONT) thổ cư</span>
        </div>
      </div>
    </div>
  </section>

  <!-- Main Content -->
  <main class="main-content">

    <!-- ==============================================================
         INTERACTIVE MASTER PLAN
         ============================================================== -->
    <section class="masterplan-interactive-section" id="masterplanSection">
      <div class="map-header">
        <div class="map-title-group">
          <h2><i class="fa-solid fa-map-location-dot" style="color:var(--gold);"></i> SƠ ĐỒ MẶT BẰNG PHÂN LÔ TƯƠNG TÁC</h2>
          <p>Click hoặc chạm vào từng lô trên sơ đồ để xem vị trí thực tế, cảnh quan, diện tích và giá niêm yết gốc đợt 1</p>
        </div>

        <div class="map-legend-group">
          <div class="legend-item legend-manor">
            <span class="legend-dot"></span> Biệt Phủ Điền Trang ({manor_count})
          </div>
          <div class="legend-item legend-founders">
            <span class="legend-dot"></span> Điền Sản ({founders_count})
          </div>
          <div class="legend-item legend-haven">
            <span class="legend-dot"></span> Điền An ({haven_count})
          </div>
          <div class="legend-item legend-reserved">
            <span class="legend-dot"></span> Đang Giữ Chỗ ({reserved_count})
          </div>
        </div>
      </div>

      <!-- Viewport & Hotspots Canvas -->
      <div class="map-viewport" id="mapViewport">
        <div class="map-canvas" id="mapCanvas">
          <div class="map-stage" id="mapStage">
            <img src="/assets/Index_asset/masterplan_tmb_sales.webp" 
                 alt="Sơ đồ phân lô tổng mặt bằng Saigon Farm Resort" 
                 class="map-image"
                 id="masterPlanImg">
            
            <!-- 34 Interactive Pins -->
            {map_hotspots_rendered}
          </div>
        </div>

        <!-- Floating Controls -->
        <div class="map-controls-floating">
          <button type="button" class="map-ctrl-btn" onclick="zoomMap(1.25)" title="Phóng to"><i class="fa-solid fa-plus"></i></button>
          <button type="button" class="map-ctrl-btn" onclick="zoomMap(0.8)" title="Thu nhỏ"><i class="fa-solid fa-minus"></i></button>
          <button type="button" class="map-ctrl-btn" onclick="resetMap()" title="Đặt lại góc nhìn"><i class="fa-solid fa-arrows-rotate"></i></button>
          <button type="button" class="map-ctrl-btn" onclick="toggleMapFullscreen()" title="Toàn màn hình"><i class="fa-solid fa-expand"></i></button>
        </div>

        <!-- Touch/Drag Hint -->
        <div class="map-hint-badge">
          <i class="fa-solid fa-hand-pointer"></i> <span>Kéo để di chuyển bản đồ · Cuộn chuột để phóng to/thu nhỏ</span>
        </div>
      </div>
    </section>

    <!-- Control Toolbar -->
    <div class="control-toolbar">
      <div class="toolbar-row-top">
        <div class="search-box-wrap">
          <i class="fa-solid fa-magnifying-glass"></i>
          <input type="text" id="searchInput" class="search-input" placeholder="Tìm theo mã căn (A04, B24...), diện tích, hướng, view...">
        </div>

        <div class="view-switcher">
          <button type="button" id="btnViewGrid" class="view-btn active" onclick="switchView('grid')" title="Dạng lưới ô vuông tiện lợi">
            <i class="fa-solid fa-grip"></i> Ô Vuông ({total_count})
          </button>
          <button type="button" id="btnViewList" class="view-btn" onclick="switchView('list')" title="Dạng hàng ngang nhỏ gọn">
            <i class="fa-solid fa-bars"></i> Hàng Ngang
          </button>
          <button type="button" id="btnViewTable" class="view-btn" onclick="switchView('table')" title="Bảng thông số chi tiết 11 cột">
            <i class="fa-solid fa-table-list"></i> Bảng Chi Tiết
          </button>
        </div>
      </div>

      <!-- Category Filter Pills -->
      <div class="category-pills">
        <button type="button" class="cat-btn active" data-cat="all" onclick="filterCategory('all', this)">
          Tất Cả Sản Phẩm <span class="cat-count-badge">{total_count}</span>
        </button>
        <button type="button" class="cat-btn" data-cat="biet-phu-dien-trang" onclick="filterCategory('biet-phu-dien-trang', this)">
          Biệt Phủ Điền Trang <span class="cat-count-badge">{manor_count}</span>
        </button>
        <button type="button" class="cat-btn" data-cat="dien-san" onclick="filterCategory('dien-san', this)">
          Điền Sản (Founders) <span class="cat-count-badge">{founders_count}</span>
        </button>
        <button type="button" class="cat-btn" data-cat="dien-an" onclick="filterCategory('dien-an', this)">
          Điền An (Haven) <span class="cat-count-badge">{haven_count}</span>
        </button>
      </div>

      <!-- Secondary Filters & Sort -->
      <div class="filters-row-secondary">
        <div class="filter-dropdowns-group">
          <!-- Dãy -->
          <select id="filterBlock" class="select-filter" onchange="applyFilters()">
            <option value="all">Tất cả Dãy (A & B)</option>
            <option value="a">Dãy A (16 căn)</option>
            <option value="b">Dãy B (18 căn)</option>
          </select>

          <!-- Vị trí -->
          <select id="filterPos" class="select-filter" onchange="applyFilters()">
            <option value="all">Tất cả Vị Trí</option>
            <option value="Lô góc">Lô Góc (6 căn)</option>
            <option value="2 MT">2 Mặt Tiền (1 căn)</option>
            <option value="Lô thường">Lô Thường (27 căn)</option>
          </select>

          <!-- Hướng -->
          <select id="filterDir" class="select-filter" onchange="applyFilters()">
            <option value="all">Tất cả Hướng</option>
            <option value="Đông Nam">Đông Nam</option>
            <option value="Tây Nam">Tây Nam</option>
            <option value="Đông Bắc">Đông Bắc</option>
            <option value="Tây Bắc">Tây Bắc</option>
          </select>

          <!-- View -->
          <select id="filterView" class="select-filter" onchange="applyFilters()">
            <option value="all">Tất cả Cảnh Quan</option>
            <option value="Garden">View Garden (28 căn)</option>
            <option value="Lúa">View Đồng Lúa (6 căn)</option>
          </select>

          <!-- Tiện ích -->
          <select id="filterAmenity" class="select-filter" onchange="applyFilters()">
            <option value="all">Tất cả Tiện Ích</option>
            <option value="Clubhouse">Kề Clubhouse (5 căn)</option>
            <option value="Công viên cảnh quan">Kề Công Viên (2 căn)</option>
            <option value="Bình thường">Tiện ích nội khu</option>
          </select>

          <!-- Trạng thái -->
          <select id="filterStatus" class="select-filter" onchange="applyFilters()">
            <option value="all">Tất cả Trạng Thái</option>
            <option value="available">Còn Hàng ({available_count})</option>
            <option value="reserved">Đang Giữ Chỗ ({reserved_count})</option>
          </select>
        </div>

        <!-- Sort -->
        <div class="sort-group">
          <span class="sort-label"><i class="fa-solid fa-arrow-down-wide-short"></i> Sắp xếp:</span>
          <select id="sortSelect" class="select-filter" onchange="applySorting()">
            <option value="stt">Mặc định (Số thứ tự)</option>
            <option value="price-asc">Giá: Thấp đến Cao</option>
            <option value="price-desc">Giá: Cao đến Thấp</option>
            <option value="area-desc">Diện tích: Lớn nhất</option>
            <option value="area-asc">Diện tích: Nhỏ nhất</option>
            <option value="unit-asc">Đơn giá: Thấp nhất</option>
          </select>
        </div>
      </div>
    </div>

    <!-- Results Summary -->
    <div class="results-summary-bar">
      <div class="results-count">
        Hiển thị <strong id="visibleCount">{total_count}</strong> / {total_count} sản phẩm
      </div>
      <div class="reset-filter-btn" style="cursor:pointer; color:var(--gold-dark); font-weight:600;" onclick="resetAllFilters()">
        <i class="fa-solid fa-rotate-left"></i> Xóa bộ lọc
      </div>
    </div>

    <!-- Card Grid View Container -->
    <div class="listings-grid" id="listingsGrid">
      {cards_rendered}
    </div>

    <!-- Table View Container -->
    <div class="table-view-container" id="tableViewContainer">
      <div class="table-responsive">
        <table class="inventory-table" id="inventoryTable">
          <thead>
            <tr>
              <th>STT</th>
              <th>Dãy</th>
              <th>Mã Căn</th>
              <th>Phân Khu</th>
              <th>Diện Tích</th>
              <th>Vị Trí</th>
              <th>Hướng</th>
              <th>View</th>
              <th>Tiện Ích</th>
              <th>Mặt Đường</th>
              <th>Đơn Giá Đất</th>
              <th>Giá Gốc Niêm Yết</th>
              <th>Trạng Thái</th>
              <th>Thao Tác</th>
            </tr>
          </thead>
          <tbody id="inventoryTableBody">
            {table_rows_rendered}
          </tbody>
        </table>
      </div>
    </div>

    <!-- No Results Box -->
    <div class="no-results-box" id="noResultsBox">
      <i class="fa-regular fa-folder-open"></i>
      <h3>Không tìm thấy sản phẩm phù hợp</h3>
      <p style="color:#777; margin-bottom:16px;">Vui lòng thử tìm kiếm với từ khóa khác hoặc thiết lập lại bộ lọc.</p>
      <button type="button" class="btn-primary-action" style="max-width:200px; margin:0 auto;" onclick="resetAllFilters()">
        <i class="fa-solid fa-rotate-left"></i> Xem Tất Cả {total_count} Căn
      </button>
    </div>

  </main>

  <!-- Booking Modal -->
  <div class="modal-overlay" id="bookingModal" onclick="closeModalOnOverlay(event)">
    <div class="modal-card">
      <div class="modal-header">
        <h3><i class="fa-solid fa-file-invoice-dollar" style="color:var(--gold); margin-right:8px;"></i> Nhận Báo Giá & Bảng Tính Chi Tiết</h3>
        <button type="button" class="modal-close-btn" onclick="closeBookingModal()">&times;</button>
      </div>
      <div class="modal-body">
        <div class="modal-lot-preview">
          <div class="mlp-title" id="modalLotTitle">Mã Căn A04 · Biệt Phủ Điền Trang</div>
          <div class="mlp-details" id="modalLotDetails">Diện tích: 1.089,62 m² • Đơn giá: 12.714.860 đ/m²</div>
          <div class="mlp-price" id="modalLotPrice">13,85 Tỷ (Giá gốc niêm yết)</div>
        </div>

        <div class="modal-direct-lock">
          <div class="mdl-title"><i class="fa-solid fa-bolt" style="color:var(--gold);"></i> Kiểm tra tình trạng căn &amp; Khóa cọc nhanh:</div>
          <div class="mdl-actions">
            <a href="tel:0909000712" class="btn-mdl-call"><i class="fa-solid fa-phone"></i> Gọi 0909 000 712</a>
            <a href="https://zalo.me/0909000712" target="_blank" class="btn-mdl-zalo"><i class="fa-solid fa-comment-dots"></i> Nhắn Zalo Khóa Cọc</a>
          </div>
        </div>

        <form id="bookingForm" onsubmit="handleFormSubmit(event)">
          <input type="hidden" id="formCode" value="">
          <input type="hidden" id="formCategory" value="">

          <div class="form-group">
            <label for="formName">Họ và tên của Quý khách (*)</label>
            <input type="text" id="formName" class="form-control" placeholder="Ví dụ: Nguyễn Văn An" required>
          </div>

          <div class="form-group">
            <label for="formPhone">Số điện thoại / Zalo nhận tài liệu (*)</label>
            <input type="tel" id="formPhone" class="form-control" placeholder="Ví dụ: 090 123 4567" required>
          </div>

          <div class="form-group">
            <label for="formNeed">Nhu cầu tư vấn ưu tiên</label>
            <select id="formNeed" class="form-control">
              <option value="Bảng tính thanh toán sớm (giảm 800Tr - 1 Tỷ)">Nhận bảng tính thanh toán sớm (giảm 800Tr - 1 Tỷ)</option>
              <option value="Chính sách cam kết thuê 80Tr/tháng">Chính sách cam kết thuê 80Tr/tháng</option>
              <option value="Đăng ký đi xe đưa đón khảo sát thực tế">Đăng ký đi xe đưa đón khảo sát thực tế</option>
              <option value="Nhận toàn bộ hồ sơ pháp lý 1/500 & sổ đỏ">Nhận toàn bộ hồ sơ pháp lý 1/500 & sổ đỏ</option>
            </select>
          </div>

          <div class="form-group">
            <label for="formNote">Ghi chú thêm (nếu có)</label>
            <textarea id="formNote" class="form-control" rows="2" placeholder="Ví dụ: Cần tư vấn hướng Tây Nam, gửi bảng tính qua Zalo..."></textarea>
          </div>

          <button type="submit" class="modal-submit-btn">
            <i class="fa-solid fa-paper-plane" style="margin-right:6px;"></i> Gửi Yêu Cầu Nhận Báo Giá Ngay
          </button>
        </form>
      </div>
    </div>
  </div>

  <!-- Mobile Fixed Bottom Dock -->
  <div class="mobile-bottom-dock">
    <a href="tel:0909000712" class="dock-btn dock-btn-call">
      <i class="fa-solid fa-phone"></i> Gọi 0909 000 712
    </a>
    <a href="https://zalo.me/0909000712" target="_blank" class="dock-btn dock-btn-zalo">
      <i class="fa-solid fa-comment-dots"></i> Nhắn Zalo Khóa Cọc
    </a>
  </div>

  <!-- Floating Sales CTA Bar -->
  <div class="floating-sales-cta">
    <a href="tel:0909000712" class="float-sales-btn float-call" title="Gọi kiểm tra giỏ hàng 0909 000 712">
      <i class="fa-solid fa-phone"></i>
      <span class="float-btn-label">Check Căn: <strong>0909 000 712</strong></span>
    </a>
    <a href="https://zalo.me/0909000712" target="_blank" class="float-sales-btn float-zalo" title="Zalo khóa cọc 0909 000 712">
      <i class="fa-solid fa-comment-dots"></i>
      <span class="float-btn-label">Zalo Khóa Cọc</span>
    </a>
  </div>

  <!-- Site Footer -->
  <footer class="site-footer">
    <div class="footer-container">
      <div class="footer-col">
        <h4 style="color:#ffffff;">SAIGON FARM RESORT</h4>
        <p style="font-size:0.86rem; color:#dfd7cc; line-height:1.6; margin-bottom:14px;">
          Quần thể điền trang nghỉ dưỡng sinh thái ven hồ 100ha đầu tiên tại TP. Hồ Chí Minh. Bộ sưu tập 34 sản phẩm giới hạn 100% thổ cư sổ đỏ riêng.
        </p>
        <p style="font-size:0.82rem; color:#aaa;">
          <strong style="color:var(--gold);">Chủ đầu tư & Phát triển:</strong> MDS Living<br/>
          <strong style="color:var(--gold);">Vị trí:</strong> Xã Đất Đỏ, TP. Hồ Chí Minh
        </p>
      </div>
      <div class="footer-col">
        <h4>Bộ Sưu Tập Sản Phẩm</h4>
        <ul>
          <li><a href="biet-phu-dien-trang.html">Biệt Phủ Điền Trang (16 Căn)</a></li>
          <li><a href="dien-san.html">Điền Sản - Founders (11 Căn)</a></li>
          <li><a href="dien-an.html">Điền An - Haven (7 Cụm)</a></li>
          <li><a href="giohang.html">Giỏ Hàng & Bảng Giá Mở Bán</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Tài Liệu & Báo Chí</h4>
        <ul>
          <li><a href="gioithieu">Bản Giới Thiệu (Pitch Deck)</a></li>
          <li><a href="story">Tạp Chí Story (98 Trang)</a></li>
          <li><a href="investment.html">Chuyên Trang Đầu Tư</a></li>
          <li><a href="index.html#ban-sac">9 Không Gian Bản Sắc</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Liên Hệ Ban Quản Lý</h4>
        <p style="font-size:0.86rem; color:#dfd7cc; line-height:1.6; margin-bottom:10px;">
          Hotline Quản Lý Giỏ Hàng & Khóa Cọc:<br/>
          <strong style="font-size:1.15rem; color:var(--gold);">0909 000 712</strong> (Call / Zalo)
        </p>
        <p style="font-size:0.82rem; color:#aaa;">
          Hỗ trợ tư vấn 24/7 · Xe đưa đón khảo sát thực tế dự án miễn phí cuối tuần.
        </p>
      </div>
    </div>

    <div class="footer-bottom">
      <div>&copy; 2026 Saigon Farm Resort & MDS Living. Toàn bộ thông tin được bảo lưu quyền tác giả.</div>
      <div>Pháp lý minh bạch · 100% Sổ đỏ thổ cư riêng từng nền</div>
    </div>
  </footer>

  <!-- Scripts -->
  <script>
    let currentCategory = 'all';
    let currentView = 'grid';

    // ==============================================================
    // MAP INTERACTION ENGINE (PAN & ZOOM)
    // ==============================================================
    const STAGE_WIDTH = 2560;
    const STAGE_HEIGHT = 1918;

    let mapScale = 1.0;
    let mapPanX = 0;
    let mapPanY = 0;
    let isDragging = false;
    let startX = 0;
    let startY = 0;

    const viewport = document.getElementById('mapViewport');
    const canvas = document.getElementById('mapCanvas');
    const masterPlanImg = document.getElementById('masterPlanImg');

    function updateMapTransform() {{
      canvas.style.transform = `translate(${{mapPanX}}px, ${{mapPanY}}px) scale(${{mapScale}})`;
    }}

    function fitMapToViewport() {{
      if (!viewport) return;
      const vpW = viewport.clientWidth || 1200;
      const vpH = viewport.clientHeight || 720;
      
      const fitScale = Math.min(vpW / STAGE_WIDTH, vpH / STAGE_HEIGHT);
      // Set comfortable initial zoom focused on lot cluster
      mapScale = Math.max(fitScale * 1.35, 0.55);
      
      // Lots cluster center is around (52% X, 55% Y)
      const targetX = STAGE_WIDTH * 0.52;
      const targetY = STAGE_HEIGHT * 0.55;
      
      mapPanX = (vpW / 2) - (targetX * mapScale);
      mapPanY = (vpH / 2) - (targetY * mapScale);
      
      updateMapTransform();
    }}

    function zoomMap(factor, clientX, clientY) {{
      const oldScale = mapScale;
      const newScale = Math.min(Math.max(0.35, mapScale * factor), 3.2);
      if (newScale === oldScale) return;

      const rect = viewport.getBoundingClientRect();
      const originX = (clientX !== undefined) ? (clientX - rect.left) : (viewport.clientWidth / 2);
      const originY = (clientY !== undefined) ? (clientY - rect.top) : (viewport.clientHeight / 2);

      const stageX = (originX - mapPanX) / oldScale;
      const stageY = (originY - mapPanY) / oldScale;

      mapScale = newScale;
      mapPanX = originX - stageX * mapScale;
      mapPanY = originY - stageY * mapScale;

      updateMapTransform();
    }}

    function resetMap() {{
      canvas.classList.add('smooth-anim');
      fitMapToViewport();
      setTimeout(() => canvas.classList.remove('smooth-anim'), 400);
    }}

    function toggleMapFullscreen() {{
      if (!document.fullscreenElement) {{
        viewport.requestFullscreen().catch(err => alert('Không thể bật toàn màn hình: ' + err.message));
      }} else {{
        document.exitFullscreen();
      }}
    }}

    viewport.addEventListener('mousedown', (e) => {{
      if (e.target.closest('.map-controls-floating') || e.target.closest('.hotspot-tooltip') || e.target.closest('button')) return;
      isDragging = true;
      startX = e.clientX - mapPanX;
      startY = e.clientY - mapPanY;
    }});

    window.addEventListener('mousemove', (e) => {{
      if (!isDragging) return;
      mapPanX = e.clientX - startX;
      mapPanY = e.clientY - startY;
      updateMapTransform();
    }});

    window.addEventListener('mouseup', () => {{
      isDragging = false;
    }});

    viewport.addEventListener('wheel', (e) => {{
      e.preventDefault();
      const zoomFactor = e.deltaY < 0 ? 1.12 : 0.89;
      zoomMap(zoomFactor, e.clientX, e.clientY);
    }}, {{ passive: false }});

    viewport.addEventListener('dblclick', (e) => {{
      if (e.target.closest('.map-controls-floating') || e.target.closest('.hotspot-tooltip') || e.target.closest('button')) return;
      zoomMap(1.35, e.clientX, e.clientY);
    }});

    // Touch support for mobile panning
    let touchStartX = 0, touchStartY = 0;
    viewport.addEventListener('touchstart', (e) => {{
      if (e.touches.length === 1) {{
        touchStartX = e.touches[0].clientX - mapPanX;
        touchStartY = e.touches[0].clientY - mapPanY;
      }}
    }});
    viewport.addEventListener('touchmove', (e) => {{
      if (e.touches.length === 1) {{
        mapPanX = e.touches[0].clientX - touchStartX;
        mapPanY = e.touches[0].clientY - touchStartY;
        updateMapTransform();
      }}
    }});

    // Initialize map positioning once image or DOM is ready
    if (masterPlanImg && masterPlanImg.complete) {{
      fitMapToViewport();
    }} else if (masterPlanImg) {{
      masterPlanImg.addEventListener('load', fitMapToViewport);
    }}
    window.addEventListener('load', fitMapToViewport);

    // Bidirectional highlighting between map & list
    function highlightHotspot(code) {{
      const pin = document.getElementById('hotspot-' + code.toLowerCase());
      if (pin) pin.classList.add('highlighted');
    }}

    function unhighlightHotspot(code) {{
      const pin = document.getElementById('hotspot-' + code.toLowerCase());
      if (pin) pin.classList.remove('highlighted');
    }}

    function focusLot(code) {{
      const c = code.toLowerCase();
      const card = document.getElementById('card-' + c);
      const row = document.getElementById('row-' + c);

      if ((currentView === 'grid' || currentView === 'list') && card) {{
        card.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
        card.classList.add('card-highlighted');
        setTimeout(() => card.classList.remove('card-highlighted'), 2500);
      }} else if (row) {{
        row.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
        row.classList.add('row-highlighted');
        setTimeout(() => row.classList.remove('row-highlighted'), 2500);
      }}
    }}

    function locateOnMap(code) {{
      const c = code.toLowerCase();
      const pin = document.getElementById('hotspot-' + c);
      const sec = document.getElementById('masterplanSection');
      if (sec) {{
        sec.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
      }}
      if (pin) {{
        const xPct = parseFloat(pin.style.left);
        const yPct = parseFloat(pin.style.top);
        
        mapScale = 1.45;
        const vpW = viewport.clientWidth;
        const vpH = viewport.clientHeight;
        const pinPixelX = (xPct / 100.0) * STAGE_WIDTH;
        const pinPixelY = (yPct / 100.0) * STAGE_HEIGHT;
        
        canvas.classList.add('smooth-anim');
        mapPanX = (vpW / 2) - (pinPixelX * mapScale);
        mapPanY = (vpH / 2) - (pinPixelY * mapScale);
        updateMapTransform();
        setTimeout(() => canvas.classList.remove('smooth-anim'), 400);

        pin.classList.add('highlighted');
        setTimeout(() => pin.classList.remove('highlighted'), 3500);
      }}
    }}

    // ==============================================================
    // VIEW SWITCHER & FILTER ENGINE
    // ==============================================================
    function switchView(view) {{
      currentView = view;
      const btnGrid = document.getElementById('btnViewGrid');
      const btnList = document.getElementById('btnViewList');
      const btnTable = document.getElementById('btnViewTable');
      const grid = document.getElementById('listingsGrid');
      const table = document.getElementById('tableViewContainer');

      if (btnGrid) btnGrid.classList.toggle('active', view === 'grid');
      if (btnList) btnList.classList.toggle('active', view === 'list');
      if (btnTable) btnTable.classList.toggle('active', view === 'table');

      if (view === 'grid') {{
        grid.style.display = 'grid';
        grid.classList.remove('view-list-mode');
        table.style.display = 'none';
      }} else if (view === 'list') {{
        grid.style.display = 'flex';
        grid.classList.add('view-list-mode');
        table.style.display = 'none';
      }} else {{
        grid.style.display = 'none';
        table.style.display = 'block';
      }}
      applyFilters();
    }}

    function filterCategory(cat, btn) {{
      currentCategory = cat;
      document.querySelectorAll('.cat-btn').forEach(b => b.classList.remove('active'));
      if (btn) btn.classList.add('active');

      // Update map pins opacity based on category
      const pins = document.querySelectorAll('.map-hotspot');
      pins.forEach(pin => {{
        const pinCat = pin.getAttribute('data-category');
        if (cat === 'all' || pinCat === cat) {{
          pin.style.opacity = '1';
          pin.style.pointerEvents = 'auto';
        }} else {{
          pin.style.opacity = '0.2';
          pin.style.pointerEvents = 'none';
        }}
      }});

      applyFilters();
    }}

    function applyFilters() {{
      const query = document.getElementById('searchInput').value.toLowerCase().trim();
      const blockFilter = document.getElementById('filterBlock').value;
      const posFilter = document.getElementById('filterPos').value;
      const dirFilter = document.getElementById('filterDir').value;
      const viewFilter = document.getElementById('filterView').value;
      const amenityFilter = document.getElementById('filterAmenity').value;
      const statusFilter = document.getElementById('filterStatus').value;

      const cards = document.querySelectorAll('.listing-card');
      const rows = document.querySelectorAll('.table-row-item');

      let visibleCount = 0;

      // Filter Cards
      cards.forEach(card => {{
        const code = card.getAttribute('data-code') || '';
        const block = card.getAttribute('data-block') || '';
        const category = card.getAttribute('data-category') || '';
        const pos = card.getAttribute('data-pos') || '';
        const dir = card.getAttribute('data-direction') || '';
        const v = card.getAttribute('data-view') || '';
        const amenity = card.getAttribute('data-amenity') || '';
        const status = card.getAttribute('data-status') || '';
        const textContent = card.textContent.toLowerCase();

        let match = true;

        if (currentCategory !== 'all' && category !== currentCategory) match = false;
        if (blockFilter !== 'all' && block !== blockFilter) match = false;
        if (posFilter !== 'all' && pos !== posFilter) match = false;
        if (dirFilter !== 'all' && dir !== dirFilter) match = false;
        if (viewFilter !== 'all' && v !== viewFilter) match = false;
        if (amenityFilter !== 'all' && amenity !== amenityFilter) match = false;
        if (statusFilter !== 'all' && status !== statusFilter) match = false;

        if (query) {{
          const matchQuery = code.includes(query) || textContent.includes(query);
          if (!matchQuery) match = false;
        }}

        card.style.display = match ? 'flex' : 'none';
        if (match) visibleCount++;
      }});

      // Filter Table Rows
      rows.forEach(row => {{
        const code = row.getAttribute('data-code') || '';
        const block = row.getAttribute('data-block') || '';
        const category = row.getAttribute('data-category') || '';
        const pos = row.getAttribute('data-pos') || '';
        const dir = row.getAttribute('data-direction') || '';
        const v = row.getAttribute('data-view') || '';
        const amenity = row.getAttribute('data-amenity') || '';
        const status = row.getAttribute('data-status') || '';
        const textContent = row.textContent.toLowerCase();

        let match = true;

        if (currentCategory !== 'all' && category !== currentCategory) match = false;
        if (blockFilter !== 'all' && block !== blockFilter) match = false;
        if (posFilter !== 'all' && pos !== posFilter) match = false;
        if (dirFilter !== 'all' && dir !== dirFilter) match = false;
        if (viewFilter !== 'all' && v !== viewFilter) match = false;
        if (amenityFilter !== 'all' && amenity !== amenityFilter) match = false;
        if (statusFilter !== 'all' && status !== statusFilter) match = false;

        if (query) {{
          const matchQuery = code.includes(query) || textContent.includes(query);
          if (!matchQuery) match = false;
        }}

        row.style.display = match ? '' : 'none';
      }});

      // Update counters & empty state
      document.getElementById('visibleCount').textContent = visibleCount;
      const noResults = document.getElementById('noResultsBox');
      const grid = document.getElementById('listingsGrid');
      const table = document.getElementById('tableViewContainer');

      if (visibleCount === 0) {{
        noResults.style.display = 'block';
        if (grid) grid.style.display = 'none';
        if (table) table.style.display = 'none';
      }} else {{
        noResults.style.display = 'none';
        if (currentView === 'grid') {{
          if (grid) {{
            grid.style.display = 'grid';
            grid.classList.remove('view-list-mode');
          }}
          if (table) table.style.display = 'none';
        }} else if (currentView === 'list') {{
          if (grid) {{
            grid.style.display = 'flex';
            grid.classList.add('view-list-mode');
          }}
          if (table) table.style.display = 'none';
        }} else {{
          if (grid) grid.style.display = 'none';
          if (table) table.style.display = 'block';
        }}
      }}
    }}

    function applySorting() {{
      const sortVal = document.getElementById('sortSelect').value;
      const grid = document.getElementById('listingsGrid');
      const tbody = document.getElementById('inventoryTableBody');

      const cards = Array.from(grid.querySelectorAll('.listing-card'));
      const rows = Array.from(tbody.querySelectorAll('.table-row-item'));

      const sortFn = (a, b) => {{
        if (sortVal === 'price-asc') {{
          return parseFloat(a.getAttribute('data-price')) - parseFloat(b.getAttribute('data-price'));
        }} else if (sortVal === 'price-desc') {{
          return parseFloat(b.getAttribute('data-price')) - parseFloat(a.getAttribute('data-price'));
        }} else if (sortVal === 'area-desc') {{
          return parseFloat(b.getAttribute('data-area')) - parseFloat(a.getAttribute('data-area'));
        }} else if (sortVal === 'area-asc') {{
          return parseFloat(a.getAttribute('data-area')) - parseFloat(b.getAttribute('data-area'));
        }} else if (sortVal === 'unit-asc') {{
          return parseFloat(a.getAttribute('data-unit-price')) - parseFloat(b.getAttribute('data-unit-price'));
        }} else {{
          return parseInt(a.getAttribute('data-stt')) - parseInt(b.getAttribute('data-stt'));
        }}
      }};

      cards.sort(sortFn).forEach(c => grid.appendChild(c));
      rows.sort(sortFn).forEach(r => tbody.appendChild(r));
    }}

    function resetAllFilters() {{
      document.getElementById('searchInput').value = '';
      document.getElementById('filterBlock').value = 'all';
      document.getElementById('filterPos').value = 'all';
      document.getElementById('filterDir').value = 'all';
      document.getElementById('filterView').value = 'all';
      document.getElementById('filterAmenity').value = 'all';
      document.getElementById('filterStatus').value = 'all';
      document.getElementById('sortSelect').value = 'stt';

      currentCategory = 'all';
      document.querySelectorAll('.cat-btn').forEach(b => {{
        if (b.getAttribute('data-cat') === 'all') b.classList.add('active');
        else b.classList.remove('active');
      }});

      // Reset pins
      document.querySelectorAll('.map-hotspot').forEach(p => {{
        p.style.opacity = '1';
        p.style.pointerEvents = 'auto';
      }});

      resetMap();
      applyFilters();
      applySorting();
    }}

    // Real-time search listener
    document.getElementById('searchInput').addEventListener('input', applyFilters);

    // Modal logic
    function openBookingModal(code, catTitle, areaStr, unitPriceStr, priceStr, priceBil) {{
      document.getElementById('formCode').value = code;
      document.getElementById('formCategory').value = catTitle;

      if (code && code !== 'TƯ VẤN CHUNG') {{
        document.getElementById('modalLotTitle').textContent = `Mã Căn ${{code}} · ${{catTitle}}`;
        document.getElementById('modalLotDetails').textContent = `Diện tích: ${{areaStr}} m² • Đơn giá: ${{unitPriceStr}}`;
        document.getElementById('modalLotPrice').textContent = `${{priceBil}} (Giá gốc niêm yết: ${{priceStr}})`;
        document.getElementById('modalLotTitle').parentElement.style.display = 'block';
      }} else {{
        document.getElementById('modalLotTitle').parentElement.style.display = 'none';
      }}

      document.getElementById('bookingModal').style.display = 'flex';
      document.body.style.overflow = 'hidden';
    }}

    function closeBookingModal() {{
      document.getElementById('bookingModal').style.display = 'none';
      document.body.style.overflow = '';
    }}

    function closeModalOnOverlay(e) {{
      if (e.target.id === 'bookingModal') {{
        closeBookingModal();
      }}
    }}

    function handleFormSubmit(e) {{
      e.preventDefault();
      const name = document.getElementById('formName').value;
      const phone = document.getElementById('formPhone').value;
      const code = document.getElementById('formCode').value || 'Tư vấn chung';
      const need = document.getElementById('formNeed').value;

      alert(`Cảm ơn Quý khách ${{name}}! Yêu cầu nhận bảng tính & chính sách cho sản phẩm ${{code}} đã được chuyển đến Ban Quản Lý Dự Án. Chuyên viên sẽ liên hệ lại qua SĐT/Zalo ${{phone}} trong ít phút.`);
      closeBookingModal();
      document.getElementById('bookingForm').reset();
    }}
  </script>
</body>
</html>
"""

    # Write primary /giohang files
    with open("giohang.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    print("Generated giohang.html successfully!")

    os.makedirs("giohang", exist_ok=True)
    with open("giohang/index.html", "w", encoding="utf-8") as f:
        f.write(html_content.replace("<head>", '<head>\n  <base href="../">'))
    print("Generated giohang/index.html successfully with base href!")

    # Also keep listing.html and listing/index.html updated as legacy fallback
    with open("listing.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    print("Generated listing.html successfully!")

    os.makedirs("listing", exist_ok=True)
    with open("listing/index.html", "w", encoding="utf-8") as f:
        f.write(html_content.replace("<head>", '<head>\n  <base href="../">'))
    print("Generated listing/index.html successfully with base href!")

if __name__ == "__main__":
    update_listing()
