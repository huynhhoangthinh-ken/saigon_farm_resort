import json
import re

with open('data/posts.json', 'r', encoding='utf-8') as f:
    existing_posts = json.load(f)

villa_ids = {101, 102, 103, 104, 111, 112, 113, 114, 115, 116, 117, 118, 119, 130, 131, 132}
other_posts = [p for p in existing_posts if p['id'] not in villa_ids]

# Clean up terminology in other_posts as well
for p in other_posts:
    if p.get('id') == 506:
        p['image'] = 'assets/Index_asset/Phoi_canh_tong_the/mds_living_01.jpg'
    # Replace Villa/Biệt thự/Dự án in titles and excerpts of other posts
    p['title'] = p['title'].replace('Villa', 'Điền Trang').replace('villa', 'điền trang').replace('biệt thự', 'điền trang').replace('Biệt thự', 'Điền Trang').replace('Biệt Thự', 'Điền Trang').replace('dự án', 'khu nghỉ dưỡng').replace('Dự án', 'Khu nghỉ dưỡng').replace('Dự Án', 'Khu Nghỉ Dưỡng')
    p['excerpt'] = p['excerpt'].replace('Villa', 'Điền Trang').replace('villa', 'điền trang').replace('biệt thự', 'điền trang').replace('Biệt thự', 'Điền Trang').replace('dự án', 'khu điền trang')
    p['content'] = p['content'].replace('biệt thự', 'điền trang').replace('Biệt thự', 'Điền Trang').replace('Biệt Thự', 'Điền Trang').replace('Villa', 'Điền Trang').replace('dự án', 'quần thể điền trang').replace('Dự án', 'Quần thể điền trang')

CONTACT_BANNER = """
<div style="background: #111; color: #fff; padding: 28px; border-radius: 8px; border-left: 4px solid #c9a96e; margin-top: 35px;">
  <h4 style="margin-bottom: 8px; font-family: var(--font-serif); font-size: 1.25rem; color: #c9a96e;">TỔNG ĐẠI LÝ TIẾP THỊ & PHÂN PHỐI: ĐẠI CHÚNG PROPERTIES</h4>
  <p style="margin-bottom: 6px; font-size: 0.95rem;">🏢 <strong>Phòng Quản Trị & Tư Vấn Điền Trang:</strong> Saigon Farm Resort</p>
  <p style="margin-bottom: 14px; font-size: 0.95rem;">📞 <strong>Hotline / Zalo Tiếp Nhận Thông Tin:</strong> <a href="https://zalo.me/0906060036" target="_blank" style="color:#0068FF; font-weight:700; text-decoration:underline;">0906060036</a></p>
  <a href="https://zalo.me/0906060036" target="_blank" style="display: inline-flex; align-items: center; gap: 8px; background: #0068FF; color: #fff; padding: 12px 24px; border-radius: 4px; font-weight: 700; text-decoration: none;">
    <i class="fa-solid fa-comment-dots"></i> Nhắn Zalo Nhận Bảng Thông Tin & Đặt Lịch Khảo Sát
  </a>
</div>
"""

