import cv2
import matplotlib.pyplot as plt


# ana görüntüyü içe aktar
chos = cv2.imread("chocolates.jpg", 0)
plt.figure(), plt.imshow(chos, cmap = "gray"),plt.axis("off")

# aranacak olan görüntü
cho = cv2.imread("nestle.jpg", 0)
plt.figure(), plt.imshow(cho, cmap = "gray"),plt.axis("off")


# orb tanımlayıcı: görüntü ve aradğımız nesne arasındaki anahtar noktaları tespit eder
# köşe-kenar gbi nesneye ait özellikler
orb = cv2.ORB_create()


# her iki görüntüye ait anahtar nokta tespiti
# kp = keypoint des = descriptor, anahtar noktaları ve tanımlayıcıları hesaplar.
kp1, des1 = orb.detectAndCompute(cho, None)
kp2, des2 = orb.detectAndCompute(chos, None)

# bf matcher
bf = cv2.BFMatcher(cv2.NORM_HAMMING)
# noktaları eşleştir
matches = bf.match(des1, des2)

# mesafeye göre sırala
matches = sorted(matches, key = lambda x: x.distance)

# eşleşen resimleri görselleştirelim
plt.figure()
img_match = cv2.drawMatches(cho, kp1, chos, kp2, matches[:20], None, flags = 2)
plt.imshow(img_match), plt.axis("off"),plt.title("orb")
"""
- kullandığımız yöntem ve orb tanımlayıcısı ile güzel sonuçlar elde edemiyoruz.
- bir de sift tanımlayıcısı ile deneyelim. sift orb ye göre biraz daha iyi çalışır
- sift opencv de kullanılan bir kütüphende olmasına rağmen dışarıdan entegre edilmiştir
- pip install opencv-contrib-python --user yazdığında otomatik eklenmiş olacak.
"""

# sift
sift = cv2.xfeatures2d.SIFT_create()

# bf
bf = cv2.BFMatcher()

# anahtar nokta tespiti sift ile
kp1, des1 = sift.detectAndCompute(cho, None) # none: maskeleme yok
kp2, des2 = sift.detectAndCompute(chos, None)

matches = bf.knnMatch(des1, des2, k = 2) # knnMatch: en yakın komşu

guzel_eslesme = [] # güzel eşleşmeleri alıcaz. 

for match1, match2 in matches:
    
    if match1.distance < 0.75*match2.distance: # tersi kötü eşleşmedir ama onları tutmuyoruz
        guzel_eslesme.append([match1])
    
plt.figure()
sift_matches = cv2.drawMatchesKnn(cho,kp1,chos,kp2,guzel_eslesme,None, flags = 2)
plt.imshow(sift_matches), plt.axis("off"), plt.title("sift")

"""
- benim sürüm sift i desteklemiyor geçtim uğraşmadım. ama sift
daha iyi tespit ediyor
- bulunan ekstra çikolatalrı elimine edebilirdik ve algoritmayı öyle çalıştırdığımızda daha başarılı olurdu
"""











