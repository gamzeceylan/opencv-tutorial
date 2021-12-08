# renk kanalların ayırabilir miyiz ? 

import cv2

resim = cv2.imread('foto.jpg')

b, g, r = cv2.split(resim)
# print(b,g,r)

# bgr üzerinde tek tek işlem yapabiliriz.

# peki sonra eski haline nasil getiricez ?
# kanalları birleştirdik
resim2 = cv2.merge((b,g,r))


# split yavaş bir işlemdir
# ayrı ayrı renk uzaylarında çalışıcaksak 
# blue renk uzayını elde edelim
b = resim[:, :, 0] # yukarıdakinden daha hızlı

# bir renk kanalını kaldırma
# örneğin kırmızıyı kaldıralım
resim[:, :, 2] = 0

cv2.imshow("resim", resim)
cv2.waitKey(0)
cv2.destroyAllWindows()


# resme çerçeve ekleme 7. video 18:57