import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Header Navigation Links & Tabs
html = html.replace('data-target="tab-villas-market">Biệt Thự Mở Bán</a>', 'data-target="tab-villas-market">Biệt Phủ Điền Trang</a>')
html = html.replace('data-target="tab-eco-villas">Villas Sinh Thái</a>', 'data-target="tab-eco-villas">Điền Trang Sinh Thái</a>')
html = html.replace('data-target="tab-amenities">Tiện Ích Resort</a>', 'data-target="tab-amenities">Tiện Ích Điền Trang</a>')

# Mobile drawer menu
html = html.replace('<i class="fa-solid fa-house-chimney" style="width:20px;margin-right:8px;"></i>Biệt Thự Mở Bán', '<i class="fa-solid fa-landmark-dome" style="width:20px;margin-right:8px;"></i>Biệt Phủ Điền Trang')
html = html.replace('<i class="fa-solid fa-tree" style="width:20px;margin-right:8px;"></i>Villas Sinh Thái', '<i class="fa-solid fa-tree" style="width:20px;margin-right:8px;"></i>Điền Trang Sinh Thái')
html = html.replace('<i class="fa-solid fa-spa" style="width:20px;margin-right:8px;"></i>Tiện Ích Resort', '<i class="fa-solid fa-spa" style="width:20px;margin-right:8px;"></i>Tiện Ích Điền Trang')

# Hero text
html = html.replace('Bộ Sưu Tập Biệt Thự Vườn Sinh Thái 1.000m² – 1.500m² Liền Kề Hồ Tràm', 'Bộ Sưu Tập Biệt Phủ Điền Trang Sinh Thái 1.000m² – 1.500m² Liền Kề Hồ Tràm')
html = html.replace('Khu Nghỉ Dưỡng Sinh Thái Ven Hồ 100ha', 'Quần Thể Điền Trang Nghỉ Dưỡng Sinh Thái Ven Hồ 100ha')

# Tab buttons in tabs-header
tab_buttons_old = """<button class="tab-btn active" data-tab="tab-villas-market">
  Biệt Thự Mở Bán
  <span style="background:#c9a96e; color:#000; font-size:0.65rem; font-weight:700; padding:2px 6px; border-radius:3px; margin-left:6px;">HOT</span>
</button>
<button class="tab-btn" data-tab="tab-heritage">
  Bản Sắc Việt
  <span style="background:#2e7d32; color:#fff; font-size:0.65rem; font-weight:700; padding:2px 6px; border-radius:3px; margin-left:6px;">ĐẶC QUYỀN</span>
</button>
<button class="tab-btn" data-tab="tab-eco-villas">Villas Sinh Thái</button>
<button class="tab-btn" data-tab="tab-amenities">Tiện Ích & Trải Nghiệm</button>
<button class="tab-btn" data-tab="tab-masterplan">Mặt Bằng Phân Khu</button>
<button class="tab-btn" data-tab="tab-editorial">Xu Hướng & Tạp Chí</button>"""

tab_buttons_new = """<button class="tab-btn active" data-tab="tab-villas-market">
  Biệt Phủ Điền Trang
  <span style="background:#c9a96e; color:#000; font-size:0.65rem; font-weight:700; padding:2px 6px; border-radius:3px; margin-left:6px;">HOT</span>
</button>
<button class="tab-btn" data-tab="tab-heritage">
  Bản Sắc Việt
  <span style="background:#2e7d32; color:#fff; font-size:0.65rem; font-weight:700; padding:2px 6px; border-radius:3px; margin-left:6px;">ĐẶC QUYỀN</span>
</button>
<button class="tab-btn" data-tab="tab-eco-villas">Điền Trang Sinh Thái</button>
<button class="tab-btn" data-tab="tab-amenities">Tiện Ích Điền Trang</button>
<button class="tab-btn" data-tab="tab-masterplan">Mặt Bằng & Quy Hoạch</button>
<button class="tab-btn" data-tab="tab-editorial">Xu Hướng & Tạp Chí</button>"""

html = html.replace(tab_buttons_old, tab_buttons_new)

