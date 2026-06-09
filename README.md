# Akıllı Ulaşım Sistemi

> Yapay zeka destekli rota optimizasyonu, gerçek zamanlı trafik verisi işleme ve toplu taşıma yönetimi için geliştirilen kapsamlı şehir içi ulaşım projesi.

---

## Proje Hakkında

**Akıllı Ulaşım Sistemi**, şehir içi ulaşım süreçlerini daha verimli, hızlı ve veri odaklı hale getirmek amacıyla geliştirilmiş bir yazılım projesidir.

Proje; trafik yoğunluğu, yol durumu, toplu taşıma verileri, rota seçenekleri ve kullanıcı ihtiyaçlarını dikkate alarak daha iyi ulaşım kararları üretmeyi hedefler. Sistem; gerçek zamanlı veri akışı, rota optimizasyonu, veri modelleme, API tasarımı, performans analizi ve test süreçlerini bir araya getirir.

Bu çalışma yalnızca bir yazılım geliştirme projesi değil; aynı zamanda haftalık görev takibi, teknik dokümantasyon, mimari tasarım ve algoritma analizi içeren bütünlüklü bir proje yönetimi örneğidir.

---

## Projenin Amacı

Şehir içi ulaşımda karşılaşılan temel problemler:

* Trafik yoğunluğu
* Uzun seyahat süreleri
* Verimsiz rota planlaması
* Toplu taşıma araçlarının düzensiz seferleri
* Anlık trafik verilerinin karar süreçlerine yeterince dahil edilmemesi
* Kullanıcıların en uygun güzergaha hızlı ulaşamaması

Bu proje, bu problemlere veri analizi ve optimizasyon yaklaşımıyla çözüm üretmeyi amaçlar.

### Hedefler

* Trafik yoğunluğunu analiz etmek
* Daha uygun ulaşım rotaları önermek
* Toplu taşıma sefer ve güzergah planlamasını desteklemek
* Seyahat süresini azaltmak
* Gerçek zamanlı trafik verilerini sistem mimarisine dahil etmek
* Rota arama algoritmasını performans açısından iyileştirmek
* Test edilebilir, sürdürülebilir ve belgelenmiş bir proje yapısı oluşturmak

---

## Temel Özellikler

* Gerçek zamanlı trafik verisi işleme mimarisi
* Kafka ve Spark tabanlı veri akışı tasarımı
* Neo4j ile grafik tabanlı trafik ağı modelleme
* Rota optimizasyon algoritması
* Priority Queue destekli arama yaklaşımı
* Trafik yoğunluğu, süre, mesafe ve maliyet kriterleriyle rota değerlendirme
* API dokümantasyonu ve toplu taşıma servis tasarımı
* Mobil ve rota optimizasyon arayüz tasarımları
* Veri yapısı entegrasyonu
* Algoritma karmaşıklığı analizi
* Performans analizi ve optimizasyon raporları
* Test senaryoları ve test raporu
* Haftalık görev ve ilerleme raporu

---

## Kullanılan Teknolojiler

| Alan              | Teknoloji                                |
| ----------------- | ---------------------------------------- |
| Programlama       | Python, Java                             |
| Veri Akışı        | Apache Kafka                             |
| Büyük Veri İşleme | Apache Spark / Spark Streaming           |
| Grafik Veritabanı | Neo4j                                    |
| API Tasarımı      | REST API, YAML / OpenAPI yaklaşımı       |
| Test              | Python test dosyaları                    |
| Veri Modelleme    | İlişkisel veritabanı, grafik veri modeli |
| Versiyon Kontrol  | Git, GitHub                              |
| Dokümantasyon     | Markdown                                 |

---

## Sistem Mimarisi

Proje katmanlı bir mimari anlayışıyla tasarlanmıştır.

```text
Veri Kaynakları
Sensörler, GPS, kameralar, mobil uygulama, olay verileri
        |
        v
Kafka Veri Akış Katmanı
Producer, Topic, Consumer yapıları
        |
        v
Spark Streaming İşleme Katmanı
Veri temizleme, filtreleme, trafik analizi
        |
        v
Veri Modelleme Katmanı
İlişkisel veritabanı ve Neo4j grafik modeli
        |
        v
Optimizasyon Katmanı
Rota arama, veri yapısı entegrasyonu, performans iyileştirme
        |
        v
API Katmanı
Toplu taşıma ve trafik yönetimi servisleri
        |
        v
Kullanıcı Arayüzü
Mobil arayüz ve rota optimizasyon ekranları
```

---

## Proje Yapısı

