import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Top 3 Cards in Section 2
old_top3_pattern = re.compile(r'<!-- Top 3 Featured Heritage Cards -->.*?<div class="top-listing">(.*?)</div>\s*<!-- Interactive Spaces Heritage Table -->', re.DOTALL)
m_top3 = old_top3_pattern.search(html)
assert m_top3, "Top 3 cards not found"

new_top3 = '''<!-- Top 3 Featured Heritage Cards (Mở Bung Lightbox Không Nhảy Trang) -->
<div class="top-listing">
<!-- Top 1: Hệ Thống Không Gian Bản Sắc Việt -->
<div class="top-listing-card heritage-photo-card" onclick="openHeritageGallery(5)" style="cursor: pointer; position: relative;" title="Nhấp để mở bung hình Cung Tường Sử Việt &amp; Không Gian Bản Sắc">
<div class="top-listing-img" style="background-image: url('assets/Index_asset/Phoicanh_3D_Tien_ich/Central_Facilities/Cung_tuong_Su_Viet.webp');">
  <span class="heritage-img-hint"><i class="fa-solid fa-expand"></i> Mở bung hình</span>
</div>
<div class="top-listing-info">
<div style="margin-bottom: 8px;">
<span style="background: #c9a96e; color: #000; font-size: 0.7rem; font-weight: 700; padding: 3px 8px; border-radius: 4px; letter-spacing: 0.05em; display: inline-block;">MDS LIVING • BẢN SẮC VIỆT</span>
</div>
<h4>Hệ Thống Không Gian Bản Sắc Việt</h4>
<p>Hiên Việt • Giáo Trí Việt • Bờ Sen • Việt Mã Viên • Nếp Nhà Việt • Cung Tường Sử Việt</p>
</div>
</div>
<!-- Top 2: Chuỗi Hoạt Động Lễ Hội Bốn Mùa -->
<div class="top-listing-card heritage-photo-card" onclick="openHeritageGallery(6)" style="cursor: pointer; position: relative;" title="Nhấp để mở bung hình Chuỗi Hoạt Động Lễ Hội Bản Sắc">
<div class="top-listing-img" style="background-image: url('assets/Index_asset/editorial_photo/Canh_dong_lua.png');">
  <span class="heritage-img-hint"><i class="fa-solid fa-expand"></i> Mở bung hình</span>
</div>
<div class="top-listing-info">
<div style="margin-bottom: 8px;">
<span style="background: #2e7d32; color: #fff; font-size: 0.7rem; font-weight: 700; padding: 3px 8px; border-radius: 4px; letter-spacing: 0.05em; display: inline-block;">HOẠT ĐỘNG 4 MÙA</span>
</div>
<h4>Chuỗi Hoạt Động Lễ Hội Bản Sắc</h4>
<p>Lễ hội mùa lúa chín • Đêm trăng rằm hoa đăng • Tết Trung Thu • Tết xưa</p>
</div>
</div>
<!-- Top 3: Việt Mã Viên -->
<div class="top-listing-card heritage-photo-card" onclick="openHeritageGallery(7)" style="cursor: pointer; position: relative;" title="Nhấp để mở bung hình Việt Mã Viên &amp; Học Viện Cưỡi Ngựa">
<div class="top-listing-img" style="background-image: url('assets/Index_asset/Phoicanh_3D_Tien_ich/Central_Facilities/Viet_Ma_Vien.jpg');">
  <span class="heritage-img-hint"><i class="fa-solid fa-expand"></i> Mở bung hình</span>
</div>
<div class="top-listing-info">
<div style="margin-bottom: 8px;">
<span style="background: #e65100; color: #fff; font-size: 0.7rem; font-weight: 700; padding: 3px 8px; border-radius: 4px; letter-spacing: 0.05em; display: inline-block;">CLB QUÝ TỘC</span>
</div>
<h4>Việt Mã Viên &amp; Học Viện Cưỡi Ngựa</h4>
<p>Cưỡi ngựa quý tộc • Lớp ngựa con • Trình diễn nghệ thuật cuối tuần</p>
</div>
</div>
</div>
'''

html = html[:m_top3.start()] + new_top3 + html[m_top3.end() - len('<!-- Interactive Spaces Heritage Table -->'):]

# 2. Update heritageGalleryData to include items 6 and 7
gallery_data_code = '''    // Data cho Gallery Không Gian Bản Sắc Việt
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
    ];'''

html = re.sub(r'// Data cho Gallery Không Gian Bản Sắc Việt.*?const heritageGalleryData = \[.*?\];', gallery_data_code, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("SUCCESS: Full heritage spaces lightbox updated!")
