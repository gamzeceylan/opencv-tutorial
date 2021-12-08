# resim nedir, kamera işlemleri, video işlemleri

import cv2
import numpy as np

#-- resim nedir --
# zeros oluşturulan matrisi siyah gösterir.
# ones olarak oluşturduklaırn beyaz olrak oluşur.
# 100x100 görüntü açarsın her biri 1 sayısından oluşur
# istersen 500x500 görüntü aç

"""
sifir = np.zeros([100,100])
# cv2.imshow("sifir",sifir)

bir = np.ones([100,100])

cv2.namedWindow("sifir", cv2.WINDOW_FREERATIO)
cv2.imshow("sifir",sifir)

cv2.namedWindow("ones", cv2.WINDOW_FREERATIO)
cv2.imshow("ones",bir)

cv2.waitKey(0)
"""

#-- kameradan görüntü alma --
# bir videoda saniyede x kadar görüntü vardır
# bu resimler arka arkaya tekrar ettiğinde ise hareketliymiş gibi bir görüntü oluşur
# buna da video denir.
# kamera işlemlerinde ise bu yüzden bir döngüye koyarak resim alırız. yani kameradan resim çekeriz
# 0 kendi kameramız. 1, 2 şeklinde arttırarak harici kameraları da kullanabilirsin.

# kameradan 2 değer döner. biri ret diğeri frame
# ret true ya da false döndürür. kameradan değerin okunup okunamadığıyla ilgilidir.
# frame ise bir önceki derste resim gibi. görüntünün gösterildiği yer. buna imshow da isim de verirsin
"""
cam = cv2.VideoCapture(0)
while True:

               ret, frame = cam.read()
               
               if not ret:
                              print("Kameradan görüntü okunamıyor")

               # her okuduunda burası döner
               elif ret:
                              print("kameradan görüntü okunabiliyor")
               
               # kameradan alınan resimleri gösterme
               cv2.imshow("kamera", frame)

               # 1 e basarsan değil. 1 sanırım q nun ascii değeri için yazılıyor. & da çarpma işlemi yapıyor.
               # yani q ya basarsan kapanır
               # bunu mutlaka yazmalısın.
               if cv2.waitKey(1) & 0xFF == ord("q"):
                              print("Görüntü sonlandı")
                              break

# koddan çıksan bile arka planda kameran açık kalır. bunu kapatmak için relaese kullnırız.
# destroyAllWindows da tüm pencereleri kapatır
cam.release()
cv2.destroyAllWindows()

"""
"""
cam = cv2.VideoCapture(0)

# eğer kamera açılmazsa ve direkt döngüye girerse hata verir.
# eğer kamera açılmazsa buraya girer
if not cam.isOpened():
               print("Kamera tanınmadı")
               exit()  # koddan çıksın. alta devam etmesin diye yoksa hata mesajı yazar
               

while True:

               ret, frame = cam.read()
               
               if not ret:
                              print("Kameradan görüntü okunamıyor")

               else:
                              print("kameradan görüntü okunabiliyor")
               

               cv2.imshow("kamera", frame)

               if cv2.waitKey(1) & 0xFF == ord("q"):
                              print("Görüntü sonlandı")
                              break


cam.release()
cv2.destroyAllWindows()
"""

#-- renk değiştirme --
# cvtcolor ile renk değiştiririz.
# BGR2 ile çünkü open.cv bgr olarak okur
"""
cam = cv2.VideoCapture(0)
while True:

               ret, frame = cam.read()

               frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

               cv2.imshow("kamera", frame)

               if cv2.waitKey(1) & 0xFF == ord("q"):
                              break


cam.release()
cv2.destroyAllWindows()
"""

#-- kamera özellikleri --
# opencv tutorial a git videocaptuare properties yaz get i ordan da propID yi bul
# get içine 0, 1, 2, 3 gibi şeyler yazabilirsin.
# tutarial da bunların ne anlama geldiğini görebilirsin.
# set ile de değiştirebilirsin
"""
cam = cv2.VideoCapture(0)

# ya da bu şekilde alabilirsin
# get = cam.get(cv2.CAP_PROP_FRAME_WIDTH)
# print(get)

print(cam.get(3))  # genişlik
print(cam.get(4))  # boy

# verdiğimiz boyutlarda görüntü elde ederiz
cam.set(3,320)
cam.set(4,240)

print(cam.get(3))  
print(cam.get(4))

while True:

               ret, frame = cam.read()

               frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

               cv2.imshow("kamera", frame)

               if cv2.waitKey(1) & 0xFF == ord("q"):
                              break

cam.release()
cv2.destroyAllWindows()
"""

#-- video görüntüleme --
# yine ilk olarak kamera tanımlıyacaksın ve okuacağın videonun yolunu vericeksin
"""
cam = cv2.VideoCapture("video.mp4")

while cam.isOpened():
               ret, frame = cam.read()

               cv2.imshow("video",frame)


               if cv2.waitKey(1) & 0xFF == ord("q"):
                              print("Gröüntü kapatıldı")
                              break

# videodan da çıkmalısın kamera gibi
cam.release()
cv2.destroyAllWindows()
"""

#-- video kayit etme --
# yine kameranı açıcaksın
# görüntü çekmek için de codec(?) işlem gerekiyor

cam = cv2.VideoCapture(0)

# bu dört parametreye M J P G verirsen video formatına ulaşmış olursun
#fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
# ama yukarıdakinin yerine windows ta aşağıdakini kullan ?
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# codec i oluşturduktan sonra boş bir şablon oluşturup içine aldığın görüntüyü yazmalısın
# 1. parametre oluşan görüntünün ismi, 2. codec, 3. ? , 4. görüntünün boyutlandırması
# burası boş şablon
out = VideoWriter("okunanVideo",fourcc, 30.0, (640, 480))

while cam.isOpened():
               ret, frame = cam.read()

               if not ret:
                              print("Görüntü alınamıyor")
                              break

               # boş sablona da yazmamıs gerekiyor.
               out.write(frame)
               # görüntüyü gösterme
               cv2.imshow("kamera", frame)
               if cv2.waitKey(1) == ord('q'):
                              print("Videodan ayrıldınız")
                              break

cam.release()
out.relaese()
cv2.destroyAllWindows()

# yukarısı hata verioy sebebini anlamadım