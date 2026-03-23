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

Gereksinim Analizi Dokümanı
1. Proje Tanımı
Akıllı Ulaşım Sistemi projesi, şehir içi ulaşımı daha verimli hale getirmek amacıyla yapay zeka, büyük veri analizi ve optimizasyon tekniklerini kullanmayı hedeflemektedir. Sistem; trafik yoğunluğunu tahmin edecek, toplu taşıma araçlarının rota ve sefer planlarını optimize edecek, yolculara mobil uygulama üzerinden bilgilendirme sağlayacaktır. Böylece trafik sıkışıklığının azaltılması, yakıt tüketiminin düşürülmesi ve seyahat sürelerinin kısaltılması amaçlanmaktadır.
2. Amaç
Bu gereksinim analizi çalışmasının amacı, proje paydaşlarıyla yapılan görüşmeler doğrultusunda sistemin ihtiyaçlarını belirlemek ve bu ihtiyaçları fonksiyonel gereksinimler ile fonksiyonel olmayan gereksinimler şeklinde sistematik olarak belgelemektir.
3. Paydaş Analizi
Projede görüşülmesi gereken temel paydaşlar şunlardır:
3.1 Belediye / Ulaşım Daire Başkanlığı
Şehir içi ulaşım politikalarını belirler.
Trafik ve toplu taşıma verilerinin kullanımına onay verir.
Sistemin şehir geneline entegrasyonundan sorumludur.
3.2 Toplu Taşıma İşletmeleri
Otobüs, minibüs, tramvay gibi araçların operasyonunu yürütür.
Araç konumları, sefer planları ve doluluk oranları gibi verileri sağlar.
Sistemden rota ve sefer optimizasyon önerileri bekler.
3.3 Trafik Yönetim Merkezi
Anlık trafik yoğunluğu, yol çalışmaları, kazalar ve kapanan yollar gibi bilgileri sisteme sağlar.
Trafik tahmin modülünden faydalanır.
3.4 Yolcular / Vatandaşlar
Mobil uygulama üzerinden sefer saatleri, gecikmeler, yoğunluk ve alternatif rotalar hakkında bilgi alır.
Kullanıcı deneyimi açısından sistemin en önemli son kullanıcı grubudur.
3.5 Sistem Yöneticileri
Tüm sistemin izlenmesi, yönetimi ve raporlanmasından sorumludur.
Kullanıcı yönetimi, sistem performansı ve veri akışını kontrol eder.
3.6 Yazılım Geliştirme Ekibi
Sistem bileşenlerini geliştirir, test eder ve bakımını sağlar.
Gereksinimlerin teknik çözümlere dönüştürülmesinden sorumludur.
4. Gereksinim Toplama Yöntemi
Proje gereksinimleri aşağıdaki yöntemlerle toplanmıştır:
Paydaş görüşmeleri
Senaryo analizi
Kullanıcı ihtiyaçlarının incelenmesi
Mevcut ulaşım sistemlerinin gözlemlenmesi
Teknik altyapı ve veri kaynaklarının değerlendirilmesi
Bu süreçte özellikle şu sorulara yanıt aranmıştır:
Trafik verileri hangi kaynaklardan alınacaktır?
Sistem hangi kullanıcı gruplarına hizmet verecektir?
Rotayı optimize ederken hangi kriterler dikkate alınacaktır?
Kullanıcılar mobil uygulamada hangi bilgilere erişmek isteyecektir?
Sistem hangi performans ve güvenlik standartlarını sağlamalıdır?
5. Fonksiyonel Gereksinimler
Fonksiyonel gereksinimler, sistemin yerine getirmesi gereken işlevleri tanımlar.
5.1 Trafik Veri Toplama Modülü
FR-1: Sistem, trafik verilerini farklı kaynaklardan toplayabilmelidir.
Açıklama: Kamera sistemleri, sensörler, GPS cihazları, toplu taşıma araçları ve açık veri kaynakları üzerinden veri alınmalıdır.
FR-2: Sistem, anlık trafik yoğunluğu verisini işleyebilmelidir.
Açıklama: Belirli yol, kavşak ve güzergâhlardaki yoğunluk bilgisi gerçek zamanlı olarak analiz edilmelidir.
FR-3: Sistem, geçmiş trafik verilerini depolayabilmelidir.
Açıklama: Trafik tahmini ve analiz süreçlerinde kullanılmak üzere tarihsel veriler saklanmalıdır.
FR-4: Sistem, veri akışındaki eksik veya hatalı kayıtları tespit edebilmelidir.
Açıklama: Yanlış, eksik veya tutarsız veriler sistem tarafından filtrelenmelidir.
5.2 Trafik Tahmin ve Analiz Modülü
FR-5: Sistem, geçmiş ve anlık verilere dayanarak trafik yoğunluğunu tahmin edebilmelidir.
Açıklama: Makine öğrenmesi algoritmaları ile belirli zaman dilimleri için yoğunluk tahmini yapılmalıdır.
FR-6: Sistem, yoğunluk artışı beklenen bölgeleri önceden belirleyebilmelidir.
Açıklama: Özellikle işe gidiş-geliş saatleri, etkinlik günleri ve hava koşullarına bağlı yoğunluklar öngörülmelidir.
FR-7: Sistem, trafik yoğunluk raporları oluşturabilmelidir.
Açıklama: Günlük, haftalık ve aylık raporlar üretilebilmelidir.
5.3 Rota Optimizasyon Modülü
FR-8: Sistem, toplu taşıma araçları için en uygun rotaları önerebilmelidir.
Açıklama: Trafik yoğunluğu, mesafe, yol durumu ve yolcu talebi dikkate alınmalıdır.
FR-9: Sistem, alternatif güzergâhlar oluşturabilmelidir.
Açıklama: Yol kapanması, kaza veya aşırı yoğunluk durumlarında sistem alternatif rota üretmelidir.
FR-10: Sistem, sefer saatlerini optimize edebilmelidir.
Açıklama: Yoğun saatlerde sefer sıklığı artırılmalı, düşük yoğunlukta optimize edilmiş planlama yapılmalıdır.
FR-11: Sistem, rota değişikliklerini ilgili yöneticilere bildirebilmelidir.
Açıklama: Operasyon birimi önerilen rota güncellemelerini görüntüleyebilmelidir.
5.4 Toplu Taşıma Yönetim Sistemi
FR-12: Sistem, araçların anlık konumunu takip edebilmelidir.
Açıklama: Her aracın lokasyonu merkezi panelde gösterilmelidir.
FR-13: Sistem, araç doluluk oranını izleyebilmelidir.
Açıklama: Yolcu yoğunluğu analiz edilerek kapasite yönetimi sağlanmalıdır.
FR-14: Sistem, sefer gecikmelerini tespit edebilmelidir.
Açıklama: Planlanan saat ile gerçekleşen saat karşılaştırılarak gecikmeler raporlanmalıdır.
FR-15: Sistem, yöneticilere karar destek ekranı sunmalıdır.
Açıklama: Yoğun bölgeler, aktif araçlar, gecikmeler ve önerilen müdahaleler tek panelde gösterilmelidir.
5.5 Mobil Uygulama
FR-16: Kullanıcılar, mobil uygulama üzerinden sefer saatlerini görüntüleyebilmelidir.
FR-17: Kullanıcılar, araçların tahmini varış süresini görebilmelidir.
FR-18: Kullanıcılar, trafik yoğunluğu nedeniyle oluşan gecikmeler hakkında bildirim alabilmelidir.
FR-19: Kullanıcılar, kendileri için önerilen alternatif güzergâhları görüntüleyebilmelidir.
FR-20: Kullanıcılar, sık kullandıkları durak ve hatları favorilere ekleyebilmelidir.
FR-21: Mobil uygulama, anlık bildirim gönderebilmelidir.
Açıklama: Sefer iptali, gecikme, rota değişikliği gibi durumlarda kullanıcılara bildirim gönderilmelidir.
5.6 Yönetim ve Yetkilendirme
FR-22: Sistem, farklı kullanıcı rolleri tanımlayabilmelidir.
Açıklama: Yönetici, operatör, analist ve son kullanıcı gibi roller desteklenmelidir.
FR-23: Yetkili kullanıcılar sisteme güvenli giriş yapabilmelidir.
FR-24: Yönetici kullanıcılar raporları görüntüleyip dışa aktarabilmelidir.
FR-25: Sistem yöneticisi, kullanıcı ve yetki yönetimi yapabilmelidir.
6. Fonksiyonel Olmayan Gereksinimler
Fonksiyonel olmayan gereksinimler, sistemin kalite özelliklerini ve çalışma koşullarını ifade eder.
6.1 Performans Gereksinimleri
NFR-1: Sistem, anlık trafik verilerini düşük gecikmeyle işleyebilmelidir.
Ölçüt: Gerçek zamanlı veri işleme gecikmesi mümkün olduğunca birkaç saniye seviyesinde olmalıdır.
NFR-2: Mobil uygulamada kullanıcı sorgularına hızlı yanıt verilmelidir.
Ölçüt: Ortalama ekran yanıt süresi kabul edilebilir düzeyde tutulmalıdır.
NFR-3: Sistem, yüksek veri hacmini kaldırabilecek yapıda olmalıdır.
Ölçüt: Büyük şehir ölçeğinde eşzamanlı veri akışı desteklenmelidir.
6.2 Güvenilirlik Gereksinimleri
NFR-4: Sistem, 7/24 çalışabilecek şekilde tasarlanmalıdır.
NFR-5: Veri kaybını önlemek için yedekleme mekanizması bulunmalıdır.
NFR-6: Hata durumlarında sistem kontrollü şekilde çalışmaya devam edebilmelidir.
Açıklama: Bir modülde hata oluşsa bile tüm sistem tamamen devre dışı kalmamalıdır.
6.3 Güvenlik Gereksinimleri
NFR-7: Kullanıcı verileri güvenli şekilde saklanmalıdır.
NFR-8: Yetkisiz erişim engellenmelidir.
NFR-9: Veri iletimi sırasında güvenli iletişim protokolleri kullanılmalıdır.
Açıklama: API ve uygulama haberleşmesinde şifreli iletişim tercih edilmelidir.
NFR-10: Yönetici paneline erişim güçlü kimlik doğrulama ile korunmalıdır.
6.4 Ölçeklenebilirlik Gereksinimleri
NFR-11: Sistem, artan kullanıcı ve veri sayısına göre ölçeklenebilir olmalıdır.
NFR-12: Yeni veri kaynakları sisteme kolayca entegre edilebilmelidir.
NFR-13: Farklı şehirler için uyarlanabilir altyapı sunmalıdır.
6.5 Kullanılabilirlik Gereksinimleri
NFR-14: Mobil uygulama sade ve kullanıcı dostu bir arayüze sahip olmalıdır.
NFR-15: Yönetim paneli kolay öğrenilebilir ve anlaşılır olmalıdır.
NFR-16: Sistem, farklı yaş ve teknoloji kullanım düzeyindeki kullanıcılar tarafından rahatça kullanılabilmelidir.
6.6 Bakım ve Sürdürülebilirlik Gereksinimleri
NFR-17: Sistem modüler mimaride geliştirilmelidir.
NFR-18: Kod yapısı bakım ve güncelleme için uygun olmalıdır.
NFR-19: Sistem loglama ve hata izleme mekanizmalarına sahip olmalıdır.
NFR-20: Yeni yapay zeka modelleri sisteme sonradan entegre edilebilmelidir.
7. Varsayımlar ve Kısıtlar
7.1 Varsayımlar
Trafik verilerine erişim için ilgili kurumlardan izin alınacağı varsayılmıştır.
Toplu taşıma araçlarında GPS benzeri takip altyapısının bulunduğu kabul edilmiştir.
Kullanıcıların mobil internet erişimine sahip olduğu varsayılmıştır.
7.2 Kısıtlar
Veri kalitesi, sistem doğruluğunu doğrudan etkileyecektir.
Şehir altyapısındaki teknik eksiklikler gerçek zamanlı veri akışını zorlaştırabilir.
Projede kullanılacak teknolojiler Java, Spark, Kafka, Neo4j ve makine öğrenmesi araçlarıyla sınırlıdır.
Kamu kurumlarıyla entegrasyon süreçleri zaman alabilir.
8. Örnek Paydaş Görüşme Soruları
Aşağıdaki sorular gereksinim toplama sürecinde kullanılabilir:
Belediye / Ulaşım Yetkilileri için
Mevcut ulaşım sisteminde en büyük problem nedir?
Trafik yoğunluğu en çok hangi bölgelerde ve saatlerde yaşanmaktadır?
Hangi veriler sisteme entegre edilebilir?
Sistemin başarısını hangi kriterlerle değerlendireceksiniz?
Toplu Taşıma İşletmeleri için
Araç rotaları ne sıklıkla değiştirilmektedir?
En çok gecikme yaşanan hatlar hangileridir?
Araç doluluk bilgileri mevcut mu?
Sistemden hangi operasyonel önerileri bekliyorsunuz?
Yolcular için
Ulaşımda en çok hangi sorunları yaşıyorsunuz?
Mobil uygulamada hangi bilgileri görmek istersiniz?
Gecikme ve rota değişikliklerinde bildirim almak ister misiniz?
Alternatif rota önerileri sizin için ne kadar önemlidir?
Sistem Yöneticileri için
Hangi raporlar kritik öneme sahiptir?
Yetkilendirme seviyeleri nasıl olmalıdır?
Sistemde hangi alarmlar ve uyarılar bulunmalıdır?
9. Sonuç
Yapılan gereksinim analizi sonucunda Akıllı Ulaşım Sistemi’nin, çok paydaşlı ve veri yoğun çalışan bir karar destek sistemi olduğu anlaşılmıştır. Projenin başarısı; doğru veri toplama, gerçek zamanlı analiz, etkili rota optimizasyonu ve kullanıcı dostu bilgilendirme mekanizmalarına bağlıdır. Belirlenen fonksiyonel ve fonksiyonel olmayan gereksinimler, sistem tasarımı ve geliştirme aşamalarına temel oluşturacaktır.
