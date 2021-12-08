import cv2
import matplotlib.pyplot as plt


# template matching: sablon esleme
"""
- arayacağımız küçük resim şablondur
- şablonu büyük resimde arıcaz

"""
img = cv2.imread("cat.jpg", 0) # ana resim
print(img.shape)
template = cv2.imread("cat_face.jpg", 0) # şablon resim
print(template.shape)
h, w = template.shape

methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
"""
- yukarıdaki metodların ana hedefi korelasyona bakmak. (iki resim arasında)
- opencv nin sağladığı hazır metodlardır
- metotları str olarak yazdık. ama cv2. diye yazmamız gerekioyrdu
- metotları cv2. formatına çevirelim. -> eval metodu

"""

for meth in methods:
    
    method = eval(meth) # 'cv2.TM_CCOEFF' -> cv2.TM_CCOEFF
    
    res = cv2.matchTemplate(img, template, method)
    print(res.shape)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    
    """
    - yukarıdaki metoların çıktıları aynı değil.
    - ilgil iki metotda sol üst köşeye min_loc diğerinde max_loc karşılık gelir
    - sebebi yok opencv yi yazanlar böyle yapmış
    """
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    
    bottom_right = (top_left[0] + w, top_left[1] + h)
    
    cv2.rectangle(img, top_left, bottom_right, 255, 2)
    
    plt.figure()
    plt.subplot(121), plt.imshow(res, cmap = "gray")
    plt.title("Eşleşen Sonuç"), plt.axis("off")
    plt.subplot(122), plt.imshow(img, cmap = "gray")
    plt.title("Tespit edilen Sonuç"), plt.axis("off")
    plt.suptitle(meth)
    
    plt.show()