```text
Akilli-Ulasim-Sistemi/
├── README.md
├── WEEKLY_PROGRESS_REPORT.md
├── project_flow.md
│
├── database/
│   ├── cypher_queries.md
│   ├── database_schema.md
│   └── neo4j_queries.cypher
│
├── docs/
│   ├── ai_route_optimization_requirements.md
│   ├── algorithm_complexity_analysis.md
│   ├── api_documentation.md
│   ├── data_structure_integration.md
│   ├── functional_requirements.md
│   ├── kafka_spark_architecture_design.md
│   ├── mobile_ui_design.md
│   ├── performance_analysis_report.md
│   ├── performance_optimization_results.md
│   ├── route_optimization_ui_design.md
│   ├── traffic_data_integration.md
│   ├── transit_api_spec.yaml
│   └── user_stories.md
│
├── src/
│   ├── ParallelRouteOptimizationDemo.java
│   ├── memory_management.md
│   ├── optimization_and_bugfix.md
│   └── route_search_optimizer.py
│
└── tests/
    ├── route_test.py
    ├── test_report.pdf
    └── test_route_search_optimizer.py
```

---

## Kurulum ve Çalıştırma

Projeyi yerel bilgisayarda çalıştırmak için repository klonlandıktan sonra ilgili dosyalar ayrı ayrı çalıştırılabilir.

### Repository'yi klonlama

```bash
git clone <repository-url>
cd Akilli-Ulasim-Sistemi
```

### Python rota optimizasyon modülünü çalıştırma

```bash
python src/route_search_optimizer.py
```

### Testleri çalıştırma

```bash
python tests/test_route_search_optimizer.py
```

veya:

```bash
python tests/route_test.py
```

### Java demo dosyasını çalıştırma

```bash
javac src/ParallelRouteOptimizationDemo.java
java -cp src ParallelRouteOptimizationDemo
```

---

## Rota Optimizasyon Modülü

Rota optimizasyon çalışmaları projenin ana teknik bileşenlerinden biridir.

İlgili dosya:

```text
src/route_search_optimizer.py
```

Bu modülde şehir içi ulaşım ağı grafik yapısı ile modellenmiştir.

* Duraklar düğüm olarak ele alınmıştır.
* Yollar bağlantı olarak tanımlanmıştır.
* Trafik yoğunluğu rota maliyetine dahil edilmiştir.
* Kapalı yollar ve engellenen duraklar rota dışı bırakılmıştır.
* Priority Queue kullanılarak arama süreci iyileştirilmiştir.
* Cache yapısı ile tekrar eden rota hesaplamaları azaltılmıştır.

---

## Veri Yapısı Entegrasyonu

Projede kullanılan veri yapıları, geliştirilen algoritmalarla uyumlu hale getirilmiştir.

İlgili dosya:

```text
docs/data_structure_integration.md
```

Kullanılan başlıca veri yapıları:

| Amaç                                  | Veri Yapısı            |
| ------------------------------------- | ---------------------- |
| Durak ve yol bilgilerine hızlı erişim | Dictionary / HashMap   |
| Ulaşım ağını modelleme                | Graph / Adjacency List |
| En uygun rotayı önceliklendirme       | Priority Queue         |
| Ziyaret edilen durakları kontrol etme | Set                    |
| Alternatif rotaları tutma             | List                   |
| Rota sonucunu düzenli saklama         | Object / Data Class    |

Bu entegrasyon sayesinde veri erişimi hızlandırılmış, gereksiz tekrarlar azaltılmış ve algoritmalar daha verimli hale getirilmiştir.

---

## Kafka ve Spark Entegrasyonu

Gerçek zamanlı trafik verilerinin işlenmesi için Kafka ve Spark tabanlı bir mimari tasarlanmıştır.

İlgili dosya:

```text
docs/kafka_spark_architecture_design.md
```

Mimari kapsamında:

* Kafka topic yapısı tasarlanmıştır.
* Producer ve consumer bileşenleri tanımlanmıştır.
* Spark Streaming ile veri işleme akışı açıklanmıştır.
* Hatalı veriler için ayrı hata yönetimi yaklaşımı belirlenmiştir.
* Partitioning ve paralel işleme ile performans artırımı değerlendirilmiştir.

---

## Veritabanı ve Neo4j Modeli

Proje kapsamında hem ilişkisel veri modeli hem de grafik tabanlı veri modeli ele alınmıştır.

İlgili dosyalar:

```text
database/database_schema.md
database/cypher_queries.md
database/neo4j_queries.cypher
```

Veritabanı çalışmaları şunları kapsar:

* Trafik sensörleri
* Duraklar
* Yollar
* Toplu taşıma hatları
* Sefer bilgileri
* Trafik yoğunluğu kayıtları
* Neo4j üzerinde düğüm ve ilişki modellemesi
* Rota sorguları için Cypher örnekleri

