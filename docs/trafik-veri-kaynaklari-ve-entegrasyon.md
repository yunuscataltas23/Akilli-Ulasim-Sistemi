# 🌐 Trafik Veri Kaynakları Araştırması ve Entegrasyon Planı

## 📌 Görevin Amacı

Bu çalışmanın amacı, Akıllı Ulaşım Sistemi içerisinde kullanılacak trafik veri kaynaklarını detaylı şekilde analiz etmek, veri akış mimarisini planlamak ve farklı veri kaynaklarından gelen bilgilerin tek bir sistem altında nasıl entegre edileceğini belirlemektir.

Sistem; gerçek zamanlı trafik analizi, rota optimizasyonu ve toplu taşıma yönetimi gerçekleştireceği için veri kalitesi, veri güncelliği ve düşük gecikmeli veri işleme kritik öneme sahiptir.

---

# 🚦 Trafik Veri Kaynakları Araştırması

Sistemin veri katmanı, doğruluk ve kapsama alanını artırmak amacıyla birden fazla veri kaynağından beslenmektedir.

# 1. Sabit Altyapı Kaynakları

## 1.1 Manyetik Döngü Dedektörleri

### Açıklama

Yol yüzeyine yerleştirilen sensörler sayesinde araç yoğunluğu ölçülmektedir.

### Sağlanan Veriler

* Araç sayısı
* Ortalama hız
* Yol doluluk oranı
* Şerit yoğunluğu

### Veri Formatı

```json id="y2gt1y"
{
  "sensor_id": "S101",
  "vehicle_count": 54,
  "average_speed": 42,
  "occupancy_rate": 78
}
```

### Avantajları

* Yüksek doğruluk oranı
* Gerçek zamanlı veri üretimi
* Düşük gecikme süresi

### Dezavantajları

* Donanım maliyeti yüksektir
* Fiziksel bakım gerektirir

---

## 1.2 Trafik Kameraları

### Açıklama

Kamera görüntüleri OpenCV ve YOLO tabanlı görüntü işleme algoritmaları ile analiz edilmektedir.

### Sağlanan Veriler

* Araç yoğunluğu
* Ortalama hız
* Kaza tespiti
* Şerit ihlali analizi

### Kullanılan Teknolojiler

* OpenCV
* YOLOv8
* CNN tabanlı görüntü işleme

### Veri Formatı

```json id="d5y58m"
{
  "camera_id": "CAM_12",
  "traffic_density": 85,
  "detected_accident": true
}
```

### Avantajları

* Görsel analiz imkanı sağlar
* Kaza tespiti yapılabilir
* Çoklu şerit analizi yapılabilir

---

# 🚍 Dinamik ve Hareketli Veri Kaynakları

# 2.1 FCD (Floating Car Data)

### Açıklama

Toplu taşıma araçları ve belediye araçlarından alınan GPS verileridir.

### Sağlanan Veriler

* Anlık konum
* Hız
* Yön bilgisi
* Durak bilgisi

### Veri Formatları

* NMEA
* GeoJSON
* JSON

### Örnek Veri

```json id="hjxev6"
{
  "vehicle_id": "BUS_21",
  "latitude": 38.4237,
  "longitude": 27.1428,
  "speed": 48,
  "timestamp": "2026-05-15T14:30:00"
}
```

### Avantajları

* Gerçek zamanlı araç takibi sağlar
* Trafik yoğunluğu dinamik ölçülebilir
* Rota optimizasyonuna katkı sağlar

---

# 2.2 Mobil Uygulama SDK Verileri

### Açıklama

Mobil uygulamadan anonimleştirilmiş kullanıcı konum verileri alınmaktadır.

### Sağlanan Veriler

* Yol yoğunluğu
* Yolculuk süresi
* Bölgesel hareket yoğunluğu

### Avantajları

* Ara sokak yoğunluklarını analiz edebilir
* Gerçek kullanıcı davranışlarını yansıtır
* Trafik tahmin doğruluğunu artırır

### Güvenlik

Kullanıcı verileri KVKK kapsamında anonimleştirilmektedir.

---

# 🌦 Çevresel ve Harici Veri Kaynakları

# 3.1 Meteorolojik Veriler

### Açıklama

Hava durumu API servislerinden alınan çevresel verilerdir.

### Sağlanan Veriler

* Yağış durumu
* Kar
* Sis
* Buzlanma
* Sıcaklık

### Kullanım Amacı

* Tahmini varış süresi hesaplama
* Riskli yol analizi
* Trafik tahmini doğruluğunu artırma

### Veri Formatı

```json id="4vxep7"
{
  "temperature": 8,
  "rain": true,
  "visibility": "low"
}
```

---

# 3.2 Belediye Açık Veri Sistemleri

### Sağlanan Veriler

* Yol çalışmaları
* Trafik kazaları
* Etkinlik duyuruları
* Yol kapanmaları

### Avantajları

* Trafik tahmini doğruluğunu artırır
* Alternatif rota üretimini kolaylaştırır

