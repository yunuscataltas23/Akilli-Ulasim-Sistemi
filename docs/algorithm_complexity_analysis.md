# Algoritma Karmaşıklığı Analizi

## 1. Amaç

Bu dokümanda Akıllı Ulaşım Sistemi projesinde kullanılan temel algoritmaların zaman ve bellek karmaşıklıkları analiz edilmiştir. Analizlerde O(n) notasyonu kullanılmış, sistemin daha verimli çalışması için iyileştirme önerileri sunulmuştur.

Projede temel amaç; trafik yoğunluğu, durak bilgileri, rota seçenekleri ve ulaşım süreleri dikkate alınarak kullanıcıya en uygun güzergahı sunmaktır. Bu nedenle rota arama, veri işleme, sıralama ve filtreleme işlemleri sistemin kritik parçalarıdır.

---

## 2. Kullanılan Değişkenler

Karmaşıklık analizinde aşağıdaki değişkenler kullanılmıştır:

* **n:** Sistemdeki toplam durak sayısı
* **m:** Duraklar arasındaki toplam bağlantı/yol sayısı
* **r:** Kullanıcıya sunulan alternatif rota sayısı
* **t:** Trafik verisi kayıt sayısı

---

## 3. Rota Arama Algoritması Karmaşıklığı

Projede başlangıç ve varış noktaları arasında en uygun rotanın bulunması için grafik tabanlı bir arama mantığı kullanılmaktadır. Duraklar grafikte düğüm, yollar ise kenar olarak düşünülür.

### Zaman Karmaşıklığı

Basit rota arama yaklaşımında tüm duraklar ve bağlantılar kontrol edilebilir.

* Zaman karmaşıklığı: **O(n + m)**

Priority Queue destekli Dijkstra yaklaşımı kullanıldığında ise her düğüm ve bağlantı daha verimli şekilde işlenir.

* Optimize edilmiş zaman karmaşıklığı: **O((n + m) log n)**

Bu yapı özellikle büyük şehir ulaşım ağlarında daha verimli çalışır. Çünkü gereksiz rota denemeleri azaltılır ve en düşük maliyetli yol öncelikli olarak değerlendirilir.

### Mekan Karmaşıklığı

Algoritma çalışırken mesafe bilgileri, önceki durak bilgileri ve ziyaret edilen düğümler bellekte tutulur.

* Mekan karmaşıklığı: **O(n + m)**

---

## 4. Trafik Verisi İşleme Karmaşıklığı

Sistemde trafik yoğunluğu, tahmini süre ve yol durumu gibi bilgiler rota hesaplamasında kullanılmaktadır. Trafik verileri her yol için ayrı ayrı değerlendirildiğinde tüm kayıtların kontrol edilmesi gerekir.

### Zaman Karmaşıklığı

* Trafik verilerinin tek tek işlenmesi: **O(t)**

Eğer trafik verileri durak veya yol kimliğine göre gruplanırsa, ilgili veriye erişim daha hızlı hale gelir.

* HashMap / Dictionary kullanımıyla erişim: **O(1)** ortalama durum

### Mekan Karmaşıklığı

Trafik kayıtları bellekte tutulduğunda kullanılan alan kayıt sayısına bağlıdır.

* Mekan karmaşıklığı: **O(t)**

---

## 5. Alternatif Rotaların Sıralanması

Kullanıcıya birden fazla rota seçeneği sunulduğunda rotalar süre, mesafe veya maliyet değerine göre sıralanabilir.

### Zaman Karmaşıklığı

Alternatif rotaların sıralanması klasik sıralama algoritmalarıyla yapılır.

* Zaman karmaşıklığı: **O(r log r)**

Burada r, kullanıcıya sunulan alternatif rota sayısını ifade eder. Rota sayısı çok fazla olmadığı sürece bu işlem sistem performansını ciddi şekilde zorlamaz.

### Mekan Karmaşıklığı

Sıralama işlemi için alternatif rotalar bellekte tutulur.

* Mekan karmaşıklığı: **O(r)**

---

## 6. Filtreleme İşlemleri

Kullanıcı en kısa süre, en düşük maliyet veya en az aktarma gibi kriterler seçebilir. Bu durumda rotalar belirlenen kritere göre filtrelenir.

### Zaman Karmaşıklığı

Tüm rota seçenekleri tek tek kontrol edildiğinde:

* Zaman karmaşıklığı: **O(r)**

### Mekan Karmaşıklığı

Filtreleme sonucunda uygun rotalar ayrı bir listede tutulursa:

* Mekan karmaşıklığı: **O(r)**

---

## 7. Cache Kullanımı ve Performans Etkisi

Aynı başlangıç ve varış noktası için tekrar tekrar rota hesaplamak sistemin gereksiz işlem yapmasına neden olur. Bu nedenle daha önce hesaplanan rota sonuçları cache yapısında saklanabilir.

### İlk Hesaplama

* Zaman karmaşıklığı: **O((n + m) log n)**

### Cache Sonrası Tekrar Erişim

* Zaman karmaşıklığı: **O(1)** ortalama durum

Bu iyileştirme özellikle sık kullanılan güzergahlarda sistemin cevap verme süresini ciddi şekilde azaltır.

### Mekan Karmaşıklığı

Cache içinde saklanan rota sayısına göre bellek kullanımı artar.

* Mekan karmaşıklığı: **O(k)**

Burada k, cache içinde tutulan rota sonucu sayısını ifade eder.

---

## 8. Genel Karmaşıklık Tablosu

| İşlem                        | Zaman Karmaşıklığı | Mekan Karmaşıklığı |
| ---------------------------- | -----------------: | -----------------: |
| Rota arama                   |   O((n + m) log n) |           O(n + m) |
| Trafik verisi işleme         |               O(t) |               O(t) |
| Alternatif rota sıralama     |         O(r log r) |               O(r) |
| Rota filtreleme              |               O(r) |               O(r) |
| Cache üzerinden rota getirme |               O(1) |               O(k) |

---

## 9. İyileştirme Önerileri

Projenin daha verimli çalışması için aşağıdaki iyileştirmeler önerilmektedir:

1. Rota arama işlemlerinde Priority Queue tabanlı Dijkstra algoritması kullanılmalıdır.
2. Trafik verileri yol veya durak kimliğine göre Dictionary yapısında saklanmalıdır.
3. Sık kullanılan rotalar cache mekanizmasıyla tekrar hesaplanmadan sunulmalıdır.
4. Kapalı yollar veya yoğun trafik olan bağlantılar rota hesaplamasından erken aşamada çıkarılmalıdır.
5. Gereksiz liste kopyalamalarından kaçınılmalı, bellek kullanımı azaltılmalıdır.
6. Büyük veri setlerinde trafik kayıtları parça parça işlenmelidir.
7. Kullanıcıya sunulacak alternatif rota sayısı sınırlandırılmalıdır.

---

## 10. Sonuç

Yapılan karmaşıklık analizine göre projenin en kritik bölümü rota arama algoritmasıdır. Rota arama işlemi optimize edilmediğinde büyük ulaşım ağlarında performans kaybı oluşabilir. Bu nedenle Dijkstra algoritması, cache kullanımı ve verimli veri yapıları sistemin performansını artırmak için önemlidir.

Bu analiz sonucunda projenin zaman ve bellek kullanımı açısından geliştirilebilir noktaları belirlenmiş, O(n) notasyonu ile algoritmaların verimlilik düzeyi açıklanmıştır.
