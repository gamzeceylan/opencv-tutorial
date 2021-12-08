"""
- önce ronaldo yüzünü bulucaz. yüz tespiti
- sonra yüzün kamera ile takip işlemi. (hoca kamerayı bilgisayara tutuyor)
- eğer yüz tespitini while içinde yazsaydık bu tespit algoritması olurdu. takip işlemini while de yazıyoruz. 
çünkü bu bir takip algoritması
- ve kamera açıldığı gibi ronaldoyla başlayacak
"""
import cv2


# kamera aç
cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture(0)
cap.set(3, 640) # width
cap.set(4, 480) # height

# bir tane frame oku
ret, frame = cap.read()

# uyarı
"""
- ilk yüz göremezse nesne tespiti yapamaz, takip algoritmasını başlatamaz ve program hata verir
"""
if ret == False:
    print("Uyarı")
    
# detection
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")    
face_rects = face_cascade.detectMultiScale(frame)

(face_x, face_y, w, h) = tuple(face_rects[0]) # rect bir tuple dir
track_window = (face_x, face_y, w, h) # meanshift algoritması girdisi
"""
- takip algoritması yukarıda girdiğimiz nesnenin konumuna göre track windowu başlatıcak
"""


# region of interest -> tespit edilen kutu içerisi (şuan yüz)
roi = frame[face_y:face_y + h, face_x : face_x + w] # roi = face

hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

# hsv roinin histogramını hesaplamamız gerek
"""
- çükü birazdan takip için back prjection yapıcaz. bunun için de histogramlar gerekli
"""
roi_hist = cv2.calcHist([hsv_roi],[0],None,[180],[0,180]) # takip için histogram gerekli

# histogramı normalize edelim
cv2.normalize(roi_hist , roi_hist ,0 ,255, cv2.NORM_MINMAX)


# takip algoritması (yineleme algoritması) icin gerekli durdurma kriterleri
# count = hesaplanacak maksimum oge sayısı
# eps = degisiklik
term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 5, 1)

# takibe başlıyoruz
while True:
    
    ret, frame = cap.read()
    
    if ret:
        
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        
        # histogramı bir goruntude bulmak için kullnıyoruz
        # piksel karşılaştırma
        """
        - arka projeksiyon için bir özelliğin histogram modelini hesaplıyor
        ve ardından bu özelliği bir görüntüde bulmak için kullanıyoruz
        böylece eşleme gerçekleşiyor ve takip yapılıyor
        """
        dst = cv2.calcBackProject([hsv], [0], roi_hist, [0,180],1)

        ret, track_window = cv2.meanShift(dst, track_window, term_crit) # track winfodw takip penceresi
        """
        - tarck window takip ettiği için nesnenin yeni konumunu döndürecek ve genişlik 
        yükseklik değerleini döndürecek
        """

        x,y,w,h = track_window
        
        img2 = cv2.rectangle(frame, (x,y), (x+w, y+h),(0,0,255),5)
        
        cv2.imshow("Takip", img2)
        
        if cv2.waitKey(1) & 0xFF == ord("q"): break
            
cap.release()
cv2.destroyAllWindows()
        


























