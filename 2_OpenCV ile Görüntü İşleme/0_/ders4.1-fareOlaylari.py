# paint benzeri bir uygulama yapıcaz
# ekrandaki mause hareketlerini yazdırıyor

import cv2
import numpy as np
# dir(cv2) opencv2 de kullanabileceğimiz fonksiyonları sıralar
# helpy(cv2)

# peki 'EVENT' için kullanabileceğimiz fonksiyonlar ? 
"""
for i in dir(cv2):
               if 'EVENT' in i:
                              print(i)

"""

# öncelikle paint gibi boş bir kütüphane açmamız gerek
# bunu yapmak için numpy kullanıyoruz
# zeros siyah, ones beyaz
# 512x512 3 tane pencere açıyoruz
# unit8 yine 255 e kadar olan pozitif değerlerle oluşacağını söyledik?
img = np.ones((512,512,3), np.uint8)


# boş bir pencere oluşturuyoruz
cv2.namedWindow('paint')

# klavye hareketlerimizi tanımlayacak fonksiyon
# 1. parametre event
# 2. paramete x
# 3. parametre y
# 4. ve 5. şuallik önemli değil ama yazman gerekiyor
def draw(event, x, y, flags, param):
               print(x,y)

# ilk parametre pencere, ikinci parametre de fonksiyonumuz
# paint penceresinde işlem yapıyor
# draw ile de verdiğimiz olayı gösteriyor
cv2.setMouseCallback('paint', draw)

# görüntümüzü gösterelim
while(1):
               cv2.imshow('paint', img)
               # döngüden çıkabilmek için
               if cv2.waitKey(1) & 0xFF == ord('q'):
                              break

# tüm pencereleri kapatmak için
cv2.destroyAllWindows()