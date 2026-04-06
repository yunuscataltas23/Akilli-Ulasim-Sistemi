def seyahat_suresi_hesapla(mesafe_km, hiz_km, trafik_durumu):
    if mesafe_km <= 0:
        return 0.0
    sure = mesafe_km / hiz_km
    if trafik_durumu == "Yogun":
        sure = sure * 2
    return sure

print("--- Test Raporu ---")
sonuc1 = seyahat_suresi_hesapla(50, 50, "Normal")
print("Senaryo 1 (Normal): Beklenen=1.0, Cikan=", sonuc1, "-> GECTI")

sonuc2 = seyahat_suresi_hesapla(50, 50, "Yogun")
print("Senaryo 2 (Yogun): Beklenen=2.0, Cikan=", sonuc2, "-> GECTI")

sonuc3 = seyahat_suresi_hesapla(0, 50, "Normal")
print("Senaryo 3 (Sifir): Beklenen=0.0, Cikan=", sonuc3, "-> GECTI")