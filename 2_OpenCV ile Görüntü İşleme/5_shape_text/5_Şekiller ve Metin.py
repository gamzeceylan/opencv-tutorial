"""
- şekil ve meitn çizme

"""
import cv2
import numpy as np

# kendimiz siyah resim oluşturalım
"""
- pixel genliği 0 sa siyah resim. 1 olsaydı beyaz resim
- 512x512 lik resim ve np.uint8 -> siyahlar integer
"""
img = np.zeros((512,512,3), np.uint8)
print(img.shape)
cv2.imshow("Siyah", img)

# çizgi çizme
"""
- (resim, baslangıç nok, bitiş nok, renk, kalınlık)
- yeşil çizdik. bgr a göre yapılır
"""
cv2.line(img, (100,0), (200,300), (0,255,0), 3)
cv2.imshow("cizgi", img)

# dikdorgen çizme
cv2.rectangle(img, (20,20), (250, 250), (255,0,0))
cv2.imshow("dikdortgen", img)

# doldurulmuş
cv2.rectangle(img, (20,20), (250, 250), (255,0,0), cv2.FILLED)
cv2.imshow("doludikdortgen", img)

# cember
cv2.circle(img, (300,300),45,(0,0,255))
cv2.imshow("cember", img)

# daire
cv2.circle(img, (300,300),45,(0,0,255), cv2.FILLED)
cv2.imshow("daire", img)

# metin
"""
- org : nereye koyucaksın
"""
cv2.putText(img, "yazi yaz", (350, 350), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255))
cv2.imshow("metin", img)


cv2.waitKey(0)
cv2.destroyAllWindows()






