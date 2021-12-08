"""
- kamera açarak kendi verimizi toplama

"""

import cv2

# pixel sayısı
cap = cv2.VideoCapture(0) #bilgisayar kamerası. diğer kameralar 1,2,3...
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(width, height) # pixel = width*height

# frameleri okumadan video kaydı başlatalım
writer = cv2.VideoWriter("video_kaydı.mp4", cv2.VideoWriter_fourcc(*"DIVX"), 20, (width, height))
"""
- fourcc: windows için kullanılan çerçeveleri sıkıştırmak için kullanılan
dört karekterli codec kodu
- 20:(frame per second) video akış hızı, her saniyede göreceğimiz resim sayısı
- son parametre de çerçeve boyutu, video kaydedici boyutu
- yani biz writer'a atıyoruz o da .mp4 olarak kaydediyor
"""

# görselleştirme

while True:
    ret, frame = cap.read()
    cv2.imshow("video", frame)
    
    # save
    writer.write(frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"): break
    
cap.release() # cap'ı serbest bıraktık
writer.release() # writer'ı serbet bıraktık
cv2.destroyAllWindows() # tüm penceleri kapdık
# neden serbest bırakıyoruz nedennnnn?