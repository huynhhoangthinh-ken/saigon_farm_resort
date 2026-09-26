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

# 1. Trang thư mời độc lập (chỉ gồm thu-moi.html)
shutil.copy('thu-moi.html', os.path.join(dist, 'index.html'))
shutil.copy('thu-moi.html', os.path.join(dist, 'thu-moi.html'))

# 2. Copy toàn bộ assets, css, js
for folder in ['assets', 'css', 'js']:
    if os.path.exists(folder):
        shutil.copytree(folder, os.path.join(dist, folder))

# 3. Tạo file CNAME cho subdomain
with open(os.path.join(dist, 'CNAME'), 'w') as f:
    f.write('$CUSTOM_DOMAIN\n')

# 4. Chặn hoàn toàn Google Bot & công cụ tìm kiếm
with open(os.path.join(dist, 'robots.txt'), 'w') as f:
    f.write('User-agent: *\nDisallow: /\n')

with open(os.path.join(dist, '_headers'), 'w') as f:
    f.write('/*\n  X-Robots-Tag: noindex, nofollow, noarchive, nosnippet, noimageindex\n')

print('  -> Đóng gói thành công (Đã gắn bảo vệ chặn Google Search 100%)!')
"

echo "⛅ [2/3] Bắn trực tiếp lên Cloudflare Pages ($PROJECT_NAME)..."
npx -y wrangler pages deploy "$DIST" --project-name="$PROJECT_NAME" --commit-dirty=true

echo "✅ [3/3] Triển khai thành công!"
echo "🌐 URL Pages: https://$PROJECT_NAME.pages.dev"
if [ -n "$CUSTOM_DOMAIN" ]; then
    echo "🌐 Domain chính thức: https://$CUSTOM_DOMAIN"
fi
