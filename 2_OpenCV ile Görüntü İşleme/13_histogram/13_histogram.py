import cv2
import matplotlib.pyplot as plt
import numpy as np

# resmi içe akar
img = cv2.imread("red_blue.jpg")
img_vis = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # cvt = convert color bgr->rgb
plt.figure(), plt.imshow(img_vis)

print(img.shape)

# histogram hesapla
"""
- channels: resmin kanalları
- mask: resmin belli bir kısmını almakla ilgili
- histSize: 0-255 arası toplam 256 tane var
- ranges
"""
img_hist = cv2.calcHist([img], channels=[0], mask=None, histSize=[256], ranges=[0,256])
print(img_hist.shape)
plt.figure(), plt.plot(img_hist)
"""
- yukarıdaki bize pixel değerlerinden kaç tane olduğunu söyler
- grafiği incelersen 0 dan 60 bin küsür, 255 ten 70 bine yakın
- ama yukarıda renk ayrımı yok. renk ayrımı da ekleyelim
"""

color = ("b", "g", "r") # b=0, g=1, r=2
plt.figure()
# enumerate-> color içindeki b (string olarak) yi c ye b nin indexini de i ye atar
for i,c in enumerate(color):
    hist = cv2.calcHist([img], channels=[i], mask=None, histSize=[256], ranges=[0,256])
    plt.plot(hist, color=c)
    
    
"""
-------------- yorumlama ---------------------
371*366
Out[17]: 135786 
tane pixel var ve bu fotoda yeşil renk olmadığından tane 0 a eşit yeşil kanalda pixel var demek
grafiğe bakarsan da yeşil çubukta bu değere eşit olduğunu görürsün

kırmızı mavi de renk oranları yarı yarıya 70 bin pixel kırmızısa 70 bin pixel mavide
yine iki ucunda yarı yarıya olduğunu görebilirsin

"""

# resmi içe aktar
golden_gate = cv2.imread("goldenGate.jpg")
C = cv2.cvtColor(golden_gate, cv2.COLOR_BGR2RGB)
plt.figure(), plt.imshow(golden_gate_vis)

print(golden_gate.shape)

# boyut çok büyük mask oluşturalım
"""
- önce resmin boyutunda siyah bir resim oluşturucaz
- sonra siyah resimde bir delik açıcaz
- ve resmin üzerine koyucaz
- böylece belli bir yer gösterilecek ve kalanı maskelenmiş olacak
"""
# siyah resim mask oluştruduk
mask = np.zeros(golden_gate.shape[:2], np.uint8)
plt.figure(), plt.imshow(mask, cmap="gray")

# belli bir yeri beyaz yaptık
mask[1500:2000, 1000:2000] = 255 # rastgele seçtiğimiz yeri beyaz yaptık
plt.figure(), plt.imshow(mask, cmap="gray")

# mask ı resme uyguladık
masked_img_vis = cv2.bitwise_and(golden_gate_vis, golden_gate_vis, mask=mask)
plt.figure(), plt.imshow(masked_img_vis, cmap="gray")

#### histogramı uygulama

# orjinal resme mask uygulama
masked_img_vis = cv2.bitwise_and(golden_gate, golden_gate, mask=mask)
masked_img_hist = cv2.calcHist([masked_img_vis], channels=[1], mask=mask, histSize=[256], ranges=[0,256])
# channel 0 kırmızı, 1 mavi, 2 kırmız nın dağılımını gösterir. -> hiç anlamdım
plt.figure(), plt.plot(masked_img_hist)


#### histogram eşitleme
"""
- kontrastı arttırmaya yarar
- kontrast arttırma = karşıtlık arttırma
"""
# histogramı çizdirelim
img = cv2.imread("hist_equ.jpg", 0)
plt.figure(),  plt.imshow(img, cmap="gray")
img_hist = cv2.calcHist([img], channels=[0], mask=None, histSize=[256], ranges=[0,256])
# siyah beyaz yaptığımız için chanell 0 olmak zorunda
plt.figure(), plt.plot(img_hist)


# equalizetion işlemi (eşitleme)
eq_hist = cv2.equalizeHist(img)
plt.figure(), plt.imshow(eq_hist, cmap="gray")
"""
- koyu renklileri 0'a açık renklileri 255'e çektik. 
- renkler arasındaki farkı açtık ve belirginliği arttırdık
"""

# equ uyguladığımız resmin histogramını çizdirme
eq_img_hist = cv2.calcHist([eq_hist], channels=[0], mask=None, histSize=[256], ranges=[0,256])
# siyah beyaz yaptığımız için chanell 0 olmak zorunda
plt.figure(), plt.plot(eq_img_hist)


"""
- hist incelersen ilk histogramdaki 100 ve 200 arasındaki dar bölgesi 0 ve 255 arasına genişlettik ve kontrastı arttırmış olduk.
ikinci histogramda bunu görebilirsin

"""





























