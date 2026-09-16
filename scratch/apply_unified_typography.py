import re

# Read current index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. INJECT EDITORIAL CSS
unified_css = '''
    /* ================================================================
       CHUẨN HÓA QUY TẮC ĐỒNG CẤP & TYPOGRAPHY TOÀN BỘ TRANG (EDITORIAL)
       ================================================================ */
    :root {
      --editorial-title-size: clamp(1.6rem, 3.2vw, 2.25rem);
      --editorial-sub-size: clamp(0.92rem, 1.4vw, 1.02rem);
      --editorial-line-height: 1.32;
    }

    /* Khung Header Cấp 1 — Thống nhất 100% CANH TRÁI toàn bộ trang */
    .editorial-section-header {
      text-align: left !important;
      margin-bottom: 24px !important;
      margin-top: 10px !important;
      max-width: 900px !important;
    }

    /* Eyebrow / Category Tag Cấp 1 */
    .editorial-eyebrow {
      display: inline-flex !important;
      align-items: center !important;
      gap: 7px !important;
      font-size: 0.72rem !important;
      font-weight: 800 !important;
      letter-spacing: 0.1em !important;
      text-transform: uppercase !important;
      color: #8c6b32 !important;
      background: #faf3e6 !important;
      border: 1px solid #dfc89f !important;
      padding: 4px 12px !important;
      border-radius: 20px !important;
      margin-bottom: 12px !important;
      line-height: 1.2 !important;
    }

    /* Tiêu đề Section Cấp 1 — Đồng nhất font Playfair, kích thước chuẩn */
    .editorial-section-title {
      font-family: 'Playfair Display', Georgia, serif !important;
      font-size: var(--editorial-title-size) !important;
      font-weight: 700 !important;
      color: #183024 !important;
      line-height: var(--editorial-line-height) !important;
      margin: 0 0 10px 0 !important;
      letter-spacing: -0.015em !important;
      text-align: left !important;
      text-transform: none !important;
    }

    /* Đoạn văn mô tả dưới Tiêu đề Section Cấp 1 */
    .editorial-section-sub {
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif !important;
      font-size: var(--editorial-sub-size) !important;
      color: #555555 !important;
      line-height: 1.68 !important;
      margin: 0 !important;
      max-width: 860px !important;
      font-weight: 400 !important;
      text-align: left !important;
    }

    /* Tiêu đề Phân mục Cấp 2 (Sub-sections) */
    .editorial-sub-header {
      margin-top: 36px !important;
      margin-bottom: 22px !important;
      text-align: left !important;
    }

    .editorial-sub-title {
      font-family: 'Playfair Display', Georgia, serif !important;
      font-size: clamp(1.25rem, 2.2vw, 1.6rem) !important;
      font-weight: 700 !important;
      color: #183024 !important;
      margin: 6px 0 8px 0 !important;
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

# Add CSS if not present
if 'CHUẨN HÓA QUY TẮC ĐỒNG CẤP & TYPOGRAPHY' not in html:
    html = html.replace('</style>', unified_css + '\n  </style>', 1)
else:
    # replace existing block
    html = re.sub(r'/\* =+ CHUẨN HÓA QUY TẮC ĐỒNG CẤP & TYPOGRAPHY.*?\*/.*?(?=\.diagram-lightbox-modal|\.villa-consultation|</style>)', unified_css + '\n', html, flags=re.DOTALL)


# 2. UPDATE SECTION 1 (#partner-toolkit)
# Match from <!-- Header Block --> up to <!-- 5 Trụ Cột Triết Lý
sec1_pattern = re.compile(r'<!-- Header Block -->.*?<!-- 5 Trụ Cột Triết Lý', re.DOTALL)
new_sec1 = '''<!-- Header Block (Đồng Cấp Chuẩn Mực - Canh Trái) -->
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

assert sec1_pattern.search(html), "Could not find Section 1 header"
html = sec1_pattern.sub(new_sec1, html, count=1)


# 3. UPDATE SECTION 2 (#ban-sac)
# 3a. Header of Section 2
sec2_pattern = re.compile(r'<div style="margin-bottom: 22px; margin-top: 12px;">.*?<!-- Top 3 Featured Heritage Cards -->', re.DOTALL)
new_sec2 = '''<div class="editorial-section-header">
      <span class="editorial-eyebrow"><i class="fa-solid fa-feather-pointed"></i> DI SẢN BẢN SẮC VIỆT</span>
      <h2 class="editorial-section-title">Điền Trang Nghỉ Dưỡng Bản Sắc Việt Đương Đại</h2>
      <p class="editorial-section-sub">
        Nơi tinh hoa văn hóa truyền thống 4.000 năm hòa quyện cùng chuẩn sống thượng lưu quốc tế, hệ tiện ích resort độc đáo, nhịp sống lễ hội bốn mùa sống động.
      </p>
    </div>

    <!-- Top 3 Featured Heritage Cards -->'''

assert sec2_pattern.search(html), "Could not find Section 2 header"
html = sec2_pattern.sub(new_sec2, html, count=1)

