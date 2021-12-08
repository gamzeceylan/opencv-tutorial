#%%
import cv2
import matplotlib.pyplot as plt
import numpy as np

# içe aktar
coin = cv2.imread("coins.jpg")
plt.figure(), plt.imshow(coin), plt.axis("off")

"""
- siyah beyaz resim
- high intecity (yüksek genlik): tepeler
- low intecty (düşük genlik): vadiler
- algoritma her bir vadi için fakrlı renk label ataması yapar
- segentasyon da bu algoritma için önemlidir
"""

# lpf: blurring (low pass filter)
"""
- resim üzerindeki gürültülerden kurtulalım
çünkü çok fazla girinti-çıkıntı var. bizim için bunlar önemli değil
sadece nesnelerin sınırları önemli
"""
coin_blur = cv2.medianBlur(coin, 13) # kernel baya büyük ondan çok bulanık
plt.figure(), plt.imshow(coin_blur), plt.axis("off")


# grayscale
coin_gray = cv2.cvtColor(coin_blur, cv2.COLOR_BGR2GRAY)
plt.figure(), plt.imshow(coin_gray, cmap="gray"), plt.axis("off")
"""
- cmap gray demezsen siyah beyaz gözükmez
"""

# binary threshold
"""
- böylece vadi ile tepeler arasındaki fark daha da çok açılacak
- çünkü biz external kontur bulucaz.
"""
ret, coin_thresh = cv2.threshold(coin_gray, 75, 255, cv2.THRESH_BINARY)
plt.figure(), plt.imshow(coin_thresh, cmap="gray"), plt.axis("off")

## konturleme
# _, contours, hierarchy = cv2.findContours(coin_thresh.copy(), cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
"""
- sürüm fakrlılıkları. eskiden 3 farklı deper return ediliyordu
"""
# kontur bulma
contours, hierarchy = cv2.findContours(coin_thresh.copy(), cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
# konturleri çizdirme
for i in range(len(contours)):
    
    if hierarchy[0][i][3] == -1: # external contour
        cv2.drawContours(coin, contours,i,(0,255,0),10)
        
plt.figure(),plt.imshow(coin),plt.axis("off")

"""
- yukarıdaki algoritma segmentasyon işini tam olarak yapamdı. nesneleri bir bütün olarak algıladı
ve ayıramadı. mevi renk tespitinde yaşadığımız olayı yaşadık
- farklı yöntemler ile bu problemi çözmeye çalışalım.
(en baştan yapıyoruz)
"""

#%%

# watershed

# içe aktar
coin = cv2.imread("coins.jpg")
plt.figure(), plt.imshow(coin), plt.axis("off")

# lpf: blurring
coin_blur = cv2.medianBlur(coin, 13)
plt.figure(), plt.imshow(coin_blur), plt.axis("off")

# grayscale
coin_gray = cv2.cvtColor(coin_blur, cv2.COLOR_BGR2GRAY)
plt.figure(), plt.imshow(coin_gray, cmap="gray"), plt.axis("off")

# binary threshold
ret, coin_thresh = cv2.threshold(coin_gray, 65, 255, cv2.THRESH_BINARY)
plt.figure(), plt.imshow(coin_thresh, cmap="gray"), plt.axis("off")

"""
- nesneler arasında köprü var. o yüzden nesneler bütün algılanıyor.(kontrulenen resimde görebilirsin)
- eğer nesneleri küçültürsek nesneler birnirinden ayrılır. sonra da açılma yaparız ve eski haline döneriz
- hedefimiz: resimdeki noise biraz arttırıp opening ile azaltmak hedefimiz.
böylece köprülerde de biraz azalma olacak
"""
# açılma
kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(coin_thresh, cv2.MORPH_OPEN, kernel, iterations = 2)
plt.figure(), plt.imshow(opening, cmap="gray"), plt.axis("off")

# nesneler arası distance
"""
- köprüler L2 distance olur
- şuan dikkat edersen köprüler de var
"""
dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
plt.figure(), plt.imshow(dist_transform, cmap="gray"), plt.axis("off")

"""
- öndeki nesneleri bulabilmek için küçültücez, arkayı bulmak için
sonra büyütücez??? wtf
"""
# resmi küçült (aslında nesneler)
ret, sure_foreground = cv2.threshold(dist_transform, 0.4*np.max(dist_transform),255,0)
plt.figure(), plt.imshow(sure_foreground, cmap="gray"), plt.axis("off")

"""
- küçültmedeki resmde nesneelrin genlik değerlerine bakıyoruz. 12, 13 15 gibi sayılar.
nesnelerin merkezlerinin genlik değerleri ise 80, 90 gibi büyük sayılar
- eğer maximun threshold değerini bulursak ve bunun yüzde 40 ını alırsak (literatürde geçen değer)
köprülerdne kurtulmuş oluruz. geriye sadece neslerin olduğu küçük adacıklar kalır
- buraya kadar su doldurma işlemini gerçekleştirdik. nesneler arası bağlanrtı kesildi
- arka planın ne olduğunu bulmak için de nesneleri büyütücez-> genişletme işlemi
"""


# arka plan için resmi büyült
"""
- adacıkların etrafı tamamen ayrılmış oldu. adacıklar boş siyah kaldı
"""
sure_background = cv2.dilate(opening, kernel, iterations = 1) # genişletme
sure_foreground = np.uint8(sure_foreground)
unknown = cv2.subtract(sure_background,sure_foreground) # arka plan ile ön planın farkını alırsak daha net bir sonuç çıkar
plt.figure(), plt.imshow(unknown, cmap="gray"), plt.axis("off")




"""
- watershed algoritmasına girdi sağlayabilmek için marker ları bulmamız gerek
- bu yüzden bağlantıları sağlamalıyız???

"""
# bağlantı
ret, marker = cv2.connectedComponents(sure_foreground)
marker = marker + 1
marker[unknown == 255] = 0 # etrafları siyahlaştırdık ve adacıklar tam ortaya çıktı
plt.figure(), plt.imshow(marker, cmap="gray"), plt.axis("off")



# havza algoritmasına verelim
"""
- artık gerçek nesneler ortaya çıktı. tek yapmamız gerek tekrar konturleme işlemine 
sokup etrafını çizdirmek
"""
marker = cv2.watershed(coin,marker)
plt.figure(), plt.imshow(marker, cmap="gray"), plt.axis("off")


# kontur
# _, contours, hierarchy = cv2.findContours(coin_thresh.copy(), cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
contours, hierarchy = cv2.findContours(marker.copy(), cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

for i in range(len(contours)):
    
    if hierarchy[0][i][3] == -1:
        cv2.drawContours(coin, contours,i,(255,0,0),2)
plt.figure(),plt.imshow(coin),plt.axis("off")


















