"""
- veri setini bul (ok)
- veri seti işleyebilmek için indir (ok)
- indirdikten sonra resimleri videota çevir. resim2video (ok)
- keşifsel veri analizi. eda
- sonra takip edeceğimiz obgeje aiy ground truth u çıkarıtcaz. gt


* kullanacağımız veri seti: https://motchallenge.net/data/MOT17/
içinde resimler var. ama zaten video da resimlerden oluşuyor
"""

import cv2
import os
from os.path import isfile, join
import matplotlib.pyplot as plt

pathIn = r"img1" # r -> read
pathOut = "MOT17-13-SDP.mp4"

files = [f for f in os.listdir(pathIn) if isfile(join(pathIn,f))] # files içine resimleri aldık

# img = cv2.imread(pathIn + "\\"+files[44]) # imread içine parh vermezsen hata alırsın. sadece files[44] hatadır
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# plt.imshow(img)

fps = 25 # frame per second. veriyi aldığımız yerde yazıyordu
size = (1920,1080) # yine veri setinde yazıyordu ama bunu kendimiz de öğrenebiliriz
out = cv2.VideoWriter(pathOut, cv2.VideoWriter_fourcc(*"MP4V"), fps, size, True)

"""
- files içinde resimlerin adları vardı ama bizim path ile almamız gerekir
"""
for i in files:
    print(i)
    
    filename = pathIn + "\\" + i
    
    img = cv2.imread(filename)
    
    out.write(img)

out.release()

"""
- bu kod çalıştırğında resimler okunacak ve frameler bir MOT17-13-SDP.mp4 içine
yazılmış olunacak. ve kaydedilecek
"""


















