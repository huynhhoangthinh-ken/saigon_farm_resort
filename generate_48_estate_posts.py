# -*- coding: utf-8 -*-
"""
Script to generate 48 in-depth, high-quality, editorial articles (>1000 words each)
for the 4 Saigon Farm Resort estate categories (12 articles each).
Updates data/posts.json and updates index.html sub-tabs.
"""

import json
import os
import re

# Images pool from existing asset library
ASSETS = {
    "sunrise1_ext": "assets/Index_asset/02_Phoi_Canh_3D/05.3D_TKCS-SUNRISE_1_VILLA/05.3D_TKCS-NHA_GO_4_MAU_1-_07.2025/01._NGOAI_THAT/SFR_NGOAI_THAT_06.jpg",
    "sunrise1_ext2": "assets/Index_asset/02_Phoi_Canh_3D/05.3D_TKCS-SUNRISE_1_VILLA/05.3D_TKCS-NHA_GO_4_MAU_1-_07.2025/01._NGOAI_THAT/SFR_NGOAI_THAT_(4).jpg",
    "sunrise1_mb": "assets/Index_asset/Loai_hinh_Villa/MatBang_Sunrise_1.png",
    
    "sunrise2_ext": "assets/Index_asset/02_Phoi_Canh_3D/07.3D_TKCS-NHA_GO_4_MAU_2-_02.2026/07.TKCS-NHA_GO_4-MAU_2/01.NGOAI_THAT/SFR_01.jpg",
    "sunrise2_ext2": "assets/Index_asset/02_Phoi_Canh_3D/07.3D_TKCS-NHA_GO_4_MAU_2-_02.2026/07.TKCS-NHA_GO_4-MAU_2/01.NGOAI_THAT/SFR_03.jpg",
    "sunrise2_mb": "assets/Index_asset/Loai_hinh_Villa/MatBang_Sunrise_2.png",
    
    "sunset1_ext": "assets/Index_asset/02_Phoi_Canh_3D/09.3D_TKCS-SUNSET_VILLA/SUNSET_1_VILLA/SFR_07.SAN_TRONG.jpg",
    "sunset1_ext2": "assets/Index_asset/02_Phoi_Canh_3D/09.3D_TKCS-SUNSET_VILLA/SUNSET_1_VILLA/SFR_04.PC_01.jpg",
    "sunset1_mb": "assets/Index_asset/Loai_hinh_Villa/MatBang_Sunset_1.png",
    
    "sunset2_ext": "assets/Index_asset/02_Phoi_Canh_3D/09.3D_TKCS-SUNSET_VILLA/SUNSET_2_VILLA/SFR_04.PC_01.jpg",
    "sunset2_ext2": "assets/Index_asset/02_Phoi_Canh_3D/09.3D_TKCS-SUNSET_VILLA/SUNSET_2_VILLA/SFR_04.PC_02.jpg",
    "sunset2_mb": "assets/Index_asset/Loai_hinh_Villa/MatBang_Sunset_2.png",
    
    "masterplan": "assets/Index_asset/Phoi_canh_tong_the/SFR_S01_Final_Fix.jpg",
    "masterplan_alt": "assets/Index_asset/Phoi_canh_tong_the/SFR_NEW_S02.jpg",
    "horse": "assets/Index_asset/Tien_ich_minh_hoa/viet_ma_trang.png",
    "lotus": "assets/Index_asset/Tien_ich_minh_hoa/Bo_sen.png",
    "kayak": "assets/Index_asset/Tien_ich_minh_hoa/ben_thuyen_kayak.png",
    "clubhouse": "assets/Index_asset/Tien_ich_minh_hoa/Clubhouse_ven_ho.png",
    "giaotri": "assets/Index_asset/Tien_ich_minh_hoa/Giao_tri_viet.png",
    "mds": "assets/Index_asset/Phoi_canh_tong_the/mds_living_01.jpg",
    "farm": "assets/Index_asset/Tien_ich_minh_hoa/Nong_trai_huu_co.png",
    "quymo": "assets/Index_asset/MatBang/TongQuan_QuyMo.png",
    "lienket": "assets/Index_asset/MatBang/SoDo_LienKet_Vung.png",
}

print("Template asset dictionary ready.")
