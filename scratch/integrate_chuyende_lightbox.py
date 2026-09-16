import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. NEW 10 CHUYEN DE CARDS HTML
new_chuyen_de_html = '''<!-- 10 Chuyên Đề Văn Hóa & Bản Sắc Việt Showcase (Mở Bung Lightbox Không Nhảy Trang) -->
    <div class="editorial-sub-header" style="padding-top: 32px; border-top: 1px solid rgba(201,169,110,0.3);">
      <span class="editorial-eyebrow"><i class="fa-solid fa-book-bookmark"></i> ẤN PHẨM CHUYÊN ĐỀ</span>
      <h3 class="editorial-sub-title">10 Chuyên Đề Văn Hóa &amp; Phong Cách Sống Điền Trang</h3>
      <p class="editorial-section-sub">Chuỗi bài viết chuyên sâu đúc kết triết lý sống, giá trị di sản và phong cách thụ hưởng đích thực của người Việt đương đại.</p>
    </div>
<div class="grid-listing" style="grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));">
<!-- 401 -->
<div class="grid-card heritage-photo-card" onclick="openChuyenDeGallery(0)" style="cursor: pointer;" title="Nhấp để mở bung hình Chuyên Đề 01">
<div class="grid-img">
<img alt="Biệt Phủ Điền Trang: Xu Hướng Định Vị Đẳng Cấp Sống Mới" decoding="async" loading="lazy" src="assets/posts/chuyen_de/401_biet_phu_xu_huong.jpg"/>
<span class="heritage-img-hint"><i class="fa-solid fa-expand"></i> Mở bung hình</span>
</div>
<div class="grid-card-info">
<div style="margin-bottom: 6px;"><span style="background: #c9a96e; color: #000; font-size: 0.65rem; font-weight: 700; padding: 2px 7px; border-radius: 3px; display: inline-block;">XU HƯỚNG BẤT ĐỘNG SẢN</span></div>
<h5>Biệt Phủ Điền Trang: Xu Hướng Định Vị Đẳng Cấp Sống Mới</h5>
<p class="grid-card-subtitle">Sự chuyển dịch từ penthouse phố thị sang điền trang sinh thái rộng lớn ven hồ</p>
<p class="grid-price" style="color: #c9a96e; display: flex; justify-content: space-between; align-items: center; margin-top: 8px;">
  <span>CHUYÊN ĐỀ 01 &rarr;</span>
  <span style="font-size: 0.76rem; color: #8c6b32; font-weight: 700;"><i class="fa-solid fa-magnifying-glass-plus"></i> Xem lớn</span>
</p>
</div>
</div>
<!-- 402 -->
<div class="grid-card heritage-photo-card" onclick="openChuyenDeGallery(1)" style="cursor: pointer;" title="Nhấp để mở bung hình Chuyên Đề 02">
<div class="grid-img">
<img alt="Hạt Lúa &amp; Đồng Quê: Linh Hồn Cuộc Sống Tinh Thần Người Việt" decoding="async" loading="lazy" src="assets/posts/chuyen_de/402_hat_lua_dong_que.jpg"/>
<span class="heritage-img-hint"><i class="fa-solid fa-expand"></i> Mở bung hình</span>
</div>
<div class="grid-card-info">
<div style="margin-bottom: 6px;"><span style="background: #2e7d32; color: #fff; font-size: 0.65rem; font-weight: 700; padding: 2px 7px; border-radius: 3px; display: inline-block;">VĂN MINH LÚA NƯỚC</span></div>
<h5>Hạt Lúa &amp; Đồng Quê: Linh Hồn Cuộc Sống Tinh Thần Người Việt</h5>
<p class="grid-card-subtitle">Hạt ngọc trời ban, triết lý lúa chín cúi đầu và ký ức bình yên quê hương</p>
<p class="grid-price" style="color: #c9a96e; display: flex; justify-content: space-between; align-items: center; margin-top: 8px;">
  <span>CHUYÊN ĐỀ 02 &rarr;</span>
  <span style="font-size: 0.76rem; color: #8c6b32; font-weight: 700;"><i class="fa-solid fa-magnifying-glass-plus"></i> Xem lớn</span>
</p>
</div>
</div>
<!-- 403 -->
<div class="grid-card heritage-photo-card" onclick="openChuyenDeGallery(2)" style="cursor: pointer;" title="Nhấp để mở bung hình Chuyên Đề 03">
<div class="grid-img">
<img alt="Sống Tự Nhiên &amp; Xa Xỉ Bản Sắc: Trở Về Cội Nguồn Dân Tộc" decoding="async" loading="lazy" src="assets/posts/chuyen_de/403_song_tu_nhien_xa_xi.jpg"/>
<span class="heritage-img-hint"><i class="fa-solid fa-expand"></i> Mở bung hình</span>
</div>
<div class="grid-card-info">
<div style="margin-bottom: 6px;"><span style="background: #0068FF; color: #fff; font-size: 0.65rem; font-weight: 700; padding: 2px 7px; border-radius: 3px; display: inline-block;">ECO-HERITAGE LUXURY</span></div>
<h5>Sống Tự Nhiên &amp; Xa Xỉ Bản Sắc: Trở Về Cội Nguồn Dân Tộc</h5>
<p class="grid-card-subtitle">Định nghĩa lại sự xa xỉ: Hàng hiên đón gió, trà sen sớm mai và nếp nhà thuần Việt</p>
<p class="grid-price" style="color: #c9a96e; display: flex; justify-content: space-between; align-items: center; margin-top: 8px;">
  <span>CHUYÊN ĐỀ 03 &rarr;</span>
  <span style="font-size: 0.76rem; color: #8c6b32; font-weight: 700;"><i class="fa-solid fa-magnifying-glass-plus"></i> Xem lớn</span>
</p>
</div>
</div>
<!-- 404 -->
<div class="grid-card heritage-photo-card" onclick="openChuyenDeGallery(3)" style="cursor: pointer;" title="Nhấp để mở bung hình Chuyên Đề 04">
<div class="grid-img">
<img alt="Tiện Nghi Nghỉ Dưỡng &amp; Dịch Vụ Quản Gia Chu Đáo 5 Sao" decoding="async" loading="lazy" src="assets/Index_asset/Phoicanh_3D_Tien_ich/Central_Restaurant/Central_Restaurant_1.avif"/>
<span class="heritage-img-hint"><i class="fa-solid fa-expand"></i> Mở bung hình</span>
</div>
<div class="grid-card-info">
<div style="margin-bottom: 6px;"><span style="background: #d4af37; color: #000; font-size: 0.65rem; font-weight: 700; padding: 2px 7px; border-radius: 3px; display: inline-block;">MDS LIVING 5 SAO</span></div>
<h5>Tiện Nghi Nghỉ Dưỡng &amp; Dịch Vụ Quản Gia Chu Đáo 5 Sao</h5>
<p class="grid-card-subtitle">Thảnh thơi tận hưởng cuộc sống với dịch vụ quản gia cá nhân hóa tận tâm</p>
<p class="grid-price" style="color: #c9a96e; display: flex; justify-content: space-between; align-items: center; margin-top: 8px;">
  <span>CHUYÊN ĐỀ 04 &rarr;</span>
  <span style="font-size: 0.76rem; color: #8c6b32; font-weight: 700;"><i class="fa-solid fa-magnifying-glass-plus"></i> Xem lớn</span>
</p>
</div>
</div>
<!-- 405 -->
<div class="grid-card heritage-photo-card" onclick="openChuyenDeGallery(4)" style="cursor: pointer;" title="Nhấp để mở bung hình Chuyên Đề 05">
<div class="grid-img">
<img alt="Lòng Tự Hào Dân Tộc: Ngọn Lửa Bất Diệt Trong Tim Mỗi Người" decoding="async" loading="lazy" src="assets/Index_asset/Phoicanh_3D_Tien_ich/Duong_noi_bo/SFR_1.jpg"/>
<span class="heritage-img-hint"><i class="fa-solid fa-expand"></i> Mở bung hình</span>
</div>
<div class="grid-card-info">
<div style="margin-bottom: 6px;"><span style="background: #c9a96e; color: #000; font-size: 0.65rem; font-weight: 700; padding: 2px 7px; border-radius: 3px; display: inline-block;">DÒNG SỬ VIỆT</span></div>
<h5>Lòng Tự Hào Dân Tộc: Ngọn Lửa Bất Diệt Trong Tim Mỗi Người</h5>
<p class="grid-card-subtitle">Bản lĩnh kiêu hùng 4.000 năm văn hiến và không gian kiến trúc Về Nguồn</p>
<p class="grid-price" style="color: #c9a96e; display: flex; justify-content: space-between; align-items: center; margin-top: 8px;">
  <span>CHUYÊN ĐỀ 05 &rarr;</span>
  <span style="font-size: 0.76rem; color: #8c6b32; font-weight: 700;"><i class="fa-solid fa-magnifying-glass-plus"></i> Xem lớn</span>
</p>
</div>
</div>
<!-- 406 -->
<div class="grid-card heritage-photo-card" onclick="openChuyenDeGallery(5)" style="cursor: pointer;" title="Nhấp để mở bung hình Chuyên Đề 06">
<div class="grid-img">
<img alt="Văn Hóa &amp; Thiên Nhiên: Con Đường Nuôi Dạy Con Trẻ Bền Vững" decoding="async" loading="lazy" src="assets/Index_asset/Phoicanh_3D_Tien_ich/Central_Restaurant/Central_Restaurant_2.avif"/>
<span class="heritage-img-hint"><i class="fa-solid fa-expand"></i> Mở bung hình</span>
</div>
<div class="grid-card-info">
<div style="margin-bottom: 6px;"><span style="background: #e65100; color: #fff; font-size: 0.65rem; font-weight: 700; padding: 2px 7px; border-radius: 3px; display: inline-block;">GIÁO TRÍ VIỆT</span></div>
<h5>Văn Hóa &amp; Thiên Nhiên: Con Đường Nuôi Dạy Con Trẻ Bền Vững</h5>
<p class="grid-card-subtitle">Tách trẻ khỏi màn hình để học làm gốm, nặn tò he và vun trồng cây gia đình</p>
<p class="grid-price" style="color: #c9a96e; display: flex; justify-content: space-between; align-items: center; margin-top: 8px;">
  <span>CHUYÊN ĐỀ 06 &rarr;</span>
  <span style="font-size: 0.76rem; color: #8c6b32; font-weight: 700;"><i class="fa-solid fa-magnifying-glass-plus"></i> Xem lớn</span>
</p>
</div>
</div>
<!-- 407 -->
<div class="grid-card heritage-photo-card" onclick="openChuyenDeGallery(6)" style="cursor: pointer;" title="Nhấp để mở bung hình Chuyên Đề 07">
<div class="grid-img">
<img alt="Đạo Hiếu: Chốn An Yên Báo Đáp Đấng Sinh Thành Đa Thế Hệ" decoding="async" loading="lazy" src="assets/posts/xa_xi_ban_sac/hien_viet.jpg"/>
<span class="heritage-img-hint"><i class="fa-solid fa-expand"></i> Mở bung hình</span>
</div>
<div class="grid-card-info">
<div style="margin-bottom: 6px;"><span style="background: #2e7d32; color: #fff; font-size: 0.65rem; font-weight: 700; padding: 2px 7px; border-radius: 3px; display: inline-block;">ĐẠO HIẾU NGHÌN ĐỜI</span></div>
<h5>Đạo Hiếu: Chốn An Yên Báo Đáp Đấng Sinh Thành Đa Thế Hệ</h5>
<p class="grid-card-subtitle">Môi trường dưỡng sinh ven hồ lý tưởng cho cha mẹ an hưởng tuổi già</p>
<p class="grid-price" style="color: #c9a96e; display: flex; justify-content: space-between; align-items: center; margin-top: 8px;">
  <span>CHUYÊN ĐỀ 07 &rarr;</span>
  <span style="font-size: 0.76rem; color: #8c6b32; font-weight: 700;"><i class="fa-solid fa-magnifying-glass-plus"></i> Xem lớn</span>
</p>
</div>
</div>
<!-- 408 -->
<div class="grid-card heritage-photo-card" onclick="openChuyenDeGallery(7)" style="cursor: pointer;" title="Nhấp để mở bung hình Chuyên Đề 08">
<div class="grid-img">
<img alt="Bức Tranh Sắc Màu Trang Phục 54 Dân Tộc Việt Nam" decoding="async" loading="lazy" src="assets/Index_asset/Tien_ich_minh_hoa/Nha_am_sac_viet.png"/>
<span class="heritage-img-hint"><i class="fa-solid fa-expand"></i> Mở bung hình</span>
</div>
<div class="grid-card-info">
<div style="margin-bottom: 6px;"><span style="background: #9c27b0; color: #fff; font-size: 0.65rem; font-weight: 700; padding: 2px 7px; border-radius: 3px; display: inline-block;">SẮC MÀU THỔ CẨM</span></div>
<h5>Bức Tranh Sắc Màu Trang Phục 54 Dân Tộc Việt Nam</h5>
<p class="grid-card-subtitle">Tinh hoa dệt may, thổ cẩm và không gian trưng bày Nhà Âm Sắc Việt</p>
<p class="grid-price" style="color: #c9a96e; display: flex; justify-content: space-between; align-items: center; margin-top: 8px;">
  <span>CHUYÊN ĐỀ 08 &rarr;</span>
  <span style="font-size: 0.76rem; color: #8c6b32; font-weight: 700;"><i class="fa-solid fa-magnifying-glass-plus"></i> Xem lớn</span>
</p>
</div>
</div>
<!-- 409 -->
<div class="grid-card heritage-photo-card" onclick="openChuyenDeGallery(8)" style="cursor: pointer;" title="Nhấp để mở bung hình Chuyên Đề 09">
<div class="grid-img">
<img alt="Ca Dao, Đờn Ca Tài Tử &amp; Cải Lương Xứ Miền Nam Hào Sảng" decoding="async" loading="lazy" src="assets/Index_asset/editorial_photo/Canh_dong_lua.png"/>
<span class="heritage-img-hint"><i class="fa-solid fa-expand"></i> Mở bung hình</span>
</div>
<div class="grid-card-info">
<div style="margin-bottom: 6px;"><span style="background: #0068FF; color: #fff; font-size: 0.65rem; font-weight: 700; padding: 2px 7px; border-radius: 3px; display: inline-block;">ÂM SẮC PHƯƠNG NAM</span></div>
<h5>Ca Dao, Đờn Ca Tài Tử &amp; Cải Lương Xứ Miền Nam Hào Sảng</h5>
<p class="grid-card-subtitle">Tiếng đàn kìm da diết và đêm trăng hoa đăng trên mặt hồ 100ha</p>
<p class="grid-price" style="color: #c9a96e; display: flex; justify-content: space-between; align-items: center; margin-top: 8px;">
  <span>CHUYÊN ĐỀ 09 &rarr;</span>
  <span style="font-size: 0.76rem; color: #8c6b32; font-weight: 700;"><i class="fa-solid fa-magnifying-glass-plus"></i> Xem lớn</span>
</p>
</div>
</div>
<!-- 410 -->
<div class="grid-card heritage-photo-card" onclick="openChuyenDeGallery(9)" style="cursor: pointer;" title="Nhấp để mở bung hình Chuyên Đề 10">
<div class="grid-img">
<img alt="Đất Rộng Ven Hồ Ngày Càng Hiếm: Tích Sản Điền Trang Sinh Thái" decoding="async" loading="lazy" src="assets/Index_asset/Flycam/Flycam_Tong_quan_SGFR/Flycam_SGFR_2.avif"/>
<span class="heritage-img-hint"><i class="fa-solid fa-expand"></i> Mở bung hình</span>
</div>
<div class="grid-card-info">
<div style="margin-bottom: 6px;"><span style="background: #e53935; color: #fff; font-size: 0.65rem; font-weight: 700; padding: 2px 7px; border-radius: 3px; display: inline-block;">TÍCH SẢN TRUYỀN ĐỜI</span></div>
<h5>Đất Rộng Ven Hồ Ngày Càng Hiếm: Tích Sản Điền Trang Sinh Thái</h5>
<p class="grid-card-subtitle">Giá trị vô giá của quỹ đất điền trang sinh thái ven hồ 100ha liền kề Sài Gòn</p>
<p class="grid-price" style="color: #c9a96e; display: flex; justify-content: space-between; align-items: center; margin-top: 8px;">
  <span>CHUYÊN ĐỀ 10 &rarr;</span>
  <span style="font-size: 0.76rem; color: #8c6b32; font-weight: 700;"><i class="fa-solid fa-magnifying-glass-plus"></i> Xem lớn</span>
</p>
</div>
</div>
</div>'''

