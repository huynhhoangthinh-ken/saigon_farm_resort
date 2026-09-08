#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build 83 static articles in bai-viet/, sitemap.xml, and slug_map.json
"""
import os
import re
import json
import unicodedata
import html

def to_slug(title):
    s = unicodedata.normalize("NFD", title)
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    s = s.replace("đ", "d").replace("Đ", "D")
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")

def clean_title_for_seo(title, max_len=60, brand=" | Saigon Farm Resort"):
    # Target total length <= 60 chars
    brand_len = len(brand)
    available_len = max_len - brand_len
    t = title.replace("&", "và").replace("\"", "").replace("'", "").strip()
    t = re.sub(r"\s+", " ", t)
    if len(t) <= available_len:
        final_title = f"{t}{brand}"
    else:
        # Truncate nicely at last word boundary before available_len
        truncated = t[:available_len].rsplit(" ", 1)[0]
        final_title = f"{truncated}{brand}"
    assert len(final_title) <= max_len, f"Title too long ({len(final_title)}): {final_title}"
    return final_title

def clean_desc_for_seo(desc, max_len=155):
    d = desc.replace("&", "và").replace("\"", "").replace("'", "").strip()
    d = re.sub(r"\s+", " ", d)
    if len(d) > max_len:
        d = d[:max_len-3].rsplit(" ", 1)[0] + "..."
    assert len(d) <= max_len, f"Desc too long ({len(d)}): {desc}"
    return d

def generate_article_html(post, slug, related_posts):
    page_title = clean_title_for_seo(post.get("title", ""))
    page_desc = clean_desc_for_seo(post.get("excerpt", "") or post.get("title", ""))
    canonical_url = f"https://saigonfarmresort.com/bai-viet/{slug}.html"
    image_url = post.get("image", "assets/Index_asset/Phoicanh_3D_Tien_ich/Tong_the/S01_Final_Fix.jpg")
    if not image_url.startswith("http"):
        image_url = f"https://saigonfarmresort.com/{image_url.lstrip('/')}"
    
    date_published = "2026-08-29"
    
    # Related posts HTML
    related_html = ""
    for rel in related_posts:
        rel_slug = to_slug(rel.get("title", ""))
        rel_img = rel.get("image", "")
        if rel_img and not rel_img.startswith("http") and not rel_img.startswith("/"):
            rel_img = f"../{rel_img}"
        related_html += f"""
        <div class="grid-card">
          <a href="{rel_slug}.html" style="display: block; text-decoration: none; color: inherit;">
            <div class="grid-img">
              <img src="{rel_img}" alt="{html.escape(rel.get('title', ''))}" loading="lazy">
              <span class="minh-hoa-tag">* Hình ảnh minh họa</span>
            </div>
          </a>
          <div class="grid-card-info">
            <a href="{rel_slug}.html" style="text-decoration: none; color: inherit;">
              <h5 style="margin-bottom: 8px; line-height: 1.4;">{html.escape(rel.get('title', ''))}</h5>
            </a>
            <p style="font-weight: 400; font-size: 0.85rem; color: #555; display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: hidden; margin-bottom: 14px;">
              {html.escape(rel.get('excerpt', ''))}
            </p>
            <div style="display: flex; gap: 8px; margin-top: auto; flex-wrap: wrap;">
              <a href="{rel_slug}.html" class="editorial-btn" style="margin-top:0;">Đọc tiếp</a>
            </div>
          </div>
        </div>
        """

    content = post.get("content", "")
    # Fix relative image paths in content
    content = content.replace('src="assets/', 'src="../assets/')

    article_jsonld = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Article",
                "@id": f"{canonical_url}#article",
                "isPartOf": {
                    "@type": "WebPage",
                    "@id": canonical_url,
                    "url": canonical_url,
                    "name": page_title
                },
                "headline": post.get("title", ""),
                "description": page_desc,
                "image": image_url,
                "datePublished": date_published,
                "dateModified": "2026-09-08",
                "mainEntityOfPage": canonical_url,
                "author": {
                    "@type": "Organization",
                    "name": "Saigon Farm Resort",
                    "url": "https://saigonfarmresort.com"
                },
                "publisher": {
                    "@type": "Organization",
                    "name": "Saigon Farm Resort",
                    "url": "https://saigonfarmresort.com",
                    "logo": {
                        "@type": "ImageObject",
                        "url": "https://saigonfarmresort.com/assets/Index_asset/LOGO_PNG/LOGO_SGF_3_BROWN.png"
                    }
                }
            },
            {
                "@type": "BreadcrumbList",
                "@id": f"{canonical_url}#breadcrumb",
                "itemListElement": [
                    {
                        "@type": "ListItem",
                        "position": 1,
                        "name": "Trang Chủ",
                        "item": "https://saigonfarmresort.com/"
                    },
                    {
                        "@type": "ListItem",
                        "position": 2,
                        "name": "Bài Viết",
                        "item": "https://saigonfarmresort.com/#tabs-section"
                    },
                    {
                        "@type": "ListItem",
                        "position": 3,
                        "name": post.get("title", ""),
                        "item": canonical_url
                    }
                ]
            },
            {
                "@type": "Place",
                "@id": "https://saigonfarmresort.com/#place",
                "name": "Saigon Farm Resort",
                "address": {
                    "@type": "PostalAddress",
                    "streetAddress": "Xã Đất Đỏ",
                    "addressLocality": "TP. Hồ Chí Minh",
                    "addressRegion": "Hồ Chí Minh",
                    "addressCountry": "VN"
                },
                "geo": {
                    "@type": "GeoCoordinates",
                    "latitude": 10.5521,
                    "longitude": 107.3130
                }
            }
        ]
    }

    schema_str = json.dumps(article_jsonld, ensure_ascii=False, indent=2)

    return f"""<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{html.escape(page_title)}</title>
  <meta name="description" content="{html.escape(page_desc)}">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="{canonical_url}">

  <!-- Open Graph -->
  <meta property="og:type" content="article">
  <meta property="og:url" content="{canonical_url}">
  <meta property="og:title" content="{html.escape(page_title)}">
  <meta property="og:description" content="{html.escape(page_desc)}">
  <meta property="og:image" content="{image_url}">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{html.escape(page_title)}">
  <meta name="twitter:description" content="{html.escape(page_desc)}">
  <meta name="twitter:image" content="{image_url}">

  <!-- Structured Data JSON-LD -->
  <script type="application/ld+json">
{schema_str}
  </script>

  <!-- CSS Stylesheets -->
  <link href="../css/main.css?v=20260904_heritage_bg" rel="stylesheet">
  <link href="../css/components.css?v=20260904_heritage_bg" rel="stylesheet">
  <link href="../css/responsive.css?v=20260904_heritage_bg" rel="stylesheet">
  <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">

  <style>
    body {{
      background-color: #fcfaf6;
      color: #2c2c2c;
      font-family: var(--font-sans, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif);
      margin: 0;
      padding: 0;
    }}
    .article-page-header {{
      background: #fff;
      border-bottom: 1px solid #ebd9b8;
      padding: 16px 0;
      position: sticky;
      top: 0;
      z-index: 100;
    }}
    .article-header-wrap {{
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .article-logo img {{
      height: 42px;
    }}
    .article-nav-links {{
      display: flex;
      gap: 20px;
      list-style: none;
      margin: 0;
      padding: 0;
    }}
    .article-nav-links a {{
      text-decoration: none;
      color: #111;
      font-weight: 600;
      font-size: 0.92rem;
    }}
    .article-nav-links a:hover {{
      color: #c9a96e;
    }}
    .article-container {{
      max-width: 860px;
      margin: 40px auto;
      padding: 0 20px;
    }}
    .article-breadcrumb {{
      font-size: 0.85rem;
      color: #777;
      margin-bottom: 24px;
    }}
    .article-breadcrumb a {{
      color: #8c6b32;
      text-decoration: none;
    }}
    .article-content-body {{
      background: #fff;
      border: 1px solid #ebd9b8;
      border-radius: 8px;
      padding: 36px;
      box-shadow: 0 4px 16px rgba(0,0,0,0.03);
    }}
    .related-articles-section {{
      max-width: 1140px;
      margin: 50px auto;
      padding: 0 20px;
    }}
    .related-title {{
      font-family: var(--font-serif);
      font-size: 1.6rem;
      color: #111;
      margin-bottom: 24px;
      text-align: center;
    }}
    @media (max-width: 768px) {{
      .article-content-body {{
        padding: 20px;
      }}
      .article-nav-links {{
        display: none;
      }}
    }}
  </style>
</head>
<body>

  <!-- Top Navigation Header -->
  <header class="article-page-header">
    <div class="container article-header-wrap">
      <a href="../index.html" class="article-logo">
        <img src="../assets/Index_asset/LOGO_PNG/LOGO_SGF_3_BROWN.png" alt="Saigon Farm Resort Logo">
      </a>
      <ul class="article-nav-links">
        <li><a href="../index.html">Trang Chủ</a></li>
        <li><a href="../biet-phu-dien-trang.html">Biệt Phủ Điền Trang</a></li>
        <li><a href="../dien-san.html">Điền Sản (Sổ Đỏ)</a></li>
        <li><a href="../dien-an.html">Điền An</a></li>
        <li><a href="../listing.html">Bảng Giá</a></li>
        <li><a href="../story.html">Tạp Chí Story</a></li>
        <li><a href="../gioi-thieu.html">Giới Thiệu</a></li>
        <li><a href="../lien-he.html">Liên Hệ</a></li>
      </ul>
    </div>
  </header>

  <!-- Main Article Body -->
  <main class="article-container">
    <nav class="article-breadcrumb" aria-label="Breadcrumb">
      <a href="../index.html">Trang Chủ</a> &rsaquo; 
      <a href="../index.html#tabs-section">Bài Viết</a> &rsaquo; 
      <span>{html.escape(post.get("title", ""))}</span>
    </nav>

    <article class="article-content-body">
      {content}
    </article>
  </main>

  <!-- Related Articles Section -->
  <section class="related-articles-section">
    <h3 class="related-title">Bài Viết Liên Quan</h3>
    <div class="grid-listing editorial-grid" id="related-grid" style="margin-top: 0;">
      {related_html}
    </div>
  </section>

  <!-- Site Footer -->
  <footer class="site-footer">
    <div class="container">
      <div class="footer-top-grid">
        <div>
          <div class="footer-brand-title">SAIGON FARM RESORT</div>
          <div class="footer-nap-block" style="margin-top:0; padding-top:0; border-top:none;">
            <p style="font-size: 0.88rem; line-height: 1.6; max-width: 360px; color: #aaa;">
              Quần thể biệt phủ điền trang sinh thái và đất nền sổ đỏ ven hồ 100ha tại Xã Đất Đỏ, TP. Hồ Chí Minh.<br/>
              <strong style="color: #c9a96e;">Chủ đầu tư:</strong> MDS Living
            </p>
            <p style="margin-top: 12px; color: #aaa; font-size: 0.88rem; line-height: 1.5;">
              <i class="fa-solid fa-location-dot" style="color: #c9a96e; margin-right: 6px;"></i><strong>Địa chỉ:</strong> Xã Đất Đỏ, TP. Hồ Chí Minh (trước đây: huyện Đất Đỏ, tỉnh Bà Rịa – Vũng Tàu)
            </p>
          </div>
        </div>
        <div>
          <h4 class="footer-col-heading">Sản Phẩm Mở Bán</h4>
          <ul class="footer-links-list">
            <li><a href="../biet-phu-dien-trang.html">Biệt Phủ Điền Trang (1.000m² – 1.452m²)</a></li>
            <li><a href="../dien-san.html">Điền Sản (Đất Nền Sổ Đỏ Ven Hồ)</a></li>
            <li><a href="../dien-an.html">Điền An (Bungalow Vườn &amp; Chuyên Gia)</a></li>
            <li><a href="../listing.html">Bảng Giá &amp; Giỏ Hàng Chi Tiết</a></li>
          </ul>
        </div>
        <div>
          <h4 class="footer-col-heading">Về Dự Án</h4>
          <ul class="footer-links-list">
            <li><a href="../gioi-thieu.html">Hồ Sơ Quy Hoạch Dự Án</a></li>
            <li><a href="../story.html">Tạp Chí Story (98 Trang)</a></li>
            <li><a href="../lien-he.html">Liên Hệ Ban Quản Lý</a></li>
          </ul>
        </div>
        <div>
          <h4 class="footer-col-heading">Khảo Sát &amp; Đặt Chỗ</h4>
          <ul class="footer-links-list">
            <li><a href="../lien-he.html"><i class="fa-solid fa-van-shuttle" style="margin-right:6px; color:#c9a96e;"></i>Đăng Ký Xe Tham Quan Thực Địa</a></li>
            <li><a href="../gioi-thieu.html"><i class="fa-solid fa-file-lines" style="margin-right:6px; color:#c9a96e;"></i>Bản Giới Thiệu Đặc Quyền</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom-bar">
        <div>© 2026 Saigon Farm Resort • Chủ đầu tư: MDS Living. Tất cả quyền được bảo lưu.</div>
      </div>
    </div>
  </footer>

</body>
</html>
"""

def main():
    os.makedirs("bai-viet", exist_ok=True)
    with open("data/posts.json", "r", encoding="utf-8") as f:
        posts = json.load(f)

    # Filter out post 301 if present
    posts = [p for p in posts if p.get("id") != 301 and p.get("id") != "301"]
    print(f"Generating static articles for {len(posts)} posts...")

    slug_map = {}
    for p in posts:
        pid = str(p.get("id"))
        slug = to_slug(p.get("title", ""))
        slug_map[pid] = slug
        slug_map[slug] = slug

    with open("data/slug_map.json", "w", encoding="utf-8") as f:
        json.dump(slug_map, f, ensure_ascii=False, indent=2)

    generated_slugs = []
    for i, p in enumerate(posts):
        slug = to_slug(p.get("title", ""))
        # Select 3 related posts
        related = [posts[(i + offset) % len(posts)] for offset in [1, 2, 3]]
        html_code = generate_article_html(p, slug, related)
        out_path = os.path.join("bai-viet", f"{slug}.html")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html_code)
        generated_slugs.append(slug)

    print(f"Successfully generated {len(generated_slugs)} static article HTML files in bai-viet/.")

    # Generate sitemap.xml
    # Exactly 8 main canonical URLs + 83 articles = 91 URLs
    main_urls = [
        "https://saigonfarmresort.com/",
        "https://saigonfarmresort.com/biet-phu-dien-trang.html",
        "https://saigonfarmresort.com/dien-san.html",
        "https://saigonfarmresort.com/dien-an.html",
        "https://saigonfarmresort.com/gioi-thieu.html",
        "https://saigonfarmresort.com/story.html",
        "https://saigonfarmresort.com/listing.html",
        "https://saigonfarmresort.com/lien-he.html"
    ]

    sitemap_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
    ]
    for url in main_urls:
        sitemap_lines.append(f"  <url>\n    <loc>{url}</loc>\n    <changefreq>weekly</changefreq>\n    <priority>1.0</priority>\n  </url>")
    for slug in generated_slugs:
        url = f"https://saigonfarmresort.com/bai-viet/{slug}.html"
        sitemap_lines.append(f"  <url>\n    <loc>{url}</loc>\n    <changefreq>monthly</changefreq>\n    <priority>0.8</priority>\n  </url>")
    sitemap_lines.append("</urlset>\n")

    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write("\n".join(sitemap_lines))
    print(f"Generated sitemap.xml with {len(main_urls) + len(generated_slugs)} URLs.")

if __name__ == "__main__":
    main()
