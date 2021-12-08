"""
- görüntünün düşük geçişli bir filtre uygulanmasıyla elde eidlir -> low pass filter
- bulanıklaştırma gürültüyü gidermek için kullanışlıdır. aslında görüntüden yüksek frekans
içeriği (parazit, kenarlar) kaldırılır.
- opencv de üç ana tür bulanıklaştırma tekniği vardır: ortalama bulanıklaştırma, gauss bulanıklaştırma
medyan bulanıklaştırma
- bulanıklaştırmada resim üzerinde bulunan detaylar azaltılır böylece gürültüde azaltılır
- bu yöntemleirn detaylarına bak netten
- kendimiz de gürültü oluşturucaz -> numpy kullanıcaz

- bulanıklaştırma gürültüyü azaltır bu yüzden görüntü detayı da azaltılmış olur
"""

import cv2
import numpy as np
import warnings # uyarıları kaldırmak için
import matplotlib.pyplot as plt

warnings.filterwarnings("ignore")

img = cv2.imread("NYC.jpg")
img = cv2.cvtColor(img, code=cv2.COLOR_BGR2RGB) # rgb ye çevirmek için
plt.figure(), plt.imshow(img), plt.axis("off"), plt.title("original"), plt.show()

# ortalama bulanıklaştırma
"""
- örn 5x5 lik bir filtre belirlersin bu kutu resim üzerinde gezer. ve her kutudaki
pixellerin toplamının ortalaması alınır ve tam ortaya(merkeze) yazılır. böylece görüntünün
hataları arındırılmış olur, detay azaltılır
"""
dst2 = cv2.blur(img, ksize=(3,3)) # kernel size : kutu boyutu
plt.figure(), plt.imshow(dst2), plt.axis("off"), plt.title("ortblur"), plt.show()

# gaussian blur
"""
- üzerinde gauss noise varsa onları elemek için kullanılan yöntem
- kernellerin içinde x ve y yönlerinde sigma değerleri yazarak kutucukların iki boyutlu bir gauss olmasını
sağlıyorduk ve içinde bulunan değerlere göre pixeller üzerinde işlem yapılıyordu

"""

gb = cv2.GaussianBlur(img, ksize=(3,3), sigmaX=7)
"""
- y yönündeki sigmayı yazmazsan otomatik y yönündeki sigmaya eşit olur
"""
plt.figure(), plt.imshow(gb), plt.axis("off"), plt.title("gb"), plt.show()

# medyan blur
"""
- filtrenin içindeki pixellerin medyanı alınır.
- merkezdeki pixelin genliğine bu medyan yazılır
"""
mb = cv2.medianBlur(img, ksize=3)
plt.figure(), plt.imshow(dst2), plt.axis("off"), plt.title("mb"), plt.show()

# resme noise (gürültü) ekleme
"""
- noise ekleyelim ki blurlamanın işe yaradığını görelim

"""
def gaussianNoise(image):
    # ch: channel resim rgb mi yoksa gray scale mi (3/1)
    row, col, ch = image.shape
    mean = 0
    var = 0.05 ## varyans standart sapma elde edebilmek için kullnırız
    sigma = var**0.05 # standart sapma = sigma
    
    gauss = np.random.normal(mean, sigma, (row, col, ch)) # gaussian nın diğer adı normal dağılımdır
    gauss = gauss.reshape(row, col, ch) # boyuttan emin olalım
    noisy = image + gauss
    
    return noisy # resme gauss gürültüsü ekledik


"""
- bizim değerlerimiz 0-255 genlik aralığında değişiyordu
- bu değerleri normalize etmemiz laızm. yani 0 ve 1 arasına taşımalıyız
çünkü oluşturudğumuz gürültü 0.x ortalamalı bir gürültü. normalize edilmemiş
bir resim üzerine gürültü eklersek çok küçük olduğu zaten bir şey gözükmez

"""
# içe aktarma ve normalize etme
img = cv2.imread("NYC.jpg")
img = cv2.cvtColor(img, code=cv2.COLOR_BGR2RGB)/255 # normalize ettik
plt.figure(), plt.imshow(img), plt.axis("off"), plt.title("original2"), plt.show()

# gauss gürültüsü ekleme
gaussianNoiseImage = gaussianNoise(img)
plt.figure(), plt.imshow(gaussianNoiseImage), plt.axis("off"), plt.title("gauss_noise"), plt.show()

"""
- gauss noise ışıktan, kameranın donanımsal özelliklerinden, kamera kalitesinden, ortamın hareketliliğinden
kaynaklanabilir. bu şartlarda resimde noise olabilir
"""

# gürültü azaltma -> gaussian bulur ile azaltıcaz
gb2 = cv2.GaussianBlur(img, ksize=(3,3), sigmaX=7)
plt.figure(), plt.imshow(gb2), plt.axis("off"), plt.title("with gaussblur"), plt.show()
    
# tuz karabiber gürültüsü oluşturma
"""
- tuz karabiber gürültüsü resme siyah ve beyaz noktaların rastgele yerleştirilmesidir
"""
def saltPepperNoise(image):
    row, col, ch = image.shape
    s_vs_p = 0.5 # salt ve pepper oranları, noktaların oranı
    amount = 0.004
    noisy = np.copy(image) # orjinal görüntüyü bozmamak için 
    
    # salt -> beyaz noktalar
    num_salt = np.ceil(amount * image.size*s_vs_p)
    """
    - ceil elimizdeki herhangi bir ondalıklı sayııyı yukarı ya da aşağı tamamalr
    - ceil 2.4 ü 2.0 a yuvalrar yani yine float o yüzden inte çevirmeliyiz
    - yukarıda kaç tane beyaz nokta olacağını belirliyoruz
    - örn 1800 gibi bir değer çıkıcak bu beyaz gürültü sayısı
    """
    # beyaz gürültünün konumlarını belirleyelim
    coords = [np.random.randint(0, i-1, int(num_salt)) for i in image.shape]
    """
    - i-1 500 karakterse son index 499. dur o demek
    - 0 ile i-1 aradında num_salt kadar
    """
    noisy[coords] = 1 # beyazı coordinatlara ekledik. çünkü beyaz 1 di.
    
    # pepper -> siyah noktaları ekleme
    num_pepper = np.ceil(amount * image.size*(1-s_vs_p))
    coords = [np.random.randint(0, i-1, int(num_pepper)) for i in image.shape]
    noisy[coords] = 0 # siyah noktaları coordinatlara ekledik. çünkü beyaz 0 di.
    """
    - not: siyah ve beyaz noktaların yüzdeleri toplamları 1 olmak zorunda o yüzden 1 den çıkartıyoruz
    """
    return noisy
    
    """
    
    for i in img.shape:
        k = np.random.randint(0, i-1, num_salt)
        print(k)
        """
        
spImage = saltPepperNoise(img)
plt.figure(), plt.imshow(spImage), plt.axis("off"), plt.title("spImage"), plt.show()
  
    
# salt-pepper dan kurtulma
# medyan blur yöntemi ile
mb2 = cv2.medianBlur(spImage.astype(np.float32), ksize=3)
plt.figure(), plt.imshow(mb2), plt.axis("off"), plt.title("mb2"), plt.show()
"""
- yine format hatası altık. float32 ye çevirdik
"""
    
    
    
    
    
    
    
    
    
    