# 2. Build Tab 1: Biệt Phủ Điền Trang (4 Ô Ngang Nổi Bật, không chứa bài viết phân tích)
tab_villas_market_html = """<!-- Tab 1: Biệt Phủ Điền Trang (tab-villas-market) -->
<div class="tab-content active" id="tab-villas-market">
  <!-- Intro Banner: 4 Loại Hình Biệt Phủ Điền Trang -->
  <div style="background: linear-gradient(135deg, rgba(201,169,110,0.2) 0%, rgba(17,17,17,0.94) 100%), url('assets/Index_asset/Phoicanh/S01_Final_Fix.jpg') center/cover; padding: 38px 24px; border-radius: 10px; margin-bottom: 32px; border: 1px solid rgba(201,169,110,0.4); text-align: center; box-shadow: 0 8px 30px rgba(0,0,0,0.35);">
    <span style="background: #c9a96e; color: #000; font-size: 0.75rem; font-weight: 800; padding: 5px 16px; border-radius: 20px; letter-spacing: 0.1em; text-transform: uppercase;">DANH MỤC BIỆT PHỦ MỞ BÁN</span>
    <h3 style="font-family: var(--font-serif); font-size: clamp(1.5rem, 3vw, 2.3rem); color: #fff; margin: 14px 0 8px;">BỘ SƯU TẬP 4 LOẠI HÌNH BIỆT PHỦ ĐIỀN TRANG</h3>
    <p style="max-width: 850px; margin: 0 auto; color: #ddd; font-size: 0.98rem; line-height: 1.6;">
      Quy tụ 4 tuyệt tác kiến trúc điền trang sinh thái độc bản ven mặt hồ 100ha: <strong>Điền Trang Sunrise 1, Dinh Thự Sunrise 2, Điền Trang Sunset 1, Điền Trang Sunset 2</strong> với khuôn viên riêng từ 1.000m² – 1.500m².
    </p>
  </div>

  <!-- 4 Ô Ngang: 4 Core Estate Models Showcase Cards -->
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 22px; margin-bottom: 25px;">
    
    <!-- Model 1: Điền Trang Sunrise 1 -->
    <div class="grid-card" style="border-radius: 10px; overflow: hidden; background: #fff; box-shadow: 0 6px 24px rgba(0,0,0,0.07); border: 1px solid #e0d5c1; display: flex; flex-direction: column; height: 100%;">
      <div class="grid-img" style="position: relative; height: 230px;">
        <img alt="Điền Trang Sunrise 1" src="assets/Index_asset/02_Phoi_Canh_3D/09.3D_TKCS-SUNRISE_VILLA/05.3D_TKCS-SUNRISE_1_VILLA/05.3D_TKCS-NHA_GO_4_MAU_1-_07.2025/01._NGOAI_THAT/SFR_NGOAI_THAT_06.jpg" style="width:100%; height:100%; object-fit:cover;"/>
        <span style="position: absolute; top: 12px; left: 12px; background: #c9a96e; color: #000; font-size: 0.72rem; font-weight: 800; padding: 4px 10px; border-radius: 4px; letter-spacing: 0.03em;">3PN TRỆT • ĐÓN BÌNH MINH</span>
        <span class="minh-hoa-tag">* Hình ảnh minh họa</span>
      </div>
      <div class="grid-card-info" style="padding: 20px; display: flex; flex-direction: column; flex-grow: 1; justify-content: space-between;">
        <div>
          <h4 style="font-size: 1.2rem; margin-bottom: 8px; font-family: var(--font-serif); color: #111;">Điền Trang Sunrise 1</h4>
          <p style="font-size: 0.85rem; color: #8a6d3b; font-weight: 700; margin-bottom: 12px;">Biệt Phủ 1 Tầng • Hướng Đông Phong Thủy</p>
          <ul style="font-size: 0.86rem; color: #555; padding-left: 18px; margin-bottom: 15px; line-height: 1.6;">
            <li><strong>Khuôn viên:</strong> 1.000m² - 1.200m²</li>
            <li><strong>Quy mô:</strong> 1 Tầng • 3 Phòng ngủ khép kín</li>
            <li><strong>Hồ bơi riêng:</strong> 45m² lọc khoáng muối</li>
            <li><strong>Sân vườn:</strong> Vườn hoa thảo mộc > 700m²</li>
            <li><strong>Đặc quyền:</strong> Mặt bằng phẳng tiện nghi cho đa thế hệ</li>
          </ul>
        </div>
        <div style="border-top: 1px solid #f0ebe1; padding-top: 14px; display: flex; justify-content: space-between; align-items: center;">
          <div>
            <span style="display:block; font-size:0.75rem; color:#888;">Tình trạng</span>
            <span style="color: #2e7d32; font-weight: 800; font-size: 0.95rem;">Đang Mở Bán</span>
          </div>
          <a href="article.html?id=103" class="editorial-btn" style="padding: 6px 14px; font-size: 0.8rem; text-decoration: none;">Xem Chi Tiết</a>
        </div>
      </div>
    </div>

    <!-- Model 2: Dinh Thự Sunrise 2 -->
    <div class="grid-card" style="border-radius: 10px; overflow: hidden; background: #fff; box-shadow: 0 6px 24px rgba(0,0,0,0.07); border: 2px solid #c9a96e; display: flex; flex-direction: column; height: 100%;">
      <div class="grid-img" style="position: relative; height: 230px;">
        <img alt="Dinh Thự Sunrise 2" src="assets/Index_asset/02_Phoi_Canh_3D/07.3D_TKCS-NHA_GO_4_MAU_2-_02.2026/07.TKCS-NHA_GO_4-MAU_2/01.NGOAI_THAT/SFR_01.jpg" style="width:100%; height:100%; object-fit:cover;"/>
        <span style="position: absolute; top: 12px; left: 12px; background: #0068FF; color: #fff; font-size: 0.72rem; font-weight: 800; padding: 4px 10px; border-radius: 4px; letter-spacing: 0.03em;">DINH THỰ SIÊU VIP • 1.500M²</span>
        <span class="minh-hoa-tag">* Hình ảnh minh họa</span>
      </div>
      <div class="grid-card-info" style="padding: 20px; display: flex; flex-direction: column; flex-grow: 1; justify-content: space-between;">
        <div>
          <h4 style="font-size: 1.2rem; margin-bottom: 8px; font-family: var(--font-serif); color: #8a6d3b;">Dinh Thự Sunrise 2</h4>
          <p style="font-size: 0.85rem; color: #0068FF; font-weight: 700; margin-bottom: 12px;">Đại Điền Trang 4PN • Trực Diện Hồ 100ha</p>
          <ul style="font-size: 0.86rem; color: #555; padding-left: 18px; margin-bottom: 15px; line-height: 1.6;">
            <li><strong>Khuôn viên:</strong> 1.500m² (Đơn Lập Siêu VIP)</li>
            <li><strong>Quy mô:</strong> 4 Phòng ngủ Master khép kín</li>
            <li><strong>Kiến trúc:</strong> Đại sảnh trần cao gỗ quý 6m</li>
            <li><strong>Hồ bơi vô cực:</strong> 53m² Jacuzzi nước ấm</li>
            <li><strong>Đặc quyền:</strong> Sky Deck 40m², bãi Gala 80 khách</li>
          </ul>
        </div>
        <div style="border-top: 1px solid #f0ebe1; padding-top: 14px; display: flex; justify-content: space-between; align-items: center;">
          <div>
            <span style="display:block; font-size:0.75rem; color:#888;">Tình trạng</span>
            <span style="color: #8a6d3b; font-weight: 800; font-size: 0.95rem;">Suất Giới Hạn</span>
          </div>
          <a href="article.html?id=104" class="editorial-btn" style="padding: 6px 14px; font-size: 0.8rem; background: #8a6d3b; color:#fff; border-color:#8a6d3b; text-decoration: none;">Dinh Thự VIP</a>
        </div>
      </div>
    </div>

    <!-- Model 3: Điền Trang Sunset 1 -->
    <div class="grid-card" style="border-radius: 10px; overflow: hidden; background: #fff; box-shadow: 0 6px 24px rgba(0,0,0,0.07); border: 1px solid #e0d5c1; display: flex; flex-direction: column; height: 100%;">
      <div class="grid-img" style="position: relative; height: 230px;">
        <img alt="Điền Trang Sunset 1" src="assets/Index_asset/02_Phoi_Canh_3D/09.3D_TKCS-SUNSET_VILLA/SUNSET_1_VILLA/SFR_07.SAN_TRONG.jpg" style="width:100%; height:100%; object-fit:cover;"/>
        <span style="position: absolute; top: 12px; left: 12px; background: #c9a96e; color: #000; font-size: 0.72rem; font-weight: 800; padding: 4px 10px; border-radius: 4px; letter-spacing: 0.03em;">3PN TRỆT • SÂN TRONG GIẾNG TRỜI</span>
        <span class="minh-hoa-tag">* Hình ảnh minh họa</span>
      </div>
      <div class="grid-card-info" style="padding: 20px; display: flex; flex-direction: column; flex-grow: 1; justify-content: space-between;">
        <div>
          <h4 style="font-size: 1.2rem; margin-bottom: 8px; font-family: var(--font-serif); color: #111;">Điền Trang Sunset 1</h4>
          <p style="font-size: 0.85rem; color: #8a6d3b; font-weight: 700; margin-bottom: 12px;">Biệt Phủ Sân Trong • View Hoàng Hôn</p>
          <ul style="font-size: 0.86rem; color: #555; padding-left: 18px; margin-bottom: 15px; line-height: 1.6;">
            <li><strong>Khuôn viên:</strong> ~1.000m² thế đất vuông vắn</li>
            <li><strong>Quy mô:</strong> 1 Tầng • 3 Phòng ngủ Master</li>
            <li><strong>Sân trong (Courtyard):</strong> 38m² giếng trời thông gió</li>
            <li><strong>Hồ bơi riêng:</strong> 45m² tràn viền</li>
            <li><strong>Vườn ăn trái:</strong> 260m² cây trái nhiệt đới</li>
          </ul>
        </div>
        <div style="border-top: 1px solid #f0ebe1; padding-top: 14px; display: flex; justify-content: space-between; align-items: center;">
          <div>
            <span style="display:block; font-size:0.75rem; color:#888;">Tình trạng</span>
            <span style="color: #2e7d32; font-weight: 800; font-size: 0.95rem;">Đang Mở Bán</span>
          </div>
          <a href="article.html?id=101" class="editorial-btn" style="padding: 6px 14px; font-size: 0.8rem; text-decoration: none;">Xem Chi Tiết</a>
        </div>
      </div>
    </div>

    <!-- Model 4: Điền Trang Sunset 2 -->
    <div class="grid-card" style="border-radius: 10px; overflow: hidden; background: #fff; box-shadow: 0 6px 24px rgba(0,0,0,0.07); border: 1px solid #e0d5c1; display: flex; flex-direction: column; height: 100%;">
      <div class="grid-img" style="position: relative; height: 230px;">
        <img alt="Điền Trang Sunset 2" src="assets/Index_asset/02_Phoi_Canh_3D/09.3D_TKCS-SUNSET_VILLA/SUNSET_2_VILLA/SFR_04.PC_01.jpg" style="width:100%; height:100%; object-fit:cover;"/>
        <span style="position: absolute; top: 12px; left: 12px; background: #2e7d32; color: #fff; font-size: 0.72rem; font-weight: 800; padding: 4px 10px; border-radius: 4px; letter-spacing: 0.03em;">2 TẦNG BỀ THẾ • 1.200M²</span>
        <span class="minh-hoa-tag">* Hình ảnh minh họa</span>
      </div>
      <div class="grid-card-info" style="padding: 20px; display: flex; flex-direction: column; flex-grow: 1; justify-content: space-between;">
        <div>
          <h4 style="font-size: 1.2rem; margin-bottom: 8px; font-family: var(--font-serif); color: #111;">Điền Trang Sunset 2</h4>
          <p style="font-size: 0.85rem; color: #2e7d32; font-weight: 700; margin-bottom: 12px;">Biệt Phủ 2 Tầng • Sunset Lounge Lầu 1</p>
          <ul style="font-size: 0.86rem; color: #555; padding-left: 18px; margin-bottom: 15px; line-height: 1.6;">
            <li><strong>Khuôn viên:</strong> 1.200m² tầm nhìn thoáng đãng</li>
            <li><strong>Quy mô:</strong> 2 Tầng • 3PN Master • 4 WC</li>
            <li><strong>Vườn ăn trái:</strong> 482m² sum suê trù phú</li>
            <li><strong>Hồ bơi vô cực:</strong> 48m² kết nối sàn gỗ Teak</li>
            <li><strong>Ban công Sky Lounge:</strong> 35m² ngắm trọn hoàng hôn</li>
          </ul>
        </div>
        <div style="border-top: 1px solid #f0ebe1; padding-top: 14px; display: flex; justify-content: space-between; align-items: center;">
          <div>
            <span style="display:block; font-size:0.75rem; color:#888;">Tình trạng</span>
            <span style="color: #2e7d32; font-weight: 800; font-size: 0.95rem;">Đang Mở Bán</span>
          </div>
          <a href="article.html?id=102" class="editorial-btn" style="padding: 6px 14px; font-size: 0.8rem; text-decoration: none;">Xem Chi Tiết</a>
        </div>
      </div>
    </div>

  </div>

  <div style="text-align: right; margin-top: 14px; font-size: 0.78rem; color: #888; font-style: italic;">* Lưu ý: Toàn bộ thông tin, mặt bằng kiến trúc và hình ảnh tiện ích mang tính chất minh họa theo định hướng phát triển thực tế của quần thể điền trang.</div>
</div>"""