Neo4j modeli, rota optimizasyonu için uygundur çünkü ulaşım ağı doğal olarak düğüm ve bağlantılardan oluşan bir grafik yapısına sahiptir.

---

## API Tasarımı

Toplu taşıma yönetim sistemi ve trafik verisi işlemleri için API yapısı tasarlanmıştır.

İlgili dosyalar:

```text
docs/api_documentation.md
docs/transit_api_spec.yaml
```

API tasarımı kapsamında:

* Rota sorgulama
* Durak bilgisi alma
* Sefer bilgisi görüntüleme
* Trafik yoğunluğu verisi alma
* Araç konumu takip etme
* JSON tabanlı istek ve yanıt formatları
* OpenAPI/YAML benzeri servis tanımı

ele alınmıştır.

---

## Kullanıcı Arayüzü Tasarımları

Proje kapsamında hem mobil uygulama hem de rota optimizasyon algoritması için arayüz tasarımları hazırlanmıştır.

İlgili dosyalar:

```text
docs/mobile_ui_design.md
docs/route_optimization_ui_design.md
```

Arayüz çalışmalarında:

* Başlangıç ve varış noktası seçimi
* Optimizasyon kriteri seçimi
* En kısa süre, en az maliyet, en kısa mesafe gibi seçenekler
* Sonuç ekranı
* Alternatif rota gösterimi
* Harita / rota görselleştirme alanı
* Wireframe taslakları
* Kullanıcı akışı

tanımlanmıştır.

---

## Algoritma Karmaşıklığı Analizi

Projede kullanılan kritik algoritmalar zaman ve mekan karmaşıklığı açısından analiz edilmiştir.

İlgili dosya:

```text
docs/algorithm_complexity_analysis.md
```

Özet karmaşıklık tablosu:

| İşlem                    | Zaman Karmaşıklığı | Mekan Karmaşıklığı |
| ------------------------ | -----------------: | -----------------: |
| Rota arama               |   O((n + m) log n) |           O(n + m) |
| Trafik verisi işleme     |               O(t) |               O(t) |
| Alternatif rota sıralama |         O(r log r) |               O(r) |
| Rota filtreleme          |               O(r) |               O(r) |
| Cache erişimi            |               O(1) |               O(k) |

Bu analiz sonucunda rota arama algoritması, veri erişimi ve bellek kullanımı açısından iyileştirme alanları belirlenmiştir.

---

## Performans ve Optimizasyon

Proje kapsamında performansı artırmak için çeşitli iyileştirmeler yapılmıştır.

İlgili dosyalar:

```text
docs/performance_analysis_report.md
docs/performance_optimization_results.md
src/memory_management.md
src/optimization_and_bugfix.md
src/ParallelRouteOptimizationDemo.java
```

Yapılan çalışmalar:

* Rota arama algoritmasının hızlandırılması
* Bellek kullanımının analiz edilmesi
* Gereksiz veri tekrarlarının azaltılması
* Kod iyileştirme ve hata giderme
* Paralel rota optimizasyonu demo çalışması
* Performans sonuçlarının raporlanması

---

## Test Süreci

Test çalışmaları, algoritmanın doğruluğunu ve sistemin güvenilirliğini kontrol etmek için hazırlanmıştır.

İlgili dosyalar:

```text
tests/route_test.py
tests/test_route_search_optimizer.py
tests/test_report.pdf
```

Test edilen başlıca durumlar:

* Geçerli iki durak arasında rota bulunması
* En düşük maliyetli rotanın seçilmesi
* Kapalı yolların rota dışında bırakılması
* Engellenen durakların kullanılmaması
* Bilinmeyen başlangıç veya hedef durak için hata verilmesi
* Ulaşılamayan hedef için hata kontrolü
* Cache mekanizmasının çalışması

---

## Haftalık Görev Takibi

Proje, haftalık görevler halinde ilerletilmiştir.

Detaylı görev listesi ve tamamlanma bilgileri:

```text
WEEKLY_PROGRESS_REPORT.md
```

Haftalık süreç özeti:

| Hafta   | Odak Alanı                                                                                |
| ------- | ----------------------------------------------------------------------------------------- |
| Hafta 1 | Proje analizi, gereksinim toplama, teknoloji seçimi, Git ve geliştirme ortamı kurulumu    |
| Hafta 2 | Kafka/Spark mimarisi, Neo4j modeli, veri kaynakları, yapay zeka rota gereksinimleri       |
| Hafta 3 | UI tasarımları, API tasarımı, veritabanı tasarımı, Kafka entegrasyon mimarisi             |
| Hafta 4 | Arama algoritması optimizasyonu, veri yapısı entegrasyonu, test ve performans çalışmaları |
| Hafta 5 | Algoritma karmaşıklığı, veri yapısı optimizasyonu, bellek yönetimi, paralel işleme        |
| Hafta 6 | Final testleri, hata giderme, dokümantasyon, performans sonuçlandırma, sunum hazırlığı    |

