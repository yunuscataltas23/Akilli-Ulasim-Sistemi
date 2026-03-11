# Akıllı Ulaşım Sistemi - Proje Akışı

**Grup Adı:** Algoritma Aşıkları
**Proje Yöneticisi:** Yunus Çataltaş

## 📌 Proje Amacı ve Kapsamı
Bu proje, şehir içi ulaşımı optimize etmek için yapay zeka ve veri analizini kullanmayı amaçlar. Trafik yoğunluğunu tahmin ederek, toplu taşıma araçlarının rotalarını ve sefer saatlerini optimize eder. Amacımız, trafik sıkışıklığını azaltmak, yakıt tüketimini düşürmek ve yolcuların seyahat sürelerini kısaltmaktır.

## 🛠 Teknoloji Yığını
* **Programlama Dili:** Java
* **Büyük Veri & Akış:** Apache Spark, Apache Kafka
* **Veritabanı:** Neo4j
* **Yapay Zeka:** Machine Learning

---

## 📅 Haftalık İlerlemeler ve Yapılan Çalışmalar

### Hafta 1 (Görev Dağılımı ve Başlangıç)
* **Yunus Çataltaş:** Versiyon Kontrol Sistemi (Git) kurulumu yapıldı, merkezi repository oluşturuldu ve takım üyelerine yetki verildi. `projeakisi.md` dosyası hocanın talimatlarına göre oluşturuldu.
* **Şule Nur Bayğut:** Proje Analizi ve Kapsam Tanımlama çalışmalarını tanımladı.
* **Uğur Metin Karabulut:** Gereksinim Toplama ve Belgeleme (Fonksiyonel ve fonksiyonel olmayan) için paydaş görüşmeleri planlandı.
* **Faik Dursun:** Teknoloji Araştırması ve Seçimi yapıldı, kullanılacak araçlar netleştirildi.
* **Ayham Nawaf Hammoud:** Geliştirme Ortamı Kurulumu ve IDE yapılandırması sağlandı.

*(Not: Her hafta ekip üyeleri kendi yaptıkları çalışmaları bu dosyadaki ilgili haftanın altına ekleyecektir.)*


# 📌 Projenin Genel Hedefleri ve Kapsamı

Projenin temel vizyonu, kentsel ulaşımı statik bir yapıdan çıkararak, anlık verilere duyarlı, proaktif ve karar-destek mekanizmalı bir ekosisteme dönüştürmektir.

## Stratejik Hedefler

**Operasyonel Verimlilik:** Mevcut ulaşım altyapısını en yüksek kapasitede kullanarak seyahat sürelerinde ortalama %18,7 oranında iyileşme sağlamak.

**Sürdürülebilirlik:** Gereksiz rölanti sürelerini ve verimsiz rotaları engelleyerek yakıt tüketiminde %10-30, karbon emisyonlarında ise %15'e varan net azalma elde etmek.

**Ulaşım Teşviki:** Toplu taşımayı daha öngörülebilir ve konforlu hale getirerek şahsi araç kullanımını minimize etmek.

## Proje Kapsamı

Proje; şehir genelindeki veri kaynaklarından beslenen bir izleme merkezi, trafik ışıklarını ve araç rotalarını yöneten bir optimizasyon motoru, toplu taşıma operasyonlarını dinamikleştiren bir yönetim sistemi ve vatandaşların kullanımına sunulacak entegre bir mobil platformun geliştirilmesini kapsamaktadır.


  
# ⚠️ Çözülecek Temel Sorunlar

Sistem, modern kent yaşamını zorlaştıran şu kronik sorunlara doğrudan müdahale etmektedir

**Öngörülemeyen Trafik Sıkışıklığı:** Trafiğin sadece o anki durumunun bilinmesi, ancak geçmiş tecrübeler ve anlık olaylar ışığında 15-30 dakika sonrasının tahmin edilememesi sonucu oluşan ani tıkanıklıklar.

**Verimsiz ve Statik Sefer Planları:** Yolcu talebiyle örtüşmeyen sabit hatlar ve saatler nedeniyle araçların düşük kapasiteyle çalışması, buna karşın bazı bölgelerde yolcu yığılmalarının yaşanması.

**Bilgi Dağınıklığı:** Farklı ulaşım modları (otobüs, metro, scooter vb.) arasındaki koordinasyon eksikliği nedeniyle yolcuların kesintisiz bir seyahat planı oluşturamaması.

**Acil Durum Gecikmeleri:** Trafik yoğunluğu nedeniyle ambulans, itfaiye gibi acil müdahale araçlarının olay yerine ulaşım sürelerinin kritik seviyelere çıkması.



# ⚙️ Sistemin İşlevsel Özellikleri ve Modüller

## A. Trafik İzleme ve Anlık Analiz Sistemi

**Gerçek Zamanlı Takip:** Şehrin stratejik noktalarındaki sensörlerden gelen hız ve konum verilerini işleyerek trafik yoğunluğunu anlık olarak haritalandırır.

**Anomali Tespiti:** Kaza veya arıza gibi olağandışı durumları anında fark ederek operatörlere uyarı gönderir ve trafik akışını otomatik olarak yeniden yönlendirir.

## B. Akıllı Rota ve Kavşak Optimizasyonu

**Gelecek Tahminleme:** Geçmiş veri modellerini kullanarak trafiğin tıkanma olasılığı olan bölgeleri önceden belirler ve yoğunluğu henüz oluşmadan dağıtır.

**Dinamik Sinyalizasyon:** Trafik ışıklarının sürelerini araç yoğunluğuna göre anlık olarak ayarlar; kavşaklardaki bekleme sürelerini %28'e kadar azaltır.

**Acil Durum Önceliği (Yeşil Dalga):** Acil durum araçlarının güzergahındaki ışıkları otomatik olarak yeşile çevirerek duraksız geçiş imkanı sağlar.

## C. Yeni Nesil Toplu Taşıma Yönetimi

**Talep Odaklı Ulaşım (DRT):** Sabit hatların verimsiz olduğu bölgelerde, yolcuların uygulama üzerinden yaptığı çağrılara göre rotasını belirleyen esnek servis imkanı sunar.

**Dinamik Çizelgeleme:** Otobüs sefer saatlerini yolcu yoğunluğuna ve trafik durumuna göre saniyeler içinde güncelleyerek duraklardaki beklemeleri en aza indirir.

**Yolcu Yoğunluk Analizi:** Kameralar üzerinden duraklardaki kalabalığı ölçer; yığılma tespit edildiğinde sisteme otomatik olarak ek sefer tanımlar.

## D. Entegre Mobil Kullanıcı Platformu

**Tek Pencereden Ulaşım (MaaS):** Scooter, bisiklet, otobüs ve metroyu tek bir uygulamada birleştirerek yolculuk planlama ve ödeme kolaylığı sağlar.

**Canlı Bilgilendirme:** Araçların harita üzerindeki anlık konumlarını, durağa kesin varış sürelerini ve ağdaki aksamaları saniye hassasiyetinde yolculara iletir.



# 📊 Beklenen Somut Kazanımlar

**Zaman Kazancı:** Toplam seyahat sürelerinde seyahat başına ortalama %18 iyileşme.

**Ekonomik Tasarruf:** Optimize edilen rotalar sayesinde yakıt harcamalarında %30'a varan düşüş.

**Çevresel Katkı:** Karbon salımının azaltılmasıyla daha yaşanabilir bir şehir atmosferi.

