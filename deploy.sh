#!/bin/bash
# ==============================================================================
# SCRIPT DEPLOY SIÊU TỐC: TỰ ĐỘNG GIT PUSH & CLOUDFLARE PAGES DIRECT DEPLOY
# ==============================================================================

# 1. Đặt tên project Cloudflare Pages của website
PROJECT_NAME="saigonfarmresort"
CUSTOM_DOMAIN="saigonfarmresort.com"
export CLOUDFLARE_ACCOUNT_ID="3f8e9f507373cd9d315b6efbb8bfb026"

# 2. Lấy thông điệp commit (mặc định nếu không truyền tham số)
COMMIT_MSG="${1:-Auto update and deploy website}"

# Tự động đồng bộ data/posts.json sang js/posts-data.js nếu người dùng vừa sửa bài viết
if [ -f "data/posts.json" ]; then
    python3 -c '
import json
with open("data/posts.json") as f:
    posts = json.load(f)
with open("js/posts-data.js", "w") as f:
    data = json.dumps(posts, ensure_ascii=False, indent=2)
    f.write("const POSTS = " + data + ";\nwindow.SAIGON_POSTS = POSTS;\n")
' 2>/dev/null
fi

echo "🚀 [1/3] Kiểm tra và gom tất cả thay đổi (Staging)..."
git add -A

# Kiểm tra nếu có thay đổi mới commit
if git diff-index --quiet HEAD --; then
    echo "ℹ️  Không có thay đổi mới trong mã nguồn Git."
else
    echo "📦 [2/3] Đang Commit & Push lên GitHub origin main..."
    git commit -m "$COMMIT_MSG"
    git push origin main
fi

echo "📦 [3/4] Đóng gói website chuẩn hóa (dist-site)..."
python3 -c "
import os, shutil

dist = 'dist-site'
if os.path.exists(dist):
    shutil.rmtree(dist)
os.makedirs(dist, exist_ok=True)

# Copy root html & meta files
for f in os.listdir('.'):
    if f.endswith('.html') or f in ['_redirects', '_headers', 'robots.txt', 'sitemap.xml', 'favicon.ico', 'app_icon_1024.png', 'app_icon_1024.jpg']:
        shutil.copy2(f, os.path.join(dist, f))

# Copy essential static web folders
folders = [
    'assets', 'css', 'js', 'data', 'bai-viet', 'listing', 'giohang', 'short',
    'introduction', 'gioi-thieu', 'investment', 'investor', 'dien-an',
    'dien-san', 'biet-phu-dien-trang', 'story', 'article', 'animation'
]
for folder in folders:
    if os.path.exists(folder):
        shutil.copytree(folder, os.path.join(dist, folder))
"

echo "⛅ [4/4] Đang bắn trực tiếp lên Cloudflare Pages ($PROJECT_NAME)..."
# wrangler sẽ tự so khớp mã băm và chỉ upload những file có thay đổi
npx -y wrangler pages deploy dist-site --project-name="$PROJECT_NAME" --branch=main --commit-dirty=true

# Đồng bộ luôn trang thư mời (invitation.saigonfarmresort.com)
if [ -f "deploy-invitation.sh" ]; then
    echo "📬 Đồng bộ trang thư mời (invitation.saigonfarmresort.com)..."
    bash deploy-invitation.sh
fi

echo "✅ Deploy hoàn tất siêu tốc!"
if [ -n "$CUSTOM_DOMAIN" ]; then
    echo "🌐 Website trực tuyến: https://$CUSTOM_DOMAIN"
    echo "🌐 Thư mời trực tuyến: https://invitation.saigonfarmresort.com"
fi

