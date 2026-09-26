import os
import subprocess
import re
import json
from PIL import Image

Image.MAX_IMAGE_PIXELS = None
orig_path = "listing/TMB bán hàng 2.png"
im = Image.open(orig_path)
W, H = im.size
print(f"Original: {W} x {H}")

# Define overlapping tiles covering the resort area (X: 0.20 to 1.0, Y: 0.05 to 0.95)
# 3 columns x 3 rows grid
cols = 3
rows = 3
min_x, max_x = 0.20, 0.98
min_y, max_y = 0.05, 0.95

tile_w = (max_x - min_x) / cols
tile_h = (max_y - min_y) / rows
overlap = 0.04 # 4% overlap

tiles = []
os.makedirs("scratch/tmb_quads", exist_ok=True)

for r in range(rows):
    for c in range(cols):
        tx1 = max(min_x, min_x + c * tile_w - overlap)
        tx2 = min(max_x, min_x + (c + 1) * tile_w + overlap)
        ty1 = max(min_y, min_y + r * tile_h - overlap)
        ty2 = min(max_y, min_y + (r + 1) * tile_h + overlap)
        
        px1, py1 = int(tx1 * W), int(ty1 * H)
        px2, py2 = int(tx2 * W), int(ty2 * H)
        
        tile_img = im.crop((px1, py1, px2, py2))
        tile_name = f"scratch/tmb_quads/tile_{r}_{c}.webp"
        tile_img.save(tile_name, "WEBP", quality=85)
        tiles.append({
            "name": tile_name,
            "r": r, "c": c,
            "tx1": tx1, "ty1": ty1,
            "tx2": tx2, "ty2": ty2,
            "px_w": px2 - px1,
            "px_h": py2 - py1
        })

print(f"Created {len(tiles)} tiles.")

with open("scratch/tmb_quads/tiles_meta.json", "w") as f:
    json.dump(tiles, f, indent=2)