# 3b. Table wrapper for Interactive Spaces Heritage Table
old_table_pattern = re.compile(r'<!-- Interactive Spaces Heritage Table -->.*?<div style="background: #ffffff; border: 1px solid #dfc89f; border-radius: 12px; padding: 25px 22px; margin: 30px 0; overflow-x: auto; box-shadow: 0 8px 24px rgba\(194, 155, 83, 0.08\);">(.*?)</table>\s*</div>', re.DOTALL)
m_table = old_table_pattern.search(html)
if m_table:
    inner = m_table.group(1)
    t_head_match = re.search(r'(<div.*?style="display: flex; justify-content: space-between;.*?</div>)\s*(<table.*)', inner, re.DOTALL)
    if t_head_match:
        t_head = t_head_match.group(1)
        t_body = t_head_match.group(2)
        new_table_block = f'''<!-- Interactive Spaces Heritage Table -->
    <div class="heritage-table-card">
      {t_head}
      <div class="heritage-table-scroll">
        {t_body}
      </table>
      </div>
    </div>'''
        html = html[:m_table.start()] + new_table_block + html[m_table.end():]

# 3c. 10 Chuyên đề sub-header
cd_pattern = re.compile(r'<!-- 10 Chuyên Đề Văn Hóa & Bản Sắc Việt Showcase -->.*?<div style="text-align: center; margin-bottom: 26px;">.*?BỘ SƯU TẬP 10 CHUYÊN ĐỀ.*?</div>', re.DOTALL)
new_cd = '''<!-- 10 Chuyên Đề Văn Hóa & Bản Sắc Việt Showcase -->
    <div class="editorial-sub-header" style="padding-top: 32px; border-top: 1px solid rgba(201,169,110,0.3);">
      <span class="editorial-eyebrow"><i class="fa-solid fa-book-bookmark"></i> ẤN PHẨM CHUYÊN ĐỀ</span>
      <h3 class="editorial-sub-title">10 Chuyên Đề Văn Hóa &amp; Phong Cách Sống Điền Trang</h3>
      <p class="editorial-section-sub">Chuỗi bài viết chuyên sâu đúc kết triết lý sống, giá trị di sản và phong cách thụ hưởng đích thực của người Việt đương đại.</p>
    </div>'''
if cd_pattern.search(html):
    html = cd_pattern.sub(new_cd, html, count=1)


# 4. UPDATE SECTION 3 (#tien-ich)
sec3_pattern = re.compile(r'<div style="margin-bottom: 24px; margin-top: 12px; text-align: left;">.*?<!-- Sơ Đồ Phân Bổ 2 Phân Khu Tiện Ích -->', re.DOTALL)
new_sec3 = '''<div class="editorial-section-header">
      <span class="editorial-eyebrow"><i class="fa-solid fa-spa"></i> ĐẶC QUYỀN THƯỢNG LƯU KHÉP KÍN</span>
      <h2 class="editorial-section-title">Quần Thể Tiện Ích Sinh Thái Quy Mô Lên Đến 30.000 m²</h2>
      <p class="editorial-section-sub">
        Dành trọn hơn 30.000m² không gian xanh và mặt nước cho hệ sinh thái 76 tiện ích đa tầng khép kín (50 tiện ích Phân khu Trung Tâm &amp; 26 tiện ích Phân khu Ven Hồ): từ tổ hợp thể thao mặt nước hồ 100ha, cụm sân Pickleball &amp; Bóng rổ, Việt Mã Viên đến Bờ Sen (Spa, Hồ bơi &amp; Thiền), Nhà hàng Nếp Nhà Việt và Nhà hàng Vị Thủy.
      </p>
    </div>

    <!-- Sơ Đồ Phân Bổ 2 Phân Khu Tiện Ích -->'''

assert sec3_pattern.search(html), "Could not find Section 3 header"
html = sec3_pattern.sub(new_sec3, html, count=1)


# 5. UPDATE SECTION 4 (#tap-chi)
sec4_pattern = re.compile(r'<div class="hht-mag-header">.*?</div>', re.DOTALL)
new_sec4 = '''<div class="editorial-section-header">
        <span class="editorial-eyebrow"><i class="fa-solid fa-newspaper"></i> GÓC NHÌN &amp; TÍCH SẢN</span>
        <h2 class="editorial-section-title">Tạp Chí &amp; Nhận Định</h2>
        <p class="editorial-section-sub">
          Những ấn phẩm chuyên sâu về tài sản, phong cách sống và nghệ thuật thưởng lãm tinh hoa.
        </p>
      </div>'''
if sec4_pattern.search(html):
    html = sec4_pattern.sub(new_sec4, html, count=1)


# 6. UPDATE SECTION 5 (#vi-tri)
sec5_pattern = re.compile(r'<div class="section-header-wrap" style="text-align: left; max-width: 860px; margin: 0 0 32px 0;">.*?</div>', re.DOTALL)
new_sec5 = '''<div class="editorial-section-header">
      <span class="editorial-eyebrow"><i class="fa-solid fa-map-location-dot"></i> TÂM ĐIỂM KẾT NỐI VÙNG</span>
      <h2 class="editorial-section-title">Vị Trí &amp; Hướng Dẫn Đường Đi</h2>
      <p class="editorial-section-sub">
        Saigon Farm Resort tọa lạc bên mặt hồ sinh thái 100ha tự nhiên tại Đất Đỏ – Liền kề cung đường biển Hồ Tràm, đón đầu các trục cao tốc huyết mạch và Sân bay Quốc tế Long Thành.
      </p>
    </div>'''
if sec5_pattern.search(html):
    html = sec5_pattern.sub(new_sec5, html, count=1)


with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("index.html updated successfully!")
