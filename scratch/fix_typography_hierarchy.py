import re

# ==============================================================================
# 1. UPDATE CSS IN INDEX.HTML
# ==============================================================================

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

unified_css = '''
    /* ================================================================
       CHUẨN HÓA QUY TẮC ĐỒNG CẤP & TYPOGRAPHY TOÀN BỘ TRANG (EDITORIAL)
       ================================================================ */
    :root {
      --editorial-title-size: clamp(1.65rem, 3.2vw, 2.3rem);
      --editorial-sub-size: 0.98rem;
    }

    /* Khung Header Cấp 1 — Thống nhất 100% CANH TRÁI toàn bộ trang */
    .editorial-section-header,
    .section-header-wrap,
    .hht-mag-header {
      text-align: left !important;
      margin-bottom: 26px !important;
      max-width: 900px !important;
    }

    /* Eyebrow / Category Tag Cấp 1 */
    .editorial-eyebrow,
    .section-eyebrow,
    .hht-mag-cat {
      display: inline-flex !important;
      align-items: center !important;
      gap: 6px !important;
      font-size: 0.72rem !important;
      font-weight: 800 !important;
      letter-spacing: 0.12em !important;
      text-transform: uppercase !important;
      color: #8c6b32 !important;
      margin-bottom: 8px !important;
      background: none !important;
      border: none !important;
      padding: 0 !important;
    }

    /* Tiêu đề Section Cấp 1 — Đồng nhất kích thước & font Playfair */
    .editorial-section-title,
    .section-title,
    .hht-mag-title {
      font-family: 'Playfair Display', Georgia, serif !important;
      font-size: var(--editorial-title-size) !important;
      font-weight: 700 !important;
      color: #183024 !important;
      line-height: 1.32 !important;
      margin: 0 0 10px 0 !important;
      letter-spacing: -0.015em !important;
      text-align: left !important;
      text-transform: none !important;
    }

    /* Đoạn văn mô tả dưới Tiêu đề Section Cấp 1 */
    .editorial-section-sub,
    .section-subtitle,
    .hht-mag-subtitle {
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif !important;
      font-size: var(--editorial-sub-size) !important;
      color: #555555 !important;
      line-height: 1.68 !important;
      margin: 0 !important;
      max-width: 820px !important;
      font-weight: 400 !important;
      text-align: left !important;
    }

    /* Tiêu đề Phân mục Cấp 2 (Sub-sections) */
    .editorial-sub-header {
      margin-top: 36px !important;
      margin-bottom: 20px !important;
      text-align: left !important;
    }

    .editorial-sub-title {
      font-family: 'Playfair Display', Georgia, serif !important;
      font-size: clamp(1.25rem, 2.2vw, 1.6rem) !important;
      font-weight: 700 !important;
      color: #183024 !important;
      margin: 4px 0 6px 0 !important;
      line-height: 1.35 !important;
      text-align: left !important;
      text-transform: none !important;
    }

    /* Bảng danh mục trải nghiệm — Responsive không bao giờ vỡ trên mobile */
    .heritage-table-card {
      background: #ffffff;
      border: 1px solid #dfc89f;
      border-radius: 12px;
      padding: 24px;
      margin: 30px 0;
      box-shadow: 0 8px 24px rgba(194, 155, 83, 0.08);
      overflow: hidden;
    }

    .heritage-table-scroll {
      width: 100%;
      overflow-x: auto;
      -webkit-overflow-scrolling: touch;
      margin-top: 14px;
    }

    @media (max-width: 768px) {
      .heritage-table-card {
        padding: 18px 14px;
        margin: 20px 0;
      }
      .heritage-table-card h4 {
        font-size: 1.15rem !important;
        line-height: 1.4 !important;
      }
    }
'''

if 'CHUẨN HÓA QUY TẮC ĐỒNG CẤP & TYPOGRAPHY' not in html:
    html = html.replace('</style>', unified_css + '\n  </style>', 1)


# ==============================================================================
# 2. UPDATE SECTION 1 (#partner-toolkit)
# ==============================================================================

old_sec1_header = re.search(r'<!-- Header Block -->.*?<!-- 5 Trụ Cột Triết Lý', html, re.DOTALL)
assert old_sec1_header, "old_sec1_header not found"

