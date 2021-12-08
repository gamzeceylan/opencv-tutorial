import cv2
import numpy as np
from collections import deque
"""
- tespit ettiğimiz objenin merkezini depolamak için deque kullanıcaz
"""

buffer_size = 16 # deque boyutu
pts = deque(maxlen = buffer_size) # pts = points

"""
- mavi rengini tespit edelim
- renk testpiti için bir aralık belirlememiz gerekir. low ve upper belirle
- bu aralıkları hsv formatında belirlicez

"""

# mavi renk aralığı (hsv ye göre)
blueLower = (84, 98, 0) # ton, doygunluk, parlaklık
blueUpper = (179, 255, 255)

# capture -> kameradan görüntü alma
cap = cv2.VideoCapture(0)
cap.set(3, 960) # kamera genişliği
cap.set(4, 460) # kamera yüksekliği

while True:
    success, imgOriginal = cap.read()
    
    """
    - buraya bir kontrol yazmazsan ve kameradan görüntü alınamazsa
    python hata vermez ve sen olmayan bir görüntü ile işlemlerini yapmaya çalışırsın
    """
    
    if success: 
        """
        - önce elimizdeki frame leri blur yapıcaz 
        - sonra noise ları elimine etmeye çalışıcaz
        """
        
        # blur
        blurred = cv2.GaussianBlur(imgOriginal, (11,11), 0) 
        
        
        # hsv
        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
        cv2.imshow("HSV Image",hsv)  # şuan kameradan renkleri hsv formatında görüyoruz
        
        # mavi için maske oluştur -> mavi renginin tespiti burada yapılır
        mask = cv2.inRange(hsv, blueLower, blueUpper)
        cv2.imshow("mask Image",mask)
        """
        - şuan yukarıdaki kodda kameradna mavi bir şey görürsen onu tespit edioyr
        - ama görüntüde noise'lar var. maskeleme tam olarak yapılamıyor
        - bunun için erosyon ve genişlmeyi arka arkaya yapıp gürültülerden arındıralım
        """
        
        # maskenin etrafında kalan gürültüleri sil
        mask = cv2.erode(mask, None, iterations = 2)
        mask = cv2.dilate(mask, None, iterations = 2)
        cv2.imshow("Mask + erozyon ve genisleme",mask)
        

        # konturleri bulma
        (contours,_) = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        center = None # ilerleyen yerlerde nesnenin merkezi olacak

        if len(contours) > 0: # demekki bir şeyler bulduk
            
            # en büyük konturu al. çünkü bir mavi cisim içinde küçük mavilikler olabilir. oraları alamsın gerek yok. tüm nesneyi kaplasın
            c = max(contours, key = cv2.contourArea)
            
            # dikdörtgene çevir 
            rect = cv2.minAreaRect(c) # c'yi kaplayacak min rectangle
            """
            - rect bir tuple dır. 
            1- resim üzerindeki x y koordinatları
            2- genişlik ve yükseklik
            3- rotasyon
            - yukarıdakileri aşağıdaki gibi ayıklıyoruz
            """
            ((x,y), (width,height), rotation) = rect
            
            s = "x: {}, y: {}, width: {}, height: {}, rotation: {}".format(np.round(x),np.round(y),np.round(width),np.round(height),np.round(rotation))
            print(s)
            
            # kutucuk oluşturma
            box = cv2.boxPoints(rect)
            box = np.int64(box)
            
            # görüntü momenti
            """
            - görüntü momenti bir görüntünün yarı çap, alan, ağırlık merkezi vb gibi 
            bazı belirli özelliklerini bulabileceğimiz göürntü pixel yoğunluklarının ağırlıklı 
            ortalamasıdır.
            - yani görüntünün merkezini bulmamıza yarayan yapı
            """
            M = cv2.moments(c) # içine en büyük conture'u yolluyoruz
            center = (int(M["m10"]/M["m00"]), int(M["m01"]/M["m00"]))
            
            # çizdirme işlemleri
            # konturu çizdir: sarı
            cv2.drawContours(imgOriginal, [box], 0, (0,255,255),2)
            
            # merkere bir tane nokta çizelim: pembe
            cv2.circle(imgOriginal, center, 5, (255,0,255),-1)  # -1 doldurur
            
            # bilgileri ekrana yazdır
            cv2.putText(imgOriginal, s, (25,50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,255,255), 2)
            
            """
            - yukarıda en büyük konturu bul dediğimiz için ekrana tuttuğun mavi cisimlerden sadece
            konturu en büyük olanı bulur. en büyük konturu bulma olayını değiştirirsen birden fazla nesneyi de tespit edebilirsin
            
            """
            
            
        # tespit ettikçe geçmişi hatırlayan takip algoritması 
        # deque
        """
        - nesneyi hareket ettirdikçe ekrana yeşil çizgi çizer.
        - buradan nesne nerede ve nereye gidiyor anlayabiliriz
        - geçmişte nerede tutuyoruz
        """
        pts.appendleft(center) # noktaları deque içine ekliyoruz
        
        for i in range(1, len(pts)): # noktaları orjinal görüntü içine ekliyoruz
            
            if pts[i-1] is None or pts[i] is None: continue
        
            cv2.line(imgOriginal, pts[i-1], pts[i],(0,255,0),3) # 
            
        cv2.imshow("Orijinal Tespit",imgOriginal)
        
    # aşağıdakini yazmazsan döngüden çıkamazsın
    if cv2.waitKey(1) & 0xFF == ord("q"): break
    
    
    








