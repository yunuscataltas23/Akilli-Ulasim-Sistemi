Akıllı Ulaşım Sistemi - Neo4j Trafik Ağı Veri Modeli Tasarımı ve Optimizasyon Raporu 🛣️

Hazırlayan: Ayham Nawaf Hammoud

1. Neo4j Veri Modeli Tasarımı (Düğümler, İlişkiler ve Özellikler)
Trafik ağının doğası gereği ilişkisel veritabanları yerine graf (çizge) tabanlı bir veritabanı olan Neo4j kullanmak, rota optimizasyonu algoritmaları için en ideal çözümdür.

A. Düğümler (Nodes / Etiketler)
Ağdaki fiziksel noktaları temsil eder.

(:Kavsak) [Intersection]: Yol kesişim noktaları.

Özellikler: kavsak_id (String), enlem (Float), boylam (Float), ad (String).

(:Durak) [Transit Stop]: Toplu taşıma noktaları.

Özellikler: durak_id (String), durak_adi (String), tur (String - "Otobüs", "Metro").

B. İlişkiler (Relationships)
Düğümler arasındaki bağlantıları ve hareket yollarını temsil eder.

[:YOL_BAGLANTISI] (Kavşak -> Kavşak): İki kavşak arasındaki fiziksel yolu ifade eder.

Özellikler: mesafe_km (Float), hiz_limiti (Integer), trafik_agirligi (Float - anlık trafik durumunu yansıtan katsayı).

[:TOPLU_TASIMA_HATTI] (Durak -> Durak): Araçların duraklar arası izlediği güzergah.

Özellikler: hat_kodu (String), ortalama_sure_dk (Integer).

2. Rota Optimizasyonu İçin Örnek Cypher Sorguları
Sistemin rotaları en verimli şekilde hesaplayabilmesi için aşağıdaki Cypher sorguları tasarlanmıştır.

Örnek Sorgu 1: Trafik Yoğunluğu Olmadan En Kısa Yolu Bulma (Shortest Path)
Sadece fiziksel bağlantı sayısına veya mesafeye göre A noktasından B noktasına en kısa rotayı çizer.

Örnek Sorgu 2: Trafik Ağırlığını Göz Önüne Alan Optimal Rota (Dijkstra Yaklaşımı için Altyapı)
Yolun mesafesi ve anlık trafik_agirligi kullanılarak toplam seyahat maliyetinin hesaplanması. (Neo4j Graph Data Science eklentisi kullanılarak çalıştırılmak üzere tasarlanmıştır).

3. Veri Modelinin Ölçeklenebilirliği ve Performansı
Sistemin binlerce kavşak ve anlık veri akışı altında çökmemesi ve yüksek performans göstermesi için şu stratejiler belirlenmiştir:

İndeksleme (Indexing): Arama sorgularını hızlandırmak için sık aranan özelliklere (örneğin kavsak_id ve ad) B-Tree indeksleri eklenecektir.

Yönlü İlişkiler: Trafik yollarının tek yön veya çift yön olma durumu ilişkilerin ok yönleriyle (Directed Relationships) belirlenerek algoritmanın ters yönleri taraması engellenecektir.

Önbellekleme ve GDS Kullanımı: Dinamik trafik verileri (trafik_agirligi) çok sık değiştiğinden, karmaşık algoritmalar için Neo4j'in Graph Data Science (GDS) kütüphanesinin bellek içi (in-memory) graf özellikleri kullanılacaktır. Bu, büyük şehir verilerinde sorgu sürelerini milisaniyeler seviyesinde tutacaktır.
