import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Header Nav
old_nav = '''<nav class="nav-menu-links">
<a class="nav-link active" href="#biet-phu">Biệt Phủ Điền Trang</a>
<a class="nav-link" href="#ban-sac">Bản Sắc Việt</a>
<a class="nav-link" href="#tien-ich">Tiện Ích 30.000m²</a>
<a class="nav-link" href="#quy-hoach">Quy Hoạch &amp; Pháp Lý</a>
<a class="nav-link" href="#tap-chi">Tạp Chí &amp; Nhận Định</a>
<a class="nav-link" href="#vi-tri">Vị Trí &amp; Bản Đồ</a>
</nav>'''

new_nav = '''<nav class="nav-menu-links">
<a class="nav-link active" href="#partner-toolkit">Dòng Sản Phẩm</a>
<a class="nav-link" href="#ban-sac">Bản Sắc Việt</a>
<a class="nav-link" href="#tien-ich">Tiện Ích 30.000m²</a>
<a class="nav-link" href="#tap-chi">Tạp Chí &amp; Nhận Định</a>
<a class="nav-link" href="#vi-tri">Vị Trí &amp; Bản Đồ</a>
<a class="nav-link" href="gioithieu">Bản Giới Thiệu (Pitch Deck)</a>
</nav>'''

assert old_nav in content, "old_nav not found"
content = content.replace(old_nav, new_nav, 1)

# 2. Update Mobile Menu
old_mobile = '''<a href="#biet-phu" onclick="closeMobileMenu()"><i class="fa-solid fa-landmark-dome" style="width:20px;margin-right:8px;"></i>Biệt Phủ Điền Trang</a>
<a href="#ban-sac" onclick="closeMobileMenu()"><i class="fa-solid fa-landmark" style="width:20px;margin-right:8px;"></i>Bản Sắc Việt</a>
<a href="#tien-ich" onclick="closeMobileMenu()"><i class="fa-solid fa-spa" style="width:20px;margin-right:8px;"></i>Tiện Ích 30.000m²</a>
<a href="#quy-hoach" onclick="closeMobileMenu()"><i class="fa-solid fa-map-location-dot" style="width:20px;margin-right:8px;"></i>Quy Hoạch &amp; Pháp Lý</a>
<a href="#tap-chi" onclick="closeMobileMenu()"><i class="fa-solid fa-newspaper" style="width:20px;margin-right:8px;"></i>Tạp Chí &amp; Nhận Định</a>
<a href="#vi-tri" onclick="closeMobileMenu()"><i class="fa-solid fa-map-pin" style="width:20px;margin-right:8px; color:#c9a96e;"></i>Vị Trí &amp; Chỉ Đường Maps</a>
<a href="story" onclick="closeMobileMenu()" style="color: #c9a96e; font-weight: 700;"><i class="fa-solid fa-book-open" style="width:20px;margin-right:8px; color:#c9a96e;"></i>Tạp Chí Story (98 Trang Lật Mở)</a>'''

new_mobile = '''<a href="#partner-toolkit" onclick="closeMobileMenu()"><i class="fa-solid fa-shapes" style="width:20px;margin-right:8px;"></i>Dòng Sản Phẩm Điền Trang</a>
<a href="#ban-sac" onclick="closeMobileMenu()"><i class="fa-solid fa-landmark" style="width:20px;margin-right:8px;"></i>Bản Sắc Việt</a>
<a href="#tien-ich" onclick="closeMobileMenu()"><i class="fa-solid fa-spa" style="width:20px;margin-right:8px;"></i>Tiện Ích 30.000m²</a>
<a href="#tap-chi" onclick="closeMobileMenu()"><i class="fa-solid fa-newspaper" style="width:20px;margin-right:8px;"></i>Tạp Chí &amp; Nhận Định</a>
<a href="#vi-tri" onclick="closeMobileMenu()"><i class="fa-solid fa-map-pin" style="width:20px;margin-right:8px; color:#c9a96e;"></i>Vị Trí &amp; Chỉ Đường Maps</a>
<a href="gioithieu" onclick="closeMobileMenu()" style="color: #c9a96e; font-weight: 700;"><i class="fa-solid fa-book-open" style="width:20px;margin-right:8px; color:#c9a96e;"></i>Bản Giới Thiệu Toàn Cảnh (Pitch Deck)</a>'''

