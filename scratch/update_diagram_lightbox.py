import os, re

# ==============================================================================
# 1. UPDATE THU-MOI.HTML
# ==============================================================================

with open('thu-moi.html', 'r', encoding='utf-8') as f:
    thu_moi = f.read()

# CSS to inject into thu-moi.html before </style>
diagram_css = '''
    /* ================================================================
       DIAGRAM IN-PAGE LIGHTBOX MODAL (KHÔNG NHẢY SANG TAB MỚI)
       ================================================================ */
    .diagram-lightbox-modal {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      height: 100dvh;
      background: rgba(8, 14, 10, 0.96);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      z-index: 10005;
      display: none;
      flex-direction: column;
      justify-content: space-between;
      opacity: 0;
      transition: opacity 0.25s ease;
    }
    .diagram-lightbox-modal.active {
      display: flex;
      opacity: 1;
    }
    .diagram-lightbox-header {
      padding: 12px 18px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: rgba(10, 18, 14, 0.9);
      border-bottom: 1px solid rgba(255, 255, 255, 0.1);
      z-index: 10;
      flex-shrink: 0;
      gap: 12px;
    }
    .diagram-lb-title-box {
      display: flex;
      flex-direction: column;
      gap: 2px;
      overflow: hidden;
    }
    .diagram-lb-badge {
      display: inline-block;
      font-size: 0.7rem;
      font-weight: 800;
      color: #dfc89f;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }
    .diagram-lb-title {
      font-family: var(--font-serif);
      font-size: 1.02rem;
      color: #fff;
      margin: 0;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }
    .diagram-lb-controls {
      display: flex;
      align-items: center;
      gap: 10px;
      flex-shrink: 0;
    }
    .diagram-lb-zoom-btn {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: rgba(255,255,255,0.12);
      border: 1px solid rgba(255,255,255,0.22);
      color: #fff;
      padding: 6px 14px;
      border-radius: 20px;
      font-size: 0.78rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s;
    }
    .diagram-lb-zoom-btn:hover {
      background: rgba(194, 155, 83, 0.35);
      border-color: #c29b53;
      color: #f7eed9;
    }
    .diagram-lb-close {
      width: 36px;
      height: 36px;
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.15);
      border: 1px solid rgba(255, 255, 255, 0.25);
      color: #ffffff;
      font-size: 1.15rem;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: all 0.2s ease;
    }
    .diagram-lb-close:hover {
      background: #c62828;
      border-color: #c62828;
      transform: scale(1.05);
    }
    .diagram-lightbox-body {
      flex: 1;
      position: relative;
      overflow: auto;
      -webkit-overflow-scrolling: touch;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 12px;
      cursor: zoom-in;
    }
    .diagram-lightbox-body.is-zoomed {
      cursor: zoom-out;
      display: block;
      text-align: center;
    }
    .diagram-img-wrap {
      display: inline-block;
      transition: transform 0.25s ease;
      max-width: 100%;
      max-height: 100%;
    }
    .diagram-lightbox-body.is-zoomed .diagram-img-wrap {
      max-width: none;
      max-height: none;
      width: 175%;
    }
    @media (min-width: 768px) {
      .diagram-lightbox-body.is-zoomed .diagram-img-wrap {
        width: 135%;
      }
    }
    .diagram-lightbox-body img {
      width: 100%;
      height: auto;
      max-height: 80vh;
      object-fit: contain;
      border-radius: 6px;
      box-shadow: 0 12px 40px rgba(0,0,0,0.5);
      display: block;
      margin: 0 auto;
    }
    .diagram-lightbox-body.is-zoomed img {
      max-height: none;
      border-radius: 4px;
    }
    .diagram-lightbox-footer {
      padding: 8px 18px;
      background: rgba(10, 18, 14, 0.9);
      border-top: 1px solid rgba(255, 255, 255, 0.08);
      color: rgba(255, 255, 255, 0.7);
      font-size: 0.78rem;
      text-align: center;
      flex-shrink: 0;
    }
'''

assert '</style>' in thu_moi, "No </style> tag in thu-moi.html"
thu_moi = thu_moi.replace('</style>', diagram_css + '\n  </style>', 1)

