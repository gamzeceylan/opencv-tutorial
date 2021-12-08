# trackbar ile renk ayarı

# trackbar : kaydırma çubuğu
# örneğin ses açma kapama yaparken kaydırdığın çubuk

import cv2
import numpy as np

# 0-255 arasında trackbarı ı oynattığımızda o trackbar ın hangi değerde olduğunu döndüren ifade
def nothing(x):
               #  print(x)
               pass

# uint 8 : pozitif integer sayılar
img = np.zeros((512,512,3), np.uint8)

# boş çerceve
cv2.namedWindow('resim')

# 0 ile 255 arasında trackbar ı oynatıcaz
# 2. parametre nereye eklenicek ? 
# nothing şuan bir şey yapmıyor ama eklemen gerek
cv2.createTrackbar('R', "resim", 0,255, nothing)
cv2.createTrackbar('G', "resim", 0,255, nothing)
cv2.createTrackbar('B', "resim", 0,255, nothing)

# bir tane switch ekleyelim
cv2.createTrackbar('ON/OFF', 'resim', 0, 1, nothing)


# ekranda pencere olduğu sürece çalışan yer burası
while(1):
               cv2.imshow("resim", img)
               # 27 esc dir
               if cv2.waitKey(1) & 0xFF == 27:
                              break
               
               # rgb kodlaırnı çekiyoruz
               r = cv2.getTrackbarPos('R', 'resim')
               g = cv2.getTrackbarPos('G', 'resim')
               b = cv2.getTrackbarPos('B', 'resim')

               switch = cv2.getTrackbarPos('ON/OFF', 'resim')

               # img in tüm pixellerini rgb ye eşitliyoruz
               # sanırım 2 değerli olunca trackbar True False döndürüyor ?
               if switch:
                              img[:] = [r,g,b]
               
               else:
                              img[:] = 0



# bunu yazmadan bi bak farkı gör
cv2.destroyAllWindows()