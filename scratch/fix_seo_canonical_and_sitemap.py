import re

# 1. Update sitemap.xml to fix redirecting URLs:
# Replace /gioi-thieu.html with /gioithieu
with open("sitemap.xml", "r", encoding="utf-8") as f:
    sitemap = f.read()

sitemap = sitemap.replace(
    "<loc>https://saigonfarmresort.com/gioi-thieu.html</loc>",
    "<loc>https://saigonfarmresort.com/gioithieu</loc>"
)

with open("sitemap.xml", "w", encoding="utf-8") as f:
    f.write(sitemap)
print("Updated sitemap.xml: replaced gioi-thieu.html with /gioithieu")

# 2. Add canonical tags to files missing them
files_to_canonical = {
    "biet-phu-dien-trang.html": "https://saigonfarmresort.com/biet-phu-dien-trang.html",
    "biet-phu-dien-trang/index.html": "https://saigonfarmresort.com/biet-phu-dien-trang.html",
    "dien-san.html": "https://saigonfarmresort.com/dien-san.html",
    "dien-san/index.html": "https://saigonfarmresort.com/dien-san.html",
    "dien-an.html": "https://saigonfarmresort.com/dien-an.html",
    "dien-an/index.html": "https://saigonfarmresort.com/dien-an.html",
    "listing.html": "https://saigonfarmresort.com/listing.html",
    "listing/index.html": "https://saigonfarmresort.com/listing.html",
    "story.html": "https://saigonfarmresort.com/story.html",
    "story/index.html": "https://saigonfarmresort.com/story.html",
    "article.html": "https://saigonfarmresort.com/article.html",
    "article/index.html": "https://saigonfarmresort.com/article.html",
}

for filepath, canonical_url in files_to_canonical.items():
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        
        if '<link rel="canonical"' not in content:
            # Insert after <meta name="description" ...> or after <title>
            canonical_tag = f'\n  <link rel="canonical" href="{canonical_url}">'
            if '</title>' in content:
                content = content.replace('</title>', '</title>' + canonical_tag, 1)
            elif '<head>' in content:
                content = content.replace('<head>', '<head>' + canonical_tag, 1)
            
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Added canonical to {filepath} -> {canonical_url}")
        else:
            print(f"Already has canonical: {filepath}")
    except Exception as e:
        print(f"Error {filepath}: {e}")