new_sec1_header = '''<!-- Header Block (Đồng Cấp Chuẩn Mực - Canh Trái) -->
      <div class="editorial-section-header">
        <span class="editorial-eyebrow"><i class="fa-solid fa-crown"></i> DÒNG SẢN PHẨM ĐIỀN TRANG</span>
        <h2 class="editorial-section-title">Cấu Trúc 3 Dòng Sản Phẩm &amp; Lối Sống Việt Đương Đại</h2>
        <p class="editorial-section-sub">
          Quần thể điền trang nghỉ dưỡng sinh thái ven hồ 100ha liền kề Hồ Tràm, tích hợp bộ 3 giải pháp độc bản dành cho gia đình thượng lưu.
        </p>
        
        <!-- 3 Điểm Trọng Tâm Hàng Ngang (Desktop & Mobile) -->
        <div style="display: flex; justify-content: flex-start; align-items: stretch; gap: 10px; max-width: 680px; margin: 18px 0 0;">
          <div style="flex: 1; min-width: 0; background: #faf5ec; border: 1px solid #dfc89f; border-radius: 8px; padding: 12px 8px; text-align: center; box-shadow: 0 2px 8px rgba(194, 155, 83, 0.08); display: flex; flex-direction: column; justify-content: center; align-items: center; gap: 4px;">
            <i class="fa-solid fa-shield-halved" style="color: #8c6b32; font-size: 0.95rem;"></i>
            <span style="font-size: 0.84rem; font-weight: 700; color: #183024; line-height: 1.35;">Tích sản an toàn</span>
          </div>
          <div style="flex: 1; min-width: 0; background: #faf5ec; border: 1px solid #dfc89f; border-radius: 8px; padding: 12px 8px; text-align: center; box-shadow: 0 2px 8px rgba(194, 155, 83, 0.08); display: flex; flex-direction: column; justify-content: center; align-items: center; gap: 4px;">
            <i class="fa-solid fa-spa" style="color: #8c6b32; font-size: 0.95rem;"></i>
            <span style="font-size: 0.84rem; font-weight: 700; color: #183024; line-height: 1.35;">Nghỉ dưỡng thụ hưởng</span>
          </div>
          <div style="flex: 1; min-width: 0; background: #faf5ec; border: 1px solid #dfc89f; border-radius: 8px; padding: 12px 8px; text-align: center; box-shadow: 0 2px 8px rgba(194, 155, 83, 0.08); display: flex; flex-direction: column; justify-content: center; align-items: center; gap: 4px;">
            <i class="fa-solid fa-chart-line" style="color: #8c6b32; font-size: 0.95rem;"></i>
            <span style="font-size: 0.84rem; font-weight: 700; color: #183024; line-height: 1.35;">Dòng tiền bền vững</span>
          </div>
        </div>
      </div>

      <!-- 5 Trụ Cột Triết Lý'''

html = html[:old_sec1_header.start()] + new_sec1_header + html[old_sec1_header.end():]


# ==============================================================================
# 3. UPDATE SECTION 2 (#ban-sac)
# ==============================================================================

# 3a. Header of #ban-sac
old_sec2_header = re.search(r'<div style="margin-bottom: 22px; margin-top: 12px;">.*?</div>\s*<!-- Top 3 Featured Heritage Cards -->', html, re.DOTALL)
assert old_sec2_header, "old_sec2_header not found"

new_sec2_header = '''<div class="editorial-section-header">
        <span class="editorial-eyebrow"><i class="fa-solid fa-feather-pointed"></i> DI SẢN BẢN SẮC VIỆT</span>
        <h2 class="editorial-section-title">Điền Trang Nghỉ Dưỡng Bản Sắc Việt Đương Đại</h2>
        <p class="editorial-section-sub">
          Nơi tinh hoa văn hóa truyền thống 4.000 năm hòa quyện cùng chuẩn sống thượng lưu quốc tế, hệ tiện ích resort độc đáo, nhịp sống lễ hội bốn mùa sống động.
        </p>
      </div>

      <!-- Top 3 Featured Heritage Cards -->'''

html = html[:old_sec2_header.start()] + new_sec2_header + html[old_sec2_header.end():]

# 3b. Interactive Spaces Heritage Table container wrap
old_table = re.search(r'<!-- Interactive Spaces Heritage Table -->.*?<div style="background: #ffffff; border: 1px solid #dfc89f; border-radius: 12px; padding: 25px 22px; margin: 30px 0; overflow-x: auto; box-shadow: 0 8px 24px rgba\(194, 155, 83, 0.08\);">(.*?)</table>\s*</div>', html, re.DOTALL)
if old_table:
    inner_table = old_table.group(1)
    # Split header from table
    table_header_match = re.search(r'(<div.*?style="display: flex; justify-content: space-between;.*?</div>)\s*(<table.*)', inner_table, re.DOTALL)
    if table_header_match:
        t_head = table_header_match.group(1)
        t_body = table_header_match.group(2)
        new_table_block = f'''<!-- Interactive Spaces Heritage Table -->
      <div class="heritage-table-card">
        {t_head}
        <div class="heritage-table-scroll">
          {t_body}
        </table>
        </div>
      </div>'''
        html = html[:old_table.start()] + new_table_block + html[old_table.end():]

