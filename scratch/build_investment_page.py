import os
import re

def build_investment_page():
    with open("gioithieu.html", "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Update Title and Meta Tags
    html = re.sub(
        r'<title>.*?</title>',
        '<title>Cơ Hội Đầu Tư Điền Trang Nghỉ Dưỡng Saigon Farm Resort | Đất Đỏ — Hồ Tràm</title>',
        html,
        flags=re.DOTALL
    )

    html = re.sub(
        r'<meta name="description" content=".*?">',
        '<meta name="description" content="Khám phá cơ hội đầu tư điền trang nghỉ dưỡng sinh thái ven hồ 100ha Saigon Farm Resort: 100% thổ cư sổ đỏ riêng, hệ tiện ích 30.000 m², dòng tiền khai thác 120 tr/tháng từ MDS Living. Đăng ký Site Tour VIP Hotline/Zalo 0909000712.">',
        html,
        flags=re.DOTALL,
        count=1
    )

    html = re.sub(
        r'<link rel="canonical" href=".*?">',
        '<link rel="canonical" href="https://saigonfarmresort.com/investment">',
        html
    )

    html = re.sub(
        r'<meta property="og:title" content=".*?">',
        '<meta property="og:title" content="Cơ Hội Đầu Tư Điền Trang Nghỉ Dưỡng Saigon Farm Resort | Đất Đỏ — Hồ Tràm">',
        html
    )

    html = re.sub(
        r'<meta property="og:description" content=".*?">',
        '<meta property="og:description" content="Khám phá cơ hội đầu tư điền trang nghỉ dưỡng sinh thái ven hồ 100ha Saigon Farm Resort: 100% thổ cư sổ đỏ riêng, hệ tiện ích 30.000 m², dòng tiền khai thác 120 tr/tháng từ MDS Living. Đăng ký Site Tour VIP Hotline/Zalo 0909000712.">',
        html
    )

    html = re.sub(
        r'<meta property="og:url" content=".*?">',
        '<meta property="og:url" content="https://saigonfarmresort.com/investment">',
        html
    )

    # 2. Add custom CSS styles for the Landing Page
    custom_css = """
    /* ================================================================
       INVESTMENT LANDING PAGE SPECIFIC ENHANCEMENTS
       ================================================================ */
    .btn-hotline-nav {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 6px 14px;
      border-radius: 20px;
      background: #b22222;
      color: #fff !important;
      font-weight: 700;
      font-size: 0.82rem;
      text-decoration: none;
      transition: all 0.25s ease;
      box-shadow: 0 2px 8px rgba(178,34,34,0.35);
    }
    .btn-hotline-nav:hover {
      background: #8b0000;
      transform: translateY(-1px);
      box-shadow: 0 4px 12px rgba(178,34,34,0.5);
    }
    .btn-zalo-nav {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 6px 14px;
      border-radius: 20px;
      background: #0068ff;
      color: #fff !important;
      font-weight: 700;
      font-size: 0.82rem;
      text-decoration: none;
      transition: all 0.25s ease;
      box-shadow: 0 2px 8px rgba(0,104,255,0.35);
    }
    .btn-zalo-nav:hover {
      background: #0052cc;
      transform: translateY(-1px);
      box-shadow: 0 4px 12px rgba(0,104,255,0.5);
    }

    /* 4 Trụ Cột Tăng Giá Trị */
    .investment-growth-pillars-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 20px;
      margin: 28px 0;
    }
    @media (max-width: 768px) {
      .investment-growth-pillars-grid {
        grid-template-columns: 1fr;
        gap: 16px;
      }
    }
    .growth-pillar-card {
      background: #ffffff;
      border: 1px solid rgba(201,169,110,0.35);
      border-radius: 12px;
      padding: 22px 20px;
      box-shadow: 0 4px 16px rgba(0,0,0,0.04);
      display: flex;
      gap: 16px;
      align-items: flex-start;
      transition: transform 0.25s ease, box-shadow 0.25s ease;
    }
    .growth-pillar-card:hover {
      transform: translateY(-3px);
      box-shadow: 0 8px 24px rgba(24,48,36,0.08);
      border-color: var(--color-gold);
    }
    .growth-pillar-icon {
      width: 48px;
      height: 48px;
      border-radius: 12px;
      background: linear-gradient(135deg, #183024 0%, #2a523e 100%);
      color: #ffd166;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.35rem;
      flex-shrink: 0;
      box-shadow: 0 4px 12px rgba(24,48,36,0.18);
    }
    .growth-pillar-content h4 {
      font-family: var(--font-serif);
      font-size: 1.12rem;
      color: #183024;
      margin: 0 0 8px;
      font-weight: 700;
      line-height: 1.35;
    }
    .growth-pillar-content p {
      font-size: 0.9rem;
      color: #4a5568;
      line-height: 1.6;
      margin: 0;
    }

    /* VIP Site Tour Box */
    .sitetour-exclusive-box {
      background: linear-gradient(135deg, #183024 0%, #112219 100%);
      border: 2px solid rgba(201,169,110,0.5);
      border-radius: 16px;
      padding: 32px 28px;
      color: #ffffff;
      margin: 32px 0 20px;
      box-shadow: 0 12px 32px rgba(18,34,25,0.25);
      position: relative;
      overflow: hidden;
    }
    .sitetour-exclusive-box::before {
      content: '';
      position: absolute;
      top: -50%;
      right: -20%;
      width: 320px;
      height: 320px;
      background: radial-gradient(circle, rgba(201,169,110,0.15) 0%, transparent 70%);
      border-radius: 50%;
      pointer-events: none;
    }
    .sitetour-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: rgba(201,169,110,0.25);
      border: 1px solid rgba(201,169,110,0.6);
      color: #ffd166;
      font-size: 0.76rem;
      font-weight: 800;
      padding: 5px 14px;
      border-radius: 20px;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      margin-bottom: 14px;
    }
    .sitetour-title {
      font-family: var(--font-brand);
      font-size: 1.55rem;
      color: #ffffff;
      margin: 0 0 12px;
      line-height: 1.35;
    }
    .sitetour-desc {
      font-size: 0.95rem;
      color: #d1e2d8;
      line-height: 1.65;
      margin-bottom: 22px;
      max-width: 820px;
    }
    .sitetour-perks-list {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 12px 18px;
      margin-bottom: 24px;
      padding-bottom: 20px;
      border-bottom: 1px solid rgba(255,255,255,0.12);
    }
    @media (max-width: 680px) {
      .sitetour-perks-list {
        grid-template-columns: 1fr;
      }
    }
    .sitetour-perk-item {
      display: flex;
      align-items: flex-start;
      gap: 10px;
      font-size: 0.88rem;
      color: #e2ede7;
      line-height: 1.5;
    }
    .sitetour-perk-item i {
      color: #ffd166;
      margin-top: 3px;
      font-size: 0.95rem;
      flex-shrink: 0;
    }

    /* Inline Lead Capture Form in Site Tour Box */
    .sitetour-inline-form-card {
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(201, 169, 110, 0.45);
      border-radius: 12px;
      padding: 20px;
      margin: 24px 0 20px;
      backdrop-filter: blur(8px);
      -webkit-backdrop-filter: blur(8px);
    }
    .inline-form-header {
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 0.82rem;
      font-weight: 800;
      color: #ffd166;
      letter-spacing: 0.05em;
      text-transform: uppercase;
      margin-bottom: 14px;
    }
    .inline-form-inputs {
      display: grid;
      grid-template-columns: 1fr 1fr 1fr;
      gap: 12px;
      margin-bottom: 12px;
    }
    @media (max-width: 850px) {
      .inline-form-inputs {
        grid-template-columns: 1fr;
      }
    }
    .inline-input-group {
      position: relative;
    }
    .inline-input-group .input-icon {
      position: absolute;
      left: 12px;
      top: 50%;
      transform: translateY(-50%);
      color: #8c6b32;
      font-size: 0.88rem;
    }
    .inline-form-input {
      width: 100%;
      padding: 11px 12px 11px 36px;
      border: 1px solid rgba(201, 169, 110, 0.4);
      border-radius: 8px;
      font-family: inherit;
      font-size: 0.88rem;
      background: #fffdfa;
      color: #111;
      box-sizing: border-box;
      transition: all 0.2s ease;
    }
    .inline-form-input:focus {
      outline: none;
      border-color: #ffd166;
      background: #ffffff;
      box-shadow: 0 0 0 3px rgba(201,169,110,0.25);
    }
    .btn-inline-submit {
      width: 100%;
      padding: 13px;
      border-radius: 8px;
      background: linear-gradient(135deg, #c9a96e 0%, #b38b4d 100%);
      color: #183024 !important;
      font-weight: 800;
      font-size: 0.95rem;
      border: none;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      box-shadow: 0 4px 14px rgba(201, 169, 110, 0.35);
      transition: all 0.2s ease;
    }
    .btn-inline-submit:hover {
      background: linear-gradient(135deg, #d4b57a 0%, #c9a96e 100%);
      transform: translateY(-1px);
      box-shadow: 0 6px 18px rgba(201, 169, 110, 0.55);
    }
    .inline-success-banner {
      margin-top: 12px;
      padding: 12px 16px;
      background: rgba(46, 125, 50, 0.25);
      border: 1px solid #81c784;
      border-radius: 8px;
      color: #c8e6c9;
      font-size: 0.88rem;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .sitetour-cta-actions {
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      align-items: center;
    }
    .btn-sitetour-hotline {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: linear-gradient(135deg, #d32f2f 0%, #b71c1c 100%);
      color: #ffffff !important;
      padding: 12px 22px;
      border-radius: 30px;
      font-weight: 700;
      font-size: 0.92rem;
      text-decoration: none;
      box-shadow: 0 4px 16px rgba(211,47,47,0.4);
      transition: all 0.25s ease;
    }
    .btn-sitetour-hotline:hover {
      background: linear-gradient(135deg, #b71c1c 0%, #880e4f 100%);
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(211,47,47,0.6);
    }
    .btn-sitetour-zalo {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: #0068ff;
      color: #ffffff !important;
      padding: 12px 22px;
      border-radius: 30px;
      font-weight: 700;
      font-size: 0.92rem;
      text-decoration: none;
      box-shadow: 0 4px 16px rgba(0,104,255,0.4);
      transition: all 0.25s ease;
    }
    .btn-sitetour-zalo:hover {
      background: #0052cc;
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(0,104,255,0.6);
    }
    .btn-sitetour-modal {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: rgba(255, 255, 255, 0.12);
      border: 1px solid rgba(201,169,110,0.6);
      color: #ffd166 !important;
      padding: 12px 22px;
      border-radius: 30px;
      font-weight: 700;
      font-size: 0.92rem;
      cursor: pointer;
      transition: all 0.25s ease;
    }
    .btn-sitetour-modal:hover {
      background: rgba(201,169,110,0.25);
      transform: translateY(-2px);
    }

    /* Floating Action Sticky Bar Mobile */
    .mobile-cta-sticky-bar {
      display: none;
    }
    @media (max-width: 768px) {
      .mobile-cta-sticky-bar {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        z-index: 9999;
        display: grid;
        grid-template-columns: 1fr 1fr 1fr;
        gap: 6px;
        background: rgba(18, 34, 25, 0.96);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        padding: 8px 10px calc(8px + env(safe-area-inset-bottom));
        border-top: 1px solid rgba(201,169,110,0.35);
        box-shadow: 0 -4px 20px rgba(0,0,0,0.3);
      }
      body {
        padding-bottom: 64px !important;
      }
    }
    .mobile-cta-btn {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 6px 4px;
      border-radius: 8px;
      font-size: 0.72rem;
      font-weight: 700;
      text-decoration: none;
      gap: 3px;
      text-align: center;
      border: none;
      cursor: pointer;
      transition: transform 0.15s ease;
    }
    .mobile-cta-btn:active {
      transform: scale(0.96);
    }
    .mobile-cta-btn.call {
      background: #c62828;
      color: #ffffff !important;
    }
    .mobile-cta-btn.zalo {
      background: #0068ff;
      color: #ffffff !important;
    }
    .mobile-cta-btn.tour {
      background: #c9a96e;
      color: #183024 !important;
    }
    .mobile-cta-btn i {
      font-size: 1rem;
    }

    /* Desktop Quick Floating Widget */
    .desktop-floating-cta {
      position: fixed;
      bottom: 24px;
      right: 24px;
      z-index: 9990;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }
    @media (max-width: 768px) {
      .desktop-floating-cta {
        display: none;
      }
    }
    .float-circle-btn {
      width: 52px;
      height: 52px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      color: #ffffff !important;
      font-size: 1.35rem;
      text-decoration: none;
      box-shadow: 0 4px 18px rgba(0,0,0,0.25);
      transition: all 0.25s ease;
      position: relative;
    }
    .float-circle-btn:hover {
      transform: scale(1.1);
    }
    .float-circle-btn.call {
      background: #d32f2f;
      animation: pulse-red 2s infinite;
    }
    .float-circle-btn.zalo {
      background: #0068ff;
      animation: pulse-blue 2s infinite 0.5s;
    }
    .float-circle-btn.tour {
      background: #183024;
      border: 2px solid #c9a96e;
      color: #ffd166 !important;
      cursor: pointer;
    }
    @keyframes pulse-red {
      0% { box-shadow: 0 0 0 0 rgba(211, 47, 47, 0.6); }
      70% { box-shadow: 0 0 0 12px rgba(211, 47, 47, 0); }
      100% { box-shadow: 0 0 0 0 rgba(211, 47, 47, 0); }
    }
    @keyframes pulse-blue {
      0% { box-shadow: 0 0 0 0 rgba(0, 104, 255, 0.6); }
      70% { box-shadow: 0 0 0 12px rgba(0, 104, 255, 0); }
      100% { box-shadow: 0 0 0 0 rgba(0, 104, 255, 0); }
    }

    /* Form within Modal */
    .lead-form-group {
      margin-bottom: 12px;
      text-align: left;
    }
    .lead-form-group label {
      display: block;
      font-size: 0.8rem;
      font-weight: 700;
      color: #183024;
      margin-bottom: 4px;
    }
    .lead-form-control {
      width: 100%;
      padding: 10px 14px;
      border: 1px solid #dcd3c1;
      border-radius: 8px;
      font-family: inherit;
      font-size: 0.88rem;
      background: #fdfbf7;
      color: #111;
      box-sizing: border-box;
      transition: border-color 0.2s;
    }
    .lead-form-control:focus {
      outline: none;
      border-color: #c9a96e;
      background: #fff;
    }
    .lead-form-submit {
      width: 100%;
      padding: 12px;
      background: linear-gradient(135deg, #183024 0%, #284c39 100%);
      color: #ffffff;
      border: none;
      border-radius: 8px;
      font-weight: 800;
      font-size: 0.95rem;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      margin-top: 14px;
      box-shadow: 0 4px 14px rgba(24,48,36,0.25);
      transition: all 0.2s ease;
    }
    .lead-form-submit:hover {
      background: linear-gradient(135deg, #244633 0%, #183024 100%);
      transform: translateY(-1px);
    }
    .direct-contact-channels {
      display: flex;
      gap: 10px;
      margin-top: 14px;
    }
    .channel-btn {
      flex: 1;
      padding: 9px 8px;
      border-radius: 8px;
      font-size: 0.82rem;
      font-weight: 700;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
    }
    .channel-btn.phone {
      background: #ffebee;
      color: #c62828 !important;
      border: 1px solid #ffcdd2;
    }
    .channel-btn.zalo {
      background: #e3f2fd;
      color: #0d47a1 !important;
      border: 1px solid #bbdefb;
    }
  </style>
"""

    html = html.replace('</style>', custom_css)

    # 3. Update top action bar to include Hotline & Zalo
    old_action_bar = re.search(r'<aside class="action-bar".*?</aside>', html, re.DOTALL)
    if old_action_bar:
        new_action_bar = """<aside class="action-bar" aria-label="Thanh công cụ trang web">
    <div style="display: flex; gap: 8px; flex-wrap: wrap; align-items: center;">
      <a href="index.html"><i class="fa-solid fa-arrow-left"></i> Trang Chủ</a>
      <a href="#buoc-6-dien-san"><i class="fa-solid fa-chart-line"></i> Bài Toán Điền Sản</a>
      <a href="#buoc-7-biet-phu"><i class="fa-solid fa-landmark"></i> Biệt Phủ</a>
      <a href="#buoc-5-dien-an"><i class="fa-solid fa-house-chimney-user"></i> Điền An</a>
      <a href="#buoc-8-loi-nhuan" style="color: var(--color-gold-dark); font-weight: 700;"><i class="fa-solid fa-arrow-trend-up"></i> Tiềm Năng Đầu Tư</a>
    </div>
    <div style="display: flex; gap: 8px; align-items: center; flex-wrap: wrap;">
      <a href="tel:0909000712" class="btn-hotline-nav"><i class="fa-solid fa-phone-volume"></i> 0909 000 712</a>
      <a href="https://zalo.me/0909000712" target="_blank" rel="noopener noreferrer" class="btn-zalo-nav"><i class="fa-solid fa-comment-dots"></i> Zalo</a>
      <button type="button" class="btn-cta-top" onclick="openBookingModal('', '', 'Đăng Ký Site Tour VIP')"><i class="fa-solid fa-car-side"></i> Đăng Ký Site Tour</button>
    </div>
  </aside>"""
        html = html.replace(old_action_bar.group(0), new_action_bar)

    # 4. Update Header Subtitle
    html = html.replace(
        '<div class="org-role">BẢN GIỚI THIỆU QUẦN THỂ ĐIỀN TRANG • BẢN SẮC VIỆT ĐƯƠNG ĐẠI</div>',
        '<div class="org-role">BẢN THUYẾT TRÌNH ĐẦU TƯ ĐIỀN TRANG NGHỈ DƯỠNG • BẢN SẮC VIỆT ĐƯƠNG ĐẠI</div>'
    )

    # 5. Redesign Step 08 with 4 Pillars, VIP Site Tour Perks, and INLINE FORM
    old_section_8 = re.search(r'<!-- ===+\s*BƯỚC 8:.*?<section class="pitch-step-section" id="buoc-8-loi-nhuan">.*?</section>', html, re.DOTALL)
    if old_section_8:
        new_section_8 = """<!-- ================================================================
           BƯỚC 8: 4 TRỤ CỘT ĐỘT PHÁ TĂNG GIÁ TRỊ & DÒNG TIỀN THỰC TẾ
           ================================================================ -->
      <section class="pitch-step-section" id="buoc-8-loi-nhuan">
        <div class="step-counter-tag"><i class="fa-solid fa-arrow-trend-up"></i> 08 • TIỀM NĂNG TĂNG TRƯỞNG TÀI SẢN</div>
        <h3 class="sheet-section-title">4 Đòn Bẩy Thúc Đẩy Giá Trị Điền Trang Ven Hồ 100ha</h3>
        <p class="section-subtitle">
          Sở hữu điền trang tại Saigon Farm Resort là nắm giữ tài sản có giá trị tích sản gia tăng lũy tiến theo tiến độ hạ tầng và dòng tiền khai thác bền vững từ đơn vị vận hành MDS Living.
        </p>

        <!-- 4 Khối Đòn Bẩy Tăng Trưởng Cốt Lõi (Ý chính súc tích, không công bố bảng chiết tính) -->
        <div class="investment-growth-pillars-grid">
          <!-- Trụ Cột 1 -->
          <div class="growth-pillar-card">
            <div class="growth-pillar-icon"><i class="fa-solid fa-plane-departure"></i></div>
            <div class="growth-pillar-content">
              <h4>1. Sóng Đòn Bẩy Hạ Tầng Trọng Điểm (2025 – 2027)</h4>
              <p>Hưởng lợi trực tiếp từ tam giác hạ tầng giao thông kết nối Đông Nam Bộ: <strong>Cao tốc Biên Hòa – Vũng Tàu</strong> thông xe toàn tuyến rút ngắn thời gian về TP.HCM còn 60 – 75 phút; <strong>Sân bay Quốc tế Long Thành</strong> vận hành đón hàng chục triệu lượt khách quốc tế chỉ cách 45 phút; và trục ven biển <strong>ĐT994 mở rộng 6 – 8 làn xe</strong> kết nối thẳng thủ phủ tỷ đô Hồ Tràm.</p>
            </div>
          </div>

          <!-- Trụ Cột 2 -->
          <div class="growth-pillar-card">
            <div class="growth-pillar-icon"><i class="fa-solid fa-mountain-sun"></i></div>
            <div class="growth-pillar-content">
              <h4>2. Hoàn Thiện Đại Tiện Ích Lên Đến 30.000 m²</h4>
              <p>Mặt bằng giá tài sản được thiết lập nấc thang mới theo từng mốc vận hành: <strong>Lake Clubhouse 3.000 m²</strong> sàn sát mép nước, <strong>Làng ngựa quý tộc Việt Mã Viên (6.800 m²)</strong>, <strong>Hồ bơi vô cực điện phân muối khoáng</strong> và hệ thống bến thuyền Kayak trên mặt hồ 100ha.</p>
            </div>
          </div>

          <!-- Trụ Cột 3 -->
          <div class="growth-pillar-card">
            <div class="growth-pillar-icon"><i class="fa-solid fa-certificate"></i></div>
            <div class="growth-pillar-content">
              <h4>3. Quỹ Đất Thổ Cư Ven Hồ Độc Bản & Sổ Đỏ Lâu Dài</h4>
              <p>Toàn khu giới hạn chỉ <strong>47 sản phẩm điền trang</strong>, 100% thổ cư với sổ đỏ riêng từng nền, sang tên công chứng nhận sổ ngay trong 10 – 20 ngày. Vị thế phong thủy ven hồ tự nhiên 100ha là tài sản di sản truyền đời có độ khan hiếm không thể tái tạo.</p>
            </div>
          </div>

          <!-- Trụ Cột 4 -->
          <div class="growth-pillar-card">
            <div class="growth-pillar-icon"><i class="fa-solid fa-hand-holding-dollar"></i></div>
            <div class="growth-pillar-content">
              <h4>4. Dòng Tiền Khai Thác Kép Bền Vững Cùng MDS Living</h4>
              <p>Khách hàng có thể lựa chọn nhận dòng tiền cho thuê thụ động từ <strong>80 – 120 Triệu/tháng (1,44 Tỷ/năm)</strong> với cụm phòng chuyên gia dòng Điền An, hoặc tham gia chương trình <strong>MDS Living cam kết mua lại 90 – 150 đêm lưu trú/năm</strong> với dòng Biệt Phủ.</p>
            </div>
          </div>
        </div>

        <!-- Khung Kêu Gọi Site Tour VIP & Form Đăng Ký Trực Tiếp -->
        <div class="sitetour-exclusive-box">
          <div class="sitetour-badge">
            <i class="fa-solid fa-car-side"></i> ĐẶC QUYỀN TRẢI NGHIỆM THỰC TẾ
          </div>
          <h4 class="sitetour-title">Đăng Ký Site Tour Khảo Sát Thực Địa &amp; Nhận Bảng Tính Suất Sinh Lời</h4>
          <p class="sitetour-desc">
            Để bảo đảm quyền lợi tối đa và tính bảo mật của dữ liệu đầu tư, <strong>Bảng chiết tính tỷ suất sinh lời chi tiết theo từng mã nền, phương án tài chính tối ưu và kịch bản dòng tiền thực tế</strong> sẽ được chuyên viên cấp cao phân tích trực tiếp cho Quý khách trong chuyến khảo sát thực địa (Site Tour VIP).
          </p>

          <div class="sitetour-perks-list">
            <div class="sitetour-perk-item">
              <i class="fa-solid fa-circle-check"></i>
              <span>Xe ô tô riêng chất lượng cao đưa đón tận nơi (TP.HCM &harr; Hồ Lồ Ồ, Đất Đỏ).</span>
            </div>
            <div class="sitetour-perk-item">
              <i class="fa-solid fa-circle-check"></i>
              <span>Trải nghiệm không gian mặt hồ sinh thái 100ha nguyên bản và ngắm hoàng hôn lộng gió.</span>
            </div>
            <div class="sitetour-perk-item">
              <i class="fa-solid fa-circle-check"></i>
              <span>Thưởng thức ẩm thực Farm-to-Table tươi sạch và tiệc trà chiều tại khuôn viên thực địa.</span>
            </div>
            <div class="sitetour-perk-item">
              <i class="fa-solid fa-circle-check"></i>
              <span>Trực tiếp kiểm tra mốc ranh quy hoạch, hồ sơ sổ đỏ riêng và nhận tư vấn giỏ hàng ưu tiên đợt 1.</span>
            </div>
          </div>

          <!-- Form Đăng Ký Trực Tiếp (Inline High-Converting Lead Form) -->
          <div class="sitetour-inline-form-card">
            <div class="inline-form-header">
              <i class="fa-solid fa-pen-nib" style="color: #ffd166;"></i>
              <span>ĐĂNG KÝ TRỰC TIẾP SITE TOUR &amp; NHẬN BẢNG TÍNH SUẤT SINH LỜI</span>
            </div>
            <form id="inline-lead-form" onsubmit="handleInlineSubmit(event)">
              <div class="inline-form-inputs">
                <div class="inline-input-group">
                  <i class="fa-solid fa-user input-icon"></i>
                  <input type="text" id="inline-name" placeholder="Họ và tên của Quý khách" required class="inline-form-input">
                </div>
                <div class="inline-input-group">
                  <i class="fa-solid fa-phone input-icon"></i>
                  <input type="tel" id="inline-phone" placeholder="Số điện thoại / Zalo" required pattern="[0-9]{9,11}" class="inline-form-input">
                </div>
                <div class="inline-input-group">
                  <i class="fa-solid fa-shapes input-icon"></i>
                  <select id="inline-product" class="inline-form-input">
                    <option value="Điền Sản (Founders)">Điền Sản (Founders) — Đất nền ven hồ</option>
                    <option value="Biệt Phủ Điền Trang">Biệt Phủ Điền Trang — Dinh thự sinh thái</option>
                    <option value="Điền An (Haven)">Điền An (Haven) — Dòng tiền 120 tr/tháng</option>
                    <option value="Đăng ký Site Tour cuối tuần">Đăng ký Site Tour trải nghiệm thực tế</option>
                  </select>
                </div>
              </div>
              <button type="submit" class="btn-inline-submit">
                <i class="fa-solid fa-paper-plane"></i>
                <span>Gửi Yêu Cầu &amp; Kết Nối Zalo 0909 000 712</span>
              </button>
            </form>
            <div id="inline-success-msg" style="display:none;" class="inline-success-banner">
              <i class="fa-solid fa-circle-check"></i>
              <span><strong>Đăng ký thành công!</strong> Chuyên viên tư vấn sẽ gửi tài liệu qua Zalo và sắp xếp lịch đón Quý khách.</span>
            </div>
          </div>

          <div class="sitetour-cta-actions">
            <a href="tel:0909000712" class="btn-sitetour-hotline">
              <i class="fa-solid fa-phone-volume"></i>
              <span>Hotline Tư Vấn: <strong>0909 000 712</strong></span>
            </a>
            <a href="https://zalo.me/0909000712" target="_blank" rel="noopener noreferrer" class="btn-sitetour-zalo">
              <i class="fa-solid fa-comment-dots"></i>
              <span>Nhắn Zalo Nhận Bảng Tính: <strong>0909 000 712</strong></span>
            </a>
            <button type="button" class="btn-sitetour-modal" onclick="openBookingModal('', '', 'Đăng Ký Site Tour Tham Quan')">
              <i class="fa-solid fa-calendar-check"></i>
              <span>Xem Thêm Lịch Trình</span>
            </button>
          </div>
        </div>
      </section>"""
        html = html.replace(old_section_8.group(0), new_section_8)

    # 6. Update Section 9 Action CTA Box
    old_cta_box = re.search(r'<div class="action-cta-box">.*?</div>\s*</section>', html, re.DOTALL)
    if old_cta_box:
        new_cta_box = """<div class="action-cta-box">
          <h4>Đăng Ký Khảo Sát Thực Địa &amp; Chọn Vị Trí Đẹp Nhất Đợt 1</h4>
          <p>
            Chỉ 36 sản phẩm Điền Trang độc bản mở bán đợt đầu tiên. Kính mời Quý khách liên hệ trực tiếp qua Hotline / Zalo hoặc gửi yêu cầu để được đón tiếp khảo sát thực địa bằng xe riêng và nhận trọn bộ hồ sơ pháp lý &amp; bảng giá chi tiết.
          </p>
          <div style="display: flex; gap: 12px; justify-content: center; flex-wrap: wrap; margin-top: 18px;">
            <a href="tel:0909000712" class="btn-sitetour-hotline">
              <i class="fa-solid fa-phone-volume"></i>
              <span>Gọi Hotline: 0909 000 712</span>
            </a>
            <a href="https://zalo.me/0909000712" target="_blank" rel="noopener noreferrer" class="btn-sitetour-zalo">
              <i class="fa-solid fa-comment-dots"></i>
              <span>Chat Zalo: 0909 000 712</span>
            </a>
            <button type="button" class="btn-cta-large" style="margin: 0;" onclick="openBookingModal('', '', 'Hồ Sơ &amp; Bảng Giá Chi Tiết')">
              <i class="fa-solid fa-file-signature"></i>
              <span>Đăng Ký Nhận Hồ Sơ &amp; Bảng Giá</span>
            </button>
          </div>
        </div>
      </section>"""
        html = html.replace(old_cta_box.group(0), new_cta_box)

    # 7. Update Footer with Phone and Zalo
    old_footer_company = re.search(r'<div class="company-details">.*?</div>', html, re.DOTALL)
    if old_footer_company:
        new_footer_company = """<div class="company-details">
          <strong>MDS LAND &amp; LIVING • SAIGON FARM RESORT</strong><br>
          <i class="fa-solid fa-location-dot" style="color: var(--color-gold-dark); margin-right: 4px;"></i> Xã Đất Đỏ, TP. Hồ Chí Minh<br>
          <i class="fa-solid fa-phone-volume" style="color: var(--color-gold-dark); margin-right: 4px;"></i> Hotline: <a href="tel:0909000712" style="color: inherit; font-weight: 700;">0909 000 712</a><br>
          <i class="fa-solid fa-comment-dots" style="color: var(--color-gold-dark); margin-right: 4px;"></i> Zalo: <a href="https://zalo.me/0909000712" target="_blank" rel="noopener noreferrer" style="color: inherit; font-weight: 700;">0909 000 712</a><br>
          <i class="fa-solid fa-globe" style="color: var(--color-gold-dark); margin-right: 4px;"></i> Website: <a href="https://www.saigonfarmresort.com" style="color: inherit; text-decoration: underline;">www.saigonfarmresort.com</a>
        </div>"""
        html = html.replace(old_footer_company.group(0), new_footer_company)

    # 8. Upgrade Booking Modal to Interactive Lead Capture Form
    old_modal = re.search(r'<!-- ===+\s*ELEGANT BOOKING GUIDANCE MODAL.*?<div id="booking-modal".*?</div>\s*</div>', html, re.DOTALL)
    if old_modal:
        new_modal = """<!-- ================================================================
       INTERACTIVE SITE TOUR & INVESTMENT BOOKING MODAL
       ================================================================ -->
  <div id="booking-modal" class="booking-modal-overlay" onclick="closeBookingModal()">
    <div class="booking-modal-box" onclick="event.stopPropagation()">
      <button class="modal-close-btn" onclick="closeBookingModal()" aria-label="Đóng">&times;</button>
      
      <div class="modal-emblem">
        <i class="fa-solid fa-car-side"></i>
      </div>
      
      <h3 class="modal-title">Đăng Ký Site Tour &amp; Nhận Bảng Giá</h3>
      <div class="modal-subtitle">Saigon Farm Resort • Hotline: 0909 000 712 • Zalo: 0909 000 712</div>
      
      <div id="modal-unit-tag" class="modal-unit-tag" style="display:none;"></div>
      
      <form id="lead-capture-form" onsubmit="handleLeadSubmit(event)">
        <div class="lead-form-group">
          <label for="lead-name">Họ và tên của Quý khách:</label>
          <input type="text" id="lead-name" class="lead-form-control" placeholder="Ví dụ: Nguyễn Văn An" required>
        </div>
        
        <div class="lead-form-group">
          <label for="lead-phone">Số điện thoại / Zalo (Bắt buộc):</label>
          <input type="tel" id="lead-phone" class="lead-form-control" placeholder="Ví dụ: 0909 000 712" required pattern="[0-9]{9,11}">
        </div>

        <div class="lead-form-group">
          <label for="lead-product">Dòng sản phẩm Quý khách quan tâm:</label>
          <select id="lead-product" class="lead-form-control">
            <option value="Điền Sản (Founders)">Điền Sản (Founders Club) — Đất nền điền trang ven hồ</option>
            <option value="Biệt Phủ Điền Trang">Biệt Phủ Điền Trang — Dinh thự sinh thái ven hồ</option>
            <option value="Điền An (Haven)">Điền An (Haven) — Dòng tiền 120 triệu/tháng</option>
            <option value="Đăng ký Site Tour cuối tuần">Đăng ký Site Tour trải nghiệm thực tế cuối tuần</option>
          </select>
        </div>

        <button type="submit" class="lead-form-submit">
          <i class="fa-solid fa-paper-plane"></i>
          <span>Xác Nhận &amp; Gửi Yêu Cầu Qua Zalo 0909 000 712</span>
        </button>
      </form>

      <div class="direct-contact-channels">
        <a href="tel:0909000712" class="channel-btn phone">
          <i class="fa-solid fa-phone-volume"></i> Gọi: 0909 000 712
        </a>
        <a href="https://zalo.me/0909000712" target="_blank" rel="noopener noreferrer" class="channel-btn zalo">
          <i class="fa-solid fa-comment-dots"></i> Chat Zalo Ngay
        </a>
      </div>
      
      <div id="form-success-msg" style="display:none; margin-top: 14px; padding: 12px; background: #e8f5e9; border: 1px solid #c8e6c9; border-radius: 8px; color: #2e7d32; font-size: 0.88rem; text-align: center;">
        <i class="fa-solid fa-circle-check" style="margin-right: 6px;"></i>
        <strong>Đăng ký thành công!</strong> Chuyên viên tư vấn sẽ liên hệ Quý khách trong ít phút.
      </div>
    </div>
  </div>"""
        html = html.replace(old_modal.group(0), new_modal)

    # 9. Add Sticky Mobile Bar, Desktop Floating Widget, and Conversion Event Tracking before </body>
    mobile_and_floating_cta = """
  <!-- ================================================================
       STICKY ACTION BAR FOR MOBILE & FLOATING CTA DESKTOP
       ================================================================ -->
  <!-- Mobile Sticky Bar -->
  <div class="mobile-cta-sticky-bar" aria-label="Thanh liên hệ nhanh">
    <a href="tel:0909000712" class="mobile-cta-btn call">
      <i class="fa-solid fa-phone-volume"></i>
      <span>0909 000 712</span>
    </a>
    <a href="https://zalo.me/0909000712" target="_blank" rel="noopener noreferrer" class="mobile-cta-btn zalo">
      <i class="fa-solid fa-comment-dots"></i>
      <span>Nhắn Zalo</span>
    </a>
    <button type="button" class="mobile-cta-btn tour" onclick="openBookingModal('', '', 'Đăng Ký Site Tour')">
      <i class="fa-solid fa-car-side"></i>
      <span>Site Tour VIP</span>
    </button>
  </div>

  <!-- Desktop Floating Quick Buttons -->
  <div class="desktop-floating-cta" aria-label="Kênh kết nối nhanh">
    <a href="tel:0909000712" class="float-circle-btn call" title="Gọi Hotline: 0909 000 712">
      <i class="fa-solid fa-phone"></i>
    </a>
    <a href="https://zalo.me/0909000712" target="_blank" rel="noopener noreferrer" class="float-circle-btn zalo" title="Chat Zalo: 0909 000 712">
      <i class="fa-solid fa-comment-dots"></i>
    </a>
    <button type="button" class="float-circle-btn tour" onclick="openBookingModal('', '', 'Đăng Ký Site Tour VIP')" title="Đăng Ký Site Tour Xe Riêng">
      <i class="fa-solid fa-car-side"></i>
    </button>
  </div>

  <script>
    // Universal Event Tracking for Facebook Pixel (fbq) & Google Analytics (gtag)
    function trackConversionEvent(eventName, params) {
      if (typeof fbq === 'function') {
        fbq('track', eventName, params);
      }
      if (typeof gtag === 'function') {
        gtag('event', eventName, params);
      }
      console.log('[Analytics Event]', eventName, params);
    }

    // Track Phone and Zalo clicks
    document.addEventListener('DOMContentLoaded', function() {
      document.querySelectorAll('a[href^="tel:"]').forEach(function(el) {
        el.addEventListener('click', function() {
          trackConversionEvent('Contact', { type: 'phone_call', value: '0909000712' });
        });
      });
      document.querySelectorAll('a[href*="zalo.me"]').forEach(function(el) {
        el.addEventListener('click', function() {
          trackConversionEvent('Contact', { type: 'zalo_chat', value: '0909000712' });
        });
      });
    });

    // Handle Inline Form
    function handleInlineSubmit(e) {
      e.preventDefault();
      var name = document.getElementById('inline-name').value.trim();
      var phone = document.getElementById('inline-phone').value.trim();
      var product = document.getElementById('inline-product').value;

      trackConversionEvent('Lead', { content_name: product, lead_source: 'inline_form', phone: phone });

      var text = encodeURIComponent("Chào Saigon Farm Resort, tôi là " + name + " (SĐT: " + phone + "). Tôi quan tâm: " + product + ". Xin gửi bảng tính suất sinh lời và hỗ trợ lịch Site Tour.");
      
      var msgBox = document.getElementById('inline-success-msg');
      if (msgBox) msgBox.style.display = 'flex';
      
      setTimeout(function() {
        window.open("https://zalo.me/0909000712?text=" + text, "_blank");
      }, 600);
    }

    // Handle Modal Form
    function handleLeadSubmit(e) {
      e.preventDefault();
      var name = document.getElementById('lead-name').value.trim();
      var phone = document.getElementById('lead-phone').value.trim();
      var product = document.getElementById('lead-product').value;

      trackConversionEvent('Lead', { content_name: product, lead_source: 'modal_popup', phone: phone });

      var text = encodeURIComponent("Chào Saigon Farm Resort, tôi là " + name + " (SĐT: " + phone + "). Tôi đang quan tâm: " + product + ". Nhờ chuyên viên gửi bảng tính suất sinh lời và hỗ trợ lịch Site Tour.");
      
      var msgBox = document.getElementById('form-success-msg');
      if (msgBox) msgBox.style.display = 'block';
      
      setTimeout(function() {
        window.open("https://zalo.me/0909000712?text=" + text, "_blank");
      }, 600);
    }
  </script>
"""
    html = html.replace('</body>', mobile_and_floating_cta + '\n</body>')

    # Double-check: ensure NO instance of "dự án" exists
    html = re.sub(r'dự án', 'quần thể', html, flags=re.IGNORECASE)

    # Write investment.html
    with open("investment.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Created investment.html successfully! Size:", len(html))

    # Also create investment/index.html
    os.makedirs("investment", exist_ok=True)
    with open("investment/index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Created investment/index.html successfully!")

if __name__ == "__main__":
    build_investment_page()
