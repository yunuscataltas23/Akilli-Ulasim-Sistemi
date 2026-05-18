TRAFİK VERİ KAYNAKLARI ARAŞTIRMASI VE ENTEGRASYON PLANI
1. Trafik Veri Kaynakları Araştırması
Sistemin veri katmanı, doğruluk ve kapsama alanını maksimize etmek amacıyla üç farklı kaynaktan beslenecektir:

Sabit Altyapı Kaynakları
Manyetik Döngü Dedektörleri: Yol yüzeyinin altına yerleştirilen bu sensörler, üzerinden geçen araç sayısını ve doluluk oranını %98 doğrulukla iletir. Veriler genellikle saniyelik periyotlarla JSON formatında akar.

Trafik İzleme Kameraları: Görüntü işleme teknolojileri (YOLO, OpenCV) kullanılarak araç yoğunluğu ve ortalama hız verisi üretilir. Bu kaynaklar özellikle kaza tespiti ve şerit bazlı analizler için kritiktir.

Dinamik ve Hareketli Kaynaklar
FCD (Floating Car Data): Toplu taşıma araçları ve belediye filosuna ait GPS ünitelerinden gelen anlık konum, yön ve hız bilgileridir. NMEA veya GeoJSON formatında iletilen bu veriler, sistemin ana damarını oluşturur.

Mobil Uygulama SDK Verileri: Kullanıcıların anonimleştirilmiş konum verileri, ana arterler dışındaki ara sokakların trafik durumu hakkında geniş kapsamlı bilgi sağlar.

Çevresel ve Harici Kaynaklar
Meteorolojik Veriler: Hava durumu API’leri üzerinden alınan yağış, kar ve buzlanma bilgileri, algoritmanın "tahmini varış süresi" hesaplamalarındaki hata payını minimize eder.

Olay ve Duyuru Verileri: Belediyelerin açık veri portallarından çekilen planlı yol çalışmaları, sosyal etkinlikler veya anlık kaza bildirimleri.

2. Veri Entegrasyon ve İşleme Planı
Veri Toplama Sıklığı
Anlık Veriler (Sıcak Veri): GPS ve sensör verileri her 5 saniyede bir güncellenir.

Analitik Veriler (Soğuk Veri): Geçmiş yoğunluk analizi için ham veriler saatlik periyotlarla büyük veri havuzuna aktarılır.

Veri Temizleme ve Normalizasyon
Filtreleme: GPS sinyal sıçramaları (jitter) ve hatalı koordinatlar (deniz veya bina içi konumlar) Kalman Filtresi kullanılarak temizlenir.

Doldurma: Kısa süreli veri kesintilerinde, aracın önceki hızı ve yolun limitlerine bakılarak lineer interpolasyon ile veri tamamlama yapılır.

Standartlaştırma: Farklı kaynaklardan gelen hız (km/s, mph) ve zaman (Unix, ISO 8601) formatları tek bir standart yapıya dönüştürülür.

3. Depolama ve Mimari Stratejisi
Katmanlı Depolama Yapısı
Hızlı Erişim Katmanı (Redis): Anlık araç konumları ve /api/toplu-tasima/arac-durumu talepleri için düşük gecikmeli bellek içi depolama.

Zaman Serisi Katmanı (InfluxDB): Trafik yoğunluk trendlerini takip etmek ve /api/trafik/yogunluk endpoint'ini beslemek için optimize edilmiş yapı.

Analiz Katmanı (PostgreSQL/HDFS): Rota optimizasyon modelinin eğitimi ve yakıt tasarrufu raporlamaları için kullanılan geniş ölçekli arşiv.

4. Güvenlik ve Güvenilirlik
Veri Erişimi: Tüm veri alışverişi TLS 1.3 protokolü ile şifrelenecek ve API Key/OAuth2 mekanizmalarıyla yetkilendirilecektir.

Hata Toleransı: Bir veri kaynağının (örneğin fiziksel sensörler) devre dışı kalması durumunda, sistem otomatik olarak mobil veri veya kamera verisi ağırlıklı hesaplama moduna (Failover) geçiş yapacaktır.

Veri Gizliliği: Kişisel verilerin korunması kapsamında, sürücü ve yolcu kimlikleri sisteme girmeden önce anonimleştirilecektir.
