# Veri Yapısı Entegrasyonu

## 1. Amaç

Bu dokümanda Akıllı Ulaşım Sistemi projesinde kullanılan mevcut veri yapılarının, geliştirilen rota optimizasyon ve trafik analizi algoritmalarıyla nasıl uyumlu hale getirildiği açıklanmıştır.

Görevin temel amacı; veri erişimini hızlandırmak, işlem performansını artırmak ve algoritmaların daha düzenli veri yapıları üzerinde çalışmasını sağlamaktır.

---

## 2. Projede Kullanılan Temel Veri Yapıları

Projede şehir içi ulaşım ağı, duraklar, yollar, trafik yoğunluğu ve rota sonuçları farklı veri yapılarıyla temsil edilmiştir.

| Veri                    | Kullanılan Yapı        | Açıklama                                                      |
| ----------------------- | ---------------------- | ------------------------------------------------------------- |
| Durak bilgileri         | Dictionary / HashMap   | Durak ID üzerinden hızlı erişim sağlar.                       |
| Yol bağlantıları        | Graph / Adjacency List | Duraklar arasındaki bağlantıları tutar.                       |
| Trafik yoğunluğu        | Dictionary             | Yol ID veya durak bağlantısı üzerinden trafik bilgisi saklar. |
| Alternatif rotalar      | List                   | Kullanıcıya sunulacak rota seçeneklerini tutar.               |
| Öncelikli rota seçimi   | Priority Queue         | En düşük maliyetli rotayı önce işler.                         |
| Ziyaret edilen duraklar | Set                    | Aynı durağın tekrar tekrar işlenmesini önler.                 |
| Rota sonucu             | Object / Data Class    | Süre, mesafe, maliyet ve rota bilgisini düzenli tutar.        |

---

## 3. Grafik Tabanlı Ulaşım Ağı Modeli

Akıllı ulaşım sisteminde duraklar ve yollar grafik yapısı ile modellenmiştir.

* Duraklar grafik üzerinde düğüm olarak temsil edilir.
* Duraklar arasındaki yollar kenar olarak tutulur.
* Her kenarda mesafe, tahmini süre, trafik yoğunluğu ve yol durumu bilgisi bulunur.

Örnek yapı:

```text
Merkez
 ├── Üniversite
 ├── Otogar
 └── Hastane

Üniversite
 ├── Otogar
 └── Sanayi
```

Bu yapı sayesinde rota arama algoritmaları ulaşım ağı üzerinde daha kolay çalışır.

---

## 4. Dictionary Kullanımı ile Veri Erişiminin Hızlandırılması

Projede durak, yol ve trafik bilgilerine hızlı erişmek için Dictionary / HashMap yapısı kullanılmıştır.

Normal listelerde veri arama işlemi tüm elemanların kontrol edilmesini gerektirir.

* Liste ile arama: O(n)
* Dictionary ile arama: O(1) ortalama durum

Bu nedenle özellikle durak ID, yol ID ve trafik yoğunluğu gibi sık erişilen veriler Dictionary yapısında tutulmuştur.

Örnek kullanım mantığı:

```text
traffic_data["Merkez-Üniversite"] = {
    "density": "medium",
    "delay": 5,
    "average_speed": 35
}
```

Bu yapı rota optimizasyon algoritmasının trafik verisine hızlı ulaşmasını sağlar.

---

## 5. Adjacency List ile Yol Bağlantılarının Tutulması

Ulaşım ağında her durak her durağa bağlı değildir. Bu nedenle tüm bağlantıları matris şeklinde tutmak gereksiz bellek kullanımına neden olur.

Bu projede daha verimli olması için adjacency list yaklaşımı tercih edilmiştir.

### Avantajları

* Bellek kullanımını azaltır.
* Sadece var olan yolları tutar.
* Rota arama algoritmalarıyla uyumludur.
* Büyük ulaşım ağlarında daha verimli çalışır.

### Karmaşıklık

* Bellek karmaşıklığı: O(n + m)

Burada n durak sayısını, m ise yol bağlantısı sayısını ifade eder.

---

## 6. Priority Queue Entegrasyonu

Rota optimizasyonunda en uygun yolun daha hızlı bulunması için Priority Queue yapısı kullanılmıştır.

Priority Queue, en düşük maliyetli rotanın önce işlenmesini sağlar. Böylece algoritma gereksiz yolları daha az kontrol eder.

### Kullanım Amacı

* En kısa süreli rotayı önceliklendirme
* En düşük maliyetli rotayı öne alma
* Trafik yoğunluğu düşük yolları daha önce değerlendirme
* Arama süresini azaltma

