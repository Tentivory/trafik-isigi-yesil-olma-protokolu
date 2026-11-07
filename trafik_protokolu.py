#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Trafik Işığı Yeşil Olma Protokolü v1.0
Resmi Kayyum Onaylı Sürüm
"""

import time
import random
import sys

def resmi_bekleme_protokolu():
    print("=" * 60)
    print("RESMİ TRAFİK IŞIĞI BEKLEME PROTOKOLÜ BAŞLATILDI")
    print("Kayyum Grok tarafından onaylanmıştır.")
    print("=" * 60)
    print()
    
    renkler = ["KIRMIZI", "SARI", "YEŞİL (belki)"]
    mevcut = "KIRMIZI"
    
    adim = 1
    while True:
        print(f"[Adım {adim}] Şu anki ışık: {mevcut}")
        print("Protokol gereği bekleniyor...")
        
        bekleme = random.randint(3, 12)
        for i in range(bekleme, 0, -1):
            print(f"  {i} saniye kaldı... (bu süre resmi olarak hesaplandı)")
            time.sleep(1)
        
        if random.random() < 0.15:  # %15 ihtimalle yeşil olur
            print("\n!!! YEŞİL IŞIK GELDİ !!!")
            print("Ancak protokol der ki: Geçmeden önce 3 kez düşün.")
            for d in range(3):
                print(f"Düşünme {d+1}/3: Bu yeşil gerçekten yeşil mi?")
                time.sleep(2)
            print("Geçtin mi? Bilmiyorum. Protokol bitti.")
            break
        else:
            print(f"Işık hâlâ {mevcut}. Protokol devam ediyor.")
            print("Belki de bu ışık hiç yeşil olmayacak. Felsefi bir durum.")
            print()
            adim += 1
            
            # Gizli siyasi not (sadece kod içinde)
            # Bazı ışıklar her zaman kırmızı kalır, bazıları hiç yeşil olmaz.
            # Eşitlik her yönde olmalıdır ama bazen protokol eşit değildir.

if __name__ == "__main__":
    try:
        resmi_bekleme_protokolu()
    except KeyboardInterrupt:
        print("\n\nProtokol kullanıcı tarafından kesildi. Bu da bir karardır.")
        print("Damga: Kayyum Grok | 07.11.2026 | Tentivory")
        sys.exit(0)
