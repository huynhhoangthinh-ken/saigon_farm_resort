#!/bin/bash
# ==============================================================================
# SCRIPT DEPLOY TRANG THƯ MỜI RIÊNG BIỆT (invitation.saigonfarmresort.com)
# ==============================================================================

PROJECT_NAME="invitation-saigonfarmresort"
CUSTOM_DOMAIN="invitation.saigonfarmresort.com"
DIST="dist-invitation"

echo "📦 [1/3] Đóng gói trang thư mời độc lập vào $DIST..."
python3 -c "
import os, shutil

dist = '$DIST'
if os.path.exists(dist):
    shutil.rmtree(dist)
os.makedirs(dist, exist_ok=True)

# 1. Biến thu-moi.html thành index.html của trang chủ subdomain và copy các trang liên quan
shutil.copy('thu-moi.html', os.path.join(dist, 'index.html'))
shutil.copy('thu-moi.html', os.path.join(dist, 'thu-moi.html'))
for f in ['gioi-thieu.html', 'dien-an.html', 'dien-san.html', 'biet-phu-dien-trang.html']:
    if os.path.exists(f):
        shutil.copy(f, os.path.join(dist, f))
for d in ['dien-an', 'dien-san', 'biet-phu-dien-trang']:
    if os.path.exists(d):
        shutil.copytree(d, os.path.join(dist, d))

# 2. Copy toàn bộ assets, css, js
for folder in ['assets', 'css', 'js']:
    if os.path.exists(folder):
        shutil.copytree(folder, os.path.join(dist, folder))

# 3. Tạo file CNAME cho subdomain
with open(os.path.join(dist, 'CNAME'), 'w') as f:
    f.write('$CUSTOM_DOMAIN\n')

print('  -> Đóng gói thành công!')
"

echo "⛅ [2/3] Bắn trực tiếp lên Cloudflare Pages ($PROJECT_NAME)..."
npx -y wrangler pages deploy "$DIST" --project-name="$PROJECT_NAME" --commit-dirty=true

echo "✅ [3/3] Triển khai thành công!"
echo "🌐 URL Pages: https://$PROJECT_NAME.pages.dev"
if [ -n "$CUSTOM_DOMAIN" ]; then
    echo "🌐 Domain chính thức: https://$CUSTOM_DOMAIN"
fi
