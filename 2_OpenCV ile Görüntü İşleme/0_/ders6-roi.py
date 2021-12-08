# ROI : region of image
# resimden bir bölgeyi çıkarıp alma

# örneğin bir insnaın gözlerini bulan program yapıcaksın.
# bunun içi önce yüzü tespit edip sonra gözlere geçmen lazı
# direk insanda gözleri arasan program performanslı olmaz.
# yüzü kesme için de roi kullanılır

"""
Neden resmi gösterirken plt kütüphanesini kullanıyoruz ? 
çünkü resmin piksellerinni ve hangi konumda olduğumu gösteriyor
ama dikkat etmen gereken bir şey var cv2 de rengler bgr ken plt de rgb dir.
o yüzden fotoğraf orjinnalden farklı gösterilir

"""

import cv2
import matplotlib.pyplot as plt

resim = cv2.imread('people.jpg')

# resimden bir alanı kırmapalım
kirp = resim[500:700, 500:700]

# kırptığımız fotoyu orjinal fotoya ekleyelim
resim[50:250, 500:700] = kirp
# 2. değeri anlamadım??


# kırptığımız alanı gösterelim
# orjinal fotoğrafı da kaybetmeyelim. ikisini yan yana gösterelim
# 121 : 1 satırdan oluşucak, 2 sütun olucak ve bu yazdığımız 1. si
plt.subplot(121)
plt.imshow(resim)

plt.subplot(122)
plt.imshow(kirp)
plt.show()

"""
plt.imshow(resim)
plt.show()
"""

"""
NOT : Resmi gri yapmak isiyorsan
resim = cv2.imread('foto.jpg', 0)
plt.imshow(resim, 'gray')
eklemelisin
"""