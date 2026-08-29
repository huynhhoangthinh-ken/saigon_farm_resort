# -*- coding: utf-8 -*-
import json

contact_box = """
<div style="background: #111; color: #fff; padding: 28px; border-radius: 8px; border-left: 4px solid #c9a96e; margin-top: 30px;">
  <h4 style="margin-bottom: 8px; font-family: var(--font-serif); font-size: 1.25rem; color: #c9a96e;">TỔNG ĐẠI LÝ TIẾP THỊ & PHÂN PHỐI: ĐẠI CHÚNG PROPERTIES</h4>
  <p style="margin-bottom: 6px; font-size: 0.95rem;">👤 <strong>Đại diện tư vấn:</strong> CEO Huỳnh Hoàng Thịnh (Ken)</p>
  <p style="margin-bottom: 14px; font-size: 0.95rem;">📞 <strong>Hotline / Zalo:</strong> <a href="https://zalo.me/0906060036" target="_blank" style="color:#0068FF; font-weight:700; text-decoration:underline;">0906060036</a></p>
  <a href="https://zalo.me/0906060036" target="_blank" style="display: inline-flex; align-items: center; gap: 8px; background: #0068FF; color: #fff; padding: 12px 24px; border-radius: 4px; font-weight: 700; text-decoration: none;">
    <i class="fa-solid fa-comment-dots"></i> Nhắn Zalo Đặt Lịch Trải Nghiệm Thực Tế
  </a>
</div>
"""