---

# 🔄 Veri Entegrasyon ve İşleme Planı

# 1. Veri Toplama Sıklığı

| Veri Türü            | Güncellenme Süresi |
| -------------------- | ------------------ |
| GPS Verileri         | 5 saniye           |
| Sensör Verileri      | 5-10 saniye        |
| Kamera Verileri      | 10 saniye          |
| Hava Durumu          | 5 dakika           |
| Açık Veri Kaynakları | Olay bazlı         |

Gerçek zamanlı çalışan sistemlerde düşük gecikme hedeflenmiştir.

---

# 2. Veri Akış Mimarisi

Sistem içerisindeki veri akışı aşağıdaki yapı üzerinden çalışmaktadır:

```text id="y3t51y"
Sensörler / GPS / Kameralar
              ↓
         Apache Kafka
              ↓
     Veri İşleme Katmanı
              ↓
 Redis / PostgreSQL / InfluxDB
              ↓
 Yapay Zeka ve Analiz Modülü
              ↓
 Mobil Uygulama & Yönetim Paneli
```

Bu mimari sayesinde sistem yüksek veri hacmini düşük gecikmeyle işleyebilmektedir.

---

# 🧹 Veri Temizleme ve Normalizasyon

# 1. GPS Veri Temizleme

### Kullanılan Yöntemler

* Kalman Filter
* Gürültü azaltma
* Hatalı koordinat filtreleme

### Amaç

GPS sıçramaları ve yanlış konum verilerini temizlemek.

---

# 2. Eksik Veri Tamamlama

### Kullanılan Teknik

Lineer interpolasyon yöntemi kullanılmıştır.

### Amaç

Kısa süreli veri kayıplarında sistem sürekliliğini korumak.

---

# 3. Veri Standardizasyonu

Farklı veri kaynaklarından gelen bilgiler ortak formata dönüştürülmektedir.

### Dönüştürülen Yapılar

* km/h → standart hız formatı
* Unix Timestamp → ISO 8601
* GeoJSON → standart koordinat yapısı

---

# 🗄 Veri Depolama Stratejisi

# 1. Redis Cache Katmanı

### Kullanım Amacı

* Anlık araç konumu saklama
* Düşük gecikmeli veri erişimi
* API performansını artırma

### Ortalama Erişim Süresi

1-5 ms

---

# 2. InfluxDB

### Kullanım Amacı

Zaman serisi trafik verilerini depolamak.

### Sağladığı Avantajlar

* Trafik yoğunluk trendleri
* Geçmiş veri analizi
* Hızlı zaman bazlı sorgular

---

# 3. PostgreSQL / HDFS

### Kullanım Amacı

* Büyük veri arşivleme
* Yapay zeka modeli eğitimi
* Uzun dönem veri saklama

---

# 🔐 Güvenlik ve Güvenilirlik

# 1. Veri Güvenliği

### Kullanılan Teknolojiler

* TLS 1.3
* OAuth2
* API Key doğrulama

### Amaç

Yetkisiz erişimi önlemek ve veri güvenliğini sağlamak.

---

# 2. Failover Mekanizması

Bir veri kaynağının devre dışı kalması durumunda sistem alternatif veri kaynaklarına geçiş yapmaktadır.

### Örnek

* Sensör arızası → Mobil veri kullanımı
* Kamera kesintisi → GPS yoğunluk analizi

---

# 3. Veri Gizliliği

Kullanıcı ve sürücü bilgileri sisteme aktarılmadan önce anonimleştirilmektedir.

Bu yapı sayesinde KVKK uyumluluğu hedeflenmiştir.

---

# 📊 Beklenen Kazanımlar

Yapılan veri entegrasyon planı sayesinde sistem:

✅ Gerçek zamanlı trafik analizi yapabilecektir
✅ Trafik yoğunluğunu önceden tahmin edebilecektir
✅ Toplu taşıma rotalarını optimize edebilecektir
✅ Trafik sıkışıklığını azaltabilecektir
✅ Yakıt tüketimini düşürebilecektir
✅ Mobil uygulama kullanıcılarına anlık bilgi sağlayabilecektir
✅ Büyük şehir ölçeğinde çalışabilecek altyapıya sahip olacaktır

---

# ✅ Sonuç

Bu çalışma kapsamında Akıllı Ulaşım Sistemi için kullanılabilecek trafik veri kaynakları detaylı şekilde incelenmiş ve veri entegrasyon mimarisi planlanmıştır.

Sensörler, kameralar, GPS sistemleri, mobil uygulama verileri ve çevresel veri kaynakları birlikte değerlendirilerek yüksek doğruluklu ve gerçek zamanlı çalışan bir veri altyapısı oluşturulmuştur.

Ayrıca:

* Veri temizleme,
* Veri standardizasyonu,
* Güvenlik,
* Ölçeklenebilirlik,
* Büyük veri işleme

gibi kritik konular ele alınarak sistemin sürdürülebilir ve profesyonel bir yapıda çalışması hedeflenmiştir.
