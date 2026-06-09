Hafta 2: Yapay Zeka Rota Optimizasyon Algoritması Gereksinim Analizi
(Sorumlu: Yunus Çataltaş)
Trafik yoğunluğunu tahmin etmek ve rota optimizasyonu yapmak için gereken yapay zeka mimarisi analiz edilmiş ve aşağıdaki gereksinimler belirlenmiştir:
1. Makine Öğrenimi Modellerinin Değerlendirilmesi
Uygun makine öğrenimi modelleri (regresyon, sınıflandırma, derin öğrenme) proje hedeflerine göre değerlendirilmiştir:
•	Trafik Yoğunluğu Tahmini (Zaman Serisi & Regresyon): Geçmiş verilere dayanarak gelecekteki yoğunluğu tahmin etmek için Derin Öğrenme modellerinden LSTM (Long Short-Term Memory) veya GRU kullanılması en uygun seçenektir. Daha düşük işlem gücü gerektiren senaryolar için ağaç tabanlı regresyon modelleri (XGBoost veya Random Forest Regressor) entegre edilebilir.
•	Rota Optimizasyonu: Tahmin edilen yoğunluk verilerini graf veritabanımız (Neo4j) ile birleştirerek dinamik yönlendirme yapmak için Pekiştirmeli Öğrenme (Reinforcement Learning) algoritmaları veya ağırlıkları anlık güncellenen A (A-Star) / Dijkstra* arama algoritmaları kullanılacaktır.
2. Kullanılacak Özellikler (Feature Engineering)
Algoritmanın doğru çalışabilmesi için modele beslenecek temel özelliklerin (zaman, hava durumu, olaylar vb.) listesi şu şekildedir:
•	Zaman Özellikleri: Günün saati, haftanın günü, resmi tatil/hafta sonu durumu.
•	Hava Durumu: Anlık sıcaklık, yağış durumu (yağmur/kar oranı), görüş mesafesi (sis).
•	Dinamik Olaylar ve Altyapı: Trafik kazaları, planlı yol bakım çalışmaları, yoğunluk yaratacak kitlesel etkinlikler (maç, konser) ve yolun şerit/hız sınırı bilgileri.
3. Algoritma Doğruluk ve Performans Metrikleri
Modelin doğruluğunu ve optimizasyon performansını değerlendirmek için aşağıdaki metrikler izlenecektir:
•	Tahmin Doğruluğu Metrikleri:
o	MAE (Ortalama Mutlak Hata): Tahmin edilen seyahat süresi ile gerçekleşen süre arasındaki ortalama dakika farkı.
o	RMSE (Kök Ortalama Kare Hata): Sistemin yaptığı büyük zaman tahmin hatalarını daha net görebilmek için.
o	$R^2$ (Belirlilik Katsayısı): Modelin trafik değişkenliğini ne oranda açıklayabildiğini ölçmek için.
•	Sistem Performans Metrikleri:
o	Seyahat Süresi Tasarrufu (%): Geleneksel navigasyon rotalarına kıyasla sağlanan zaman kazancı.
o	Algoritma Yanıt Süresi (Milisaniye): Anlık rota hesaplama taleplerine sistemin (Neo4j + ML Modeli) cevap verme hızı.
