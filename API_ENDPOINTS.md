# Akıllı Ulaşım Sistemi - API Endpoint Tanımları

Bu belgede, projenin yapay zeka ve veri analizi süreçleriyle iletişim kurmak için kullanılacak temel API uç noktaları (endpoints) tanımlanmıştır.

## 1. Trafik Yoğunluğu Verisi Alma
* **Endpoint:** `GET /api/trafik/yogunluk`
* **Açıklama:** Belirli bir bölgedeki anlık veya geçmiş trafik yoğunluğu verilerini getirir.
* **Alınacak Veriler (Girdi):** `bolge_id` (Bölge kodu), `tarih_saat` (Zaman dilimi)
* **Dönen Veriler (Çıktı):** `yogunluk_seviyesi` (0-100 arası trafik durumu), `ortalama_hiz` (Bölgedeki araçların ortalama hızı)

## 2. Rota ve Sefer Optimizasyonu (Yapay Zeka Tahmini)
* **Endpoint:** `POST /api/optimizasyon/rota-tahmini`
* **Açıklama:** Makine öğrenmesi modelini kullanarak trafik sıkışıklığını önleyecek en verimli rotayı tahmin eder.
* **Alınacak Veriler (Girdi):** `baslangic_noktasi`, `varis_noktasi`, `arac_tipi` (otobüs, otomobil), `kalkis_saati`
* **Dönen Veriler (Çıktı):** `tahmini_sure` (Dakika cinsinden), `onerilen_rota_koordinatlari`, `yakit_tasarrufu_orani`

## 3. Toplu Taşıma Durum Bildirimi
* **Endpoint:** `GET /api/toplu-tasima/arac-durumu`
* **Açıklama:** Toplu taşıma araçlarının sefer saatlerini optimize etmek için anlık konumlarını ve duraklara varış sürelerini verir.
* **Alınacak Veriler (Girdi):** `hat_numarasi`, `durak_id`
* **Dönen Veriler (Çıktı):** `arac_konumu` (GPS verisi), `tahmini_varis_suresi`