# Update the 2 diagrams in thu-moi.html
old_diagram_1 = '''      <!-- Sơ Đồ 1: Tiện Ích Khu Vực Trung Tâm -->
      <figure class="editorial-diagram-showcase" style="margin-bottom: 24px;">
        <a href="assets/Index_asset/MatBang/SGFR_tien_ich_trung_tam.png" target="_blank" style="display: block; position: relative; text-decoration: none;">
          <img src="assets/Index_asset/MatBang/SGFR_tien_ich_trung_tam.webp" alt="Sơ đồ phân bổ tiện ích khu vực trung tâm Saigon Farm Resort" class="diagram-img" loading="lazy">
          <span class="diagram-zoom-badge" style="position: absolute; bottom: 12px; right: 12px; background: rgba(0,0,0,0.75); color: #fff; padding: 6px 14px; border-radius: 20px; font-size: 0.8rem; font-weight: 600; backdrop-filter: blur(4px); display: inline-flex; align-items: center; gap: 6px;"><i class="fa-solid fa-expand"></i> Nhấp xem ảnh gốc</span>
        </a>'''

new_diagram_1 = '''      <!-- Sơ Đồ 1: Tiện Ích Khu Vực Trung Tâm -->
      <figure class="editorial-diagram-showcase" style="margin-bottom: 24px;">
        <div onclick="openDiagramModal('assets/Index_asset/MatBang/SGFR_tien_ich_trung_tam.png', '1. Sơ Đồ Phân Bổ Tiện Ích Khu Vực Trung Tâm', 'Phân Khu Trung Tâm', 'Chạm vào ảnh để phóng to chi tiết 50 hạng mục hoặc bấm X để đóng.')" style="display: block; position: relative; text-decoration: none; cursor: pointer;">
          <img src="assets/Index_asset/MatBang/SGFR_tien_ich_trung_tam.webp" alt="Sơ đồ phân bổ tiện ích khu vực trung tâm Saigon Farm Resort" class="diagram-img" loading="lazy">
          <span class="diagram-zoom-badge" style="position: absolute; bottom: 12px; right: 12px; background: rgba(0,0,0,0.75); color: #fff; padding: 6px 14px; border-radius: 20px; font-size: 0.8rem; font-weight: 600; backdrop-filter: blur(4px); display: inline-flex; align-items: center; gap: 6px;"><i class="fa-solid fa-expand"></i> Nhấp xem ảnh gốc</span>
        </div>'''

assert old_diagram_1 in thu_moi, "old_diagram_1 not found in thu-moi.html"
thu_moi = thu_moi.replace(old_diagram_1, new_diagram_1, 1)

old_diagram_2 = '''      <!-- Sơ Đồ 2: Tiện Ích Ven Hồ -->
      <figure class="editorial-diagram-showcase" style="margin-bottom: 32px;">
        <a href="assets/Index_asset/MatBang/SGFR_Tien_ich_Ven_ho.png" target="_blank" style="display: block; position: relative; text-decoration: none;">
          <img src="assets/Index_asset/MatBang/SGFR_Tien_ich_Ven_ho.webp" alt="Sơ đồ phân bổ tiện ích ven hồ Saigon Farm Resort" class="diagram-img" loading="lazy">
          <span class="diagram-zoom-badge" style="position: absolute; bottom: 12px; right: 12px; background: rgba(0,0,0,0.75); color: #fff; padding: 6px 14px; border-radius: 20px; font-size: 0.8rem; font-weight: 600; backdrop-filter: blur(4px); display: inline-flex; align-items: center; gap: 6px;"><i class="fa-solid fa-expand"></i> Nhấp xem ảnh gốc</span>
        </a>'''

