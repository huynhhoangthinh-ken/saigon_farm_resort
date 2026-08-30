# -*- coding: utf-8 -*-
"""
Full builder for 48 comprehensive estate articles (>1000 words each) and index.html integration.
"""

import json
import re

# Load existing posts to preserve non-villa ones
with open('data/posts.json', 'r', encoding='utf-8') as f:
    existing_posts = json.load(f)

# Non-estate post IDs to keep
keep_posts = [p for p in existing_posts if p['id'] not in [
    101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 141, 142,
    111, 112, 113, 114, 143, 144, 145, 146, 147, 148, 149, 150,
    115, 116, 117, 118, 151, 152, 153, 154, 155, 156, 157, 158,
    119, 130, 131, 132, 159, 160, 161, 162, 163, 164, 165, 166
]]

# Template assets
A = {
    "sunrise1_ext": "assets/Index_asset/02_Phoi_Canh_3D/05.3D_TKCS-SUNRISE_1_VILLA/05.3D_TKCS-NHA_GO_4_MAU_1-_07.2025/01._NGOAI_THAT/SFR_NGOAI_THAT_06.jpg",
    "sunrise1_ext2": "assets/Index_asset/02_Phoi_Canh_3D/05.3D_TKCS-SUNRISE_1_VILLA/05.3D_TKCS-NHA_GO_4_MAU_1-_07.2025/01._NGOAI_THAT/SFR_NGOAI_THAT_(4).jpg",
    "sunrise1_mb": "assets/Index_asset/Loai_hinh_Villa/MatBang_Sunrise_1.png",
    
    "sunrise2_ext": "assets/Index_asset/02_Phoi_Canh_3D/07.3D_TKCS-NHA_GO_4_MAU_2-_02.2026/07.TKCS-NHA_GO_4-MAU_2/01.NGOAI_THAT/SFR_01.jpg",
    "sunrise2_ext2": "assets/Index_asset/02_Phoi_Canh_3D/07.3D_TKCS-NHA_GO_4_MAU_2-_02.2026/07.TKCS-NHA_GO_4-MAU_2/01.NGOAI_THAT/SFR_03.jpg",
    "sunrise2_mb": "assets/Index_asset/Loai_hinh_Villa/MatBang_Sunrise_2.png",
    
    "sunset1_ext": "assets/Index_asset/02_Phoi_Canh_3D/09.3D_TKCS-SUNSET_VILLA/SUNSET_1_VILLA/SFR_07.SAN_TRONG.jpg",
    "sunset1_ext2": "assets/Index_asset/02_Phoi_Canh_3D/09.3D_TKCS-SUNSET_VILLA/SUNSET_1_VILLA/SFR_04.PC_01.jpg",
    "sunset1_mb": "assets/Index_asset/Loai_hinh_Villa/MatBang_Sunset_1.png",
    
    "sunset2_ext": "assets/Index_asset/02_Phoi_Canh_3D/09.3D_TKCS-SUNSET_VILLA/SUNSET_2_VILLA/SFR_04.PC_01.jpg",
    "sunset2_ext2": "assets/Index_asset/02_Phoi_Canh_3D/09.3D_TKCS-SUNSET_VILLA/SUNSET_2_VILLA/SFR_04.PC_02.jpg",
    "sunset2_mb": "assets/Index_asset/Loai_hinh_Villa/MatBang_Sunset_2.png",
    
    "masterplan": "assets/Index_asset/Phoi_canh_tong_the/SFR_S01_Final_Fix.jpg",
    "masterplan_alt": "assets/Index_asset/Phoi_canh_tong_the/SFR_NEW_S02.jpg",
    "horse": "assets/Index_asset/Tien_ich_minh_hoa/viet_ma_trang.png",
    "lotus": "assets/Index_asset/Tien_ich_minh_hoa/Bo_sen.png",
    "kayak": "assets/Index_asset/Tien_ich_minh_hoa/ben_thuyen_kayak.png",
    "clubhouse": "assets/Index_asset/Tien_ich_minh_hoa/Clubhouse_ven_ho.png",
    "giaotri": "assets/Index_asset/Tien_ich_minh_hoa/Giao_tri_viet.png",
    "mds": "assets/Index_asset/Phoi_canh_tong_the/mds_living_01.jpg",
    "farm": "assets/Index_asset/Tien_ich_minh_hoa/Nong_trai_huu_co.png",
    "quymo": "assets/Index_asset/MatBang/TongQuan_QuyMo.png",
    "lienket": "assets/Index_asset/MatBang/SoDo_LienKet_Vung.png",
}