pattern_villas = re.compile(r'<!-- Tab 1: Biệt Thự Mở Bán \(tab-villas-market\) -->.*?(?=<!-- Tab: Bản Sắc Việt \(tab-heritage\) -->)', re.DOTALL)
if pattern_villas.search(html):
    html = pattern_villas.sub(tab_villas_market_html + "\n\n", html)
    print("Replaced tab-villas-market with 4 horizontal estate cards successfully.")
else:
    print("Could not find tab-villas-market pattern.")

# 3. Build Tab 5: Mặt Bằng & Quy Hoạch (Chứa Mặt Bằng + 16 Chuyên Đề Phân Tích Đa Góc Độ)
tab_masterplan_html = """<!-- Tab 4: Mặt Bằng & Quy Hoạch (tab-masterplan) -->
<div class="tab-content" id="tab-masterplan">
  
  <!-- Phối Cảnh & Quy Hoạch Tổng Thể -->
  <div class="top-listings-grid">
    <!-- Top 1: Phối cảnh tổng thể -->
    <a class="top-listing-card" href="article.html?id=122" style="text-decoration: none; color: inherit; display: block;">
      <div class="top-listing-img" style="background-image: url('assets/Index_asset/Phoicanh/S01_Final_Fix.jpg');"></div>
      <span class="top-listing-minh-hoa">* Hình ảnh minh họa</span>
      <div class="top-listing-info">
        <h4>Phối Cảnh Toàn Cảnh Điền Trang 100ha</h4>
        <p>Tổng quan hệ tiện ích sinh thái đa tầng khép kín</p>
      </div>
    </a>
    <!-- Top 2: Sơ đồ liên kết vùng -->
    <a class="top-listing-card" href="article.html?id=125" style="text-decoration: none; color: inherit; display: block;">
      <div class="top-listing-img" style="background-image: url('assets/Index_asset/MatBang/SoDo_LienKet_Vung.png');"></div>
      <span class="top-listing-minh-hoa">* Hình ảnh minh họa</span>
      <div class="top-listing-info">
        <h4>Sơ Đồ Liên Kết Vùng Giao Thương</h4>
        <p>55 phút về TP.HCM • 25 phút đến Sân bay Long Thành</p>
      </div>
    </a>
    <!-- Top 3: Phối cảnh trên cao -->
    <a class="top-listing-card" href="article.html?id=303" style="text-decoration: none; color: inherit; display: block;">
      <div class="top-listing-img" style="background-image: url('assets/Index_asset/Phoicanh/NEW_S02.jpg');"></div>
      <span class="top-listing-minh-hoa">* Hình ảnh minh họa</span>
      <div class="top-listing-info">
        <h4>Quy Hoạch & Pháp Lý Minh Bạch</h4>
        <p>Sổ đỏ riêng từng khuôn viên điền trang • Sở hữu bền vững</p>
      </div>
    </a>
  </div>

  <!-- Mặt Bằng 4 Loại Hình Điền Trang Chi Tiết -->
  <div style="margin: 35px 0 20px;">
    <h3 style="font-family: var(--font-serif); font-size: 1.45rem; color: #111; margin-bottom: 6px;">
      <i class="fa-solid fa-layer-group" style="color: #c9a96e; margin-right: 8px;"></i>MẶT BẰNG CÔNG NĂNG 4 LOẠI HÌNH ĐIỀN TRANG
    </h3>
    <p style="color: #666; font-size: 0.92rem;">Chi tiết bố cục không gian, giao thông và công năng nội khu của từng mẫu biệt phủ điền trang.</p>
  </div>

  <div class="grid-listing">
    <!-- MB Sunrise 1 -->
    <a class="grid-card" href="article.html?id=103" style="text-decoration: none; color: inherit; display: block;">
      <div class="grid-img"><img alt="Mặt bằng Điền Trang Sunrise 1" src="assets/Index_asset/Loai_hinh_Villa/MatBang_Sunrise_1.png"/><span class="minh-hoa-tag">* Hình ảnh minh họa</span></div>
      <div class="grid-card-info">
        <h5>Mặt Bằng Điền Trang Sunrise 1 (1 Tầng Trệt)</h5>
        <p class="grid-card-subtitle">Khuôn viên 1.000m² - 1.200m², layout trải ngang đón nắng bình minh</p>
        <p class="grid-price">Xem Chi Tiết Công Năng</p>
      </div>
    </a>
    <!-- MB Sunrise 2 -->
    <a class="grid-card" href="article.html?id=104" style="text-decoration: none; color: inherit; display: block;">
      <div class="grid-img"><img alt="Mặt bằng Dinh Thự Sunrise 2" src="assets/Index_asset/Loai_hinh_Villa/MatBang_Sunrise_2.png"/><span class="minh-hoa-tag">* Hình ảnh minh họa</span></div>
      <div class="grid-card-info">
        <h5>Mặt Bằng Dinh Thự Sunrise 2 (1.500m² VIP)</h5>
        <p class="grid-card-subtitle">Đại sảnh gỗ quý trần cao 6m, 4PN Master, Sky Deck 40m²</p>
        <p class="grid-price">Xem Chi Tiết Công Năng</p>
      </div>
    </a>
    <!-- MB Sunset 1 -->
    <a class="grid-card" href="article.html?id=101" style="text-decoration: none; color: inherit; display: block;">
      <div class="grid-img"><img alt="Mặt bằng Điền Trang Sunset 1" src="assets/Index_asset/Loai_hinh_Villa/MatBang_Sunset_1.png"/><span class="minh-hoa-tag">* Hình ảnh minh họa</span></div>
      <div class="grid-card-info">
        <h5>Mặt Bằng Điền Trang Sunset 1 (Sân Trong)</h5>
        <p class="grid-card-subtitle">Khuôn viên 1.000m², sân trong 38m², vườn cây ăn trái 260m²</p>
        <p class="grid-price">Xem Chi Tiết Công Năng</p>
      </div>
    </a>
    <!-- MB Sunset 2 -->
    <a class="grid-card" href="article.html?id=102" style="text-decoration: none; color: inherit; display: block;">
      <div class="grid-img"><img alt="Mặt bằng Điền Trang Sunset 2" src="assets/Index_asset/Loai_hinh_Villa/MatBang_Sunset_2.png"/><span class="minh-hoa-tag">* Hình ảnh minh họa</span></div>
      <div class="grid-card-info">
        <h5>Mặt Bằng Điền Trang Sunset 2 (2 Tầng)</h5>
        <p class="grid-card-subtitle">Khuôn viên 1.200m², vườn ăn trái 482m², ban công ngắm hoàng hôn</p>
        <p class="grid-price">Xem Chi Tiết Công Năng</p>
      </div>
    </a>
    <!-- Vận hành MDS -->
    <a class="grid-card" href="article.html?id=506" style="text-decoration: none; color: inherit; display: block;">
      <div class="grid-img"><img alt="Vận hành MDS" src="assets/Index_asset/MatBang/QuanLy_MDS_Living.png"/><span class="minh-hoa-tag">* Hình ảnh minh họa</span></div>
      <div class="grid-card-info">
        <h5>Mô Hình Vận Hành MDS Living</h5>
        <p class="grid-card-subtitle">4 trụ cột chăm sóc xúc cảm & tối ưu dòng tiền cho gia chủ</p>
        <p class="grid-price">Xem Chi Tiết Vận Hành</p>
      </div>
    </a>
    <!-- Quy mô -->
    <a class="grid-card" href="article.html?id=303" style="text-decoration: none; color: inherit; display: block;">
      <div class="grid-img"><img alt="Quy mô tổng quan" src="assets/Index_asset/MatBang/TongQuan_QuyMo.png"/><span class="minh-hoa-tag">* Hình ảnh minh họa</span></div>
      <div class="grid-card-info">
        <h5>Tổng Quan Quy Mô Phân Khu Điền Trang</h5>
        <p class="grid-card-subtitle">Phân bổ không gian xanh, mặt nước và các trục giao thông chính</p>
        <p class="grid-price">Xem Sơ Đồ Quy Hoạch</p>
      </div>
    </a>
  </div>

  <!-- 16 CHUYÊN ĐỀ PHÂN TÍCH SECTION (CHUYỂN SANG MẶT BẰNG & QUY HOẠCH) -->
  <div style="background: #fdfbf7; border: 1px solid #e0d5c1; border-radius: 10px; padding: 34px 22px; margin-top: 45px; box-shadow: 0 4px 20px rgba(0,0,0,0.04);">
    <div style="text-align: center; margin-bottom: 26px;">
      <span style="background: #c9a96e; color: #000; font-size: 0.72rem; font-weight: 700; padding: 4px 14px; border-radius: 20px; text-transform: uppercase; letter-spacing: 0.05em;">GÓC NHÌN CHUYÊN GIA & PHÂN TÍCH MẶT BẰNG</span>
      <h3 style="font-family: var(--font-serif); font-size: clamp(1.4rem, 2.5vw, 1.95rem); margin-top: 10px; color: #111;">
        16 CHUYÊN ĐỀ PHÂN TÍCH MẶT BẰNG & GÓC NHÌN ĐIỀN TRANG
      </h3>
      <p style="color: #666; font-size: 0.93rem; max-width: 780px; margin: 6px auto 0;">
        Bóc tách toàn diện 4 góc độ chuyên sâu của 4 mẫu điền trang (Sunrise 1, Sunrise 2, Sunset 1, Sunset 2): Mặt bằng & Kiến trúc • Phong thủy & Vi khí hậu • Trải nghiệm & Dưỡng sinh • Suất đầu tư & Tích sản.
      </p>
    </div>

    <!-- Sub tabs navigation -->
    <div class="sub-tabs-header" style="justify-content: center; flex-wrap: wrap; gap: 8px; margin-bottom: 25px;">
      <button class="sub-tab-btn active" data-subtab="subtab-villa-layout">
        <i class="fa-solid fa-ruler-combined" style="margin-right:6px;"></i>1. Mặt Bằng & Kiến Trúc (4 Bài)
      </button>
      <button class="sub-tab-btn" data-subtab="subtab-villa-climate">
        <i class="fa-solid fa-compass" style="margin-right:6px;"></i>2. Phong Thủy & Vi Khí Hậu (4 Bài)
      </button>
      <button class="sub-tab-btn" data-subtab="subtab-villa-experience">
        <i class="fa-solid fa-spa" style="margin-right:6px;"></i>3. Trải Nghiệm & Dưỡng Sinh (4 Bài)
      </button>
      <button class="sub-tab-btn" data-subtab="subtab-villa-investment">
        <i class="fa-solid fa-chart-line" style="margin-right:6px;"></i>4. Đầu Tư & Tích Sản (4 Bài)
      </button>
    </div>

    <!-- Sub-tab 1: Mặt Bằng & Kiến Trúc -->
    <div class="sub-tab-content active" id="subtab-villa-layout">
      <div class="grid-listing">
        <a class="grid-card" href="article.html?id=103" style="text-decoration: none; color: inherit; display: block;">
          <div class="grid-img"><img alt="Điền Trang Sunrise 1 Mặt bằng" src="assets/Index_asset/Loai_hinh_Villa/MatBang_Sunrise_1.png"/><span class="minh-hoa-tag">* Hình ảnh minh họa</span></div>
          <div class="grid-card-info">
            <h5>Điền Trang Sunrise 1: Giải Mã Mặt Bằng 1 Tầng Trệt Trải Rộng</h5>
            <p class="grid-card-subtitle">Phân tích layout trệt trải ngang, tối ưu ánh sáng tự nhiên và luồng giao thông không góc chết</p>
            <p class="grid-price">Chuyên Đề Kiến Trúc</p>
          </div>
        </a>
        <a class="grid-card" href="article.html?id=104" style="text-decoration: none; color: inherit; display: block;">
          <div class="grid-img"><img alt="Dinh Thự Sunrise 2" src="assets/Index_asset/Loai_hinh_Villa/MatBang_Sunrise_2.png"/><span class="minh-hoa-tag">* Hình ảnh minh họa</span></div>
          <div class="grid-card-info">
            <h5>Dinh Thự Sunrise 2: Đỉnh Cao Kiến Trúc Đại Điền Trang 1.500m²</h5>
            <p class="grid-card-subtitle">Không gian đại sảnh trần cao gỗ quý 6m, 4 phòng ngủ Master khép kín và Sky Deck 360°</p>
            <p class="grid-price">Dinh Thự Đẳng Cấp</p>
          </div>
        </a>
        <a class="grid-card" href="article.html?id=101" style="text-decoration: none; color: inherit; display: block;">
          <div class="grid-img"><img alt="Điền Trang Sunset 1 Sân trong" src="assets/Index_asset/Loai_hinh_Villa/MatBang_Sunset_1.png"/><span class="minh-hoa-tag">* Hình ảnh minh họa</span></div>
          <div class="grid-card-info">
            <h5>Điền Trang Sunset 1: Bố Cục Sân Trong (Courtyard) Gắn Kết</h5>
            <p class="grid-card-subtitle">Giải pháp giếng trời sân trong lấy gió chéo và kết nối đa thế hệ trong nếp nhà 1 tầng</p>
            <p class="grid-price">Sân Trong Độc Bản</p>
          </div>
        </a>
        <a class="grid-card" href="article.html?id=102" style="text-decoration: none; color: inherit; display: block;">
          <div class="grid-img"><img alt="Điền Trang Sunset 2" src="assets/Index_asset/Loai_hinh_Villa/MatBang_Sunset_2.png"/><span class="minh-hoa-tag">* Hình ảnh minh họa</span></div>
          <div class="grid-card-info">
            <h5>Điền Trang Sunset 2: Bố Cục Không Gian 2 Tầng Panorama</h5>
            <p class="grid-card-subtitle">Phân tách tĩnh - động hoàn hảo, ban công ngắm hoàng hôn ôm trọn mặt hồ tự nhiên 100ha</p>
            <p class="grid-price">Tầm Nhìn Tuyệt Mỹ</p>
          </div>
        </a>
      </div>
    </div>

    <!-- Sub-tab 2: Phong Thủy & Vi Khí Hậu -->
    <div class="sub-tab-content" id="subtab-villa-climate">
      <div class="grid-listing">
        <a class="grid-card" href="article.html?id=111" style="text-decoration: none; color: inherit; display: block;">
          <div class="grid-img"><img alt="Phong thủy Sunrise" src="assets/Index_asset/02_Phoi_Canh_3D/09.3D_TKCS-SUNRISE_VILLA/05.3D_TKCS-SUNRISE_1_VILLA/05.3D_TKCS-NHA_GO_4_MAU_1-_07.2025/01._NGOAI_THAT/SFR_NGOAI_THAT_(2).jpg"/><span class="minh-hoa-tag">* Hình ảnh minh họa</span></div>
          <div class="grid-card-info">
            <h5>Phong Thủy Điền Trang Hướng Đông: Đón Vượng Khí Nắng Sớm</h5>
            <p class="grid-card-subtitle">Thế đất Tọa Sơn Hướng Thủy, đón photon năng lượng dương tái tạo thể chất và tinh thần</p>
            <p class="grid-price">Phong Thủy Sinh Khí</p>
          </div>
        </a>
        <a class="grid-card" href="article.html?id=112" style="text-decoration: none; color: inherit; display: block;">
          <div class="grid-img"><img alt="Vi khí hậu Sunset" src="assets/Index_asset/02_Phoi_Canh_3D/09.3D_TKCS-SUNSET_VILLA/SUNSET_2_VILLA/SFR_02.MAT_DUNG.jpg"/><span class="minh-hoa-tag">* Hình ảnh minh họa</span></div>
          <div class="grid-card-info">
            <h5>Giải Pháp Vi Khí Hậu Hướng Tây: Lọc Nắng Chiều Êm Dịu</h5>
            <p class="grid-card-subtitle">Sự kết hợp giữa hơi nước hồ 100ha, vườn cây 3 tầng tán và lam chắn nắng nhiệt đới</p>
            <p class="grid-price">Kiến Trúc Nhiệt Đới</p>
          </div>
        </a>
        <a class="grid-card" href="article.html?id=113" style="text-decoration: none; color: inherit; display: block;">
          <div class="grid-img"><img alt="24 Giờ Sinh Thái" src="assets/Index_asset/Phoicanh/S01_Final_Fix.jpg"/><span class="minh-hoa-tag">* Hình ảnh minh họa</span></div>
          <div class="grid-card-info">
            <h5>Trải Nghiệm 24 Giờ Vi Khí Hậu: Sunrise vs Sunset</h5>
            <p class="grid-card-subtitle">Theo dõi nhịp thở sinh thái, biểu đồ nhiệt độ và sự biến chuyển ánh sáng qua từng khung giờ</p>
            <p class="grid-price">Nhịp Sống Tự Nhiên</p>
          </div>
        </a>
        <a class="grid-card" href="article.html?id=114" style="text-decoration: none; color: inherit; display: block;">
          <div class="grid-img"><img alt="Thủy khí hồ 100ha" src="assets/Index_asset/Phoicanh/S01_Final_Fix.jpg"/><span class="minh-hoa-tag">* Hình ảnh minh họa</span></div>
          <div class="grid-card-info">
            <h5>Thủy Khí Hồ 100ha: Trụ Cột Nuôi Dưỡng Sức Khỏe Gia Chủ</h5>
            <p class="grid-card-subtitle">Nồng độ ion âm cực đại, không khí sạch chuẩn quốc tế và hiệu ứng Blue Mind giảm stress</p>
            <p class="grid-price">Dưỡng Sinh Sinh Thái</p>
          </div>
        </a>
      </div>
    </div>

    <!-- Sub-tab 3: Trải Nghiệm Sống, Tiện Ích & Dưỡng Sinh -->
    <div class="sub-tab-content" id="subtab-villa-experience">
      <div class="grid-listing">
        <a class="grid-card" href="article.html?id=115" style="text-decoration: none; color: inherit; display: block;">
          <div class="grid-img"><img alt="Pool & Farm" src="assets/Index_asset/02_Phoi_Canh_3D/09.3D_TKCS-SUNRISE_VILLA/05.3D_TKCS-SUNRISE_1_VILLA/05.3D_TKCS-NHA_GO_4_MAU_1-_07.2025/01._NGOAI_THAT/SFR_NGOAI_THAT_(4).jpg"/><span class="minh-hoa-tag">* Hình ảnh minh họa</span></div>
          <div class="grid-card-info">
            <h5>Đặc Quyền Hồ Bơi Vô Cực & Vườn Nông Trại Riêng</h5>
            <p class="grid-card-subtitle">Bể bơi khoáng muối tự nhiên 45m² và mảnh vườn rau củ quả tự thu hoạch chuẩn Farm-to-Table</p>
            <p class="grid-price">Resort Tại Gia</p>
          </div>
        </a>
        <a class="grid-card" href="article.html?id=116" style="text-decoration: none; color: inherit; display: block;">
          <div class="grid-img"><img alt="Gala Sunrise 2" src="assets/Index_asset/02_Phoi_Canh_3D/07.3D_TKCS-NHA_GO_4_MAU_2-_02.2026/07.TKCS-NHA_GO_4-MAU_2/01.NGOAI_THAT/SFR_03.jpg"/><span class="minh-hoa-tag">* Hình ảnh minh họa</span></div>
          <div class="grid-card-info">
            <h5>Đẳng Cấp Thượng Lưu Sunrise 2: Tiệc Gala 1.500m²</h5>
            <p class="grid-card-subtitle">Không gian tiếp khách ngoại giao bí mật, tiệc sân vườn 80 khách và dịch vụ quản gia MDS Living</p>
            <p class="grid-price">Tiếp Khách Thượng Lưu</p>
          </div>
        </a>
        <a class="grid-card" href="article.html?id=117" style="text-decoration: none; color: inherit; display: block;">
          <div class="grid-img"><img alt="Sunset Lounge" src="assets/Index_asset/02_Phoi_Canh_3D/09.3D_TKCS-SUNSET_VILLA/SUNSET_2_VILLA/SFR_04.PC_02.jpg"/><span class="minh-hoa-tag">* Hình ảnh minh họa</span></div>
          <div class="grid-card-info">
            <h5>Phong Cách Sống 'Sunset Lounge' Tầng Thượng</h5>
            <p class="grid-card-subtitle">Tiệc trà hoàng hôn kiểu Anh, thưởng rượu vang trên ban công 35m² ngắm mặt hồ chuyển màu</p>
            <p class="grid-price">Lối Sống Thời Thượng</p>
          </div>
        </a>
        <a class="grid-card" href="article.html?id=118" style="text-decoration: none; color: inherit; display: block;">
          <div class="grid-img"><img alt="Dưỡng sinh điền trang" src="assets/Index_asset/Tien_ich_minh_hoa/Bo_sen.png"/><span class="minh-hoa-tag">* Hình ảnh minh họa</span></div>
          <div class="grid-card-info">
            <h5>Lối Sống Chữa Lành Thân - Tâm - Trí 24 Giờ</h5>
            <p class="grid-card-subtitle">Lịch trình dưỡng sinh mẫu: Thiền đón bình minh, cưỡi ngựa, Onsen Bờ Sen và thực dưỡng thuần khiết</p>
            <p class="grid-price">Chăm Sóc Toàn Diện</p>
          </div>
        </a>
      </div>
    </div>

    <!-- Sub-tab 4: Suất Đầu Tư, Hiệu Quả & Tích Sản -->
    <div class="sub-tab-content" id="subtab-villa-investment">
      <div class="grid-listing">
        <a class="grid-card" href="article.html?id=119" style="text-decoration: none; color: inherit; display: block;">
          <div class="grid-img"><img alt="Cashflow 3PN" src="assets/Index_asset/02_Phoi_Canh_3D/09.3D_TKCS-SUNSET_VILLA/SUNSET_1_VILLA/SFR_04.PC_01.jpg"/><span class="minh-hoa-tag">* Hình ảnh minh họa</span></div>
          <div class="grid-card-info">
            <h5>Bài Toán Dòng Tiền & Suất Cho Thuê Mẫu 3PN</h5>
            <p class="grid-card-subtitle">So sánh chi phí đầu tư và lợi nhuận ròng hàng năm giữa Sunrise 1 và Sunset 1 qua MDS Living</p>
            <p class="grid-price">Tỷ Suất Sinh Lời Cao</p>
          </div>
        </a>
        <a class="grid-card" href="article.html?id=130" style="text-decoration: none; color: inherit; display: block;">
          <div class="grid-img"><img alt="Di sản Sunrise 2" src="assets/Index_asset/02_Phoi_Canh_3D/07.3D_TKCS-NHA_GO_4_MAU_2-_02.2026/07.TKCS-NHA_GO_4-MAU_2/01.NGOAI_THAT/SFR_04.jpg"/><span class="minh-hoa-tag">* Hình ảnh minh họa</span></div>
          <div class="grid-card-info">
            <h5>Sunrise 2 - Tài Sản Di Sản 1.500m² Khan Hiếm</h5>
            <p class="grid-card-subtitle">Giá trị thặng dư quỹ đất lớn ven hồ 100ha, khả năng chống lạm phát và truyền đời gia tộc</p>
            <p class="grid-price">Tích Sản Trường Tồn</p>
          </div>
        </a>
        <a class="grid-card" href="article.html?id=131" style="text-decoration: none; color: inherit; display: block;">
          <div class="grid-img"><img alt="Lưu trú Sunset 2" src="assets/Index_asset/02_Phoi_Canh_3D/09.3D_TKCS-SUNSET_VILLA/SUNSET_2_VILLA/SFR_04.PC_03.jpg"/><span class="minh-hoa-tag">* Hình ảnh minh họa</span></div>
          <div class="grid-card-info">
            <h5>Tiềm Năng Lưu Trú Cao Cấp Của Điền Trang Sunset 2</h5>
            <p class="grid-card-subtitle">Khai thác nguồn khách chuyên gia Sân bay Quốc tế Long Thành và du khách quốc tế</p>
            <p class="grid-price">Đón Sóng Hạ Tầng</p>
          </div>
        </a>
        <a class="grid-card" href="article.html?id=132" style="text-decoration: none; color: inherit; display: block;">
          <div class="grid-img"><img alt="Ma trận đối sánh" src="assets/Index_asset/Phoicanh/S04_Final_Fix.jpg"/><span class="minh-hoa-tag">* Hình ảnh minh họa</span></div>
          <div class="grid-card-info">
            <h5>Ma Trận Đối Sánh Toàn Diện 4 Mẫu Điền Trang</h5>
            <p class="grid-card-subtitle">Bảng đối chiếu 12 tiêu chí chuyên sâu giúp gia chủ chọn đúng mẫu căn phù hợp nhất</p>
            <p class="grid-price">Cẩm Nang Đầu Tư</p>
          </div>
        </a>
      </div>
    </div>

  </div>

  <div style="text-align: right; margin-top: 18px; font-size: 0.78rem; color: #888; font-style: italic;">* Lưu ý: Toàn bộ thông tin, mặt bằng kiến trúc và hình ảnh tiện ích mang tính chất minh họa theo định hướng phát triển thực tế của quần thể điền trang.</div>
</div>"""

