# Kafka ve Spark Entegrasyonu için Mimari Tasarımı

## 1. Amaç

Bu dokümanda Akıllı Ulaşım Sistemi projesinde gerçek zamanlı trafik verilerinin Apache Kafka ve Apache Spark kullanılarak nasıl işleneceği açıklanmıştır. Amaç; sensörlerden, GPS cihazlarından, mobil uygulamalardan ve trafik yoğunluğu kaynaklarından gelen verileri anlık olarak toplamak, işlemek ve rota optimizasyon modülüne aktarılabilir hale getirmektir.

Kafka veri akışının yönetilmesini sağlarken, Spark Streaming gelen verilerin gerçek zamanlı analiz edilmesi ve anlamlı hale getirilmesi için kullanılacaktır.

---

## 2. Genel Mimari Yapı

Sistem üç ana katmandan oluşur:

1. **Veri Toplama Katmanı**

   * Trafik sensörleri
   * GPS verileri
   * Mobil uygulama konum verileri
   * Yol durumu ve kaza bilgileri
   * Toplu taşıma araçlarından gelen anlık veriler

2. **Veri Akış Katmanı**

   * Apache Kafka
   * Kafka topic yapısı
   * Producer ve consumer bileşenleri

3. **Veri İşleme Katmanı**

   * Apache Spark Streaming
   * Trafik yoğunluğu analizi
   * Veri temizleme
   * Ortalama hız ve gecikme hesaplama
   * Rota optimizasyon modülüne veri gönderme

---

## 3. Kafka Entegrasyon Mimarisi

Kafka, farklı veri kaynaklarından gelen trafik verilerini düzenli ve ölçeklenebilir şekilde sisteme aktarmak için kullanılacaktır.

### Kafka Producer Bileşenleri

| Producer                  | Görevi                                                                                 |
| ------------------------- | -------------------------------------------------------------------------------------- |
| `traffic-sensor-producer` | Trafik sensörlerinden gelen yoğunluk verilerini Kafka'ya gönderir.                     |
| `gps-producer`            | Toplu taşıma araçlarından gelen GPS konum verilerini gönderir.                         |
| `mobile-app-producer`     | Kullanıcıların mobil uygulama üzerinden oluşturduğu rota ve konum verilerini gönderir. |
| `incident-producer`       | Kaza, yol çalışması ve kapalı yol gibi olay verilerini gönderir.                       |
| `weather-producer`        | Hava durumu bilgisini sisteme aktarır.                                                 |

---

## 4. Kafka Topic Yapısı

Sistemde verilerin düzenli işlenebilmesi için farklı veri türlerine göre topic yapısı oluşturulacaktır.

| Topic Adı                  | Açıklama                                                 |
| -------------------------- | -------------------------------------------------------- |
| `raw-traffic-data`         | Sensörlerden gelen ham trafik yoğunluğu verileri         |
| `raw-gps-data`             | Araçlardan gelen ham GPS konum verileri                  |
| `raw-mobile-data`          | Mobil uygulamadan gelen kullanıcı verileri               |
| `raw-incident-data`        | Kaza, yol çalışması ve kapanan yol bilgileri             |
| `raw-weather-data`         | Hava durumu verileri                                     |
| `processed-traffic-data`   | Spark tarafından temizlenmiş ve işlenmiş trafik verileri |
| `route-optimization-input` | Rota optimizasyon algoritmasına gönderilecek hazır veri  |
| `dead-letter-topic`        | Hatalı, eksik veya işlenemeyen veriler                   |

Bu yapı sayesinde her veri türü kendi topic'i üzerinden yönetilir. Böylece sistem daha düzenli, okunabilir ve ölçeklenebilir hale gelir.

---

## 5. Spark Streaming Kullanımı

Spark Streaming, Kafka topic'lerinden gelen verileri gerçek zamanlı olarak okuyacak ve işleyecektir. Spark'ın temel görevi ham verileri analiz edilebilir hale getirmek ve rota optimizasyon modülüne uygun formatta veri üretmektir.

### Spark Streaming'in Yapacağı İşlemler

* Kafka'dan ham trafik verilerini okuma
* Eksik veya hatalı verileri filtreleme
* Trafik yoğunluğu ortalaması hesaplama
* Yol bazlı gecikme süresi çıkarma
* Araç hızlarını analiz etme
* Kapalı yol veya kaza durumlarını işaretleme
* İşlenmiş verileri yeni Kafka topic'lerine gönderme

---

## 6. Veri Akışı

Sistemde veri akışı aşağıdaki şekilde ilerleyecektir:

```text
Trafik Sensörleri / GPS / Mobil Uygulama / Olay Verileri
                    |
                    v
              Kafka Producers
                    |
                    v
              Kafka Raw Topics
                    |
                    v
            Spark Streaming
                    |
                    v
        Veri Temizleme ve Analiz
                    |
                    v
        Processed Kafka Topics
                    |
                    v
        Rota Optimizasyon Modülü
                    |
                    v
           Kullanıcı Arayüzü / API
```

