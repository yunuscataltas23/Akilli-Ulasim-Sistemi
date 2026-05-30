# Rota Optimizasyon Algoritması Arayüz Tasarımı

## 1. Amaç

Bu dokümanda Akıllı Ulaşım Sistemi projesinde yer alan yapay zeka tabanlı rota optimizasyon algoritması için kullanıcı arayüzü tasarımı açıklanmıştır. Amaç, kullanıcıların başlangıç ve varış noktalarını kolayca seçebilmesi, farklı optimizasyon kriterlerine göre rota oluşturabilmesi ve sonuçları anlaşılır şekilde görüntüleyebilmesidir.

Arayüz tasarımında kullanıcı dostu, sade ve sezgisel bir yapı hedeflenmiştir.

---

## 2. Kullanıcı Arayüzü Genel Yapısı

Arayüz temel olarak dört ana bölümden oluşur:

1. Başlangıç ve varış noktası seçimi
2. Optimizasyon kriteri seçimi
3. Rota hesaplama ve sonuç gösterimi
4. Harita / görsel rota ekranı

Bu yapı sayesinde kullanıcı, karmaşık teknik detaylarla uğraşmadan kendisi için en uygun ulaşım rotasını seçebilir.

---

## 3. Ana Ekran Tasarımı

Ana ekranda kullanıcıdan rota hesaplama için gerekli temel bilgiler alınır.

### Ana Ekranda Yer Alacak Alanlar

* Başlangıç noktası seçimi
* Varış noktası seçimi
* Optimizasyon kriteri seçimi
* Rota hesapla butonu
* Sonuçların görüntüleneceği alan
* Harita veya rota görselleştirme alanı

### Örnek Ana Ekran Yerleşimi

```text
+--------------------------------------------------+
|              Akıllı Ulaşım Sistemi              |
+--------------------------------------------------+
| Başlangıç Noktası: [ Merkez              v ]     |
| Varış Noktası:     [ Üniversite          v ]     |
|                                                  |
| Optimizasyon Kriteri:                            |
| ( ) En Kısa Süre                                 |
| ( ) En Az Maliyet                                |
| ( ) En Kısa Mesafe                               |
| ( ) En Az Trafik Yoğunluğu                       |
|                                                  |
| [ Rotayı Hesapla ]                               |
+--------------------------------------------------+
| Önerilen Rota:                                   |
| Merkez -> Hastane -> Üniversite                  |
| Tahmini Süre: 18 dakika                          |
| Mesafe: 7.5 km                                   |
| Trafik Durumu: Orta                              |
+--------------------------------------------------+
| Harita / Rota Görselleştirme Alanı               |
+--------------------------------------------------+
```

---

## 4. Optimizasyon Kriterleri

Kullanıcı farklı ihtiyaçlara göre rota seçebilmelidir. Bu nedenle arayüzde birden fazla optimizasyon kriteri sunulmalıdır.

### Desteklenecek Kriterler

| Kriter                 | Açıklama                                       |
| ---------------------- | ---------------------------------------------- |
| En kısa süre           | Kullanıcıyı hedefe en hızlı ulaştıran rota     |
| En az maliyet          | Yakıt, mesafe veya ulaşım maliyeti düşük rota  |
| En kısa mesafe         | Kilometre olarak en kısa rota                  |
| En az trafik yoğunluğu | Trafik seviyesi düşük yolları tercih eden rota |

Bu kriterler sayesinde sistem farklı kullanıcı ihtiyaçlarına cevap verebilir.

---

## 5. Sonuç Ekranı Tasarımı

Rota hesaplandıktan sonra kullanıcıya sadece teknik veri değil, anlaşılır bir özet sunulmalıdır.

### Sonuç Ekranında Gösterilecek Bilgiler

* Önerilen rota
* Tahmini ulaşım süresi
* Toplam mesafe
* Trafik yoğunluğu bilgisi
* Alternatif rotalar
* Kullanılan optimizasyon kriteri
* Uyarılar

### Örnek Sonuç Görünümü

```text
Önerilen Rota:
Merkez -> Hastane -> Üniversite

Tahmini Süre:
18 dakika

Toplam Mesafe:
7.5 km

Trafik Durumu:
Orta yoğunluk

Seçilen Kriter:
En kısa süre

Alternatif Rotalar:
1. Merkez -> Otogar -> Üniversite
2. Merkez -> Sanayi -> Üniversite
```

---

## 6. Kullanıcı Akışı

Kullanıcı akışı, sistemin nasıl kullanılacağını adım adım açıklar.

### Kullanıcı Akış Adımları

