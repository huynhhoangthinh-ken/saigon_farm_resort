# -*- coding: utf-8 -*-
"""
Script tự động đọc các file Word (.docx), Markdown (.md) hoặc Text (.txt)
từ thư mục `posts/` và xuất bản thành bài viết trên website Saigon Farm Resort.
"""
import os
import json
import zipfile
import xml.etree.ElementTree as ET
import datetime

POSTS_DIR = 'posts'
OUTPUT_MEDIA_DIR = 'assets/posts_media'
POSTS_JSON_PATH = 'data/posts.json'

os.makedirs(POSTS_DIR, exist_ok=True)
os.makedirs(OUTPUT_MEDIA_DIR, exist_ok=True)

CONTACT_BOX = """
<div style="background: #111; color: #fff; padding: 28px; border-radius: 8px; border-left: 4px solid #c9a96e; margin-top: 30px;">
  <h4 style="margin-bottom: 8px; font-family: var(--font-serif); font-size: 1.25rem; color: #c9a96e;">TỔNG ĐẠI LÝ TIẾP THỊ & PHÂN PHỐI: ĐẠI CHÚNG PROPERTIES</h4>
  <p style="margin-bottom: 6px; font-size: 0.95rem;">👤 <strong>Đại diện tư vấn:</strong> CEO Huỳnh Hoàng Thịnh (Ken)</p>
  <p style="margin-bottom: 14px; font-size: 0.95rem;">📞 <strong>Hotline / Zalo:</strong> <a href="https://zalo.me/0906060036" target="_blank" style="color:#0068FF; font-weight:700; text-decoration:underline;">0906060036</a></p>
  <a href="https://zalo.me/0906060036" target="_blank" style="display: inline-flex; align-items: center; gap: 8px; background: #0068FF; color: #fff; padding: 12px 24px; border-radius: 4px; font-weight: 700; text-decoration: none;">
    <i class="fa-solid fa-comment-dots"></i> Nhắn Zalo Đặt Lịch Trải Nghiệm Thực Tế
  </a>
</div>
"""

def extract_docx(docx_path):
    """Trích xuất nội dung văn bản và hình ảnh từ file Word .docx"""
    paragraphs = []
    extracted_images = []
    filename_base = os.path.splitext(os.path.basename(docx_path))[0]
    
    with zipfile.ZipFile(docx_path) as z:
        # Extract images if any
        for item in z.namelist():
            if item.startswith('word/media/'):
                img_ext = os.path.splitext(item)[1]
                img_name = f"{filename_base}_{os.path.basename(item)}"
                target_path = os.path.join(OUTPUT_MEDIA_DIR, img_name)
                with open(target_path, 'wb') as f_out:
                    f_out.write(z.read(item))
                extracted_images.append(target_path)
                
        # Extract XML document
        tree = ET.fromstring(z.read('word/document.xml'))
        ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
        
        for p in tree.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'):
            texts = [node.text for node in p.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t') if node.text]
            full_text = ''.join(texts).strip()
            if full_text:
                paragraphs.append(full_text)
                
    return paragraphs, extracted_images

def extract_text(txt_path):
    with open(txt_path, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]
    return lines, []

def process_posts():
    if not os.path.exists(POSTS_JSON_PATH):
        existing_posts = []
    else:
        with open(POSTS_JSON_PATH, 'r', encoding='utf-8') as f:
            existing_posts = json.load(f)
            
    existing_ids = set(p['id'] for p in existing_posts)
    next_id = max(existing_ids, default=600) + 1
    
    added_count = 0
    now_str = datetime.datetime.now().strftime("%d TH%m %Y").upper()
    
    for fname in sorted(os.listdir(POSTS_DIR)):
        if fname.startswith('.'):
            continue
        full_path = os.path.join(POSTS_DIR, fname)
        if not os.path.isfile(full_path):
            continue
            
        ext = os.path.splitext(fname)[1].lower()
        if ext == '.docx':
            paragraphs, images = extract_docx(full_path)
        elif ext in ['.txt', '.md']:
            paragraphs, images = extract_text(full_path)
        else:
            continue
            
        if not paragraphs:
            print(f"Bỏ qua file trống: {fname}")
            continue
            
        # Title is the first paragraph or the filename
        title = paragraphs[0] if len(paragraphs[0]) < 150 else os.path.splitext(fname)[0]
        content_paras = paragraphs[1:] if title == paragraphs[0] else paragraphs
        
        # Excerpt is the first available content paragraph
        excerpt = content_paras[0] if content_paras else title
        if len(excerpt) > 220:
            excerpt = excerpt[:217] + '...'
            
        # Choose featured image
        if images:
            feat_img = images[0]
        else:
            feat_img = 'assets/Index_asset/02_Phoi_Canh_3D/02.3D_TKCS-CANH_QUAN_VEN_HO-12.2025/SFR_1.jpg'
            
        # Build HTML content
        html_parts = []
        for para in content_paras:
            if para.startswith('# ') or para.startswith('## '):
                heading_text = para.lstrip('#').strip()
                html_parts.append(f"<h2>{heading_text}</h2>")
            elif para.startswith('### '):
                heading_text = para.lstrip('#').strip()
                html_parts.append(f"<h3>{heading_text}</h3>")
            elif para.startswith('- ') or para.startswith('* '):
                html_parts.append(f"<ul><li>{para[2:].strip()}</li></ul>")
            else:
                html_parts.append(f"<p>{para}</p>")
                
        # Embed extracted images
        if len(images) > 1:
            html_parts.append('<div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 16px; margin: 30px 0;">')
            for img in images[1:]:
                html_parts.append(f'<img src="{img}" style="border-radius: 6px; width:100%; height: 260px; object-fit: cover;">')
            html_parts.append('</div>')
            
        html_parts.append(CONTACT_BOX)
        full_content = '\n\n'.join(html_parts)
        
        # Check if already exists by title
        exists = any(p['title'] == title for p in existing_posts)
        if not exists:
            new_post = {
                "id": next_id,
                "title": title,
                "excerpt": excerpt,
                "image": feat_img,
                "date": now_str,
                "content": full_content
            }
            existing_posts.append(new_post)
            print(f"✓ Đã thêm bài viết mới [ID {next_id}]: '{title}' từ file {fname}")
            next_id += 1
            added_count += 1
        else:
            print(f"Bài viết '{title}' đã tồn tại trong posts.json.")
            
    if added_count > 0:
        with open(POSTS_JSON_PATH, 'w', encoding='utf-8') as f:
            json.dump(existing_posts, f, ensure_ascii=False, indent=2)
        print(f"\n🎉 Thành công xuất bản {added_count} bài viết mới vào website!")
    else:
        print("\nKhông có bài viết mới nào cần thêm.")

if __name__ == '__main__':
    process_posts()
