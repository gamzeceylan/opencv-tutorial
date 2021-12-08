import cv2
import matplotlib.pyplot as plt
import numpy as np

# resmi içe aktar
img = cv2.imread("contour.jpg",0)
plt.figure(), plt.imshow(img, cmap = "gray"), plt.axis("off")

"""
- kontur tespiti içi findContours metodu kullanılır
- RETR_CCOMP internal ya da external olarak  konturleri extract edeceğimizi gösterir
- şuan iç ve dış konturlerin ikisinide bulacak
- CHAIN_APPROX_SIMPLE yatay dikey ve çapraz bölümleri sıkıştırmamızı sağlar yalnızca uç noktaları bırakır
- findContours iki çıkıtısı vardır. 1 contours 2 hierarch (iç ve dış konturler için)
"""
contours, hierarch=cv2.findContours(image=img, mode=cv2.RETR_CCOMP, method=cv2.CHAIN_APPROX_SIMPLE)

external_contour = np.zeros(img.shape)
internal_contour = np.zeros(img.shape)

for i in range(len(contours)): # len conturlerin uzaklıkları
    
    # external
    if hierarch[0][i][3] == -1: # bu external. 255: renk, -1: kalınlık->konturlerle sınırlı alanı doldur anlamına gelir
        cv2.drawContours(external_contour,contours, i, 255, -1)
    else: # internal
        cv2.drawContours(internal_contour,contours, i, 255, -1)


plt.figure(), plt.imshow(external_contour, cmap = "gray"),plt.axis("off")
plt.figure(), plt.imshow(internal_contour, cmap = "gray"),plt.axis("off")
