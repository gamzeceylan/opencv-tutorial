#%% resmi içe aktarma
"""
- .py dosyan ile resimlerin bulunduğu klasör aynı dizinde bulunmalı
aynı dizinde değilse ayrıca belirtmen gerekir
- ve sağ yukarıda path'de de aynı dizinde olmalısın
"""
import cv2
img = cv2.imread("messi5.jpg", 0)
# 0 -> resmi siyah yapar
cv2.imshow("ilk resim", img)
"""
- img deki sayılar resmin genliği 0-255 arası değişebilir
- dikkat edersen bir matris oluştu
- şuan 280*450 = 126000 boyutunda array var
"""

k = cv2.waitKey(0) &0xFF # klavyeye bağlanma
# klavyeden komut bekler

if k == 27: # esc tuşu 
    cv2.destroyAllWindows()
elif k == ord("s"):
    cv2.imwrite("messi_gray.png", img)   


