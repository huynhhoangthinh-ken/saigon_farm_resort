import re

with open("gioithieu.html", "r", encoding="utf-8") as f:
    content = f.read()

print("Original length:", len(content))

# Check for "dự án" in gioithieu.html
matches = re.findall(r'dự án', content, re.IGNORECASE)
print("dự án matches:", len(matches))

