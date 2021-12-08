"""
- resimleri for döngüsü ile toplu olarak içe aktaralım
"""

import cv2
import os

files = os.listdir()
print(files)

img_path_list = []
for f in files:
    if f.endswith(".jpg"):
        img_path_list.append(f)
        
print(img_path_list)

for i in img_path_list:
    print(i)
    image = cv2.imread(i)
    
    
    # yüz tespiti
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    detector = cv2.CascadeClassifier("haarcascade_frontalcatface.xml")
    rects = detector.detectMultiScale(gray, scaleFactor = 1.045, minNeighbors = 2)
    """
    - scaleFactor resmin üzerinde ne kadar zoom yapacağını belirleyen bir katsayı
    - scaleFactor :
        Her görüntü ölçeğinde görüntü boyutunun ne kadar küçültüleceğini belirten parametre.
        Temel olarak, ölçek faktörü, ölçek piramidinizi oluşturmak için kullanılır. 
        Daha fazla açıklama, modelinizin eğitim sırasında tanımlanmış ve XML'de görünen sabit 
        bir boyutu vardır. Bu, varsa yüzün bu boyutunun görüntüde algılandığı anlamına gelir. 
        Bununla birlikte, giriş görüntüsünü yeniden ölçeklendirerek, daha büyük bir yüzü daha 
        küçük bir yüze yeniden boyutlandırabilir ve algoritma tarafından algılanabilir 
        hale getirebilirsiniz.
    """
    
    # rect resmin üzerine koyma
    """
    - i indexi alır
    """
    for (i, (x,y,w,h)) in enumerate(rects):
        cv2.rectangle(image, (x,y), (x+w, y+h),(0,255,255),2)
        cv2.putText(image, "Kedi {}".format(i+1), (x,y-10),cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0,255,255),2)
 
    
    
    cv2.imshow("kedi", image)
    # q ya bastıkça resimler arasında gezelim
    if cv2.waitKey(0) & 0xFF == ord("q"): continue


