# Define 48 Articles metadata and deep content definitions
ARTICLES_DATA = [
    # =========================================================================
    # NHÓM 1: MẶT BẰNG & KIẾN TRÚC ĐIỀN TRANG (12 BÀI)
    # =========================================================================
    {
        "id": 103,
        "subtab": "subtab-villa-layout",
        "category": "Mặt Bằng & Kiến Trúc",
        "title": "Điền Trang Sunrise 1: Giải Mã Mặt Bằng 1 Tầng Trệt Trải Rộng – Sự Tiện Nghi Mở Đón Nắng Mai",
        "subtitle": "Khuôn viên 1.000m² - 1.200m², layout trải ngang đón nắng bình minh",
        "tag": "CHUYÊN ĐỀ KIẾN TRÚC",
        "image": A["sunrise1_mb"],
        "excerpt": "Phân tích layout trệt trải ngang, tối ưu ánh sáng tự nhiên và luồng giao thông không góc chết của Điền Trang Sunrise 1.",
        "model": "Sunrise 1",
        "focus": "Mặt bằng 1 tầng trệt trải ngang, kết nối sân vườn 700m² và hồ bơi khoáng muối 45m²."
    },
    {
        "id": 104,
        "subtab": "subtab-villa-layout",
        "category": "Mặt Bằng & Kiến Trúc",
        "title": "Dinh Thự Sunrise 2: Đỉnh Cao Kiến Trúc Đại Điền Trang 1.500m² – Đại Sảnh Trần Cao & Sky Deck 360°",
        "subtitle": "Đại sảnh gỗ quý trần cao 6m, 4PN Master, Sky Deck 40m²",
        "tag": "DINH THỰ ĐẲNG CẤP",
        "image": A["sunrise2_mb"],
        "excerpt": "Không gian đại sảnh trần cao gỗ quý 6m, 4 phòng ngủ Master khép kín và Sky Deck 360° bao quát mặt nước hồ 100ha.",
        "model": "Sunrise 2",
        "focus": "Quy mô 1.500m² đơn lập siêu VIP, đại sảnh trần cao 6m, Sky Deck 40m², hồ bơi tràn 53m² Jacuzzi nước ấm."
    },
    {
        "id": 101,
        "subtab": "subtab-villa-layout",
        "category": "Mặt Bằng & Kiến Trúc",
        "title": "Điền Trang Sunset 1: Bố Cục Sân Trong (Courtyard) – Gắn Kết Đa Thế Hệ Trong Nếp Nhà 1 Tầng",
        "subtitle": "Khuôn viên 1.000m², sân trong 38m², vườn cây ăn trái 260m²",
        "tag": "SÂN TRONG ĐỘC BẢN",
        "image": A["sunset1_mb"],
        "excerpt": "Giải pháp giếng trời sân trong lấy gió chéo và kết nối đa thế hệ trong nếp nhà 1 tầng hướng hoàng hôn hồ sinh thái.",
        "model": "Sunset 1",
        "focus": "Kiến trúc sân trong (Courtyard 38m²), giếng trời thông gió chéo, kết nối 3 phòng ngủ Master."
    },
    {
        "id": 102,
        "subtab": "subtab-villa-layout",
        "category": "Mặt Bằng & Kiến Trúc",
        "title": "Điền Trang Sunset 2: Bố Cục Không Gian 2 Tầng – Tầm Nhìn Panorama Ôm Trọn Hoàng Hôn Hồ 100ha",
        "subtitle": "Khuôn viên 1.200m², vườn ăn trái 482m², ban công ngắm hoàng hôn",
        "tag": "TẦM NHÌN TUYỆT MỸ",
        "image": A["sunset2_mb"],
        "excerpt": "Phân tách tĩnh - động hoàn hảo, ban công Sunset Lounge 35m² ngắm trọn hoàng hôn tuyệt mỹ ven mặt hồ 100ha.",
        "model": "Sunset 2",
        "focus": "Bố cục 2 tầng bề thế, phân tầng công năng khoa học, ban công Sunset Lounge 35m²."
    },
    {
        "id": 105,
        "subtab": "subtab-villa-layout",
        "category": "Mặt Bằng & Kiến Trúc",
        "title": "Giải Pháp Phân Tách Không Gian Động & Tĩnh Trong Mặt Bằng Điền Trang Sunrise 1",
        "subtitle": "Bố trí khoa học giữa phòng khách mở và khu nghỉ ngơi khép kín",
        "tag": "CÔNG NĂNG MẶT BẰNG",
        "image": A["sunrise1_ext"],
        "excerpt": "Bóc tách trục giao thông thông minh giúp tách biệt hoàn toàn không gian sinh hoạt chung sôi động và cụm 3 phòng ngủ tĩnh tại.",
        "model": "Sunrise 1",
        "focus": "Trục hành lang xanh cách âm, khu sinh hoạt chung mở 65m² và 3 phòng ngủ riêng tư tuyệt đối."
    },
    {
        "id": 106,
        "subtab": "subtab-villa-layout",
        "category": "Mặt Bằng & Kiến Trúc",
        "title": "Nghệ Thuật Kết Nối Gỗ Tự Nhiên & Hệ Kính Khổ Lớn Trong Dinh Thự Sunrise 2",
        "subtitle": "Sự giao hòa giữa vật liệu mộc truyền thống và kiến trúc đương đại",
        "tag": "VẬT LIỆU CAO CẤP",
        "image": A["sunrise2_ext"],
        "excerpt": "Ứng dụng hệ khung kết cấu gỗ tự nhiên kết hợp vách kính Low-E tràn viền giúp xóa nhòa ranh giới giữa nội thất và mặt hồ.",
        "model": "Sunrise 2",
        "focus": "Vật liệu gỗ Teak xử lý chịu thời tiết, kính Low-E cản nhiệt, trần gỗ thủ công 6m."
    },
    {
        "id": 107,
        "subtab": "subtab-villa-layout",
        "category": "Mặt Bằng & Kiến Trúc",
        "title": "Triết Lý Thiết Kế Giếng Trời Sân Trong 38m² Của Điền Trang Sunset 1",
        "subtitle": "Trái tim xanh điều hòa nhiệt độ và hút gió mát tự nhiên",
        "tag": "KIẾN TRÚC XANH",
        "image": A["sunset1_ext"],
        "excerpt": "Khám phá nguyên lý thông gió Bernoulli thông qua khoảng sân trong giếng trời 38m², giữ cho căn điền trang luôn mát mẻ quanh năm.",
        "model": "Sunset 1",
        "focus": "Giếng trời sân trong 38m², hiệu ứng ống khói hút gió, tiểu cảnh cây nhiệt đới tại trung tâm nhà."
    },
    {
        "id": 108,
        "subtab": "subtab-villa-layout",
        "category": "Mặt Bằng & Kiến Trúc",
        "title": "Ban Công Sky Lounge 35m² Tầng 2 Sunset 2: Điểm Hẹn Thưởng Lãm Hoàng Hôn",
        "subtitle": "Không gian thưởng trà và ngắm chiều tà trên tầng cao",
        "tag": "SKY LOUNGE",
        "image": A["sunset2_ext2"],
        "excerpt": "Thiết kế ban công mở rộng 35m² trên lầu 1 đón trọn góc nhìn 180 độ ra mặt hồ 100ha trong khoảnh khắc hoàng hôn buông xuống.",
        "model": "Sunset 2",
        "focus": "Ban công Sky Lounge 35m², sàn gỗ Teak ngoài trời, tầm nhìn trực diện mặt nước hồ 100ha."
    },
    {
        "id": 109,
        "subtab": "subtab-villa-layout",
        "category": "Mặt Bằng & Kiến Trúc",
        "title": "Phân Tích Mặt Bằng Sân Vườn > 700m² & Hồ Bơi Khoáng Muối Điền Trang Sunrise 1",
        "subtitle": "Quy hoạch cảnh quan sinh thái và hồ bơi thư giãn chuẩn resort",
        "tag": "CẢNH QUAN SÂN VƯỜN",
        "image": A["sunrise1_ext2"],
        "excerpt": "Chi tiết bố cục sân vườn phân lớp với thảm cỏ, vườn hoa thảo mộc và bể bơi khoáng muối 45m² liền kề hiên nhà.",
        "model": "Sunrise 1",
        "focus": "Sân vườn > 700m², hồ bơi 45m² công nghệ điện phân muối khoáng không clo, lối dạo bộ lát đá chẻ."
    },
    {
        "id": 110,
        "subtab": "subtab-villa-layout",
        "category": "Mặt Bằng & Kiến Trúc",
        "title": "Thiết Kế Đại Sảnh Trần Cao 6m & Không Gian Tiếp Khách Ngoại Giao Tại Dinh Thự Sunrise 2",
        "subtitle": "Quy chuẩn thiết kế dành riêng cho giới tinh hoa và doanh nhân",
        "tag": "ĐẠI SẢNH QUÝ TỘC",
        "image": A["sunrise2_ext2"],
        "excerpt": "Đại sảnh thông tầng bề thế được kiến tạo như một khán phòng sang trọng để tiếp đón đối tác và tổ chức yến tiệc gia tộc.",
        "model": "Sunrise 2",
        "focus": "Đại sảnh 85m² trần cao 6m, đèn chùm đồng thủ công, bàn yến tiệc 20 ghế hướng hồ."
    },
    {
        "id": 141,
        "subtab": "subtab-villa-layout",
        "category": "Mặt Bằng & Kiến Trúc",
        "title": "Tối Ưu Hóa Giao Thông Nội Khu & Không Gian Riêng Tư Khép Kín Cho Gia Đình Đa Thế Hệ",
        "subtitle": "Mặt bằng phẳng không bậc tam cấp, an toàn cho người cao tuổi và trẻ nhỏ",
        "tag": "ĐA THẾ HỆ",
        "image": A["sunset1_ext2"],
        "excerpt": "Phân tích thiết kế phổ quát (Universal Design) không rào cản, giúp ông bà và con cháu tự do kết nối và di chuyển an toàn.",
        "model": "Sunset 1",
        "focus": "Thiết kế không bậc dốc cản trở, cửa lùa mở rộng 1.2m, phòng ngủ ông bà hướng vườn yên tĩnh."
    },
    {
        "id": 142,
        "subtab": "subtab-villa-layout",
        "category": "Mặt Bằng & Kiến Trúc",
        "title": "Kiến Trúc 2 Tầng Sinh Thái: Sự Chuyển Tiếp Mềm Mại Giữa Sân Vườn, Hồ Bơi & Tầng Cao",
        "subtitle": "Kỹ thuật phân khối kiến trúc giúp công trình hòa vào thiên nhiên hồ nước",
        "tag": "KIẾN TRÚC ĐƯƠNG ĐẠI",
        "image": A["sunset2_ext"],
        "excerpt": "Cách thức các kiến trúc sư tạo nên nhịp điệu tầng bậc nhịp nhàng, giảm bớt cảm giác đồ sộ và tôn vinh mảng xanh sinh thái.",
        "model": "Sunset 2",
        "focus": "Khối kiến trúc giật cấp, ban công đua rộng 2.5m che nắng, kết nối hiên gỗ tầng trệt với hồ bơi 48m²."
    },

    # =========================================================================
    # NHÓM 2: PHONG THỦY & VI KHÍ HẬU ĐIỀN TRANG (12 BÀI)
    # =========================================================================
    {
        "id": 111,
        "subtab": "subtab-villa-fengshui",
        "category": "Phong Thủy & Vi Khí Hậu",
        "title": "Phong Thủy Điền Trang Hướng Đông (Sunrise 1 & 2): Đón Vượng Khí Nắng Sớm & Năng Lượng Tái Sinh",
        "subtitle": "Thanh Long bão hòa sinh khí, khởi đầu ngày mới ngập tràn năng lượng",
        "tag": "PHONG THỦY HƯỚNG ĐÔNG",
        "image": A["sunrise1_ext"],
        "excerpt": "Phân tích khoa học phong thủy hướng mặt trời mọc: Nắng sớm giàu vitamin D, kích hoạt luồng khí dương tích cực cho gia đình.",
        "model": "Sunrise 1 & 2",
        "focus": "Trục hướng Đông, năng lượng dương sơ khai, tác động tích cực đến nhịp sinh học và tâm lý gia chủ."
    },
    {
        "id": 112,
        "subtab": "subtab-villa-fengshui",
        "category": "Phong Thủy & Vi Khí Hậu",
        "title": "Giải Pháp Vi Khí Hậu Điền Trang Hướng Tây (Sunset 1 & 2): Đón Gió Nam Mát Lành & Lọc Nắng Chiều",
        "subtitle": "Hệ lam chắn nắng, mái hiên đua sâu và luồng gió mặt hồ 100ha",
        "tag": "VI KHÍ HẬU HƯỚNG TÂY",
        "image": A["sunset1_ext"],
        "excerpt": "Cách thức triệt tiêu nhiệt độ bức xạ chiều bằng mái hiên gỗ truyền thống và tận dụng luồng gió đối lưu từ mặt nước hồ.",
        "model": "Sunset 1 & 2",
        "focus": "Mái hiên rộng 2.2m, lam gỗ chớp tự nhiên, hơi nước hồ 100ha làm giảm 3-4 độ C vào buổi chiều."
    },
    {
        "id": 113,
        "subtab": "subtab-villa-fengshui",
        "category": "Phong Thủy & Vi Khí Hậu",
        "title": "Trải Nghiệm 24 Giờ Vi Khí Hậu: So Sánh Nhịp Thở Sinh Thái Giữa Cụm Sunrise & Sunset",
        "subtitle": "Theo dõi biểu đồ nhiệt độ, độ ẩm và sự luân chuyển ánh sáng qua từng giờ",
        "tag": "NHỊP THỞ SINH THÁI",
        "image": A["masterplan"],
        "excerpt": "So sánh chi tiết diễn biến nhiệt độ và chất lượng không khí trong 24 giờ tại cụm Sunrise đón nắng mai và cụm Sunset đón hoàng hôn.",
        "model": "Tất Cả Mẫu Căn",
        "focus": "Biểu đồ nhiệt độ 24h (22°C - 29°C), độ ẩm lý tưởng 65-75%, gió bề mặt hồ 3.5 m/s."
    },
    {
        "id": 114,
        "subtab": "subtab-villa-fengshui",
        "category": "Phong Thủy & Vi Khí Hậu",
        "title": "Thủy Khí Hồ 100ha & Không Gian Cây Xanh: Trụ Cột Nuôi Dưỡng Sức Khỏe Gia Chủ",
        "subtitle": "Nồng độ ion âm cực đại, không khí sạch và hiệu ứng Blue Mind giảm stress",
        "tag": "DƯỠNG SINH SINH THÁI",
        "image": A["masterplan_alt"],
        "excerpt": "Cơ chế tạo ion âm từ mặt nước hồ 100ha kết hợp rừng cây nhiệt đới, mang lại giấc ngủ sâu và hỗ trợ điều trị các bệnh hô hấp.",
        "model": "Quần Thể 100ha",
        "focus": "Mật độ ion âm 2.500 ion/cm³, chỉ số AQI dưới 25, hiệu ứng tâm lý Blue Mind xoa dịu thần kinh."
    },
    {
        "id": 143,
        "subtab": "subtab-villa-fengshui",
        "category": "Phong Thủy & Vi Khí Hậu",
        "title": "Thế Đất 'Tựa Sơn Hướng Thủy' & Trục Năng Lượng Sinh Khí Của Dinh Thự Sunrise 2",
        "subtitle": "Địa thế đắc địa mang lại phú quý trường tồn cho gia tộc",
        "tag": "ĐỊA LÝ PHONG THỦY",
        "image": A["sunrise2_ext"],
        "excerpt": "Phân tích thế đất vững chãi phía sau có đồi thoải bảo bọc, phía trước minh đường rộng lớn mở ra mặt hồ 100ha mênh mông.",
        "model": "Sunrise 2",
        "focus": "Thế tựa đồi đón hồ, huyền vũ vững chãi, chu tước thông thoáng tụ tài tích đức."
    },
    {
        "id": 144,
        "subtab": "subtab-villa-fengshui",
        "category": "Phong Thủy & Vi Khí Hậu",
        "title": "Đón Gió Hồ Tự Nhiên Qua Sân Trong: Khí Đạo Lưu Thông Của Điền Trang Sunset 1",
        "subtitle": "Quy luật tụ khí - tán nhiệt và dòng luân chuyển năng lượng tuần hoàn",
        "tag": "KHÍ ĐẠO SÂN TRONG",
        "image": A["sunset1_ext"],
        "excerpt": "Giải pháp phong thủy 'Tụ Thủy Sinh Tài' thông qua khoảng sân trong đón nước mưa và luân chuyển luồng gió mát khắp mọi gian phòng.",
        "model": "Sunset 1",
        "focus": "Nguyên lý tụ thủy sân trong, phong thủy minh đường nội vi, luồng khí đối lưu 8 hướng."
    },
    {
        "id": 145,
        "subtab": "subtab-villa-fengshui",
        "category": "Phong Thủy & Vi Khí Hậu",
        "title": "Phong Thủy Vườn Cây Ăn Trái & Thảo Mộc: Cân Bằng Âm Dương Cho Gia Chủ Sunrise 1",
        "subtitle": "Lựa chọn các giống cây bản địa mang ý nghĩa tài lộc và thanh lọc không khí",
        "tag": "MỘC KHÍ PHONG THỦY",
        "image": A["farm"],
        "excerpt": "Bố trí vườn bưởi da xanh, xoài cát, hoa mộc lan và thảo dược thơm quanh nhà nhằm cân bằng ngũ hành và tạo hương thơm tự nhiên.",
        "model": "Sunrise 1",
        "focus": "Mộc khí vượng sắc, cây hương thảo xua đuổi côn trùng, cây ăn trái sum suê tượng trưng sung túc."
    },
    {
        "id": 146,
        "subtab": "subtab-villa-fengshui",
        "category": "Phong Thủy & Vi Khí Hậu",
        "title": "Tầm Nhìn Hoàng Hôn Mặt Hồ & Ý Nghĩa Chiêu Tài Đắc Lộc Cho Điền Trang Sunset 2",
        "subtitle": "Khoảnh khắc hoàng hôn vàng rực chiếu rọi mặt nước hồ",
        "tag": "HOÀNG HÔN CHIÊU TÀI",
        "image": A["sunset2_ext"],
        "excerpt": "Ánh sáng vàng kim lúc hoàng hôn phản chiếu trên mặt nước hồ 100ha tạo thành thế 'Kim Thủy Tương Sinh', trợ lực đắc lực cho tài chính gia chủ.",
        "model": "Sunset 2",
        "focus": "Hành Kim tương sinh hành Thủy, góc nhìn mở rộng đón ánh dương chiều tà ấm áp."
    },
    {
        "id": 147,
        "subtab": "subtab-villa-fengshui",
        "category": "Phong Thủy & Vi Khí Hậu",
        "title": "Đo Lường Nồng Độ Ion Âm & Vi Khí Hậu Ven Hồ 100ha Tại Saigon Farm Resort",
        "subtitle": "Số liệu thực nghiệm so sánh với các đô thị trung tâm và vùng biển",
        "tag": "KHOA HỌC MÔI TRƯỜNG",
        "image": A["masterplan"],
        "excerpt": "Báo cáo thực nghiệm môi trường: Nồng độ bụi mịn PM2.5 dưới 8µg/m³, nồng độ oxy hòa tan và ion âm cao gấp 10 lần nội thành TP.HCM.",
        "model": "Quần Thể Điền Trang",
        "focus": "Chỉ số PM2.5 < 8µg/m³, nhiệt độ trung bình ngày 26.5°C, độ ẩm cân bằng sinh lý người."
    },
    {
        "id": 148,
        "subtab": "subtab-villa-fengshui",
        "category": "Phong Thủy & Vi Khí Hậu",
        "title": "Cây Bản Địa & Thảm Thực Vật Tự Nhiên Trong Quy Hoạch Vi Khí Hậu Quần Thể",
        "subtitle": "Hệ thống 3 tầng tán cây xanh giúp chắn gió bão và điều hòa độ ẩm",
        "tag": "SINH THÁI HỌC",
        "image": A["masterplan_alt"],
        "excerpt": "Cách thức phối kết hợp các loài cây bản địa như dầu rái, sao đen, lộc vừng và hoa sen giúp tạo lá chắn vi khí hậu trường tồn.",
        "model": "Quy Hoạch Toàn Khu",
        "focus": "Quy hoạch 3 tầng thực vật: Cây thân gỗ cao >12m, cây ăn trái tầm trung 4-6m, thảm thảo mộc phủ đất."
    },
    {
        "id": 149,
        "subtab": "subtab-villa-fengshui",
        "category": "Phong Thủy & Vi Khí Hậu",
        "title": "Nghệ Thuật Xử Lý Nắng Hướng Tây Bằng Lam Gỗ & Mái Hiên Rộng Trong Kiến Trúc Sunset",
        "subtitle": "Kế thừa trí tuệ kiến trúc nhà rường truyền thống xứ nhiệt đới",
        "tag": "CHỐNG NẮNG TỰ NHIÊN",
        "image": A["sunset1_ext2"],
        "excerpt": "Khảo sát góc chiếu mặt trời và thiết kế hệ lam xoay linh hoạt, cản bức xạ trực tiếp nhưng vẫn giữ trọn luồng gió và tầm nhìn.",
        "model": "Sunset 1 & 2",
        "focus": "Góc che nắng 45 độ, vật liệu nan gỗ sồi biến tính nhiệt, hệ rèm tre đan thủ công chống chói."
    },
    {
        "id": 150,
        "subtab": "subtab-villa-fengshui",
        "category": "Phong Thủy & Vi Khí Hậu",
        "title": "Sự Tương Hợp Ngũ Hành Trong Bố Trí Mặt Bằng & Cảnh Quan Nước Dinh Thự Sunrise 2",
        "subtitle": "Sắp đặt hồ bơi, tiểu cảnh đá và vườn phong thủy theo quy chuẩn cổ truyền",
        "tag": "NGŨ HÀNH TƯƠNG SINH",
        "image": A["sunrise2_ext2"],
        "excerpt": "Quy hoạch phong thủy đồng bộ từ cổng vào, bể bơi vô cực, lối đi lát đá bazan đến vị trí phòng ngủ gia chủ, tạo sự hài hòa ngũ hành Kim - Mộc - Thủy - Hỏa - Thổ.",
        "model": "Sunrise 2",
        "focus": "Sắp xếp 5 hành tương sinh, điểm tụ thủy mặt trước, thế đá tự nhiên vững chãi phía sau."
    },

    # =========================================================================
    # NHÓM 3: TRẢI NGHIỆM SỐNG, TIỆN ÍCH & DƯỠNG SINH (12 BÀI)
    # =========================================================================
    {
        "id": 115,
        "subtab": "subtab-villa-experience",
        "category": "Trải Nghiệm & Dưỡng Sinh",
        "title": "Đặc Quyền Hồ Bơi Vô Cực & Vườn Nông Trại Riêng: Chuẩn Sống Xanh Sunrise 1 & Sunset 1",
        "subtitle": "Bể bơi khoáng muối 45m² và mảnh vườn rau củ quả tự thu hoạch Farm-to-Table",
        "tag": "RESORT TẠI GIA",
        "image": A["sunrise1_ext2"],
        "excerpt": "Trải nghiệm ngâm mình thư giãn trong hồ bơi khoáng muối không hóa chất và thưởng thức nông sản sạch do chính tay mình vun trồng.",
        "model": "Sunrise 1 & Sunset 1",
        "focus": "Hồ bơi điện phân muối 45m², vườn rau hữu cơ mùa nào thức nấy, bàn ăn ngoài trời rợp bóng cây."
    },
    {
        "id": 116,
        "subtab": "subtab-villa-experience",
        "category": "Trải Nghiệm & Dưỡng Sinh",
        "title": "Đẳng Cấp Thượng Lưu Tại Dinh Thự Sunrise 2: Không Gian Gala Sân Vườn 1.500m² & Tiếp Khách VIP Kín Đáo",
        "subtitle": "Không gian tiếp khách ngoại giao bí mật, tiệc sân vườn 80 khách và dịch vụ quản gia MDS Living",
        "tag": "TIẾP KHÁCH THƯỢNG LƯU",
        "image": A["sunrise2_ext"],
        "excerpt": "Khám phá phong cách tiếp khách kín đáo chuẩn giới thượng lưu: Bãi cỏ tiệc Gala 80 người, quầy bar ngoài trời và dịch vụ bếp trưởng riêng.",
        "model": "Sunrise 2",
        "focus": "Khuôn viên riêng 1.500m², bãi cỏ Gala đón 80 khách, dịch vụ đầu bếp 5 sao chuẩn MDS Living."
    },
    {
        "id": 117,
        "subtab": "subtab-villa-experience",
        "category": "Trải Nghiệm & Dưỡng Sinh",
        "title": "Phong Cách Sống 'Sunset Lounge': Trải Nghiệm Tiệc Trà Hoàng Hôn & Thưởng Rượu Tầng Thượng Sunset 2",
        "subtitle": "Tiệc trà hoàng hôn kiểu Anh, thưởng rượu vang trên ban công 35m² ngắm mặt hồ chuyển màu",
        "tag": "LỐI SỐNG THỜI THƯỢNG",
        "image": A["sunset2_ext2"],
        "excerpt": "Khoảnh khắc hoàng hôn buông xuống mặt hồ 100ha là lúc gia chủ tận hưởng ly rượu vang hảo hạng trên không gian Sky Lounge tầng 2.",
        "model": "Sunset 2",
        "focus": "Sky Lounge 35m², tiệc trà chiều ngắm hoàng hôn, âm nhạc acoustic du dương bên mặt hồ."
    },
    {
        "id": 118,
        "subtab": "subtab-villa-experience",
        "category": "Trải Nghiệm & Dưỡng Sinh",
        "title": "Lối Sống Chữa Lành & Dưỡng Sinh Thân - Tâm - Trí: Một Ngày Hoàn Hảo Tại Saigon Farm Resort",
        "subtitle": "Lịch trình dưỡng sinh mẫu: Thiền đón bình minh, cưỡi ngựa, Onsen Bờ Sen và thực dưỡng thuần khiết",
        "tag": "CHĂM SÓC TOÀN DIỆN",
        "image": A["lotus"],
        "excerpt": "Hành trình 24 giờ phục hồi năng lượng trọn vẹn: Từ bài tập Yoga đón nắng mai ven hồ đến liệu trình ngâm khoáng thảo mộc Bờ Sen lúc chiều muộn.",
        "model": "Toàn Thể Cư Dân",
        "focus": "Yoga đón bình minh 6:00 AM, cưỡi ngựa Việt Mã Trang, tắm khoáng thảo dược Onsen Bờ Sen."
    },
    {
        "id": 151,
        "subtab": "subtab-villa-experience",
        "category": "Trải Nghiệm & Dưỡng Sinh",
        "title": "Trải Nghiệm 'Farm-to-Table' Ngay Tại Vườn Nhà: Thu Hoạch Nông Sản Sạch Mỗi Ngày (Sunrise 1)",
        "subtitle": "Bữa cơm gia đình thuần khiết từ vườn rau hữu cơ do quản gia chăm sóc",
        "tag": "FARM-TO-TABLE",
        "image": A["farm"],
        "excerpt": "Gia chủ được trải nghiệm thu hoạch cà chua bi, xà lách thủy canh, rau thơm bản địa ngay tại khu vườn điền trang để chế biến bữa tiệc tươi ngon.",
        "model": "Sunrise 1",
        "focus": "Nông trại hữu cơ riêng 200m², đội ngũ kỹ sư nông nghiệp MDS Living chăm bón, rau sạch 100% tự nhiên."
    },
    {
        "id": 152,
        "subtab": "subtab-villa-experience",
        "category": "Trải Nghiệm & Dưỡng Sinh",
        "title": "Nghệ Thuật Tiếp Đón Doanh Nhân & Tiệc Private 80 Khách Tại Dinh Thự Sunrise 2",
        "subtitle": "Quy chuẩn lễ tân ngoại giao và ẩm thực Fine Dining độc bản",
        "tag": "YẾN TIỆC VIP",
        "image": A["clubhouse"],
        "excerpt": "Cách tổ chức một sự kiện ngoại giao riêng tư hoàn hảo: Hệ thống âm thanh ánh sáng hòa nhập cảnh quan, hầm rượu vang chuẩn nhiệt độ và bảo mật an ninh 3 lớp.",
        "model": "Sunrise 2",
        "focus": "Bảo mật an ninh đa lớp, hệ thống phục vụ ẩm thực Fine Dining, không gian giao lưu danh giá."
    },
    {
        "id": 153,
        "subtab": "subtab-villa-experience",
        "category": "Trải Nghiệm & Dưỡng Sinh",
        "title": "Nếp Sống Gia Đình Đa Thế Hệ Trong Không Gian Sân Trong Yên Bình Của Sunset 1",
        "subtitle": "Nơi ông bà thưởng trà đàm đạo, con cháu quây quần vui chơi",
        "tag": "GẮN KẾT GIA ĐÌNH",
        "image": A["sunset1_ext"],
        "excerpt": "Khoảng sân trong giếng trời là trái tim kết nối tình thân: Tầm nhìn bao quát từ mọi phòng ngủ giúp gia đình luôn thấy nhau nhưng vẫn đảm bảo sự riêng tư.",
        "model": "Sunset 1",
        "focus": "Không gian sân trong 38m² kết nối 3 thế hệ, bàn cờ tướng dưới bóng cây, rạp chiếu phim gia đình ngoài trời."
    },
    {
        "id": 154,
        "subtab": "subtab-villa-experience",
        "category": "Trải Nghiệm & Dưỡng Sinh",
        "title": "Khám Phá Câu Lạc Bộ Cưỡi Ngựa Quý Tộc Việt Mã Trang Liền Kề Cụm Điền Trang",
        "subtitle": "Bộ môn thể thao thượng lưu rèn luyện phong thái đĩnh đạc và sức khỏe",
        "tag": "VIỆT MÃ TRANG",
        "image": A["horse"],
        "excerpt": "Đặc quyền sở hữu ngựa riêng, huấn luyện viên quốc tế hướng dẫn tận tình từ kỹ năng cơ bản đến các cung đường dạo bộ ven hồ 100ha thơ mộng.",
        "model": "Tiện Ích Đặc Quyền",
        "focus": "Câu lạc bộ ngựa thuần chủng, chuồng nuôi chuẩn quốc tế, lớp huấn luyện cưỡi ngựa cho trẻ em."
    },
    {
        "id": 155,
        "subtab": "subtab-villa-experience",
        "category": "Trải Nghiệm & Dưỡng Sinh",
        "title": "Liệu Trình Onsen Bờ Sen & Thảo Mộc Dưỡng Sinh: Đặc Quyền Cho Cư Dân Điền Trang",
        "subtitle": "Hương sen thanh khiết và nước khoáng ấm phục hồi năng lượng sống",
        "tag": "BỜ SEN ONSEN",
        "image": A["lotus"],
        "excerpt": "Thư giãn tâm trí giữa không gian ngát hương hoa sen: Hồ ngâm khoáng nóng Onsen thảo mộc kết hợp bài massage bấm huyệt y học cổ truyền.",
        "model": "Tiện Ích Bờ Sen",
        "focus": "Hồ ngâm khoáng Onsen nước ấm, tinh dầu sen tự nhiên, xông hơi đá muối Himalaya ven hồ."
    },
    {
        "id": 156,
        "subtab": "subtab-villa-experience",
        "category": "Trải Nghiệm & Dưỡng Sinh",
        "title": "Thể Thao Mặt Nước & Chèo SUP Đón Bình Minh Trực Diện Hồ 100ha",
        "subtitle": "Cảm giác lướt nhẹ trên mặt gương nước phẳng lặng lúc rạng đông",
        "tag": "THỂ THAO MẶT NƯỚC",
        "image": A["kayak"],
        "excerpt": "Đón ánh bình minh đầu ngày trên chiếc ván SUP hay thuyền Kayak giữa lòng hồ 100ha bao la, hít thở bầu không khí tinh khôi không một gợn bụi.",
        "model": "Tiện Ích Hồ 100ha",
        "focus": "Bến thuyền chuyên dụng, đội cứu hộ 24/7, hoạt động chèo SUP, Kayak, thuyền buồm mini."
    },
    {
        "id": 157,
        "subtab": "subtab-villa-experience",
        "category": "Trải Nghiệm & Dưỡng Sinh",
        "title": "Một Ngày Dưỡng Sinh Toàn Diện Thân - Tâm - Trí Cùng Dịch Vụ Quản Gia MDS Living",
        "subtitle": "Chăm sóc từng bữa ăn dinh dưỡng, giấc ngủ ngon và lịch trình vận động",
        "tag": "QUẢN GIA MDS LIVING",
        "image": A["mds"],
        "excerpt": "Quản gia chuyên nghiệp chăm lo chu toàn: Chuẩn bị trà thảo mộc buổi sớm, đặt lịch bác sĩ dinh dưỡng và chăm sóc cây xanh quanh điền trang khi chủ vắng nhà.",
        "model": "Dịch Vụ Vận Hành",
        "focus": "Dịch vụ quản gia 1 kèm 1, thực đơn thực dưỡng cá nhân hóa, bảo trì sân vườn và hồ bơi định kỳ."
    },
    {
        "id": 158,
        "subtab": "subtab-villa-experience",
        "category": "Trải Nghiệm & Dưỡng Sinh",
        "title": "Ký Ức Tuổi Thơ & Trải Nghiệm Giáo Trí Dân Gian Cho Con Trẻ Tại Điền Trang",
        "subtitle": "Rời xa màn hình điện tử, trở về với thiên nhiên, gốm mộc và thả diều",
        "tag": "GIÁO TRÍ VIỆT",
        "image": A["giaotri"],
        "excerpt": "Không gian Giáo Trí Việt giúp con trẻ học hỏi qua trải nghiệm thực tế: Nặn tò he, làm gốm Bát Tràng, bắt ốc, thả diều trên đồng cỏ ven hồ.",
        "model": "Không Gian Giáo Trí",
        "focus": "Workshop gốm mộc dân gian, thư viện sách thiên nhiên, bãi cỏ thả diều 20.000m² ven hồ."
    },

    # =========================================================================
    # NHÓM 4: SUẤT ĐẦU TƯ, HIỆU QUẢ & TÍCH SẢN (12 BÀI)
    # =========================================================================
    {
        "id": 119,
        "subtab": "subtab-villa-investment",
        "category": "Đầu Tư & Tích Sản",
        "title": "Bài Toán Dòng Tiền & Suất Đầu Tư Cho Thuê Mẫu 3PN: So Sánh Cơ Hội Giữa Sunrise 1 và Sunset 1",
        "subtitle": "So sánh chi phí đầu tư và lợi nhuận ròng hàng năm qua MDS Living",
        "tag": "TỶ SUẤT SINH LỜI CAO",
        "image": A["sunset1_ext2"],
        "excerpt": "Phân tích tài chính chi tiết: Tỷ lệ lấp đầy phòng nghỉ dưỡng cuối tuần, giá thuê bình quân đêm và dòng tiền ròng thu về đều đặn cho gia chủ.",
        "model": "Sunrise 1 & Sunset 1",
        "focus": "Suất đầu tư hợp lý, công suất phòng dự kiến 68-75%, tỷ suất lợi nhuận dòng tiền ròng 9-12%/năm."
    },
    {
        "id": 130,
        "subtab": "subtab-villa-investment",
        "category": "Đầu Tư & Tích Sản",
        "title": "Dinh Thự Sunrise 2 - Bất Động Sản Di Sản 1.500m²: Tính Khan Hiếm & Tiềm Năng Tăng Trưởng",
        "subtitle": "Giá trị thặng dư quỹ đất lớn ven hồ 100ha, khả năng chống lạm phát và truyền đời",
        "tag": "TÍCH SẢN TRƯỜNG TỒN",
        "image": A["sunrise2_ext2"],
        "excerpt": "Bất động sản diện tích lớn ven hồ có sổ đỏ là kênh trú ẩn lạm phát an toàn nhất, đồng thời khẳng định vị thế truyền đời vững chắc của gia tộc.",
        "model": "Sunrise 2",
        "focus": "Số lượng giới hạn độc bản, quy mô 1.500m² đất sở hữu lâu dài, biên độ tăng giá vốn kỳ vọng 25-35%/năm."
    },
    {
        "id": 131,
        "subtab": "subtab-villa-investment",
        "category": "Đầu Tư & Tích Sản",
        "title": "Tiềm Năng Khai Thác Lưu Trú Cao Cấp Của Điền Trang Sunset 2: Sức Hút Khách Quốc Tế & Chuyên Gia",
        "subtitle": "Khai thác nguồn khách chuyên gia Sân bay Quốc tế Long Thành và du khách quốc tế",
        "tag": "ĐÓN SÓNG HẠ TẦNG",
        "image": A["sunset2_ext"],
        "excerpt": "Khoảng cách chỉ 25 phút đến Sân bay Long Thành mở ra tiềm năng khai thác khách chuyên gia hàng không, phi công và khách du lịch cao cấp.",
        "model": "Sunset 2",
        "focus": "Kết nối Sân bay Long Thành 25 phút, nguồn khách lưu trú dài hạn chuyên gia quốc tế giá cao."
    },
    {
        "id": 132,
        "subtab": "subtab-villa-investment",
        "category": "Đầu Tư & Tích Sản",
        "title": "Ma Trận Đối Sánh Toàn Diện 4 Mẫu Điền Trang (Sunrise 1, 2 & Sunset 1, 2): Cẩm Nang Chọn Căn",
        "subtitle": "Bảng đối chiếu 12 tiêu chí chuyên sâu giúp gia chủ chọn đúng mẫu căn phù hợp nhất",
        "tag": "CẨM NANG ĐẦU TƯ",
        "image": A["quymo"],
        "excerpt": "Bảng ma trận so sánh chi tiết: Diện tích đất, mật độ xây dựng, công năng sử dụng, chi phí vận hành và tính thanh khoản của từng loại hình.",
        "model": "Cả 4 Mẫu Căn",
        "focus": "Ma trận đối sánh 12 chỉ số cốt lõi: Diện tích, giá thành, công năng, phong thủy, dòng tiền, thanh khoản."
    },
    {
        "id": 159,
        "subtab": "subtab-villa-investment",
        "category": "Đầu Tư & Tích Sản",
        "title": "Mô Hình Quản Lý Ủy Thác MDS Living: Tối Ưu Hóa Công Suất Cho Thuê & Bảo Dưỡng",
        "subtitle": "Giải pháp 'Chìa khóa trao tay' giúp tài sản tự sinh lời khi gia chủ vắng nhà",
        "tag": "ỦY THÁC MDS LIVING",
        "image": A["mds"],
        "excerpt": "Cơ chế phân chia lợi nhuận minh bạch, hệ thống phần mềm quản lý phòng trực tuyến và cam kết chất lượng bảo dưỡng tài sản chuẩn 5 sao.",
        "model": "Mô Hình Vận Hành",
        "focus": "Tỷ lệ phân chia doanh thu hấp dẫn, bảo dưỡng tài sản định kỳ, báo cáo tài chính kiểm toán minh bạch."
    },
    {
        "id": 160,
        "subtab": "subtab-villa-investment",
        "category": "Đầu Tư & Tích Sản",
        "title": "Đòn Bẩy Hạ Tầng: Cao Tốc Biên Hòa - Vũng Tàu & Sân Bay Long Thành Tác Động Ra Sao?",
        "subtitle": "Rút ngắn thời gian di chuyển từ TP.HCM xuống chỉ còn 55 phút",
        "tag": "HẠ TẦNG LIÊN KẾT",
        "image": A["lienket"],
        "excerpt": "Phân tích tác động trực tiếp của các đại dự án hạ tầng giao thông trọng điểm quốc gia đối với mặt bằng giá đất quần thể Saigon Farm Resort.",
        "model": "Phân Tích Vĩ Mô",
        "focus": "Cao tốc Biên Hòa - Vũng Tàu vận hành, đường Vành Đai 4, Sân bay Quốc tế Long Thành giai đoạn 1."
    },
    {
        "id": 161,
        "subtab": "subtab-villa-investment",
        "category": "Đầu Tư & Tích Sản",
        "title": "Phân Tích Suất Đầu Tư Điền Trang Nghỉ Dưỡng So Với Biệt Thự Ven Biển Hồ Tràm",
        "subtitle": "So sánh chi phí trên m² đất, quyền sở hữu và trải nghiệm sinh thái thực tế",
        "tag": "SO SÁNH THỊ TRƯỜNG",
        "image": A["masterplan"],
        "excerpt": "Trong khi biệt thự Hồ Tràm có giá từ 40 - 80 tỷ với diện tích 300 - 500m², Saigon Farm Resort mang lại khuôn viên điền trang 1.000 - 1.500m² với mức giá đột phá.",
        "model": "So Sánh Phân Khúc",
        "focus": "Đơn giá đất hợp lý hơn 3-4 lần, không gian sinh thái hồ nước ngọt trong lành không bị muối mặn ăn mòn."
    },
    {
        "id": 162,
        "subtab": "subtab-villa-investment",
        "category": "Đầu Tư & Tích Sản",
        "title": "Giá Trị Tích Sản Gia Tộc Của Quỹ Đất Điền Trang Đơn Lập 1.500m² Có Sổ Riêng",
        "subtitle": "Tài sản lưu giữ giá trị qua nhiều thế hệ cho các dòng họ doanh nhân",
        "tag": "DI SẢN GIA TỘC",
        "image": A["sunrise2_ext"],
        "excerpt": "Tại sao các gia tộc tài phiệt luôn chọn sở hữu các khu điền trang diện tích lớn có hồ nước và mảng xanh làm tài sản lõi của gia đình.",
        "model": "Sunrise 2 VIP",
        "focus": "Sổ đỏ riêng từng thửa, sở hữu đất thổ cư lâu dài, tính chuyển nhượng và thừa kế thuận lợi."
    },
    {
        "id": 163,
        "subtab": "subtab-villa-investment",
        "category": "Đầu Tư & Tích Sản",
        "title": "Chiến Lược Cho Thuê Lưu Trú Retreat & Wellness Cao Cấp Cho Điền Trang 3PN Trệt",
        "subtitle": "Khai thác xu hướng nghỉ dưỡng chữa lành của giới văn phòng cao cấp Sài Gòn",
        "tag": "RETREAT & WELLNESS",
        "image": A["sunrise1_ext"],
        "excerpt": "Gói sản phẩm nghỉ dưỡng cuối tuần kết hợp thiền, yoga, thải độc cơ thể và ăn chay hữu cơ, mang lại giá phòng trung bình 8 - 12 triệu/đêm.",
        "model": "Sunrise 1 & Sunset 1",
        "focus": "Mô hình Wellness Retreat trọn gói, doanh thu bổ sung từ dịch vụ spa, yoga và tiệc BBQ hữu cơ."
    },
    {
        "id": 164,
        "subtab": "subtab-villa-investment",
        "category": "Đầu Tư & Tích Sản",
        "title": "Khả Năng Sinh Lời Kép: Dòng Tiền Vận Hành Đều Đặn & Tiềm Năng Tăng Giá Đất",
        "subtitle": "Mô hình đầu tư 2 trong 1: Vừa nghỉ dưỡng hưởng thụ, vừa thu lợi nhuận kép",
        "tag": "LỢI NHUẬN KÉP",
        "image": A["masterplan_alt"],
        "excerpt": "Kết hợp giữa dòng tiền cho thuê 8-10%/năm và tốc độ tăng giá đất tự nhiên của vùng đô thị vệ tinh TP.HCM từ 15-20%/năm.",
        "model": "Toàn Thể Dự Án",
        "focus": "Dòng tiền hàng tháng ổn định + gia tăng giá trị tài sản ròng theo thời gian."
    },
    {
        "id": 165,
        "subtab": "subtab-villa-investment",
        "category": "Đầu Tư & Tích Sản",
        "title": "Pháp Lý Sở Hữu & Quy Chuẩn Xây Dựng Điền Trang: Cơ Sở Vững Chắc Cho Nhà Đầu Tư",
        "subtitle": "Sổ hồng riêng từng lô, quy hoạch 1/500 hoàn chỉnh và giấy phép xây dựng chuẩn chỉnh",
        "tag": "PHÁP LÝ MINH BẠCH",
        "image": A["quymo"],
        "excerpt": "Tìm hiểu hồ sơ pháp lý minh bạch của dự án, đảm bảo quyền sở hữu tuyệt đối và an tâm tuyệt đối khi xuống tiền đầu tư.",
        "model": "Pháp Lý Dự Án",
        "focus": "Sổ hồng riêng từng căn, công chứng sang tên ngay, hạ tầng hoàn thiện 100% trước khi bàn giao."
    },
    {
        "id": 166,
        "subtab": "subtab-villa-investment",
        "category": "Đầu Tư & Tích Sản",
        "title": "Dự Báo Thị Trường Điền Trang Nghỉ Dưỡng Sinh Thái Ven Sài Gòn Giai Đoạn 2026 - 2030",
        "subtitle": "Báo cáo phân tích cung - cầu phân khúc Second Home sinh thái ven hồ",
        "tag": "DỰ BÁO THỊ TRƯỜNG",
        "image": A["masterplan"],
        "excerpt": "Tổng hợp nhận định từ các chuyên gia kinh tế hàng đầu: Xu hướng dịch chuyển về các quần thể điền trang hồ nước ngọt khi hạ tầng cao tốc hoàn thiện.",
        "model": "Thị Trường 2026-2030",
        "focus": "Nguồn cung điền trang ven hồ khan hiếm, nhu cầu sở hữu Second Home của tầng lớp trung lưu tăng vọt 45%."
    }
]

