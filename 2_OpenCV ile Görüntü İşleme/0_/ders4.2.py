# paint

import cv2
import numpy as np



# biz tıkladığımız sürece true olucak
# tıklamyı bıraktığımızda false olucak
cizim = False

# başlangıç koordinatları 
xi, yi = -1, -1

# m ye basınca çizim moduna geçsin
mod = False

"""
NOT : LB -> left button, RB -> right button, M -> mouse hareketleri
"""

def draw(event, x, y, flags, param):
               """
               # eğer çift tıklanırsa daire çizsin
               if event == cv2.EVENT_LBUTTONDBLCLK:
                              # 1. parametre nereye çizicek
                              # 2. parametre merkez kordinatlar
                              # 3. parametre yarıçap
                              # 4. parametre renk
                              # 5. parametre kalınlık
                              cv2.circle(img,(x,y), 50, (255,0,0), -1)
               print(x,y)
               """
               # eğer global olarak atamazsak ifadeyi değiştiremeyiz (?)
               global cizim, xi, yi

               # 1- sol tıklama eventi lazım, 2. mouse hakeret eventi lazım, 3- tıklanmayı sonlandıran event lazım

               if event == cv2.EVENT_LBUTTONDOWN:
                              xi, yi = x, y
                              cizim = True

               elif event == cv2.EVENT_MOUSEMOVE:
                              if cizim == True:
                                             if mod:
                                                            cv2.circle(img,(x,y), 10, (100,50,0), -1)
                                             
                                             else:
                                                            cv2.rectangle(img,(xi,yi), (x,y), (0,0,255), -1)
                              else:
                                             pass

               elif event == cv2.EVENT_LBUTTONUP:
                              cizim = False
                                             


img = np.ones((512,512,3), np.uint8)
cv2.namedWindow('paint')
cv2.setMouseCallback('paint', draw)

"""
NOT : Pencere isimlerinin aynı olması onları aynı yapıyor (?)
"""
while (True):
               cv2.imshow("paint", img)
               if cv2.waitKey(1) & 0xFF == ord('q'):
                              break
               # m klavyeden m ye basmayı algılar m ye basarsa false olur
               if cv2.waitKey(1) & 0xFF == ord("m"):
                              # mod tersine dönüyor
                              mod = not mod

cv2.destroyAllWindows()