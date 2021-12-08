# kameradan veri toplama ve dosyaya kaydetme
"""
- veriyi asıl toplamak için nesnenin arkasına beyaz kağıt koy ve her açıdan çek
- negatif resim de aynı şekilde topla. alakasız bir nesne çek
- çok veri olursa eğitim süresi uzar.
- images0 -> n
- images1 -> p
- https://amin-ahmadi.com/cascade-trainer-gui/ cascade programını indirme siztesi
"""

"""
1) (önce veri seti oluşturucaz) veri seti:
    n (negatif resimler), p (pozitif resimler-> tespit etmek istediğin)
2) cascade programı indir
3) (sonra cascade oluşturucaz) cascade oluştur. cascade programı türkçe karakter sevmez
4) cascade kullanarak tespit algoritması yaz
"""

import cv2
import os

# resim depo klasörü
path = "images" # verileri depoladığımı zklasör

# resim boyutu
imgWidth = 180
imgHeight = 120

# video capture
cap = cv2.VideoCapture(0)
cap.set(3, 640) # kamera genişliği
cap.set(4, 480) # kamera yüksekliği.. kamera 640x480 piksel
cap.set(10, 180) # aydınlık seviyesi

# klasor oluşturma (images klasörü oluştuur)
global countFolder
def saveDataFunc():
    global countFolder
    countFolder = 0 # klasor yok q
    while os.path.exists(path + str(countFolder)):
        countFolder += 1
    os.makedirs(path+str(countFolder))

saveDataFunc()

count = 0
countSave = 0

while True:
    
    success, img = cap.read()
    
    if success:
        
        # kamerasnın nasıl okuyacağını bilmiyoruz. o yüzden resimleri boyutlandırmamız gerekir
        img = cv2.resize(img, (imgWidth, imgHeight))
        
        if count % 5 == 0: # her resmi almaısın, aynı görüntüyü depolamasın beş tanede bir depolasın yeter
            cv2.imwrite(path+str(countFolder)+"/"+str(countSave)+"_"+".png",img)
            countSave += 1
            print(countSave)
        count += 1
        
        cv2.imshow("Image",img)
    if cv2.waitKey(1) & 0xFF == ord("q"): break

cap.release()
cv2.destroyAllWindows()

