new_diagram_2 = '''      <!-- Sơ Đồ 2: Tiện Ích Ven Hồ -->
      <figure class="editorial-diagram-showcase" style="margin-bottom: 32px;">
        <div onclick="openDiagramModal('assets/Index_asset/MatBang/SGFR_Tien_ich_Ven_ho.png', '2. Sơ Đồ Phân Bổ Tiện Ích Ven Hồ', 'Phân Khu Ven Hồ', 'Chạm vào ảnh để phóng to chi tiết 26 hạng mục ven hồ hoặc bấm X để đóng.')" style="display: block; position: relative; text-decoration: none; cursor: pointer;">
          <img src="assets/Index_asset/MatBang/SGFR_Tien_ich_Ven_ho.webp" alt="Sơ đồ phân bổ tiện ích ven hồ Saigon Farm Resort" class="diagram-img" loading="lazy">
          <span class="diagram-zoom-badge" style="position: absolute; bottom: 12px; right: 12px; background: rgba(0,0,0,0.75); color: #fff; padding: 6px 14px; border-radius: 20px; font-size: 0.8rem; font-weight: 600; backdrop-filter: blur(4px); display: inline-flex; align-items: center; gap: 6px;"><i class="fa-solid fa-expand"></i> Nhấp xem ảnh gốc</span>
        </div>'''

assert old_diagram_2 in thu_moi, "old_diagram_2 not found in thu-moi.html"
thu_moi = thu_moi.replace(old_diagram_2, new_diagram_2, 1)

# Add Diagram Modal Markup and JS before </body>
diagram_markup_and_js = '''
  <!-- ================================================================
       MODAL PHÓNG TO SƠ ĐỒ TIỆN ÍCH TRONG TRANG (IN-PAGE LIGHTBOX)
       ================================================================ -->
  <div class="diagram-lightbox-modal" id="diagram-lightbox" role="dialog" aria-modal="true" aria-label="Xem chi tiết sơ đồ tiện ích" onclick="handleDiagramBackdropClick(event)">
    <div class="diagram-lightbox-header" onclick="event.stopPropagation()">
      <div class="diagram-lb-title-box">
        <span class="diagram-lb-badge" id="diagram-lb-badge">Phân Khu Tiện Ích</span>
        <h4 class="diagram-lb-title" id="diagram-lb-title">Sơ Đồ Phân Bổ Tiện Ích</h4>
      </div>
      <div class="diagram-lb-controls">
        <button type="button" class="diagram-lb-zoom-btn" onclick="toggleDiagramZoom(event)" id="diagramZoomToggleBtn" title="Phóng to / Thu nhỏ">
          <i class="fa-solid fa-magnifying-glass-plus"></i> <span class="zoom-btn-text">Phóng to</span>
        </button>
        <button type="button" class="diagram-lb-close" onclick="closeDiagramModal()" aria-label="Đóng"><i class="fa-solid fa-xmark"></i></button>
      </div>
    </div>
    <div class="diagram-lightbox-body" id="diagram-lb-body">
      <div class="diagram-img-wrap" id="diagramImgWrap">
        <img id="diagram-lb-img" src="" alt="Sơ đồ tiện ích chi tiết" onclick="toggleDiagramZoom(event)">
      </div>
    </div>
    <div class="diagram-lightbox-footer" onclick="event.stopPropagation()">
      <span id="diagram-lb-desc">Chạm vào ảnh để phóng to / thu nhỏ. Nhấp ra ngoài hoặc bấm nút [X] để đóng lại.</span>
    </div>
  </div>

  <script>
    window.openDiagramModal = function(src, title, badge, desc) {
      const modal = document.getElementById('diagram-lightbox');
      const img = document.getElementById('diagram-lb-img');
      const titleEl = document.getElementById('diagram-lb-title');
      const badgeEl = document.getElementById('diagram-lb-badge');
      const descEl = document.getElementById('diagram-lb-desc');
      const body = document.getElementById('diagram-lb-body');
      
      if (!modal || !img) return;

      img.src = src;
      if (titleEl) titleEl.textContent = title || 'Sơ Đồ Phân Bổ Tiện Ích';
      if (badgeEl) badgeEl.textContent = badge || 'Phân Khu Tiện Ích';
      if (descEl) descEl.textContent = desc || 'Chạm vào ảnh để phóng to/thu nhỏ. Nhấp ra ngoài hoặc bấm [X] để đóng.';
      
      if (body) body.classList.remove('is-zoomed');
      updateZoomButtonState(false);

      modal.style.display = 'flex';
      setTimeout(() => {
        modal.classList.add('active');
        document.body.style.overflow = 'hidden';
      }, 10);
    };

    window.closeDiagramModal = function() {
      const modal = document.getElementById('diagram-lightbox');
      if (!modal) return;
      modal.classList.remove('active');
      setTimeout(() => {
        modal.style.display = 'none';
        document.body.style.overflow = '';
      }, 250);
    };

    window.handleDiagramBackdropClick = function(e) {
      if (e.target.id === 'diagram-lightbox' || e.target.id === 'diagram-lb-body') {
        closeDiagramModal();
      }
    };

    window.toggleDiagramZoom = function(e) {
      if (e) e.stopPropagation();
      const body = document.getElementById('diagram-lb-body');
      if (!body) return;
      const isZoomed = body.classList.toggle('is-zoomed');
      updateZoomButtonState(isZoomed);
    };

    function updateZoomButtonState(isZoomed) {
      const btn = document.getElementById('diagramZoomToggleBtn');
      if (!btn) return;
      if (isZoomed) {
        btn.innerHTML = '<i class="fa-solid fa-magnifying-glass-minus"></i> <span class="zoom-btn-text">Thu nhỏ</span>';
      } else {
        btn.innerHTML = '<i class="fa-solid fa-magnifying-glass-plus"></i> <span class="zoom-btn-text">Phóng to</span>';
      }
    }

    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape') {
        closeDiagramModal();
      }
    });
  </script>
'''