### Performans Etkisi

Priority Queue ile rota arama işlemi daha düzenli hale gelir.

* Basit arama yaklaşımı: O(n + m)
* Priority Queue destekli Dijkstra yaklaşımı: O((n + m) log n)

---

## 7. Set Kullanımı ile Tekrarlı İşlemlerin Azaltılması

Rota arama sırasında aynı durağın tekrar tekrar işlenmesi performans kaybına neden olabilir. Bu nedenle ziyaret edilen duraklar Set yapısında tutulmuştur.

Set yapısı sayesinde bir durağın daha önce kontrol edilip edilmediği hızlıca anlaşılır.

* Set içinde arama: O(1) ortalama durum

Bu yapı hem işlem süresini azaltır hem de algoritmanın daha güvenilir çalışmasını sağlar.

---

## 8. Rota Sonuçlarının Düzenli Veri Modeli ile Tutulması

Rota sonucu sadece durak listesinden oluşmaz. Sonuç içinde süre, mesafe, maliyet ve ziyaret edilen düğüm sayısı gibi bilgiler de yer alır.

Bu nedenle rota sonuçları düzenli bir veri modeli içinde tutulmuştur.

Örnek alanlar:

| Alan                | Açıklama                                 |
| ------------------- | ---------------------------------------- |
| `path`              | Rota üzerindeki durak sırası             |
| `total_minutes`     | Toplam tahmini süre                      |
| `total_distance_km` | Toplam mesafe                            |
| `total_cost`        | Hesaplanan rota maliyeti                 |
| `visited_nodes`     | Algoritmanın kontrol ettiği durak sayısı |

Bu yapı sonuçların hem testlerde hem de kullanıcı arayüzünde daha kolay kullanılmasını sağlar.

---

## 9. Veri Yapılarının Algoritmalarla Uyumluluğu

Geliştirilen veri yapıları rota optimizasyon algoritmalarıyla uyumlu olacak şekilde düzenlenmiştir.

| Algoritma / Modül         | Uyumlu Veri Yapısı                |
| ------------------------- | --------------------------------- |
| Rota arama algoritması    | Graph, Priority Queue, Dictionary |
| Trafik yoğunluğu analizi  | Dictionary, List                  |
| Alternatif rota listeleme | List, Object                      |
| Kapalı yol kontrolü       | Set, Dictionary                   |
| Test senaryoları          | Object / Data Class               |
| Cache mekanizması         | Dictionary / LRU Cache            |

Bu uyum sayesinde sistemin farklı modülleri aynı veri mantığı üzerinden çalışabilir.

---

## 10. Performans İyileştirmeleri

Veri yapısı entegrasyonu sonucunda aşağıdaki performans iyileştirmeleri hedeflenmiştir:

1. Durak ve yol bilgilerine erişim hızlandırıldı.
2. Gereksiz liste taramaları azaltıldı.
3. Rota arama algoritması grafik yapısıyla uyumlu hale getirildi.
4. Trafik verileri hızlı erişilebilir şekilde düzenlendi.
5. Ziyaret edilen duraklar Set ile kontrol edilerek tekrarlar azaltıldı.
6. Priority Queue ile en uygun rota daha verimli seçildi.
7. Bellek kullanımı adjacency list yaklaşımıyla daha kontrollü hale getirildi.

---

## 11. Genel Karmaşıklık Değerlendirmesi

| İşlem                    | Eski Yaklaşım | Entegre Edilen Yapı | Yeni Yaklaşım |
| ------------------------ | ------------: | ------------------- | ------------: |
| Durak arama              |          O(n) | Dictionary          |          O(1) |
| Trafik verisine erişim   |          O(n) | Dictionary          |          O(1) |
| Ziyaret kontrolü         |          O(n) | Set                 |          O(1) |
| Yol bağlantılarını tutma |         O(n²) | Adjacency List      |      O(n + m) |
| Öncelikli rota seçimi    |          O(n) | Priority Queue      |      O(log n) |

---

## 12. Sonuç

Veri yapısı entegrasyonu ile proje, yeni geliştirilen rota optimizasyon algoritmalarıyla daha uyumlu hale getirilmiştir. Dictionary, Set, Priority Queue ve Adjacency List gibi veri yapıları kullanılarak veri erişimi hızlandırılmış, işlem süresi azaltılmış ve bellek kullanımı daha verimli hale getirilmiştir.

Bu çalışma sonucunda Akıllı Ulaşım Sistemi projesinin algoritmik altyapısı daha düzenli, ölçeklenebilir ve sürdürülebilir bir yapıya kavuşmuştur.