---

## Ekip ve Görev Alanları

| Ekip Üyesi           | Öne Çıkan Görev Alanları                                                                                                                   |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Şule Nur Bayğut      | Proje analizi, trafik veri kaynakları, veritabanı tasarımı, arama algoritması optimizasyonu, veri yapıları optimizasyonu, proje testleri   |
| Yunus Çataltaş       | Git kurulumu, yapay zeka rota optimizasyon gereksinimleri, mobil arayüz tasarımı, hata ayıklama, bellek yönetimi, performans sonuçlandırma |
| Faik Dursun          | Teknoloji araştırması, Kafka/Spark mimarisi, rota optimizasyon arayüz tasarımı, veri yapısı entegrasyonu, algoritma karmaşıklığı analizi   |
| Uğur Metin Karabulut | Gereksinim toplama, kullanıcı hikayeleri, Kafka entegrasyon mimarisi, performans analizi, paralel işleme, final sunum                      |
| Ayham Nawaf Hammoud  | Geliştirme ortamı kurulumu, Neo4j veri modeli, API tasarımı, test senaryoları, kod tekrarının azaltılması, dokümantasyon                   |

---

## Dokümantasyon Haritası

| Dosya                                        | Açıklama                                    |
| -------------------------------------------- | ------------------------------------------- |
| `WEEKLY_PROGRESS_REPORT.md`                  | Haftalık görev ve ilerleme raporu           |
| `project_flow.md`                            | Proje akışı ve genel sistem planı           |
| `docs/functional_requirements.md`            | Fonksiyonel gereksinimler ve proje kapsamı  |
| `docs/user_stories.md`                       | Kullanıcı hikayeleri                        |
| `docs/ai_route_optimization_requirements.md` | Yapay zeka rota optimizasyon gereksinimleri |
| `docs/traffic_data_integration.md`           | Trafik veri kaynakları ve entegrasyon planı |
| `docs/kafka_spark_architecture_design.md`    | Kafka ve Spark mimari tasarımı              |
| `docs/route_optimization_ui_design.md`       | Rota optimizasyon UI tasarımı               |
| `docs/mobile_ui_design.md`                   | Mobil uygulama UI tasarımı                  |
| `docs/api_documentation.md`                  | API dokümantasyonu                          |
| `docs/transit_api_spec.yaml`                 | Toplu taşıma API servis tanımı              |
| `docs/algorithm_complexity_analysis.md`      | Algoritma karmaşıklığı analizi              |
| `docs/data_structure_integration.md`         | Veri yapısı entegrasyonu                    |
| `docs/performance_analysis_report.md`        | Performans analizi raporu                   |
| `docs/performance_optimization_results.md`   | Performans optimizasyon sonuçları           |
| `database/database_schema.md`                | İlişkisel veritabanı şeması                 |
| `database/cypher_queries.md`                 | Neo4j Cypher sorgu açıklamaları             |
| `database/neo4j_queries.cypher`              | Neo4j sorgu dosyası                         |
| `src/route_search_optimizer.py`              | Optimize edilmiş rota arama algoritması     |
| `src/ParallelRouteOptimizationDemo.java`     | Paralel rota optimizasyon demo dosyası      |
| `src/memory_management.md`                   | Bellek yönetimi çalışması                   |
| `src/optimization_and_bugfix.md`             | Hata giderme ve kod iyileştirme notları     |
| `tests/test_route_search_optimizer.py`       | Rota optimizasyon test senaryoları          |
| `tests/route_test.py`                        | Rota test dosyası                           |
| `tests/test_report.pdf`                      | Test raporu                                 |

---

## Sonuç

Akıllı Ulaşım Sistemi projesi; gerçek zamanlı trafik verisi işleme, rota optimizasyonu, veri modelleme, API tasarımı, kullanıcı arayüzü planlaması, performans analizi ve test süreçlerini bir araya getiren kapsamlı bir şehir içi ulaşım çözümüdür.

Proje süreci haftalık görevlerle planlanmış, her görev teknik dokümantasyon ve uygulama dosyalarıyla desteklenmiştir. Bu sayede proje yalnızca çalışan bileşenlerden değil, aynı zamanda sürdürülebilir ve anlaşılır bir yazılım geliştirme sürecinden oluşmaktadır.
