# Meme Kanseri Sınıflandırma Projesi

## Açıklama

Bu proje, meme kanseri teşhisini otomatikleştirmek için bir karar ağacı tabanlı sınıflandırma modeli oluşturmayı amaçlamaktadır. Meme kanseri, dünya genelinde kadınlarda en sık görülen kanser türlerinden biridir ve erken teşhis, tedavi şansını artırabilir. Bu projenin amacı, bir makine öğrenimi modeli kullanarak meme kanseri teşhis sürecini iyileştirmektir.

Proje, breast cancer veri seti üzerinde çalışmaktadır. Veri seti, meme kanseri teşhisiyle ilgili özellikler içeren bir veri kümesini içermektedir. Bu özellikler arasında hastaların yaş, tümör boyutu, nod durumu, tümör derecesi gibi demografik ve klinik faktörler yer almaktadır. Veri seti, projenin amacına uygun olarak önceden toplanmış ve hazırlanmıştır.

Bu projenin başlıca hedefleri şunlardır:
- Meme kanseri teşhisini otomatikleştirmek için bir sınıflandırma modeli oluşturmak.
- Modelin, teşhis sürecinde doğruluk oranını artırmak ve yanlış teşhis oranını azaltmak.
- Modelin gerçek dünya verileri üzerinde test edilerek performansını değerlendirmek.

Proje, veri ön işleme, model oluşturma ve model performansının değerlendirilmesi olmak üzere üç ana aşamadan oluşmaktadır. Veri ön işleme aşamasında, veri seti temizlenir, eksik değerler doldurulur ve öznitelik mühendisliği teknikleri uygulanır. Model oluşturma aşamasında, karar ağacı tabanlı bir sınıflandırma modeli eğitilir ve optimize edilir. Model performansı değerlendirme aşamasında ise, modelin doğruluğu, hassasiyeti, özgüllüğü ve F1 skoru gibi metrikler kullanılarak test edilir.

Bu proje, meme kanseri teşhisine yardımcı olmak isteyen sağlık profesyonelleri, veri bilimcileri ve makine öğrenimi meraklıları için faydalı olabilir. Ayrıca, veri seti üzerinde yapılacak çalışmalar ve modelin performansını iyileştirmek için yapılan geliştirmeler, meme kanseri teşhisi konusunda daha ileri çalışmaların temelini oluşturabilir.

## Gereksinimler

Proje, aşağıdaki yazılım ve kütüphanelerin yüklü olmasını gerektirir:

- **Python 3.x:** Proje Python programlama dilinde geliştirilmiştir, bu nedenle Python 3.x sürümünün yüklü olması gerekmektedir. Python'i [buradan](https://www.python.org/downloads/) indirebilir ve yükleyebilirsiniz.
- **NumPy:** Sayısal hesaplamalar için kullanılan bir Python kütüphanesidir. NumPy'yi yüklemek için şu komutu kullanabilirsiniz: ***pip install numpy***
- **Pandas:** Veri manipülasyonu ve analizi için kullanılan bir Python kütüphanesidir. Pandas'ı yüklemek için şu komutu kullanabilirsiniz: ***pip install pandas***
- **Scikit-learn:** Makine öğrenimi algoritmalarını içeren bir Python kütüphanesidir. Scikit-learn'ü yüklemek için şui komutu kullanabilirsiniz: ***pip install scikit-learn***
- **Jupyter Notebook (isteğe bağlı):** Projeyi Jupyter Notebook üzerinde çalıştırmak isterseniz, Jupyter Notebook'un yüklü olması gerekmektedir. Jupyter Notebook'u yüklemek için şu komutu kullanabilirsiniz: ***pip install jupyterlab***

Bu gereksinimler, projeyi çalıştırmak için gerekli olan temel yazılım ve kütüphaneleri içermektedir. Bu adımları izleyerek projenin gereksinimlerini karşılayabilir ve projeyi çalıştırabilirsiniz.

## Kullanılan Veri Seti: Breast Cancer Dataset

Bu veri seti, meme kanseri teşhisi için kullanılan bazı klinik özelliklerin yanı sıra hasta özniteliklerini içeren bir meme kanseri veri setidir. Veri setindeki her bir örnek, bir meme kanseri hastasını temsil etmektedir.

