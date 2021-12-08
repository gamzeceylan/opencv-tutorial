"""
- resim önce siyah beyaza çevrilir
- sonra kenarlar tespit edilmeye çalışır

"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

# resmi içe aktarma
img = cv2.imread("london.jpg", 0)
plt.figure(), plt.imshow(img, cmap="gray"), plt.axis("off")

# kenar tespiti
edges = cv2.Canny(image=img, threshold1=0, threshold2=255)
plt.figure(), plt.imshow(edges, cmap="gray"), plt.axis("off")

"""
- herhangi bir threshold kullanmazsan tüm kenarlar ortaya çıkar.
- ve nehrin içindeki suda girintili çıkıntılı olduğu için kenar gibi algılanır.
threshold kullanmazsan böyle istenmeyen yerler de tespit edilir
- threshold için en mantıklı değer mean veya medyan değeridir. medyan daha iyi sonuç 
verir
- alt ve üst threshold da medyan ya mean e göre belirlenir
"""

# median - mean
med_val = np.median(img)
print(med_val)

mean_val = np.mean(img)
print(mean_val)

# alt - üst threshold
"""
- literatürdeki hesaplamalar kullanılır

"""
low = int(max(0, (1-0.33)*med_val))
high = int(min(255, (1+0.33)*med_val))
print(low, high)

# kenar tespiti
edges = cv2.Canny(image=img, threshold1=low, threshold2=high)
plt.figure(), plt.imshow(edges, cmap="gray"), plt.axis("off")

"""
- kenar tespiti azalsa da yine de istediğimiz sonucu elde edemedik
hala sudaki kenarlar algılanıyor.
- bu detayı azaltmak için bluring işlemi uygulanır. ya sadece suya ya da tüm resme

"""

# blurlama işlemi (tüm resme) ve kenar bulma
blurred_img = cv2.blur(img, ksize=(4,4))
plt.figure(), plt.imshow(blurred_img, cmap="gray"), plt.axis("off")

med_val = np.median(blurred_img)
print(med_val)

low = int(max(0, (1-0.33)*med_val))
high = int(min(255, (1+0.33)*med_val))
print(low, high)


edges = cv2.Canny(image=blurred_img, threshold1=low, threshold2=high)
plt.figure(), plt.imshow(edges, cmap="gray"), plt.axis("off")

"""
- kernel arttırdıkça detaylar daha da azalıcağından istediğimiz kenarlar daha çok belirginleşir istemediklerimiz gider
"""








