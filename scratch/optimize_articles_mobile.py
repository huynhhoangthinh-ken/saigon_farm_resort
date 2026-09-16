import os, glob, re

# ==============================================================================
# 1. UPDATE CSS/RESPONSIVE.CSS
# ==============================================================================
with open('css/responsive.css', 'r', encoding='utf-8') as f:
    resp_css = f.read()

article_responsive_block = '''/* ================================================================
   ARTICLE PAGES & EDITORIAL DETAIL — MOBILE OPTIMIZATION
   (Tối ưu toàn diện cho bài viết, bảng so sánh & lưới ảnh trên mobile)
================================================================ */
@media (max-width: 768px) {
  .article-header { padding: 80px 0 28px !important; }
  .article-title { font-size: 1.6rem !important; line-height: 1.3 !important; }
  .article-body { font-size: 0.98rem !important; line-height: 1.75 !important; }
  
  /* Article Containers & Content Padding */
  .article-container {
    padding: 0 12px !important;
    margin: 16px auto 36px !important;
    width: 100% !important;
    box-sizing: border-box !important;
  }
  .article-content-body {
    padding: 22px 14px !important;
    border-radius: 8px !important;
  }
  .article-content {
    font-size: 0.98rem !important;
    line-height: 1.75 !important;
    max-width: 100% !important;
  }
  .article-content p,
  .article-content-body p {
    font-size: 0.96rem !important;
    line-height: 1.72 !important;
    margin-bottom: 18px !important;
  }
  .article-content h2,
  .article-content-body h2 {
    font-size: 1.32rem !important;
    line-height: 1.38 !important;
    margin: 32px 0 14px !important;
  }
  .article-content h3,
  .article-content-body h3 {
    font-size: 1.15rem !important;
    line-height: 1.4 !important;
    margin: 24px 0 10px !important;
  }

  /* Multi-column Grids inside articles stacked to 1 column on mobile */
  .article-content div[style*="grid-template-columns"],
  .article-content-body div[style*="grid-template-columns"],
  .article-container div[style*="grid-template-columns"] {
    grid-template-columns: 1fr !important;
    gap: 16px !important;
  }

  /* Responsive Tables Wrapper — Eliminates narrow vertical noodles */
  .table-scroll-wrapper,
  div[style*="overflow-x: auto"],
  .article-table-wrap,
  .table-responsive {
    width: 100% !important;
    max-width: 100% !important;
    overflow-x: auto !important;
    -webkit-overflow-scrolling: touch !important;
    margin: 22px 0 !important;
    border: 1px solid #dfc89f !important;
    border-radius: 8px !important;
    background: #ffffff !important;
    position: relative !important;
    display: block !important;
    box-shadow: 0 4px 16px rgba(194, 155, 83, 0.08) !important;
  }

  /* Mobile scroll hint banner */
  .table-scroll-wrapper::before,
  div[style*="overflow-x: auto"]::before {
    content: "← Vuốt sang ngang để xem đầy đủ bảng so sánh →";
    display: block;
    background: #faf4e8;
    color: #8c6b32;
    font-size: 0.72rem;
    font-weight: 700;
    text-align: center;
    padding: 6px 10px;
    border-bottom: 1px dashed #dfc89f;
    letter-spacing: 0.02em;
    position: sticky;
    left: 0;
    width: 100%;
    box-sizing: border-box;
    z-index: 2;
  }

  /* Force comfortable minimum width on tables so words never break awkwardly */
  .table-scroll-wrapper table,
  div[style*="overflow-x: auto"] > table,
  .article-content table,
  .article-content-body table {
    min-width: 620px !important;
    width: 100% !important;
    font-size: 0.86rem !important;
    margin: 0 !important;
    border-collapse: collapse !important;
  }

  /* Table Header cells */
  .table-scroll-wrapper th,
  div[style*="overflow-x: auto"] th,
  .article-content th,
  .article-content-body th {
    padding: 12px 14px !important;
    font-size: 0.82rem !important;
    letter-spacing: 0.03em !important;
    white-space: nowrap !important;
    text-align: left !important;
    line-height: 1.3 !important;
  }

  /* Table Body cells */
  .table-scroll-wrapper td,
  div[style*="overflow-x: auto"] td,
  .article-content td,
  .article-content-body td {
    padding: 12px 14px !important;
    font-size: 0.86rem !important;
    line-height: 1.55 !important;
    white-space: normal !important;
    word-break: normal !important;
    overflow-wrap: break-word !important;
  }

  /* Quotes and figures */
  .magazine-quote {
    font-size: 1.05rem !important;
    padding: 18px 16px !important;
    margin: 20px auto !important;
    max-width: 100% !important;
  }
  .magazine-dropcap::first-letter {
    font-size: 2.6rem !important;
    padding-right: 6px !important;
  }
  .magazine-figure { margin: 20px 0 !important; }

  /* Images inside articles */
  .article-content img,
  .article-content-body img {
    max-width: 100% !important;
    height: auto !important;
  }
}

@media (max-width: 480px) {
  .article-header { padding: 75px 0 24px !important; }
  .article-title { font-size: 1.35rem !important; line-height: 1.25 !important; }
  .article-content-body { padding: 18px 12px !important; }
  .magazine-quote { font-size: 0.92rem !important; padding: 14px 12px !important; }
  .article-content-body h2 { font-size: 1.2rem !important; }

  .table-scroll-wrapper table,
  div[style*="overflow-x: auto"] > table,
  .article-content table,
  .article-content-body table {
    min-width: 580px !important;
    font-size: 0.84rem !important;
  }
}
'''

