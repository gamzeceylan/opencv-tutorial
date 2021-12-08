"""
- şimdilik burada hazır eğitilmiş model kullanıcaz.
- nesne tespitinde kullanılan farklı cascade ler vardır. örn gözleri,
yüzü, body, plaka tespiti için ayrı ayrı cascade ler varıdr
- githubtan haar cascade reposuna gidelim
https://github.com/opencv/opencv/tree/master/data/haarcascades

"""

import cv2
import matplotlib.pyplot as plt

#%% einstein
# içe aktar 
einstein = cv2.imread("einstein.jpg", 0)
plt.figure(), plt.imshow(einstein, cmap = "gray"), plt.axis("off")


# sınıflandırıcı
"""
- buradaki sınıflandırıcı einstein'ı tanımaz sadece orada bir yüz olup olmadığını görür
- bu da pozitif ve negartif resimlerin eğitilmesi sonucu elde edilir

"""
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
face_rect = face_cascade.detectMultiScale(einstein)
"""
- face_rect içinde koordinatlar, genişlik, yükseklik değerleri var
- einstein resmi içinde yüzü bulup kutu içine aldığı kısım

"""
for (x,y,w,h) in face_rect:
    cv2.rectangle(einstein, (x,y),(x+w, y+h),(255,255,255),10)

plt.figure(), plt.imshow(einstein, cmap = "gray"), plt.axis("off")



#%% barcelona
# barce
# içe aktar 
barce = cv2.imread("barcelona.jpg", 0)
plt.figure(), plt.imshow(barce, cmap = "gray"), plt.axis("off")

face_rect = face_cascade.detectMultiScale(barce, minNeighbors = 7)
"""
- eğer detectMultiScale parametrelerini vermezsen çoğu şeyi yanlış bulur.
- bu parametreleri araştırırsın.
"""

for (x,y,w,h) in face_rect:
    cv2.rectangle(barce, (x,y),(x+w, y+h),(255,255,255),10)
plt.figure(), plt.imshow(barce, cmap = "gray"), plt.axis("off")



#%% video
cap = cv2.VideoCapture(0)

while True:
    
    ret, frame = cap.read()
    
    if ret:
        
        face_rect = face_cascade.detectMultiScale(frame, minNeighbors = 7)
            
        for (x,y,w,h) in face_rect:
            cv2.rectangle(frame, (x,y),(x+w, y+h),(255,255,255),10)
        cv2.imshow("face detect", frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"): break

cap.release()
cv2.destroyAllWindows()

