old_cd_pattern = re.compile(r'<!-- 10 Chuyên Đề.*?<div class="grid-listing"[^>]*>.*?<!-- 410 -->.*?</div>\s*</div>\s*</div>', re.DOTALL)
m = old_cd_pattern.search(html)
assert m, "Could not match old 10 chuyen de section"
html = html[:m.start()] + new_chuyen_de_html + '</div>' + html[m.end():]


# 2. UPDATE SCRIPT IN INDEX.HTML FOR BOTH GALLERIES
gallery_script = '''    // Data cho Gallery Không Gian Bản Sắc Việt (8 Điểm Đến)
    const heritageGalleryData = [
      {
        src: 'assets/Index_asset/Phoicanh_3D_Tien_ich/Ven_ho_clubhouse/Lake_Clubhouse_3.jpg',
        badge: 'MẶT HỒ 100HA',
        title: 'Bến Thuyền, Chèo SUP & Kayak',
        desc: 'Chèo SUP đón bình minh, Kayak, thuyền du ngoạn ngắm hoàng hôn trên mặt hồ sinh thái 100ha.',
        articleUrl: 'bai-viet/ben-thuyen-cheo-sup-kayak-the-thao-mat-nuoc-ben-ho-100ha.html'
      },
      {
        src: 'assets/Index_asset/Phoicanh_3D_Tien_ich/Central_Facilities/Ho_boi_trung_tam.jpg',
        badge: 'THE LOTUS SHORE',
        title: 'Bờ Sen – Hồ Thủy An Viên',
        desc: 'Hồ sen, hồ bơi điện phân muối khoáng, spa, tắm thảo mộc dưỡng sinh, trà Việt và không gian thiền tịnh.',
        articleUrl: 'bai-viet/bo-sen-herbal-spa-the-lotus-shore-nghe-thuat-duong-sinh-cham-soc-suc-khoe-thao-moc.html'
      },
      {
        src: 'assets/Index_asset/Tien_ich_minh_hoa/Nong_trai_huu_co.png',
        badge: 'THE VIETNAMESE TABLE',
        title: 'Nếp Nhà Việt',
        desc: 'Nhà hàng — từ khu vườn đến bàn ăn, bàn ăn cùng bếp trưởng, tiệc giữa đồng lúa, tiệc bên hồ sen.',
        articleUrl: 'bai-viet/am-thuc-ban-sac-triet-ly-farm-to-table-bua-com-sum-vay-ben-mai-hien-dien-trang.html'
      },
      {
        src: 'assets/Index_asset/Phoicanh_3D_Tien_ich/Central_Restaurant/Central_Restaurant_2.avif',
        badge: "THE MAKER'S HOUSE",
        title: 'Hiên Việt – Giáo Trí Việt',
        desc: 'Nơi trẻ học bằng đôi tay: gốm Bát Tràng, vẽ tranh dân gian, thư pháp, thắt lá dừa, nặn tò he truyền thống.',
        articleUrl: 'bai-viet/giao-tri-viet-vuon-coi-the-gioi-tuoi-tho-hoc-bang-doi-tay-giua-thien-nhien.html'
      },
      {
        src: 'assets/Index_asset/Tien_ich_minh_hoa/Nha_am_sac_viet.png',
        badge: 'THE SOUND & SILK HOUSE',
        title: 'Thanh Âm Các & Hội Việt',
        desc: 'Trang phục và nhạc cụ 54 dân tộc, gallery sống, lễ hội truyền thống, sân khấu hòa nhạc ngoài trời.',
        articleUrl: 'bai-viet/am-sac-viet-khong-gian-sinh-hoat-cong-dong-danh-thuc-hon-dan-toc-trong-nhip-song-duong-dai.html'
      },
      {
        src: 'assets/Index_asset/Phoicanh_3D_Tien_ich/Central_Facilities/Cung_tuong_Su_Viet.webp',
        badge: 'THE WALL OF TIME',
        title: 'Cung Tường Sử Việt',
        desc: 'Bốn nghìn năm hào khí kể bằng nghệ thuật cảnh quan: đá tự nhiên, đồng, phù điêu lịch sử, ánh sáng & mặt nước.',
        articleUrl: 'bai-viet/he-thong-9-khong-gian-ban-sac-viet-duong-dai-tai-saigon-farm-resort-tu-hien-viet-den-dong-su-viet.html'
      },
      {
        src: 'assets/Index_asset/editorial_photo/Canh_dong_lua.png',
        badge: 'HOẠT ĐỘNG 4 MÙA',
        title: 'Chuỗi Hoạt Động Lễ Hội Bản Sắc',
        desc: 'Lễ hội mùa lúa chín, thả hoa đăng bên hồ sinh thái 100ha, Tết Trung Thu và lễ hội ẩm thực truyền thống bốn mùa.',
        articleUrl: 'bai-viet/chuoi-hoat-dong-le-hoi-ban-sac-viet-khi-dien-trang-la-noi-tro-ve-cua-ky-uc-gan-ket-gia-dinh.html'
      },
      {
        src: 'assets/Index_asset/Phoicanh_3D_Tien_ich/Central_Facilities/Viet_Ma_Vien.jpg',
        badge: 'CLB QUÝ TỘC',
        title: 'Việt Mã Viên & Học Viện Cưỡi Ngựa',
        desc: 'Cưỡi ngựa quý tộc, học viện cưỡi ngựa cho trẻ nhỏ, khu chăm sóc ngựa quý và các buổi trình diễn cuối tuần.',
        articleUrl: 'bai-viet/viet-ma-vien-the-equestrian-estate-cau-lac-bo-cuoi-ngua-quy-toc-giua-dong-lua-tien-ich-doc-ban-khang-dinh-dang-cap-thuong-luu.html'
      }
    ];

    // Data cho 10 Chuyên Đề Văn Hóa & Phong Cách Sống Điền Trang
    const chuyenDeGalleryData = [
      {
        src: 'assets/posts/chuyen_de/401_biet_phu_xu_huong.jpg',
        badge: 'XU HƯỚNG BẤT ĐỘNG SẢN • CHUYÊN ĐỀ 01',
        title: 'Biệt Phủ Điền Trang: Xu Hướng Định Vị Đẳng Cấp Sống Mới',
        desc: 'Sự chuyển dịch từ penthouse phố thị sang điền trang sinh thái rộng lớn ven hồ tự nhiên 100ha.',
        articleUrl: 'bai-viet/biet-phu-dien-trang-xu-huong-dinh-vi-dang-cap-song-moi-cua-tang-lop-tinh-hoa-viet.html'
      },
      {
        src: 'assets/posts/chuyen_de/402_hat_lua_dong_que.jpg',
        badge: 'VĂN MINH LÚA NƯỚC • CHUYÊN ĐỀ 02',
        title: 'Hạt Lúa & Đồng Quê: Linh Hồn Cuộc Sống Tinh Thần Người Việt',
        desc: 'Hạt ngọc trời ban, triết lý lúa chín cúi đầu và ký ức bình yên quê hương trong từng nếp nhà.',
        articleUrl: 'bai-viet/hat-lua-dong-que-linh-hon-cuoc-song-tinh-than-va-van-hoa-truong-ton-cua-nguoi-viet.html'
      },
      {
        src: 'assets/posts/chuyen_de/403_song_tu_nhien_xa_xi.jpg',
        badge: 'ECO-HERITAGE LUXURY • CHUYÊN ĐỀ 03',
        title: 'Sống Tự Nhiên & Xa Xỉ Bản Sắc: Trở Về Cội Nguồn Dân Tộc',
        desc: 'Định nghĩa lại sự xa xỉ: Hàng hiên đón gió, trà sen sớm mai và nếp nhà thuần Việt thanh tao.',
        articleUrl: 'bai-viet/song-tu-nhien-xa-xi-ban-sac-khi-dang-cap-thuong-luu-la-tro-ve-voi-coi-nguon-dan-toc.html'
      },
      {
        src: 'assets/Index_asset/Phoicanh_3D_Tien_ich/Central_Restaurant/Central_Restaurant_1.avif',
        badge: 'MDS LIVING 5 SAO • CHUYÊN ĐỀ 04',
        title: 'Tiện Nghi Nghỉ Dưỡng & Dịch Vụ Quản Gia Chu Đáo 5 Sao',
        desc: 'Thảnh thơi tận hưởng cuộc sống với dịch vụ quản gia cá nhân hóa tận tâm chu đáo từng chi tiết.',
        articleUrl: 'bai-viet/tien-nghi-nghi-duong-dich-vu-chu-dao-chuan-muc-quan-gia-5-sao-giua-long-saigon-farm-resort.html'
      },
      {
        src: 'assets/Index_asset/Phoicanh_3D_Tien_ich/Duong_noi_bo/SFR_1.jpg',
        badge: 'DÒNG SỬ VIỆT • CHUYÊN ĐỀ 05',
        title: 'Lòng Tự Hào Dân Tộc: Ngọn Lửa Bất Diệt Trong Tim Mỗi Người',
        desc: 'Bản lĩnh kiêu hùng 4.000 năm văn hiến và không gian kiến trúc Về Nguồn hào khí dân tộc.',
        articleUrl: 'bai-viet/long-tu-hao-dan-toc-ngon-lua-bat-diet-trong-tim-moi-the-he-con-lac-chau-hong-dau-an-di-san.html'
      },
      {
        src: 'assets/Index_asset/Phoicanh_3D_Tien_ich/Central_Restaurant/Central_Restaurant_2.avif',
        badge: 'GIÁO TRÍ VIỆT • CHUYÊN ĐỀ 06',
        title: 'Văn Hóa & Thiên Nhiên: Con Đường Nuôi Dạy Con Trẻ Bền Vững',
        desc: 'Tách trẻ khỏi màn hình để học làm gốm, nặn tò he và vun trồng cây gia đình giữa thiên nhiên.',
        articleUrl: 'bai-viet/van-hoa-thien-nhien-con-duong-nuoi-day-dinh-hinh-nhan-cach-con-tre-ben-vung-nhat.html'
      },
      {
        src: 'assets/posts/xa_xi_ban_sac/hien_viet.jpg',
        badge: 'ĐẠO HIẾU NGHÌN ĐỜI • CHUYÊN ĐỀ 07',
        title: 'Đạo Hiếu: Chốn An Yên Báo Đáp Đấng Sinh Thành Đa Thế Hệ',
        desc: 'Môi trường dưỡng sinh ven hồ lý tưởng cho cha mẹ an dưỡng tuổi già, con cháu sum vầy.',
        articleUrl: 'bai-viet/dao-hieu-trong-van-hoa-viet-chon-an-yen-bao-dap-dang-sinh-thanh-nep-nha-tam-dai-dong-duong.html'
      },
      {
        src: 'assets/Index_asset/Tien_ich_minh_hoa/Nha_am_sac_viet.png',
        badge: 'SẮC MÀU THỔ CẨM • CHUYÊN ĐỀ 08',
        title: 'Bức Tranh Sắc Màu Trang Phục 54 Dân Tộc Việt Nam',
        desc: 'Tinh hoa dệt may, thổ cẩm và không gian trưng bày Nhà Âm Sắc Việt sống động.',
        articleUrl: 'bai-viet/buc-tranh-sac-mau-trang-phuc-54-dan-toc-viet-nam-tinh-hoa-det-may-bieu-tuong-song-cua-di-san.html'
      },
      {
        src: 'assets/Index_asset/editorial_photo/Canh_dong_lua.png',
        badge: 'ÂM SẮC PHƯƠNG NAM • CHUYÊN ĐỀ 09',
        title: 'Ca Dao, Đờn Ca Tài Tử & Cải Lương Xứ Miền Nam Hào Sảng',
        desc: 'Tiếng đàn kìm da diết và đêm trăng hoa đăng trên mặt nước hồ sinh thái 100ha.',
        articleUrl: 'bai-viet/ca-dao-don-ca-tai-tu-cai-luong-tieng-long-sau-lang-cua-mien-dat-phuong-nam-hao-sang.html'
      },
      {
        src: 'assets/Index_asset/Flycam/Flycam_Tong_quan_SGFR/Flycam_SGFR_2.avif',
        badge: 'TÍCH SẢN TRUYỀN ĐỜI • CHUYÊN ĐỀ 10',
        title: 'Đất Rộng Ven Hồ Ngày Càng Hiếm: Tích Sản Điền Trang Sinh Thái',
        desc: 'Giá trị vô giá của quỹ đất điền trang sinh thái ven hồ 100ha sổ đỏ lâu dài liền kề Sài Gòn.',
        articleUrl: 'bai-viet/dat-rong-ven-ho-ngay-cang-hiem-tich-san-dien-trang-sinh-thai-bieu-tuong-dang-cap-di-san-truyen-doi.html'
      }
    ];

    let activeGalleryData = heritageGalleryData;
    let curGalleryIndex = 0;
    let isGalleryMode = false;

    // Mở Gallery Không Gian Bản Sắc Việt
    window.openHeritageGallery = function(idx) {
      activeGalleryData = heritageGalleryData;
      curGalleryIndex = (typeof idx === 'number' && idx >= 0 && idx < activeGalleryData.length) ? idx : 0;
      isGalleryMode = true;
      openActiveGalleryModal();
    };

    // Mở Gallery 10 Chuyên Đề (Mở bung hình, không nhảy trang)
    window.openChuyenDeGallery = function(idx) {
      activeGalleryData = chuyenDeGalleryData;
      curGalleryIndex = (typeof idx === 'number' && idx >= 0 && idx < activeGalleryData.length) ? idx : 0;
      isGalleryMode = true;
      openActiveGalleryModal();
    };

    function openActiveGalleryModal() {
      const modal = document.getElementById('diagram-lightbox');
      const prevBtn = document.getElementById('diagram-lb-prev');
      const nextBtn = document.getElementById('diagram-lb-next');
      const counterEl = document.getElementById('diagram-lb-counter');
      
      if (!modal) return;

      if (prevBtn) prevBtn.style.display = 'flex';
      if (nextBtn) nextBtn.style.display = 'flex';
      if (counterEl) counterEl.style.display = 'inline-block';
      
      renderActiveGalleryItem();

      modal.style.display = 'flex';
      setTimeout(() => {
        modal.classList.add('active');
        document.body.style.overflow = 'hidden';
      }, 10);
    }

    function renderActiveGalleryItem() {
      const item = activeGalleryData[curGalleryIndex];
      if (!item) return;
      
      const img = document.getElementById('diagram-lb-img');
      const titleEl = document.getElementById('diagram-lb-title');
      const badgeEl = document.getElementById('diagram-lb-badge');
      const descEl = document.getElementById('diagram-lb-desc');
      const counterEl = document.getElementById('diagram-lb-counter');
      const articleLink = document.getElementById('diagram-lb-article-link');
      const body = document.getElementById('diagram-lb-body');
      
      if (img) {
        img.src = item.src;
        img.alt = item.title;
      }
      if (titleEl) titleEl.textContent = item.title;
      if (badgeEl) badgeEl.textContent = item.badge;
      if (descEl) descEl.textContent = item.desc;
      if (counterEl) counterEl.textContent = (curGalleryIndex + 1) + ' / ' + activeGalleryData.length;
      
      if (articleLink) {
        if (item.articleUrl) {
          articleLink.href = item.articleUrl;
          articleLink.style.display = 'inline-flex';
        } else {
          articleLink.style.display = 'none';
        }
      }
      
      if (body) body.classList.remove('is-zoomed');
      updateZoomButtonState(false);
    }

    window.navigateHeritageGallery = function(direction, e) {
      if (e) e.stopPropagation();
      curGalleryIndex = (curGalleryIndex + direction + activeGalleryData.length) % activeGalleryData.length;
      renderActiveGalleryItem();
    };'''

# Replace the gallery script block in index.html
old_script_pattern = re.compile(r'// Data cho Gallery Không Gian Bản Sắc Việt.*?window\.navigateHeritageGallery = function\(direction, e\) \{.*?\};', re.DOTALL)
m_script = old_script_pattern.search(html)
assert m_script, "Old gallery script not found"
html = html[:m_script.start()] + gallery_script + html[m_script.end():]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("SUCCESS: 10 Chuyên Đề now open in lightbox modal!")