thu_moi = thu_moi.replace('</body>', diagram_markup_and_js + '\n</body>', 1)

with open('thu-moi.html', 'w', encoding='utf-8') as f:
    f.write(thu_moi)

print("SUCCESS: thu-moi.html updated with in-page diagram lightbox!")


# ==============================================================================
# 2. ALSO UPDATE INDEX.HTML FOR A CONSISTENT EXPERIENCE
# ==============================================================================

with open('index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()

# Add CSS to index.html
if '.diagram-lightbox-modal' not in idx_content:
    idx_content = idx_content.replace('</style>', diagram_css + '\n  </style>', 1)

# Replace the 2 card links in index.html
old_idx_card1 = '''    <a href="assets/Index_asset/MatBang/SGFR_tien_ich_trung_tam.png" target="_blank" style="display: block; position: relative; overflow: hidden;">
      <img src="assets/Index_asset/MatBang/SGFR_tien_ich_trung_tam.webp" alt="Sơ đồ tiện ích khu vực trung tâm Saigon Farm Resort" style="width: 100%; height: auto; display: block;">
      <span style="position: absolute; bottom: 12px; right: 12px; background: rgba(0,0,0,0.75); color: #fff; padding: 6px 12px; border-radius: 16px; font-size: 0.78rem; font-weight: 600; backdrop-filter: blur(4px);"><i class="fa-solid fa-expand"></i> Nhấp xem ảnh gốc</span>
    </a>'''

new_idx_card1 = '''    <div onclick="openDiagramModal('assets/Index_asset/MatBang/SGFR_tien_ich_trung_tam.png', 'Sơ Đồ Phân Bổ Tiện Ích Khu Vực Trung Tâm', 'Phân Khu Trung Tâm (50 Hạng Mục)', 'Chạm vào ảnh để phóng to chi tiết 50 hạng mục hoặc bấm [X] để đóng.')" style="display: block; position: relative; overflow: hidden; cursor: pointer;">
      <img src="assets/Index_asset/MatBang/SGFR_tien_ich_trung_tam.webp" alt="Sơ đồ tiện ích khu vực trung tâm Saigon Farm Resort" style="width: 100%; height: auto; display: block;">
      <span style="position: absolute; bottom: 12px; right: 12px; background: rgba(0,0,0,0.75); color: #fff; padding: 6px 12px; border-radius: 16px; font-size: 0.78rem; font-weight: 600; backdrop-filter: blur(4px);"><i class="fa-solid fa-expand"></i> Nhấp xem ảnh gốc</span>
    </div>'''

if old_idx_card1 in idx_content:
    idx_content = idx_content.replace(old_idx_card1, new_idx_card1, 1)

old_idx_card2 = '''    <a href="assets/Index_asset/MatBang/SGFR_Tien_ich_Ven_ho.png" target="_blank" style="display: block; position: relative; overflow: hidden;">
      <img src="assets/Index_asset/MatBang/SGFR_Tien_ich_Ven_ho.webp" alt="Sơ đồ tiện ích ven hồ Saigon Farm Resort" style="width: 100%; height: auto; display: block;">
      <span style="position: absolute; bottom: 12px; right: 12px; background: rgba(0,0,0,0.75); color: #fff; padding: 6px 12px; border-radius: 16px; font-size: 0.78rem; font-weight: 600; backdrop-filter: blur(4px);"><i class="fa-solid fa-expand"></i> Nhấp xem ảnh gốc</span>
    </a>'''

new_idx_card2 = '''    <div onclick="openDiagramModal('assets/Index_asset/MatBang/SGFR_Tien_ich_Ven_ho.png', 'Sơ Đồ Phân Bổ Tiện Ích Ven Hồ Sinh Thái', 'Phân Khu Ven Hồ (26 Hạng Mục)', 'Chạm vào ảnh để phóng to chi tiết 26 hạng mục ven hồ hoặc bấm [X] để đóng.')" style="display: block; position: relative; overflow: hidden; cursor: pointer;">
      <img src="assets/Index_asset/MatBang/SGFR_Tien_ich_Ven_ho.webp" alt="Sơ đồ tiện ích ven hồ Saigon Farm Resort" style="width: 100%; height: auto; display: block;">
      <span style="position: absolute; bottom: 12px; right: 12px; background: rgba(0,0,0,0.75); color: #fff; padding: 6px 12px; border-radius: 16px; font-size: 0.78rem; font-weight: 600; backdrop-filter: blur(4px);"><i class="fa-solid fa-expand"></i> Nhấp xem ảnh gốc</span>
    </div>'''

if old_idx_card2 in idx_content:
    idx_content = idx_content.replace(old_idx_card2, new_idx_card2, 1)

# Also update the bottom mini links "Phóng to"
idx_content = idx_content.replace(
    '<a href="assets/Index_asset/MatBang/SGFR_tien_ich_trung_tam.png" target="_blank" style="font-size: 0.82rem; color: #0068FF; font-weight: 600; text-decoration: none;">Phóng to <i class="fa-solid fa-arrow-up-right-from-square"></i></a>',
    '<a href="javascript:void(0)" onclick="openDiagramModal(\'assets/Index_asset/MatBang/SGFR_tien_ich_trung_tam.png\', \'Sơ Đồ Phân Bổ Tiện Ích Khu Vực Trung Tâm\', \'Phân Khu Trung Tâm (50 Hạng Mục)\')" style="font-size: 0.82rem; color: #8c6b32; font-weight: 700; text-decoration: none;">Phóng to <i class="fa-solid fa-magnifying-glass-plus"></i></a>'
)
idx_content = idx_content.replace(
    '<a href="assets/Index_asset/MatBang/SGFR_Tien_ich_Ven_ho.png" target="_blank" style="font-size: 0.82rem; color: #0068FF; font-weight: 600; text-decoration: none;">Phóng to <i class="fa-solid fa-arrow-up-right-from-square"></i></a>',
    '<a href="javascript:void(0)" onclick="openDiagramModal(\'assets/Index_asset/MatBang/SGFR_Tien_ich_Ven_ho.png\', \'Sơ Đồ Phân Bổ Tiện Ích Ven Hồ Sinh Thái\', \'Phân Khu Ven Hồ (26 Hạng Mục)\')" style="font-size: 0.82rem; color: #8c6b32; font-weight: 700; text-decoration: none;">Phóng to <i class="fa-solid fa-magnifying-glass-plus"></i></a>'
)

# Add Diagram Modal Markup and JS to index.html
if 'id="diagram-lightbox"' not in idx_content:
    idx_content = idx_content.replace('</body>', diagram_markup_and_js + '\n</body>', 1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(idx_content)

print("SUCCESS: index.html updated with in-page diagram lightbox!")