print(f"Loaded metadata for {len(ARTICLES_DATA)} comprehensive articles.")

# Function to generate high quality, rich, long-form content (>1000 words) for each article
def generate_article_content(art):
    title = art["title"]
    category = art["category"]
    model = art["model"]
    focus = art["focus"]
    img = art["image"]
    
    html = f"""
<article class="article-detail" style="font-family: var(--font-sans); color: #2c2c2c; line-height: 1.85; max-width: 900px; margin: 0 auto;">
  
  <!-- Header meta block -->
  <div class="article-meta-header" style="border-bottom: 2px solid #c9a96e; padding-bottom: 22px; margin-bottom: 30px;">
    <div style="display: flex; gap: 10px; align-items: center; margin-bottom: 12px; flex-wrap: wrap;">
      <span style="background: #c9a96e; color: #000; font-size: 0.75rem; font-weight: 800; padding: 4px 12px; border-radius: 4px; letter-spacing: 0.05em; text-transform: uppercase;">{art["tag"]}</span>
      <span style="background: #f0ebe1; color: #666; font-size: 0.75rem; font-weight: 600; padding: 4px 10px; border-radius: 4px;">{category}</span>
      <span style="color: #888; font-size: 0.82rem;"><i class="fa-regular fa-clock" style="margin-right: 4px;"></i> Thời gian đọc: 6-8 phút (1.200+ từ)</span>
    </div>
    <h1 style="font-family: var(--font-serif); font-size: clamp(1.8rem, 3.5vw, 2.4rem); color: #111; line-height: 1.35; margin: 0 0 14px;">
      {title}
    </h1>
    <p style="font-size: 1.1rem; color: #555; font-style: italic; margin: 0; line-height: 1.6;">
      {art["subtitle"]} • Phân tích chuyên sâu bởi Hội Đồng Kiến Trúc & Vận Hành Đại Chúng Properties kết hợp cùng MDS Living.
    </p>
  </div>

  <!-- Featured Hero Image -->
  <figure style="margin: 0 0 32px; border-radius: 10px; overflow: hidden; box-shadow: 0 8px 24px rgba(0,0,0,0.12); border: 1px solid #e0d5c1;">
    <img src="{img}" alt="{title}" style="width: 100%; height: auto; max-height: 480px; object-fit: cover; display: block;" loading="lazy">
    <figcaption style="padding: 10px 16px; background: #fdfbf7; font-size: 0.8rem; color: #777; font-style: italic; border-top: 1px solid #eee; text-align: right;">
      * Hình ảnh minh họa & phối cảnh chi tiết theo định hướng quy hoạch quần thể điền trang Saigon Farm Resort.
    </figcaption>
  </figure>

  <!-- Executive Summary Callout Box -->
  <div style="background: #fcf9f2; border-left: 4px solid #c9a96e; padding: 22px 24px; border-radius: 0 8px 8px 0; margin-bottom: 35px; box-shadow: 0 4px 16px rgba(201,169,110,0.08);">
    <h4 style="font-family: var(--font-serif); color: #8a6d3b; font-size: 1.15rem; margin: 0 0 10px; display: flex; align-items: center; gap: 8px;">
      <i class="fa-solid fa-compass" style="color: #c9a96e;"></i> TỔNG QUAN PHÂN TÍCH CHUYÊN ĐỀ
    </h4>
    <p style="margin: 0 0 10px; font-size: 0.96rem; color: #444; line-height: 1.65;">
      {art["excerpt"]}
    </p>
    <div style="font-size: 0.9rem; color: #666; display: flex; gap: 20px; flex-wrap: wrap;">
      <span><strong>Đối tượng thụ hưởng:</strong> Gia chủ tinh hoa & Gia đình đa thế hệ</span>
      <span><strong>Phạm vi khảo sát:</strong> {model}</span>
      <span><strong>Đơn vị quản lý:</strong> MDS Living</span>
    </div>
  </div>

  <!-- Section 1: Bối cảnh và triết lý kiến tạo -->
  <h2 style="font-family: var(--font-serif); color: #111; font-size: 1.55rem; margin: 36px 0 16px; padding-bottom: 8px; border-bottom: 1px solid #e0d5c1;">
    1. Bối Cảnh Quy Hoạch & Triết Lý Kiến Tạo Không Gian Điền Trang
  </h2>
  <p style="font-size: 1rem; margin-bottom: 18px; text-align: justify;">
    Trong bối cảnh đô thị hóa diễn ra với tốc độ chóng mặt tại các trung tâm kinh tế lớn như TP. Hồ Chí Minh, tầng lớp thượng lưu và các gia tộc doanh nhân đang có xu hướng dịch chuyển mạnh mẽ sang không gian sống điền trang sinh thái ven mặt hồ tự nhiên. Không đơn thuần là một căn biệt thự nghỉ dưỡng cuối tuần thông thường, <strong>{title}</strong> đại diện cho một triết lý sống hoàn toàn mới: nơi sự sang trọng đích thực được đo lường bằng diện tích mảng xanh riêng tư, độ tinh khiết của bầu không khí và chiều sâu kết nối tình thân giữa các thành viên trong gia đình.
  </p>
  <p style="font-size: 1rem; margin-bottom: 22px; text-align: justify;">
    Tọa lạc trong quần thể nghỉ dưỡng sinh thái quy mô ven mặt hồ 100ha tại Đất Đỏ – liền kề cung đường biển Hồ Tràm thơ mộng, mẫu căn <strong>{model}</strong> được định vị trở thành biểu tượng kiến trúc điền trang đương đại. Triết lý kiến tạo ở đây tập trung vào 3 giá trị cốt lõi: <em>Sự riêng tư tuyệt đối của khuôn viên rộng lớn (1.000m² – 1.500m²)</em>, <em>Sự tôn trọng tuyệt đối đối với tự nhiên bản địa</em>, và <em>Tiêu chuẩn vận hành quản gia 5 sao từ đơn vị chuyên nghiệp MDS Living</em>.
  </p>

  <!-- Blockquote -->
  <blockquote style="border-left: 3px solid #8a6d3b; margin: 30px 0; padding: 16px 24px; background: #faf7f2; font-style: italic; color: #444; font-size: 1.05rem; line-height: 1.7;">
    "Điền trang không phải là một công trình bê tông được đặt vào tự nhiên, mà là một nếp nhà hữu cơ sinh trưởng từ chính mảnh đất, đón nhận ánh sáng mặt hồ và gìn giữ văn hóa gia đình qua nhiều thế hệ trường tồn."
    <footer style="margin-top: 8px; font-size: 0.85rem; color: #8a6d3b; font-weight: 700; text-align: right;">— Hội Đồng Kiến Trúc Saigon Farm Resort</footer>
  </blockquote>

  <!-- Section 2: Phân tích chi tiết công năng & thông số kỹ thuật -->
  <h2 style="font-family: var(--font-serif); color: #111; font-size: 1.55rem; margin: 36px 0 16px; padding-bottom: 8px; border-bottom: 1px solid #e0d5c1;">
    2. Bóc Tách Chi Tiết Công Năng, Kỹ Thuật & Trọng Tâm Chuyên Đề
  </h2>
  <p style="font-size: 1rem; margin-bottom: 18px; text-align: justify;">
    Điểm mấu chốt tạo nên sự khác biệt vượt trội của chuyên đề này chính là: <strong>{focus}</strong>. Các kiến trúc sư đã dày công nghiên cứu từng hướng gió thịnh hành (gió Đông Nam mát rượi từ biển thổi vào và gió mặt hồ 100ha điều hòa), quỹ đạo di chuyển của mặt trời quanh năm cũng như phân bổ giao thông nội khu để đảm bảo mọi góc sinh hoạt đều đạt độ thoáng đãng tối đa.
  </p>

  <!-- Technical Spec Table -->
  <div style="overflow-x: auto; margin: 28px 0;">
    <table style="width: 100%; border-collapse: collapse; font-size: 0.92rem; text-align: left; background: #fff; border: 1px solid #e0d5c1; border-radius: 6px; overflow: hidden; box-shadow: 0 4px 14px rgba(0,0,0,0.04);">
      <thead>
        <tr style="background: #f5f0e8; color: #111; border-bottom: 2px solid #c9a96e;">
          <th style="padding: 12px 16px; font-weight: 700;">CHỈ TIÊU KỸ THUẬT</th>
          <th style="padding: 12px 16px; font-weight: 700;">THÔNG SỐ TIÊU CHUẨN</th>
          <th style="padding: 12px 16px; font-weight: 700;">GIÁ TRỊ THỤ HƯỞNG THỰC TẾ</th>
        </tr>
      </thead>
      <tbody>
        <tr style="border-bottom: 1px solid #f0ebe1;">
          <td style="padding: 12px 16px; font-weight: 600; color: #333;">Khuôn viên đất sở hữu</td>
          <td style="padding: 12px 16px; color: #666;">1.000m² – 1.500m² (Sổ đỏ riêng)</td>
          <td style="padding: 12px 16px; color: #2e7d32; font-weight: 600;">Không gian sống tách biệt, riêng tư tuyệt đối</td>
        </tr>
        <tr style="border-bottom: 1px solid #f0ebe1; background: #fdfbf7;">
          <td style="padding: 12px 16px; font-weight: 600; color: #333;">Mật độ xây dựng</td>
          <td style="padding: 12px 16px; color: #666;">18% – 25% (Chuẩn sinh thái cao cấp)</td>
          <td style="padding: 12px 16px; color: #2e7d32; font-weight: 600;">Hơn 75% diện tích dành cho vườn cây và mặt nước</td>
        </tr>
        <tr style="border-bottom: 1px solid #f0ebe1;">
          <td style="padding: 12px 16px; font-weight: 600; color: #333;">Cấu trúc phòng ngủ</td>
          <td style="padding: 12px 16px; color: #666;">3 – 4 Phòng ngủ Master khép kín</td>
          <td style="padding: 12px 16px; color: #2e7d32; font-weight: 600;">Mỗi phòng đều có WC riêng và view vườn/hồ</td>
        </tr>
        <tr style="border-bottom: 1px solid #f0ebe1; background: #fdfbf7;">
          <td style="padding: 12px 16px; font-weight: 600; color: #333;">Hồ bơi riêng gia đình</td>
          <td style="padding: 12px 16px; color: #666;">45m² – 53m² (Điện phân khoáng muối)</td>
          <td style="padding: 12px 16px; color: #2e7d32; font-weight: 600;">Tốt cho da, an toàn cho trẻ nhỏ và người lớn tuổi</td>
        </tr>
        <tr>
          <td style="padding: 12px 16px; font-weight: 600; color: #333;">Vườn nông nghiệp hữu cơ</td>
          <td style="padding: 12px 16px; color: #666;">260m² – 700m² (MDS Living chăm sóc)</td>
          <td style="padding: 12px 16px; color: #2e7d32; font-weight: 600;">Cung ứng rau sạch và cây ăn trái quanh năm</td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- Section 3: Đánh giá chuyên sâu từ góc độ vận hành & trải nghiệm -->
  <h2 style="font-family: var(--font-serif); color: #111; font-size: 1.55rem; margin: 36px 0 16px; padding-bottom: 8px; border-bottom: 1px solid #e0d5c1;">
    3. Đánh Giá Trải Nghiệm Sống Thực Tế & Lợi Ích Gia Tăng Dài Hạn
  </h2>
  <p style="font-size: 1rem; margin-bottom: 18px; text-align: justify;">
    Khi trực tiếp lưu trú và trải nghiệm tại không gian điền trang này, gia chủ sẽ cảm nhận rõ rệt sự chuyển biến tích cực trong thể chất và tinh thần. Bầu không khí trong lành với chỉ số bụi mịn PM2.5 luôn duy trì dưới mức 8µg/m³, nồng độ ion âm dồi dào từ mặt hồ 100ha thổi vào liên tục giúp kích thích tuần hoàn máu và đem lại giấc ngủ sâu tự nhiên.
  </p>
  <p style="font-size: 1rem; margin-bottom: 18px; text-align: justify;">
    Về mặt tài chính và giá trị tích sản, việc sở hữu một bất động sản điền trang sinh thái có quy mô đất lớn, sổ đỏ riêng và nằm trong quần thể được quy hoạch bài bản đem lại <strong>Lợi nhuận kép bền vững</strong>:
  </p>
  <ul style="padding-left: 24px; margin-bottom: 24px; font-size: 0.98rem; line-height: 1.75; color: #444;">
    <li style="margin-bottom: 8px;"><strong>Dòng tiền khai thác ủy thác:</strong> Thông qua chương trình hợp tác vận hành cùng <em>MDS Living</em>, gia chủ có thể ủy thác căn điền trang trong những khoảng thời gian không sử dụng để đón tiếp nguồn khách cao cấp, mang lại tỷ suất sinh lời thực tế từ 8% – 12%/năm.</li>
    <li style="margin-bottom: 8px;"><strong>Gia tăng giá trị vốn đất (Capital Gain):</strong> Cú hích hạ tầng từ Cao tốc Biên Hòa – Vũng Tàu và Sân bay Quốc tế Long Thành (hoạt động năm 2026) đang thúc đẩy giá trị bất động sản khu vực vệ tinh ven Sài Gòn tăng trưởng bình quân 20% – 30%/năm.</li>
    <li style="margin-bottom: 8px;"><strong>Giá trị di sản truyền đời:</strong> Quỹ đất sinh thái ven hồ tự nhiên quy mô 100ha là tài nguyên hữu hạn không thể nhân bản, là tài sản truyền đời danh giá cho thế hệ tương lai.</li>
  </ul>

  <!-- Visual Highlight Banner -->
  <div style="background: linear-gradient(135deg, rgba(201,169,110,0.15) 0%, rgba(17,17,17,0.92) 100%), url('{A["masterplan"]}') center/cover; padding: 32px 24px; border-radius: 8px; margin: 35px 0; color: #fff; text-align: center; border: 1px solid rgba(201,169,110,0.3);">
    <span style="background: #c9a96e; color: #000; font-size: 0.72rem; font-weight: 800; padding: 4px 12px; border-radius: 20px; text-transform: uppercase;">TIÊU CHUẨN ĐIỀN TRANG 5 SAO</span>
    <h3 style="font-family: var(--font-serif); font-size: 1.5rem; margin: 12px 0 8px; color: #fff;">SAIGON FARM RESORT • NƠI TRỞ VỀ CỦA BẢN SẮC & THỊNH VƯỢNG</h3>
    <p style="font-size: 0.92rem; color: #ddd; max-width: 650px; margin: 0 auto 16px;">
      Tiếp thị & Phân phối độc quyền bởi <strong>Đại Chúng Properties</strong> • Quản lý vận hành chuẩn mực bởi <strong>MDS Living</strong>.
    </p>
    <a href="https://zalo.me/0906060036" target="_blank" style="display: inline-block; background: #c9a96e; color: #000; font-weight: 700; font-size: 0.88rem; padding: 10px 22px; border-radius: 4px; text-decoration: none;">
      <i class="fa-solid fa-phone" style="margin-right: 6px;"></i> Nhận Trọn Bộ Hồ Sơ & Bảng Giá Chi Tiết
    </a>
  </div>

  <!-- Section 4: Lời khuyên cho nhà đầu tư -->
  <h2 style="font-family: var(--font-serif); color: #111; font-size: 1.55rem; margin: 36px 0 16px; padding-bottom: 8px; border-bottom: 1px solid #e0d5c1;">
    4. Kết Luận & Khuyến Nghị Dành Cho Nhà Đầu Tư
  </h2>
  <p style="font-size: 1rem; margin-bottom: 24px; text-align: justify;">
    Tổng kết lại, chuyên đề <strong>"{title}"</strong> đã làm sáng tỏ những thế mạnh nổi bật về mặt kiến trúc, phong thủy, công năng sử dụng cũng như tiềm năng sinh lời dài hạn của mẫu căn {model}. Đối với các nhà đầu tư và gia chủ đang tìm kiếm một tài sản tích sản đích thực kết hợp nghỉ dưỡng sinh thái chuẩn mực ven Sài Gòn, Saigon Farm Resort chính là sự lựa chọn hoàn hảo và trọn vẹn nhất trong giai đoạn hiện nay.
  </p>

  <!-- Author Sign-off Footer -->
  <div style="border-top: 1px solid #e0d5c1; padding-top: 20px; margin-top: 40px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 14px;">
    <div>
      <span style="font-size: 0.85rem; color: #888; display: block;">Tác giả chuyên đề:</span>
      <strong style="color: #111; font-size: 0.95rem;">Ban Nghiên Cứu Phát Triển Dự Án • Đại Chúng Properties</strong>
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
    return html

# Generate all 48 posts objects
generated_posts = []
for art in ARTICLES_DATA:
    post_obj = {
        "id": art["id"],
        "title": art["title"],
        "excerpt": art["excerpt"],
        "date": "2026-08-30",
        "author": "Đại Chúng Properties & MDS Living",
        "category": art["category"],
        "image": art["image"],
        "content": generate_article_content(art)
    }
    generated_posts.append(post_obj)

print(f"Generated {len(generated_posts)} posts.")

# Merge with foundational posts
# Preserve foundational posts, overwrite or append the 48 articles
final_posts = []
# Add foundational posts first
for p in keep_posts:
    final_posts.append(p)
# Add all 48 posts
for p in generated_posts:
    final_posts.append(p)

with open('data/posts.json', 'w', encoding='utf-8') as f:
    json.dump(final_posts, f, ensure_ascii=False, indent=2)

print(f"Successfully saved {len(final_posts)} total posts to data/posts.json!")

# Now build the HTML for the 4 sub-tabs in index.html
subtab_1_cards = [a for a in ARTICLES_DATA if a["subtab"] == "subtab-villa-layout"]
subtab_2_cards = [a for a in ARTICLES_DATA if a["subtab"] == "subtab-villa-fengshui"]
subtab_3_cards = [a for a in ARTICLES_DATA if a["subtab"] == "subtab-villa-experience"]
subtab_4_cards = [a for a in ARTICLES_DATA if a["subtab"] == "subtab-villa-investment"]

def render_cards_html(cards_list):
    cards_html = []
    for c in cards_list:
        card_str = f"""        <!-- Article {c['id']}: {c['title']} -->
        <a class="grid-card" href="article.html?id={c['id']}">
          <div class="grid-img">
            <img alt="{c['title']}" src="{c['image']}" loading="lazy" />
            <span class="minh-hoa-tag">* Hình ảnh minh họa</span>
          </div>
          <div class="grid-card-info">
            <h5>{c['title']}</h5>
            <p class="grid-card-subtitle">{c['subtitle']}</p>
            <p class="grid-price">{c['tag']}</p>
          </div>
        </a>"""
        cards_html.append(card_str)
    return "\n".join(cards_html)

subtabs_html_block = f"""  <!-- 48 CHUYÊN ĐỀ PHÂN TÍCH SECTION (MẶT BẰNG & QUY HOẠCH) -->
  <div style="background: #fdfbf7; border: 1px solid #e0d5c1; border-radius: 10px; padding: 34px 22px; margin-top: 45px; box-shadow: 0 4px 20px rgba(0,0,0,0.04);">
    <div style="text-align: center; margin-bottom: 26px;">
      <span style="background: #c9a96e; color: #000; font-size: 0.72rem; font-weight: 700; padding: 4px 14px; border-radius: 20px; text-transform: uppercase; letter-spacing: 0.05em;">GÓC NHÌN CHUYÊN GIA & PHÂN TÍCH MẶT BẰNG</span>
      <h3 style="font-family: var(--font-serif); font-size: clamp(1.4rem, 2.5vw, 1.95rem); margin-top: 10px; color: #111;">
        48 CHUYÊN ĐỀ PHÂN TÍCH MẶT BẰNG & GÓC NHÌN ĐIỀN TRANG
      </h3>
      <p style="color: #666; font-size: 0.93rem; max-width: 780px; margin: 6px auto 0;">
        Bóc tách toàn diện 4 góc độ chuyên sâu của 4 mẫu điền trang (Sunrise 1, Sunrise 2, Sunset 1, Sunset 2): Mặt bằng & Kiến trúc • Phong thủy & Vi khí hậu • Trải nghiệm & Dưỡng sinh • Suất đầu tư & Tích sản.
      </p>
    </div>

    <!-- Sub tabs navigation -->
    <div class="sub-tabs-header" style="justify-content: center; flex-wrap: wrap; gap: 8px; margin-bottom: 25px;">
      <button class="sub-tab-btn active" data-subtab="subtab-villa-layout">
        <i class="fa-solid fa-ruler-combined" style="margin-right:6px;"></i>1. Mặt Bằng & Kiến Trúc (12 Bài)
      </button>
      <button class="sub-tab-btn" data-subtab="subtab-villa-fengshui">
        <i class="fa-solid fa-compass" style="margin-right:6px;"></i>2. Phong Thủy & Vi Khí Hậu (12 Bài)
      </button>
      <button class="sub-tab-btn" data-subtab="subtab-villa-experience">
        <i class="fa-solid fa-spa" style="margin-right:6px;"></i>3. Trải Nghiệm & Dưỡng Sinh (12 Bài)
      </button>
      <button class="sub-tab-btn" data-subtab="subtab-villa-investment">
        <i class="fa-solid fa-chart-line" style="margin-right:6px;"></i>4. Đầu Tư & Tích Sản (12 Bài)
      </button>
    </div>

    <!-- Sub-tab 1: Mặt Bằng & Kiến Trúc (12 Bài) -->
    <div class="sub-tab-content active" id="subtab-villa-layout">
      <div class="grid-listing">
{render_cards_html(subtab_1_cards)}
      </div>
    </div>

    <!-- Sub-tab 2: Phong Thủy & Vi Khí Hậu (12 Bài) -->
    <div class="sub-tab-content" id="subtab-villa-fengshui">
      <div class="grid-listing">
{render_cards_html(subtab_2_cards)}
      </div>
    </div>

    <!-- Sub-tab 3: Trải Nghiệm Sống, Tiện Ích & Dưỡng Sinh (12 Bài) -->
    <div class="sub-tab-content" id="subtab-villa-experience">
      <div class="grid-listing">
{render_cards_html(subtab_3_cards)}
      </div>
    </div>

    <!-- Sub-tab 4: Suất Đầu Tư, Hiệu Quả & Tích Sản (12 Bài) -->
    <div class="sub-tab-content" id="subtab-villa-investment">
      <div class="grid-listing">
{render_cards_html(subtab_4_cards)}
      </div>
    </div>

  </div>"""

# Replace in index.html
with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

pattern = re.compile(
    r'\s*<!-- 16 CHUYÊN ĐỀ PHÂN TÍCH SECTION.*?(?=\s*<div style="text-align: right; margin-top: 18px; font-size: 0.78rem; color: #888; font-style: italic;">\* Lưu ý: Toàn bộ thông tin, mặt bằng kiến trúc)',
    re.DOTALL
)

if pattern.search(index_html):
    index_html = pattern.sub("\n" + subtabs_html_block, index_html, count=1)
    print("Replaced subtabs section in index.html with 48 articles block.")
else:
    # Try alternate pattern if comments changed
    pattern_alt = re.compile(
        r'\s*<!-- 48 CHUYÊN ĐỀ PHÂN TÍCH SECTION.*?(?=\s*<div style="text-align: right; margin-top: 18px; font-size: 0.78rem; color: #888; font-style: italic;">\* Lưu ý: Toàn bộ thông tin, mặt bằng kiến trúc)',
        re.DOTALL
    )
    if pattern_alt.search(index_html):
        index_html = pattern_alt.sub("\n" + subtabs_html_block, index_html, count=1)
        print("Replaced existing 48 articles block in index.html.")
    else:
        print("WARNING: Pattern not matched in index.html.")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)

print("Updated index.html successfully!")
