import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Build the new tab-villas-market content
tab_villas_market_html = """<!-- Tab 1: Biệt Thự Mở Bán (tab-villas-market) -->
<div class="tab-content active" id="tab-villas-market">
  <!-- Intro Banner: 4 Dòng Villa Mở Bán -->
  <div style="background: linear-gradient(135deg, rgba(201,169,110,0.18) 0%, rgba(17,17,17,0.92) 100%), url('assets/Index_asset/Phoicanh/S01_Final_Fix.jpg') center/cover; padding: 36px 24px; border-radius: 10px; margin-bottom: 30px; border: 1px solid rgba(201,169,110,0.35); text-align: center; box-shadow: 0 8px 30px rgba(0,0,0,0.35);">
    <span style="background: #c9a96e; color: #000; font-size: 0.75rem; font-weight: 800; padding: 5px 14px; border-radius: 20px; letter-spacing: 0.1em; text-transform: uppercase;">DANH MỤC SẢN PHẨM CHỦ LỰC</span>
    <h3 style="font-family: var(--font-serif); font-size: clamp(1.5rem, 3vw, 2.2rem); color: #fff; margin: 14px 0 8px;">BỘ SƯU TẬP 4 DÒNG BIỆT THỰ SINH THÁI MỞ BÁN</h3>
    <p style="max-width: 820px; margin: 0 auto; color: #ddd; font-size: 0.96rem; line-height: 1.6;">
      Quy tụ 4 tuyệt tác kiến trúc điền trang độc bản: <strong>Sunrise 1, Sunrise 2, Sunset 1, Sunset 2</strong> với khuôn viên vườn từ 1.000m² – 1.500m² ven mặt hồ 100ha.
    </p>
  </div>

  <!-- 4 Core Villa Models Showcase Cards -->
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(270px, 1fr)); gap: 20px; margin-bottom: 45px;">
    
    <!-- Model 1: Sunrise 1 -->
    <a href="article.html?id=103" class="grid-card" style="text-decoration: none; color: inherit; display: block; border-radius: 8px; overflow: hidden; background: #fff; box-shadow: 0 4px 20px rgba(0,0,0,0.06); border: 1px solid #e0d5c1; transition: transform 0.3s ease;">
      <div class="grid-img" style="position: relative; height: 230px;">
        <img alt="Sunrise 1 Villa" src="assets/Index_asset/02_Phoi_Canh_3D/09.3D_TKCS-SUNRISE_VILLA/05.3D_TKCS-SUNRISE_1_VILLA/05.3D_TKCS-NHA_GO_4_MAU_1-_07.2025/01._NGOAI_THAT/SFR_NGOAI_THAT_06.jpg" style="width:100%; height:100%; object-fit:cover;"/>
        <span style="position: absolute; top: 12px; left: 12px; background: #c9a96e; color: #000; font-size: 0.7rem; font-weight: 700; padding: 4px 10px; border-radius: 4px;">MẪU 3PN • ĐÓN BÌNH MINH</span>
        <span class="minh-hoa-tag">* Hình ảnh minh họa</span>
      </div>
      <div class="grid-card-info" style="padding: 18px;">
        <h5 style="font-size: 1.15rem; margin-bottom: 6px; font-family: var(--font-serif);">Sunrise 1 Villa (3PN Trệt)</h5>
        <p class="grid-card-subtitle" style="font-size: 0.85rem; color: #666; margin-bottom: 10px;">Khuôn viên 1.000m² - 1.200m² • Hồ bơi 45m² • Vườn thảo mộc • Không gian mở 1 tầng</p>
        <div style="display: flex; justify-content: space-between; align-items: center; border-top: 1px solid #f0f0f0; padding-top: 10px;">
          <span style="color: #2e7d32; font-weight: 700; font-size: 0.9rem;">Liên Hệ Báo Giá</span>
          <span class="editorial-btn" style="padding: 4px 12px; font-size: 0.78rem;">Xem Chi Tiết</span>
        </div>
      </div>
    </a>

    <!-- Model 2: Sunrise 2 -->
    <a href="article.html?id=104" class="grid-card" style="text-decoration: none; color: inherit; display: block; border-radius: 8px; overflow: hidden; background: #fff; box-shadow: 0 4px 20px rgba(0,0,0,0.06); border: 2px solid #c9a96e; transition: transform 0.3s ease;">
      <div class="grid-img" style="position: relative; height: 230px;">
        <img alt="Sunrise 2 Villa" src="assets/Index_asset/02_Phoi_Canh_3D/07.3D_TKCS-NHA_GO_4_MAU_2-_02.2026/07.TKCS-NHA_GO_4-MAU_2/01.NGOAI_THAT/SFR_01.jpg" style="width:100%; height:100%; object-fit:cover;"/>
        <span style="position: absolute; top: 12px; left: 12px; background: #0068FF; color: #fff; font-size: 0.7rem; font-weight: 700; padding: 4px 10px; border-radius: 4px;">DINH THỰ SIÊU VIP • 1.500M²</span>
        <span class="minh-hoa-tag">* Hình ảnh minh họa</span>
      </div>
      <div class="grid-card-info" style="padding: 18px;">
        <h5 style="font-size: 1.15rem; margin-bottom: 6px; font-family: var(--font-serif); color: #8a6d3b;">Sunrise 2 Villa (4PN VIP)</h5>
        <p class="grid-card-subtitle" style="font-size: 0.85rem; color: #666; margin-bottom: 10px;">Khuôn viên 1.500m² • Hồ bơi vô cực 53m² • Trần cao 6m • Sân thượng Sky Deck 40m²</p>
        <div style="display: flex; justify-content: space-between; align-items: center; border-top: 1px solid #f0f0f0; padding-top: 10px;">
          <span style="color: #2e7d32; font-weight: 700; font-size: 0.9rem;">Liên Hệ Báo Giá</span>
          <span class="editorial-btn" style="padding: 4px 12px; font-size: 0.78rem; background: #8a6d3b; color:#fff; border-color:#8a6d3b;">Dinh Thự VIP</span>
        </div>
      </div>
    </a>

    <!-- Model 3: Sunset 1 -->
    <a href="article.html?id=101" class="grid-card" style="text-decoration: none; color: inherit; display: block; border-radius: 8px; overflow: hidden; background: #fff; box-shadow: 0 4px 20px rgba(0,0,0,0.06); border: 1px solid #e0d5c1; transition: transform 0.3s ease;">
      <div class="grid-img" style="position: relative; height: 230px;">
        <img alt="Sunset 1 Villa" src="assets/Index_asset/02_Phoi_Canh_3D/09.3D_TKCS-SUNSET_VILLA/SUNSET_1_VILLA/SFR_07.SAN_TRONG.jpg" style="width:100%; height:100%; object-fit:cover;"/>
        <span style="position: absolute; top: 12px; left: 12px; background: #c9a96e; color: #000; font-size: 0.7rem; font-weight: 700; padding: 4px 10px; border-radius: 4px;">MẪU 3PN • SÂN TRONG GIẾNG TRỜI</span>
        <span class="minh-hoa-tag">* Hình ảnh minh họa</span>
      </div>
      <div class="grid-card-info" style="padding: 18px;">
        <h5 style="font-size: 1.15rem; margin-bottom: 6px; font-family: var(--font-serif);">Sunset 1 Villa (3PN - 1 Tầng)</h5>
        <p class="grid-card-subtitle" style="font-size: 0.85rem; color: #666; margin-bottom: 10px;">Khuôn viên 1.000m² • Sân trong 38m² • Hồ bơi 45m² • Vườn ăn trái hữu cơ 260m²</p>
        <div style="display: flex; justify-content: space-between; align-items: center; border-top: 1px solid #f0f0f0; padding-top: 10px;">
          <span style="color: #2e7d32; font-weight: 700; font-size: 0.9rem;">Liên Hệ Báo Giá</span>
          <span class="editorial-btn" style="padding: 4px 12px; font-size: 0.78rem;">Xem Chi Tiết</span>
        </div>
      </div>
    </a>

    <!-- Model 4: Sunset 2 -->
    <a href="article.html?id=102" class="grid-card" style="text-decoration: none; color: inherit; display: block; border-radius: 8px; overflow: hidden; background: #fff; box-shadow: 0 4px 20px rgba(0,0,0,0.06); border: 1px solid #e0d5c1; transition: transform 0.3s ease;">
      <div class="grid-img" style="position: relative; height: 230px;">
        <img alt="Sunset 2 Villa" src="assets/Index_asset/02_Phoi_Canh_3D/09.3D_TKCS-SUNSET_VILLA/SUNSET_2_VILLA/SFR_04.PC_01.jpg" style="width:100%; height:100%; object-fit:cover;"/>
        <span style="position: absolute; top: 12px; left: 12px; background: #2e7d32; color: #fff; font-size: 0.7rem; font-weight: 700; padding: 4px 10px; border-radius: 4px;">2 TẦNG BỀ THẾ • 1.200M²</span>
        <span class="minh-hoa-tag">* Hình ảnh minh họa</span>
      </div>
      <div class="grid-card-info" style="padding: 18px;">
        <h5 style="font-size: 1.15rem; margin-bottom: 6px; font-family: var(--font-serif);">Sunset 2 Villa (3PN - 2 Tầng)</h5>
        <p class="grid-card-subtitle" style="font-size: 0.85rem; color: #666; margin-bottom: 10px;">Khuôn viên 1.200m² • Vườn ăn trái 482m² • Ban công Sky Lounge ngắm hoàng hôn</p>
        <div style="display: flex; justify-content: space-between; align-items: center; border-top: 1px solid #f0f0f0; padding-top: 10px;">
          <span style="color: #2e7d32; font-weight: 700; font-size: 0.9rem;">Liên Hệ Báo Giá</span>
          <span class="editorial-btn" style="padding: 4px 12px; font-size: 0.78rem;">Xem Chi Tiết</span>
        </div>
      </div>
    </a>

  </div>

  <!-- 16 CHUYÊN ĐỀ PHÂN TÍCH SECTION -->
  <div style="background: #fdfbf7; border: 1px solid #e0d5c1; border-radius: 10px; padding: 32px 20px; margin-top: 40px; box-shadow: 0 4px 20px rgba(0,0,0,0.04);">
    <div style="text-align: center; margin-bottom: 25px;">
      <span style="background: #c9a96e; color: #000; font-size: 0.72rem; font-weight: 700; padding: 4px 14px; border-radius: 20px; text-transform: uppercase; letter-spacing: 0.05em;">GÓC NHÌN CHUYÊN GIA</span>
      <h3 style="font-family: var(--font-serif); font-size: clamp(1.4rem, 2.5vw, 1.9rem); margin-top: 10px; color: #111;">
        16 CHUYÊN ĐỀ PHÂN TÍCH ĐA GÓC ĐỘ (SUNRISE 1, 2 & SUNSET 1, 2)
      </h3>
      <p style="color: #666; font-size: 0.92rem; max-width: 750px; margin: 6px auto 0;">
        Bóc tách toàn diện 4 góc độ chuyên sâu: Mặt bằng & Kiến trúc • Phong thủy & Vi khí hậu • Trải nghiệm & Dưỡng sinh • Suất đầu tư & Tích sản.
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
          <div class="grid-img"><img alt="Sunrise 1 Mặt bằng" src="assets/Index_asset/Loai_hinh_Villa/MatBang_Sunrise_1.png"/><span class="minh-hoa-tag">* Hình ảnh minh họa</span></div>
          <div class="grid-card-info">
            <h5>Sunrise 1 Villa: Giải Mã Mặt Bằng 1 Tầng Trệt Trải Rộng</h5>
            <p class="grid-card-subtitle">Phân tích layout trệt trải ngang, tối ưu ánh sáng tự nhiên và luồng giao thông không góc chết</p>
            <p class="grid-price">Chuyên Đề Kiến Trúc</p>
          </div>
        </a>
        <a class="grid-card" href="article.html?id=104" style="text-decoration: none; color: inherit; display: block;">
          <div class="grid-img"><img alt="Sunrise 2 Dinh thự" src="assets/Index_asset/Loai_hinh_Villa/MatBang_Sunrise_2.png"/><span class="minh-hoa-tag">* Hình ảnh minh họa</span></div>
          <div class="grid-card-info">
            <h5>Sunrise 2 Villa: Đỉnh Cao Kiến Trúc Dinh Thự 4PN 1.500m²</h5>
            <p class="grid-card-subtitle">Không gian đại sảnh trần cao gỗ quý 6m, 4 phòng ngủ Master khép kín và Sky Deck 360°</p>
            <p class="grid-price">Dinh Thự Đẳng Cấp</p>
          </div>
        </a>
        <a class="grid-card" href="article.html?id=101" style="text-decoration: none; color: inherit; display: block;">
          <div class="grid-img"><img alt="Sunset 1 Sân trong" src="assets/Index_asset/Loai_hinh_Villa/MatBang_Sunset_1.png"/><span class="minh-hoa-tag">* Hình ảnh minh họa</span></div>
          <div class="grid-card-info">
            <h5>Sunset 1 Villa: Bố Cục Sân Trong (Courtyard) Gắn Kết</h5>
            <p class="grid-card-subtitle">Giải pháp giếng trời sân trong lấy gió chéo và kết nối đa thế hệ trong nếp nhà 1 tầng</p>
            <p class="grid-price">Sân Trong Độc Bản</p>
          </div>
        </a>
        <a class="grid-card" href="article.html?id=102" style="text-decoration: none; color: inherit; display: block;">
          <div class="grid-img"><img alt="Sunset 2 2 Tầng" src="assets/Index_asset/Loai_hinh_Villa/MatBang_Sunset_2.png"/><span class="minh-hoa-tag">* Hình ảnh minh họa</span></div>
          <div class="grid-card-info">
            <h5>Sunset 2 Villa: Bố Cục Không Gian 2 Tầng Panorama</h5>
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
            <h5>Phong Thủy Hướng Đông: Đón Vượng Khí Nắng Sớm</h5>
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
            <h5>Thủy Khí Hồ 100ha: Trụ Cột Nuôi Dưỡng Sức Khỏe</h5>
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
            <h5>Đặc Quyền Hồ Bơi Vô Cực & Vườn Farm Tại Gia</h5>
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
            <h5>Tiềm Năng Lưu Trú Cao Cấp Của Sunset 2</h5>
            <p class="grid-card-subtitle">Khai thác nguồn khách chuyên gia Sân bay Quốc tế Long Thành và du khách quốc tế</p>
            <p class="grid-price">Đón Sóng Hạ Tầng</p>
          </div>
        </a>
        <a class="grid-card" href="article.html?id=132" style="text-decoration: none; color: inherit; display: block;">
          <div class="grid-img"><img alt="Ma trận đối sánh" src="assets/Index_asset/Phoicanh/S04_Final_Fix.jpg"/><span class="minh-hoa-tag">* Hình ảnh minh họa</span></div>
          <div class="grid-card-info">
            <h5>Ma Trận Đối Sánh Toàn Diện 4 Mẫu Villa</h5>
            <p class="grid-card-subtitle">Bảng đối chiếu 12 tiêu chí chuyên sâu giúp gia chủ chọn đúng mẫu căn phù hợp nhất</p>
            <p class="grid-price">Cẩm Nang Đầu Tư</p>
          </div>
        </a>
      </div>
    </div>

  </div>

  <div style="text-align: right; margin-top: 18px; font-size: 0.78rem; color: #888; font-style: italic;">* Lưu ý: Toàn bộ thông tin, mặt bằng kiến trúc và hình ảnh tiện ích mang tính chất minh họa theo định hướng phát triển thực tế của khu điền trang.</div>
</div>"""

# Replace tab-villas-market section using regex
pattern = re.compile(r'<!-- Tab 1: Biệt Thự Mở Bán \(tab-villas-market\) -->.*?(?=<!-- Tab: Bản Sắc Việt \(tab-heritage\) -->)', re.DOTALL)
if pattern.search(html):
    html = pattern.sub(tab_villas_market_html + "\n\n", html)
    print("Replaced tab-villas-market successfully.")
else:
    print("Could not find tab-villas-market pattern.")

# Write updated index.html
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated index.html successfully.")