assert old_mobile in content, "old_mobile not found"
content = content.replace(old_mobile, new_mobile, 1)

# 3. Update Product Card 1 CTA
old_card_cta = '<a href="#tabs-section" style="flex: 1; text-align: center; background: #c29b53; color: #fff; padding: 9px 12px; border-radius: 6px; font-size: 0.86rem; font-weight: 700; text-decoration: none;">Chiêm Ngưỡng Biệt Phủ →</a>'
new_card_cta = '<a href="gioithieu#buoc-7-biet-phu" style="flex: 1; text-align: center; background: #c29b53; color: #fff; padding: 9px 12px; border-radius: 6px; font-size: 0.86rem; font-weight: 700; text-decoration: none;">Khám Phá Biệt Phủ Chi Tiết →</a>'

assert old_card_cta in content, "old_card_cta not found"
content = content.replace(old_card_cta, new_card_cta, 1)

# 4. Remove Target 1 (Image 1): Green MDS Living Cashflow Box
start_t1 = '    <!-- Phân Tích Dòng Tiền Thuê 215 Đêm (Đặc Quyền Chủ Sở Hữu) -->'
end_t1 = '    </div>\n\n  </div>\n</section>'
p1_start = content.find(start_t1)
p1_end = content.find(end_t1, p1_start)
assert p1_start != -1 and p1_end != -1, "Target 1 bounds not found"
chunk1_len = p1_end + len('    </div>\n') - p1_start
content = content[:p1_start] + content[p1_start + chunk1_len:]

# 5. Remove Target 2 (Image 3): Section 1 Biệt Phủ Điền Trang (#biet-phu)
start_t2 = '<!-- Backward Compatibility Anchor -->'
end_t2 = '<!-- ====================================================================\n     SECTION 2: BẢN SẮC VIỆT ĐƯƠNG ĐẠI (#ban-sac)'
p2_start = content.find(start_t2)
p2_end = content.find(end_t2, p2_start)
assert p2_start != -1 and p2_end != -1, "Target 2 bounds not found"
content = content[:p2_start] + content[p2_end:]

# 6. Remove Target 3 (Image 2): Section 4 Quy Hoạch & Pháp Lý (#quy-hoach)
start_t3 = '<!-- ====================================================================\n     SECTION 4: QUY HOẠCH TOÀN CẢNH 100HA & PHÁP LÝ (#quy-hoach)'
end_t3 = '<!-- ====================================================================\n     SECTION 5: TẠP CHÍ & NHẬN ĐỊNH (#tap-chi)'
p3_start = content.find(start_t3)
p3_end = content.find(end_t3, p3_start)
assert p3_start != -1 and p3_end != -1, "Target 3 bounds not found"
content = content[:p3_start] + content[p3_end:]

# 7. Update Footer Links
footer_target = '''<ul class="footer-links-list">
<li><a href="#biet-phu">Biệt Phủ Điền Trang</a></li>
<li><a href="#ban-sac">Bản Sắc Việt</a></li>
<li><a href="#tien-ich">Tiện Ích Điền Trang 30.000m²</a></li>
<li><a href="#quy-hoach">Quy Hoạch &amp; Pháp Lý</a></li>
<li><a href="#tap-chi">Tạp Chí &amp; Nhận Định</a></li>
<li><a href="#vi-tri">Vị Trí &amp; Bản Đồ</a></li>'''

footer_new = '''<ul class="footer-links-list">
<li><a href="#partner-toolkit">Dòng Sản Phẩm Điền Trang</a></li>
<li><a href="#ban-sac">Bản Sắc Việt</a></li>
<li><a href="#tien-ich">Tiện Ích Điền Trang 30.000m²</a></li>
<li><a href="#tap-chi">Tạp Chí &amp; Nhận Định</a></li>
<li><a href="#vi-tri">Vị Trí &amp; Bản Đồ</a></li>
<li><a href="gioithieu#buoc-7-biet-phu">Biệt Phủ Điền Trang (Pitch Deck)</a></li>'''

assert footer_target in content, "footer_target not found"
content = content.replace(footer_target, footer_new, 1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: index.html updated and cleaned!")
