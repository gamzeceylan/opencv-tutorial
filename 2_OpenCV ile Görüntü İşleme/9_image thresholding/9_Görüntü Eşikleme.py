"""
- bir resimde isteidğin yeri ön plana çıkartmak istersen görüntü
eşikleme yapabilirsin
- bir sınır belirlersin örn 125, üzerindekileri gösterme dersin
"""

import cv2
import matplotlib.pyplot as plt

img = cv2.imread("img1.jpg", 0)
# , cv2.COLOR_BGR2GRAY çalışmadı neden anlamadım. 0 ile aynı anlamda
"""
- resimi gray formatına çevirdiğimiz zaman resmin siyah beyaz olacağı
anlamına gelmez. resmin renk tonlarının gray skala da olacağı anlamına gelir
bu da resmin renk tonlarının siyah beyaz olması değil gri sklada gösterilmesi
- koyu yerler 0'a yaklaşoır açık renkler 255'e yaklaşır
- siyah 0, beyaz 1
- cmap="gray" eklemezsen beyaz yerler sarıi siyah yerler yeşil mavi arası bir renk görülür
- cmap = "gray" demek siyah-beyaz renklerde göster demektir
"""
plt.figure()
plt.imshow(img, cmap="gray")
plt.axis("off")
plt.show()

"""
- şimdi 60 diye bir genlik belirleyelim. genliği 60 altı olanlar kaybolucak, 60 üstü olanlar 
kalacak
- genlik 255' e yaklaştıkça renk koyulaşır, genlik 0 a yaklaştıkça renk açılır
"""

# eşikleme 1. yöntem
"""
- iki parametre döndürür. _ -> kullanmıcaz, diğeri tresh_img -> threshold'u alınmış image
- tresh = eşik değeri (global değer 60 sanırım)
  maxval = bizim max belirlediğimizgenliğimiz
  type = eşik türleri. binary kullanırsak 60 ve 255 araısını beyaz yapar, inverse'unu kullansaydık o değerler arasında
kalan yerleri silerdi
"""
_, thres_img = cv2.threshold(img, thresh=60, maxval=255, type=cv2.THRESH_BINARY)
plt.figure()
plt.imshow(thres_img, cmap="gray")
plt.axis("off")
plt.show()

_, thres_img2 = cv2.threshold(img, thresh=60, maxval=255, type=cv2.THRESH_BINARY_INV)
plt.figure()
plt.imshow(thres_img2, cmap="gray")
plt.axis("off")
plt.show()

# eşikleme 2. yöntem -> adaptive
"""
    resimdeki aydınlatmalar farklı. threshold uyguladığın zaman bir dağa bütün olarak baktığında
farklı aydınlatmadan kaynaklı olarak gördüğün gibi yarısı elimizde kaldı yarısı kayboldu. bütünü
kaybettik. bu istenmeyen durumdur
- bütünlüğü bozmamak için adaptive threshholding kullanıcaz. global değer kullanmak her zaman iyi olamayabilir
algoritma görüntünün farklı bölgeleri için farklı eşik değerleri hesaplıyor. bu da bütünü kaynetmemek için, aydınlatması
farklı olan yerlerde avantaj sağlar
- c sabitine göre bir ortalama alınır ve bu kullanacağımız thresh sabiti
- bunun nasıl yapıldığını iyice araştır
- 11 pixel topluluğunun komşu sayısı
"""
thresh_img3 = cv2.adaptiveThreshold(img, maxValue=255, adaptiveMethod=cv2.ADAPTIVE_THRESH_MEAN_C, 
                    thresholdType=cv2.THRESH_BINARY, blockSize=11 , C=8)

plt.figure()
plt.imshow(thresh_img3, cmap="gray")
plt.axis("off")
plt.show()
"""
- oluşan resimde bir bütünlük var. zemin ve dağ bir bütün olarak ayırt edilebilir. 
- gökyüzü yok edilmiş
- adaptive thresh algoritması çok daha iyi sonuç verir

"""












 