import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("sudoku.jpg", 0)
img = np.float32(img) # neden?
print(img.shape)
plt.figure(), plt.imshow(img, cmap="gray"), plt.axis("off")


# harris corner detection
"""
- blocksize: komuşuk boyutu. kaç komşusuna bakıcaz?
- ksize: kernel size kutunun boyutu
- k: Harris detection daki parametrelerden birisi
"""
dst = cv2.cornerHarris(src=img, blockSize=2, ksize=3, k=0.04)
plt.figure(), plt.imshow(dst, cmap="gray"), plt.axis("off")

"""
- yukarıdaki köşeleri buldu ama çok belirgin değil
- köşeleri farklı şekilde görselleştirelim. (genişletme uygulayarak)
"""

dst = cv2.dilate(dst, None)
img[dst> 0.2*dst.max()] = 1 # anlamadım?? aşağıda görselleştirince beyaz bir şey oldu
plt.figure(), plt.imshow(dst, cmap="gray"), plt.axis("off")

plt.figure(), plt.imshow(img, cmap="gray"), plt.axis("off")

# shi tomsai detection algoritması
img = cv2.imread("sudoku.jpg", 0)
img = np.float32(img)
"""
- max corner: kaç kçşe istiyorsun? istediğin kadar yapabilirsin

"""
corners = cv2.goodFeaturesToTrack(image=img, maxCorners=100, qualityLevel=0.01, minDistance=10)
corners = np.int64(corners)

for i in corners:
    x,y = i.ravel()
    cv2.circle(img, (x,y), 3, (125,125,125), cv2.FILLED)

plt.imshow(img)
plt.axis("off")
"""
- toplamda 100 dediğimiz için bazı köşeleri tespit edemedi. arttırsan hepsini tespit eder
"""
    
    
    
    
    
    
    
    