new_estate_posts = [
    # =========================================================================
    # TRỤC 1: MẶT BẰNG CÔNG NĂNG & KIẾN TRÚC KHÔNG GIAN (4 BÀI)
    # =========================================================================
    {
        "id": 103,
        "title": "Điền Trang Sunrise 1: Giải Mã Mặt Bằng 1 Tầng Trệt Trải Rộng – Sự Tiện Nghi Mở Đón Nắng Mai",
        "excerpt": "Phân tích chi tiết layout trệt của Điền Trang Sunrise 1: kiến trúc trải ngang tối ưu ánh sáng tự nhiên, hồ bơi riêng biệt lập, không góc chết và sự gắn kết các thế hệ trong cùng một mặt bằng điền trang thuần khiết.",
        "image": "assets/Index_asset/02_Phoi_Canh_3D/05.3D_TKCS-SUNRISE_1_VILLA/05.3D_TKCS-NHA_GO_4_MAU_1-_07.2025/01._NGOAI_THAT/SFR_NGOAI_THAT_06.jpg",
        "date": "30 TH8 2026",
        "category": "Mặt Bằng & Kiến Trúc",
        "content": f"""
<p><strong>Điền Trang Sunrise 1</strong> là mẫu biệt phủ sinh thái 1 tầng (trệt) tiêu biểu hướng về phía Đông của quần thể <strong>Saigon Farm Resort</strong>. Được thiết kế dành riêng cho những gia đình tìm kiếm sự bình yên trọn vẹn, căn điền trang sở hữu ngôn ngữ kiến trúc mở, tận dụng tối đa lợi thế của khuôn viên đất rộng từ <strong>1.000m² đến 1.200m²</strong> để mang thiên nhiên vào từng ngóc ngách không gian sống.</p>

<div class="pull-quote">
  "Mặt bằng 1 tầng trải rộng của Điền Trang Sunrise 1 là lời giải hoàn hảo cho nếp sống gia đình đa thế hệ: không cầu thang ngăn cách, không giới hạn tầm nhìn, chỉ có thiên nhiên và sự gắn kết yêu thương."
</div>

<h2>1. Triết Lý Bố Cục Mặt Bằng Trải Ngang (Horizontal Layout)</h2>
<p>Khác biệt hoàn toàn với những mẫu nhà phố hay biệt thự cao tầng tại đô thị vốn bị chia cắt bởi cầu thang bộ, <strong>Điền Trang Sunrise 1</strong> được phát triển trên một mặt bằng trệt duy nhất. Bố cục trải ngang giúp toàn bộ các phòng chức năng chính (phòng khách, phòng bếp - ăn, 3 phòng ngủ) đều có ít nhất 2 mặt thoáng tiếp xúc trực tiếp với sân vườn và hồ bơi sinh thái.</p>

<div style="margin: 30px 0;">
  <img src="assets/Index_asset/Loai_hinh_Villa/MatBang_Sunrise_1.png" alt="Mặt bằng kiến trúc Điền Trang Sunrise 1" style="border-radius: 8px; width:100%; object-fit: contain; box-shadow: 0 4px 20px rgba(0,0,0,0.12); background: #fff; padding: 10px;">
  <p style="font-size: 0.85rem; color: #777; text-align: center; margin-top: 10px; font-style: italic;">Mặt bằng phân bổ công năng chi tiết Điền Trang Sunrise 1 (* Hình ảnh minh họa)</p>
</div>

<h2>2. Bảng Thông Số Kỹ Thuật Chi Tiết Điền Trang Sunrise 1</h2>
<div style="overflow-x: auto; margin: 25px 0;">
<table style="width: 100%; border-collapse: collapse; font-size: 0.95rem; background: #ffffff; border: 1px solid #e0d5c1; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.05); min-width: 600px;">
  <thead>
    <tr style="background: #fbf9f5; border-bottom: 2px solid #c9a96e; text-align: left;">
      <th style="padding: 14px 16px; color: #8a6d3b; font-weight: 700;">HẠNG MỤC</th>
      <th style="padding: 14px 16px; color: #8a6d3b; font-weight: 700;">THÔNG SỐ</th>
      <th style="padding: 14px 16px; color: #8a6d3b; font-weight: 700;">ĐẶC ĐIỂM CÔNG NĂNG</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid #eee;">
      <td style="padding: 14px 16px; font-weight: 700;">Diện tích khuôn viên</td>
      <td style="padding: 14px 16px; color: #2e7d32; font-weight: 700;">1.000m² - 1.200m²</td>
      <td style="padding: 14px 16px;">Khuôn viên vườn riêng biệt lập, bao bọc bởi hàng rào sinh thái thảo mộc</td>
    </tr>
    <tr style="border-bottom: 1px solid #eee; background: #faf9f6;">
      <td style="padding: 14px 16px; font-weight: 700;">Số tầng & Phòng ngủ</td>
      <td style="padding: 14px 16px;">1 Tầng • 3 Phòng Ngủ</td>
      <td style="padding: 14px 16px;">1 Master Suite view hồ bơi + 2 Phòng ngủ tiêu chuẩn khép kín</td>
    </tr>
    <tr style="border-bottom: 1px solid #eee;">
      <td style="padding: 14px 16px; font-weight: 700;">Diện tích xây dựng</td>
      <td style="padding: 14px 16px;">~210m²</td>
      <td style="padding: 14px 16px;">Mật độ xây dựng lý tưởng ~20%, 80% diện tích cho thiên nhiên</td>
    </tr>
    <tr style="border-bottom: 1px solid #eee; background: #faf9f6;">
      <td style="padding: 14px 16px; font-weight: 700;">Hồ bơi tràn bờ riêng</td>
      <td style="padding: 14px 16px; color: #0068FF; font-weight: 700;">45m²</td>
      <td style="padding: 14px 16px;">Hệ thống lọc khoáng muối tự nhiên, deck gỗ tắm nắng liền kề</td>
    </tr>
    <tr>
      <td style="padding: 14px 16px; font-weight: 700;">Vườn hoa & Sân cỏ</td>
      <td style="padding: 14px 16px;">> 700m²</td>
      <td style="padding: 14px 16px;">Trồng cây ăn trái, hoa chuông vàng, hương thảo và lối dạo sỏi trắng</td>
    </tr>
  </tbody>
</table>
</div>

<h2>3. Phân Tích Công Năng Chi Tiết Từng Khu Vực</h2>
<ul>
  <li><strong>Đại sảnh & Phòng khách liên hoàn bếp:</strong> Không gian mở rộng hơn 65m² với hệ vách kính kịch trần, kết nối trực tiếp ra hiên gỗ và hồ bơi.</li>
  <li><strong>Phòng ngủ Master Suite:</strong> Phòng ngủ lớn với ban công riêng, bồn tắm ngâm thảo dược hướng vườn tĩnh lặng, mở cửa là chạm làn nước trong xanh.</li>
  <li><strong>2 Phòng ngủ phụ:</strong> Bố trí đối xứng khoa học, đảm bảo sự riêng tư tuyệt đối cho con trẻ hoặc khách quý, có lối đi riêng ra vườn cảnh quan.</li>
</ul>

<div class="key-takeaways">
  <h3>Điểm Nhấn Đắt Giá Của Điền Trang Sunrise 1</h3>
  <ul>
    <li>An toàn tuyệt đối cho người lớn tuổi và trẻ nhỏ nhờ thiết kế không bậc cấp, một tầng phẳng duy nhất.</li>
    <li>Đón trọn ánh bình minh dịu lành lúc 6:00 sáng, kích hoạt năng lượng tích cực cho ngày mới.</li>
    <li>Tối ưu chi phí xây dựng và bảo trì định kỳ nhưng vẫn giữ trọn vẹn đặc quyền nghỉ dưỡng đẳng cấp 5 sao.</li>
  </ul>
</div>

{CONTACT_BANNER}
"""
    },
    {
        "id": 104,
        "title": "Dinh Thự Sunrise 2: Đỉnh Cao Kiến Trúc Đại Điền Trang 4PN 1.500m² – Đại Sảnh Trần Cao & Sky Deck 360°",
        "excerpt": "Bóc tách không gian dinh thự đỉnh cao nhất Saigon Farm Resort: khuôn viên 1.500m², 4 phòng ngủ master, đại sảnh trần cao gỗ quý 6m, bể bơi vô cực 53m² và tầng thượng Sky Deck ngắm bình minh tuyệt mỹ.",
        "image": "assets/Index_asset/02_Phoi_Canh_3D/07.3D_TKCS-NHA_GO_4_MAU_2-_02.2026/07.TKCS-NHA_GO_4-MAU_2/01.NGOAI_THAT/SFR_01.jpg",
        "date": "30 TH8 2026",
        "category": "Mặt Bằng & Kiến Trúc",
        "content": f"""
<p>Được định vị là dòng sản phẩm <strong>Di Sản Truyền Đời</strong> danh giá nhất tại <strong>Saigon Farm Resort</strong>, <strong>Dinh Thự Sunrise 2</strong> là tác phẩm kiến trúc đỉnh cao dành cho các gia tộc thượng lưu. Tọa lạc tại những vị trí kim cương hướng thẳng ra mặt hồ sinh thái 100ha, mỗi căn dinh thự sở hữu khuôn viên khổng lồ lên tới <strong>1.500m²</strong> cùng kiến trúc 4 phòng ngủ tráng lệ.</p>

<div class="pull-quote">
  "Dinh Thự Sunrise 2 không đơn thuần là một căn biệt phủ nghỉ dưỡng, đây là tuyên ngôn về vị thế, gu thẩm mỹ tinh tế và là bảo chứng giá trị gia tộc trường tồn theo thời gian."
</div>

<h2>1. Kiến Trúc Đại Sảnh Trần Cao 6m & Khung Kính Panorama</h2>
<p>Bước qua cánh cổng gỗ nguyên khối và khoảng sân đón rộng lớn, gia chủ sẽ choáng ngợp trước đại sảnh phòng khách với chiều cao thông tầng gần <strong>6 mét</strong>. Hệ khung kết cấu gỗ tự nhiên kết hợp cùng đá hoa cương nguyên tấm và vách kính thông suốt từ sàn đến trần tạo nên một không gian bề thế, đón trọn ánh sáng ban mai lộng lẫy.</p>

<div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 16px; margin: 30px 0;">
  <div>
    <img src="assets/Index_asset/02_Phoi_Canh_3D/07.3D_TKCS-NHA_GO_4_MAU_2-_02.2026/07.TKCS-NHA_GO_4-MAU_2/01.NGOAI_THAT/SFR_02.jpg" alt="Mặt đứng dinh thự Sunrise 2" style="border-radius: 8px; width:100%; height: 280px; object-fit: cover; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
    <p style="font-size: 0.8rem; color: #888; text-align: center; margin-top: 6px; font-style: italic;">Phối cảnh góc Dinh Thự Sunrise 2 (* Hình ảnh minh họa)</p>
  </div>
  <div>
    <img src="assets/Index_asset/Loai_hinh_Villa/MatBang_Sunrise_2.png" alt="Mặt bằng dinh thự Sunrise 2" style="border-radius: 8px; width:100%; height: 280px; object-fit: contain; background:#fff; padding:6px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
    <p style="font-size: 0.8rem; color: #888; text-align: center; margin-top: 6px; font-style: italic;">Mặt bằng công năng dinh thự 1.500m² (* Hình ảnh minh họa)</p>
  </div>
</div>

<h2>2. Bảng Thông Số Kỹ Thuật Dinh Thự Sunrise 2</h2>
<div style="overflow-x: auto; margin: 25px 0;">
<table style="width: 100%; border-collapse: collapse; font-size: 0.95rem; background: #ffffff; border: 1px solid #e0d5c1; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.05); min-width: 600px;">
  <thead>
    <tr style="background: #fbf9f5; border-bottom: 2px solid #c9a96e; text-align: left;">
      <th style="padding: 14px 16px; color: #8a6d3b; font-weight: 700;">HẠNG MỤC</th>
      <th style="padding: 14px 16px; color: #8a6d3b; font-weight: 700;">THÔNG SỐ</th>
      <th style="padding: 14px 16px; color: #8a6d3b; font-weight: 700;">ĐẶC QUYỀN ĐỈNH CAO</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid #eee;">
      <td style="padding: 14px 16px; font-weight: 700;">Khuôn viên đất</td>
      <td style="padding: 14px 16px; color: #2e7d32; font-weight: 700;">1.500m² (Đại Điền Trang Siêu VIP)</td>
      <td style="padding: 14px 16px;">Vị trí mặt hồ đắt giá nhất toàn khu, thế đất nở hậu đón tài lộc</td>
    </tr>
    <tr style="border-bottom: 1px solid #eee; background: #faf9f6;">
      <td style="padding: 14px 16px; font-weight: 700;">Cấu trúc công năng</td>
      <td style="padding: 14px 16px;">4 Phòng Ngủ Master Khép Kín</td>
      <td style="padding: 14px 16px;">Tất cả các phòng đều có ban công, bồn tắm kính mở và walk-in closet</td>
    </tr>
    <tr style="border-bottom: 1px solid #eee;">
      <td style="padding: 14px 16px; font-weight: 700;">Bể bơi vô cực</td>
      <td style="padding: 14px 16px; color: #0068FF; font-weight: 700;">53m² tràn viền</td>
      <td style="padding: 14px 16px;">Hệ thống sục Jacuzzi nước ấm, hệ đèn LED quang phổ dưới nước</td>
    </tr>
    <tr style="border-bottom: 1px solid #eee; background: #faf9f6;">
      <td style="padding: 14px 16px; font-weight: 700;">Sky Deck ngắm cảnh</td>
      <td style="padding: 14px 16px;">40m² trên tầng thượng</td>
      <td style="padding: 14px 16px;">Khu vực ngắm sao đêm, thưởng trà và tiệc rượu vang riêng tư 360°</td>
    </tr>
    <tr>
      <td style="padding: 14px 16px; font-weight: 700;">Sân vườn & Bãi cỏ Gala</td>
      <td style="padding: 14px 16px;">> 1.000m²</td>
      <td style="padding: 14px 16px;">Đủ sức tổ chức tiệc BBQ ngoài trời lên đến 50 - 80 khách VIP</td>
    </tr>
  </tbody>
</table>
</div>

<h2>3. Không Gian Tiện Nghi Độc Bản Dành Riêng Cho Giới Tinh Hoa</h2>
<p>Sunrise 2 được trang bị các phòng chức năng cao cấp hiếm có: phòng Cigar & Hầm rượu gia đình, phòng spa xông hơi thảo dược tại gia, khu bếp ướt và bếp khô phân tách theo tiêu chuẩn điền trang 5 sao quốc tế.</p>

<div class="key-takeaways">
  <h3>Giá Trị Cốt Lõi Của Dinh Thự Sunrise 2</h3>
  <ul>
    <li>Số lượng cực kỳ giới hạn, chiếm chưa đầy 10% tổng số căn toàn quần thể.</li>
    <li>Khuôn viên 1.500m² mở ra tiềm năng thiết kế cảnh quan cá nhân hóa độc bản (vườn Nhật, sân tập golf putting green mini, đài phun nước).</li>
    <li>Bảo chứng tài chính vững chãi và là di sản truyền lại qua nhiều thế hệ.</li>
  </ul>
</div>

{CONTACT_BANNER}
"""
    },
    {
        "id": 101,
        "title": "Điền Trang Sunset 1: Bố Cục Sân Trong (Courtyard) – Gắn Kết Đa Thế Hệ Trong Nếp Nhà 1 Tầng",
        "excerpt": "Khám phá giải pháp kiến trúc sân trong (Courtyard) độc đáo của Điền Trang Sunset 1: khuôn viên 1.000m², thông gió chéo vi khí hậu, hồ bơi 45m², vườn cây ăn trái 260m² và không gian sum vầy ấm cúng.",
        "image": "assets/Index_asset/02_Phoi_Canh_3D/09.3D_TKCS-SUNSET_VILLA/SUNSET_1_VILLA/SFR_07.SAN_TRONG.jpg",
        "date": "30 TH8 2026",
        "category": "Mặt Bằng & Kiến Trúc",
        "content": f"""
<p><strong>Điền Trang Sunset 1</strong> là biểu tượng kiến trúc lấy cảm hứng từ cấu trúc nhà vườn truyền thống Việt Nam kết hợp phong cách nghỉ dưỡng nhiệt đới đương đại. Với điểm nhấn trung tâm là <strong>Khoảng Sân Trong (Courtyard)</strong>, ngôi điền trang như một ốc đảo xanh khép kín, mang lại sự riêng tư tối đa và sự gắn kết ấm áp giữa các thành viên trong gia đình.</p>

<div class="pull-quote">
  "Khoảng sân trong tại Sunset 1 là 'lá phổi xanh' điều hòa toàn bộ vi khí hậu trong nhà, biến mỗi khoảnh khắc bước ra hành lang thành một chuyến dạo chơi giữa cỏ hoa và ánh sáng."
</div>

<h2>1. Giải Mã Nghệ Thuật Thiết Kế Sân Trong (Courtyard Concept)</h2>
<p>Không gian của <strong>Điền Trang Sunset 1</strong> được bố trí bao quanh một khu vườn nhiệt đới và giếng trời trung tâm. Cấu trúc này mang lại 3 ưu thế vượt trội:</p>
<ul>
  <li><strong>Thông gió xuyên phòng (Cross Ventilation):</strong> Không khí mát lành từ mặt hồ nước được hút qua sân trong, làm mát tự nhiên toàn bộ các phòng ngủ và phòng khách mà không phụ thuộc vào điều hòa.</li>
  <li><strong>Ánh sáng tự nhiên 100%:</strong> Bất kể ngày hay đêm, các phòng đều ngập tràn ánh sáng trời nhưng không bị chói gắt nhờ lớp tán cây xanh che chắn tự nhiên.</li>
  <li><strong>Góc nhìn xanh 360 độ:</strong> Ngồi ở bất kỳ vị trí nào trong nhà, mắt bạn đều chạm vào màu xanh mướt mát của cây cỏ và làn nước hồ bơi.</li>
</ul>

<div style="margin: 30px 0;">
  <img src="assets/Index_asset/Loai_hinh_Villa/MatBang_Sunset_1.png" alt="Mặt bằng Điền Trang Sunset 1" style="border-radius: 8px; width:100%; object-fit: contain; box-shadow: 0 4px 20px rgba(0,0,0,0.12); background:#fff; padding:10px;">
  <p style="font-size: 0.85rem; color: #777; text-align: center; margin-top: 10px; font-style: italic;">Mặt bằng sân trong và phân khu Điền Trang Sunset 1 (* Hình ảnh minh họa)</p>
</div>

<h2>2. Bảng Cơ Cấu Không Gian Điền Trang Sunset 1</h2>
<div style="overflow-x: auto; margin: 25px 0;">
<table style="width: 100%; border-collapse: collapse; font-size: 0.95rem; background: #ffffff; border: 1px solid #e0d5c1; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.05); min-width: 600px;">
  <thead>
    <tr style="background: #fbf9f5; border-bottom: 2px solid #c9a96e; text-align: left;">
      <th style="padding: 14px 16px; color: #8a6d3b; font-weight: 700;">KHU VỰC</th>
      <th style="padding: 14px 16px; color: #8a6d3b; font-weight: 700;">DIỆN TÍCH</th>
      <th style="padding: 14px 16px; color: #8a6d3b; font-weight: 700;">CHỨC NĂNG & TIỆN ÍCH</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid #eee;">
      <td style="padding: 14px 16px; font-weight: 700;">Tổng diện tích khuôn viên</td>
      <td style="padding: 14px 16px; color: #2e7d32; font-weight: 700;">~1.000m²</td>
      <td style="padding: 14px 16px;">Khuôn viên vuông vắn, thế đất phẳng vững chãi</td>
    </tr>
    <tr style="border-bottom: 1px solid #eee; background: #faf9f6;">
      <td style="padding: 14px 16px; font-weight: 700;">Diện tích sàn xây dựng</td>
      <td style="padding: 14px 16px;">~205m²</td>
      <td style="padding: 14px 16px;">3 Phòng ngủ master, phòng khách lớn, bếp mở Farm-to-Table</td>
    </tr>
    <tr style="border-bottom: 1px solid #eee;">
      <td style="padding: 14px 16px; font-weight: 700;">Sân trong (Courtyard)</td>
      <td style="padding: 14px 16px; color: #c9a96e; font-weight: 700;">38m²</td>
      <td style="padding: 14px 16px;">Trồng cây thị, hoa chuối cảnh, sỏi trắng tự nhiên và tiểu cảnh nước</td>
    </tr>
    <tr style="border-bottom: 1px solid #eee; background: #faf9f6;">
      <td style="padding: 14px 16px; font-weight: 700;">Hồ bơi tràn viền</td>
      <td style="padding: 14px 16px; color: #0068FF; font-weight: 700;">45m²</td>
      <td style="padding: 14px 16px;">Định vị góc ngắm trọn hoàng hôn rực rỡ buổi chiều tà</td>
    </tr>
    <tr>
      <td style="padding: 14px 16px; font-weight: 700;">Vườn cây ăn trái hữu cơ</td>
      <td style="padding: 14px 16px;">260m²</td>
      <td style="padding: 14px 16px;">Bưởi da xanh, xoài cát Hòa Lộc, ổi nữ hoàng và mận An Phước</td>
    </tr>
  </tbody>
</table>
</div>

<div class="key-takeaways">
  <h3>Tại Sao Sunset 1 Phù Hợp Với Gia Đình Bạn?</h3>
  <ul>
    <li>Thiết kế 1 tầng mang tính riêng tư cao, che chắn gió mạnh và bụi bên ngoài nhờ cấu trúc sân trong.</li>
    <li>Khu vườn ăn trái rộng 260m² là không gian tuyệt vời để con trẻ trải nghiệm thu hoạch trái cây tự nhiên.</li>
    <li>Vị trí hướng Tây Nam đón trọn những buổi chiều hoàng hôn tím biếc bên ly trà chiều thảnh thơi.</li>
  </ul>
</div>

{CONTACT_BANNER}
"""
    },
    {
        "id": 102,
        "title": "Điền Trang Sunset 2: Bố Cục Không Gian 2 Tầng – Tầm Nhìn Panorama Ôm Trọn Hoàng Hôn Hồ 100ha",
        "excerpt": "Phân tích bố cục 2 tầng bề thế của Điền Trang Sunset 2: khuôn viên 1.200m², vườn cây ăn trái 482m², ban công ngắm hoàng hôn lầu 1 và không gian sinh hoạt chung tách biệt tĩnh - động hoàn hảo.",
        "image": "assets/Index_asset/02_Phoi_Canh_3D/09.3D_TKCS-SUNSET_VILLA/SUNSET_2_VILLA/SFR_04.PC_01.jpg",
        "date": "30 TH8 2026",
        "category": "Mặt Bằng & Kiến Trúc",
        "content": f"""
<p>Là mẫu biệt phủ 2 tầng nổi bật hướng về phía Tây của <strong>Saigon Farm Resort</strong>, <strong>Điền Trang Sunset 2</strong> được thiết kế nhằm nâng tầm trải nghiệm thị giác lên một nấc thang mới. Với cao độ tầng 2 và ban công panorama rộng mở, căn điền trang giúp gia chủ thưởng ngoạn trọn vẹn khoảnh khắc mặt trời từ từ lặn xuống mặt hồ 100ha trong sắc cam rực rỡ.</p>

<div class="pull-quote">
  "Đứng trên ban công lầu 2 của Sunset 2 khi hoàng hôn buông xuống, bạn sẽ hiểu vì sao người ta gọi đây là bức tranh thủy mặc sống động nhất của vùng duyên hải Đất Đỏ."
</div>

<h2>1. Bố Cục Phân Tách Không Gian 'Động - Tĩnh' Hoàn Hảo</h2>
<p>Cấu trúc 2 tầng của <strong>Điền Trang Sunset 2</strong> cho phép phân chia công năng vô cùng khoa học:</p>
<ul>
  <li><strong>Tầng 1 (Khu Vực Gắn Kết & Tiếp Khách):</strong> Đại sảnh, phòng khách lớn, khu bàn ăn 10 chỗ nối liền đảo bếp hiện đại, 1 phòng ngủ master cho người lớn tuổi view thẳng vườn cây và hồ bơi ngoài trời.</li>
  <li><strong>Tầng 2 (Khu Nghỉ Ngơi Riêng Tư & Thư Giãn):</strong> 2 phòng ngủ khép kín với ban công kính lớn, phòng sinh hoạt chung (Family Lounge) kết hợp thư phòng và khu Sunset Deck ngoài trời.</li>
</ul>

<div style="margin: 30px 0;">
  <img src="assets/Index_asset/Loai_hinh_Villa/MatBang_Sunset_2.png" alt="Mặt bằng kiến trúc Điền Trang Sunset 2" style="border-radius: 8px; width:100%; object-fit: contain; box-shadow: 0 4px 20px rgba(0,0,0,0.12); background:#fff; padding:10px;">
  <p style="font-size: 0.85rem; color: #777; text-align: center; margin-top: 10px; font-style: italic;">Mặt bằng 2 tầng chi tiết Điền Trang Sunset 2 (* Hình ảnh minh họa)</p>
</div>

<h2>2. Bảng Quy Chuẩn Kỹ Thuật Điền Trang Sunset 2</h2>
<div style="overflow-x: auto; margin: 25px 0;">
<table style="width: 100%; border-collapse: collapse; font-size: 0.95rem; background: #ffffff; border: 1px solid #e0d5c1; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.05); min-width: 600px;">
  <thead>
    <tr style="background: #fbf9f5; border-bottom: 2px solid #c9a96e; text-align: left;">
      <th style="padding: 14px 16px; color: #8a6d3b; font-weight: 700;">HẠNG MỤC</th>
      <th style="padding: 14px 16px; color: #8a6d3b; font-weight: 700;">THÔNG SỐ</th>
      <th style="padding: 14px 16px; color: #8a6d3b; font-weight: 700;">ƯU THẾ NỔI BẬT</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid #eee;">
      <td style="padding: 14px 16px; font-weight: 700;">Khuôn viên đất</td>
      <td style="padding: 14px 16px; color: #2e7d32; font-weight: 700;">1.200m²</td>
      <td style="padding: 14px 16px;">Thửa đất rộng rãi, tầm nhìn khoáng đạt không bị che chắn</td>
    </tr>
    <tr style="border-bottom: 1px solid #eee; background: #faf9f6;">
      <td style="padding: 14px 16px; font-weight: 700;">Tổng diện tích xây dựng</td>
      <td style="padding: 14px 16px;">~280m² (2 Tầng)</td>
      <td style="padding: 14px 16px;">3 Phòng ngủ Master • 4 WC • Phòng SHC lầu 1 • Ban công Sky Lounge</td>
    </tr>
    <tr style="border-bottom: 1px solid #eee;">
      <td style="padding: 14px 16px; font-weight: 700;">Vườn cây ăn trái biệt lập</td>
      <td style="padding: 14px 16px; color: #c9a96e; font-weight: 700;">482m²</td>
      <td style="padding: 14px 16px;">Khu vườn sum suê lớn nhất trong các mẫu biệt phủ 3 phòng ngủ</td>
    </tr>
    <tr style="border-bottom: 1px solid #eee; background: #faf9f6;">
      <td style="padding: 14px 16px; font-weight: 700;">Hồ bơi vô cực & Sân cỏ</td>
      <td style="padding: 14px 16px; color: #0068FF; font-weight: 700;">Hồ 48m² + Cỏ 220m²</td>
      <td style="padding: 14px 16px;">Bể bơi tràn bờ kết nối sàn tắm nắng gỗ Teak ngoài trời</td>
    </tr>
    <tr>
      <td style="padding: 14px 16px; font-weight: 700;">Ban công Panorama lầu 1</td>
      <td style="padding: 14px 16px;">35m²</td>
      <td style="padding: 14px 16px;">Góc thưởng rượu vang ngắm hoàng hôn đỉnh cao nhất quần thể</td>
    </tr>
  </tbody>
</table>
</div>

<div class="key-takeaways">
  <h3>Điểm Nhấn Độc Quyền Tại Sunset 2</h3>
  <ul>
    <li>Cao độ tầng 2 mở rộng góc nhìn bao quát toàn bộ mặt nước hồ 100ha và cánh đồng lúa liền kề.</li>
    <li>Khu vườn ăn trái 482m² tạo nên vành đai sinh thái che mát tự nhiên, làm dịu hoàn toàn nắng chiều.</li>
    <li>Mẫu nhà lý tưởng cho các buổi tiệc cuối tuần cùng bạn bè và đối tác thân thiết.</li>
  </ul>
</div>

{CONTACT_BANNER}
"""
    },

    # =========================================================================
    # TRỤC 2: VI KHÍ HẬU, HƯỚNG NẮNG GIÓ & PHONG THỦY SINH THÁI (4 BÀI)
    # =========================================================================
    {
        "id": 111,
        "title": "Phong Thủy Điền Trang Hướng Đông (Sunrise 1 & 2): Đón Vượng Khí Nắng Sớm & Năng Lượng Tái Sinh",
        "excerpt": "Phân tích phong thủy nhà hướng Đông tại Saigon Farm Resort: thế đất Tọa Sơn Hướng Thủy, trường năng lượng sinh khí buổi sớm và tác động kích hoạt sức khỏe, sự hanh thông cho gia chủ.",
        "image": "assets/Index_asset/02_Phoi_Canh_3D/05.3D_TKCS-SUNRISE_1_VILLA/05.3D_TKCS-NHA_GO_4_MAU_1-_07.2025/01._NGOAI_THAT/SFR_NGOAI_THAT_(2).jpg",
        "date": "30 TH8 2026",
        "category": "Phong Thủy & Vi Khí Hậu",
        "content": f"""
<p>Trong khoa học phong thủy Á Đông, hướng Đông (quẻ Chấn - thuộc hành Mộc) tượng trưng cho mùa xuân, sự sinh sôi nảy nở và khởi đầu của mọi nguồn năng lượng cát lành. Tại <strong>Saigon Farm Resort</strong>, cụm biệt phủ <strong>Sunrise 1 & Dinh Thự Sunrise 2</strong> được quy hoạch với thế đất đón trọn hướng Đông nhằm mang lại vượng khí dồi dào cho chủ nhân.</p>

<div class="pull-quote">
  "Mặt trời mọc ở hướng Đông mang theo ánh sáng tinh khôi chứa nhiều photon năng lượng dương thuần khiết, giúp thanh lọc không gian sống và kích hoạt khả năng tự chữa lành của cơ thể."
</div>

<h2>1. Thế Đất 'Tọa Khang Hướng Thủy' Của Cụm Điền Trang Sunrise</h2>
<p>Cụm điền trang Sunrise được bố trí với lưng tựa vào dải đồi xanh thoai thoải và mặt tiền hướng thẳng ra mặt gương nước trong xanh. Đây là thế đất <em>"Thủy tụ sinh tài, Sơn định an khang"</em> chuẩn mực:</p>
<ul>
  <li><strong>Đón tia nắng đầu ngày (Morning Sunlight):</strong> Ánh nắng từ 6:00 đến 8:30 sáng giàu vitamin D tự nhiên, giúp điều hòa nhịp sinh học cơ thể, tăng cường hệ miễn dịch cho người già và phát triển chiều cao cho trẻ nhỏ.</li>
  <li><strong>Trường khí thanh tịnh:</strong> Không khí buổi sáng sớm trên mặt hồ mang hàm lượng oxy tinh sạch cao, không khói bụi đô thị, giúp tinh thần minh mẫn, an yên.</li>
</ul>

<h2>2. Bảng Đối Soát Phong Thủy Cụm Sunrise 1 & Sunrise 2</h2>
<div style="overflow-x: auto; margin: 25px 0;">
<table style="width: 100%; border-collapse: collapse; font-size: 0.95rem; background: #ffffff; border: 1px solid #e0d5c1; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.05); min-width: 600px;">
  <thead>
    <tr style="background: #fbf9f5; border-bottom: 2px solid #c9a96e; text-align: left;">
      <th style="padding: 14px 16px; color: #8a6d3b; font-weight: 700;">YẾU TỐ PHONG THỦY</th>
      <th style="padding: 14px 16px; color: #8a6d3b; font-weight: 700;">ĐIỀN TRANG SUNRISE 1</th>
      <th style="padding: 14px 16px; color: #8a6d3b; font-weight: 700;">DINH THỰ SUNRISE 2</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid #eee;">
      <td style="padding: 14px 16px; font-weight: 700;">Hướng chính & Cung vị</td>
      <td style="padding: 14px 16px;">Chính Đông (Cung Chấn)</td>
      <td style="padding: 14px 16px; color: #2e7d32; font-weight:700;">Đông Nam (Cung Tốn - Cung Tài Lộc)</td>
    </tr>
    <tr style="border-bottom: 1px solid #eee; background: #faf9f6;">
      <td style="padding: 14px 16px; font-weight: 700;">Ngũ hành chủ đạo</td>
      <td style="padding: 14px 16px;">Mộc đới Thủy (Cây xanh & Hồ bơi)</td>
      <td style="padding: 14px 16px;">Thủy - Mộc - Thổ hòa hợp, tích tụ trường khí</td>
    </tr>
    <tr style="border-bottom: 1px solid #eee;">
      <td style="padding: 14px 16px; font-weight: 700;">Thế đất & Minh đường</td>
      <td style="padding: 14px 16px;">Minh đường phẳng rộng, cỏ xanh bao bọc</td>
      <td style="padding: 14px 16px;">Đại minh đường 1.500m², hồ bơi vô cực tụ thủy</td>
    </tr>
    <tr>
      <td style="padding: 14px 16px; font-weight: 700;">Ý nghĩa phong thủy</td>
      <td style="padding: 14px 16px;">Gia đạo bình an, sức khỏe trường thọ</td>
      <td style="padding: 14px 16px; color: #0068FF; font-weight:700;">Sự nghiệp thăng tiến, tài lộc vượng phát truyền đời</td>
    </tr>
  </tbody>
</table>
</div>

<div class="key-takeaways">
  <h3>Chuyên Gia Nhận Định Về Cụm Sunrise</h3>
  <ul>
    <li>Căn điền trang hướng Đông mát mẻ vào buổi chiều do được bóng râm che chắn tự nhiên từ 13:00 trở đi.</li>
    <li>Thích hợp nhất cho các chủ nhân mệnh Mộc, Hỏa và Thủy mong muốn tìm kiếm một không gian tĩnh dưỡng, tái tạo năng lượng sau chuỗi ngày làm việc căng thẳng.</li>
  </ul>
</div>

{CONTACT_BANNER}
"""
    },
    {
        "id": 112,
        "title": "Giải Pháp Vi Khí Hậu Điền Trang Hướng Tây (Sunset 1 & 2): Đón Gió Nam Mát Lành & Nghệ Thuật Lọc Nắng Chiều",
        "excerpt": "Giải mã bài toán kiến trúc nhiệt đới tại Sunset 1 & Sunset 2: kết hợp hành lang đệm, lam gỗ tự nhiên, thảm thực vật 3 tầng tán và gió hồ 100ha để biến nắng chiều thành khoảnh khắc hoàng hôn lãng mạn.",
        "image": "assets/Index_asset/02_Phoi_Canh_3D/09.3D_TKCS-SUNSET_VILLA/SUNSET_2_VILLA/SFR_02.MAT_DUNG.jpg",
        "date": "30 TH8 2026",
        "category": "Phong Thủy & Vi Khí Hậu",
        "content": f"""
<p>Nhiều người thường e ngại hướng Tây sẽ bị nắng nóng vào buổi chiều. Tuy nhiên, tại <strong>Saigon Farm Resort</strong>, các kiến trúc sư bậc thầy đã biến hướng Tây của <strong>Điền Trang Sunset 1 & Sunset 2</strong> thành một tuyệt tác nghỉ dưỡng nhờ ứng dụng nghệ thuật xử lý <strong>Vi Khí Hậu Đa Tầng</strong>.</p>

<div class="pull-quote">
  "Nắng hướng Tây qua bàn tay kiến trúc sư tài hoa không còn là sự oi bức, mà trở thành chất liệu ánh sáng nghệ thuật – nơi mỗi buổi chiều biến thành một kiệt tác hoàng hôn rực rỡ."
</div>

<h2>1. Ba Lớp Bảo Vệ Vi Khí Hậu Độc Quyền Tại Cụm Sunset</h2>
<ul>
  <li><strong>Lớp 1: Mặt nước hồ 100ha hạ nhiệt gió:</strong> Gió hướng Tây Nam thổi qua mặt nước mênh mông hơn 100ha được bão hòa hơi ẩm, giảm nhiệt độ tức thì từ 3 - 5°C trước khi chạm tới khuôn viên điền trang.</li>
  <li><strong>Lớp 2: Vườn cây ăn trái 3 tầng tán:</strong> Khu vườn từ 260m² - 482m² với các tầng cây cao (dừa, xoài), tầng trung (bưởi, mận) và tầng thấp (cỏ nhung, hoa thảo mộc) tạo thành tấm màng lọc nhiệt tự nhiên hoàn hảo.</li>
  <li><strong>Lớp 3: Mái hiên sâu & Lam chắn nắng gỗ tự nhiên:</strong> Hệ mái đua rộng 2.5m cùng lam chắn xoay góc giúp cản bức xạ trực tiếp, chỉ giữ lại ánh sáng êm dịu phản chiếu vào không gian nội thất.</li>
</ul>

<h2>2. Bảng So Sánh Nhiệt Độ & Vi Khí Hậu Thực Tế</h2>
<div style="overflow-x: auto; margin: 25px 0;">
<table style="width: 100%; border-collapse: collapse; font-size: 0.95rem; background: #ffffff; border: 1px solid #e0d5c1; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.05); min-width: 600px;">
  <thead>
    <tr style="background: #fbf9f5; border-bottom: 2px solid #c9a96e; text-align: left;">
      <th style="padding: 14px 16px; color: #8a6d3b; font-weight: 700;">THỜI ĐIỂM TRONG NGÀY</th>
      <th style="padding: 14px 16px; color: #8a6d3b; font-weight: 700;">ĐÔ THỊ TP.HCM</th>
      <th style="padding: 14px 16px; color: #8a6d3b; font-weight: 700;">ĐIỀN TRANG SUNSET (SAIGON FARM RESORT)</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid #eee;">
      <td style="padding: 14px 16px; font-weight: 700;">12:00 Trưa (Đỉnh điểm nắng)</td>
      <td style="padding: 14px 16px; color: #d32f2f;">36°C - 38°C (Hiệu ứng đảo nhiệt)</td>
      <td style="padding: 14px 16px; color: #2e7d32; font-weight: 700;">29°C - 31°C (Mát mẻ dưới bóng cây & hồ nước)</td>
    </tr>
    <tr style="border-bottom: 1px solid #eee; background: #faf9f6;">
      <td style="padding: 14px 16px; font-weight: 700;">16:30 Chiều (Khoảnh khắc hoàng hôn)</td>
      <td style="padding: 14px 16px;">34°C - Ngột ngạt khói bụi</td>
      <td style="padding: 14px 16px; color: #0068FF; font-weight: 700;">26°C - 28°C - Gió hồ lồng lộng, êm dịu</td>
    </tr>
    <tr>
      <td style="padding: 14px 16px; font-weight: 700;">20:00 Tối (Nghỉ ngơi)</td>
      <td style="padding: 14px 16px;">30°C - Bức xạ tường bê tông</td>
      <td style="padding: 14px 16px; color: #2e7d32; font-weight: 700;">22°C - 24°C - Mát lành, sảng khoái tự nhiên</td>
    </tr>
  </tbody>
</table>
</div>

<div class="key-takeaways">
  <h3>Đặc Quyền Của Cư Dân Cụm Sunset</h3>
  <ul>
    <li>Tận hưởng trọn vẹn cảnh sắc hoàng hôn lộng lẫy nhất trong ngày mà không chịu ảnh hưởng của nhiệt độ gay gắt.</li>
    <li>Không khí buổi tối mát mẻ nhanh chóng nhờ hơi nước từ hồ và sân vườn tỏa ra.</li>
  </ul>
</div>

{CONTACT_BANNER}
"""
    },
    {
        "id": 113,
        "title": "Trải Nghiệm 24 Giờ Vi Khí Hậu: So Sánh Nhịp Thở Sinh Thái Giữa Cụm Sunrise & Sunset",
        "excerpt": "Hành trình 24 giờ trải nghiệm nhịp sống sinh thái tại Saigon Farm Resort: theo dõi sự biến chuyển kỳ diệu của ánh sáng, nhiệt độ, độ ẩm và ngọn gió tại cụm điền trang đón Bình Minh (Sunrise) và Hoàng Hôn (Sunset).",
        "image": "assets/Index_asset/Phoicanh/S01_Final_Fix.jpg",
        "date": "30 TH8 2026",
        "category": "Phong Thủy & Vi Khí Hậu",
        "content": f"""
<p>Mỗi ngày tại <strong>Saigon Farm Resort</strong> là một bản giao hưởng thiên nhiên sống động. Sự khác biệt về hướng tiếp xúc ánh sáng giữa cụm điền trang <strong>Sunrise (Bình Minh)</strong> và <strong>Sunset (Hoàng Hôn)</strong> mang lại hai phong cách trải nghiệm nghỉ dưỡng hoàn toàn độc đáo cho gia chủ.</p>

<div class="pull-quote">
  "Nếu Sunrise là khúc ca rộn rã đón chào ngày mới tràn đầy sức sống thì Sunset lại là bản tình ca êm dịu, lắng đọng sau những bộn bề của cuộc sống."
</div>

<h2>1. Biểu Đồ 24 Giờ Trải Nghiệm Sinh Thái</h2>
<ul>
  <li><strong>05:30 - 08:00 (Bình Minh Tinh Khôi):</strong> Cụm Sunrise đón những tia nắng ấm đầu tiên chiếu qua mặt nước hồ bảng lảng sương sớm. Không khí se lạnh 21°C, rất lý tưởng để tập Yoga trên bãi cỏ hoặc thưởng thức tách cà phê nóng ngoài hiên. Trong khi đó, cụm Sunset đang chìm trong giấc ngủ êm đềm dưới bóng râm dịu mát.</li>
  <li><strong>11:30 - 14:00 (Trưa Hè Râm Mát):</strong> Mặt trời lên đỉnh đầu, cả hai cụm điền trang đều được làm mát bởi tán cây xanh rợp bóng và hệ thống hồ bơi riêng biệt. Không gian tĩnh lặng, chỉ có tiếng xào xạc của lá dừa và tiếng chim hót.</li>
  <li><strong>16:30 - 18:30 (Hoàng Hôn Tráng Lệ):</strong> Cụm Sunset bước vào "giờ vàng" đẹp nhất. Bầu trời chuyển dần từ vàng cam sang tím thẫm, phản chiếu xuống mặt nước hồ 100ha. Cư dân Sunset quây quần bên ban công tầng 2 ngắm cảnh, trong khi cụm Sunrise đã đón luồng gió mát lành đầu tối.</li>
  <li><strong>19:00 - 22:00 (Đêm Trăng Tĩnh Mịch):</strong> Gió hồ thổi mát rượi, nhiệt độ giảm còn 23°C. Không gian ấm cúng bên bữa tiệc BBQ ngoài trời, tiếng dế kêu rả rích và bầu trời ngập tràn ánh sao.</li>
</ul>

<h2>2. Bảng Đối Sánh Trực Quan Sunrise vs Sunset</h2>
<div style="overflow-x: auto; margin: 25px 0;">
<table style="width: 100%; border-collapse: collapse; font-size: 0.95rem; background: #ffffff; border: 1px solid #e0d5c1; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.05); min-width: 600px;">
  <thead>
    <tr style="background: #fbf9f5; border-bottom: 2px solid #c9a96e; text-align: left;">
      <th style="padding: 14px 16px; color: #8a6d3b; font-weight: 700;">TIÊU CHÍ TRẢI NGHIỆM</th>
      <th style="padding: 14px 16px; color: #8a6d3b; font-weight: 700;">CỤM SUNRISE (1 & 2)</th>
      <th style="padding: 14px 16px; color: #8a6d3b; font-weight: 700;">CỤM SUNSET (1 & 2)</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid #eee;">
      <td style="padding: 14px 16px; font-weight: 700;">Thời khắc đẹp nhất</td>
      <td style="padding: 14px 16px; color: #2e7d32; font-weight: 700;">06:00 - 08:30 Sáng (Đón bình minh)</td>
      <td style="padding: 14px 16px; color: #c9a96e; font-weight: 700;">16:30 - 18:30 Chiều (Ngắm hoàng hôn)</td>
    </tr>
    <tr style="border-bottom: 1px solid #eee; background: #faf9f6;">
      <td style="padding: 14px 16px; font-weight: 700;">Cảm xúc chủ đạo</td>
      <td style="padding: 14px 16px;">Tươi mới, năng động, khởi sinh năng lượng</td>
      <td style="padding: 14px 16px;">Lãng mạn, thư giãn, lắng đọng, sum vầy</td>
    </tr>
    <tr style="border-bottom: 1px solid #eee;">
      <td style="padding: 14px 16px; font-weight: 700;">Bóng râm buổi chiều</td>
      <td style="padding: 14px 16px; color: #0068FF; font-weight: 700;">Mát rượi từ 13:00 chiều trở đi</td>
      <td style="padding: 14px 16px;">Được bảo vệ bởi vườn cây & lam chắn nắng</td>
    </tr>
    <tr>
      <td style="padding: 14px 16px; font-weight: 700;">Phù hợp với thói quen</td>
      <td style="padding: 14px 16px;">Gia chủ thích dậy sớm, tập thiền, thể thao</td>
      <td style="padding: 14px 16px;">Gia chủ thích tiệc tối, thưởng rượu, ngắm cảnh chiều</td>
    </tr>
  </tbody>
</table>
</div>

{CONTACT_BANNER}
"""
    },
    {
        "id": 114,
        "title": "Thủy Khí Hồ 100ha & Không Gian Cây Xanh: Trụ Cột Nuôi Dưỡng Sức Khỏe Gia Chủ Tại Cụm Điền Trang",
        "excerpt": "Phân tích tác động y sinh học của mặt nước hồ 100ha và thảm thực vật nhiệt đới: mật độ ion âm cực đại, cải thiện giấc ngủ sâu, hạ huyết áp và thanh lọc hệ hô hấp cho cư dân Saigon Farm Resort.",
        "image": "assets/Index_asset/Phoi_canh_tong_the/SFR_S01_Final_Fix.jpg",
        "date": "30 TH8 2026",
        "category": "Phong Thủy & Vi Khí Hậu",
        "content": f"""
<p>Khoa học hiện đại đã chứng minh rằng sống gần nguồn nước tự nhiên và không gian cây xanh dày đặc mang lại những chuyển biến kỳ diệu cho sức khỏe thể chất lẫn tinh thần. Tại <strong>Saigon Farm Resort</strong>, hồ nước tự nhiên quy mô hơn <strong>100ha</strong> kết hợp cùng hàng chục nghìn cây xanh cổ thụ tạo nên một "bầu sinh quyển" vô giá cho cả 4 dòng điền trang <strong>Sunrise 1, 2 và Sunset 1, 2</strong>.</p>

<div class="pull-quote">
  "Mỗi mét khối không khí tại Saigon Farm Resort chứa hàm lượng ion âm cao gấp 15 lần so với trung tâm đô thị, giúp trung hòa các gốc tự do và tái sinh tế bào một cách tự nhiên."
</div>

<h2>1. Những Lợi Ích Sức Khỏe Đo Lường Được</h2>
<ul>
  <li><strong>Tăng Cường Chất Lượng Giấc Ngủ:</strong> Độ ẩm lý tưởng từ mặt hồ và hương thơm thảo mộc tự nhiên giúp kích thích não bộ tiết melatonin, đưa gia chủ vào giấc ngủ sâu không mộng mị.</li>
  <li><strong>Cải Thiện Hệ Hô Hấp & Tim Mạch:</strong> Môi trường hoàn toàn không có bụi mịn PM2.5, hàm lượng oxy giàu có giúp hạ nhịp tim, ổn định huyết áp cho người cao tuổi.</li>
  <li><strong>Giảm Căng Thẳng & Trầm Cảm (Hiệu Ứng Blue Mind):</strong> Nghiên cứu từ Đại học Exeter (Anh) chỉ ra rằng việc ngắm nhìn mặt nước gợn sóng mỗi ngày làm giảm 30% hormone cortisol gây căng thẳng thần kinh.</li>
</ul>

<h2>2. Bảng Thống Kê Chỉ Số Môi Trường Tại Quần Thể Điền Trang</h2>
<div style="overflow-x: auto; margin: 25px 0;">
<table style="width: 100%; border-collapse: collapse; font-size: 0.95rem; background: #ffffff; border: 1px solid #e0d5c1; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.05); min-width: 600px;">
  <thead>
    <tr style="background: #fbf9f5; border-bottom: 2px solid #c9a96e; text-align: left;">
      <th style="padding: 14px 16px; color: #8a6d3b; font-weight: 700;">CHỈ SỐ ĐO LƯỜNG</th>
      <th style="padding: 14px 16px; color: #8a6d3b; font-weight: 700;">NỘI THÀNH TP.HCM</th>
      <th style="padding: 14px 16px; color: #8a6d3b; font-weight: 700;">SAIGON FARM RESORT</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid #eee;">
      <td style="padding: 14px 16px; font-weight: 700;">Nồng độ bụi mịn PM2.5</td>
      <td style="padding: 14px 16px; color: #d32f2f;">45 - 80 µg/m³ (Báo động vàng/đỏ)</td>
      <td style="padding: 14px 16px; color: #2e7d32; font-weight: 700;">< 8 µg/m³ (Chuẩn không khí sạch quốc tế)</td>
    </tr>
    <tr style="border-bottom: 1px solid #eee; background: #faf9f6;">
      <td style="padding: 14px 16px; font-weight: 700;">Mật độ Ion âm (Negative Ions)</td>
      <td style="padding: 14px 16px;">100 - 300 ions/cm³</td>
      <td style="padding: 14px 16px; color: #0068FF; font-weight: 700;">3.500 - 5.000 ions/cm³ (Tương đương rừng nguyên sinh)</td>
    </tr>
    <tr>
      <td style="padding: 14px 16px; font-weight: 700;">Mức độ ô nhiễm tiếng ồn</td>
      <td style="padding: 14px 16px; color: #d32f2f;">70 - 85 dB (Gây căng thẳng thần kinh)</td>
      <td style="padding: 14px 16px; color: #2e7d32; font-weight: 700;">< 35 dB (Tĩnh lặng tuyệt đối)</td>
    </tr>
  </tbody>
</table>
</div>

<div class="key-takeaways">
  <h3>Giá Trị Dưỡng Lành Của Thủy Khí Điền Trang</h3>
  <ul>
    <li>Mỗi căn điền trang Sunrise & Sunset là một "bệnh viện sinh thái tại gia", giúp phục hồi thể lực sau những áp lực công việc.</li>
    <li>Không gian lý tưởng để thế hệ ông bà an dưỡng tuổi già và con trẻ lớn lên khỏe mạnh, cứng cáp.</li>
  </ul>
</div>

{CONTACT_BANNER}
"""
    },

    # =========================================================================
    # TRỤC 3: TRẢI NGHIỆM SỐNG, TIỆN ÍCH ĐỘC BẢN & DƯỠNG SINH (4 BÀI)
    # =========================================================================
    {
        "id": 115,
        "title": "Đặc Quyền Hồ Bơi Vô Cực & Vườn Nông Trại Riêng: Chuẩn Sống Xanh Sunrise 1 & Sunset 1",
        "excerpt": "Trải nghiệm đặc quyền 'Resort tại gia' của hai mẫu điền trang 1 tầng Sunrise 1 & Sunset 1: sở hữu bể bơi lọc khoáng muối 45m² và mảnh vườn rau quả hữu cơ tự thu hoạch chuẩn Farm-to-Table.",
        "image": "assets/Index_asset/02_Phoi_Canh_3D/05.3D_TKCS-SUNRISE_1_VILLA/05.3D_TKCS-NHA_GO_4_MAU_1-_07.2025/01._NGOAI_THAT/SFR_NGOAI_THAT_(4).jpg",
        "date": "30 TH8 2026",
        "category": "Trải Nghiệm & Tiện Ích",
        "content": f"""
<p>Sở hữu một căn điền trang vườn 1 tầng tại <strong>Saigon Farm Resort</strong> (gồm <strong>Sunrise 1</strong> và <strong>Sunset 1</strong>) đồng nghĩa với việc gia chủ nắm giữ trọn vẹn hai đặc quyền nghỉ dưỡng đắt giá nhất: <strong>Hồ bơi vô cực riêng tư</strong> và <strong>Mảnh vườn sinh thái hữu cơ</strong> ngay trước hiên nhà.</p>

<div class="pull-quote">
  "Cảm giác tự tay hái những quả cà chua mọng nước, vài nhánh rau thơm tươi xanh ngoài vườn rồi cùng gia đình thưởng thức bên mép hồ bơi là định nghĩa chân thực nhất của sự xa xỉ đích thực."
</div>

<h2>1. Hồ Bơi Khoáng Muối Sinh Thái 45m²</h2>
<p>Mỗi căn Sunrise 1 và Sunset 1 đều được trang bị hồ bơi tràn bờ riêng với công nghệ điện phân muối khoáng tự nhiên, không sử dụng hóa chất clo công nghiệp:</p>
<ul>
  <li>Nước hồ trong vắt, êm dịu cho làn da nhạy cảm của trẻ nhỏ và phụ nữ.</li>
  <li>Khu vực sàn tắm nắng gỗ ngoài trời kết nối trực tiếp với hiên phòng khách, tạo nên không gian thư giãn liền mạch.</li>
  <li>Đèn LED dưới nước tạo hiệu ứng lấp lánh lung linh cho các buổi tối bơi lội dưới bầu trời ngập sao.</li>
</ul>

<h2>2. Vườn Nông Nghiệp Hữu Cơ (Organic Farm) Tại Gia</h2>
<p>Với diện tích sân vườn từ <strong>260m² đến hơn 700m²</strong>, gia chủ được bàn giao sẵn một khu vườn hoàn chỉnh với hệ thống tưới tự động thông minh do đội ngũ kỹ sư nông nghiệp <strong>MDS Living</strong> chăm sóc và vận hành:</p>
<ul>
  <li><strong>Rau củ theo mùa:</strong> Xà lách thủy tinh, cải kale, cà chua bi, mướp hương, ớt chuông.</li>
  <li><strong>Cây ăn trái nhiệt đới:</strong> Xoài, bưởi, vú sữa, ổi, mận sum suê cho trái quanh năm.</li>
  <li><strong>Thảo mộc trị liệu:</strong> Bạc hà, hương thảo, sả, húng quế, gừng sẻ cung cấp tinh dầu thơm ngát xua đuổi côn trùng tự nhiên.</li>
</ul>

<div class="key-takeaways">
  <h3>Chuẩn Sống Farm-to-Table Đích Thực</h3>
  <ul>
    <li>Nguồn thực phẩm sạch, an toàn tuyệt đối ngay tại vườn nhà.</li>
    <li>Con trẻ được thỏa sức lội đất, tưới cây, thu hoạch nông sản để hiểu và yêu thiên nhiên hơn.</li>
  </ul>
</div>

{CONTACT_BANNER}
"""
    },
    {
        "id": 116,
        "title": "Đẳng Cấp Thượng Lưu Tại Dinh Thự Sunrise 2: Không Gian Gala Sân Vườn 1.500m² & Tiếp Khách VIP Kín Đáo",
        "excerpt": "Khám phá không gian tiếp khách ngoại giao và tổ chức tiệc thượng lưu tại Dinh Thự Sunrise 2: khuôn viên vườn 1.500m² sức chứa 80 khách, hồ bơi vô cực 53m², phòng Cigar & Hầm rượu riêng tư tuyệt đối.",
        "image": "assets/Index_asset/02_Phoi_Canh_3D/07.3D_TKCS-NHA_GO_4_MAU_2-_02.2026/07.TKCS-NHA_GO_4-MAU_2/01.NGOAI_THAT/SFR_03.jpg",
        "date": "30 TH8 2026",
        "category": "Trải Nghiệm & Tiện Ích",
        "content": f"""
<p>Đối với giới doanh nhân thành đạt và các gia tộc danh giá, điền trang không chỉ là nơi nghỉ ngơi mà còn là không gian giao lưu ngoại giao, tiếp đón đối tác và gắn kết bạn bè thân hữu. <strong>Dinh Thự Sunrise 2 (1.500m²)</strong> tại <strong>Saigon Farm Resort</strong> được kiến tạo để đáp ứng hoàn hảo những tiêu chuẩn khắt khe nhất của phong cách sống thượng lưu này.</p>

<div class="pull-quote">
  "Một đêm tiệc Gala bên bờ hồ lung linh, tiếng nhạc acoustic du dương, rượu vang hảo hạng và những cuộc trò chuyện tâm giao thân mật – Sunrise 2 là sân khấu hoàn hảo cho những dấu ấn đỉnh cao."
</div>

<h2>1. Khả Năng Tổ Chức Tiệc Sân Vườn Lên Đến 80 Khách</h2>
<p>Với khuôn viên bãi cỏ xanh mướt hơn <strong>1.000m²</strong> nối liền với đại sảnh trần cao 6m, Sunrise 2 dễ dàng biến hóa thành một không gian tiệc ngoài trời tráng lệ:</p>
<ul>
  <li>Khu vực quầy bar ngoài trời và bếp nướng BBQ chuyên nghiệp ven hồ bơi.</li>
  <li>Đội ngũ đầu bếp riêng của <strong>MDS Living</strong> sẵn sàng phục vụ thực đơn Fine Dining 5 sao theo yêu cầu riêng của gia chủ.</li>
  <li>Dịch vụ âm thanh, ánh sáng và quản gia chuẩn quốc tế túc trực chăm sóc từng vị khách.</li>
</ul>

<h2>2. Không Gian Kín Đáo Dành Cho Những Cuộc Đàm Phán Bí Mật</h2>
<p>Sunrise 2 sở hữu hệ thống phòng chức năng biệt lập: Phòng thưởng Cigar, Hầm rượu vang với nhiệt độ tiêu chuẩn quốc tế và Thư phòng doanh nhân cách âm hoàn toàn, đảm bảo sự riêng tư tuyệt đối cho các quyết sách kinh doanh quan trọng.</p>

<div class="key-takeaways">
  <h3>Đặc Quyền Dành Riêng Cho Chủ Nhân Sunrise 2</h3>
  <ul>
    <li>Hệ thống an ninh 3 lớp nghiêm ngặt, đảm bảo tính riêng tư và bảo mật tuyệt đối cho gia chủ và khách mời.</li>
    <li>Dịch vụ hỗ trợ sự kiện trọn gói từ MDS Living: từ cắm hoa nghệ thuật, setup bàn tiệc đến biểu diễn âm nhạc thính phòng.</li>
  </ul>
</div>

{CONTACT_BANNER}
"""
    },
    {
        "id": 117,
        "title": "Phong Cách Sống 'Sunset Lounge': Trải Nghiệm Tiệc Trà Hoàng Hôn & Thưởng Rượu Tầng Thượng Sunset 2",
        "excerpt": "Hòa mình vào văn hóa 'Sunset Lounge' thời thượng tại biệt phủ 2 tầng Sunset 2: nhâm nhi ly cocktail khi hoàng hôn buông xuống, thưởng thức tiệc trà chiều kiểu Anh và ngắm nhìn mặt hồ 100ha chuyển màu kỳ ảo.",
        "image": "assets/Index_asset/02_Phoi_Canh_3D/09.3D_TKCS-SUNSET_VILLA/SUNSET_2_VILLA/SFR_04.PC_02.jpg",
        "date": "30 TH8 2026",
        "category": "Trải Nghiệm & Tiện Ích",
        "content": f"""
<p>Trên thế giới, những điểm ngắm hoàng hôn nổi tiếng như Santorini (Hy Lạp) hay Ibiza (Tây Ban Nha) đã nâng tầm khoảnh khắc chiều tà thành một phong cách sống nghệ thuật mang tên <em>Sunset Ritual</em>. Tại <strong>Saigon Farm Resort</strong>, gia chủ của căn biệt phủ 2 tầng <strong>Điền Trang Sunset 2</strong> có thể tận hưởng trọn vẹn văn hóa <strong>Sunset Lounge</strong> độc bản ngay tại tư gia của mình.</p>

<div class="pull-quote">
  "Khi mặt trời từ từ chạm vào đường chân trời trên mặt hồ 100ha, rót một ly Pinot Noir và thả mình trên ghế êm tầng thượng – đó là giây phút mọi giác quan được thăng hoa."
</div>

<h2>1. Thiết Kế Ban Công Sky Lounge 35m² Độc Đáo</h2>
<p>Ban công tầng 2 của Sunset 2 được kiến tạo như một quầy lounge ngoài trời sang trọng:</p>
<ul>
  <li>Lan can kính cường lực không viền mở rộng tầm nhìn vô cực ra mặt hồ và đồng lúa.</li>
  <li>Bố trí sofa ngoài trời chống chịu thời tiết, bàn trà gỗ lũa tự nhiên và hệ thống đèn hắt ánh sáng vàng ấm cúng.</li>
  <li>Kết nối trực tiếp với quầy Mini Bar và tủ ướp rượu vang trong phòng sinh hoạt chung lầu 1.</li>
</ul>

<h2>2. Nghi Thức Thưởng Trà Chiều & Rượu Vang Hoàng Hôn</h2>
<p>Từ 16:30 đến 18:30 hàng ngày, không gian này trở thành nơi sum họp lý tưởng nhất: các quý cô thưởng thức trà sen hảo hạng cùng bánh ngọt hữu cơ, trong khi các quý ông đàm đạo bên ly rượu vang trong tiếng nhạc êm dịu.</p>

<div class="key-takeaways">
  <h3>Trải Nghiệm Thượng Lưu Tại Sunset 2</h3>
  <ul>
    <li>Góc check-in và chụp ảnh hoàng hôn đẹp bậc nhất toàn vùng duyên hải Hồ Tràm - Đất Đỏ.</li>
    <li>Không gian tái tạo cảm xúc mạnh mẽ, khơi nguồn cảm hứng sáng tạo cho giới nghệ thuật và doanh nhân.</li>
  </ul>
</div>

{CONTACT_BANNER}
"""
    },
    {
        "id": 118,
        "title": "Lối Sống Chữa Lành & Dưỡng Sinh Thân - Tâm - Trí: Một Ngày Hoàn Hảo Tại Điền Trang Saigon Farm Resort",
        "excerpt": "Lịch trình một ngày dưỡng sinh trọn vẹn của cư dân Sunrise & Sunset: từ thiền định đón bình minh, chèo SUP mặt hồ, ngâm Onsen thảo dược Bờ Sen đến thưởng thức ẩm thực thực dưỡng Farm-to-Table.",
        "image": "assets/Index_asset/Tien_ich_minh_hoa/Bo_sen.png",
        "date": "30 TH8 2026",
        "category": "Trải Nghiệm & Tiện Ích",
        "content": f"""
<p>Trong bối cảnh áp lực cuộc sống đô thị ngày càng gia tăng, nhu cầu tìm kiếm một ngôi nhà thứ hai (Second Home) để chữa lành và chăm sóc sức khỏe toàn diện (Wellness Living) đã trở thành xu hướng tất yếu. Tại <strong>Saigon Farm Resort</strong>, cư dân của 4 mẫu điền trang <strong>Sunrise 1, 2 và Sunset 1, 2</strong> được thụ hưởng một hành trình dưỡng sinh <strong>Thân - Tâm - Trí</strong> chuẩn mực suốt 24 giờ.</p>

<div class="pull-quote">
  "Dưỡng sinh không phải là một liệu trình ngắn hạn, mà là một lối sống gắn bó mật thiết với thiên nhiên, thực phẩm thuần khiết và sự an nhiên trong từng hơi thở."
</div>

<h2>1. Hành Trình Một Ngày Dưỡng Sinh Mẫu Của Cư Dân</h2>
<div style="overflow-x: auto; margin: 25px 0;">
<table style="width: 100%; border-collapse: collapse; font-size: 0.95rem; background: #ffffff; border: 1px solid #e0d5c1; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.05); min-width: 600px;">
  <thead>
    <tr style="background: #fbf9f5; border-bottom: 2px solid #c9a96e; text-align: left;">
      <th style="padding: 14px 16px; color: #8a6d3b; font-weight: 700;">KHUNG GIỜ</th>
      <th style="padding: 14px 16px; color: #8a6d3b; font-weight: 700;">HOẠT ĐỘNG DƯỠNG SINH</th>
      <th style="padding: 14px 16px; color: #8a6d3b; font-weight: 700;">TÁC ĐỘNG SỨC KHỎE</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid #eee;">
      <td style="padding: 14px 16px; font-weight: 700;">06:00 - 07:00</td>
      <td style="padding: 14px 16px;">Tập Yoga / Thiền đón bình minh trên thảm cỏ hướng hồ</td>
      <td style="padding: 14px 16px;">Kích hoạt luân xa, nạp năng lượng dương, thanh lọc phổi</td>
    </tr>
    <tr style="border-bottom: 1px solid #eee; background: #faf9f6;">
      <td style="padding: 14px 16px; font-weight: 700;">07:30 - 08:30</td>
      <td style="padding: 14px 16px;">Bữa sáng thực dưỡng Farm-to-Table tại nhà hàng Nếp Nhà Việt</td>
      <td style="padding: 14px 16px;">Bổ sung enzym tươi, cân bằng hệ vi sinh đường ruột</td>
    </tr>
    <tr style="border-bottom: 1px solid #eee;">
      <td style="padding: 14px 16px; font-weight: 700;">09:00 - 11:00</td>
      <td style="padding: 14px 16px;">Cưỡi ngựa tại Việt Mã Trang / Chèo Kayak mặt hồ 100ha</td>
      <td style="padding: 14px 16px;">Rèn luyện cơ lõi, thăng bằng và sức bền tim mạch</td>
    </tr>
    <tr style="border-bottom: 1px solid #eee; background: #faf9f6;">
      <td style="padding: 14px 16px; font-weight: 700;">14:30 - 16:30</td>
      <td style="padding: 14px 16px;">Ngâm khoáng thảo mộc & Massage trị liệu tại Bờ Sen Spa</td>
      <td style="padding: 14px 16px;">Thư giãn sâu cơ bắp, đào thải độc tố qua da, giảm đau nhức</td>
    </tr>
    <tr>
      <td style="padding: 14px 16px; font-weight: 700;">20:30 - 21:30</td>
      <td style="padding: 14px 16px;">Thưởng trà Việt cổ thụ, đọc sách và thiền tĩnh lặng tại tư gia</td>
      <td style="padding: 14px 16px;">Làm dịu hệ thần kinh trung ương, chuẩn bị cho giấc ngủ sâu</td>
    </tr>
  </tbody>
</table>
</div>

<div class="key-takeaways">
  <h3>Hệ Sinh Thái Chăm Sóc Sức Khỏe Đa Tầng Gần 3ha</h3>
  <ul>
    <li>MDS Living cung cấp chuyên gia dinh dưỡng và huấn luyện viên sức khỏe cá nhân theo yêu cầu.</li>
    <li>Nguồn thảo dược tự nhiên được thu hái trực tiếp từ vườn dược liệu sinh thái của khu điền trang.</li>
  </ul>
</div>

{CONTACT_BANNER}
"""
    },

    # =========================================================================
    # TRỤC 4: SUẤT ĐẦU TƯ, HIỆU QUẢ KHAI THÁC & TÍCH SẢN BỀN VỮNG (4 BÀI)
    # =========================================================================
    {
        "id": 119,
        "title": "Bài Toán Dòng Tiền & Suất Đầu Tư Cho Thuê Mẫu 3PN: So Sánh Cơ Hội Giữa Sunrise 1 và Sunset 1",
        "excerpt": "Phân tích tài chính chi tiết cho hai mẫu điền trang 3 phòng ngủ 1 tầng: cơ cấu vốn đầu tư, chi phí vận hành qua MDS Living, công suất phòng kỳ vọng và tỷ suất sinh lời dòng tiền (Cash-on-Cash Return).",
        "image": "assets/Index_asset/02_Phoi_Canh_3D/09.3D_TKCS-SUNSET_VILLA/SUNSET_1_VILLA/SFR_04.PC_01.jpg",
        "date": "30 TH8 2026",
        "category": "Đầu Tư & Tích Sản",
        "content": f"""
<p>Phân khúc điền trang sinh thái 3 phòng ngủ 1 tầng (gồm <strong>Sunrise 1</strong> và <strong>Sunset 1</strong>) là dòng sản phẩm có tính thanh khoản cao nhất và dễ dàng khai thác cho thuê nghỉ dưỡng gia đình tại <strong>Saigon Farm Resort</strong>. Dưới đây là bài toán phân tích dòng tiền và hiệu quả tài chính chi tiết dành cho nhà đầu tư.</p>

<div class="pull-quote">
  "Mẫu điền trang 3PN 1 tầng đạt hiệu suất khai thác cao nhất nhờ phù hợp với 85% nhu cầu thuê nghỉ dưỡng của các gia đình đa thế hệ từ TP.HCM và chuyên gia nước ngoài."
</div>

<h2>1. Mô Hình Vận Hành Cho Thuê Ủy Thác Qua MDS Living</h2>
<p>Chủ sở hữu có thể linh hoạt sử dụng để nghỉ dưỡng kết hợp ủy thác cho đơn vị quản lý chuyên nghiệp <strong>MDS Living</strong> khai thác cho thuê trong những ngày không sử dụng, với tỷ lệ chia sẻ doanh thu minh bạch và hệ thống quản lý phòng thời gian thực qua ứng dụng di động.</p>

<h2>2. Bảng Phân Tích Dòng Tiền Dự Phóng Hàng Năm</h2>
<div style="overflow-x: auto; margin: 25px 0;">
<table style="width: 100%; border-collapse: collapse; font-size: 0.95rem; background: #ffffff; border: 1px solid #e0d5c1; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.05); min-width: 600px;">
  <thead>
    <tr style="background: #fbf9f5; border-bottom: 2px solid #c9a96e; text-align: left;">
      <th style="padding: 14px 16px; color: #8a6d3b; font-weight: 700;">CHỈ SỐ TÀI CHÍNH</th>
      <th style="padding: 14px 16px; color: #8a6d3b; font-weight: 700;">ĐIỀN TRANG SUNRISE 1</th>
      <th style="padding: 14px 16px; color: #8a6d3b; font-weight: 700;">ĐIỀN TRANG SUNSET 1</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid #eee;">
      <td style="padding: 14px 16px; font-weight: 700;">Giá thuê bình quân ngày thường</td>
      <td style="padding: 14px 16px;">6.500.000 VNĐ / đêm</td>
      <td style="padding: 14px 16px;">6.500.000 VNĐ / đêm</td>
    </tr>
    <tr style="border-bottom: 1px solid #eee; background: #faf9f6;">
      <td style="padding: 14px 16px; font-weight: 700;">Giá thuê cuối tuần & Lễ tết</td>
      <td style="padding: 14px 16px;">9.500.000 VNĐ / đêm</td>
      <td style="padding: 14px 16px;">10.000.000 VNĐ / đêm (Lợi thế view hoàng hôn)</td>
    </tr>
    <tr style="border-bottom: 1px solid #eee;">
      <td style="padding: 14px 16px; font-weight: 700;">Công suất phòng bình quân (ADR)</td>
      <td style="padding: 14px 16px; color: #2e7d32; font-weight:700;">55% - 62% / năm</td>
      <td style="padding: 14px 16px; color: #2e7d32; font-weight:700;">58% - 65% / năm</td>
    </tr>
    <tr style="border-bottom: 1px solid #eee; background: #faf9f6;">
      <td style="padding: 14px 16px; font-weight: 700;">Doanh thu gộp ước tính / năm</td>
      <td style="padding: 14px 16px;">~ 1.450.000.000 VNĐ</td>
      <td style="padding: 14px 16px;">~ 1.550.000.000 VNĐ</td>
    </tr>
    <tr style="border-bottom: 1px solid #eee;">
      <td style="padding: 14px 16px; font-weight: 700;">Chi phí vận hành & Quản lý (35%)</td>
      <td style="padding: 14px 16px;">~ 507.000.000 VNĐ</td>
      <td style="padding: 14px 16px;">~ 542.000.000 VNĐ</td>
    </tr>
    <tr>
      <td style="padding: 14px 16px; font-weight: 700;">Lợi nhuận ròng thu về cho chủ nhà</td>
      <td style="padding: 14px 16px; color: #0068FF; font-weight: 700;">~ 943.000.000 VNĐ / năm</td>
      <td style="padding: 14px 16px; color: #0068FF; font-weight: 700;">~ 1.008.000.000 VNĐ / năm</td>
    </tr>
  </tbody>
</table>
</div>

<div class="key-takeaways">
  <h3>Đánh Giá Hiệu Quả Đầu Tư</h3>
  <ul>
    <li>Tỷ suất sinh lời dòng tiền ước tính đạt <strong>8.5% - 10.2%/năm</strong>, cao hơn đáng kể so với gửi tiết kiệm ngân hàng hoặc cho thuê chung cư đô thị.</li>
    <li>Giá trị đất gia tăng kép nhờ vị trí hưởng lợi trực tiếp từ Sân bay Quốc tế Long Thành (hoạt động 2026) và Cao tốc Biên Hòa - Vũng Tàu.</li>
  </ul>
</div>

{CONTACT_BANNER}
"""
    },
    {
        "id": 130,
        "title": "Dinh Thự Sunrise 2 - Bất Động Sản Di Sản 1.500m²: Tính Khan Hiếm & Tiềm Năng Tăng Trưởng Bền Vững",
        "excerpt": "Đánh giá giá trị quỹ đất lớn 1.500m² ven hồ sinh thái 100ha: tính khan hiếm không thể sao chép, khả năng chống lạm phát tuyệt đối và tiềm năng tăng trưởng vốn bền vững theo chu kỳ kinh tế.",
        "image": "assets/Index_asset/02_Phoi_Canh_3D/07.3D_TKCS-NHA_GO_4_MAU_2-_02.2026/07.TKCS-NHA_GO_4-MAU_2/01.NGOAI_THAT/SFR_04.jpg",
        "date": "30 TH8 2026",
        "category": "Đầu Tư & Tích Sản",
        "content": f"""
<p>Trong danh mục đầu tư của giới siêu giàu (UHNWI), các bất động sản sở hữu diện tích đất lớn ven mặt nước tự nhiên luôn được xem là lớp tài sản phòng thủ vững chắc nhất trước lạm phát và suy thoái kinh tế. <strong>Dinh Thự Sunrise 2 (1.500m²)</strong> tại <strong>Saigon Farm Resort</strong> chính là hình mẫu tiêu biểu của dòng tài sản di sản này.</p>

<div class="pull-quote">
  "Đất đai ven hồ tự nhiên 100ha là hữu hạn và không thể tạo thêm. Sở hữu một khuôn viên 1.500m² ngày hôm nay là nắm giữ một di sản vô giá cho các thế hệ mai sau."
</div>

<h2>1. Tính Khan Hiếm & Luật Quy Hoạch Mới</h2>
<p>Với các quy định ngày càng khắt khe về việc chuyển mục đích sử dụng đất và phân lô diện tích lớn, việc tìm kiếm một khu đất rộng <strong>1.500m²</strong> có quy hoạch nghỉ dưỡng bài bản, tiếp giáp hồ tự nhiên lớn và chỉ cách TP.HCM chưa đầy 1 giờ di chuyển gần như là bất khả thi trong tương lai.</p>

<h2>2. Bảng Phân Tích Giá Trị Tích Sản Sunrise 2</h2>
<div style="overflow-x: auto; margin: 25px 0;">
<table style="width: 100%; border-collapse: collapse; font-size: 0.95rem; background: #ffffff; border: 1px solid #e0d5c1; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.05); min-width: 600px;">
  <thead>
    <tr style="background: #fbf9f5; border-bottom: 2px solid #c9a96e; text-align: left;">
      <th style="padding: 14px 16px; color: #8a6d3b; font-weight: 700;">GÓC ĐỘ PHÂN TÍCH</th>
      <th style="padding: 14px 16px; color: #8a6d3b; font-weight: 700;">ĐẶC ĐIỂM NỔI BẬT</th>
      <th style="padding: 14px 16px; color: #8a6d3b; font-weight: 700;">TÁC ĐỘNG TÀI CHÍNH</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid #eee;">
      <td style="padding: 14px 16px; font-weight: 700;">Quy mô đất 1.500m²</td>
      <td style="padding: 14px 16px;">Tỷ lệ đất ở chiếm đa số, mật độ xây dựng thấp</td>
      <td style="padding: 14px 16px; color: #2e7d32; font-weight: 700;">Giá trị thặng dư đất tăng trưởng lũy tiến theo thời gian</td>
    </tr>
    <tr style="border-bottom: 1px solid #eee; background: #faf9f6;">
      <td style="padding: 14px 16px; font-weight: 700;">Vị trí mặt tiền hồ 100ha</td>
      <td style="padding: 14px 16px;">Không bị chắn tầm nhìn vĩnh viễn</td>
      <td style="padding: 14px 16px;">Thanh khoản cao trong phân khúc dinh thự độc bản</td>
    </tr>
    <tr style="border-bottom: 1px solid #eee;">
      <td style="padding: 14px 16px; font-weight: 700;">Hạ tầng bứt phá 2026</td>
      <td style="padding: 14px 16px;">Sân bay Long Thành & Cao tốc Biên Hòa - Vũng Tàu</td>
      <td style="padding: 14px 16px; color: #0068FF; font-weight: 700;">Đòn bẩy tăng giá tài sản từ 25% - 40% trong chu kỳ 3 năm</td>
    </tr>
    <tr>
      <td style="padding: 14px 16px; font-weight: 700;">Công năng linh hoạt</td>
      <td style="padding: 14px 16px;">Vừa ở, vừa tiếp khách VIP, vừa ủy thác MDS Living</td>
      <td style="padding: 14px 16px;">Tạo dòng tiền thụ động ổn định hàng trăm triệu mỗi tháng</td>
    </tr>
  </tbody>
</table>
</div>

<div class="key-takeaways">
  <h3>Khuyến Nghị Dành Cho Nhà Đầu Tư Lớn</h3>
  <ul>
    <li>Sunrise 2 là lựa chọn lý tưởng cho các gia đình muốn tích lũy tài sản thực có pháp lý minh bạch.</li>
    <li>Bất động sản không bị ảnh hưởng bởi biến động ngắn hạn của thị trường tài chính.</li>
  </ul>
</div>

{CONTACT_BANNER}
"""
    },
    {
        "id": 131,
        "title": "Tiềm Năng Khai Thác Lưu Trú Cao Cấp Của Điền Trang Sunset 2: Sức Hút Với Khách Du Lịch Quốc Tế & Chuyên Gia Long Thành",
        "excerpt": "Phân tích tệp khách hàng tiềm năng thuê điền trang 2 tầng Sunset 2: chuyên gia cấp cao sân bay quốc tế Long Thành, gia đình doanh nhân đa thế hệ và xu hướng 'Workcation' nghỉ dưỡng kết hợp làm việc từ xa.",
        "image": "assets/Index_asset/02_Phoi_Canh_3D/09.3D_TKCS-SUNSET_VILLA/SUNSET_2_VILLA/SFR_04.PC_03.jpg",
        "date": "30 TH8 2026",
        "category": "Đầu Tư & Tích Sản",
        "content": f"""
<p>Điền trang 2 tầng <strong>Sunset 2</strong> sở hữu những ưu thế vượt trội về mặt không gian và kiến trúc để trở thành "ngôi sao" trên các nền tảng đặt phòng cao cấp như Airbnb Luxe hay hệ thống vận hành quốc tế của <strong>MDS Living</strong>. Bài viết này phân tích sâu nguồn cầu lưu trú cao cấp từ khu vực phụ cận.</p>

<div class="pull-quote">
  "Khoảng cách 25 phút đến Sân bay Long Thành biến Sunset 2 thành điểm dừng chân nghỉ dưỡng số 1 cho các chuyên gia hàng không, phi công quốc tế và giới quản lý cấp cao."
</div>

<h2>1. Ba Động Lực Tạo Nguồn Cầu Thuê Khổng Lồ</h2>
<ul>
  <li><strong>Làn sóng chuyên gia Sân bay Long Thành & KCN Đất Đỏ:</strong> Hàng nghìn chuyên gia nước ngoài và lãnh đạo cấp cao có nhu cầu thuê lưu trú dài hạn hoặc nghỉ dưỡng cuối tuần trong không gian sinh thái biệt lập đẳng cấp.</li>
  <li><strong>Xu hướng du lịch Staycation & Workcation:</strong> Giới trí thức và chủ doanh nghiệp tại TP.HCM chỉ mất 55 phút lái xe để đến làm việc từ xa giữa thiên nhiên với đầy đủ tiện ích internet tốc độ cao và không gian yên tĩnh.</li>
  <li><strong>Khách du lịch gia đình cao cấp:</strong> Thiết kế 2 tầng với 3 phòng ngủ khép kín và ban công Sunset Lounge đáp ứng hoàn hảo nhu cầu sum họp gia đình 6 - 8 người.</li>
</ul>

<h2>2. Bảng Dự Phóng Giá Trị Khai Thác Sunset 2</h2>
<div style="overflow-x: auto; margin: 25px 0;">
<table style="width: 100%; border-collapse: collapse; font-size: 0.95rem; background: #ffffff; border: 1px solid #e0d5c1; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.05); min-width: 600px;">
  <thead>
    <tr style="background: #fbf9f5; border-bottom: 2px solid #c9a96e; text-align: left;">
      <th style="padding: 14px 16px; color: #8a6d3b; font-weight: 700;">HÌNH THỨC CHO THUÊ</th>
      <th style="padding: 14px 16px; color: #8a6d3b; font-weight: 700;">MỨC GIÁ DỰ KIẾN</th>
      <th style="padding: 14px 16px; color: #8a6d3b; font-weight: 700;">TỶ LỆ LẤP ĐẦY KỲ VỌNG</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid #eee;">
      <td style="padding: 14px 16px; font-weight: 700;">Thuê nghỉ dưỡng ngắn ngày (Daily)</td>
      <td style="padding: 14px 16px; color: #0068FF; font-weight: 700;">8.000.000 - 12.000.000 VNĐ / đêm</td>
      <td style="padding: 14px 16px;">60% - 68% / năm</td>
    </tr>
    <tr style="border-bottom: 1px solid #eee; background: #faf9f6;">
      <td style="padding: 14px 16px; font-weight: 700;">Thuê chuyên gia theo tháng (Monthly)</td>
      <td style="padding: 14px 16px; color: #2e7d32; font-weight: 700;">75.000.000 - 90.000.000 VNĐ / tháng</td>
      <td style="padding: 14px 16px;">Ký hợp đồng dài hạn từ 6 - 12 tháng</td>
    </tr>
    <tr>
      <td style="padding: 14px 16px; font-weight: 700;">Doanh thu ròng ước tính</td>
      <td style="padding: 14px 16px; font-weight: 700;" colspan="2">> 1.100.000.000 VNĐ / năm (sau khi trừ chi phí vận hành)</td>
    </tr>
  </tbody>
</table>
</div>

<div class="key-takeaways">
  <h3>Lợi Thế Cạnh Tranh Vượt Trội Của Sunset 2</h3>
  <ul>
    <li>Kiến trúc 2 tầng bề thế tạo cảm giác nghỉ dưỡng tại một điền trang 5 sao thu nhỏ.</li>
    <li>Khu vườn ăn trái 482m² và ban công hoàng hôn là điểm cộng độc nhất vô nhị khó tìm thấy ở các khu vực lân cận.</li>
  </ul>
</div>

{CONTACT_BANNER}
"""
    },
    {
        "id": 132,
        "title": "Ma Trận Đối Sánh Toàn Diện 4 Mẫu Điền Trang (Sunrise 1, 2 & Sunset 1, 2): Cẩm Nang Chọn Mẫu Căn Cho Nhà Đầu Tư",
        "excerpt": "Bảng tổng hợp đối chiếu toàn diện 4 mẫu điền trang mở bán tại Saigon Farm Resort theo 12 tiêu chí chuyên sâu: giúp gia chủ và nhà đầu tư chọn lựa chính xác căn điền trang phù hợp với nhu cầu và phong cách sống.",
        "image": "assets/Index_asset/Phoicanh/S04_Final_Fix.jpg",
        "date": "30 TH8 2026",
        "category": "Đầu Tư & Tích Sản",
        "content": f"""
<p>Để giúp quý khách hàng và nhà đầu tư dễ dàng đưa ra quyết định chọn lựa căn điền trang hoàn hảo nhất tại <strong>Saigon Farm Resort</strong>, Đại Chúng Properties tổng hợp <strong>Ma Trận So Sánh Toàn Diện</strong> giữa 4 mẫu điền trang mở bán: <strong>Sunrise 1, Dinh Thự Sunrise 2, Sunset 1 và Sunset 2</strong>.</p>

<div class="pull-quote">
  "Mỗi mẫu điền trang tại Saigon Farm Resort là một mảnh ghép kiến trúc độc bản. Không có căn nhà tốt nhất, chỉ có căn nhà phù hợp nhất với triết lý sống và kỳ vọng của bạn."
</div>

<h2>BẢNG MA TRẬN ĐỐI SÁNH CHI TIẾT 4 MẪU ĐIỀN TRANG</h2>
<div style="overflow-x: auto; margin: 25px 0;">
<table style="width: 100%; border-collapse: collapse; font-size: 0.9rem; background: #ffffff; border: 1px solid #e0d5c1; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.05); min-width: 800px;">
  <thead>
    <tr style="background: #fbf9f5; border-bottom: 2px solid #c9a96e; text-align: left;">
      <th style="padding: 12px 14px; color: #8a6d3b; font-weight: 700;">TIÊU CHÍ SO SÁNH</th>
      <th style="padding: 12px 14px; color: #8a6d3b; font-weight: 700;">SUNRISE 1</th>
      <th style="padding: 12px 14px; color: #8a6d3b; font-weight: 700;">SUNRISE 2 (DINH THỰ)</th>
      <th style="padding: 12px 14px; color: #8a6d3b; font-weight: 700;">SUNSET 1</th>
      <th style="padding: 12px 14px; color: #8a6d3b; font-weight: 700;">SUNSET 2</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid #eee;">
      <td style="padding: 12px 14px; font-weight: 700;">Diện tích đất</td>
      <td style="padding: 12px 14px;">1.000m² - 1.200m²</td>
      <td style="padding: 12px 14px; color: #d32f2f; font-weight:700;">1.500m² (Lớn nhất)</td>
      <td style="padding: 12px 14px;">~1.000m²</td>
      <td style="padding: 12px 14px;">1.200m²</td>
    </tr>
    <tr style="border-bottom: 1px solid #eee; background: #faf9f6;">
      <td style="padding: 12px 14px; font-weight: 700;">Số tầng & Phòng ngủ</td>
      <td style="padding: 12px 14px;">1 Tầng • 3 Phòng ngủ</td>
      <td style="padding: 12px 14px;">1 Tầng trần cao 6m • 4PN VIP</td>
      <td style="padding: 12px 14px;">1 Tầng • 3 Phòng ngủ</td>
      <td style="padding: 12px 14px; color: #2e7d32; font-weight:700;">2 Tầng • 3 Phòng ngủ</td>
    </tr>
    <tr style="border-bottom: 1px solid #eee;">
      <td style="padding: 12px 14px; font-weight: 700;">Hướng chính & Tầm nhìn</td>
      <td style="padding: 12px 14px;">Đông (Đón bình minh)</td>
      <td style="padding: 12px 14px;">Đông Nam (Mặt hồ VIP)</td>
      <td style="padding: 12px 14px;">Tây (Sân trong & Hoàng hôn)</td>
      <td style="padding: 12px 14px;">Tây (Panorama ngắm hoàng hôn)</td>
    </tr>
    <tr style="border-bottom: 1px solid #eee; background: #faf9f6;">
      <td style="padding: 12px 14px; font-weight: 700;">Hồ bơi riêng</td>
      <td style="padding: 12px 14px;">45m²</td>
      <td style="padding: 12px 14px; color: #0068FF; font-weight:700;">53m² Vô cực tràn viền</td>
      <td style="padding: 12px 14px;">45m²</td>
      <td style="padding: 12px 14px;">48m²</td>
    </tr>
    <tr style="border-bottom: 1px solid #eee;">
      <td style="padding: 12px 14px; font-weight: 700;">Điểm nhấn kiến trúc</td>
      <td style="padding: 12px 14px;">Layout phẳng trải rộng mở</td>
      <td style="padding: 12px 14px;">Đại sảnh gỗ quý, Sky Deck 40m²</td>
      <td style="padding: 12px 14px;">Sân trong Courtyard giếng trời</td>
      <td style="padding: 12px 14px;">Ban công Sky Lounge lầu 1</td>
    </tr>
    <tr style="border-bottom: 1px solid #eee; background: #faf9f6;">
      <td style="padding: 12px 14px; font-weight: 700;">Vườn cây ăn trái hữu cơ</td>
      <td style="padding: 12px 14px;">Vườn hoa thảo mộc</td>
      <td style="padding: 12px 14px;">Vườn cảnh quan & Bãi cỏ Gala</td>
      <td style="padding: 12px 14px;">260m² Vườn ăn trái</td>
      <td style="padding: 12px 14px; color: #2e7d32; font-weight:700;">482m² Vườn ăn trái trù phú</td>
    </tr>
    <tr>
      <td style="padding: 12px 14px; font-weight: 700;">Khuyến nghị đối tượng</td>
      <td style="padding: 12px 14px;">Gia đình thích an yên, người già & trẻ nhỏ</td>
      <td style="padding: 12px 14px; font-weight:700; color:#8a6d3b;">Doanh nhân, gia tộc, tiếp khách VIP</td>
      <td style="padding: 12px 14px;">Gia đình trẻ, thích không gian kín đáo</td>
      <td style="padding: 12px 14px;">Khách yêu thích tiệc tối & view hoàng hôn</td>
    </tr>
  </tbody>
</table>
</div>

<div class="key-takeaways">
  <h3>Tóm Tắt Khuyến Nghị Chọn Căn</h3>
  <ul>
    <li><strong>Sunrise 1:</strong> Lựa chọn an toàn, chuẩn mực cho gia đình đa thế hệ, tối ưu chi phí đầu tư.</li>
    <li><strong>Sunrise 2:</strong> Dinh thự khẳng định đẳng cấp tột bậc, giá trị truyền đời không thể thay thế.</li>
    <li><strong>Sunset 1:</strong> Điền trang sinh thái sân trong tĩnh lặng, bảo vệ gia đình trong không gian xanh mát.</li>
    <li><strong>Sunset 2:</strong> Căn nhà nghỉ dưỡng 2 tầng thời thượng, tiềm năng khai thác cho thuê cao cấp dẫn đầu.</li>
  </ul>
</div>

{CONTACT_BANNER}
"""
    }
]

all_posts = other_posts + new_estate_posts

with open('data/posts.json', 'w', encoding='utf-8') as f:
    json.dump(all_posts, f, ensure_ascii=False, indent=2)

print(f"Successfully generated {len(all_posts)} posts with updated estate terminology into data/posts.json.")
