"""
- gt.txt dosyasında her bir frame için o frame içinde bulunan her bir objeye ait kutu bilgileri
var. (x,y,genişlik,yükseklik). bunlar nesne tespitinden olan bilgiler.
- bu bilgilerin ne olduğuna mot17 dökümanından ulaşabilirsin 

- şimdi gt dosyasını içe aktarıcaz, içlerinden bir obje seçicez, üzerine bir kutu çizip
gt bilgisini çıkartıcaz
"""

import pandas as pd # veriyi içe aktarırken ve analiz yaparken kullanıcaz
import cv2
import numpy as np
import matplotlib.pyplot as plt # görselleştirme
import time
import seaborn as sns # görselleştirme kütüphanesi

"""
https://motchallenge.net/vis/MOT17-13-SDP/det/
https://arxiv.org/pdf/1603.00831.pdf
"""

# makale içindeki gt değerleirnin karşılığını yazıyoruz
col_list = ["frame_number","identity_number","left","top","width","height","score","class","visibility"]

data = pd.read_csv("gt.txt", names = col_list) # oluşturukacak veri içinde en üstte col_şist isimleri yazıcak

# veri içinde kaç class var?
plt.figure()
sns.countplot(data["class"])

car = data[data["class"] == 3] # makaleden bak. araçların class numarası 3


video_path = "MOT17-13-SDP.mp4"
cap = cv2.VideoCapture(video_path)

"""
- takip ettiğimiz zaman nesne gözden kaybolduğunda takibe devam ederiz sadece kutunun 
görünürlüğü düşer.

"""


id1 = 29 # takip etmek istediğimiz aracın identity number ı 29. videolardan görebilirsin
numberOfImage = np.max(data["frame_number"]) # 750
fps = 25
bound_box_list = []

for i in range(numberOfImage-1):
    
    ret, frame = cap.read()
    
    if ret:
        
        frame = cv2.resize(frame, dsize=(960,540))
        
        """
        - filter_id1 frame_number ve identity_number'a göre ilgili nesnemizi çekicek
        - yani 29 a ait olan aracın gt değerini çıkartmamıza yardım eder
        """
        filter_id1 = np.logical_and(car["frame_number"] == i+1, car["identity_number"]==id1)
        
        if len(car[filter_id1]) != 0: # yani doluysa
            
            x = int(car[filter_id1].left.values[0]/2)
            y = int(car[filter_id1].top.values[0]/2)
            w = int(car[filter_id1].width.values[0]/2)
            h = int(car[filter_id1].height.values[0]/2)
            
            
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
            cv2.circle(frame, (int(x+w/2),int(y+h/2)), 2, (0,0,255),-1)
            
            # frame, x, y, genis, yuksek, center_x, center_y
            bound_box_list.append([i, x,y,w,h,int(x+w/2),int(y+h/2)]) # merkezi eklemek istediğimiz için 2 ye bölüyoruz?
            
        cv2.putText(frame, "Frame num:"+str(i+1), (10,30), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,1,(0,0,255),2) # index 0'dan başladığı için frame_number her zaman i+1 olur
        cv2.imshow("frame", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"): break
    else: break # herhangi bir şey okuyamadıyssak

cap.release()
cv2.destroyAllWindows()        
  

# 29 nolu araca ait gt bir dosyaya yazdıralım yazdırma
df = pd.DataFrame(bound_box_list, columns = ["frame_no", "x", "y", "w", "h", "center_x", "center_y"])
df.to_csv("gt_new.txt",index=False)

"""
- arabanın etrafına çizdirdiğimiz kutu bitim ground truth bilgimizdir.

"""



