posts = [
    # 0. Editorial: Xa Xỉ Đến Từ Bản Sắc (ID 203)
    {
        "id": 203,
        "title": "Xa Xỉ Đến Từ Bản Sắc: Khi Sự Sang Trọng Của Người Việt Là Trở Về Với Những Điều Thuộc Về Mình",
        "excerpt": "Không nhất thiết phải mang hình hài Tuscany hay Kyoto, sự xa xỉ đích thực của người Việt đương đại là một điền trang có mái hiên, bờ sen, đồng lúa và những ký ức gia đình vô giá.",
        "image": "assets/Index_asset/02_Phoi_Canh_3D/08._TKSP-CANH_QUAN_VEN_RUONG-20260515T044351Z-3-001/SFR_1.png",
        "date": "29 TH8 2026",
        "content": f"""
<p>Một người bạn của tôi, sau hơn hai mươi năm sống và làm việc tại nước ngoài, trở về Việt Nam và tìm mua một bất động sản để cả gia đình có thể về nghỉ ngơi thường xuyên. Anh đi xem khá nhiều khu biệt thự cao cấp quanh TP.HCM và các vùng lân cận.</p>

<p>Nhà rất đẹp. Vật liệu rất tốt. Tiện ích cũng đầy đủ. Nhưng anh vẫn cảm thấy thiếu một khoảng thở, thiếu một khu vườn đủ rộng và tổng thể có phần quá “Tây”. Thứ anh hình dung lại rất quen thuộc với nhiều người Việt: <em>một ngôi nhà vườn có mái hiên, một bàn trà, khoảng sân rộng để con cháu chạy chơi, nhiều cây xanh, và nếu có thêm một cánh đồng hay một hồ nước thì càng tốt.</em></p>

<div class="pull-quote">
  "Thế giới đến Việt Nam để nhìn thấy Việt Nam. Người Việt, sau khi đã đi rất xa, cũng có thể muốn trở về với những điều thuộc về mình."
</div>

<h2>Tái Định Nghĩa Sự Xa Xỉ</h2>
<p>Trong ngành khách sạn cao cấp, một sự dịch chuyển tương tự đã diễn ra từ nhiều năm nay. Một chiếc giường thật tốt, một bữa ăn tinh tế, spa hoàn chỉnh hay tiêu chuẩn phục vụ quốc tế có thể được tìm thấy tại rất nhiều điểm đến trên thế giới. Nhưng một khu nghỉ dưỡng khiến người ta nhớ mãi thường là nơi lưu giữ được tinh thần của vùng đất mà nó thuộc về.</p>
<p>Khách hàng cao cấp ngày nay quan tâm nhiều hơn đến những trải nghiệm có bản sắc, những câu chuyện chân thực và mối liên hệ với con người địa phương. Bất động sản cao cấp cũng đang đứng trước một câu hỏi tương tự:</p>
<p>Một ngôi nhà Việt Nam hoàn toàn có thể sử dụng đá Ý, thiết bị Đức, công nghệ Nhật và những tiêu chuẩn thiết kế, vận hành tốt nhất của thế giới. Tiếp nhận tinh hoa quốc tế là điều bình thường. Nhưng một căn nhà ở Việt Nam không nhất thiết phải mang hình hài Tuscany, Kyoto hay một vùng ngoại ô châu Âu để được xem là sang trọng. <strong>Chúng ta đã có những chất liệu của riêng mình.</strong></p>

<h2>Những Điều Từng Rất Bình Thường</h2>
<p>Một mái hiên rộng với chiếc bàn trà. Một khu vườn đủ lớn để ông bà trồng những loại cây mình thích. Khoảng sân để trẻ nhỏ chạy chơi. Một hồ sen, những hàng dừa và cánh đồng lúa chuyển màu theo mùa. Buổi sáng nghe tiếng chim ngoài vườn, chiều nhìn con trẻ chơi trên cỏ, tối cả gia đình ngồi lại quanh một bàn ăn.</p>
<p>Với thế hệ lớn lên cách đây vài chục năm, những hình ảnh ấy từng là một phần khá bình thường của cuộc sống. Nhưng với một đứa trẻ lớn lên giữa đô thị hôm nay, đó có thể là một trải nghiệm hoàn toàn khác.</p>
<p>Nhiều gia đình vẫn muốn giữ sự thuận tiện, dịch vụ và tiêu chuẩn sống hiện đại, đồng thời có thêm một nơi đủ gần thiên nhiên để trở về thường xuyên. Chính từ nhu cầu ấy, ý tưởng về một <strong>điền trang bản sắc Việt đương đại</strong> tại <strong>Saigon Farm Resort</strong> trở nên đáng để suy nghĩ.</p>

<div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 16px; margin: 30px 0;">
  <img src="assets/Index_asset/02_Phoi_Canh_3D/09.3D_TKCS-SUNSET_VILLA/SUNSET_1_VILLA/SFR_07.SAN_TRONG.jpg" alt="Hiên nhà & Sân trong đón gió" style="border-radius: 6px; width:100%; height: 280px; object-fit: cover;">
  <img src="assets/Index_asset/02_Phoi_Canh_3D/08._TKSP-CANH_QUAN_VEN_RUONG-20260515T044351Z-3-001/SFR_0.jpg" alt="Cánh đồng & Cảnh quan sinh thái" style="border-radius: 6px; width:100%; height: 280px; object-fit: cover;">
</div>

<h2>Saigon Farm Resort & Một Cách Sống Rộng Hơn</h2>
<p>Tại <strong>Saigon Farm Resort</strong>, mỗi điền trang có diện tích từ <strong>808m² đến 1.322m²</strong>. Quy mô ấy tạo ra một cách tổ chức không gian rất khác với nhà ở đô thị. Ngôi nhà có thể lùi lại để nhường chỗ cho sân, vườn, mái hiên, những hàng cây và các khoảng sinh hoạt ngoài trời.</p>
<p>Bao quanh khu nghỉ dưỡng là hồ nước tự nhiên 100ha, đồng lúa và những vườn dừa. Ở trung tâm, <strong>24.488m²</strong> được dành cho hệ tiện ích và trải nghiệm với nhà hàng, sân khấu ngoài trời, khu ngựa, khu nông nghiệp hữu cơ, hồ sen, hồ bơi, spa, bến thuyền cùng các hoạt động thư giãn.</p>

<div class="key-takeaways">
  <h3>Hệ Thống Không Gian Văn Hóa & Trải Nghiệm MDS Living</h3>
  <ul>
    <li><strong>Hiên Việt & Bờ Sen:</strong> Không gian thưởng trà, ngắm cảnh và kết nối thảnh thơi giữa thiên nhiên.</li>
    <li><strong>Giáo Trí Việt & Vườn Cội:</strong> Trẻ nhỏ tự tay gieo hạt, làm gốm, hội họa, thư pháp, tìm hiểu nhạc cụ dân tộc và đờn ca tài tử.</li>
    <li><strong>Việt Mã Trang (Horse Riding):</strong> Câu lạc bộ cưỡi ngựa quý tộc giữa thiên nhiên khoáng đạt.</li>
    <li><strong>Nếp Nhà Việt & Dòng Sử Việt:</strong> Nơi lưu giữ giá trị gia đình qua các mùa Tết, mùa diều, mùa sen, Trung Thu và mùa gặt.</li>
    <li><strong>Nhà Âm Sắc Việt & Quảng Trường Hội Việt:</strong> Không gian giao lưu văn hóa nghệ thuật tinh hoa.</li>
  </ul>
</div>

<div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 16px; margin: 30px 0;">
  <img src="assets/Index_asset/02_Phoi_Canh_3D/02.3D_TKCS-CANH_QUAN_VEN_HO-12.2025/SFR_20.jpg" alt="Việt Mã Trang" style="border-radius: 6px; width:100%; height: 280px; object-fit: cover;">
  <img src="assets/Index_asset/02_Phoi_Canh_3D/07.3D_TKCS-SUNRISE_2_VILLA/07.3D_TKCS-NHA_GO_4_MAU_2-_02.2026/07.TKCS-NHA_GO_4-MAU_2/02.NOI_THAT/01._TRET_PKHACH_&_BEP/SFR_01.jpg" alt="Không gian ẩm thực gia đình" style="border-radius: 6px; width:100%; height: 280px; object-fit: cover;">
</div>

<h2>Bản Sắc Cũng Cần Được Vận Hành</h2>
<p>Một gia đình hiện đại có điều kiện sẽ sống như thế nào nếu họ muốn giữ lại những điều đẹp của đời sống Việt trước đây? Họ vẫn cần một ngôi nhà được thiết kế tốt, hồ bơi, spa, nhà hàng, dịch vụ, an ninh, sự riêng tư và những tiêu chuẩn vận hành hiện đại. Nhưng trong một buổi chiều tiếp bạn bè hay đối tác, không gian ấy hoàn toàn mang một tinh thần khác: <em>một bàn tiệc Việt được chuẩn bị tinh tế, âm nhạc truyền thống vang lên vừa đủ, phía ngoài là hồ sen, khu vườn hay cánh đồng đang vào mùa.</em></p>
<p>Đó là lúc bản sắc trở thành một phần của hospitality và đời sống thực tế. Sự tinh tế nằm ở chỗ những trải nghiệm văn hóa phải đủ tự nhiên để người Việt cảm thấy gần gũi, đồng thời đủ chỉn chu để một thế hệ đã quen với tiêu chuẩn quốc tế vẫn cảm thấy tự hào và thoải mái.</p>

<h2>Thế Giới Đến Việt Nam Để Nhìn Thấy Việt Nam</h2>
<p>Nhật Bản có rất nhiều điều đáng để học. Ý, Hàn Quốc và những nền văn hóa phát triển khác cũng vậy. Nhưng điều khiến chúng ta yêu thích một khu vườn Nhật chính là tinh thần Nhật Bản trong đó. Người ta đi nửa vòng trái đất đến Tuscany bởi những ngôi nhà đá, vườn nho, ẩm thực và cảnh quan ấy thuộc về nước Ý. Bali được nhớ bởi Bali.</p>
<p><strong>Saigon Farm Resort</strong> được phát triển từ chính những chất liệu ấy, trong một chuẩn sống dành cho gia đình Việt hôm nay. Chúng ta có thể tiếp nhận những gì tốt nhất của thế giới, đồng thời đủ tự tin để tạo ra một nơi sống mang câu chuyện, cảnh quan và ký ức của chính mình.</p>

{contact_box}
"""
    },
    # 1. Sunset 1 Villa
    {
        "id": 101,
        "title": "Sunset 1 Villa (Mẫu 3PN - 1 Tầng): Tuyệt Tác Biệt Thự Vườn 1.000m² Bên Hồ",
        "excerpt": "Khuôn viên đất 1.000m², thiết kế 3 phòng ngủ 1 tầng tối ưu không gian sinh hoạt, hồ bơi riêng 45m², sân cỏ 182m² và vườn cây ăn trái 260m².",
        "image": "assets/Index_asset/02_Phoi_Canh_3D/09.3D_TKCS-SUNSET_VILLA/SUNSET_1_VILLA/SFR_04.PC_01.jpg",
        "date": "29 TH8 2026",
        "content": f"""
<p><strong>Sunset 1 Villa</strong> là mẫu biệt thự vườn 1 tầng mang triết lý kiến trúc tối giản, mở rộng tối đa tầm nhìn hướng hồ và thiên nhiên đồng nội. Mỗi căn biệt thự là một ốc đảo an yên, nơi gia chủ có thể hòa mình trọn vẹn vào không gian xanh khoáng đạt.</p>

<div class="key-takeaways">
  <h3>Thông Số Kỹ Thuật & Chi Tiết Thiết Kế</h3>
  <ul>
    <li><strong>Loại hình:</strong> Biệt thự vườn 1 tầng (Mẫu 3 Phòng Ngủ)</li>
    <li><strong>Diện tích khuôn viên đất:</strong> ~1.000m²</li>
    <li><strong>Cơ cấu công năng:</strong> Sảnh đón, Tiền sảnh, Phòng khách lớn 47m², Bếp khô & bàn ăn 29m², Bếp ướt, Phòng ngủ Master 26m² (WC Master 15m²), 02 Phòng ngủ phụ (16m²), Sân trong 42m²</li>
    <li><strong>Không gian cảnh quan & Tiện ích riêng:</strong>
      <ul>
        <li>Hồ bơi tràn viền riêng: <strong>45m²</strong></li>
        <li>Bãi cỏ xanh thư giãn: <strong>182m²</strong></li>
        <li>Vườn cây ăn trái Organic: <strong>260m²</strong></li>
      </ul>
    </li>
    <li><strong>Bàn giao:</strong> Hoàn thiện cao cấp, may đo theo gu thẩm mỹ riêng của gia chủ</li>
    <li><strong>Mức giá niêm yết:</strong> <span style="color:#c9a96e; font-size:1.2rem; font-weight:700;">Giá: Liên Hệ Trực Tiếp Đại Chúng Properties</span></li>
  </ul>
</div>

<h2>Mặt Bằng Bố Trí Công Năng Sunset 1 Villa</h2>
<p>Thiết kế mặt bằng chi tiết tối ưu hóa đối lưu gió tự nhiên và ánh sáng ngập tràn khắp các phòng:</p>
<div style="margin: 24px 0; text-align: center;">
  <img src="assets/Index_asset/02_Phoi_Canh_3D/09.3D_TKCS-SUNSET_VILLA/SUNSET_1_VILLA/SFR_01a.MB_TRET.jpg" alt="Mặt bằng Sunset 1 Villa" style="width: 100%; max-width: 800px; border-radius: 8px; border: 1px solid #333;">
</div>

<h2>Không Gian 3D Thực Tế & Nội Thất Nghỉ Dưỡng</h2>
<div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 16px; margin: 30px 0;">
  <img src="assets/Index_asset/02_Phoi_Canh_3D/09.3D_TKCS-SUNSET_VILLA/SUNSET_1_VILLA/SFR_04.PC_02.jpg" alt="Ngoại thất Sunset 1 Villa" style="border-radius: 6px; width:100%; height: 280px; object-fit: cover;">
  <img src="assets/Index_asset/02_Phoi_Canh_3D/09.3D_TKCS-SUNSET_VILLA/SUNSET_1_VILLA/SFR_05.P.KHACH_01.jpg" alt="Phòng khách sang trọng" style="border-radius: 6px; width:100%; height: 280px; object-fit: cover;">
  <img src="assets/Index_asset/02_Phoi_Canh_3D/09.3D_TKCS-SUNSET_VILLA/SUNSET_1_VILLA/SFR_06.BEP_01.jpg" alt="Khu vực bếp và bàn ăn" style="border-radius: 6px; width:100%; height: 280px; object-fit: cover;">
  <img src="assets/Index_asset/02_Phoi_Canh_3D/09.3D_TKCS-SUNSET_VILLA/SUNSET_1_VILLA/SFR_10.PNGU_MASTER_01.jpg" alt="Phòng ngủ Master view vườn" style="border-radius: 6px; width:100%; height: 280px; object-fit: cover;">
</div>

{contact_box}
"""
    },
    # 2. Sunset 2 Villa
    {
        "id": 102,
        "title": "Sunset 2 Villa (Mẫu 3PN - 2 Tầng): Không Gian Thượng Lưu View Trọn Hoàng Hôn",
        "excerpt": "Thiết kế 2 tầng bề thế với vườn cây ăn trái rộng đến 482m², hồ bơi riêng 45m², ban công rộng mở ngắm trọn sắc ráng chiều hoàng hôn buông xuống mặt hồ 100ha.",
        "image": "assets/Index_asset/02_Phoi_Canh_3D/09.3D_TKCS-SUNSET_VILLA/SUNSET_2_VILLA/SFR_04.PC_01.jpg",
        "date": "29 TH8 2026",
        "content": f"""
<p><strong>Sunset 2 Villa</strong> được tạo tác dành cho những chủ nhân yêu thích không gian sinh hoạt cao rộng và tầm view khoáng đạt từ tầng lầu. Nơi mỗi buổi chiều tà trở thành một bức tranh nghệ thuật với ánh hoàng hôn phản chiếu rực rỡ trên mặt hồ sinh thái.</p>

<div class="key-takeaways">
  <h3>Thông Số Chi Tiết Sunset 2 Villa</h3>
  <ul>
    <li><strong>Loại hình:</strong> Biệt thự vườn 2 tầng (3 Phòng Ngủ)</li>
    <li><strong>Diện tích khuôn viên đất:</strong> ~1.200m²</li>
    <li><strong>Cơ cấu công năng:</strong>
      <ul>
        <li>Tầng trệt: Sảnh đón, Phòng khách 37m², Bếp khô & Bàn ăn 31m², Bếp ướt, Kho, Hồ bơi 45m², Sân cỏ 192m², Vườn cây ăn trái 482m²</li>
        <li>Tầng lầu: Sảnh tầng, Phòng sinh hoạt chung, Phòng ngủ Master 30m² (WC Master 15m²), 02 Phòng ngủ phụ (26m²), 02 Balcony ngắm cảnh rộng mở</li>
      </ul>
    </li>
    <li><strong>Mức giá niêm yết:</strong> <span style="color:#c9a96e; font-size:1.2rem; font-weight:700;">Giá: Liên Hệ Trực Tiếp Đại Chúng Properties</span></li>
  </ul>
</div>

<h2>Mặt Bằng Bố Trí Tầng Trệt & Tầng Lầu</h2>
<div style="margin: 24px 0; text-align: center;">
  <img src="assets/Index_asset/02_Phoi_Canh_3D/09.3D_TKCS-SUNSET_VILLA/SUNSET_2_VILLA/SFR_01a.MB_TRET.jpg" alt="Mặt bằng Sunset 2 Villa" style="width: 100%; max-width: 800px; border-radius: 8px; border: 1px solid #333;">
</div>

<h2>Phối Cảnh Kiến Trúc Hoàng Hôn Tuyệt Đẹp</h2>
<div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 16px; margin: 30px 0;">
  <img src="assets/Index_asset/02_Phoi_Canh_3D/09.3D_TKCS-SUNSET_VILLA/SUNSET_2_VILLA/SFR_04.PC_02.jpg" alt="Phối cảnh Sunset 2 Villa" style="border-radius: 6px; width:100%; height: 280px; object-fit: cover;">
  <img src="assets/Index_asset/02_Phoi_Canh_3D/09.3D_TKCS-SUNSET_VILLA/SUNSET_2_VILLA/SFR_05.PKHACH_&_BEP_01.jpg" alt="Kiến trúc nội thất ven hồ" style="border-radius: 6px; width:100%; height: 280px; object-fit: cover;">
  <img src="assets/Index_asset/02_Phoi_Canh_3D/09.3D_TKCS-SUNSET_VILLA/SUNSET_2_VILLA/SFR_06.SAN_SAU.jpg" alt="Không gian sân sau và hồ bơi" style="border-radius: 6px; width:100%; height: 280px; object-fit: cover;">
  <img src="assets/Index_asset/02_Phoi_Canh_3D/09.3D_TKCS-SUNSET_VILLA/SUNSET_2_VILLA/SFR_10.PNGU_MASTER_01.jpg" alt="Phòng ngủ tầng lầu view panorama" style="border-radius: 6px; width:100%; height: 280px; object-fit: cover;">
</div>

{contact_box}
"""
    },
    # 3. Sunrise 1 Villa
    {
        "id": 103,
        "title": "Sunrise 1 Villa (Mẫu 3PN Đơn Lập Vườn Sinh Thái): Đón Trọn Ánh Bình Minh Tinh Khôi",
        "excerpt": "Khuôn viên 1.000m² - 1.200m², hướng Đông Nam đón bình minh, hồ bơi riêng 40m², thảm cỏ xanh và vườn thảo mộc hương thơm tự nhiên.",
        "image": "assets/Index_asset/02_Phoi_Canh_3D/05.3D_TKCS-SUNRISE_1_VILLA/05.3D_TKCS-NHA_GO_4_MAU_1-_07.2025/01._NGOAI_THAT/SFR_NGOAI_THAT_(4).jpg",
        "date": "29 TH8 2026",
        "content": f"""
<p><strong>Sunrise 1 Villa</strong> là biểu tượng của nguồn sinh khí tươi mới mỗi sớm mai. Thiết kế mở hướng nắng sớm, mang năng lượng thiên nhiên nguyên lành vào từng ngóc ngách không gian sống.</p>

<div class="key-takeaways">
  <h3>Thông Số Kỹ Thuật Sunrise 1 Villa</h3>
  <ul>
    <li><strong>Loại hình:</strong> Biệt thự đơn lập sinh thái (3 Phòng Ngủ)</li>
    <li><strong>Diện tích khuôn viên đất:</strong> 1.000m² - 1.200m²</li>
    <li><strong>Tiện ích khuôn viên:</strong> Hồ bơi riêng 40m², Thềm Deck tắm nắng, Vườn hoa thảo mộc 300m², Sân cỏ BBQ</li>
    <li><strong>Không gian nội thất:</strong> Phòng khách cao trần 4.2m view hồ bơi, bếp mở tiêu chuẩn Châu Âu, 3 phòng ngủ khép kín tiện nghi.</li>
    <li><strong>Mức giá niêm yết:</strong> <span style="color:#c9a96e; font-size:1.2rem; font-weight:700;">Giá: Liên Hệ Trực Tiếp Đại Chúng Properties</span></li>
  </ul>
</div>

<h2>Mặt Bằng Chi Tiết Sunrise 1 Villa</h2>
<div style="margin: 24px 0; text-align: center;">
  <img src="assets/Index_asset/MatBang/MatBang_Sunrise_1.png" alt="Mặt bằng Sunrise 1 Villa" style="width: 100%; max-width: 800px; border-radius: 8px; border: 1px solid #333;">
</div>

<h2>Hình Ảnh Phối Cảnh & Thực Tế 3D</h2>
<div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 16px; margin: 30px 0;">
  <img src="assets/Index_asset/02_Phoi_Canh_3D/05.3D_TKCS-SUNRISE_1_VILLA/05.3D_TKCS-NHA_GO_4_MAU_1-_07.2025/01._NGOAI_THAT/SFR_NGOAI_THAT_(10).jpg" alt="Phối cảnh Sunrise 1 Villa" style="border-radius: 6px; width:100%; height: 280px; object-fit: cover;">
  <img src="assets/Index_asset/02_Phoi_Canh_3D/05.3D_TKCS-SUNRISE_1_VILLA/05.3D_TKCS-NHA_GO_4_MAU_1-_07.2025/02._NOI_THAT/01.TANG_TRET/SFR_P.KHACH_&_AN_(1).jpg" alt="Phòng khách thoáng đãng" style="border-radius: 6px; width:100%; height: 280px; object-fit: cover;">
  <img src="assets/Index_asset/02_Phoi_Canh_3D/05.3D_TKCS-SUNRISE_1_VILLA/05.3D_TKCS-NHA_GO_4_MAU_1-_07.2025/02._NOI_THAT/01.TANG_TRET/SFR_P.KHACH_&_AN_(2).jpg" alt="Bếp ăn gia đình ấm cúng" style="border-radius: 6px; width:100%; height: 280px; object-fit: cover;">
  <img src="assets/Index_asset/02_Phoi_Canh_3D/05.3D_TKCS-SUNRISE_1_VILLA/05.3D_TKCS-NHA_GO_4_MAU_1-_07.2025/02._NOI_THAT/01.TANG_TRET/SFR_P.NGU_01_(1).jpg" alt="Phòng ngủ hướng vườn bình minh" style="border-radius: 6px; width:100%; height: 280px; object-fit: cover;">
</div>

{contact_box}
"""
    },
    # 4. Sunrise 2 Villa
    {
        "id": 104,
        "title": "Sunrise 2 Villa (Mẫu 4PN Đơn Lập Siêu VIP - 1.500m²): Di Sản Truyền Đời Đẳng Cấp Nhất",
        "excerpt": "Tuyệt tác Dinh thự đơn lập 4 phòng ngủ trên khuôn viên đất 1.500m², hồ bơi đại gia đình 53m², sân sàn gỗ ngoài trời 31m² và sân thượng ngắm bình minh 40m².",
        "image": "assets/Index_asset/02_Phoi_Canh_3D/07.3D_TKCS-SUNRISE_2_VILLA/07.3D_TKCS-NHA_GO_4_MAU_2-_02.2026/07.TKCS-NHA_GO_4-MAU_2/01.NGOAI_THAT/SFR_TONG_THE_01.jpg",
        "date": "29 TH8 2026",
        "content": f"""
<p><strong>Sunrise 2 Villa</strong> là biểu tượng cao quý nhất tại Saigon Farm Resort. Dành riêng cho các gia đình đa thế hệ mong muốn sở hữu một bất động sản di sản truyền đời thực thụ, nơi lưu giữ sự gắn kết thiêng liêng và khẳng định vị thế tinh hoa của gia tộc.</p>

<div class="key-takeaways">
  <h3>Thông Số Đỉnh Cao Sunrise 2 Villa</h3>
  <ul>
    <li><strong>Loại hình:</strong> Biệt thự đơn lập 4 Phòng Ngủ siêu sang (2 Tầng)</li>
    <li><strong>Diện tích khuôn viên đất:</strong> Từ <strong>1.200m² - 1.500m²</strong></li>
    <li><strong>Điểm nhấn tiện ích đặc quyền tại gia:</strong>
      <ul>
        <li>Hồ bơi riêng kích thước lớn: <strong>53m²</strong></li>
        <li>Sàn gỗ ngoài trời & Lounge: <strong>31m²</strong></li>
        <li>Hành lang & Hiên ngắm cảnh: <strong>60m²</strong></li>
        <li>Sân thượng ngắm bình minh tầng lầu: <strong>40m²</strong></li>
        <li>04 Phòng ngủ rộng lớn tiêu chuẩn 5 sao quốc tế</li>
      </ul>
    </li>
    <li><strong>Mức giá niêm yết:</strong> <span style="color:#c9a96e; font-size:1.2rem; font-weight:700;">Giá: Liên Hệ Trực Tiếp Đại Chúng Properties</span></li>
  </ul>
</div>

<h2>Mặt Bằng Tổng Thể & Chi Tiết Sunrise 2 Villa</h2>
<div style="margin: 24px 0; text-align: center;">
  <img src="assets/Index_asset/MatBang/MatBang_Sunrise_2.png" alt="Mặt bằng Sunrise 2 Villa" style="width: 100%; max-width: 800px; border-radius: 8px; border: 1px solid #333;">
</div>

<h2>Không Gian Sống Xa Hoa Giữa Thiên Nhiên Nguyên Bản</h2>
<div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 16px; margin: 30px 0;">
  <img src="assets/Index_asset/02_Phoi_Canh_3D/07.3D_TKCS-SUNRISE_2_VILLA/07.3D_TKCS-NHA_GO_4_MAU_2-_02.2026/07.TKCS-NHA_GO_4-MAU_2/01.NGOAI_THAT/SFR_04.update_san_vuon.jpg" alt="Kiến trúc Sunrise 2 Villa" style="border-radius: 6px; width:100%; height: 280px; object-fit: cover;">
  <img src="assets/Index_asset/02_Phoi_Canh_3D/07.3D_TKCS-SUNRISE_2_VILLA/07.3D_TKCS-NHA_GO_4_MAU_2-_02.2026/07.TKCS-NHA_GO_4-MAU_2/02.NOI_THAT/01._TRET_PKHACH_&_BEP/SFR_01.jpg" alt="Phòng khách đại tiệc" style="border-radius: 6px; width:100%; height: 280px; object-fit: cover;">
  <img src="assets/Index_asset/02_Phoi_Canh_3D/07.3D_TKCS-SUNRISE_2_VILLA/07.3D_TKCS-NHA_GO_4_MAU_2-_02.2026/07.TKCS-NHA_GO_4-MAU_2/02.NOI_THAT/04._LAU_P_SHC/SFR_1.jpg" alt="Phòng sinh hoạt chung tầng lầu" style="border-radius: 6px; width:100%; height: 280px; object-fit: cover;">
  <img src="assets/Index_asset/02_Phoi_Canh_3D/07.3D_TKCS-SUNRISE_2_VILLA/07.3D_TKCS-NHA_GO_4_MAU_2-_02.2026/07.TKCS-NHA_GO_4-MAU_2/02.NOI_THAT/02._TRET_PN_TRET_01/SFR_01-2.jpg" alt="Phòng ngủ Master sang trọng" style="border-radius: 6px; width:100%; height: 280px; object-fit: cover;">
</div>

{contact_box}
"""
    },
    # 5. Lakeview Grand Villa
    {
        "id": 105,
        "title": "Lakeview Grand Villa (Biệt Thự Vườn Ven Hồ): Bản Giao Hưởng Giữa Nước Và Cây Xanh",
        "excerpt": "Tọa độ trực diện mặt nước hồ sinh thái 100ha, bến câu cá riêng tại sân sau, hồ bơi vô cực view mặt gương phản chiếu mây trời tuyệt mỹ.",
        "image": "assets/Index_asset/02_Phoi_Canh_3D/02.3D_TKCS-CANH_QUAN_VEN_HO-12.2025/SFR_1.jpg",
        "date": "29 TH8 2026",
        "content": f"""
<p><strong>Lakeview Grand Villa</strong> là sự kết hợp hoàn hảo giữa kiến trúc nhiệt đới đương đại và cảnh quan mặt nước tráng lệ. Mỗi căn biệt thự trực diện bờ hồ mang lại không khí mát lành quanh năm cùng tầm nhìn vô cực khoáng đạt.</p>

<div class="key-takeaways">
  <h3>Đặc Điểm Nổi Bật Lakeview Grand Villa</h3>
  <ul>
    <li><strong>Khuôn viên:</strong> 1.100m² - 1.350m² trực diện mặt hồ sinh thái</li>
    <li><strong>Tiện ích đặc quyền:</strong> Bến ngắm cảnh / chèo thuyền riêng, Hồ bơi vô cực mặt gương 50m², Vườn hoa ven hồ</li>
    <li><strong>Thiết kế:</strong> 3 - 4 Phòng ngủ mở hoàn toàn ra cảnh quan nước, kính Low-E cản nhiệt chạm sàn</li>
    <li><strong>Pháp lý & Sở hữu:</strong> Pháp lý hoàn chỉnh, sổ đỏ sẵn sàng</li>
    <li><strong>Mức giá niêm yết:</strong> <span style="color:#c9a96e; font-size:1.2rem; font-weight:700;">Giá: Liên Hệ Trực Tiếp Đại Chúng Properties</span></li>
  </ul>
</div>

<h2>Hình Ảnh Phối Cảnh & Trải Nghiệm Ven Hồ</h2>
<div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 16px; margin: 30px 0;">
  <img src="assets/Index_asset/02_Phoi_Canh_3D/02.3D_TKCS-CANH_QUAN_VEN_HO-12.2025/SFR_1.jpg" alt="Hồ bơi vô cực ven hồ" style="border-radius: 6px; width:100%; height: 280px; object-fit: cover;">
  <img src="assets/Index_asset/02_Phoi_Canh_3D/02.3D_TKCS-CANH_QUAN_VEN_HO-12.2025/SFR_21.jpg" alt="Hiên ngắm cảnh hoàng hôn" style="border-radius: 6px; width:100%; height: 280px; object-fit: cover;">
  <img src="assets/Index_asset/02_Phoi_Canh_3D/02.3D_TKCS-CANH_QUAN_VEN_HO-12.2025/SFR_22.jpg" alt="Khuôn viên vườn hoa ven hồ" style="border-radius: 6px; width:100%; height: 280px; object-fit: cover;">
  <img src="assets/Index_asset/02_Phoi_Canh_3D/04.3D_TKCS-NHA_GO_3-07.2025/01.NGOAI_THAT/SFR_1.jpg" alt="Không gian kiến trúc gỗ sinh thái" style="border-radius: 6px; width:100%; height: 280px; object-fit: cover;">
</div>

{contact_box}
"""
    },
    # 6. Riverside Eco Villa
    {
        "id": 106,
        "title": "Riverside Eco Villa (Biệt Thự Vườn Thảo Dược): Chốn An Trú Thanh Lọc Thân Tâm Trí",
        "excerpt": "Bao bọc bởi kênh đào sinh thái tự nhiên và khu vườn thảo dược dược liệu quý, đem lại không gian sống thuần khiết giúp tái tạo năng lượng thể chất hoàn hảo.",
        "image": "assets/Index_asset/02_Phoi_Canh_3D/08._TKSP-CANH_QUAN_VEN_RUONG-20260515T044351Z-3-001/SFR_0.jpg",
        "date": "29 TH8 2026",
        "content": f"""
<p><strong>Riverside Eco Villa</strong> ra đời từ mong ước kiến tạo một chốn an dưỡng đích thực cho những chủ nhân tìm kiếm sự an yên, tĩnh lặng và chữa lành giữa thiên nhiên.</p>

<div class="key-takeaways">
  <h3>Chi Tiết Không Gian Riverside Eco Villa</h3>
  <ul>
    <li><strong>Khuôn viên:</strong> 1.000m² - 1.200m² với kênh nước chảy tuần hoàn tự nhiên</li>
    <li><strong>Hệ sinh thái vườn:</strong> Vườn dược liệu cổ truyền (xả, hương nhu, bạc hà, cúc kim cương), vườn bưởi da xanh và xoài cát sạch</li>
    <li><strong>Khu trị liệu tại gia:</strong> Bồn ngâm khoáng nóng Onsen thảo dược, chòi Yoga ven suối</li>
    <li><strong>Mức giá niêm yết:</strong> <span style="color:#c9a96e; font-size:1.2rem; font-weight:700;">Giá: Liên Hệ Trực Tiếp Đại Chúng Properties</span></li>
  </ul>
</div>

<div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 16px; margin: 30px 0;">
  <img src="assets/Index_asset/02_Phoi_Canh_3D/08._TKSP-CANH_QUAN_VEN_RUONG-20260515T044351Z-3-001/SFR_1.png" alt="Vườn sinh thái xanh ngát" style="border-radius: 6px; width:100%; height: 280px; object-fit: cover;">
  <img src="assets/Index_asset/02_Phoi_Canh_3D/08._TKSP-CANH_QUAN_VEN_RUONG-20260515T044351Z-3-001/SFR_2.png" alt="Không gian thư thái ven rạch" style="border-radius: 6px; width:100%; height: 280px; object-fit: cover;">
  <img src="assets/Index_asset/02_Phoi_Canh_3D/08._TKSP-CANH_QUAN_VEN_RUONG-20260515T044351Z-3-001/SFR_4.png" alt="Lối đi phủ bóng cây" style="border-radius: 6px; width:100%; height: 280px; object-fit: cover;">
  <img src="assets/Index_asset/02_Phoi_Canh_3D/08._TKSP-CANH_QUAN_VEN_RUONG-20260515T044351Z-3-001/SFR_5.png" alt="Vườn hữu cơ xanh mướt" style="border-radius: 6px; width:100%; height: 280px; object-fit: cover;">
</div>

{contact_box}
"""
    },
    # 7. Hệ tiện ích đa tầng
    {
        "id": 122,
        "title": "Hệ Sinh Thái Tiện Ích Đa Tầng Gần 3ha: Clubhouse, Bến Thuyền, Organic Farm & Herbal Spa",
        "excerpt": "Dành hơn nửa diện tích cho thiên nhiên và tiện ích: Nông trại Organic Farm to Table tại gia, CLB cưỡi ngựa Horse Riding, Sân thể thao Pickleball, Spa thảo dược và Bến thuyền ven hồ.",
        "image": "assets/Index_asset/MatBang/SoDo_TienIch_TongThe.png",
        "date": "29 TH8 2026",
        "content": f"""
<p>Tại <strong>Saigon Farm Resort</strong>, triết lý phát triển lấy trải nghiệm sống an lành làm trọng tâm. Với gần 3ha diện tích dành trọn cho cảnh quan và hệ tiện ích đặc quyền, mỗi ngày tại đây là một kỳ nghỉ bất tận:</p>

<div class="key-takeaways">
  <h3>Các Phân Khu Tiện Ích Đặc Quyền</h3>
  <ul>
    <li><strong>Clubhouse & Lounge Ven Hồ:</strong> Không gian giao lưu thượng lưu, nhà hàng ẩm thực Fine Dining giao hòa cùng thiên nhiên.</li>
    <li><strong>Nông Trại Hữu Cơ Organic Farm:</strong> Cung cấp nguồn thực phẩm sạch khép kín chuẩn Farm-to-Table tại gia (Rau hữu cơ, trứng sạch, trái cây nhiệt đới).</li>
    <li><strong>Horse Riding Club:</strong> Câu lạc bộ cưỡi ngựa quý tộc đẳng cấp ven biển.</li>
    <li><strong>Herbal Spa & Zen Zone:</strong> Khu trị liệu thảo dược, thiền tịnh, tái tạo năng lượng thể chất và tinh thần.</li>
    <li><strong>Thể Thao & Năng Động (Wellness & Sport):</strong> Sân thể thao thời thượng Pickleball, Phòng Gym & Yoga hướng hồ, đường chạy bộ rợp bóng cây xanh.</li>
    <li><strong>Hoạt Động Gia Đình (Outdoor Activities):</strong> Bãi cỏ thả diều, tiệc nướng BBQ ngoài trời, khu cắm trại Glamping ven hồ.</li>
  </ul>
</div>

<h2>Sơ Đồ Phân Bổ Hệ Thống Tiện Ích Đa Tầng</h2>
<div style="margin: 24px 0; text-align: center;">
  <img src="assets/Index_asset/MatBang/SoDo_TienIch_TongThe.png" alt="Sơ đồ tiện ích tổng thể" style="width: 100%; max-width: 800px; border-radius: 8px; border: 1px solid #333;">
</div>

<div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 16px; margin: 30px 0;">
  <img src="assets/Index_asset/02_Phoi_Canh_3D/02.3D_TKCS-CANH_QUAN_VEN_HO-12.2025/SFR_0.jpg" alt="Clubhouse ven hồ" style="border-radius: 6px; width:100%; height: 280px; object-fit: cover;">
  <img src="assets/Index_asset/02_Phoi_Canh_3D/02.3D_TKCS-CANH_QUAN_VEN_HO-12.2025/SFR_21.jpg" alt="Không gian thư giãn ven nước" style="border-radius: 6px; width:100%; height: 280px; object-fit: cover;">
  <img src="assets/Index_asset/02_Phoi_Canh_3D/02.3D_TKCS-CANH_QUAN_VEN_HO-12.2025/SFR_1.jpg" alt="Hồ bơi vô cực bên hồ lớn" style="border-radius: 6px; width:100%; height: 280px; object-fit: cover;">
  <img src="assets/Index_asset/02_Phoi_Canh_3D/02.3D_TKCS-CANH_QUAN_VEN_HO-12.2025/SFR_6.jpg" alt="Nông trại sinh thái xanh ngát" style="border-radius: 6px; width:100%; height: 280px; object-fit: cover;">
</div>

{contact_box}
"""
    },
    # 8. Tọa độ vàng & Liên kết vùng
    {
        "id": 125,
        "title": "Tọa Độ Vàng Tứ Cận: Tựa Hồ - Hướng Biển - Ôm Trọn Hương Đồng Nội",
        "excerpt": "Tọa lạc tại Phường Đất Đỏ, chỉ 55 phút về trung tâm TP.HCM, 25 phút đến Sân bay Quốc tế Long Thành, kết nối trực tiếp các trục cao tốc và thủ phủ du lịch Hồ Tràm.",
        "image": "assets/Index_asset/Flycam/DJI_0014_2.JPG",
        "date": "29 TH8 2026",
        "content": f"""
<p><strong>Saigon Farm Resort</strong> sở hữu vị thế độc tôn hiếm có: <em>Tựa hồ tự nhiên 100ha - Hướng biển Lộc An / Hồ Tràm - Ôm trọn hương đồng nội thanh bình</em>. Một khoảng cách hoàn hảo để tách biệt khỏi sự ồn ào phố thị nhưng vẫn kết nối nhanh chóng với trung tâm kinh tế.</p>

<div class="key-takeaways">
  <h3>Tâm Điểm Kết Nối Vùng Hoàn Hảo</h3>
  <ul>
    <li><strong>55 Phút:</strong> Di chuyển nhanh chóng về trung tâm TP.HCM qua mạng lưới cao tốc</li>
    <li><strong>25 Phút:</strong> Tiếp cận trực tiếp Cảng hàng không Quốc tế Long Thành</li>
    <li><strong>10 - 15 Phút:</strong> Chạm đến Bãi tắm Lộc An, Bãi biển Long Hải và Quần thể Casino / Sân Golf Hồ Tràm</li>
    <li><strong>Hạ tầng giao thông đồng bộ:</strong> Cao tốc Biên Hòa - Vũng Tàu, Cao tốc Hồ Tràm - Long Thành, Tuyến đường ven biển DT994, Quốc lộ 55.</li>
  </ul>
</div>

<h2>Sơ Đồ Kết Nối Giao Thương & Du Lịch</h2>
<div style="margin: 24px 0; text-align: center;">
  <img src="assets/Index_asset/MatBang/SoDo_LienKet_Vung.png" alt="Sơ đồ liên kết vùng Saigon Farm Resort" style="width: 100%; max-width: 800px; border-radius: 8px; border: 1px solid #333;">
</div>

<div style="margin: 24px 0;">
  <img src="assets/Index_asset/Flycam/DJI_0997_2.JPG" alt="Toàn cảnh thiên nhiên hồ nước 100ha nhìn từ flycam" style="width: 100%; border-radius: 8px;">
</div>

{contact_box}
"""
    },
    # 9. MDS Living
    {
        "id": 506,
        "title": "MDS LIVING: Chuẩn Mực Quản Gia & Quản Lý Vận Hành Nghỉ Dưỡng Chuyên Nghiệp",
        "excerpt": "Dịch vụ quản gia chuyên trách, an ninh đa lớp, bảo trì chuẩn resort và chương trình khai thác cho thuê minh bạch, tối ưu dòng tiền bền vững cho gia chủ.",
        "image": "assets/Index_asset/02_Phoi_Canh_3D/06.3D_TKCS-NHA_DIEU_HANH_VEN_RUONG-08.2025_(update)/01.TANG_TRET_+_NGOAI_THAT/SFR_1.jpg",
        "date": "29 TH8 2026",
        "content": f"""
<p>Với <strong>MDS LIVING</strong>, quản lý vận hành không chỉ là quy trình mà là nghệ thuật chăm sóc xúc cảm. Từng nhành cây, ngọn cỏ, căn biệt thự đều được nâng niu chu đáo để mỗi ngày trôi qua đều là một kỳ nghỉ bất tận.</p>

<div class="key-takeaways">
  <h3>4 Trụ Cột Vận Hành Của MDS LIVING</h3>
  <ul>
    <li><strong>Đặc Quyền 24/7 & Quản Gia Chuyên Trách:</strong> Đáp ứng mọi nhu cầu cá nhân hóa “may đo” cho từng thành viên trong gia đình.</li>
    <li><strong>An Ninh Đa Lớp:</strong> Lá chắn an toàn tuyệt đối, đảm bảo không gian riêng tư và tĩnh lặng.</li>
    <li><strong>Bảo Trì - Bảo Dưỡng Chuẩn Resort:</strong> Chăm sóc chủ động cảnh quan, hồ bơi, hệ thống kỹ thuật để giữ trọn giá trị tài sản qua nhiều thế hệ.</li>
    <li><strong>Khai Thác Cho Thuê Bền Vững:</strong> Giải pháp tối ưu dòng tiền cho thuê minh bạch khi gia chủ không sử dụng, chia sẻ lợi nhuận bền vững.</li>
  </ul>
</div>

<h2>Mô Hình Vận Hành Chuẩn Quốc Tế</h2>
<div style="margin: 24px 0; text-align: center;">
  <img src="assets/Index_asset/MatBang/QuanLy_MDS_Living.png" alt="Quản lý vận hành MDS Living" style="width: 100%; max-width: 800px; border-radius: 8px; border: 1px solid #333;">
</div>

<div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 16px; margin: 30px 0;">
  <img src="assets/Index_asset/02_Phoi_Canh_3D/06.3D_TKCS-NHA_DIEU_HANH_VEN_RUONG-08.2025_(update)/01.TANG_TRET_+_NGOAI_THAT/SFR_10.jpg" alt="Không gian tiếp đón khách" style="border-radius: 6px; width:100%; height: 280px; object-fit: cover;">
  <img src="assets/Index_asset/02_Phoi_Canh_3D/06.3D_TKCS-NHA_DIEU_HANH_VEN_RUONG-08.2025_(update)/01.TANG_TRET_+_NGOAI_THAT/SFR_15.jpg" alt="Dịch vụ quản gia chuyên nghiệp" style="border-radius: 6px; width:100%; height: 280px; object-fit: cover;">
</div>

{contact_box}
"""
    },
    # 10. Bến Thuyền & Thể Thao Dưới Nước (ID 120)
    {
        "id": 120,
        "title": "Bến Thuyền & Trải Nghiệm Thể Thao Mặt Nước Bên Hồ 100ha",
        "excerpt": "Trải nghiệm chèo SUP, Kayak đón bình minh hoặc du ngoạn du thuyền thưởng ngoạn hoàng hôn buông lơi trên mặt hồ thơ mộng.",
        "image": "assets/Index_asset/02_Phoi_Canh_3D/02.3D_TKCS-CANH_QUAN_VEN_HO-12.2025/SFR_21.jpg",
        "date": "29 TH8 2026",
        "content": f"""
<p>Hồ sinh thái 100ha mang đến cho Saigon Farm Resort một đặc quyền hiếm có: không gian mặt nước bao la, tĩnh lặng và khoáng đạt. Bến thuyền sinh thái tại resort là nơi khởi đầu của những chuyến phiêu lưu nhẹ nhàng và những khoảnh khắc lãng mạn.</p>

<div class="key-takeaways">
  <h3>Trải Nghiệm Mặt Nước Không Thể Bỏ Lỡ</h3>
  <ul>
    <li><strong>Chèo Kayak & SUP buổi sớm:</strong> Đón làn sương mai bồng bềnh trên mặt hồ và lắng nghe tiếng chim ca ríu rít.</li>
    <li><strong>Du thuyền thưởng ngoạn hoàng hôn:</strong> Thưởng thức ly rượu vang hảo hạng khi mặt trời từ từ lặn xuống mặt nước lấp lánh ráng chiều.</li>
    <li><strong>Bến câu cá thư giãn:</strong> Những giờ phút tĩnh tâm rèn luyện sự kiên nhẫn giữa khung cảnh sơn thủy hữu tình.</li>
  </ul>
</div>

<div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 16px; margin: 30px 0;">
  <img src="assets/Index_asset/02_Phoi_Canh_3D/02.3D_TKCS-CANH_QUAN_VEN_HO-12.2025/SFR_21.jpg" alt="Bến thuyền hoàng hôn" style="border-radius: 6px; width:100%; height: 280px; object-fit: cover;">
  <img src="assets/Index_asset/02_Phoi_Canh_3D/02.3D_TKCS-CANH_QUAN_VEN_HO-12.2025/SFR_22.jpg" alt="Mặt hồ trong xanh" style="border-radius: 6px; width:100%; height: 280px; object-fit: cover;">
</div>

{contact_box}
"""
    },
    # 11. Nông Trại Hữu Cơ Organic Farm (ID 121)
    {
        "id": 121,
        "title": "Nông Trại Hữu Cơ Organic Farm: Chuẩn Sống Xanh Farm-to-Table Tại Gia",
        "excerpt": "Cung cấp nguồn rau quả hữu cơ, trứng sạch và nông sản tươi lành mỗi ngày cho bữa cơm gia đình trọn vẹn dinh dưỡng.",
        "image": "assets/Index_asset/02_Phoi_Canh_3D/08._TKSP-CANH_QUAN_VEN_RUONG-20260515T044351Z-3-001/SFR_1.png",
        "date": "29 TH8 2026",
        "content": f"""
<p>Tại Saigon Farm Resort, chúng tôi tin rằng sức khỏe và hạnh phúc bắt đầu từ những điều thuần khiết nhất. Nông trại hữu cơ Organic Farm gần 1ha được chăm sóc theo tiêu chuẩn canh tác tự nhiên không hóa chất.</p>

<div class="key-takeaways">
  <h3>Giá Trị Nông Trại Mang Đến Cho Gia Đình</h3>
  <ul>
    <li><strong>Thực phẩm sạch 100%:</strong> Rau xanh, củ quả theo mùa được thu hoạch trực tiếp gửi tới tận căn bếp biệt thự của bạn.</li>
    <li><strong>Trải nghiệm làm nông dân nhí:</strong> Không gian giáo dục sinh động giúp con trẻ yêu thiên nhiên, học cách ươm mầm, tưới cây và chăm sóc động vật.</li>
    <li><strong>Vườn cây ăn trái sum suê:</strong> Xoài, bưởi, mít, ổi được trồng lâu năm cho bóng mát và quả ngọt quanh năm.</li>
  </ul>
</div>

<div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 16px; margin: 30px 0;">
  <img src="assets/Index_asset/02_Phoi_Canh_3D/08._TKSP-CANH_QUAN_VEN_RUONG-20260515T044351Z-3-001/SFR_2.png" alt="Nông trại hữu cơ" style="border-radius: 6px; width:100%; height: 280px; object-fit: cover;">
  <img src="assets/Index_asset/02_Phoi_Canh_3D/08._TKSP-CANH_QUAN_VEN_RUONG-20260515T044351Z-3-001/SFR_5.png" alt="Khu vườn ươm xanh mướt" style="border-radius: 6px; width:100%; height: 280px; object-fit: cover;">
</div>

{contact_box}
"""
    },
    # 12. Horse Riding Club (ID 123)
    {
        "id": 123,
        "title": "Horse Riding Club: Câu Lạc Bộ Cưỡi Ngựa Quý Tộc Đầu Tiên Ven Biển",
        "excerpt": "Trải nghiệm bộ môn thể thao quý tộc với đàn ngựa thuần chủng được huấn luyện bài bản bởi các chuyên gia quốc tế.",
        "image": "assets/Index_asset/02_Phoi_Canh_3D/02.3D_TKCS-CANH_QUAN_VEN_HO-12.2025/SFR_20.jpg",
        "date": "29 TH8 2026",
        "content": f"""
<p>Cưỡi ngựa không chỉ là một môn thể thao mà còn là nghệ thuật rèn luyện phong thái đĩnh đạc, tính kiên định và khả năng thấu cảm. <strong>Horse Riding Club</strong> tại Saigon Farm Resort mang đến sân tập tiêu chuẩn và những cung đường dạo rợp bóng cây.</p>

<div class="key-takeaways">
  <h3>Đặc Quyền Cưỡi Ngựa Dành Cho Cư Dân</h3>
  <ul>
    <li>Đội ngũ huấn luyện viên chuyên nghiệp kèm cặp từng học viên từ cơ bản đến nâng cao.</li>
    <li>Khu chuồng trại chuẩn Châu Âu, chăm sóc y tế và dinh dưỡng định kỳ cho ngựa.</li>
    <li>Cung đường mòn ven hồ dành cho các buổi cưỡi ngựa thư giãn ngắm cảnh bình minh và chiều tà.</li>
  </ul>
</div>

{contact_box}
"""
    },
    # 13. Herbal Spa & Wellness (ID 124)
    {
        "id": 124,
        "title": "Herbal Spa & Zen Zone: Nghệ Thuật Chăm Sóc Sức Khỏe Bằng Thảo Dược Tự Nhiên",
        "excerpt": "Liệu pháp xông hơi thảo mộc cổ truyền, ngâm khoáng nóng Onsen và các lớp thiền định, Yoga ngoài trời giúp phục hồi sinh lực.",
        "image": "assets/Index_asset/02_Phoi_Canh_3D/02.3D_TKCS-CANH_QUAN_VEN_HO-12.2025/SFR_10.jpg",
        "date": "29 TH8 2026",
        "content": f"""
<p>Bước vào <strong>Herbal Spa</strong>, mọi âu lo căng thẳng của nhịp sống đô thị đều tan biến sau cánh cửa. Mùi hương tinh dầu thảo mộc dịu nhẹ hòa cùng tiếng nước chảy róc rách tạo nên một không gian thiền định thuần khiết.</p>

<div class="key-takeaways">
  <h3>Các Gói Liệu Trình Trị Liệu Đặc Trưng</h3>
  <ul>
    <li><strong>Tắm khoáng Onsen & Thảo dược bản địa:</strong> Giải độc cơ thể, lưu thông khí huyết và trẻ hóa làn da.</li>
    <li><strong>Massage trị liệu ấn huyệt cổ truyền:</strong> Giảm đau mỏi cơ khớp, mang lại giấc ngủ sâu êm dịu.</li>
    <li><strong>Sàn Yoga ven hồ:</strong> Nơi bắt đầu ngày mới với những bài tập hít thở dưỡng khí trong lành.</li>
  </ul>
</div>

{contact_box}
"""
    },
    # 14. Pickleball & Thể Thao Năng Động (ID 126)
    {
        "id": 126,
        "title": "Tổ Hợp Thể Thao Pickleball, Gym & Yoga Hướng Hồ Sinh Thái",
        "excerpt": "Sân chơi Pickleball xu hướng thời thượng, phòng tập Gym kính panorama hướng hồ và đường dạo bộ xanh mát 2.5km.",
        "image": "assets/Index_asset/02_Phoi_Canh_3D/02.3D_TKCS-CANH_QUAN_VEN_HO-12.2025/SFR_11.jpg",
        "date": "29 TH8 2026",
        "content": f"""
<p>Một lối sống lành mạnh không thể thiếu vận động thể chất mỗi ngày. Saigon Farm Resort trang bị chuỗi sân thể thao tiêu chuẩn quốc tế giúp cư dân duy trì phong độ đỉnh cao.</p>

<div class="key-takeaways">
  <h3>Tiện Ích Thể Thao Hiện Đại</h3>
  <ul>
    <li>Cụm sân Pickleball tiêu chuẩn mặt sân chuyên dụng, hệ thống đèn chiếu sáng ban đêm.</li>
    <li>Phòng Gym trang bị thiết bị cao cấp nhìn trực diện ra hồ bơi và mặt hồ.</li>
    <li>Đường chạy bộ và đạp xe lát sỏi tự nhiên rợp bóng cây xanh dài hơn 2.5km bao quanh resort.</li>
  </ul>
</div>

{contact_box}
"""
    },
    # 15. Glamping & Tiệc Nướng BBQ Ven Hồ (ID 127)
    {
        "id": 127,
        "title": "Khu Cắm Trại Glamping & Tiệc Nướng BBQ Ngoài Trời Ven Nước",
        "excerpt": "Không gian kết nối yêu thương với lều trại sang trọng phong cách Bohemian, lửa trại ấm cúng và tiệc BBQ nông sản tươi ngon.",
        "image": "assets/Index_asset/02_Phoi_Canh_3D/02.3D_TKCS-CANH_QUAN_VEN_HO-12.2025/SFR_14.jpg",
        "date": "29 TH8 2026",
        "content": f"""
<p>Tận hưởng cảm giác ngủ dưới bầu trời đầy sao, lắng nghe tiếng côn trùng rả rích trong những căn lều Glamping tiện nghi như khách sạn 5 sao. Nơi ghi dấu những kỷ niệm gia đình đầm ấm và khó quên.</p>

<div class="key-takeaways">
  <h3>Điểm Nhấn Trải Nghiệm Glamping</h3>
  <ul>
    <li>Lều trại vải canvas chống thấm cao cấp trang bị đệm êm, máy lạnh và nhà vệ sinh riêng.</li>
    <li>Khu tiệc BBQ sân vườn được đầu bếp phục vụ tại chỗ với các món nướng đặc sản tươi sống.</li>
    <li>Sân khấu acoustic ngoài trời bên bếp lửa bập bùng mỗi dịp cuối tuần.</li>
  </ul>
</div>

{contact_box}
"""
    },
    # 16. Bãi Cỏ Thả Diều & Thế Giới Tuổi Thơ (ID 128)
    {
        "id": 128,
        "title": "Bãi Cỏ Thả Diều & Thế Giới Vui Chơi Trẻ Thơ Giữa Thiên Nhiên",
        "excerpt": "Hơn 5.000m² bãi cỏ xanh ngát để con trẻ thỏa thích chạy nhảy, thả diều, bắt bướm và khám phá thế giới tự nhiên kỳ thú.",
        "image": "assets/Index_asset/02_Phoi_Canh_3D/02.3D_TKCS-CANH_QUAN_VEN_HO-12.2025/SFR_15.jpg",
        "date": "29 TH8 2026",
        "content": f"""
<p>Tại Saigon Farm Resort, tuổi thơ của con trẻ không gắn liền với màn hình điện thoại hay ipad, mà là những ngày tháng chạy chân trần trên cỏ mềm, ngước nhìn cánh diều no gió bay cao giữa bầu trời xanh thẳm.</p>

<div class="key-takeaways">
  <h3>Không Gian Vui Chơi An Toàn & Lành Mạnh</h3>
  <ul>
    <li>Thảm cỏ tự nhiên êm ái, được cắt tỉa và vệ sinh định kỳ an toàn tuyệt đối.</li>
    <li>Khu vui chơi mộc bằng gỗ tự nhiên: xích đu, cầu trượt, nhà trên cây mạo hiểm.</li>
    <li>Các buổi workshop kỹ năng sinh tồn, làm đồ thủ công và tìm hiểu thế giới thực vật.</li>
  </ul>
</div>

{contact_box}
"""
    },
    # 17. News Featured: Saigon Farm Resort Chuẩn Sống Eco-Luxury (ID 202)
    {
        "id": 202,
        "title": "Saigon Farm Resort Thiết Lập Chuẩn Sống Eco-Luxury: Bản Giao Hưởng Giữa Thiên Nhiên & Tiện Nghi Thượng Lưu",
        "excerpt": "Sự kết hợp tinh tế giữa triết lý sinh thái bền vững và chuẩn mực nghỉ dưỡng xa hoa, kiến tạo không gian sống di sản truyền đời tại tọa độ vàng ven biển.",
        "image": "assets/Index_asset/02_Phoi_Canh_3D/07.3D_TKCS-SUNRISE_2_VILLA/07.3D_TKCS-NHA_GO_4_MAU_2-_02.2026/07.TKCS-NHA_GO_4-MAU_2/01.NGOAI_THAT/SFR_TONG_THE_01.jpg",
        "date": "29 TH8 2026",
        "content": f"""
<p>Trong bối cảnh đô thị hóa nhanh chóng và áp lực cuộc sống ngày càng gia tăng, giới thượng lưu đang tìm kiếm những giá trị sống đích thực: sự riêng tư, bầu không khí trong lành và sức khỏe toàn diện. <strong>Saigon Farm Resort</strong> ra đời để đáp ứng trọn vẹn khát vọng đó.</p>

<div class="pull-quote">
  "Một bất động sản thực sự giá trị không chỉ nằm ở mét vuông xây dựng, mà ở sự thảnh thơi trong tâm hồn và nguồn năng lượng dồi dào mà nó mang lại cho mỗi thành viên trong gia đình."
</div>

<h2>Kiến Trúc Tôn Trọng Bản Sắc Sinh Thái</h2>
<p>Mỗi căn biệt thự tại Saigon Farm Resort sở hữu diện tích đất rộng lớn từ 1.000m² đến 1.500m², với mật độ xây dựng dưới 25%. Hơn 75% diện tích còn lại được dành trọn cho hồ bơi riêng, thảm cỏ, vườn cây ăn trái và không gian mặt nước.</p>

<div class="key-takeaways">
  <h3>Vì Sao Saigon Farm Resort Trở Thành Tâm Điểm Thu Hút Giới Tinh Hoa?</h3>
  <ul>
    <li><strong>Vị thế độc tôn:</strong> Tựa hồ 100ha, hưởng trọn gió biển mát lành và hương đồng nội thanh bình.</li>
    <li><strong>Khoảng cách lý tưởng:</strong> Chỉ 55 phút từ TP.HCM và 25 phút từ Sân bay Quốc tế Long Thành.</li>
    <li><strong>Sở hữu di sản:</strong> Pháp lý minh bạch, sổ đỏ trao tay từng căn biệt thự.</li>
    <li><strong>Đơn vị vận hành chuyên nghiệp:</strong> MDS Living đảm bảo tài sản luôn được chăm sóc hoàn hảo và sinh lời bền vững.</li>
  </ul>
</div>

<div style="margin: 24px 0; text-align: center;">
  <img src="assets/Index_asset/02_Phoi_Canh_3D/02.3D_TKCS-CANH_QUAN_VEN_HO-12.2025/SFR_0.jpg" alt="Clubhouse Saigon Farm Resort" style="width: 100%; border-radius: 8px;">
</div>

{contact_box}
"""
    },
    # 18. News Side 1: Second Home Sinh Thái Ven Hồ (ID 1)
    {
        "id": 1,
        "title": "Second Home Sinh Thái Ven Hồ 100ha: Xu Hướng Tích Sản & Nghỉ Dưỡng Bền Vững 2026",
        "excerpt": "Phân tích sự dịch chuyển dòng vốn đầu tư tinh hoa vào phân khúc bất động sản nghỉ dưỡng sinh thái ven đô có pháp lý hoàn chỉnh và tiện ích vận hành trọn gói.",
        "image": "assets/Index_asset/Flycam/DJI_0997_2.JPG",
        "date": "29 TH8 2026",
        "content": f"""
<p>Năm 2026 chứng kiến bước ngoặt lớn trong khẩu vị đầu tư của giới tinh hoa. Những sản phẩm căn hộ hay condotel trung tâm dần nhường chỗ cho dòng sản phẩm <strong>Biệt thự vườn sinh thái ven hồ (Eco-Villa Second Home)</strong> với diện tích khuôn viên lớn từ 1.000m² trở lên.</p>

<div class="key-takeaways">
  <h3>3 Động Lực Khiến Second Home Ven Hồ Bứt Phá</h3>
  <ul>
    <li><strong>Sự hoàn thiện của hạ tầng cao tốc:</strong> Tuyến Cao tốc Biên Hòa - Vũng Tàu và Vành đai 3 giúp rút ngắn thời gian di chuyển từ TP.HCM xuống dưới 1 giờ.</li>
    <li><strong>Nhu cầu chăm sóc sức khỏe thể chất & tinh thần (Wellness Living):</strong> Xu hướng tìm về thiên nhiên để thanh lọc cơ thể sau những ngày làm việc bận rộn.</li>
    <li><strong>Tính khan hiếm của quỹ đất tựa hồ tự nhiên:</strong> Những khu đất rộng tựa hồ lớn 100ha liền kề biển ngày càng trở nên vô giá.</li>
  </ul>
</div>

<div style="margin: 24px 0;">
  <img src="assets/Index_asset/MatBang/SoDo_LienKet_Vung.png" alt="Liên kết vùng giao thông" style="width: 100%; border-radius: 8px;">
</div>

{contact_box}
"""
    },
    # 19. Company: Giới thiệu Đại Chúng Properties (ID 301)
    {
        "id": 301,
        "title": "Về Đại Chúng Properties & Đơn Vị Tiếp Thị Phân Phối Độc Quyền",
        "excerpt": "Đại Chúng Properties là thương hiệu tư vấn, tiếp thị và phân phối bất động sản nghỉ dưỡng sinh thái và cao cấp hàng đầu với triết lý phụng sự tận tâm.",
        "image": "assets/Index_asset/ceo_thinh.jpg",
        "date": "29 TH8 2026",
        "content": f"""
<p><strong>Đại Chúng Properties</strong> tự hào là Đơn vị Tổng Đại Lý Tiếp Thị & Phân Phối độc quyền cho khu nghỉ dưỡng sinh thái Saigon Farm Resort. Dưới sự dẫn dắt của CEO Huỳnh Hoàng Thịnh (Ken), chúng tôi cam kết mang lại giải pháp đầu tư và an cư thịnh vượng nhất cho quý khách hàng.</p>

<div class="key-takeaways">
  <h3>Tầm Nhìn & Giá Trị Cốt Lõi</h3>
  <ul>
    <li><strong>Tâm huyết & Minh bạch:</strong> Cung cấp thông tin chuẩn xác, pháp lý rõ ràng, bảo vệ quyền lợi tối đa của khách hàng.</li>
    <li><strong>Chuyên nghiệp & Tận tụy:</strong> Đồng hành xuyên suốt từ giai đoạn tư vấn, thủ tục công chứng, bàn giao đến vận hành khai thác tài sản.</li>
    <li><strong>Đẳng cấp & Khác biệt:</strong> Chỉ lựa chọn phân phối những sản phẩm có giá trị thực, cảnh quan độc bản và tiềm năng sinh lời vượt trội.</li>
  </ul>
</div>

<h2>Thông Tin Người Sáng Lập & Đại Diện</h2>
<p>👤 <strong>CEO Huỳnh Hoàng Thịnh (Ken)</strong> — Chuyên gia tư vấn đầu tư bất động sản cao cấp với hơn 10 năm kinh nghiệm đồng hành cùng hàng trăm nhà đầu tư tinh hoa.</p>
<p>📞 Hotline / Zalo: <a href="https://zalo.me/0906060036" target="_blank" style="color:#0068FF; font-weight:700;">0906060036</a></p>

{contact_box}
"""
    },
    # 20. Company: Tuyển Dụng (ID 302)
    {
        "id": 302,
        "title": "Cơ Hội Nghề Nghiệp: Gia Nhập Đội Ngũ Chuyên Viên Tư Vấn Bất Động Sản Nghỉ Dưỡng Triệu Đô",
        "excerpt": "Đại Chúng Properties chào đón những tài năng nhiệt huyết, có tư duy dịch vụ thượng lưu và khao khát khẳng định bản thân trong phân khúc BĐS cao cấp.",
        "image": "assets/Index_asset/02_Phoi_Canh_3D/02.3D_TKCS-CANH_QUAN_VEN_HO-12.2025/SFR_0.jpg",
        "date": "29 TH8 2026",
        "content": f"""
<p>Bạn đam mê lĩnh vực bất động sản nghỉ dưỡng cao cấp? Bạn muốn làm việc trong môi trường chuyên nghiệp với những khách hàng thượng lưu và thu nhập không giới hạn? Hãy gia nhập đội ngũ Đại Chúng Properties ngay hôm nay!</p>

<div class="key-takeaways">
  <h3>Quyền Lợi Dành Cho Bạn</h3>
  <ul>
    <li>Hoa hồng cao nhất thị trường, thanh toán nhanh chóng và minh bạch.</li>
    <li>Được đào tạo bài bản trực tiếp từ CEO Huỳnh Hoàng Thịnh về tư duy bán hàng xa xỉ và kỹ năng đàm phán cấp cao.</li>
    <li>Nguồn khách hàng tiềm năng chất lượng cao được công ty hỗ trợ liên tục.</li>
    <li>Môi trường làm việc văn minh, năng động, nhiều cơ hội thăng tiến lên cấp Quản lý / Giám đốc kinh doanh.</li>
  </ul>
</div>

<p>📩 Gửi CV hoặc liên hệ trực tiếp qua Hotline/Zalo: <strong>0906060036</strong> để đặt lịch phỏng vấn.</p>

{contact_box}
"""
    },
    # 21. Company: Báo Chí & Pháp Lý (ID 303)
    {
        "id": 303,
        "title": "Pháp Lý Vững Vàng & Chuẩn Mực Phát Triển Của Saigon Farm Resort",
        "excerpt": "Minh bạch 100% về quy hoạch và pháp lý: Sổ hồng riêng từng khuôn viên biệt thự, giấy phép xây dựng và đầy đủ phê duyệt từ cơ quan chức năng.",
        "image": "assets/Index_asset/MatBang/TongQuan_QuyMo.png",
        "date": "29 TH8 2026",
        "content": f"""
<p>Một trong những yếu tố làm nên uy tín và sức hút của Saigon Farm Resort chính là sự <strong>minh bạch và hoàn chỉnh tuyệt đối về mặt pháp lý</strong>. Mỗi gia chủ khi sở hữu biệt thự tại đây đều hoàn toàn yên tâm về giá trị gia tăng bền vững theo thời gian.</p>

<div class="key-takeaways">
  <h3>Hồ Sơ Pháp Lý Hoàn Chỉnh</h3>
  <ul>
    <li>Sổ hồng riêng sở hữu lâu dài cho từng khuôn viên đất biệt thự.</li>
    <li>Quy hoạch chi tiết đồng bộ, hạ tầng đường nội khu trải nhựa, điện âm, nước máy đạt chuẩn.</li>
    <li>Được ngân hàng uy tín thẩm định pháp lý và hỗ trợ vay vốn với lãi suất ưu đãi.</li>
  </ul>
</div>

<h2>Sơ Đồ Quy Hoạch & Quy Mô Toàn Khu</h2>
<div style="margin: 24px 0; text-align: center;">
  <img src="assets/Index_asset/MatBang/TongQuan_QuyMo.png" alt="Quy mô toàn khu Saigon Farm Resort" style="width: 100%; max-width: 800px; border-radius: 8px; border: 1px solid #333;">
</div>

{contact_box}
"""
    },
    # 22. Company: Liên Hệ & Đặt Lịch (ID 304)
    {
        "id": 304,
        "title": "Thông Tin Liên Hệ & Đăng Ký Trải Nghiệm Thực Tế Saigon Farm Resort",
        "excerpt": "Đại diện tư vấn: CEO Huỳnh Hoàng Thịnh. Hỗ trợ xe đưa đón tận nơi từ TP.HCM xuống tham quan và trải nghiệm ẩm thực ven hồ tại resort.",
        "image": "assets/Index_asset/Flycam/DJI_0007_2.JPG",
        "date": "29 TH8 2026",
        "content": f"""
<p>Kính mời Quý khách hàng và Quý nhà đầu tư cùng gia đình đến tham quan thực tế và trải nghiệm một ngày sống xanh tại <strong>Saigon Farm Resort</strong>. Chúng tôi có xe sang đưa đón tận nơi từ trung tâm TP.HCM vào tất cả các ngày trong tuần.</p>

<div class="key-takeaways">
  <h3>Chương Trình Trải Nghiệm Thực Tế Bao Gồm</h3>
  <ul>
    <li>Xe Limousine cao cấp đưa đón gia đình tận nơi (TP.HCM ↔ Saigon Farm Resort).</li>
    <li>Tham quan thực tế toàn khu, khuôn viên đất và nhà mẫu biệt thự Sunset & Sunrise.</li>
    <li>Thưởng thức bữa trưa ấm cúng với ẩm thực tươi ngon tại không gian nhà hàng ven hồ.</li>
    <li>Giới thiệu chi tiết quy hoạch, pháp lý sổ hồng và tư vấn chính sách ưu đãi trực tiếp từ Đại Chúng Properties.</li>
  </ul>
</div>

{contact_box}
"""
    }
]

# Write to data/posts.json
with open('data/posts.json', 'w', encoding='utf-8') as f:
    json.dump(posts, f, ensure_ascii=False, indent=2)

print(f"Successfully updated {len(posts)} posts with new 3D render images in data/posts.json!")