**Veri Seti Özellikleri:**

***Yaş:*** Hastanın yaşı

***Menopoz Durumu:*** Menopoza girmiş (ge40) veya menopoza girmemiş (premeno)

***Tümör Boyutu:*** Tümörün boyutu aralığında ifade edilir

***İnfüzyon Nüvesi:*** İnfüzyon nüvesi hücrelerinin sayısı aralığında ifade edilir

***Lenf Nodu Durumu:*** Lenf nodu durumu (0-2, 3, 4-9, 10-14, 15-19, 20-24, 25-29, 30-34, 35-39)

***Metastaz:*** İki yıl içinde metastaz durumu (evet veya hayır)

***Olay Durumu:*** Kanser tekrarlayıp tekrarlamadığı (tekrarlayan veya tekrarlamayan)

***Meme Konum:*** Meme yerleşimi (sol, sağ)

***Meme Alt Bölge:*** Meme alt bölgesi (sol_up, sol_low, sağ_up, sağ_low, merkezi, çeyrek)

***Radyoterapi:*** Radyoterapi alıp almadığı (evet veya hayır)

Veri setindeki her bir özellik, meme kanseri teşhisi yapmak için potansiyel olarak kullanılabilir. Özellikler, numerik (yaş, tümör boyutu, infüzyon nüvesi), kategorik (menopoz durumu, lenf nodu durumu, metastaz, olay durumu, meme konumu, meme alt bölgesi, radyoterapi) veya sıralı (tümör boyutu) olabilir.

Bu veri seti, meme kanseri teşhisi ile ilgilenen araştırmacılar, veri bilimi uzmanları ve öğrenciler için değerli bir kaynak olabilir. Veri seti üzerinde yapılan analizler, meme kanseri teşhisine yönelik yeni yaklaşımların geliştirilmesine ve tedavi planlarının oluşturulmasına yardımcı olabilir.

**Veri Seti Kaynağı:**

Bu veri seti, meme kanseri teşhisiyle ilgili araştırmalar için UCI Machine Learning Repository'de https://archive.ics.uci.edu/ml/index.php bulunan "Breast Cancer" veri setinin bir parçasıdır.

## Lisans

Bu veri seti, UCI Machine Learning Repository'nin lisans koşullarına tabidir. Aşağıda verilen lisans metnini inceleyiniz:

Bu veri seti, UCI Machine Learning Repository tarafından sağlanmaktadır ve Creative Commons Attribution 4.0 International (CC BY 4.0) lisansı altında lisanslanmıştır. Bu lisans, veri setini ticari veya ticari olmayan herhangi bir amaçla kullanmanıza, dağıtmanıza, yeniden üretmenize, uyarlamalar yapmanıza ve paylaşmanıza olanak tanır. Ancak, bu lisans altında kullanım yaparken aşağıdaki şartları yerine getirmeniz gerekmektedir:

- Veri setinin kaynağını açıkça belirtmelisiniz, bu README dosyasında verilen UCI Machine Learning Repository referansını kullanabilirsiniz.
- Veri setini kullanırken yapılan değişiklikleri belirtmelisiniz ve orijinal veri setini de paylaşmalısınız.
- Veri setini kullanırken herhangi bir garantinin olmadığını ve veri seti sağlayıcılarının sorumluluktan muaf olduğunu anlamalısınız.

Lisansın tam metnine ve detaylarına UCI Machine Learning Repository web sitesinden erişebilirsiniz.

**Önemli Notlar:**

- Bu veri seti, yalnızca bilimsel araştırma, öğrenim ve eğitim amaçları için kullanılmalıdır. Gerçek dünya uygulamaları için kullanmadan önce ek doğrulama ve doğruluk testleri yapmanız önerilir.
- Bu veri setini kullanırken veri gizliliğine dikkat etmelisiniz ve kişisel bilgileri ifşa etmekten kaçınmalısınız.
- Veri setini kullanırken etik kurallara uymalı ve araştırma etiğine saygı göstermelisiniz.

## Kaynakça

- **UCI Machine Learning Repository:** https://archive.ics.uci.edu/ml/index.php

- **Creative Commons Attribution 4.0 International (CC BY 4.0) lisansı:** https://creativecommons.org/licenses/by/4.0/






