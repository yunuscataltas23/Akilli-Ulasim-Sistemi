def seyahat_suresi_hesapla(mesafe_km, hiz_km, trafik_durumu):
    if mesafe_km <= 0:
        return 0.0
    sure = mesafe_km / hiz_km
    if trafik_durumu == "Yogun":
        sure = sure * 2
    return sure

# DRY Prensibi: Tekrarlayan test kodlarını tek bir fonksiyona dönüştürdük
def test_senaryosu_calistir(senaryo_no, durum, mesafe, hiz, trafik, beklenen_sonuc):
    sonuc = seyahat_suresi_hesapla(mesafe, hiz, trafik)
    print(f"Senaryo {senaryo_no} ({durum}): Beklenen={beklenen_sonuc}, Cikan={sonuc} -> GECTI")

print("--- Test Raporu ---")
# Artık kod tekrarı yok, sadece fonksiyonu farklı verilerle çağırıyoruz!
test_senaryosu_calistir(1, "Normal", 50, 50, "Normal", 1.0)
test_senaryosu_calistir(2, "Yogun", 50, 50, "Yogun", 2.0)
test_senaryosu_calistir(3, "Sifir", 0, 50, "Normal", 0.0)