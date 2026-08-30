import json
import os

POSTS_JSON = "data/posts.json"

new_articles = [
    # -------------------------------------------------------------
    # 1. BIỆT PHỦ & XU HƯỚNG Ở VIỆT NAM (ID: 401)
    # -------------------------------------------------------------
    {
        "id": 401,
        "title": "Biệt Phủ Điền Trang: Xu Hướng Định Vị Đẳng Cấp Sống Mới Của Tầng Lớp Tinh Hoa Việt",
        "excerpt": "Sự chuyển dịch từ những căn penthouse hào nhoáng nơi phố thị nén sang không gian biệt phủ điền trang 1.000m² - 1.500m² ven hồ tự nhiên 100ha: Khi đỉnh cao của sự xa xỉ là diện tích mảng xanh và sự an yên tuyệt đối.",
        "image": "assets/posts/chuyen_de/401_biet_phu_xu_huong.jpg",
        "date": "31 TH8 2026",
        "author": "Ban Nghiên Cứu Phát Triển & Xu Hướng Thị Trường • Đại Chúng Properties",
        "category": "Xu Hướng Điền Trang",
        "content": """
<article class="article-detail" style="font-family: var(--font-sans); color: #2c2c2c; line-height: 1.85; max-width: 900px; margin: 0 auto;">

  <div class="article-meta-header" style="border-bottom: 2px solid #c9a96e; padding-bottom: 22px; margin-bottom: 30px;">
    <div style="display: flex; gap: 10px; align-items: center; margin-bottom: 12px; flex-wrap: wrap;">
      <span style="background: #c9a96e; color: #000; font-size: 0.75rem; font-weight: 800; padding: 4px 12px; border-radius: 4px; letter-spacing: 0.05em; text-transform: uppercase;">XU HƯỚNG ĐIỀN TRANG</span>
      <span style="background: #f0ebe1; color: #666; font-size: 0.75rem; font-weight: 600; padding: 4px 10px; border-radius: 4px;">Phong Cách Sống Thượng Lưu</span>
      <span style="color: #888; font-size: 0.82rem;"><i class="fa-regular fa-clock" style="margin-right: 4px;"></i> Thời gian đọc: 8-10 phút (1.500+ từ)</span>
    </div>
    <h1 style="font-family: var(--font-serif); font-size: clamp(1.8rem, 3.5vw, 2.4rem); color: #111; line-height: 1.35; margin: 0 0 14px;">
      Biệt Phủ Điền Trang: Xu Hướng Định Vị Đẳng Cấp Sống Mới Của Tầng Lớp Tinh Hoa Việt
    </h1>
    <p style="font-size: 1.1rem; color: #555; font-style: italic; margin: 0; line-height: 1.6;">
      Khi đỉnh cao của sự thịnh vượng không còn đo đếm bằng những khối bê tông chọc trời, mà được khẳng định bằng chiều rộng của đất, độ tĩnh lặng của mặt nước và chiều sâu của di sản gia tộc.
    </p>
  </div>

  <figure style="margin: 0 0 32px; border-radius: 10px; overflow: hidden; box-shadow: 0 8px 24px rgba(0,0,0,0.12); border: 1px solid #e0d5c1;">
    <img src="assets/posts/chuyen_de/401_biet_phu_xu_huong.jpg" alt="Biệt phủ điền trang sinh thái ven hồ" style="width: 100%; height: auto; max-height: 480px; object-fit: cover; display: block;" loading="lazy">
    <figcaption style="padding: 10px 16px; background: #fdfbf7; font-size: 0.8rem; color: #777; font-style: italic; border-top: 1px solid #eee; text-align: right;">
      * Không gian biệt phủ điền trang đương đại tựa hồ sinh thái tại Saigon Farm Resort.
    </figcaption>
  </figure>

  <div style="background: #fcf9f2; border-left: 4px solid #c9a96e; padding: 22px 24px; border-radius: 0 8px 8px 0; margin-bottom: 35px; box-shadow: 0 4px 16px rgba(201,169,110,0.08);">
    <h4 style="font-family: var(--font-serif); color: #8a6d3b; font-size: 1.15rem; margin: 0 0 10px; display: flex; align-items: center; gap: 8px;">
      <i class="fa-solid fa-compass" style="color: #c9a96e;"></i> TỔNG QUAN XU HƯỚNG BẤT ĐỘNG SẢN TINH HOA
    </h4>
    <p style="margin: 0 0 10px; font-size: 0.96rem; color: #444; line-height: 1.65;">
      Bài viết phân tích sự chuyển dịch mang tính bước ngoặt của giới thượng lưu Việt: từ những căn hộ penthouse nội đô sang mô hình biệt phủ điền trang sinh thái (Eco-Estate) rộng 1.000m² – 1.500m², nơi kết hợp hoàn mỹ giữa tiện nghi resort 5 sao và không gian thiên nhiên nguyên bản.
    </p>
  </div>

  <h2 style="font-family: var(--font-serif); color: #111; font-size: 1.55rem; margin: 36px 0 16px; padding-bottom: 8px; border-bottom: 1px solid #e0d5c1;">
    1. Nghịch Lý Của Đô Thị Nén & Cơn Khát Không Gian Xanh Nguyên Bản
  </h2>
  <p style="font-size: 1rem; margin-bottom: 18px; text-align: justify;">
    Trong hai thập niên qua, định nghĩa về sự giàu có tại Việt Nam thường gắn liền với những căn biệt thự nguy nga trong các khu đô thị khép kín, hoặc những căn penthouse triệu đô tọa lạc trên tầng mây trung tâm TP. Hồ Chí Minh hay Hà Nội. Đó là giai đoạn mà sự sang trọng đồng nghĩa với vị trí đắc địa, ánh đèn rực rỡ và những thương hiệu nội thất đắt đỏ nhập khẩu từ châu Âu.
  </p>
  <p style="font-size: 1rem; margin-bottom: 18px; text-align: justify;">
    Thế nhưng, khi nền kinh tế bước vào giai đoạn phát triển trưởng thành, một nghịch lý lớn đã lộ diện: <strong>Càng thành đạt, con người lại càng bị giam cầm trong những khối bê tông chật hẹp</strong>. Bụi mịn PM2.5, tiếng còi xe inh ỏi, sự thiếu vắng mảng xanh tự nhiên và nhịp sống áp lực liên tục đã đẩy thể chất lẫn tinh thần của tầng lớp doanh nhân vào tình trạng quá tải. Một căn nhà phố vài trăm mét vuông hay một căn hộ cao tầng dù xa hoa đến đâu cũng không thể mang lại cảm giác được chạm tay vào đất mẹ, được hít thở bầu không khí tinh khôi mỗi sớm mai hay ngắm nhìn mặt nước hồ trải dài vô tận.
  </p>

  <blockquote style="border-left: 3px solid #8a6d3b; margin: 30px 0; padding: 16px 24px; background: #faf7f2; font-style: italic; color: #444; font-size: 1.05rem; line-height: 1.7;">
    "Sự xa xỉ tột cùng của thời đại mới không phải là một chiếc đồng hồ nạm kim cương hay một căn phòng dát vàng, mà là quyền năng sở hữu một khoảng trời khoáng đạt, một mặt hồ tự nhiên và không gian sống hoàn toàn không có tiếng ồn phố thị."
    <footer style="margin-top: 8px; font-size: 0.85rem; color: #8a6d3b; font-weight: 700; text-align: right;">— Triết Lý Phát Triển Đại Chúng Properties</footer>
  </blockquote>

  <h2 style="font-family: var(--font-serif); color: #111; font-size: 1.55rem; margin: 36px 0 16px; padding-bottom: 8px; border-bottom: 1px solid #e0d5c1;">
    2. Sự Trỗi Dậy Của Biệt Phủ Điền Trang (Eco-Estate) Tại Việt Nam
  </h2>
  <p style="font-size: 1rem; margin-bottom: 18px; text-align: justify;">
    Nhìn ra thế giới, xu hướng sở hữu điền trang ngoại ô (Country Estate) đã là chuẩn mực khẳng định vị thế của các gia tộc quý tộc Anh, các tài phiệt phố Wall hay giới quý tộc Pháp qua nhiều thế kỷ. Tại Việt Nam, làn sóng này đang bùng nổ mạnh mẽ với tên gọi <strong>Biệt Phủ Điền Trang Sinh Thái</strong>.
  </p>
  <p style="font-size: 1rem; margin-bottom: 18px; text-align: justify;">
    Không đơn thuần là một ngôi nhà vườn để về nghỉ cuối tuần, biệt phủ điền trang là một quần thể kiến trúc nghỉ dưỡng hoàn chỉnh tọa lạc trên khuôn viên đất rộng lớn từ <strong>1.000m² đến 1.500m²</strong>. Ở đó, mật độ xây dựng chỉ chiếm từ 18% đến 25%, nhường hơn 75% diện tích còn lại cho vườn cây ăn trái, mặt nước hồ bơi khoáng muối, lối dạo bộ thiền hành và thảm cỏ xanh mướt. Đây là nơi chủ nhân tìm về để thanh lọc tâm trí, tái tạo năng lượng sáng tạo và kết nối sâu sắc với người thân.
  </p>

  <div style="overflow-x: auto; margin: 28px 0;">
    <table style="width: 100%; border-collapse: collapse; font-size: 0.92rem; text-align: left; background: #fff; border: 1px solid #e0d5c1; border-radius: 6px; overflow: hidden; box-shadow: 0 4px 14px rgba(0,0,0,0.04);">
      <thead>
        <tr style="background: #f5f0e8; color: #111; border-bottom: 2px solid #c9a96e;">
          <th style="padding: 12px 16px; font-weight: 700;">TIÊU CHÍ SO SÁNH</th>
          <th style="padding: 12px 16px; font-weight: 700;">PENTHOUSE / BIỆT THỰ PHỐ ĐÔ THỊ</th>
          <th style="padding: 12px 16px; font-weight: 700;">BIỆT PHỦ ĐIỀN TRANG SAIGON FARM RESORT</th>
        </tr>
      </thead>
      <tbody>
        <tr style="border-bottom: 1px solid #f0ebe1;">
          <td style="padding: 12px 16px; font-weight: 600; color: #333;">Quy mô khuôn viên</td>
          <td style="padding: 12px 16px; color: #666;">200m² – 500m² (Diện tích hạn hẹp)</td>
          <td style="padding: 12px 16px; color: #2e7d32; font-weight: 600;">1.000m² – 1.500m² (Sổ hồng riêng từng nền)</td>
        </tr>
        <tr style="border-bottom: 1px solid #f0ebe1; background: #fdfbf7;">
          <td style="padding: 12px 16px; font-weight: 600; color: #333;">Cảnh quan & Mặt nước</td>
          <td style="padding: 12px 16px; color: #666;">Bê tông vây quanh, hồ bơi nhân tạo nhỏ</td>
          <td style="padding: 12px 16px; color: #2e7d32; font-weight: 600;">Trực diện mặt hồ tự nhiên 100ha, đồng lúa & vườn cây</td>
        </tr>
        <tr style="border-bottom: 1px solid #f0ebe1;">
          <td style="padding: 12px 16px; font-weight: 600; color: #333;">Chất lượng sống & Sức khỏe</td>
          <td style="padding: 12px 16px; color: #666;">Bụi mịn đô thị, tiếng ồn liên tục</td>
          <td style="padding: 12px 16px; color: #2e7d32; font-weight: 600;">Không khí ion âm dồi dào, thực phẩm Organic vườn nhà</td>
        </tr>
        <tr style="border-bottom: 1px solid #f0ebe1; background: #fdfbf7;">
          <td style="padding: 12px 16px; font-weight: 600; color: #333;">Giá trị truyền đời</td>
          <td style="padding: 12px 16px; color: #666;">Khấu hao công trình theo thời gian</td>
          <td style="padding: 12px 16px; color: #2e7d32; font-weight: 600;">Quỹ đất sinh thái ven hồ ngày càng khan hiếm, truyền đời gia tộc</td>
        </tr>
      </tbody>
    </table>
  </div>

  <h2 style="font-family: var(--font-serif); color: #111; font-size: 1.55rem; margin: 36px 0 16px; padding-bottom: 8px; border-bottom: 1px solid #e0d5c1;">
    3. Saigon Farm Resort – Chuẩn Mực Điền Trang Bản Sắc Việt Ven Sài Gòn
  </h2>
  <p style="font-size: 1rem; margin-bottom: 18px; text-align: justify;">
    Tọa lạc tại vùng đất Đất Đỏ – Liền kề cung đường biển Hồ Tràm thơ mộng, <strong>Saigon Farm Resort</strong> tiên phong kiến tạo một quần thể biệt phủ điền trang sinh thái quy mô bậc nhất khu vực phía Nam. Dự án chỉ cách TP.HCM 90 phút di chuyển qua Cao tốc Biên Hòa – Vũng Tàu và Sân bay Quốc tế Long Thành.
  </p>
  <p style="font-size: 1rem; margin-bottom: 18px; text-align: justify;">
    Mỗi căn biệt phủ Sunrise và Sunset tại đây được thiết kế theo ngôn ngữ kiến trúc thuần Việt đương đại: mái ngói đất nung truyền thống, cột gỗ mộc sang trọng kết hợp cùng hệ vách kính Low-E tràn viền mở toang tầm nhìn ra mặt nước 100ha. Tại đây, gia chủ được tận hưởng hệ sinh thái tiện ích quản gia 5 sao từ <strong>MDS Living</strong>: từ dịch vụ đầu bếp riêng, chăm sóc vườn cây, hồ bơi điện phân khoáng muối đến câu lạc bộ cưỡi ngựa quý tộc Việt Mã Trang và bến thuyền kayak dạo hồ.
  </p>

  <h2 style="font-family: var(--font-serif); color: #111; font-size: 1.55rem; margin: 36px 0 16px; padding-bottom: 8px; border-bottom: 1px solid #e0d5c1;">
    4. Lời Kết: Ngôi Nhà Là Di Sản Tinh Thần Trường Tồn
  </h2>
  <p style="font-size: 1rem; margin-bottom: 24px; text-align: justify;">
    Tiền tài và danh vọng có thể đến rồi đi theo những biến động của thị trường, nhưng một mảnh đất điền trang ngập tràn bóng mát, nơi lưu giữ tiếng cười của ba thế hệ sum vầy và những ký ức tuổi thơ êm đềm của con trẻ, sẽ mãi là tài sản vô giá trường tồn cùng thời gian. Biệt phủ điền trang tại Saigon Farm Resort không chỉ là một khoản đầu tư tài chính thông minh, mà là biểu tượng danh giá của phong cách sống tự do, thịnh vượng và an nhiên đích thực.
  </p>

  <div style="background: #111; color: #fff; padding: 28px; border-radius: 8px; border-left: 4px solid #c9a96e; margin-top: 30px;">
    <h4 style="margin-bottom: 8px; font-family: var(--font-serif); font-size: 1.25rem; color: #c9a96e;">TỔNG ĐẠI LÝ TIẾP THỊ & PHÂN PHỐI: ĐẠI CHÚNG PROPERTIES</h4>
    <p style="margin-bottom: 6px; font-size: 0.95rem;">🏢 <strong>Phòng Kinh Doanh & Tư Vấn Dự Án:</strong> Saigon Farm Resort</p>
    <p style="margin-bottom: 14px; font-size: 0.95rem;">📞 <strong>Hotline / Zalo Tiếp Nhận Thông Tin:</strong> <a href="https://zalo.me/0906060036" target="_blank" style="color:#0068FF; font-weight:700; text-decoration:underline;">0906060036</a></p>
    <a href="https://zalo.me/0906060036" target="_blank" style="display: inline-flex; align-items: center; gap: 8px; background: #0068FF; color: #fff; padding: 12px 24px; border-radius: 4px; font-weight: 700; text-decoration: none;">
      <i class="fa-solid fa-comment-dots"></i> Nhắn Zalo Nhận Bảng Giá & Đặt Lịch Trải Nghiệm
    </a>
  </div>

  <div style="border-top: 1px solid #e0d5c1; padding-top: 20px; margin-top: 40px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 14px;">
    <div>
      <span style="font-size: 0.85rem; color: #888; display: block;">Tác giả chuyên đề:</span>
      <strong style="color: #111; font-size: 0.95rem;">Ban Nghiên Cứu Phát Triển & Xu Hướng Thị Trường • Đại Chúng Properties</strong>
    </div>
    <div style="display: flex; gap: 10px;">
      <a href="index.html#tabs-section" class="editorial-btn" style="padding: 8px 16px; font-size: 0.82rem; text-decoration: none;">
        ← Về Danh Mục Chuyên Đề
      </a>
      <a href="https://zalo.me/0906060036" target="_blank" class="editorial-btn" style="padding: 8px 16px; font-size: 0.82rem; background: #0068FF; color: #fff; border-color: #0068FF; text-decoration: none;">
        Tư Vấn Trực Tiếp (Zalo)
      </a>
    </div>
  </div>

</article>
"""
    },

    # -------------------------------------------------------------
    # 2. LÚA TRONG VAI TRÒ CUỘC SỐNG TINH THẦN VÀ VĂN HÓA NGƯỜI VIỆT (ID: 402)
    # -------------------------------------------------------------
    {
        "id": 402,
        "title": "Hạt Lúa & Đồng Quê: Linh Hồn Cuộc Sống Tinh Thần Và Văn Hóa Trường Tồn Của Người Việt",
        "excerpt": "Từ cội nguồn nền văn minh lúa nước bốn nghìn năm đến biểu tượng của sự khiêm nhường, tình nghĩa thủy chung và sự chữa lành tâm hồn cho người hiện đại giữa nhịp sống đô thị gấp gáp.",
        "image": "assets/posts/chuyen_de/402_hat_lua_dong_que.jpg",
        "date": "31 TH8 2026",
        "author": "Hội Đồng Cố Vấn Văn Hóa & Di Sản • Saigon Farm Resort",
        "category": "Văn Hóa & Bản Sắc",
        "content": """
<article class="article-detail" style="font-family: var(--font-sans); color: #2c2c2c; line-height: 1.85; max-width: 900px; margin: 0 auto;">

  <div class="article-meta-header" style="border-bottom: 2px solid #c9a96e; padding-bottom: 22px; margin-bottom: 30px;">
    <div style="display: flex; gap: 10px; align-items: center; margin-bottom: 12px; flex-wrap: wrap;">
      <span style="background: #c9a96e; color: #000; font-size: 0.75rem; font-weight: 800; padding: 4px 12px; border-radius: 4px; letter-spacing: 0.05em; text-transform: uppercase;">DI SẢN VĂN HÓA</span>
      <span style="background: #f0ebe1; color: #666; font-size: 0.75rem; font-weight: 600; padding: 4px 10px; border-radius: 4px;">Văn Minh Lúa Nước</span>
      <span style="color: #888; font-size: 0.82rem;"><i class="fa-regular fa-clock" style="margin-right: 4px;"></i> Thời gian đọc: 8-10 phút (1.500+ từ)</span>
    </div>
    <h1 style="font-family: var(--font-serif); font-size: clamp(1.8rem, 3.5vw, 2.4rem); color: #111; line-height: 1.35; margin: 0 0 14px;">
      Hạt Lúa & Đồng Quê: Linh Hồn Cuộc Sống Tinh Thần Và Văn Hóa Trường Tồn Của Người Việt
    </h1>
    <p style="font-size: 1.1rem; color: #555; font-style: italic; margin: 0; line-height: 1.6;">
      "Hạt gạo làng ta, có vị phù sa, có hương sen thơm..." — Cây lúa không chỉ nuôi sống thể xác người Việt qua hàng nghìn năm, mà là căn tính tâm hồn, là bài học đạo đức và nguồn cảm hứng bất tận của triết lý sống an nhiên.
    </p>
  </div>

  <figure style="margin: 0 0 32px; border-radius: 10px; overflow: hidden; box-shadow: 0 8px 24px rgba(0,0,0,0.12); border: 1px solid #e0d5c1;">
    <img src="assets/posts/chuyen_de/402_hat_lua_dong_que.jpg" alt="Đồng lúa chín vàng óng mùa gặt tại Việt Nam" style="width: 100%; height: auto; max-height: 480px; object-fit: cover; display: block;" loading="lazy">
    <figcaption style="padding: 10px 16px; background: #fdfbf7; font-size: 0.8rem; color: #777; font-style: italic; border-top: 1px solid #eee; text-align: right;">
      * Cánh đồng lúa vàng óng ả gợi mở cảm thức bình yên và no ấm trong tâm hồn người Việt.
    </figcaption>
  </figure>

  <div style="background: #fcf9f2; border-left: 4px solid #c9a96e; padding: 22px 24px; border-radius: 0 8px 8px 0; margin-bottom: 35px; box-shadow: 0 4px 16px rgba(201,169,110,0.08);">
    <h4 style="font-family: var(--font-serif); color: #8a6d3b; font-size: 1.15rem; margin: 0 0 10px; display: flex; align-items: center; gap: 8px;">
      <i class="fa-solid fa-seedling" style="color: #c9a96e;"></i> Ý NGHĨA VĂN HÓA CỦA CÂY LÚA
    </h4>
    <p style="margin: 0 0 10px; font-size: 0.96rem; color: #444; line-height: 1.65;">
      Bài viết đào sâu vai trò của cây lúa trong đời sống tâm thức người Việt: từ nguồn gốc bánh Chưng bánh Giầy thuở vua Hùng, triết lý "Lúa chín cúi đầu", đến sự xuất hiện của những thửa ruộng hữu cơ trong không gian điền trang nghỉ dưỡng cao cấp như một liệu pháp chữa lành tự nhiên.
    </p>
  </div>

  <h2 style="font-family: var(--font-serif); color: #111; font-size: 1.55rem; margin: 36px 0 16px; padding-bottom: 8px; border-bottom: 1px solid #e0d5c1;">
    1. Cội Nguồn Văn Minh Lúa Nước & Căn Tính Của Con Người Việt
  </h2>
  <p style="font-size: 1rem; margin-bottom: 18px; text-align: justify;">
    Nếu phương Tây hình thành trên nền văn minh săn bắn và du mục với tính cách chinh phục, thì phương Đông và đặc biệt là dải đất Việt Nam lại khởi nguồn từ nền văn minh lúa nước ngàn đời. Cây lúa gắn liền với giọt mồ hôi của người nông dân một nắng hai sương, phụ thuộc vào mưa thuận gió hòa và sự bao dung của trời đất.
  </p>
  <p style="font-size: 1rem; margin-bottom: 18px; text-align: justify;">
    Từ truyền thuyết Lang Liêu dùng gạo nếp gói bánh Chưng vuông tượng trưng cho Đất, bánh Giầy tròn tượng trưng cho Trời để dâng lên Vua Hùng, hạt gạo đã vượt qua khái niệm một loại lương thực thông thường để trở thành <strong>Hạt Ngọc Trời (Ngọc Thực)</strong>. Nó chuyên chở lòng biết ơn tiền nhân, sự tôn kính tổ tiên và triết lý sống hòa hợp giữa con người với vũ trụ tự nhiên.
  </p>

  <h2 style="font-family: var(--font-serif); color: #111; font-size: 1.55rem; margin: 36px 0 16px; padding-bottom: 8px; border-bottom: 1px solid #e0d5c1;">
    2. Triết Lý Sống Từ Cây Lúa: "Bông Lúa Chín Là Bông Lúa Cúi Đầu"
  </h2>
  <p style="font-size: 1rem; margin-bottom: 18px; text-align: justify;">
    Người xưa thường dạy: <em>"Lúa trổ đòng thì vươn thẳng, nhưng khi đã trĩu hạt căng tròn thì cúi đầu khiêm nhường."</em> Đây chính là bài học đạo đức sâu sắc nhất về cốt cách của người quân tử và tầng lớp trí thức tinh hoa. Người càng có hiểu biết uyên bác, tích lũy được nhiều tài sản và danh vọng trong xã hội lại càng phải giữ thái độ khiêm tốn, biết trân trọng những người bình dị xung quanh và tri ân cội nguồn đã nâng đỡ mình.
  </p>
  <p style="font-size: 1rem; margin-bottom: 18px; text-align: justify;">
    Hương lúa non thoang thoảng mỗi mùa trổ đòng, tiếng rơm rạ khô giòn tan trong nắng chiều và mâm cơm gạo mới dẻo thơm ngát khói là liều thuốc xoa dịu mọi vết thương tâm hồn của người thành đạt sau những tháng ngày bôn ba thương trường.
  </p>

  <div style="background: #faf7f2; border: 1px solid #e0d5c1; border-radius: 8px; padding: 22px; margin: 28px 0;">
    <h4 style="font-family: var(--font-serif); color: #8a6d3b; margin: 0 0 12px; font-size: 1.1rem;">🌾 Ca Dao Việt Nam Về Hạt Gạo & Nghĩa Tình Đồng Quê:</h4>
    <p style="font-style: italic; color: #555; font-size: 0.98rem; margin: 0; line-height: 1.7;">
      "Cày đồng đang buổi ban trưa,<br>
      Mồ hôi thánh thót như mưa ruộng cày.<br>
      Ai ơi bưng bát cơm đầy,<br>
      Dẻo thơm một hạt đắng cay muôn phần."
    </p>
  </div>

  <h2 style="font-family: var(--font-serif); color: #111; font-size: 1.55rem; margin: 36px 0 16px; padding-bottom: 8px; border-bottom: 1px solid #e0d5c1;">
    3. Đưa Cánh Đồng Lúa Vào Kiến Trúc Nghỉ Dưỡng: Liệu Pháp Chữa Lành Tại Saigon Farm Resort
  </h2>
  <p style="font-size: 1rem; margin-bottom: 18px; text-align: justify;">
    Tại <strong>Saigon Farm Resort</strong>, đồng lúa không phải là một chi tiết trang trí ngẫu nhiên, mà được quy hoạch thành một phân khu cảnh quan nông nghiệp sinh thái rộng lớn, hòa quyện bên bờ hồ 100ha và bao quanh hệ thống điền trang biệt phủ.
  </p>
  <p style="font-size: 1rem; margin-bottom: 18px; text-align: justify;">
    Mỗi buổi chiều hoàng hôn, khi gió từ mặt nước hồ thổi qua ngọn lúa đang thì con gái, cả không gian dậy lên mùi hương thanh khiết, ngào ngạt của đất trời. Cư dân và du khách có thể ngồi thưởng trà dưới mái hiên nhà, tham gia <strong>Lễ hội Mùa Gặt</strong> cùng gia đình, tự tay gặt những bó lúa trĩu hạt và thưởng thức món xôi nếp mới dẻo thơm bên ánh lửa bập bùng.
  </p>

  <h2 style="font-family: var(--font-serif); color: #111; font-size: 1.55rem; margin: 36px 0 16px; padding-bottom: 8px; border-bottom: 1px solid #e0d5c1;">
    4. Lời Kết: Trở Về Với Hạt Gạo Quê Nhà Để Tìm Lại Sự An Nhiên
  </h2>
  <p style="font-size: 1rem; margin-bottom: 24px; text-align: justify;">
    Dù đi khắp bốn phương trời, thưởng thức sơn hào hải vị của năm châu bốn bể, trong sâu thẳm tâm thức mỗi người Việt vẫn luôn khao khát một bữa cơm quê đầm ấm với bát cơm gạo mới, đĩa rau muống luộc chấm tương và con cá bống kho tiêu dưới mái nhà ấm áp. Giữ gìn hình ảnh cánh đồng lúa giữa lòng một khu nghỉ dưỡng cao cấp chính là cách chúng ta giữ gìn linh hồn dân tộc, nuôi dưỡng lòng nhân ái cho thế hệ con cháu tương lai.
  </p>

  <div style="background: #111; color: #fff; padding: 28px; border-radius: 8px; border-left: 4px solid #c9a96e; margin-top: 30px;">
    <h4 style="margin-bottom: 8px; font-family: var(--font-serif); font-size: 1.25rem; color: #c9a96e;">TỔNG ĐẠI LÝ TIẾP THỊ & PHÂN PHỐI: ĐẠI CHÚNG PROPERTIES</h4>
    <p style="margin-bottom: 6px; font-size: 0.95rem;">🏢 <strong>Phòng Kinh Doanh & Tư Vấn Dự Án:</strong> Saigon Farm Resort</p>
    <p style="margin-bottom: 14px; font-size: 0.95rem;">📞 <strong>Hotline / Zalo Tiếp Nhận Thông Tin:</strong> <a href="https://zalo.me/0906060036" target="_blank" style="color:#0068FF; font-weight:700; text-decoration:underline;">0906060036</a></p>
    <a href="https://zalo.me/0906060036" target="_blank" style="display: inline-flex; align-items: center; gap: 8px; background: #0068FF; color: #fff; padding: 12px 24px; border-radius: 4px; font-weight: 700; text-decoration: none;">
      <i class="fa-solid fa-comment-dots"></i> Nhắn Zalo Nhận Bảng Giá & Đặt Lịch Trải Nghiệm
    </a>
  </div>

  <div style="border-top: 1px solid #e0d5c1; padding-top: 20px; margin-top: 40px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 14px;">
    <div>
      <span style="font-size: 0.85rem; color: #888; display: block;">Tác giả chuyên đề:</span>
      <strong style="color: #111; font-size: 0.95rem;">Hội Đồng Cố Vấn Văn Hóa & Di Sản • Saigon Farm Resort</strong>
    </div>
    <div style="display: flex; gap: 10px;">
      <a href="index.html#tabs-section" class="editorial-btn" style="padding: 8px 16px; font-size: 0.82rem; text-decoration: none;">
        ← Về Danh Mục Chuyên Đề
      </a>
      <a href="https://zalo.me/0906060036" target="_blank" class="editorial-btn" style="padding: 8px 16px; font-size: 0.82rem; background: #0068FF; color: #fff; border-color: #0068FF; text-decoration: none;">
        Tư Vấn Trực Tiếp (Zalo)
      </a>
    </div>
  </div>

</article>
"""
    },

    # -------------------------------------------------------------
    # 3. XU HƯỚNG SỐNG TỰ NHIÊN, XA XỈ VỚI BẢN SẮC VIỆT (ID: 403)
    # -------------------------------------------------------------
    {
        "id": 403,
        "title": "Sống Tự Nhiên & Xa Xỉ Bản Sắc: Khi Đẳng Cấp Thượng Lưu Là Trở Về Với Cội Nguồn Dân Tộc",
        "excerpt": "Định nghĩa lại sự xa xỉ trong kỷ nguyên mới: Không cần vay mượn hình bóng Tuscany hay Kyoto, sự sang trọng đích thực của người Việt nằm ở việc nâng tầm vật liệu mộc mạc, hàng hiên đón gió và chiều sâu văn hóa truyền đời.",
        "image": "assets/posts/chuyen_de/403_xa_xi_ban_sac.jpg",
        "date": "31 TH8 2026",
        "author": "Hội Đồng Kiến Trúc & Văn Hóa MDS Living",
        "category": "Phong Cách Sống",
        "content": """
<article class="article-detail" style="font-family: var(--font-sans); color: #2c2c2c; line-height: 1.85; max-width: 900px; margin: 0 auto;">

  <div class="article-meta-header" style="border-bottom: 2px solid #c9a96e; padding-bottom: 22px; margin-bottom: 30px;">
    <div style="display: flex; gap: 10px; align-items: center; margin-bottom: 12px; flex-wrap: wrap;">
      <span style="background: #c9a96e; color: #000; font-size: 0.75rem; font-weight: 800; padding: 4px 12px; border-radius: 4px; letter-spacing: 0.05em; text-transform: uppercase;">TRIẾT LÝ SỐNG</span>
      <span style="background: #f0ebe1; color: #666; font-size: 0.75rem; font-weight: 600; padding: 4px 10px; border-radius: 4px;">Eco-Heritage Luxury</span>
      <span style="color: #888; font-size: 0.82rem;"><i class="fa-regular fa-clock" style="margin-right: 4px;"></i> Thời gian đọc: 8-10 phút (1.500+ từ)</span>
    </div>
    <h1 style="font-family: var(--font-serif); font-size: clamp(1.8rem, 3.5vw, 2.4rem); color: #111; line-height: 1.35; margin: 0 0 14px;">
      Sống Tự Nhiên & Xa Xỉ Bản Sắc: Khi Đẳng Cấp Thượng Lưu Là Trở Về Với Cội Nguồn Dân Tộc
    </h1>
    <p style="font-size: 1.1rem; color: #555; font-style: italic; margin: 0; line-height: 1.6;">
      Sự xa xỉ đỉnh cao không nằm ở việc khoác lên mình những lớp áo ngoại lai, mà là sự tự tin bước ra thế giới với niềm kiêu hãnh về kiến trúc, văn hóa và nếp sống của dân tộc mình.
    </p>
  </div>

  <figure style="margin: 0 0 32px; border-radius: 10px; overflow: hidden; box-shadow: 0 8px 24px rgba(0,0,0,0.12); border: 1px solid #e0d5c1;">
    <img src="assets/posts/chuyen_de/403_xa_xi_ban_sac.jpg" alt="Hiên trà sen thanh tịnh bên hồ nước sớm mai" style="width: 100%; height: auto; max-height: 480px; object-fit: cover; display: block;" loading="lazy">
    <figcaption style="padding: 10px 16px; background: #fdfbf7; font-size: 0.8rem; color: #777; font-style: italic; border-top: 1px solid #eee; text-align: right;">
      * Hiên trà gỗ mộc ngắm hồ sen sớm mai — Nét xa xỉ thâm trầm, sâu lắng đậm chất Việt.
    </figcaption>
  </figure>

  <div style="background: #fcf9f2; border-left: 4px solid #c9a96e; padding: 22px 24px; border-radius: 0 8px 8px 0; margin-bottom: 35px; box-shadow: 0 4px 16px rgba(201,169,110,0.08);">
    <h4 style="font-family: var(--font-serif); color: #8a6d3b; font-size: 1.15rem; margin: 0 0 10px; display: flex; align-items: center; gap: 8px;">
      <i class="fa-solid fa-gem" style="color: #c9a96e;"></i> TÁI ĐỊNH NGHĨA SỰ SANG TRỌNG (ECO-HERITAGE LUXURY)
    </h4>
    <p style="margin: 0 0 10px; font-size: 0.96rem; color: #444; line-height: 1.65;">
      Bài viết làm sáng tỏ cuộc cách mạng tư duy thẩm mỹ của giới thượng lưu Việt Nam: Từ việc phô trương vật chất ngoại nhập chuyển sang trân trọng các giá trị văn hóa bản địa, đề cao sự tinh tế của chất liệu thủ công truyền thống và lối sống hòa hợp cùng thiên nhiên.
    </p>
  </div>

  <h2 style="font-family: var(--font-serif); color: #111; font-size: 1.55rem; margin: 36px 0 16px; padding-bottom: 8px; border-bottom: 1px solid #e0d5c1;">
    1. Sự Thoái Trào Của Trào Lưu Vay Mượn Văn Hóa Ngoại Lai
  </h2>
  <p style="font-size: 1rem; margin-bottom: 18px; text-align: justify;">
    Trong một thời gian dài, khi thị trường bất động sản cao cấp bắt đầu hình thành, người mua nhà thường bị thu hút bởi những tên gọi và phong cách mang đậm màu sắc phương Tây: "Biệt thự phong cách Địa Trung Hải", "Lâu đài Tân cổ điển Pháp", "Làng cổ Tuscany" hay "Khu nghỉ dưỡng phong cách Kyoto Nhật Bản". Điều này phản ánh tâm lý sùng bái chuẩn mực quốc tế của một giai đoạn phát triển ban đầu.
  </p>
  <p style="font-size: 1rem; margin-bottom: 18px; text-align: justify;">
    Tuy nhiên, khi chủ nhân của những bất động sản này là những doanh nhân từng đi khắp năm châu bốn bể, họ nhận ra một sự thật: <em>Một căn biệt thự Tuscany ở Việt Nam sẽ không bao giờ có được cái hồn của nước Ý, và một ngôi nhà phong cách Kyoto đặt giữa khí hậu nhiệt đới gió mùa sẽ sớm bộc lộ sự bất hợp lý về công năng lẫn vi khí hậu.</em> Đã đến lúc chúng ta tự hào kiến tạo nên những công trình mang dấu ấn của người Việt, phục vụ cho thói quen và cảm xúc của người Việt.
  </p>

  <h2 style="font-family: var(--font-serif); color: #111; font-size: 1.55rem; margin: 36px 0 16px; padding-bottom: 8px; border-bottom: 1px solid #e0d5c1;">
    2. Bốn Trụ Cột Định Hình Phong Cách "Xa Xỉ Bản Sắc"
  </h2>
  <ul style="padding-left: 24px; margin-bottom: 24px; font-size: 0.98rem; line-height: 1.8; color: #444;">
    <li style="margin-bottom: 10px;">
      <strong>Vật liệu bản địa được chế tác thượng thừa:</strong> Gỗ tự nhiên được xử lý chống ẩm cong vênh, đá bazan chẻ tay, ngói đất nung giữ nhiệt, gốm men lam Bát Tràng và mây tre đan thủ công tinh xảo.
    </li>
    <li style="margin-bottom: 10px;">
      <strong>Không gian mở giao hòa với tự nhiên:</strong> Hàng hiên rộng 30m² - 50m² che mát nắng nhiệt đới, sân trong (Courtyard) đón gió đối lưu từ mặt hồ 100ha, tạo vi khí hậu mát mẻ tự nhiên mà không phụ thuộc vào điều hòa máy lạnh.
    </li>
    <li style="margin-bottom: 10px;">
      <strong>Trải nghiệm văn hóa sống động:</strong> Bàn trà đạo thuần khiết, tiếng đàn tranh ngân nga buổi chiều tà, bữa cơm gia đình với cá sông rau vườn sạch.
    </li>
    <li style="margin-bottom: 10px;">
      <strong>Tiêu chuẩn vận hành 5 sao chuẩn quốc tế:</strong> Hòa quyện mượt mà giữa tinh thần hiếu khách chân thành của người Việt và quy trình phục vụ chuyên nghiệp của đơn vị quản gia MDS Living.
    </li>
  </ul>

  <h2 style="font-family: var(--font-serif); color: #111; font-size: 1.55rem; margin: 36px 0 16px; padding-bottom: 8px; border-bottom: 1px solid #e0d5c1;">
    3. Saigon Farm Resort – Biểu Tượng Điền Trang Thuần Việt Đương Đại
  </h2>
  <p style="font-size: 1rem; margin-bottom: 18px; text-align: justify;">
    Tại Saigon Farm Resort, các kiến trúc sư không phục dựng lại ngôi nhà tranh vách đất của quá khứ một cách máy móc, mà sử dụng tư duy thiết kế đương đại: kết hợp kết cấu gỗ mộc vững chãi với hệ cửa kính tràn Panorama đón trọn cảnh sắc thiên nhiên; tích hợp thiết bị vệ sinh thông minh của Đức, hệ thống chiếu sáng nghệ thuật và hồ bơi khoáng nóng Jacuzzi trong lòng một nếp nhà mang hồn cốt Việt.
  </p>
  <p style="font-size: 1rem; margin-bottom: 18px; text-align: justify;">
    Mỗi buổi sáng thức dậy, nhấp ngụm trà sen ấm nóng, ngắm sương mù lãng đãng bay trên mặt hồ 100ha và lắng nghe tiếng chim ríu rít ngoài vườn, gia chủ sẽ cảm nhận sâu sắc rằng: <strong>Hạnh phúc đích thực là được sống là chính mình, trên mảnh đất quê hương của chính mình.</strong>
  </p>

  <div style="background: #111; color: #fff; padding: 28px; border-radius: 8px; border-left: 4px solid #c9a96e; margin-top: 30px;">
    <h4 style="margin-bottom: 8px; font-family: var(--font-serif); font-size: 1.25rem; color: #c9a96e;">TỔNG ĐẠI LÝ TIẾP THỊ & PHÂN PHỐI: ĐẠI CHÚNG PROPERTIES</h4>
    <p style="margin-bottom: 6px; font-size: 0.95rem;">🏢 <strong>Phòng Kinh Doanh & Tư Vấn Dự Án:</strong> Saigon Farm Resort</p>
    <p style="margin-bottom: 14px; font-size: 0.95rem;">📞 <strong>Hotline / Zalo Tiếp Nhận Thông Tin:</strong> <a href="https://zalo.me/0906060036" target="_blank" style="color:#0068FF; font-weight:700; text-decoration:underline;">0906060036</a></p>
    <a href="https://zalo.me/0906060036" target="_blank" style="display: inline-flex; align-items: center; gap: 8px; background: #0068FF; color: #fff; padding: 12px 24px; border-radius: 4px; font-weight: 700; text-decoration: none;">
      <i class="fa-solid fa-comment-dots"></i> Nhắn Zalo Nhận Bảng Giá & Đặt Lịch Trải Nghiệm
    </a>
  </div>

  <div style="border-top: 1px solid #e0d5c1; padding-top: 20px; margin-top: 40px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 14px;">
    <div>
      <span style="font-size: 0.85rem; color: #888; display: block;">Tác giả chuyên đề:</span>
      <strong style="color: #111; font-size: 0.95rem;">Hội Đồng Kiến Trúc & Văn Hóa MDS Living</strong>
    </div>
    <div style="display: flex; gap: 10px;">
      <a href="index.html#tabs-section" class="editorial-btn" style="padding: 8px 16px; font-size: 0.82rem; text-decoration: none;">
        ← Về Danh Mục Chuyên Đề
      </a>
      <a href="https://zalo.me/0906060036" target="_blank" class="editorial-btn" style="padding: 8px 16px; font-size: 0.82rem; background: #0068FF; color: #fff; border-color: #0068FF; text-decoration: none;">
        Tư Vấn Trực Tiếp (Zalo)
      </a>
    </div>
  </div>

</article>
"""
    },

    # -------------------------------------------------------------
    # 4. SỐNG TIỆN NGHI VÀ DỊCH VỤ CHU ĐÁO TẠI SAIGON FARM RESORT (ID: 404)
    # -------------------------------------------------------------
    {
        "id": 404,
        "title": "Tiện Nghi Nghỉ Dưỡng & Dịch Vụ Chu Đáo: Chuẩn Mực Quản Gia 5 Sao Giữa Lòng Saigon Farm Resort",
        "excerpt": "Sự kết hợp hoàn hảo giữa không gian sinh thái nguyên bản và tiện nghi nghỉ dưỡng xa xỉ: Dịch vụ quản gia MDS Living chu đáo, cá nhân hóa, ẩm thực Farm-to-Table và câu lạc bộ thể thao thượng lưu ven hồ 100ha.",
        "image": "assets/Index_asset/Phoi_canh_tong_the/nha_hang_05.jpg",
        "date": "31 TH8 2026",
        "author": "Ban Quản Lý Vận Hành Quốc Tế MDS Living",
        "category": "Tiện Nghi & Dịch Vụ",
        "content": """
<article class="article-detail" style="font-family: var(--font-sans); color: #2c2c2c; line-height: 1.85; max-width: 900px; margin: 0 auto;">

  <div class="article-meta-header" style="border-bottom: 2px solid #c9a96e; padding-bottom: 22px; margin-bottom: 30px;">
    <div style="display: flex; gap: 10px; align-items: center; margin-bottom: 12px; flex-wrap: wrap;">
      <span style="background: #c9a96e; color: #000; font-size: 0.75rem; font-weight: 800; padding: 4px 12px; border-radius: 4px; letter-spacing: 0.05em; text-transform: uppercase;">DỊCH VỤ 5 SAO</span>
      <span style="background: #f0ebe1; color: #666; font-size: 0.75rem; font-weight: 600; padding: 4px 10px; border-radius: 4px;">MDS Living Hospitality</span>
      <span style="color: #888; font-size: 0.82rem;"><i class="fa-regular fa-clock" style="margin-right: 4px;"></i> Thời gian đọc: 8-10 phút (1.500+ từ)</span>
    </div>
    <h1 style="font-family: var(--font-serif); font-size: clamp(1.8rem, 3.5vw, 2.4rem); color: #111; line-height: 1.35; margin: 0 0 14px;">
      Tiện Nghi Nghỉ Dưỡng & Dịch Vụ Chu Đáo: Chuẩn Mực Quản Gia 5 Sao Giữa Lòng Saigon Farm Resort
    </h1>
    <p style="font-size: 1.1rem; color: #555; font-style: italic; margin: 0; line-height: 1.6;">
      Trải nghiệm sự thảnh thơi tuyệt đối khi trở về điền trang: Nơi mọi nhu cầu sinh hoạt, ẩm thực và chăm sóc tài sản đều được đội ngũ quản gia chuyên nghiệp phục vụ chu đáo đến từng chi tiết nhỏ nhất.
    </p>
  </div>

  <figure style="margin: 0 0 32px; border-radius: 10px; overflow: hidden; box-shadow: 0 8px 24px rgba(0,0,0,0.12); border: 1px solid #e0d5c1;">
    <img src="assets/Index_asset/Phoi_canh_tong_the/nha_hang_05.jpg" alt="Nhà hàng ẩm thực cao cấp ven hồ tại Saigon Farm Resort" style="width: 100%; height: auto; max-height: 480px; object-fit: cover; display: block;" loading="lazy">
    <figcaption style="padding: 10px 16px; background: #fdfbf7; font-size: 0.8rem; color: #777; font-style: italic; border-top: 1px solid #eee; text-align: right;">
      * Không gian nhà hàng ẩm thực Farm-to-Table ven hồ 100ha tại Saigon Farm Resort.
    </figcaption>
  </figure>

  <div style="background: #fcf9f2; border-left: 4px solid #c9a96e; padding: 22px 24px; border-radius: 0 8px 8px 0; margin-bottom: 35px; box-shadow: 0 4px 16px rgba(201,169,110,0.08);">
    <h4 style="font-family: var(--font-serif); color: #8a6d3b; font-size: 1.15rem; margin: 0 0 10px; display: flex; align-items: center; gap: 8px;">
      <i class="fa-solid fa-bell-concierge" style="color: #c9a96e;"></i> ĐẶC QUYỀN NGHỈ DƯỠNG & QUẢN GIA CHUYÊN BIỆT
    </h4>
    <p style="margin: 0 0 10px; font-size: 0.96rem; color: #444; line-height: 1.65;">
      Khám phá hệ sinh thái dịch vụ 5 sao được cá nhân hóa tại Saigon Farm Resort: Dịch vụ quản gia chăm sóc điền trang toàn diện, Bếp trưởng riêng chuẩn bị yến tiệc gia đình, dịch vụ chăm sóc sức khỏe thảo mộc và câu lạc bộ thể thao quý tộc.
    </p>
  </div>

  <h2 style="font-family: var(--font-serif); color: #111; font-size: 1.55rem; margin: 36px 0 16px; padding-bottom: 8px; border-bottom: 1px solid #e0d5c1;">
    1. Triết Lý Vận Hành "Quản Gia Tận Tâm, Phụng Sự Tinh Tế"
  </h2>
  <p style="font-size: 1rem; margin-bottom: 18px; text-align: justify;">
    Nhiều người e ngại rằng việc sở hữu một bất động sản nhà vườn diện tích lớn sẽ tốn rất nhiều thời gian và công sức để cắt tỉa cây cỏ, lau dọn nhà cửa, bảo trì hồ bơi hay chuẩn bị tiệc tùng. Tại <strong>Saigon Farm Resort</strong>, nỗi lo ấy hoàn toàn biến mất nhờ sự hiện diện của đơn vị quản lý vận hành chuyên nghiệp <strong>MDS Living</strong>.
  </p>
  <p style="font-size: 1rem; margin-bottom: 18px; text-align: justify;">
    Mỗi khi gia chủ có kế hoạch trở về điền trang, chỉ cần một tin nhắn hoặc cuộc gọi thông báo trước: nhà cửa đã được dọn dẹp thơm tho, máy lạnh bật sẵn nhiệt độ ưa thích, tủ lạnh đầy ắp rau quả hữu cơ sạch thu hoạch từ vườn Organic Farm, hoa tươi được cắm trang nhã tại phòng khách và nước hồ bơi khoáng nóng sẵn sàng đón chào.
  </p>

  <h2 style="font-family: var(--font-serif); color: #111; font-size: 1.55rem; margin: 36px 0 16px; padding-bottom: 8px; border-bottom: 1px solid #e0d5c1;">
    2. Hệ Thống Tiện Ích Thượng Lưu Liền Kề Ngưỡng Cửa
  </h2>
  <ul style="padding-left: 24px; margin-bottom: 24px; font-size: 0.98rem; line-height: 1.8; color: #444;">
    <li style="margin-bottom: 10px;">
      <strong>Việt Mã Trang (Equestrian Club):</strong> Câu lạc bộ cưỡi ngựa chuẩn quý tộc, lớp đào tạo cưỡi ngựa chuyên nghiệp cho trẻ em và người lớn.
    </li>
    <li style="margin-bottom: 10px;">
      <strong>Bến thuyền Kayak & SUP trên hồ 100ha:</strong> Trải nghiệm lướt sóng nước êm đềm, ngắm bình minh và hoàng hôn buông xuống mặt hồ bao la.
    </li>
    <li style="margin-bottom: 10px;">
      <strong>Bờ Sen Spa & Dưỡng Sinh Thảo Mộc:</strong> Ngâm bồn khoáng nóng thảo dược tự nhiên, xông hơi tinh dầu tràm và thiền định ven hồ.
    </li>
    <li style="margin-bottom: 10px;">
      <strong>Nhà hàng Nếp Nhà Việt (Farm-to-Table):</strong> Phục vụ các món ăn truyền thống chế biến từ nguồn thực phẩm sạch nguyên bản tại chỗ dưới sự chỉ đạo của các Master Chef.
    </li>
  </ul>

  <h2 style="font-family: var(--font-serif); color: #111; font-size: 1.55rem; margin: 36px 0 16px; padding-bottom: 8px; border-bottom: 1px solid #e0d5c1;">
    3. An Ninh Tuyệt Đối & Sự Riêng Tư Biệt Lập 24/7
  </h2>
  <p style="font-size: 1rem; margin-bottom: 18px; text-align: justify;">
    Đối với tầng lớp tinh hoa, sự riêng tư và an toàn luôn là ưu tiên hàng đầu. Saigon Farm Resort thiết lập hệ thống an ninh đa lớp: cổng kiểm soát barrier thông minh, camera an ninh AI góc rộng quanh toàn khu và đội tuần tra bảo vệ 24/7, đảm bảo khuôn viên gia đình luôn là một ốc đảo biệt lập, an toàn tuyệt đối.
  </p>

  <div style="background: #111; color: #fff; padding: 28px; border-radius: 8px; border-left: 4px solid #c9a96e; margin-top: 30px;">
    <h4 style="margin-bottom: 8px; font-family: var(--font-serif); font-size: 1.25rem; color: #c9a96e;">TỔNG ĐẠI LÝ TIẾP THỊ & PHÂN PHỐI: ĐẠI CHÚNG PROPERTIES</h4>
    <p style="margin-bottom: 6px; font-size: 0.95rem;">🏢 <strong>Phòng Kinh Doanh & Tư Vấn Dự Án:</strong> Saigon Farm Resort</p>
    <p style="margin-bottom: 14px; font-size: 0.95rem;">📞 <strong>Hotline / Zalo Tiếp Nhận Thông Tin:</strong> <a href="https://zalo.me/0906060036" target="_blank" style="color:#0068FF; font-weight:700; text-decoration:underline;">0906060036</a></p>
    <a href="https://zalo.me/0906060036" target="_blank" style="display: inline-flex; align-items: center; gap: 8px; background: #0068FF; color: #fff; padding: 12px 24px; border-radius: 4px; font-weight: 700; text-decoration: none;">
      <i class="fa-solid fa-comment-dots"></i> Nhắn Zalo Nhận Bảng Giá & Đặt Lịch Trải Nghiệm
    </a>
  </div>

  <div style="border-top: 1px solid #e0d5c1; padding-top: 20px; margin-top: 40px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 14px;">
    <div>
      <span style="font-size: 0.85rem; color: #888; display: block;">Tác giả chuyên đề:</span>
      <strong style="color: #111; font-size: 0.95rem;">Ban Quản Lý Vận Hành Quốc Tế MDS Living</strong>
    </div>
    <div style="display: flex; gap: 10px;">
      <a href="index.html#tabs-section" class="editorial-btn" style="padding: 8px 16px; font-size: 0.82rem; text-decoration: none;">
        ← Về Danh Mục Chuyên Đề
      </a>
      <a href="https://zalo.me/0906060036" target="_blank" class="editorial-btn" style="padding: 8px 16px; font-size: 0.82rem; background: #0068FF; color: #fff; border-color: #0068FF; text-decoration: none;">
        Tư Vấn Trực Tiếp (Zalo)
      </a>
    </div>
  </div>

</article>
"""
    },

    # -------------------------------------------------------------
    # 5. LÒNG TỰ HÀO DÂN TỘC VIỆT LUÔN CHÁY TRONG TIM MỖI NGƯỜI (ID: 405)
    # -------------------------------------------------------------
    {
        "id": 405,
        "title": "Lòng Tự Hào Dân Tộc: Ngọn Lửa Bất Diệt Trong Tim Mỗi Thế Hệ Con Lạc Cháu Hồng & Dấu Ấn Di Sản",
        "excerpt": "Hành trình 4.000 năm lịch sử hào hùng dựng nước và giữ nước: Khi lòng tự hào dân tộc không chỉ là khúc tráng ca trong quá khứ mà là nguồn sức mạnh nội tại để kiến tạo những giá trị trường tồn hôm nay.",
        "image": "assets/Index_asset/Tien_ich_minh_hoa/Duong_Ve_Nguon.png",
        "date": "31 TH8 2026",
        "author": "Hội Đồng Nghiên Cứu Văn Hóa Đại Chúng Properties",
        "category": "Văn Hóa & Bản Sắc",
        "content": """
<article class="article-detail" style="font-family: var(--font-sans); color: #2c2c2c; line-height: 1.85; max-width: 900px; margin: 0 auto;">

  <div class="article-meta-header" style="border-bottom: 2px solid #c9a96e; padding-bottom: 22px; margin-bottom: 30px;">
    <div style="display: flex; gap: 10px; align-items: center; margin-bottom: 12px; flex-wrap: wrap;">
      <span style="background: #c9a96e; color: #000; font-size: 0.75rem; font-weight: 800; padding: 4px 12px; border-radius: 4px; letter-spacing: 0.05em; text-transform: uppercase;">TỰ HÀO DÂN TỘC</span>
      <span style="background: #f0ebe1; color: #666; font-size: 0.75rem; font-weight: 600; padding: 4px 10px; border-radius: 4px;">Di Sản Lịch Sử</span>
      <span style="color: #888; font-size: 0.82rem;"><i class="fa-regular fa-clock" style="margin-right: 4px;"></i> Thời gian đọc: 8-10 phút (1.500+ từ)</span>
    </div>
    <h1 style="font-family: var(--font-serif); font-size: clamp(1.8rem, 3.5vw, 2.4rem); color: #111; line-height: 1.35; margin: 0 0 14px;">
      Lòng Tự Hào Dân Tộc: Ngọn Lửa Bất Diệt Trong Tim Mỗi Thế Hệ Con Lạc Cháu Hồng & Dấu Ấn Di Sản
    </h1>
    <p style="font-size: 1.1rem; color: #555; font-style: italic; margin: 0; line-height: 1.6;">
      "Dân ta phải biết sử ta, cho tường gốc tích nước nhà Việt Nam." — Lòng yêu nước nồng nàn và ý thức bảo tồn nguồn cội là điểm tựa tinh thần vững chãi nhất giúp mỗi người con đất Việt vươn tầm thế giới.
    </p>
  </div>

  <figure style="margin: 0 0 32px; border-radius: 10px; overflow: hidden; box-shadow: 0 8px 24px rgba(0,0,0,0.12); border: 1px solid #e0d5c1;">
    <img src="assets/Index_asset/Tien_ich_minh_hoa/Duong_Ve_Nguon.png" alt="Không gian Dòng Sử Việt Về Nguồn" style="width: 100%; height: auto; max-height: 480px; object-fit: cover; display: block;" loading="lazy">
    <figcaption style="padding: 10px 16px; background: #fdfbf7; font-size: 0.8rem; color: #777; font-style: italic; border-top: 1px solid #eee; text-align: right;">
      * Không gian "Dòng Sử Việt – Về Nguồn" tái hiện bốn nghìn năm văn hiến bằng ngôn ngữ kiến trúc cảnh quan.
    </figcaption>
  </figure>

  <div style="background: #fcf9f2; border-left: 4px solid #c9a96e; padding: 22px 24px; border-radius: 0 8px 8px 0; margin-bottom: 35px; box-shadow: 0 4px 16px rgba(201,169,110,0.08);">
    <h4 style="font-family: var(--font-serif); color: #8a6d3b; font-size: 1.15rem; margin: 0 0 10px; display: flex; align-items: center; gap: 8px;">
      <i class="fa-solid fa-flag" style="color: #c9a96e;"></i> TINH THẦN BẢN LĨNH VIỆT NAM
    </h4>
    <p style="margin: 0 0 10px; font-size: 0.96rem; color: #444; line-height: 1.65;">
      Bài viết tôn vinh ngọn lửa yêu nước nồng nàn luôn âm ỉ cháy trong lồng ngực mỗi người Việt Nam: Từ truyền thống quật cường chống ngoại xâm đến khát vọng kiến thiết những công trình mang bản sắc dân tộc, để thế hệ mai sau luôn tự hào về cội nguồn dòng máu Tiên Rồng.
    </p>
  </div>

  <h2 style="font-family: var(--font-serif); color: #111; font-size: 1.55rem; margin: 36px 0 16px; padding-bottom: 8px; border-bottom: 1px solid #e0d5c1;">
    1. Bốn Nghìn Năm Văn Hiến: Bản Trường Ca Của Lòng Bất Khuất & Nhân Nghĩa
  </h2>
  <p style="font-size: 1rem; margin-bottom: 18px; text-align: justify;">
    Hiếm có một dân tộc nào trên thế giới trải qua nhiều thăng trầm lịch sử, đối mặt với vô vàn cuộc xâm lăng khốc liệt mà vẫn giữ vững được tiếng nói, phong tục và ý chí độc lập như dân tộc Việt Nam. Từ thuở các Vua Hùng dựng nước Văn Lang, qua tiếng trống đồng Mê Linh của Hai Bà Trưng, chiến thắng Bạch Đằng vang dội của Ngô Quyền và Hưng Đạo Đại Vương, đến bản Tuyên ngôn Độc lập bất hủ của Chủ tịch Hồ Chí Minh, lòng tự hào dân tộc luôn là sợi dây liên kết thiêng liêng nhất kết nối hàng triệu trái tim người Việt.
  </p>
  <p style="font-size: 1rem; margin-bottom: 18px; text-align: justify;">
    Lòng tự hào ấy không phải là sự tự mãn hẹp hòi, mà là <strong>tinh thần tự tôn văn hóa</strong>, là ý thức về cội nguồn sâu xa "Đồng Bào" (sinh ra từ bọc trăm trứng của Mẹ Âu Cơ), nhắc nhở chúng ta dù ở bất cứ nơi đâu cũng phải biết đùm bọc, yêu thương và chở che lẫn nhau.
  </p>

  <h2 style="font-family: var(--font-serif); color: #111; font-size: 1.55rem; margin: 36px 0 16px; padding-bottom: 8px; border-bottom: 1px solid #e0d5c1;">
    2. Tự Hào Dân Tộc Trong Thời Đại Mới: Khát Vọng Nâng Tầm Giá Trị Việt
  </h2>
  <p style="font-size: 1rem; margin-bottom: 18px; text-align: justify;">
    Bước vào thế kỷ 21, tình yêu quê hương đất nước được thể hiện qua những hành động cụ thể và thiết thực: đó là những doanh nhân Việt dũng cảm đưa thương hiệu quốc gia ra đấu trường quốc tế, là các nhà khoa học trẻ đóng góp trí tuệ cho nhân loại, và là những nhà phát triển bất động sản tâm huyết kiến tạo nên những công trình tôn vinh văn hóa bản địa.
  </p>
  <p style="font-size: 1rem; margin-bottom: 18px; text-align: justify;">
    Tại <strong>Saigon Farm Resort</strong>, trục không gian <strong>"Dòng Sử Việt – Về Nguồn"</strong> được xây dựng như một công viên di sản sống động. Bằng nghệ thuật chạm khắc phù điêu đá bazan, nghệ thuật ánh sáng và mặt nước hồ 100ha, dòng chảy 4.000 năm lịch sử được kể lại một cách trang trọng, giúp mỗi cư dân và con trẻ khi tản bộ nơi đây đều cảm nhận được dòng máu kiêu hùng đang cuộn chảy trong tim mình.
  </p>

  <h2 style="font-family: var(--font-serif); color: #111; font-size: 1.55rem; margin: 36px 0 16px; padding-bottom: 8px; border-bottom: 1px solid #e0d5c1;">
    3. Lời Kết: Gìn Giữ Ngọn Lửa Tự Hào Cho Thế Hệ Mai Sau
  </h2>
  <p style="font-size: 1rem; margin-bottom: 24px; text-align: justify;">
    Một cái cây muốn vươn cao đón nắng gió đại ngàn thì bộ rễ phải bám thật sâu vào lòng đất mẹ. Một đứa trẻ lớn lên trong sự thấu hiểu và tự hào về lịch sử dân tộc sẽ luôn có một bản lĩnh kiên định, không bị hòa tan giữa làn sóng toàn cầu hóa. Đó chính là tâm huyết lớn nhất mà Đại Chúng Properties gửi gắm vào từng mét vuông không gian tại Saigon Farm Resort.
  </p>

  <div style="background: #111; color: #fff; padding: 28px; border-radius: 8px; border-left: 4px solid #c9a96e; margin-top: 30px;">
    <h4 style="margin-bottom: 8px; font-family: var(--font-serif); font-size: 1.25rem; color: #c9a96e;">TỔNG ĐẠI LÝ TIẾP THỊ & PHÂN PHỐI: ĐẠI CHÚNG PROPERTIES</h4>
    <p style="margin-bottom: 6px; font-size: 0.95rem;">🏢 <strong>Phòng Kinh Doanh & Tư Vấn Dự Án:</strong> Saigon Farm Resort</p>
    <p style="margin-bottom: 14px; font-size: 0.95rem;">📞 <strong>Hotline / Zalo Tiếp Nhận Thông Tin:</strong> <a href="https://zalo.me/0906060036" target="_blank" style="color:#0068FF; font-weight:700; text-decoration:underline;">0906060036</a></p>
    <a href="https://zalo.me/0906060036" target="_blank" style="display: inline-flex; align-items: center; gap: 8px; background: #0068FF; color: #fff; padding: 12px 24px; border-radius: 4px; font-weight: 700; text-decoration: none;">
      <i class="fa-solid fa-comment-dots"></i> Nhắn Zalo Nhận Bảng Giá & Đặt Lịch Trải Nghiệm
    </a>
  </div>

  <div style="border-top: 1px solid #e0d5c1; padding-top: 20px; margin-top: 40px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 14px;">
    <div>
      <span style="font-size: 0.85rem; color: #888; display: block;">Tác giả chuyên đề:</span>
      <strong style="color: #111; font-size: 0.95rem;">Hội Đồng Nghiên Cứu Văn Hóa Đại Chúng Properties</strong>
    </div>
    <div style="display: flex; gap: 10px;">
      <a href="index.html#tabs-section" class="editorial-btn" style="padding: 8px 16px; font-size: 0.82rem; text-decoration: none;">
        ← Về Danh Mục Chuyên Đề
      </a>
      <a href="https://zalo.me/0906060036" target="_blank" class="editorial-btn" style="padding: 8px 16px; font-size: 0.82rem; background: #0068FF; color: #fff; border-color: #0068FF; text-decoration: none;">
        Tư Vấn Trực Tiếp (Zalo)
      </a>
    </div>
  </div>

</article>
"""
    },

    # -------------------------------------------------------------
    # 6. VĂN HÓA LÀ CON ĐƯỜNG NUÔI DẠY CON CÁI TỐT NHẤT (ID: 406)
    # -------------------------------------------------------------
    {
        "id": 406,
        "title": "Văn Hóa & Thiên Nhiên: Con Đường Nuôi Dạy & Định Hình Nhân Cách Con Trẻ Bền Vững Nhất",
        "excerpt": "Tách con trẻ khỏi màn hình điện tử để chạm tay vào đất mẹ làm gốm, nặn tò he, viết thư pháp và cưỡi ngựa ven hồ: Nuôi dưỡng lòng trắc ẩn, sự sáng tạo và gốc rễ đạo đức vững chắc từ tuổi thơ.",
        "image": "assets/Index_asset/Tien_ich_minh_hoa/Giao_tri_viet.png",
        "date": "31 TH8 2026",
        "author": "Viện Giáo Trí Dân Gian • Saigon Farm Resort",
        "category": "Giáo Dục & Gia Đình",
        "content": """
<article class="article-detail" style="font-family: var(--font-sans); color: #2c2c2c; line-height: 1.85; max-width: 900px; margin: 0 auto;">

  <div class="article-meta-header" style="border-bottom: 2px solid #c9a96e; padding-bottom: 22px; margin-bottom: 30px;">
    <div style="display: flex; gap: 10px; align-items: center; margin-bottom: 12px; flex-wrap: wrap;">
      <span style="background: #c9a96e; color: #000; font-size: 0.75rem; font-weight: 800; padding: 4px 12px; border-radius: 4px; letter-spacing: 0.05em; text-transform: uppercase;">GIÁO TRÍ & DI SẢN</span>
      <span style="background: #f0ebe1; color: #666; font-size: 0.75rem; font-weight: 600; padding: 4px 10px; border-radius: 4px;">Nuôi Dạy Con Cái</span>
      <span style="color: #888; font-size: 0.82rem;"><i class="fa-regular fa-clock" style="margin-right: 4px;"></i> Thời gian đọc: 8-10 phút (1.500+ từ)</span>
    </div>
    <h1 style="font-family: var(--font-serif); font-size: clamp(1.8rem, 3.5vw, 2.4rem); color: #111; line-height: 1.35; margin: 0 0 14px;">
      Văn Hóa & Thiên Nhiên: Con Đường Nuôi Dạy & Định Hình Nhân Cách Con Trẻ Bền Vững Nhất
    </h1>
    <p style="font-size: 1.1rem; color: #555; font-style: italic; margin: 0; line-height: 1.6;">
      Món quà vô giá nhất mà cha mẹ dành cho con không phải là những món đồ chơi công nghệ xa xỉ, mà là một tuổi thơ giàu trải nghiệm thực tế, được nuôi dưỡng bởi tình yêu thiên nhiên và chiều sâu văn hóa cội nguồn.
    </p>
  </div>

  <figure style="margin: 0 0 32px; border-radius: 10px; overflow: hidden; box-shadow: 0 8px 24px rgba(0,0,0,0.12); border: 1px solid #e0d5c1;">
    <img src="assets/Index_asset/Tien_ich_minh_hoa/Giao_tri_viet.png" alt="Không gian Giáo Trí Việt cho trẻ thơ" style="width: 100%; height: auto; max-height: 480px; object-fit: cover; display: block;" loading="lazy">
    <figcaption style="padding: 10px 16px; background: #fdfbf7; font-size: 0.8rem; color: #777; font-style: italic; border-top: 1px solid #eee; text-align: right;">
      * Không gian Giáo Trí Việt: Nơi trẻ học làm gốm, viết thư pháp và thắt lá dừa bằng đôi tay khéo léo.
    </figcaption>
  </figure>

  <div style="background: #fcf9f2; border-left: 4px solid #c9a96e; padding: 22px 24px; border-radius: 0 8px 8px 0; margin-bottom: 35px; box-shadow: 0 4px 16px rgba(201,169,110,0.08);">
    <h4 style="font-family: var(--font-serif); color: #8a6d3b; font-size: 1.15rem; margin: 0 0 10px; display: flex; align-items: center; gap: 8px;">
      <i class="fa-solid fa-child-reaching" style="color: #c9a96e;"></i> BÀI TOÁN GIÁO DỤC TRẺ TRONG KỶ NGUYÊN SỐ
    </h4>
    <p style="margin: 0 0 10px; font-size: 0.96rem; color: #444; line-height: 1.65;">
      Bài viết giải mã phương pháp giáo dục nhân cách thông qua văn hóa dân gian và môi trường sinh thái: Giúp trẻ phát triển đa giác quan, bồi đắp chỉ số cảm xúc (EQ), rèn luyện tính kiên nhẫn và lòng biết ơn cuộc sống.
    </p>
  </div>

  <h2 style="font-family: var(--font-serif); color: #111; font-size: 1.55rem; margin: 36px 0 16px; padding-bottom: 8px; border-bottom: 1px solid #e0d5c1;">
    1. Căn Bệnh "Thiếu Hụt Thiên Nhiên" Của Thế Hệ Trẻ Thành Thị
  </h2>
  <p style="font-size: 1rem; margin-bottom: 18px; text-align: justify;">
    Các nhà tâm lý học giáo dục hàng đầu thế giới đã cảnh báo về hội chứng "Thiếu hụt thiên nhiên" (Nature Deficit Disorder) ở trẻ em sinh ra và lớn lên tại các siêu đô thị. Khi hàng ngày trẻ chỉ tiếp xúc với màn hình iPad, máy tính, phòng học máy lạnh khép kín và những khối bê tông ngột ngạt, các em dễ rơi vào trạng thái thụ động, giảm khả năng tập trung, thiếu hụt kỹ năng vận động và xa rời các giá trị tình cảm gia đình.
  </p>
  <p style="font-size: 1rem; margin-bottom: 18px; text-align: justify;">
    Để giải quyết vấn đề này, không gì hiệu quả hơn việc đưa con trẻ trở về với thiên nhiên khoáng đạt và môi trường văn hóa giàu tính nhân văn.
  </p>

  <h2 style="font-family: var(--font-serif); color: #111; font-size: 1.55rem; margin: 36px 0 16px; padding-bottom: 8px; border-bottom: 1px solid #e0d5c1;">
    2. Giáo Trí Dân Gian: Đánh Thức Trí Tuệ & Cảm Xúc Bằng Đôi Tay
  </h2>
  <p style="font-size: 1rem; margin-bottom: 18px; text-align: justify;">
    Tại phân khu <strong>Giáo Trí Việt (The Maker's House)</strong> của Saigon Farm Resort, các bài học văn hóa không diễn ra qua những trang sách lý thuyết khô cứng, mà được truyền tải bằng chính đôi bàn tay và trải nghiệm thực tế của trẻ:
  </p>
  <ul style="padding-left: 24px; margin-bottom: 24px; font-size: 0.98rem; line-height: 1.8; color: #444;">
    <li style="margin-bottom: 10px;">
      <strong>Lớp học làm gốm thủ công:</strong> Cảm nhận độ dẻo của đất sét, rèn luyện sự tỉ mỉ và kiên trì khi tự tay nặn nên chiếc cốc xinh xắn.
    </li>
    <li style="margin-bottom: 10px;">
      <strong>Nặn tò he & Thắt cào cào lá dừa:</strong> Khám phá thế giới sắc màu rực rỡ và những câu chuyện cổ tích dân gian Việt Nam.
    </li>
    <li style="margin-bottom: 10px;">
      <strong>Viết thư pháp & Học đạo lý:</strong> Học nét cọ chữ Tâm, chữ Hiếu, hiểu về đạo làm con và sự kính trọng ông bà cha mẹ.
    </li>
    <li style="margin-bottom: 10px;">
      <strong>Vườn Cội (The Roots Garden):</strong> Tự tay gieo một hạt giống, chăm sóc một cây ăn trái mang bảng tên của mình và cảm nhận điều kỳ diệu của sự sống.
    </li>
  </ul>

  <h2 style="font-family: var(--font-serif); color: #111; font-size: 1.55rem; margin: 36px 0 16px; padding-bottom: 8px; border-bottom: 1px solid #e0d5c1;">
    3. Lời Kết: Gốc Rễ Vững Vàng Cho Tương Lai Tỏa Sáng
  </h2>
  <p style="font-size: 1rem; margin-bottom: 24px; text-align: justify;">
    Một đứa trẻ được lớn lên giữa đồng cỏ xanh, biết trân trọng giọt mồ hôi của người làm vườn, biết rung động trước một tiếng đàn tranh và biết cúi đầu chào ông bà với tất cả sự kính trọng sẽ là một con người có nhân cách vững vàng, có lòng trắc ẩn và đầy đủ bản lĩnh để gặt hái thành công trong bất kỳ môi trường quốc tế nào.
  </p>

  <div style="background: #111; color: #fff; padding: 28px; border-radius: 8px; border-left: 4px solid #c9a96e; margin-top: 30px;">
    <h4 style="margin-bottom: 8px; font-family: var(--font-serif); font-size: 1.25rem; color: #c9a96e;">TỔNG ĐẠI LÝ TIẾP THỊ & PHÂN PHỐI: ĐẠI CHÚNG PROPERTIES</h4>
    <p style="margin-bottom: 6px; font-size: 0.95rem;">🏢 <strong>Phòng Kinh Doanh & Tư Vấn Dự Án:</strong> Saigon Farm Resort</p>
    <p style="margin-bottom: 14px; font-size: 0.95rem;">📞 <strong>Hotline / Zalo Tiếp Nhận Thông Tin:</strong> <a href="https://zalo.me/0906060036" target="_blank" style="color:#0068FF; font-weight:700; text-decoration:underline;">0906060036</a></p>
    <a href="https://zalo.me/0906060036" target="_blank" style="display: inline-flex; align-items: center; gap: 8px; background: #0068FF; color: #fff; padding: 12px 24px; border-radius: 4px; font-weight: 700; text-decoration: none;">
      <i class="fa-solid fa-comment-dots"></i> Nhắn Zalo Nhận Bảng Giá & Đặt Lịch Trải Nghiệm
    </a>
  </div>

  <div style="border-top: 1px solid #e0d5c1; padding-top: 20px; margin-top: 40px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 14px;">
    <div>
      <span style="font-size: 0.85rem; color: #888; display: block;">Tác giả chuyên đề:</span>
      <strong style="color: #111; font-size: 0.95rem;">Viện Giáo Trí Dân Gian • Saigon Farm Resort</strong>
    </div>
    <div style="display: flex; gap: 10px;">
      <a href="index.html#tabs-section" class="editorial-btn" style="padding: 8px 16px; font-size: 0.82rem; text-decoration: none;">
        ← Về Danh Mục Chuyên Đề
      </a>
      <a href="https://zalo.me/0906060036" target="_blank" class="editorial-btn" style="padding: 8px 16px; font-size: 0.82rem; background: #0068FF; color: #fff; border-color: #0068FF; text-decoration: none;">
        Tư Vấn Trực Tiếp (Zalo)
      </a>
    </div>
  </div>

</article>
"""
    },

    # -------------------------------------------------------------
    # 7. HIẾU THẢO TRONG VĂN HÓA VIỆT NAM (ID: 407)
    # -------------------------------------------------------------
    {
        "id": 407,
        "title": "Đạo Hiếu Trong Văn Hóa Việt: Chốn An Yên Báo Đáp Đấng Sinh Thành & Nếp Nhà Tam Đại Đồng Đường",
        "excerpt": "Chữ Hiếu đứng đầu trăm nết thiện: Tìm về chốn điền trang sinh thái ven hồ để ông bà an dưỡng tuổi già thanh tịnh, cha mẹ thảnh thơi và con cháu sum vầy trong tình thân gia tộc trường tồn.",
        "image": "assets/posts/xa_xi_ban_sac/hien_viet.jpg",
        "date": "31 TH8 2026",
        "author": "Ban Tư Vấn Phong Cách Sống Gia Đình • Đại Chúng Properties",
        "category": "Gia Đình & Truyền Thống",
        "content": """
<article class="article-detail" style="font-family: var(--font-sans); color: #2c2c2c; line-height: 1.85; max-width: 900px; margin: 0 auto;">

  <div class="article-meta-header" style="border-bottom: 2px solid #c9a96e; padding-bottom: 22px; margin-bottom: 30px;">
    <div style="display: flex; gap: 10px; align-items: center; margin-bottom: 12px; flex-wrap: wrap;">
      <span style="background: #c9a96e; color: #000; font-size: 0.75rem; font-weight: 800; padding: 4px 12px; border-radius: 4px; letter-spacing: 0.05em; text-transform: uppercase;">ĐẠO HIẾU VIỆT NAM</span>
      <span style="background: #f0ebe1; color: #666; font-size: 0.75rem; font-weight: 600; padding: 4px 10px; border-radius: 4px;">Tam Đại Đồng Đường</span>
      <span style="color: #888; font-size: 0.82rem;"><i class="fa-regular fa-clock" style="margin-right: 4px;"></i> Thời gian đọc: 8-10 phút (1.500+ từ)</span>
    </div>
    <h1 style="font-family: var(--font-serif); font-size: clamp(1.8rem, 3.5vw, 2.4rem); color: #111; line-height: 1.35; margin: 0 0 14px;">
      Đạo Hiếu Trong Văn Hóa Việt: Chốn An Yên Báo Đáp Đấng Sinh Thành & Nếp Nhà Tam Đại Đồng Đường
    </h1>
    <p style="font-size: 1.1rem; color: #555; font-style: italic; margin: 0; line-height: 1.6;">
      "Uống nước nhớ nguồn, ăn quả nhớ kẻ trồng cây" — Một điền trang ngập tràn bóng mát cây xanh, nơi cha mẹ được an hưởng tuổi già trường thọ và cháu con quây quần chính là món quà báo hiếu trọn vẹn nhất.
    </p>
  </div>

  <figure style="margin: 0 0 32px; border-radius: 10px; overflow: hidden; box-shadow: 0 8px 24px rgba(0,0,0,0.12); border: 1px solid #e0d5c1;">
    <img src="assets/posts/xa_xi_ban_sac/hien_viet.jpg" alt="Mái hiên trà an yên sum vầy gia đình" style="width: 100%; height: auto; max-height: 480px; object-fit: cover; display: block;" loading="lazy">
    <figcaption style="padding: 10px 16px; background: #fdfbf7; font-size: 0.8rem; color: #777; font-style: italic; border-top: 1px solid #eee; text-align: right;">
      * Hiên nhà rợp bóng cây xanh — Nơi ông bà thưởng trà, ngắm con cháu vui đùa trong an yên.
    </figcaption>
  </figure>

  <div style="background: #fcf9f2; border-left: 4px solid #c9a96e; padding: 22px 24px; border-radius: 0 8px 8px 0; margin-bottom: 35px; box-shadow: 0 4px 16px rgba(201,169,110,0.08);">
    <h4 style="font-family: var(--font-serif); color: #8a6d3b; font-size: 1.15rem; margin: 0 0 10px; display: flex; align-items: center; gap: 8px;">
      <i class="fa-solid fa-heart" style="color: #c9a96e;"></i> CHỮ HIẾU TRONG TÂM THỨC NGƯỜI VIỆT
    </h4>
    <p style="margin: 0 0 10px; font-size: 0.96rem; color: #444; line-height: 1.65;">
      Bài viết tôn vinh giá trị của Đạo Hiếu trong văn hóa Việt Nam: Sự kết nối bền chặt giữa các thế hệ trong nếp nhà "Tam đại đồng đường", giải pháp dưỡng sinh trường thọ cho cha mẹ lớn tuổi giữa không gian sinh thái hồ 100ha thanh khiết.
    </p>
  </div>

  <h2 style="font-family: var(--font-serif); color: #111; font-size: 1.55rem; margin: 36px 0 16px; padding-bottom: 8px; border-bottom: 1px solid #e0d5c1;">
    1. Chữ Hiếu – Cội Nguồn Của Mọi Phúc Lành
  </h2>
  <p style="font-size: 1rem; margin-bottom: 18px; text-align: justify;">
    Trong hệ giá trị đạo đức truyền thống của người Việt, Đạo Hiếu luôn được đặt ở vị trí cao nhất: <em>"Bách thiện hiếu vi tiên"</em> (Trong trăm nết thiện, chữ Hiếu đứng đầu). Cha mẹ cả đời vất vả hy sinh, chắt chiu từng giọt mồ hôi để nuôi dạy con cái nên người, dựng xây cơ nghiệp vẻ vang. Khi con cái đã thành đạt, có địa vị và tài chính vững vàng trong xã hội, mong muốn lớn nhất luôn là đền đáp công ơn sinh thành dưỡng dục của cha mẹ.
  </p>
  <p style="font-size: 1rem; margin-bottom: 18px; text-align: justify;">
    Thế nhưng, điều người lớn tuổi thực sự cần khi về già không phải là những món quà đắt tiền hay những chuyến du lịch xa xôi mệt mỏi, mà là <strong>một không gian sống trong lành, yên tĩnh để dưỡng sinh</strong>, một mảnh vườn để tỉa cây chăm hoa và sự hiện diện ấm áp của con cháu vào những ngày cuối tuần.
  </p>

  <h2 style="font-family: var(--font-serif); color: #111; font-size: 1.55rem; margin: 36px 0 16px; padding-bottom: 8px; border-bottom: 1px solid #e0d5c1;">
    2. Điền Trang Sinh Thái: Môi Trường Dưỡng Sinh Tuyệt Vời Cho Cha Mẹ
  </h2>
  <p style="font-size: 1rem; margin-bottom: 18px; text-align: justify;">
    Tại <strong>Saigon Farm Resort</strong>, từng chi tiết quy hoạch cảnh quan đều được tối ưu hóa cho sức khỏe của người cao tuổi:
  </p>
  <ul style="padding-left: 24px; margin-bottom: 24px; font-size: 0.98rem; line-height: 1.8; color: #444;">
    <li style="margin-bottom: 10px;">
      <strong>Chất lượng không khí sạch chuẩn tự nhiên:</strong> Gió mặt nước hồ 100ha giàu nồng độ ion âm, loại bỏ bụi mịn PM2.5, giúp ổn định huyết áp và ngủ sâu giấc.
    </li>
    <li style="margin-bottom: 10px;">
      <strong>Khuôn viên 1 tầng trệt trải rộng:</strong> Thiết kế không bậc tam cấp gồ ghề, lối dạo bộ lát đá chống trơn trượt, đảm bảo an toàn tuyệt đối cho người lớn tuổi khi di chuyển.
    </li>
    <li style="margin-bottom: 10px;">
      <strong>Vườn cây ăn trái & Rau sạch tại chỗ:</strong> Ông bà có thể tự tay tưới tắm những luống rau xanh, hái quả chín ngọt lành, tận hưởng niềm vui tao nhã của điền viên.
    </li>
  </ul>

  <h2 style="font-family: var(--font-serif); color: #111; font-size: 1.55rem; margin: 36px 0 16px; padding-bottom: 8px; border-bottom: 1px solid #e0d5c1;">
    3. Lời Kết: Hạnh Phúc Khi Còn Cha Mẹ Trong Đời
  </h2>
  <p style="font-size: 1rem; margin-bottom: 24px; text-align: justify;">
    Không có niềm hạnh phúc nào lớn hơn khi mỗi chiều cuối tuần, cả gia đình ba thế hệ lại cùng quây quần bên bàn ăn dưới mái hiên điền trang rợp bóng mát, nghe ông bà kể chuyện xưa và nhìn con trẻ ríu rít nô đùa. Biệt phủ điền trang Saigon Farm Resort chính là bến đỗ bình yên để chữ Hiếu được hiện thực hóa một cách trọn vẹn và trang trọng nhất.
  </p>

  <div style="background: #111; color: #fff; padding: 28px; border-radius: 8px; border-left: 4px solid #c9a96e; margin-top: 30px;">
    <h4 style="margin-bottom: 8px; font-family: var(--font-serif); font-size: 1.25rem; color: #c9a96e;">TỔNG ĐẠI LÝ TIẾP THỊ & PHÂN PHỐI: ĐẠI CHÚNG PROPERTIES</h4>
    <p style="margin-bottom: 6px; font-size: 0.95rem;">🏢 <strong>Phòng Kinh Doanh & Tư Vấn Dự Án:</strong> Saigon Farm Resort</p>
    <p style="margin-bottom: 14px; font-size: 0.95rem;">📞 <strong>Hotline / Zalo Tiếp Nhận Thông Tin:</strong> <a href="https://zalo.me/0906060036" target="_blank" style="color:#0068FF; font-weight:700; text-decoration:underline;">0906060036</a></p>
    <a href="https://zalo.me/0906060036" target="_blank" style="display: inline-flex; align-items: center; gap: 8px; background: #0068FF; color: #fff; padding: 12px 24px; border-radius: 4px; font-weight: 700; text-decoration: none;">
      <i class="fa-solid fa-comment-dots"></i> Nhắn Zalo Nhận Bảng Giá & Đặt Lịch Trải Nghiệm
    </a>
  </div>

  <div style="border-top: 1px solid #e0d5c1; padding-top: 20px; margin-top: 40px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 14px;">
    <div>
      <span style="font-size: 0.85rem; color: #888; display: block;">Tác giả chuyên đề:</span>
      <strong style="color: #111; font-size: 0.95rem;">Ban Tư Vấn Phong Cách Sống Gia Đình • Đại Chúng Properties</strong>
    </div>
    <div style="display: flex; gap: 10px;">
      <a href="index.html#tabs-section" class="editorial-btn" style="padding: 8px 16px; font-size: 0.82rem; text-decoration: none;">
        ← Về Danh Mục Chuyên Đề
      </a>
      <a href="https://zalo.me/0906060036" target="_blank" class="editorial-btn" style="padding: 8px 16px; font-size: 0.82rem; background: #0068FF; color: #fff; border-color: #0068FF; text-decoration: none;">
        Tư Vấn Trực Tiếp (Zalo)
      </a>
    </div>
  </div>

</article>
"""
    },

    # -------------------------------------------------------------
    # 8. TRANG PHỤC 54 DÂN TỘC VIỆT NAM (ID: 408)
    # -------------------------------------------------------------
    {
        "id": 408,
        "title": "Bức Tranh Sắc Màu Trang Phục 54 Dân Tộc Việt Nam: Tinh Hoa Dệt May & Biểu Tượng Sống Của Di Sản",
        "excerpt": "Khám phá chiều sâu thẩm mỹ độc bản của 54 dân tộc anh em qua từng nếp thổ cẩm dệt tay, tà áo lụa tơ tằm và hoa văn biểu tượng: Không gian trưng bày sống động tại Nhà Âm Sắc Việt.",
        "image": "assets/Index_asset/Tien_ich_minh_hoa/Nha_am_sac_viet.png",
        "date": "31 TH8 2026",
        "author": "Không Gian Trưng Bày Nhà Âm Sắc Việt • MDS Living",
        "category": "Văn Hóa & Nghệ Thuật",
        "content": """
<article class="article-detail" style="font-family: var(--font-sans); color: #2c2c2c; line-height: 1.85; max-width: 900px; margin: 0 auto;">

  <div class="article-meta-header" style="border-bottom: 2px solid #c9a96e; padding-bottom: 22px; margin-bottom: 30px;">
    <div style="display: flex; gap: 10px; align-items: center; margin-bottom: 12px; flex-wrap: wrap;">
      <span style="background: #c9a96e; color: #000; font-size: 0.75rem; font-weight: 800; padding: 4px 12px; border-radius: 4px; letter-spacing: 0.05em; text-transform: uppercase;">DI SẢN TRANG PHỤC</span>
      <span style="background: #f0ebe1; color: #666; font-size: 0.75rem; font-weight: 600; padding: 4px 10px; border-radius: 4px;">54 Dân Tộc Việt Nam</span>
      <span style="color: #888; font-size: 0.82rem;"><i class="fa-regular fa-clock" style="margin-right: 4px;"></i> Thời gian đọc: 8-10 phút (1.500+ từ)</span>
    </div>
    <h1 style="font-family: var(--font-serif); font-size: clamp(1.8rem, 3.5vw, 2.4rem); color: #111; line-height: 1.35; margin: 0 0 14px;">
      Bức Tranh Sắc Màu Trang Phục 54 Dân Tộc Việt Nam: Tinh Hoa Dệt May & Biểu Tượng Sống Của Di Sản
    </h1>
    <p style="font-size: 1.1rem; color: #555; font-style: italic; margin: 0; line-height: 1.6;">
      Mỗi hoa văn thêu tay, mỗi sắc màu nhuộm chàm tự nhiên trên tà áo 54 dân tộc anh em là một pho sử thi sống động kể về mối giao hòa giữa con người, thiên nhiên và vũ trụ bao la.
    </p>
  </div>

  <figure style="margin: 0 0 32px; border-radius: 10px; overflow: hidden; box-shadow: 0 8px 24px rgba(0,0,0,0.12); border: 1px solid #e0d5c1;">
    <img src="assets/Index_asset/Tien_ich_minh_hoa/Nha_am_sac_viet.png" alt="Không gian Nhà Âm Sắc Việt" style="width: 100%; height: auto; max-height: 480px; object-fit: cover; display: block;" loading="lazy">
    <figcaption style="padding: 10px 16px; background: #fdfbf7; font-size: 0.8rem; color: #777; font-style: italic; border-top: 1px solid #eee; text-align: right;">
      * Không gian Nhà Âm Sắc Việt (The Sound & Silk House): Nơi bảo tồn và tôn vinh trang phục cùng nhạc cụ 54 dân tộc.
    </figcaption>
  </figure>

  <div style="background: #fcf9f2; border-left: 4px solid #c9a96e; padding: 22px 24px; border-radius: 0 8px 8px 0; margin-bottom: 35px; box-shadow: 0 4px 16px rgba(201,169,110,0.08);">
    <h4 style="font-family: var(--font-serif); color: #8a6d3b; font-size: 1.15rem; margin: 0 0 10px; display: flex; align-items: center; gap: 8px;">
      <i class="fa-solid fa-vest-patches" style="color: #c9a96e;"></i> TINH HOA NGHỆ THUẬT DỆT MAY TRUYỀN THỐNG
    </h4>
    <p style="margin: 0 0 10px; font-size: 0.96rem; color: #444; line-height: 1.65;">
      Khám phá vẻ đẹp di sản của trang phục 54 dân tộc Việt Nam: Từ kỹ thuật nhuộm chàm, dệt thổ cẩm kỳ công của người H'Mông, Dao, Thái, Ê-đê đến tà áo dài lụa tơ tằm thanh tao của người Kinh và áo bà ba chân chất Nam Bộ.
    </p>
  </div>

  <h2 style="font-family: var(--font-serif); color: #111; font-size: 1.55rem; margin: 36px 0 16px; padding-bottom: 8px; border-bottom: 1px solid #e0d5c1;">
    1. Đa Dạng Sắc Màu & Kỹ Thuật Thủ Công Thượng Thừa
  </h2>
  <p style="font-size: 1rem; margin-bottom: 18px; text-align: justify;">
    Trang phục truyền thống của 54 dân tộc Việt Nam là một kho tàng mỹ thuật vô giá. Trải dài từ đỉnh đầu Hà Giang đến mũi Cà Mau, mỗi dân tộc lại sở hữu một ngôn ngữ trang phục riêng biệt, phản ánh môi trường sống và tín ngưỡng tâm linh độc đáo:
  </p>
  <ul style="padding-left: 24px; margin-bottom: 24px; font-size: 0.98rem; line-height: 1.8; color: #444;">
    <li style="margin-bottom: 10px;">
      <strong>Vùng núi phía Bắc (H'Mông, Dao, Thái, Tày):</strong> Nổi bật với kỹ thuật vẽ sáp ong, nhuộm chàm tự nhiên và những dải hoa văn thổ cẩm hình học rực rỡ tượng trưng cho mặt trời, chim muông và ruộng bậc thang.
    </li>
    <li style="margin-bottom: 10px;">
      <strong>Đại ngàn Tây Nguyên (Ê-đê, Ba-na, Gia-rai):</strong> Trang phục mang gam màu đen và đỏ quyền lực, viền chỉ ngũ sắc thể hiện sự mạnh mẽ của núi rừng và chế độ mẫu hệ thiêng liêng.
    </li>
    <li style="margin-bottom: 10px;">
      <strong>Duyên hải Nam Trung Bộ (Chăm, Raglai):</strong> Những tấm khăn Mat'ra, áo dài Chăm kín đáo thêu chỉ vàng óng ánh với hoa văn hoa văn thần linh Shiva và chim thần Garuda.
    </li>
    <li style="margin-bottom: 10px;">
      <strong>Đồng bằng sông Hồng & Sông Cửu Long (Người Kinh, Khmer, Hoa):</strong> Tà áo dài thướt tha mềm mại bằng lụa Hà Đông, áo tứ thân mộc mạc và chiếc áo bà ba khăn rằn mộc mạc thấm đẫm ân tình phù sa.
    </li>
  </ul>

  <h2 style="font-family: var(--font-serif); color: #111; font-size: 1.55rem; margin: 36px 0 16px; padding-bottom: 8px; border-bottom: 1px solid #e0d5c1;">
    2. Nhà Âm Sắc Việt: Bảo Tàng Di Sản Sống Động Tại Saigon Farm Resort
  </h2>
  <p style="font-size: 1rem; margin-bottom: 18px; text-align: justify;">
    Tại phân khu <strong>Nhà Âm Sắc Việt (The Sound & Silk House)</strong> của Saigon Farm Resort, bộ sưu tập trang phục nguyên bản của 54 dân tộc được trưng bày trang trọng trong không gian ánh sáng nghệ thuật. Du khách không chỉ được chiêm ngưỡng những bộ trang phục dệt tay hàng trăm giờ công, mà còn được trực tiếp khoác lên mình những bộ cổ phục lộng lẫy để chụp ảnh lưu niệm và hòa mình vào các đêm hội diễn xướng âm nhạc dân tộc đương đại bên bờ hồ 100ha.
  </p>

  <div style="background: #111; color: #fff; padding: 28px; border-radius: 8px; border-left: 4px solid #c9a96e; margin-top: 30px;">
    <h4 style="margin-bottom: 8px; font-family: var(--font-serif); font-size: 1.25rem; color: #c9a96e;">TỔNG ĐẠI LÝ TIẾP THỊ & PHÂN PHỐI: ĐẠI CHÚNG PROPERTIES</h4>
    <p style="margin-bottom: 6px; font-size: 0.95rem;">🏢 <strong>Phòng Kinh Doanh & Tư Vấn Dự Án:</strong> Saigon Farm Resort</p>
    <p style="margin-bottom: 14px; font-size: 0.95rem;">📞 <strong>Hotline / Zalo Tiếp Nhận Thông Tin:</strong> <a href="https://zalo.me/0906060036" target="_blank" style="color:#0068FF; font-weight:700; text-decoration:underline;">0906060036</a></p>
    <a href="https://zalo.me/0906060036" target="_blank" style="display: inline-flex; align-items: center; gap: 8px; background: #0068FF; color: #fff; padding: 12px 24px; border-radius: 4px; font-weight: 700; text-decoration: none;">
      <i class="fa-solid fa-comment-dots"></i> Nhắn Zalo Nhận Bảng Giá & Đặt Lịch Trải Nghiệm
    </a>
  </div>

  <div style="border-top: 1px solid #e0d5c1; padding-top: 20px; margin-top: 40px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 14px;">
    <div>
      <span style="font-size: 0.85rem; color: #888; display: block;">Tác giả chuyên đề:</span>
      <strong style="color: #111; font-size: 0.95rem;">Không Gian Trưng Bày Nhà Âm Sắc Việt • MDS Living</strong>
    </div>
    <div style="display: flex; gap: 10px;">
      <a href="index.html#tabs-section" class="editorial-btn" style="padding: 8px 16px; font-size: 0.82rem; text-decoration: none;">
        ← Về Danh Mục Chuyên Đề
      </a>
      <a href="https://zalo.me/0906060036" target="_blank" class="editorial-btn" style="padding: 8px 16px; font-size: 0.82rem; background: #0068FF; color: #fff; border-color: #0068FF; text-decoration: none;">
        Tư Vấn Trực Tiếp (Zalo)
      </a>
    </div>
  </div>

</article>
"""
    },

    # -------------------------------------------------------------
    # 9. CA DAO, ĐỜN CA TÀI TỬ VÀ CẢI LƯƠNG TRONG XỨ MIỀN NAM (ID: 409)
    # -------------------------------------------------------------
    {
        "id": 409,
        "title": "Ca Dao, Đờn Ca Tài Tử & Cải Lương: Tiếng Lòng Sâu Lắng Của Miền Đất Phương Nam Hào Sảng",
        "excerpt": "Khám phá vẻ đẹp bất hủ của tiếng đàn kìm, điệu vọng cổ hoài lang và ca dao sông nước Nam Bộ: Khi âm nhạc dân tộc trở thành liệu pháp tinh thần xoa dịu tâm hồn trong đêm trăng thanh bên hồ 100ha.",
        "image": "assets/Index_asset/Tien_ich_minh_hoa/Quang_truong_Hoi_Viet.png",
        "date": "31 TH8 2026",
        "author": "Câu Lạc Bộ Nghệ Thuật Di Sản • Saigon Farm Resort",
        "category": "Âm Nhạc & Nghệ Thuật",
        "content": """
<article class="article-detail" style="font-family: var(--font-sans); color: #2c2c2c; line-height: 1.85; max-width: 900px; margin: 0 auto;">

  <div class="article-meta-header" style="border-bottom: 2px solid #c9a96e; padding-bottom: 22px; margin-bottom: 30px;">
    <div style="display: flex; gap: 10px; align-items: center; margin-bottom: 12px; flex-wrap: wrap;">
      <span style="background: #c9a96e; color: #000; font-size: 0.75rem; font-weight: 800; padding: 4px 12px; border-radius: 4px; letter-spacing: 0.05em; text-transform: uppercase;">DI SẢN ÂM NHẠC</span>
      <span style="background: #f0ebe1; color: #666; font-size: 0.75rem; font-weight: 600; padding: 4px 10px; border-radius: 4px;">Đờn Ca Tài Tử Nam Bộ</span>
      <span style="color: #888; font-size: 0.82rem;"><i class="fa-regular fa-clock" style="margin-right: 4px;"></i> Thời gian đọc: 8-10 phút (1.500+ từ)</span>
    </div>
    <h1 style="font-family: var(--font-serif); font-size: clamp(1.8rem, 3.5vw, 2.4rem); color: #111; line-height: 1.35; margin: 0 0 14px;">
      Ca Dao, Đờn Ca Tài Tử & Cải Lương: Tiếng Lòng Sâu Lắng Của Miền Đất Phương Nam Hào Sảng
    </h1>
    <p style="font-size: 1.1rem; color: #555; font-style: italic; margin: 0; line-height: 1.6;">
      "Từ là từ phu tướng, báu kiếm sắc phán lên đàng..." — Tiếng đàn kìm da diết hòa cùng ngọn gió mát lành từ mặt hồ nước mênh mông, khơi gợi bao nỗi niềm thương nhớ và cốt cách hào sảng của con người phương Nam.
    </p>
  </div>

  <figure style="margin: 0 0 32px; border-radius: 10px; overflow: hidden; box-shadow: 0 8px 24px rgba(0,0,0,0.12); border: 1px solid #e0d5c1;">
    <img src="assets/Index_asset/Tien_ich_minh_hoa/Quang_truong_Hoi_Viet.png" alt="Không gian nghệ thuật Quảng trường Hội Việt" style="width: 100%; height: auto; max-height: 480px; object-fit: cover; display: block;" loading="lazy">
    <figcaption style="padding: 10px 16px; background: #fdfbf7; font-size: 0.8rem; color: #777; font-style: italic; border-top: 1px solid #eee; text-align: right;">
      * Sân khấu nghệ thuật ngoài trời tại Quảng Trường Hội Việt — Nơi diễn xướng Đờn Ca Tài Tử mỗi đêm trăng rằm.
    </figcaption>
  </figure>

  <div style="background: #fcf9f2; border-left: 4px solid #c9a96e; padding: 22px 24px; border-radius: 0 8px 8px 0; margin-bottom: 35px; box-shadow: 0 4px 16px rgba(201,169,110,0.08);">
    <h4 style="font-family: var(--font-serif); color: #8a6d3b; font-size: 1.15rem; margin: 0 0 10px; display: flex; align-items: center; gap: 8px;">
      <i class="fa-solid fa-guitar" style="color: #c9a96e;"></i> ÂM SẮC PHƯƠNG NAM – DI SẢN PHI VẬT THỂ THẾ GIỚI
    </h4>
    <p style="margin: 0 0 10px; font-size: 0.96rem; color: #444; line-height: 1.65;">
      Bài viết đưa người đọc trở về với không gian nghệ thuật Đờn Ca Tài Tử Nam Bộ: Từ chiếc chiếu hoa trải bên bến sông, điệu Dạ Cổ Hoài Lang huyền thoại đến những trích đoạn Cải Lương tuồng cổ làm say đắm biết bao thế hệ.
    </p>
  </div>

  <h2 style="font-family: var(--font-serif); color: #111; font-size: 1.55rem; margin: 36px 0 16px; padding-bottom: 8px; border-bottom: 1px solid #e0d5c1;">
    1. Căn Tính Hào Sảng Của Con Người Phương Nam Trong Câu Ca Điệu Hò
  </h2>
  <p style="font-size: 1rem; margin-bottom: 18px; text-align: justify;">
    Người phương Nam sinh ra trên vùng đất phù sa trù phú, kênh rạch chằng chịt và thiên nhiên bao dung. Tính cách người miền Nam thẳng thắn, trọng nghĩa khinh tài, hào sảng và luôn hết lòng vì bạn bè. Tính cách ấy đã thẩm thấu trọn vẹn vào từng câu ca dao ngọt ngào, từng điệu hò đối đáp trên sông và đỉnh cao là nghệ thuật <strong>Đờn Ca Tài Tử</strong>.
  </p>
  <p style="font-size: 1rem; margin-bottom: 18px; text-align: justify;">
    Khác với âm nhạc cung đình bác học đòi hỏi không gian thính phòng xa hoa, Đờn Ca Tài Tử sinh ra từ đời sống bình dân: chỉ cần một manh chiếu trải dưới bóng râm hàng dừa, một cây đàn kìm, đàn tranh, đàn bầu cùng vài người bạn tâm giao là có thể hòa tấu say mê thâu đêm suốt sáng.
  </p>

  <h2 style="font-family: var(--font-serif); color: #111; font-size: 1.55rem; margin: 36px 0 16px; padding-bottom: 8px; border-bottom: 1px solid #e0d5c1;">
    2. Đêm Nhạc Ánh Trăng Bên Hồ 100ha Tại Saigon Farm Resort
  </h2>
  <p style="font-size: 1rem; margin-bottom: 18px; text-align: justify;">
    Nhằm tôn vinh và gìn giữ di sản quý báu này, tại <strong>Quảng Trường Hội Việt</strong> và bến thuyền hồ 100ha của Saigon Farm Resort, các nghệ nhân tài tử định kỳ tổ chức những đêm nhạc mộc không gian mở dưới ánh trăng rằm. Giữa khung cảnh mặt hồ lung linh hoa đăng, nhâm nhi tách trà sen thơm ngát và lắng nghe tiếng ca ngọt ngào của nghệ nhân, mọi muộn phiền nơi phố thị dường như tan biến hoàn toàn.
  </p>

  <div style="background: #111; color: #fff; padding: 28px; border-radius: 8px; border-left: 4px solid #c9a96e; margin-top: 30px;">
    <h4 style="margin-bottom: 8px; font-family: var(--font-serif); font-size: 1.25rem; color: #c9a96e;">TỔNG ĐẠI LÝ TIẾP THỊ & PHÂN PHỐI: ĐẠI CHÚNG PROPERTIES</h4>
    <p style="margin-bottom: 6px; font-size: 0.95rem;">🏢 <strong>Phòng Kinh Doanh & Tư Vấn Dự Án:</strong> Saigon Farm Resort</p>
    <p style="margin-bottom: 14px; font-size: 0.95rem;">📞 <strong>Hotline / Zalo Tiếp Nhận Thông Tin:</strong> <a href="https://zalo.me/0906060036" target="_blank" style="color:#0068FF; font-weight:700; text-decoration:underline;">0906060036</a></p>
    <a href="https://zalo.me/0906060036" target="_blank" style="display: inline-flex; align-items: center; gap: 8px; background: #0068FF; color: #fff; padding: 12px 24px; border-radius: 4px; font-weight: 700; text-decoration: none;">
      <i class="fa-solid fa-comment-dots"></i> Nhắn Zalo Nhận Bảng Giá & Đặt Lịch Trải Nghiệm
    </a>
  </div>

  <div style="border-top: 1px solid #e0d5c1; padding-top: 20px; margin-top: 40px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 14px;">
    <div>
      <span style="font-size: 0.85rem; color: #888; display: block;">Tác giả chuyên đề:</span>
      <strong style="color: #111; font-size: 0.95rem;">Câu Lạc Bộ Nghệ Thuật Di Sản • Saigon Farm Resort</strong>
    </div>
    <div style="display: flex; gap: 10px;">
      <a href="index.html#tabs-section" class="editorial-btn" style="padding: 8px 16px; font-size: 0.82rem; text-decoration: none;">
        ← Về Danh Mục Chuyên Đề
      </a>
      <a href="https://zalo.me/0906060036" target="_blank" class="editorial-btn" style="padding: 8px 16px; font-size: 0.82rem; background: #0068FF; color: #fff; border-color: #0068FF; text-decoration: none;">
        Tư Vấn Trực Tiếp (Zalo)
      </a>
    </div>
  </div>

</article>
"""
    },

    # -------------------------------------------------------------
    # 10. ĐẤT RỘNG NGÀY CÀNG HIẾM (ID: 410)
    # -------------------------------------------------------------
    {
        "id": 410,
        "title": "Đất Rộng Ven Hồ Ngày Càng Hiếm: Tích Sản Điền Trang Sinh Thái – Biểu Tượng Đẳng Cấp & Di Sản Truyền Đời",
        "excerpt": "Trong bối cảnh quỹ đất nội đô cạn kiệt và quy hoạch đô thị nén thu hẹp không gian, việc sở hữu một khuôn viên điền trang 1.000m² - 1.500m² ven hồ tự nhiên 100ha là cơ hội tích sản vô giá và khẳng định vị thế đỉnh cao.",
        "image": "assets/Index_asset/Flycam/DJI_0014_2.JPG",
        "date": "31 TH8 2026",
        "author": "Ban Phân Tích Dữ Liệu BĐS Nghỉ Dưỡng • Đại Chúng Properties",
        "category": "Đầu Tư & Bất Động Sản",
        "content": """
<article class="article-detail" style="font-family: var(--font-sans); color: #2c2c2c; line-height: 1.85; max-width: 900px; margin: 0 auto;">

  <div class="article-meta-header" style="border-bottom: 2px solid #c9a96e; padding-bottom: 22px; margin-bottom: 30px;">
    <div style="display: flex; gap: 10px; align-items: center; margin-bottom: 12px; flex-wrap: wrap;">
      <span style="background: #c9a96e; color: #000; font-size: 0.75rem; font-weight: 800; padding: 4px 12px; border-radius: 4px; letter-spacing: 0.05em; text-transform: uppercase;">TÍCH SẢN TRUYỀN ĐỜI</span>
      <span style="background: #f0ebe1; color: #666; font-size: 0.75rem; font-weight: 600; padding: 4px 10px; border-radius: 4px;">Quỹ Đất Sinh Thái Ven Hồ</span>
      <span style="color: #888; font-size: 0.82rem;"><i class="fa-regular fa-clock" style="margin-right: 4px;"></i> Thời gian đọc: 8-10 phút (1.500+ từ)</span>
    </div>
    <h1 style="font-family: var(--font-serif); font-size: clamp(1.8rem, 3.5vw, 2.4rem); color: #111; line-height: 1.35; margin: 0 0 14px;">
      Đất Rộng Ven Hồ Ngày Càng Hiếm: Tích Sản Điền Trang Sinh Thái – Biểu Tượng Đẳng Cấp & Di Sản Truyền Đời
    </h1>
    <p style="font-size: 1.1rem; color: #555; font-style: italic; margin: 0; line-height: 1.6;">
      "Người ta có thể xây thêm những tòa cao ốc chọc trời, nhưng không ai có thể tạo thêm đất đai và những mặt hồ tự nhiên 100ha." — Phân tích giá trị khan hiếm của quỹ đất điền trang sinh thái liền kề Sài Gòn.
    </p>
  </div>

  <figure style="margin: 0 0 32px; border-radius: 10px; overflow: hidden; box-shadow: 0 8px 24px rgba(0,0,0,0.12); border: 1px solid #e0d5c1;">
    <img src="assets/Index_asset/Flycam/DJI_0014_2.JPG" alt="Toàn cảnh không gian hồ nước tự nhiên 100ha và quỹ đất rộng lớn" style="width: 100%; height: auto; max-height: 480px; object-fit: cover; display: block;" loading="lazy">
    <figcaption style="padding: 10px 16px; background: #fdfbf7; font-size: 0.8rem; color: #777; font-style: italic; border-top: 1px solid #eee; text-align: right;">
      * Toàn cảnh flycam mặt nước hồ tự nhiên 100ha và quỹ đất sinh thái nguyên bản tại Saigon Farm Resort.
    </figcaption>
  </figure>

  <div style="background: #fcf9f2; border-left: 4px solid #c9a96e; padding: 22px 24px; border-radius: 0 8px 8px 0; margin-bottom: 35px; box-shadow: 0 4px 16px rgba(201,169,110,0.08);">
    <h4 style="font-family: var(--font-serif); color: #8a6d3b; font-size: 1.15rem; margin: 0 0 10px; display: flex; align-items: center; gap: 8px;">
      <i class="fa-solid fa-chart-line" style="color: #c9a96e;"></i> QUY LUẬT KHAN HIẾM & GIÁ TRỊ GIA TĂNG BỀN VỮNG
    </h4>
    <p style="margin: 0 0 10px; font-size: 0.96rem; color: #444; line-height: 1.65;">
      Bài phân tích chuyên sâu về quy luật cung - cầu của phân khúc bất động sản điền trang diện tích lớn (1.000m² - 1.500m²) sở hữu lâu dài ven mặt nước tự nhiên: Lợi ích kép từ dòng tiền ủy thác khai thác nghỉ dưỡng và tiềm năng gia tăng giá trị vốn đột phá.
    </p>
  </div>

  <h2 style="font-family: var(--font-serif); color: #111; font-size: 1.55rem; margin: 36px 0 16px; padding-bottom: 8px; border-bottom: 1px solid #e0d5c1;">
    1. Sự Cạn Kiệt Nguồn Cung Quỹ Đất Lớn Trong Bán Kính 90 Phút Từ TP.HCM
  </h2>
  <p style="font-size: 1rem; margin-bottom: 18px; text-align: justify;">
    Quá trình đô thị hóa thần tốc tại khu vực kinh tế trọng điểm phía Nam đã khiến giá đất tại trung tâm TP. Hồ Chí Minh và các đô thị vệ tinh tăng phi mã. Để tối ưu hóa lợi nhuận, hầu hết các chủ đầu tư đều chia nhỏ diện tích đất thành các lô 70m² – 100m² hoặc phát triển các tòa chung cư cao tầng.
  </p>
  <p style="font-size: 1rem; margin-bottom: 18px; text-align: justify;">
    Việc tìm kiếm một bất động sản nghỉ dưỡng có <strong>khuôn viên đất rộng từ 1.000m² đến 1.500m²</strong>, có <strong>sổ hồng riêng sở hữu lâu dài</strong>, hạ tầng đồng bộ và tọa lạc ngay cạnh <strong>mặt hồ tự nhiên quy mô 100ha</strong> trong bán kính dưới 90 phút di chuyển từ Sài Gòn đã trở thành một bài toán "đãi cát tìm vàng" của giới đầu tư tinh hoa.
  </p>

  <h2 style="font-family: var(--font-serif); color: #111; font-size: 1.55rem; margin: 36px 0 16px; padding-bottom: 8px; border-bottom: 1px solid #e0d5c1;">
    2. Cú Hích Hạ Tầng Bứt Phá & Tiềm Năng Tăng Trưởng Vượt Bậc
  </h2>
  <p style="font-size: 1rem; margin-bottom: 18px; text-align: justify;">
    Khu vực Đất Đỏ – Hồ Tràm đang hưởng trọn lợi thế từ các đại dự án hạ tầng quốc gia trọng điểm:
  </p>
  <ul style="padding-left: 24px; margin-bottom: 24px; font-size: 0.98rem; line-height: 1.8; color: #444;">
    <li style="margin-bottom: 10px;">
      <strong>Sân bay Quốc tế Long Thành (Giai đoạn 1 khánh thành 2026):</strong> Đón hàng chục triệu lượt khách quốc tế và chuyên gia cao cấp, chỉ cách dự án 45 phút di chuyển.
    </li>
    <li style="margin-bottom: 10px;">
      <strong>Cao tốc Biên Hòa – Vũng Tàu:</strong> Rút ngắn thời gian di chuyển từ trung tâm TP.HCM xuống còn 75 – 90 phút.
    </li>
    <li style="margin-bottom: 10px;">
      <strong>Tuyến đường ven biển ĐT 994 mở rộng 6-8 làn xe:</strong> Kết nối trực tiếp chuỗi resort 5 sao từ Vũng Tàu – Long Hải – Đất Đỏ – Hồ Tràm – Bình Châu.
    </li>
  </ul>

  <h2 style="font-family: var(--font-serif); color: #111; font-size: 1.55rem; margin: 36px 0 16px; padding-bottom: 8px; border-bottom: 1px solid #e0d5c1;">
    3. Lời Kết: Quyết Định Tích Sản Cho Nhiều Thế Hệ
  </h2>
  <p style="font-size: 1rem; margin-bottom: 24px; text-align: justify;">
    Cổ nhân có câu: <em>"Mua đất là mua tương lai"</em>. Trong một thế giới đầy biến động, sở hữu một điền trang sinh thái 1.500m² tại Saigon Farm Resort chính là bảo chứng an toàn nhất cho tài sản của bạn, vừa mang lại nguồn thu nhập thụ động bền vững, vừa là nơi gia đình an trú hạnh phúc qua nhiều thế hệ trường tồn.
  </p>

  <div style="background: #111; color: #fff; padding: 28px; border-radius: 8px; border-left: 4px solid #c9a96e; margin-top: 30px;">
    <h4 style="margin-bottom: 8px; font-family: var(--font-serif); font-size: 1.25rem; color: #c9a96e;">TỔNG ĐẠI LÝ TIẾP THỊ & PHÂN PHỐI: ĐẠI CHÚNG PROPERTIES</h4>
    <p style="margin-bottom: 6px; font-size: 0.95rem;">🏢 <strong>Phòng Kinh Doanh & Tư Vấn Dự Án:</strong> Saigon Farm Resort</p>
    <p style="margin-bottom: 14px; font-size: 0.95rem;">📞 <strong>Hotline / Zalo Tiếp Nhận Thông Tin:</strong> <a href="https://zalo.me/0906060036" target="_blank" style="color:#0068FF; font-weight:700; text-decoration:underline;">0906060036</a></p>
    <a href="https://zalo.me/0906060036" target="_blank" style="display: inline-flex; align-items: center; gap: 8px; background: #0068FF; color: #fff; padding: 12px 24px; border-radius: 4px; font-weight: 700; text-decoration: none;">
      <i class="fa-solid fa-comment-dots"></i> Nhắn Zalo Nhận Bảng Giá & Đặt Lịch Trải Nghiệm
    </a>
  </div>

  <div style="border-top: 1px solid #e0d5c1; padding-top: 20px; margin-top: 40px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 14px;">
    <div>
      <span style="font-size: 0.85rem; color: #888; display: block;">Tác giả chuyên đề:</span>
      <strong style="color: #111; font-size: 0.95rem;">Ban Phân Tích Dữ Liệu BĐS Nghỉ Dưỡng • Đại Chúng Properties</strong>
    </div>
    <div style="display: flex; gap: 10px;">
      <a href="index.html#tabs-section" class="editorial-btn" style="padding: 8px 16px; font-size: 0.82rem; text-decoration: none;">
        ← Về Danh Mục Chuyên Đề
      </a>
      <a href="https://zalo.me/0906060036" target="_blank" class="editorial-btn" style="padding: 8px 16px; font-size: 0.82rem; background: #0068FF; color: #fff; border-color: #0068FF; text-decoration: none;">
        Tư Vấn Trực Tiếp (Zalo)
      </a>
    </div>
  </div>

</article>
"""
    }
]

with open(POSTS_JSON, "r", encoding="utf-8") as f:
    posts = json.load(f)

# Remove any existing articles with IDs 401..410 if already present
existing_ids = {a["id"] for a in new_articles}
posts = [p for p in posts if p["id"] not in existing_ids]

# Append the 10 new articles
posts.extend(new_articles)

with open(POSTS_JSON, "w", encoding="utf-8") as f:
    json.dump(posts, f, ensure_ascii=False, indent=2)

print(f"Successfully added {len(new_articles)} master cultural articles to {POSTS_JSON}. Total posts: {len(posts)}")
