"""
- perspektif değiştirebilmek neden önemli?
 iki tane 10 tl düşünelim biri düz duruyor diğeri 20derece yamuk.
 götünrü işleme ile düz duranı sınıflandırabilirken 20 derece yamuk duranı
 sınıflandıramayız. önce perspektifini düzeltmeliyiz
- çevirmek için Transform matrixlerini kullanıcaz
"""

import cv2
import numpy as np

"""
- önce boyut belirle, sonra köşeleri belirle
- köşeleri paint ile bulabilirsin. sol altta gösteriyor
- noktalar sol üstten başlar sol alt sağ üst sağ alt sırasıyla devam eder
"""

# içe aktar
img = cv2.imread("kart.png")
cv2.imshow("kart", img)

# boyut belirle
width = 400
height = 500

# noktaları belirle
"""
- pointleri float32 ile oluşturuyoruz??
"""
pts1 = np.float32([[230,1],[1,472], [540,150],[338,617]]) # yamuk resim köşeleri
pts2= np.float32([[0,0], [0, height],[width, 0], [width,height]]) # çevirmek istediğin köşeler

matrix = cv2.getPerspectiveTransform(pts1, pts2) 
# 1. noktadan 2. noktaya geçebilmek için oluşan matrix. 3x3 lük oldu??
# anlamadım ilerde bak buraya
print(matrix)

imgOutput = cv2.warpPerspective(img, matrix, (width, height))
cv2.imshow("donusturulmus", imgOutput)