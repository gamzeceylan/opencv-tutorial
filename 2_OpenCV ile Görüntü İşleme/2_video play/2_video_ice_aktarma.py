"""
- video resimleirn hızlı bir şekilde içe aktarılmasıdır.
- resimler hızla aktarılarak video oluşur.
"""

import cv2
import time
video_name = "MOT17-04-DPM.mp4"

# videoyu içe aktarmak capture diye geçer ve cap diye kısaltılır

cap = cv2.VideoCapture(video_name) # içe aktarma
# böyle bir video olmasa da cap'e yükler ve boş gözükür kontrolunun yapılması gerek

# cap 3. parametre -> genişlik
# cap 4. parametre -> yükseklik
# genişlik * yükseklik = pixel

print("Genişlik: ", cap.get(3))
print("Yükseklik: ", cap.get(4))

# cap açılıp açılmadığının kontrolu
if cap.isOpened() == False:
        print("hata")


# videoyu okuma -> read
"""
- read iki şey döner. 1. si return, 2. si frame
- frame her bir resim demektir. 
- return da bu işlemin başarılı olup olmadığıdır
"""

ret, frame = cap.read()

# video bitene kadar ya da biz çıkana kadar videoyu göster 
while True:
    if ret == True:
        time.sleep(0.01) # kullanmazsak çok hızlı akar
        cv2.imshow("video", frame)
        
    else: break # video bittiyse
    
    if cv2.waitKey(1) & 0xFF == ord("q"): # kendi isteğimizle çıkmak
        break
    

# video almayı, yakalmayı bırak ve pencereleri kapat
cap.release() # stop capture
cv2.destroyAllWindows() # tüm pencereleri serbest bırakma











