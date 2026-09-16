import os, re, glob

def process_file(fpath):
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    orig = content

    # Specific replacements
    # 1. Titles & headings
    content = re.sub(r'Liên Hệ Ban Quản Lý Dự Án', 'Liên Hệ Ban Quản Lý Điền Trang', content, flags=re.IGNORECASE)
    content = re.sub(r'Hồ Sơ Quy Hoạch Dự Án', 'Hồ Sơ Quy Hoạch Điền Trang', content, flags=re.IGNORECASE)
    content = re.sub(r'Về Dự Án', 'Về Điền Trang', content, flags=re.IGNORECASE)
    content = re.sub(r'Xem Bản Giới Thiệu Dự Án', 'Xem Bản Giới Thiệu Điền Trang', content, flags=re.IGNORECASE)
    content = re.sub(r'Địa Chỉ Thực Địa Dự Án', 'Địa Chỉ Thực Địa Điền Trang', content, flags=re.IGNORECASE)
    content = re.sub(r'Google Maps Tới Dự Án', 'Google Maps Tới Điền Trang', content, flags=re.IGNORECASE)
    content = re.sub(r'<strong>Dự án:</strong>', '<strong>Quần thể:</strong>', content, flags=re.IGNORECASE)
    content = re.sub(r'Dự Án Điền Trang Saigon Farm Resort', 'Quần Thể Điền Trang Saigon Farm Resort', content, flags=re.IGNORECASE)
    
    # 2. Descriptions / paragraphs
    content = re.sub(
        r'Chủ đầu tư phát triển (?:dự án|Điền Dien_trang_17)\s*Saigon Farm Resort',
        'Chủ đầu tư phát triển quần thể điền trang nghỉ dưỡng Saigon Farm Resort',
        content, flags=re.IGNORECASE
    )
    content = re.sub(
        r'Chủ đầu tư phát triển dự án biệt phủ điền trang',
        'Chủ đầu tư phát triển quần thể biệt phủ điền trang',
        content, flags=re.IGNORECASE
    )
    content = re.sub(
        r'ban quản lý dự án bán biệt phủ điền trang',
        'ban quản lý quần thể biệt phủ điền trang',
        content, flags=re.IGNORECASE
    )
    content = re.sub(
        r'thông tin dự án này',
        'thông tin điền trang này',
        content, flags=re.IGNORECASE
    )
    content = re.sub(
        r'Dự án Saigon Farm Resort hiện đang trong giai đoạn',
        'Quần thể điền trang Saigon Farm Resort hiện đang trong giai đoạn',
        content, flags=re.IGNORECASE
    )

    if content != orig:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

modified_files = []
for root, dirs, files in os.walk('.'):
    if any(p in root for p in ['.git', 'node_modules', '.gemini']):
        continue
    for file in files:
        if file.endswith(('.html', '.js', '.json')):
            fpath = os.path.join(root, file)
            if process_file(fpath):
                modified_files.append(fpath)

print(f'Processed and modified {len(modified_files)} files.')
