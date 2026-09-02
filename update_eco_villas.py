import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

tab_eco_villas_html = """<!-- Tab 2: Villas Sinh Thái (tab-eco-villas) -->
<div class="tab-content" id="tab-eco-villas">
  <div style="background: linear-gradient(135deg, rgba(46,125,50,0.18) 0%, rgba(17,17,17,0.92) 100%), url('assets/Index_asset/Phoicanh/NEW_S02.jpg') center/cover; padding: 36px 24px; border-radius: 10px; margin-bottom: 30px; border: 1px solid rgba(46,125,50,0.35); text-align: center; box-shadow: 0 8px 30px rgba(0,0,0,0.35);">
    <span style="background: #2e7d32; color: #fff; font-size: 0.75rem; font-weight: 800; padding: 5px 14px; border-radius: 20px; letter-spacing: 0.1em; text-transform: uppercase;">CHUẨN SỐNG ECO-LUXURY</span>
    <h3 style="font-family: var(--font-serif); font-size: clamp(1.5rem, 3vw, 2.2rem); color: #fff; margin: 14px 0 8px;">4 MẪU BIỆT THỰ VƯỜN SINH THÁI ĐỘC BẢN</h3>
    <p style="max-width: 820px; margin: 0 auto; color: #ddd; font-size: 0.96rem; line-height: 1.6;">
      Sự hòa quyện tuyệt mỹ giữa nếp sống điền trang thuần Việt, vi khí hậu mặt hồ 100ha và tiêu chuẩn nghỉ dưỡng 5 sao quốc tế từ <strong>MDS Living</strong>.
    </p>
  </div>

  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(270px, 1fr)); gap: 20px; margin-bottom: 35px;">
    <!-- Sunrise 1 -->
    <a href="article.html?id=103" class="grid-card" style="text-decoration: none; color: inherit; display: block; border-radius: 8px; overflow: hidden; background: #fff; box-shadow: 0 4px 20px rgba(0,0,0,0.06); border: 1px solid #e0d5c1;">
      <div class="grid-img" style="position: relative; height: 220px;">
        <img alt="Sunrise 1 Villa" src="assets/Index_asset/02_Phoi_Canh_3D/09.3D_TKCS-SUNRISE_VILLA/05.3D_TKCS-SUNRISE_1_VILLA/05.3D_TKCS-NHA_GO_4_MAU_1-_07.2025/01._NGOAI_THAT/SFR_NGOAI_THAT_06.jpg" style="width:100%; height:100%; object-fit:cover;"/>
        <span style="position: absolute; top: 12px; left: 12px; background: #c9a96e; color: #000; font-size: 0.7rem; font-weight: 700; padding: 4px 10px; border-radius: 4px;">MẪU 3PN • ĐÓN BÌNH MINH</span>
        <span class="minh-hoa-tag">* Hình ảnh minh họa</span>
      </div>
      <div class="grid-card-info" style="padding: 16px;">
        <h5 style="font-size: 1.1rem; margin-bottom: 6px; font-family: var(--font-serif);">Sunrise 1 Villa (3PN Trệt)</h5>
        <p class="grid-card-subtitle" style="font-size: 0.84rem; color: #666; margin-bottom: 8px;">Khuôn viên 1.000m² - 1.200m² • Hồ bơi 45m² • Vườn thảo mộc • 1 Tầng thoáng đãng</p>
        <span style="color: #2e7d32; font-weight: 700; font-size: 0.88rem;">Giá: Liên Hệ Đại Chúng</span>
      </div>
    </a>

    <!-- Sunrise 2 -->
    <a href="article.html?id=104" class="grid-card" style="text-decoration: none; color: inherit; display: block; border-radius: 8px; overflow: hidden; background: #fff; box-shadow: 0 4px 20px rgba(0,0,0,0.06); border: 2px solid #c9a96e;">
      <div class="grid-img" style="position: relative; height: 220px;">
        <img alt="Sunrise 2 Villa" src="assets/Index_asset/02_Phoi_Canh_3D/07.3D_TKCS-NHA_GO_4_MAU_2-_02.2026/07.TKCS-NHA_GO_4-MAU_2/01.NGOAI_THAT/SFR_01.jpg" style="width:100%; height:100%; object-fit:cover;"/>
        <span style="position: absolute; top: 12px; left: 12px; background: #0068FF; color: #fff; font-size: 0.7rem; font-weight: 700; padding: 4px 10px; border-radius: 4px;">DINH THỰ SIÊU VIP • 1.500M²</span>
        <span class="minh-hoa-tag">* Hình ảnh minh họa</span>
      </div>
      <div class="grid-card-info" style="padding: 16px;">
        <h5 style="font-size: 1.1rem; margin-bottom: 6px; font-family: var(--font-serif); color: #8a6d3b;">Sunrise 2 Villa (4PN VIP)</h5>
        <p class="grid-card-subtitle" style="font-size: 0.84rem; color: #666; margin-bottom: 8px;">Khuôn viên 1.500m² • Hồ bơi vô cực 53m² • Trần cao 6m • Sân thượng 40m²</p>
        <span style="color: #8a6d3b; font-weight: 700; font-size: 0.88rem;">Giá: Liên Hệ Đại Chúng</span>
      </div>
    </a>

    <!-- Sunset 1 -->
    <a href="article.html?id=101" class="grid-card" style="text-decoration: none; color: inherit; display: block; border-radius: 8px; overflow: hidden; background: #fff; box-shadow: 0 4px 20px rgba(0,0,0,0.06); border: 1px solid #e0d5c1;">
      <div class="grid-img" style="position: relative; height: 220px;">
        <img alt="Sunset 1 Villa" src="assets/Index_asset/02_Phoi_Canh_3D/09.3D_TKCS-SUNSET_VILLA/SUNSET_1_VILLA/SFR_07.SAN_TRONG.jpg" style="width:100%; height:100%; object-fit:cover;"/>
        <span style="position: absolute; top: 12px; left: 12px; background: #c9a96e; color: #000; font-size: 0.7rem; font-weight: 700; padding: 4px 10px; border-radius: 4px;">MẪU 3PN • SÂN TRONG GIẾNG TRỜI</span>
        <span class="minh-hoa-tag">* Hình ảnh minh họa</span>
      </div>
      <div class="grid-card-info" style="padding: 16px;">
        <h5 style="font-size: 1.1rem; margin-bottom: 6px; font-family: var(--font-serif);">Sunset 1 Villa (3PN - 1 Tầng)</h5>
        <p class="grid-card-subtitle" style="font-size: 0.84rem; color: #666; margin-bottom: 8px;">Khuôn viên 1.000m² • Sân trong 38m² • Hồ bơi 45m² • Vườn ăn trái hữu cơ 260m²</p>
        <span style="color: #2e7d32; font-weight: 700; font-size: 0.88rem;">Giá: Liên Hệ Đại Chúng</span>
      </div>
    </a>

    <!-- Sunset 2 -->
    <a href="article.html?id=102" class="grid-card" style="text-decoration: none; color: inherit; display: block; border-radius: 8px; overflow: hidden; background: #fff; box-shadow: 0 4px 20px rgba(0,0,0,0.06); border: 1px solid #e0d5c1;">
      <div class="grid-img" style="position: relative; height: 220px;">
        <img alt="Sunset 2 Villa" src="assets/Index_asset/02_Phoi_Canh_3D/09.3D_TKCS-SUNSET_VILLA/SUNSET_2_VILLA/SFR_04.PC_01.jpg" style="width:100%; height:100%; object-fit:cover;"/>
        <span style="position: absolute; top: 12px; left: 12px; background: #2e7d32; color: #fff; font-size: 0.7rem; font-weight: 700; padding: 4px 10px; border-radius: 4px;">2 TẦNG BỀ THẾ • 1.200M²</span>
        <span class="minh-hoa-tag">* Hình ảnh minh họa</span>
      </div>
      <div class="grid-card-info" style="padding: 16px;">
        <h5 style="font-size: 1.1rem; margin-bottom: 6px; font-family: var(--font-serif);">Sunset 2 Villa (3PN - 2 Tầng)</h5>
        <p class="grid-card-subtitle" style="font-size: 0.84rem; color: #666; margin-bottom: 8px;">Khuôn viên 1.200m² • Vườn ăn trái 482m² • Ban công ngắm trọn hoàng hôn</p>
        <span style="color: #2e7d32; font-weight: 700; font-size: 0.88rem;">Giá: Liên Hệ Đại Chúng</span>
      </div>
    </a>
  </div>

  <div style="text-align: center; margin-top: 20px;">
    <a href="#tabs-section" onclick="activateTab('tab-villas-market')" class="editorial-btn" style="background: #111; color: #fff; padding: 12px 28px; border-radius: 4px; font-size: 0.9rem;">
      <i class="fa-solid fa-newspaper" style="margin-right:8px; color:#c9a96e;"></i>Xem 16 Chuyên Đề Phân Tích Chuyên Sâu Villa
    </a>
  </div>

  <div style="text-align: right; margin-top: 18px; font-size: 0.78rem; color: #888; font-style: italic;">* Lưu ý: Toàn bộ thông tin, mặt bằng kiến trúc và hình ảnh tiện ích mang tính chất minh họa theo định hướng phát triển thực tế của dự án.</div>
</div>"""

pattern = re.compile(r'<!-- Tab 2: Villas Sinh Thái \(tab-eco-villas\) -->.*?(?=<!-- Tab 3: Tiện Ích Resort \(tab-amenities\) -->)', re.DOTALL)
if pattern.search(html):
    html = pattern.sub(tab_eco_villas_html + "\n\n", html)
    print("Replaced tab-eco-villas successfully.")
else:
    print("Could not find tab-eco-villas pattern.")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated index.html tab-eco-villas successfully.")
