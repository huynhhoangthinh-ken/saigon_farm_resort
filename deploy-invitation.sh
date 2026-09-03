#!/bin/bash
# ==============================================================================
# SCRIPT DEPLOY TRANG THƯ MỜI RIÊNG BIỆT (invitation.saigonfarmresort.com)
# ==============================================================================

PROJECT_NAME="invitation-saigonfarmresort"
DIST="dist-invitation"

echo "📦 [1/3] Đóng gói trang thư mời độc lập vào $DIST..."
python3 -c "
import os, shutil

dist = '$DIST'
if os.path.exists(dist):
    shutil.rmtree(dist)
os.makedirs(dist, exist_ok=True)

# 1. Biến thu-moi.html thành index.html của trang chủ subdomain
shutil.copy('thu-moi.html', os.path.join(dist, 'index.html'))
shutil.copy('thu-moi.html', os.path.join(dist, 'thu-moi.html'))

# 2. Copy toàn bộ assets, css, js
for folder in ['assets', 'css', 'js']:
    if os.path.exists(folder):
        shutil.copytree(folder, os.path.join(dist, folder))

print('  -> Đóng gói thành công!')
"

echo "⛅ [2/3] Bắn trực tiếp lên Cloudflare Pages ($PROJECT_NAME)..."
npx -y wrangler pages deploy "$DIST" --project-name="$PROJECT_NAME" --commit-dirty=true

echo "✅ [3/3] Triển khai thành công!"
echo "🌐 URL Pages: https://$PROJECT_NAME.pages.dev"
