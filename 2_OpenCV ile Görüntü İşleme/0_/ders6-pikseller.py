# pikseller

import cv2

resim = cv2.imread('foto.jpg')

# resmin kanallarını görme
k = resim.shape
print(k)

# resmin 100-100 olan koordinatındaki pikselere erişme
px = resim[100,100]
print(px)
print(type(px))
# px in içinde 3 değeri olan bir array vardır tipi de uint8
# 3 değerin olması renkli bir görüntü olduğu anlamına gelir
# opencv ile çalıştığımız için bgr olarak okunuyor
# yani sayı kodları mavi-yeşil-kırmızı


# yani rnekli resimler mavi yeşil ve kırmızı kanallardan oluşur
# ve 0-1-2 dite sıralanırlar. bildiğin liste mantığı
px_blue = resim[100,100,0]
print(px_blue)
# 0 veridimizde mavi, 1 verdiğimizde yeşil, 2 veridiğimizce mevi kanalı döner


# pixselin mavi rengini dğiştirelim
resim[100,100,0] = 2
px_blue = resim[100,100,0]
print(px_blue)

# pixelin rengini değiştirelim
resim[100,100] = [255,255,255]


# resmin boyutunu görme
print(resim.size)

# resmin türü
print(resim.dtype)
