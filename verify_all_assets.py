import json
import re
import os

with open('data/posts.json', 'r', encoding='utf-8') as f:
    posts = json.load(f)

post_ids = {p['id'] for p in posts}
print(f"Total posts in data/posts.json: {len(posts)}")

# 1. Check images in posts.json
missing_post_imgs = 0
for p in posts:
    img = p.get('image', '')
    if img and not os.path.exists(img):
        print(f"ERROR: Post {p['id']} image missing: {img}")
        missing_post_imgs += 1
    # Check inner html images
    content = p.get('content', '')
    for m in re.findall(r'src=["\']([^"\']+)["\']', content):
        if not m.startswith('http') and not os.path.exists(m):
            print(f"ERROR: Post {p['id']} inner image missing: {m}")
            missing_post_imgs += 1

if missing_post_imgs == 0:
    print("✓ All images in data/posts.json exist on disk!")

# 2. Check images in index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

missing_html_imgs = 0
for m in re.findall(r'src=["\']([^"\']+)["\']', html):
    if not m.startswith('http') and not os.path.exists(m):
        print(f"ERROR: index.html img src missing: {m}")
        missing_html_imgs += 1

for m in re.findall(r'url\([\'"]?([^\'")]+)[\'"]?\)', html):
    if not m.startswith('http') and not m.startswith('data:') and not os.path.exists(m):
        print(f"ERROR: index.html css url missing: {m}")
        missing_html_imgs += 1

if missing_html_imgs == 0:
    print("✓ All images and CSS background urls in index.html exist on disk!")

# 3. Check article links in index.html
missing_article_ids = 0
for m in re.findall(r'article\.html\?id=(\d+)', html):
    aid = int(m)
    if aid not in post_ids:
        print(f"ERROR: index.html links to non-existent post id: {aid}")
        missing_article_ids += 1

if missing_article_ids == 0:
    print("✓ All article.html?id= links in index.html point to valid existing posts!")

print("\n--- Summary of 16 Villa Articles ---")
villa_ids = [103, 104, 101, 102, 111, 112, 113, 114, 115, 116, 117, 118, 119, 130, 131, 132]
for idx, vid in enumerate(villa_ids, 1):
    p = next((x for x in posts if x['id'] == vid), None)
    if p:
        print(f"{idx:2d}. [ID {p['id']}] [{p.get('category',''):<24}] {p['title']}")
    else:
        print(f"{idx:2d}. [ID {vid}] MISSING!")