# Replace old ARTICLE PAGE block in responsive.css
old_article_block = re.search(r'/\* =+\s*ARTICLE PAGE — article\.html specific.*?(?=\n/\* =+\s*TOUCH DEVICE)', resp_css, re.DOTALL)
if old_article_block:
    resp_css = resp_css[:old_article_block.start()] + article_responsive_block + '\n' + resp_css[old_article_block.end():]
else:
    resp_css += '\n' + article_responsive_block

with open('css/responsive.css', 'w', encoding='utf-8') as f:
    f.write(resp_css)
print("Updated css/responsive.css successfully!")


# ==============================================================================
# 2. UPDATE BAI-VIET/*.HTML
# ==============================================================================
updated_articles = 0
for filepath in glob.glob('bai-viet/*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add class="table-scroll-wrapper" to <div style="overflow-x: auto...
    # E.g. <div style="overflow-x: auto; margin: 26px 0;">
    new_content = re.sub(
        r'<div\s+(style=[\"\'][^\"\']*overflow-x:\s*auto[^\"\']*[\"\'])',
        r'<div class="table-scroll-wrapper" \1',
        content
    )
    # Avoid duplicate class="table-scroll-wrapper" class="table-scroll-wrapper"
    new_content = new_content.replace('class="table-scroll-wrapper" class="table-scroll-wrapper"', 'class="table-scroll-wrapper"')

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        updated_articles += 1

print(f"Updated {updated_articles} articles in bai-viet/ with table-scroll-wrapper!")


# ==============================================================================
# 3. UPDATE JS/POSTS-DATA.JS
# ==============================================================================
with open('js/posts-data.js', 'r', encoding='utf-8') as f:
    posts_data = f.read()

new_posts_data = re.sub(
    r'<div\s+(style=[\"\'][^\"\']*overflow-x:\s*auto[^\"\']*[\"\'])',
    r'<div class="table-scroll-wrapper" \1',
    posts_data
)
new_posts_data = new_posts_data.replace('class="table-scroll-wrapper" class="table-scroll-wrapper"', 'class="table-scroll-wrapper"')

if new_posts_data != posts_data:
    with open('js/posts-data.js', 'w', encoding='utf-8') as f:
        f.write(new_posts_data)
    print("Updated js/posts-data.js with table-scroll-wrapper!")


# ==============================================================================
# 4. UPDATE ARTICLE.HTML
# ==============================================================================
with open('article.html', 'r', encoding='utf-8') as f:
    art_html = f.read()

# Make sure article.html has the table-scroll-wrapper style in its head as well
if '.table-scroll-wrapper' not in art_html:
    art_html = art_html.replace('</style>', '''
    .table-scroll-wrapper {
      width: 100%;
      overflow-x: auto;
      -webkit-overflow-scrolling: touch;
      margin: 24px 0;
      border: 1px solid #dfc89f;
      border-radius: 8px;
      background: #ffffff;
      box-shadow: 0 4px 16px rgba(194, 155, 83, 0.08);
    }
  </style>''', 1)
    with open('article.html', 'w', encoding='utf-8') as f:
        f.write(art_html)
    print("Updated article.html!")

print("ALL MOBILE ARTICLE OPTIMIZATIONS COMPLETED!")