---

## 7. Veri İşleme Adımları

### 7.1 Ham Verinin Alınması

Kafka producer bileşenleri farklı kaynaklardan gelen verileri Kafka topic'lerine gönderir. Bu veriler başlangıçta ham halde bulunur.

Örnek veri alanları:

* Yol ID
* Araç ID
* Konum
* Ortalama hız
* Trafik yoğunluğu
* Zaman bilgisi
* Kaza veya yol çalışması durumu

### 7.2 Verinin Temizlenmesi

Spark Streaming gelen verileri kontrol eder. Eksik, bozuk veya anlamsız veriler ayıklanır.

Örnek kontroller:

* Konum bilgisi boş mu?
* Hız değeri negatif mi?
* Zaman bilgisi geçerli mi?
* Yol ID sistemde kayıtlı mı?

Hatalı kayıtlar silinmek yerine `dead-letter-topic` içine gönderilir. Böylece daha sonra hata analizi yapılabilir.

### 7.3 Verinin Zenginleştirilmesi

Temizlenen veriler hava durumu, yol durumu ve geçmiş trafik bilgileriyle birleştirilebilir. Bu sayede rota optimizasyon algoritması daha doğru karar verebilir.

### 7.4 Rota Optimizasyonuna Aktarma

İşlenen veriler `route-optimization-input` topic'ine gönderilir. Rota optimizasyon modülü bu topic'i dinleyerek güncel trafik durumuna göre rota hesaplaması yapar.

---

## 8. Performans Optimizasyonları

Sistemin yüksek veri yoğunluğunda daha verimli çalışması için bazı optimizasyonlar uygulanacaktır.

### 8.1 Kafka Partition Kullanımı

Kafka topic'leri birden fazla partition ile oluşturulacaktır. Böylece veriler paralel olarak işlenebilir.

Örnek:

```text
raw-traffic-data
├── partition-0
├── partition-1
├── partition-2
└── partition-3
```

Bu yapı sayesinde aynı anda birden fazla consumer veri okuyabilir.

### 8.2 Consumer Group Yapısı

Kafka consumer group kullanılarak aynı topic'teki veriler birden fazla consumer tarafından paralel şekilde işlenebilir. Bu durum sistemin hızını artırır.

### 8.3 Spark Partitioning

Spark tarafında veriler partition'lara ayrılarak dağıtık şekilde işlenecektir. Böylece büyük trafik verileri tek bir işlemciye yüklenmeden paralel olarak analiz edilir.

### 8.4 Veri Filtreleme

Gereksiz veya eski veriler erken aşamada filtrelenerek sistem yükü azaltılır. Örneğin çok eski GPS kayıtları rota optimizasyonuna dahil edilmez.

### 8.5 Cache Kullanımı

Sık kullanılan yol yoğunluğu verileri ve rota hesaplama sonuçları cache yapısıyla saklanabilir. Böylece aynı veriler tekrar tekrar hesaplanmaz.

---

## 9. Hata Yönetimi

Gerçek zamanlı sistemlerde veri kaybı ve hatalı kayıtlar önemli bir sorundur. Bu nedenle sistemde hata yönetimi için ayrı bir yapı kurulacaktır.

### Hata Yönetimi Adımları

1. Spark gelen veriyi kontrol eder.
2. Hatalı veri tespit edilirse işleme alınmaz.
3. Hatalı veri `dead-letter-topic` içine gönderilir.
4. Hata kayıtları loglanır.
5. Sistem yöneticisi hatalı verileri daha sonra inceleyebilir.

---

## 10. Mimari Tasarım Özeti

| Bileşen                  | Görevi                                                  |
| ------------------------ | ------------------------------------------------------- |
| Kafka Producer           | Veriyi kaynaklardan Kafka'ya gönderir.                  |
| Kafka Topic              | Verilerin türlerine göre saklandığı akış kanalıdır.     |
| Kafka Consumer           | Topic'lerdeki verileri okur.                            |
| Spark Streaming          | Gerçek zamanlı veri işleme ve analiz yapar.             |
| Rota Optimizasyon Modülü | İşlenmiş trafik verisine göre en uygun rotayı hesaplar. |
| API / Arayüz             | Sonuçları kullanıcıya gösterir.                         |

---

## 11. Sonuç

Bu mimari tasarım ile Akıllı Ulaşım Sistemi'nin gerçek zamanlı trafik verilerini daha düzenli, hızlı ve ölçeklenebilir şekilde işlemesi hedeflenmiştir. Kafka veri akışını yönetirken, Spark Streaming verileri analiz ederek rota optimizasyon algoritmasına hazır hale getirir.

Kafka topic yapısı, Spark partitioning, consumer group kullanımı ve hata yönetimi sayesinde sistem yüksek veri yoğunluğunda daha kararlı çalışabilir. Bu yapı projenin gerçek zamanlı trafik analizi ve dinamik rota optimizasyonu hedefleriyle uyumludur.