# 3c. 10 Chuyên đề Sub-header
old_10_chuyende = re.search(r'<!-- 10 Chuyên Đề Văn Hóa & Bản Sắc Việt Showcase -->.*?<div style="text-align: center; margin-bottom: 26px;">.*?BỘ SƯU TẬP 10 CHUYÊN ĐỀ.*?</div>', html, re.DOTALL)
if old_10_chuyende:
    new_10_chuyende = '''<!-- 10 Chuyên Đề Văn Hóa & Bản Sắc Việt Showcase -->
      <div class="editorial-sub-header" style="padding-top: 28px; border-top: 1px solid rgba(201,169,110,0.3);">
        <span class="editorial-eyebrow"><i class="fa-solid fa-book-bookmark"></i> ẤN PHẨM CHUYÊN ĐỀ</span>
        <h3 class="editorial-sub-title">10 Chuyên Đề Văn Hóa &amp; Phong Cách Sống Điền Trang</h3>
        <p class="editorial-section-sub">Chuỗi bài viết chuyên sâu đúc kết triết lý sống, giá trị di sản và phong cách thụ hưởng đích thực của người Việt đương đại.</p>
      </div>'''
    html = html[:old_10_chuyende.start()] + new_10_chuyende + html[old_10_chuyende.end():]


# ==============================================================================
# 4. UPDATE SECTION 3 (#tien-ich)
# ==============================================================================

old_sec3_header = re.search(r'<div style="margin-bottom: 24px; margin-top: 12px; text-align: left;">.*?</div>\s*<!-- Sơ Đồ Phân Bổ 2 Phân Khu Tiện Ích -->', html, re.DOTALL)
assert old_sec3_header, "old_sec3_header not found"

new_sec3_header = '''<div class="editorial-section-header">
        <span class="editorial-eyebrow"><i class="fa-solid fa-spa"></i> ĐẶC QUYỀN THƯỢNG LƯU KHÉP KÍN</span>
        <h2 class="editorial-section-title">Quần Thể Tiện Ích Sinh Thái Quy Mô Lên Đến 30.000 m²</h2>
        <p class="editorial-section-sub">
          Dành trọn hơn 30.000m² không gian xanh và mặt nước cho hệ sinh thái 76 tiện ích đa tầng khép kín (50 tiện ích Phân khu Trung Tâm &amp; 26 tiện ích Phân khu Ven Hồ): từ tổ hợp thể thao mặt nước hồ 100ha, cụm sân Pickleball &amp; Bóng rổ, Việt Mã Viên đến Bờ Sen (Spa, Hồ bơi &amp; Thiền), Nhà hàng Nếp Nhà Việt và Nhà hàng Vị Thủy.
        </p>
      </div>

      <!-- Sơ Đồ Phân Bổ 2 Phân Khu Tiện Ích -->'''

html = html[:old_sec3_header.start()] + new_sec3_header + html[old_sec3_header.end():]


# ==============================================================================
# 5. UPDATE SECTION 4 (#tap-chi)
# ==============================================================================

old_sec4_header = re.search(r'<div class="hht-mag-header">.*?</div>', html, re.DOTALL)
if old_sec4_header:
    new_sec4_header = '''<div class="editorial-section-header">
          <span class="editorial-eyebrow"><i class="fa-solid fa-newspaper"></i> GÓC NHÌN &amp; TÍCH SẢN</span>
          <h2 class="editorial-section-title">Tạp Chí &amp; Nhận Định</h2>
          <p class="editorial-section-sub">
            Những ấn phẩm chuyên sâu về tài sản, phong cách sống và nghệ thuật thưởng lãm tinh hoa.
          </p>
        </div>'''
    html = html[:old_sec4_header.start()] + new_sec4_header + html[old_sec4_header.end():]


# ==============================================================================
# 6. UPDATE SECTION 5 (#vi-tri)
# ==============================================================================

old_sec5_header = re.search(r'<div class="section-header-wrap".*?</div>', html, re.DOTALL)
if old_sec5_header:
    new_sec5_header = '''<div class="editorial-section-header">
        <span class="editorial-eyebrow"><i class="fa-solid fa-map-location-dot"></i> TÂM ĐIỂM KẾT NỐI VÙNG</span>
        <h2 class="editorial-section-title">Vị Trí &amp; Hướng Dẫn Đường Đi</h2>
        <p class="editorial-section-sub">
          Saigon Farm Resort tọa lạc bên mặt hồ sinh thái 100ha tự nhiên tại Đất Đỏ – Liền kề cung đường biển Hồ Tràm, đón đầu các trục cao tốc huyết mạch và Sân bay Quốc tế Long Thành.
        </p>
      </div>'''
    html = html[:old_sec5_header.start()] + new_sec5_header + html[old_sec5_header.end():]


with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("SUCCESS: index.html typography hierarchy unified!")