pattern_masterplan = re.compile(r'<!-- Tab 4: Mặt Bằng & Quy Hoạch \(tab-masterplan\) -->.*?(?=<!-- Tab 5: Editorial \(JSON Auto-Publishing\) -->)', re.DOTALL)
if pattern_masterplan.search(html):
    html = pattern_masterplan.sub(tab_masterplan_html + "\n\n", html)
    print("Replaced tab-masterplan successfully.")
else:
    print("Could not find tab-masterplan pattern.")

# 4. Tab 2: Điền Trang Sinh Thái (tab-eco-villas)
tab_eco_villas_html = """<!-- Tab 3: Điền Trang Sinh Thái (tab-eco-villas) -->
<div class="tab-content" id="tab-eco-villas">
  <div style="background: linear-gradient(135deg, rgba(46,125,50,0.18) 0%, rgba(17,17,17,0.92) 100%), url('assets/Index_asset/Phoicanh/NEW_S02.jpg') center/cover; padding: 36px 24px; border-radius: 10px; margin-bottom: 30px; border: 1px solid rgba(46,125,50,0.35); text-align: center; box-shadow: 0 8px 30px rgba(0,0,0,0.35);">
    <span style="background: #2e7d32; color: #fff; font-size: 0.75rem; font-weight: 800; padding: 5px 14px; border-radius: 20px; letter-spacing: 0.1em; text-transform: uppercase;">CHUẨN SỐNG ECO-LUXURY</span>
    <h3 style="font-family: var(--font-serif); font-size: clamp(1.5rem, 3vw, 2.2rem); color: #fff; margin: 14px 0 8px;">4 MẪU BIỆT PHỦ ĐIỀN TRANG SINH THÁI ĐỘC BẢN</h3>
    <p style="max-width: 820px; margin: 0 auto; color: #ddd; font-size: 0.96rem; line-height: 1.6;">
      Sự hòa quyện tuyệt mỹ giữa nếp sống điền trang thuần Việt, vi khí hậu mặt hồ 100ha và tiêu chuẩn quản lý 5 sao từ <strong>MDS Living</strong>.
    </p>
  </div>

  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 20px; margin-bottom: 35px;">
    <!-- Sunrise 1 -->
    <a href="article.html?id=103" class="grid-card" style="text-decoration: none; color: inherit; display: block; border-radius: 8px; overflow: hidden; background: #fff; box-shadow: 0 4px 20px rgba(0,0,0,0.06); border: 1px solid #e0d5c1;">
      <div class="grid-img" style="position: relative; height: 220px;">
        <img alt="Điền Trang Sunrise 1" src="assets/Index_asset/02_Phoi_Canh_3D/09.3D_TKCS-SUNRISE_VILLA/05.3D_TKCS-SUNRISE_1_VILLA/05.3D_TKCS-NHA_GO_4_MAU_1-_07.2025/01._NGOAI_THAT/SFR_NGOAI_THAT_06.jpg" style="width:100%; height:100%; object-fit:cover;"/>
        <span style="position: absolute; top: 12px; left: 12px; background: #c9a96e; color: #000; font-size: 0.7rem; font-weight: 700; padding: 4px 10px; border-radius: 4px;">MẪU 3PN • ĐÓN BÌNH MINH</span>
        <span class="minh-hoa-tag">* Hình ảnh minh họa</span>
      </div>
      <div class="grid-card-info" style="padding: 16px;">
        <h5 style="font-size: 1.1rem; margin-bottom: 6px; font-family: var(--font-serif);">Điền Trang Sunrise 1</h5>
        <p class="grid-card-subtitle" style="font-size: 0.84rem; color: #666; margin-bottom: 8px;">Khuôn viên 1.000m² - 1.200m² • Hồ bơi 45m² • Vườn thảo mộc • 1 Tầng thoáng đãng</p>
        <span style="color: #2e7d32; font-weight: 700; font-size: 0.88rem;">Giá: Liên Hệ Đại Chúng</span>
      </div>
    </a>

    <!-- Sunrise 2 -->
    <a href="article.html?id=104" class="grid-card" style="text-decoration: none; color: inherit; display: block; border-radius: 8px; overflow: hidden; background: #fff; box-shadow: 0 4px 20px rgba(0,0,0,0.06); border: 2px solid #c9a96e;">
      <div class="grid-img" style="position: relative; height: 220px;">
        <img alt="Dinh Thự Sunrise 2" src="assets/Index_asset/02_Phoi_Canh_3D/07.3D_TKCS-NHA_GO_4_MAU_2-_02.2026/07.TKCS-NHA_GO_4-MAU_2/01.NGOAI_THAT/SFR_01.jpg" style="width:100%; height:100%; object-fit:cover;"/>
        <span style="position: absolute; top: 12px; left: 12px; background: #0068FF; color: #fff; font-size: 0.7rem; font-weight: 700; padding: 4px 10px; border-radius: 4px;">DINH THỰ SIÊU VIP • 1.500M²</span>
        <span class="minh-hoa-tag">* Hình ảnh minh họa</span>
      </div>
      <div class="grid-card-info" style="padding: 16px;">
        <h5 style="font-size: 1.1rem; margin-bottom: 6px; font-family: var(--font-serif); color: #8a6d3b;">Dinh Thự Sunrise 2</h5>
        <p class="grid-card-subtitle" style="font-size: 0.84rem; color: #666; margin-bottom: 8px;">Khuôn viên 1.500m² • Hồ bơi vô cực 53m² • Trần cao 6m • Sân thượng 40m²</p>
        <span style="color: #8a6d3b; font-weight: 700; font-size: 0.88rem;">Giá: Liên Hệ Đại Chúng</span>
      </div>
    </a>

    <!-- Sunset 1 -->
    <a href="article.html?id=101" class="grid-card" style="text-decoration: none; color: inherit; display: block; border-radius: 8px; overflow: hidden; background: #fff; box-shadow: 0 4px 20px rgba(0,0,0,0.06); border: 1px solid #e0d5c1;">
      <div class="grid-img" style="position: relative; height: 220px;">
        <img alt="Điền Trang Sunset 1" src="assets/Index_asset/02_Phoi_Canh_3D/09.3D_TKCS-SUNSET_VILLA/SUNSET_1_VILLA/SFR_07.SAN_TRONG.jpg" style="width:100%; height:100%; object-fit:cover;"/>
        <span style="position: absolute; top: 12px; left: 12px; background: #c9a96e; color: #000; font-size: 0.7rem; font-weight: 700; padding: 4px 10px; border-radius: 4px;">MẪU 3PN • SÂN TRONG GIẾNG TRỜI</span>
        <span class="minh-hoa-tag">* Hình ảnh minh họa</span>
      </div>
      <div class="grid-card-info" style="padding: 16px;">
        <h5 style="font-size: 1.1rem; margin-bottom: 6px; font-family: var(--font-serif);">Điền Trang Sunset 1</h5>
        <p class="grid-card-subtitle" style="font-size: 0.84rem; color: #666; margin-bottom: 8px;">Khuôn viên 1.000m² • Sân trong 38m² • Hồ bơi 45m² • Vườn ăn trái hữu cơ 260m²</p>
        <span style="color: #2e7d32; font-weight: 700; font-size: 0.88rem;">Giá: Liên Hệ Đại Chúng</span>
      </div>
    </a>

    <!-- Sunset 2 -->
    <a href="article.html?id=102" class="grid-card" style="text-decoration: none; color: inherit; display: block; border-radius: 8px; overflow: hidden; background: #fff; box-shadow: 0 4px 20px rgba(0,0,0,0.06); border: 1px solid #e0d5c1;">
      <div class="grid-img" style="position: relative; height: 220px;">
        <img alt="Điền Trang Sunset 2" src="assets/Index_asset/02_Phoi_Canh_3D/09.3D_TKCS-SUNSET_VILLA/SUNSET_2_VILLA/SFR_04.PC_01.jpg" style="width:100%; height:100%; object-fit:cover;"/>
        <span style="position: absolute; top: 12px; left: 12px; background: #2e7d32; color: #fff; font-size: 0.7rem; font-weight: 700; padding: 4px 10px; border-radius: 4px;">2 TẦNG BỀ THẾ • 1.200M²</span>
        <span class="minh-hoa-tag">* Hình ảnh minh họa</span>
      </div>
      <div class="grid-card-info" style="padding: 16px;">
        <h5 style="font-size: 1.1rem; margin-bottom: 6px; font-family: var(--font-serif);">Điền Trang Sunset 2</h5>
        <p class="grid-card-subtitle" style="font-size: 0.84rem; color: #666; margin-bottom: 8px;">Khuôn viên 1.200m² • Vườn ăn trái 482m² • Ban công ngắm trọn hoàng hôn</p>
        <span style="color: #2e7d32; font-weight: 700; font-size: 0.88rem;">Giá: Liên Hệ Đại Chúng</span>
      </div>
    </a>
  </div>

  <div style="text-align: center; margin-top: 20px;">
    <a href="#tabs-section" onclick="activateTab('tab-masterplan')" class="editorial-btn" style="background: #111; color: #fff; padding: 12px 28px; border-radius: 4px; font-size: 0.9rem;">
      <i class="fa-solid fa-layer-group" style="margin-right:8px; color:#c9a96e;"></i>Xem Mặt Bằng & 16 Chuyên Đề Phân Tích Điền Trang
    </a>
  </div>

  <div style="text-align: right; margin-top: 18px; font-size: 0.78rem; color: #888; font-style: italic;">* Lưu ý: Toàn bộ thông tin, mặt bằng kiến trúc và hình ảnh tiện ích mang tính chất minh họa theo định hướng phát triển thực tế của quần thể điền trang.</div>
</div>"""

pattern_eco = re.compile(r'<!-- Tab 2: Villas Sinh Thái \(tab-eco-villas\) -->.*?(?=<!-- Tab 3: Tiện Ích Resort \(tab-amenities\) -->)', re.DOTALL)
if pattern_eco.search(html):
    html = pattern_eco.sub(tab_eco_villas_html + "\n\n", html)
    print("Replaced tab-eco-villas successfully.")
else:
    print("Could not find tab-eco-villas pattern.")

# Write updated index.html
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated index.html successfully.")
