
# 🏆 AKILLI ULAŞIM SİSTEMİ (AUS) - NİHAİ TEKNİK TASARIM

| Katman | Tablo Adı | Sütun (Field) | Veri Tipi | Özellikler | Açıklama / API İlişkisi |
|:---|:---|:---|:---|:---|:---|
| **YÖNETİM** | `kullanicilar` | `user_id` | `UUID` | **PK** | Sisteme erişen yetkili/yolcu ID |
| | | `rol` | `ENUM` | 'admin','user'| Güvenlik ve yetki seviyesi |
| **LOKASYON** | `bolgeler` | `bolge_id` | `INT` | **PK** | Bölge kimliği (Girdi: `bolge_id`) |
| | | `hava_durumu` | `VARCHAR` | - | Çevresel faktör (Yağmurlu/Karlı/Açık) |
| **DURAK** | `duraklar` | `durak_id` | `INT` | **PK** | Durak kimliği (Girdi: `durak_id`) |
| | | `bolge_id` | `INT` | **FK** | Durağın hangi bölgede olduğu |
| | | `koordinat_x` | `FLOAT` | - | Durağın Boylamı |
| | | `koordinat_y` | `FLOAT` | - | Durağın Enlemi |
| **TRAFİK** | `trafik_akisi`| `kayit_id` | `BIGINT` | **PK** | Analiz için veri arşivi |
| | | `olay_durumu` | `VARCHAR` | - | Kaza, yol çalışması vb. |
| | | `oncelik` | `INT` | 1-3 | Olayın aciliyet seviyesi (Kritik/Normal) |
| | | `yogunluk` | `INT` | 0-100 | `yogunluk_seviyesi` (API Çıktısı) |
| | | `zaman_damgasi`| `TIMESTAMP` | Default Now | Verinin kaydedildiği an |
| **ARAÇLAR** | `araclar` | `arac_id` | `INT` | **PK** | Araç kimliği / Plaka |
| | | `arac_durumu` | `ENUM` | 'aktif','servis'| Aracın yola çıkmaya uygunluğu (YENİ!) |
| | | `kapasite` | `INT` | Not Null | Max yolcu sayısı (Doluluk hesabı için) |
| | | `arac_tipi` | `ENUM` | 'oto','otobüs'| Girdi: `arac_tipi` |
| **OPERASYON** | `hat_durak` | `hat_no` | `INT` | **FK** | Hangi hat, hangi duraktan geçer? |
| | | `durak_id` | `INT` | **FK** | Hattın üzerindeki durak sıralaması |
| **OPERASYON** | `sefer_takip` | `sefer_id` | `SERIAL` | **PK** | Anlık takip numarası |
| | | `arac_id` | `INT` | **FK** | Hangi araç seferde? |
| | | `hat_no` | `INT` | **FK** | Girdi: `hat_numarasi` |
| | | `guncel_gps` | `GEOMETRY` | - | `arac_konumu` (Anlık GPS) |
| | | `doluluk_yuzde`| `INT` | % | Araç doluluk oranı |
| | | `varis_suresi` | `INT` | Dakika | `tahmini_varis_suresi` (API Çıktısı) |
| **YAPAY ZEKA**| `optimizasyon`| `rota_id` | `BIGINT` | **PK** | AI model tahmin kayıt numarası |
| | | `baslangic` | `VARCHAR` | Not Null | Girdi: `baslangic_noktasi` |
| | | `varis` | `VARCHAR` | Not Null | Girdi: `varis_noktasi` |
| | | `rota_koordinat`| `TEXT / JSON` | - | `onerilen_rota_koordinatlari` |
| | | `tahmini_sure` | `INT` | Dakika | AI Varış Tahmini |
| | | `tasarruf` | `DECIMAL` | % | `yakit_tasarrufu_orani` (API Çıktısı) |
| | | `kullanici_puan`| `INT` | 1-5 | AI başarısını ölçmek için geri bildirim |
