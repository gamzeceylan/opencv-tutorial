"""
- aşağıdakiler noise azaltma yöntemleridir
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

# resmi içe aktar
img = cv2.imread("datai_team.jpg", 0)
plt.figure(), plt.imshow(img, cmap="gray"), plt.axis("off"), plt.title("original img")

##### erozyon -> sınırları küçültme
"""
- bir kutucuk belirliyoruz -> kernel
- sınırları küçültücez. bu kernel resim üzerinde dolaşıcak ve dolaşırken sınırları küçültücek

"""
kernel = np.ones((5,5), dtype = np.uint8) # np.uint8 -> integer
"""
- erode -> erozyon fonksiyonu
- iterations: erozyonun kaç kere yapılacağının sayısı. arttıkça 
daha çok knarlar yok olur
"""
result = cv2.erode(img, kernel, iterations=2)
plt.figure(), plt.imshow(result, cmap="gray"), plt.axis("off"), plt.title("erozyon img")

##### genişleme(dilation)
result2 = cv2.dilate(img, kernel, iterations=1)
plt.figure(), plt.imshow(result2, cmap="gray"), plt.axis("off"), plt.title("dilate img")

##### açılma
"""
- açılma beyaz gürültüyü azaltmak için kullanılır
- o yüzden önce beyaz gürültü oluşturalım
- acilma erozyon ve genişlemenin artarda uygulanmasıydı.
- erosyon beyazlıkları azaltıyordu ve yok ediyordu e böyle olunca da
resim küçülüyordu
- orjinal resmi geri elde etmek için genişleme kullanıyoruz
"""
whiteNoise = np.random.randint(0,2, size=img.shape[:2]) # normalize whitenoise elde ederiz. 0 ve 1 lerden oluşur
whiteNoise = whiteNoise*255 # istediğimiz skalaya çıkardık
plt.figure(), plt.imshow(whiteNoise, cmap="gray"), plt.axis("off"), plt.title("whiteNoise img")

noise_img = img + whiteNoise # gürültüyü resme ekledik. toplama için ikisi de aynı boyutta olmalı. resmi siyah beyaz yaparsak üç kanallı olmaktna çıkar. ürettiğimiz siyah beyazz noktalarda tek kanallıdır
plt.figure(), plt.imshow(noise_img, cmap="gray"), plt.axis("off"), plt.title("img with whitenoisy")

# açılma ile noise ortadan kaldıralım
opening = cv2.morphologyEx(src=noise_img.astype(np.float32), op=cv2.MORPH_OPEN, kernel=kernel)
plt.figure(), plt.imshow(opening, cmap="gray"), plt.axis("off"), plt.title("acilma")

#### kapatma
"""
- kapatmayı yapabilmek için noisy'e ihtiyac var. bu sefer de black noisy elde edelim
- kapama da önce genişletiyo sonra erozyonla daraltıp orjinal resmi elde ediyor
"""
# black noisy elde etme
blackNoise = np.random.randint(0,2, size=img.shape[:2]) # normalize whitenoise elde ederiz. 0 ve 1 lerden oluşur
blackNoise = blackNoise*-255 # whiteNoise de yazdığımıza - eklerdek blackNoise elde edermişiz???
plt.figure(), plt.imshow(blackNoise, cmap="gray"), plt.axis("off"), plt.title("blackNoise img")

# blackNoise'ı resme ekleme
black_noise_img = blackNoise + img
black_noise_img[black_noise_img <= 245] = 0
plt.figure(), plt.imshow(black_noise_img, cmap="gray"), plt.axis("off"), plt.title("black_noise_img")
# resimde dikkat edersen renk kanalında siyak yerlerde 0 yazıyor pixellerde

# kapatma
closing = cv2.morphologyEx(src=black_noise_img.astype(np.float32), op=cv2.MORPH_CLOSE, kernel=kernel)
plt.figure(), plt.imshow(closing, cmap="gray"), plt.axis("off"), plt.title("kapama")

#### morfolojik gradyaan
"""
- genişleme ile erosyon arasındaki farkı alır
- neden yapıyoruz? kenar testpitinin en temel yöntemlerinden biridir.
dikkat edersen sadce harflerin kenarları kalır
"""
gradient = cv2.morphologyEx(img, op=cv2.MORPH_GRADIENT, kernel=kernel)
plt.figure(), plt.imshow(gradient, cmap="gray"), plt.axis("off"), plt.title("gradyan")



















