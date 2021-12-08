# geometrik şekil çizmek

import cv2
import numpy as np # boş bir görüntü elde etmek için kullanıyoruz?

# eğer 3 parametre verirsek rgb de 3 renkli oluşur.
# np.unit8 eklemezsen default olarak float alır. onu eklersen de pozitif int sayılar kullanıcam demek
# boş bir ekran oluşturalım
img = np.zeros((512,512,3), np.uint8)

#-- çizgi çizme --
# line çizgi çizer.
# pt1 : hangi noktadan başlayacağı
# pt2 : hangi noktaya gideceği. biz xy düzleminde çalışıyoruz.
# renkte şuan rgb çalışıyoruz. o yüzden (x,y,z) olarak yazdık
# thickness : çizgi kalınlığı

# cv2.line(img, (0,0), (512,512), (255,0,0), 5)
# cv2.line(img, (50,400), (0,0), (0,255,0), 10)


#-- dikdörtgen çizme --
# thickness a -1 verirsen içini doldurur. pozitif sayı verirsen kalınlık olur

# cv2.rectangle(img, (50,50), (200,300), (0,0,255), 5)
# cv2.rectangle(img, (200,200), (100,100), (0,255,0), -1)


#-- daire çizme --
# 2. parametre yarıçap konumudur.
# içini doldurup daire yapmak istiyorsan -1 vermelisin

# cv2.circle(img, (250,250), 60, (40,180,50), -1)
# cv2.circle(img, (100,120), 80, (0,180,250), 3)

#-- elips çizme --
# cv2.ellipse(img, (250,250), (100,50), 0,0,180,(0,130,250), 4)
# cv2.ellipse(img, (150,150), (100,50), 0,0,180,(0,0,250), -1)


#-- çokgen çizme --


#-- yazı yazma --
# 3. parametre nerden başlayacak
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img, 'Merhaba Dünya', (10,310), font,4, (255,255,255), 2, cv2.LINE_AA)


cv2.imshow("resim", img)

cv2.waitKey(0)
cv2.destroyAllWindows()