1. Kullanıcı uygulamayı açar.
2. Başlangıç noktasını seçer.
3. Varış noktasını seçer.
4. Optimizasyon kriterini belirler.
5. “Rotayı Hesapla” butonuna basar.
6. Sistem rota optimizasyon algoritmasını çalıştırır.
7. Kullanıcıya önerilen rota ve alternatif rotalar gösterilir.
8. Kullanıcı isterse farklı kriter seçerek yeniden hesaplama yapar.

### Kullanıcı Akışı Şeması

```text
Uygulama Açılır
       |
       v
Başlangıç Noktası Seçilir
       |
       v
Varış Noktası Seçilir
       |
       v
Optimizasyon Kriteri Seçilir
       |
       v
Rotayı Hesapla Butonuna Basılır
       |
       v
Algoritma En Uygun Rotayı Hesaplar
       |
       v
Sonuçlar ve Alternatif Rotalar Gösterilir
```

---

## 7. Wireframe Tasarımı

Arayüzün ilk taslak görünümü aşağıdaki gibi planlanmıştır.

```text
+------------------------------------------------------+
| LOGO / Akıllı Ulaşım Sistemi                         |
+------------------------------------------------------+
| Başlangıç: [________________________]                |
| Varış:     [________________________]                |
|                                                      |
| Kriter Seçimi:                                      |
| [ En Kısa Süre ] [ En Az Maliyet ]                  |
| [ En Kısa Mesafe ] [ En Az Trafik ]                 |
|                                                      |
|                  [ ROTA HESAPLA ]                   |
+------------------------------------------------------+
| SONUÇLAR                                             |
| Rota: Merkez -> Hastane -> Üniversite                |
| Süre: 18 dk                                          |
| Mesafe: 7.5 km                                       |
| Trafik: Orta                                         |
+------------------------------------------------------+
| HARİTA ALANI                                         |
| [ Görsel rota çizimi burada yer alacak ]             |
+------------------------------------------------------+
```

---

## 8. Kullanıcı Deneyimi İlkeleri

Arayüz tasarlanırken aşağıdaki kullanıcı deneyimi ilkelerine dikkat edilmiştir:

* Kullanıcının yapacağı işlem sayısı azaltılmalıdır.
* Başlangıç ve varış noktası seçimi kolay olmalıdır.
* Butonlar açık ve anlaşılır isimlendirilmelidir.
* Sonuçlar sade bir şekilde gösterilmelidir.
* Teknik kavramlar kullanıcıyı yormayacak şekilde açıklanmalıdır.
* Hata durumlarında kullanıcıya anlaşılır uyarı verilmelidir.
* Mobil ve masaüstü ekranlarda okunabilir tasarım tercih edilmelidir.

---

## 9. Hata ve Uyarı Mesajları

Kullanıcı eksik veya hatalı bilgi girdiğinde sistem uygun uyarılar vermelidir.

### Örnek Uyarı Mesajları

| Durum                   | Uyarı Mesajı                                                      |
| ----------------------- | ----------------------------------------------------------------- |
| Başlangıç noktası boş   | Lütfen başlangıç noktasını seçiniz.                               |
| Varış noktası boş       | Lütfen varış noktasını seçiniz.                                   |
| Aynı nokta seçildi      | Başlangıç ve varış noktası aynı olamaz.                           |
| Rota bulunamadı         | Seçilen noktalar arasında uygun rota bulunamadı.                  |
| Trafik verisi alınamadı | Güncel trafik verisi alınamadı, varsayılan değerler kullanılıyor. |

---

## 10. Geri Bildirim ve İyileştirme

Arayüz tasarımı ekip içinde paylaşılmalı ve geri bildirimlere göre geliştirilmelidir. Kullanıcıların en çok zorlandığı alanlar belirlenerek tasarımda sadeleştirmeler yapılmalıdır.

### İyileştirme Önerileri

* Harita üzerinde rota çizimi eklenebilir.
* Alternatif rotalar farklı kartlar halinde gösterilebilir.
* Trafik yoğunluğu renklerle belirtilebilir.
* Kullanıcı geçmiş rotalarını görüntüleyebilir.
* Sık kullanılan konumlar favorilere eklenebilir.
* Mobil kullanım için daha büyük butonlar kullanılabilir.

---

## 11. Sonuç

Bu arayüz tasarımı, yapay zeka tabanlı rota optimizasyon algoritmasının kullanıcı tarafından kolayca kullanılmasını amaçlamaktadır. Başlangıç ve varış noktası seçimi, optimizasyon kriterleri, rota sonuçları ve görsel gösterim alanları sayesinde sistem daha anlaşılır ve kullanıcı dostu hale getirilmiştir.

Hazırlanan wireframe ve kullanıcı akışı, ilerleyen aşamalarda geliştirilecek gerçek arayüz için temel tasarım planı olarak kullanılabilir.
