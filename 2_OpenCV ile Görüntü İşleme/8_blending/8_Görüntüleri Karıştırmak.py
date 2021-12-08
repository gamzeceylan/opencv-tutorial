"""
- opencv default olarak resimleri bgr yükler 
- yani direkt yüklersen orjinal resimler rgb olduğu için renkler değişir
- bunu düzeltmenin yolu renk skalasını değiştirmektir

- birleştirdiğimiz resim boyutları aynı olmak zorunda. çünkü bir yerde matris
topluyoruz. 

"""

import cv2
import matplotlib.pyplot as plt # görselleştirme için

img1 = cv2.imread("img1.jpg")
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB) # renk skalasını değiştirme
img2 = cv2.imread("img2.jpg")
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

plt.figure()
plt.imshow(img1)

plt.figure()
plt.imshow(img2)


# boyutları kontrol edelim
print(img1.shape)
print(img2.shape)

# boyutları ayarlama
img1 = cv2.resize(img1, (600, 600))
img2 = cv2.resize(img2, (600, 600))
print(img1.shape)
print(img2.shape)
"""
- acaba yeniden boyutlandırma nasıl yapılıyor???
"""
plt.figure()
plt.imshow(img1)

plt.figure()
plt.imshow(img2)

# birleştirme
"""
- karıştırılmış resim = alpha katsayısı*img1 + beta kat sayısı*img2
- alpha ve beta resimlerden ne kadar alacağın ile ilgilidir. ister 1 yap ister 0.1
"""
blended = cv2.addWeighted(src1=img1, alpha=0.5, src2=img2, beta=0.5, gamma=0)
plt.figure()
plt.imshow(blended)


cv2.waitKey(0)
cv2.destroyAllWindows()



