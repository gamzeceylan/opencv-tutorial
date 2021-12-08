# foto okuma, gösterme, kaydetme

"""
NOT : Resimler üç boyutlu birer matristir. 0 gray kodunu verirsen de iki boyutlu
bir matris oluşur. Yani renk 3. boyuttur. Bu ne demek araştır

"""
# import etmeden önce kütüphaneleri yükledik
import cv2
from matplotlib import pyplot as plt

#-- resim okuma --
# imread ile okunur.
# filename : dosya yolu.
# resim bir matristir ve rgb olarak okunur ve sayısal verilere dönüşür
resim = cv2.imread("foto.jpg")

#-- resim gösterme --
# imshow ile okunan resim gösterilir.
# winname : windows penceresinin adı
# mat : neyi göstericeksen
# cv2.imshow("image",resim)

# -- resmi ekranda tutma --
# resmin durması için
# waitkey kullanılır. normalde içine mili saniye cinsinden parametre alır.
# 0 -> herhangi bir tuşa basana kadar bekle.
# eğer bunu yapmazsan resim açıldığı gibi kapanır.
# cv2.waitKey(0)

#-- pencereleri kapatma --
# destroyWindow içine winname alır. ve herheangi bir tuşa bastığında içinde yazanı kapatır
# cv2.destroyWindow("image")

# destrolallwindow da birden fazla pencere açıldığında hepsini kapatır.
# yukarıdaki tek birini kapatıyordu
# cv2.destroyAllWindows()

#-- gri yapma --
# flags = 0 ise resim gri olur
# resim = cv2.imread("foto.png", 0)

#-- basılan karakter --
# herhangi bir tuşa bastığımızda pencereler kapanıyordu.
# basılan tuşun ascii karşılığını alabiliriz.
"""
a = cv2.waitKey(0)
print(a)
# a nın ascii karşılığının 32 olduğunu gördük
if a==32:
               print("Boşluk tuşuna basıldı")

if a == ord("k"):
               print("k tuşuna basıldı")
"""

# ord içine basılan karakteri alabilirsin. ord("q") da buradan geliyor 

#-- resim kaydetme --
# aynı dizine kayıt olur.
# ilk parametre verilecek isim
# ikinci parametre ne kayıt olacak ?
# cv2.imwrite("kayitOlanFoto.png", resim)

#-- matplotlib --
# görsele yakınlaşma, hangi pixelde neyin yer aldığını bilmek için pyplot fonk kullanırız
# renkler farklı gelir çünkü matplotib faklı bir renk düzeni kullanır.
plt.imshow(resim)
plt.show()

# rengi gri yapmak için cmap = 0
# tabi asıl resmin de gri yapılması gerekir
# plt.imshow(resim, cmap="gray")
"""
NOT : Opencv de renkli görüntü BGR modunda. Matplotlib RGB modunda görüntüler.(?).
bu yüzden ikisinde farklı renkler ortaya çıkar. opencv de kırmızı yerler matplotlib da mavidir gibi.

"""


#-- resim gösterme --
# imshow resmin boyutlarıyla oynamamıza izin vermez.
# kendimiz bir pencere oluştup resmi bu pencereye verebiliriz.
# WINDOW_FREERATIO : boyutlarla oynayabilirsin
# WINDOW_AUTOSIZE : boyutlarla oynayamazsın. resme göre ayarlanır.

# once kendi penceremizi oluşturuyouz. imhow u yazmasak pencere boş oluşur
cv2.namedWindow("bosPencere",cv2.WINDOW_FREERATIO) 
cv2.imshow("bosPencere",resim)

"""
NOT : cv3.waitKey(0) & 0xFF yazmalsın
tam mantığını anlamadım. 3. videonun başında anlatıyor

"""




cv2.waitKey(0)