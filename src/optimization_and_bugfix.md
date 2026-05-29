## Akıllı Ulaşım Sistemi - Proje Geliştirme Akışı

### Hafta 1: Proje Başlangıcı, Analiz ve Kurulum Süreçleri 

**1. Proje Analizi ve Kapsam Tanımlama**
*(Sorumlu: Şule Nur Bayğut)*
* Projenin genel hedefleri ve kapsamı belirlenmiştir. Çözülecek olan şehir içi ulaşım sorunları ve sistemin içereceği temel modüller netleştirilmiştir.

**2. Gereksinim Toplama ve Belgeleme**
*(Sorumlu: Uğur Metin Karabulut)*
* Paydaşlarla görüşülerek projenin ihtiyaçları analiz edilmiştir. Sistemin fonksiyonel ve fonksiyonel olmayan tüm gereksinimleri detaylı bir şekilde belgelenmiştir.

**3. Teknoloji Araştırması ve Seçimi**
*(Sorumlu: Faik Dursun)*
* Proje için en uygun teknoloji yığını (Java, Spark, Kafka, Neo4j ve Machine Learning) araştırılarak seçilmiş ve seçim gerekçeleri rapora eklenmiştir.

**4. Geliştirme Ortamı Kurulumu**
*(Sorumlu: Ayham Nawaf Hammoud)*
* Gerekli yazılımlar ve araçlar kurularak tüm ekip için standart bir geliştirme ortamı ve IDE yapılandırması tamamlanmıştır.

**5. Versiyon Kontrol Sistemi Kurulumu (Git)**
*(Sorumlu: Yunus Çataltaş)*
* Projenin kod yönetimi için Git altyapısı kurulmuş, GitHub üzerinde merkezi bir repository oluşturularak tüm ekip üyelerinin erişimi ve yetkilendirmeleri sağlanmıştır.

---

### Hafta 2: Yapay Zeka Rota Optimizasyon Algoritması Gereksinim Analizi
*(Sorumlu: Yunus Çataltaş)*

**1. Makine Öğrenimi Modellerinin Değerlendirilmesi**
* **Trafik Yoğunluğu Tahmini:** Zaman serisi ve regresyon tabanlı tahminler için LSTM, GRU veya ağaç tabanlı (XGBoost, Random Forest) modeller değerlendirilmiştir.
* **Rota Optimizasyonu:** Grafik veritabanı (Neo4j) ile entegre çalışacak Pekiştirmeli Öğrenme (Reinforcement Learning) ve dinamik A* / Dijkstra arama algoritmaları belirlenmiştir.

**2. Özellik Mühendisliği (Feature Engineering)**
* Modellerde kullanılacak zaman özellikleri (saat, gün, tatiller), hava durumu (sıcaklık, yağış, sis) ve dinamik olaylar (kazalar, yol bakımları, etkinlikler) listelenmiştir.

**3. Algoritma Doğruluk ve Sistem Performans Metrikleri**
* Model başarısı için MAE, RMSE ve $R^2$ metrikleri; sistem başarısı için seyahat süresi tasarrufu (%) ve algoritma yanıt süreleri (ms) hedef değerleri tanımlanmıştır.

---

### Hafta 3: Mobil Uygulama Kullanıcı Arayüzü (UI) Tasarımı
*(Sorumlu: Yunus Çataltaş)*

**1. Arayüz Özellikleri ve Kullanıcı Akışları**
* Kullanıcıların toplu taşıma rotalarını görüntüleyebileceği, gerçek zamanlı trafik bilgilerini alabileceği, seyahat planları oluşturabileceği ve kişiselleştirilmiş bildirimler alabileceği ekran tasarımları planlanmıştır.

**2. Tasarım Çıktıları ve Kullanıcı Testleri**
* Uygulamanın UX akışını gösteren tel kafes modelleri (wireframes) ve görsel dili yansıtan yüksek sadakatli mock-up'lar oluşturulmuş, kullanıcı testleri yapılarak tasarımlar iyileştirilmiştir.

---

### Hafta 4: Hata Ayıklama ve Kod İyileştirmesi
*(Sorumlu: Yunus Çataltaş)*

**1. Kod Kalitesinin Artırılması**
* Proje genelindeki mevcut hatalar ayıklanmış, kod yapısı refactor edilerek okunabilirlik ve sürdürülebilirlik standartları yükseltilmiştir.

**2. Performans ve Optimizasyon**
* Yazılan modüllerin kararlı çalışması adına kod mimarisi optimize edilmiş ve teknik borçların (technical debt) temizlenmesi sağlanmıştır.
