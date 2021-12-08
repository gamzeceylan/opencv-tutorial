"""
- bazı deep learning modellerinde belli boyutlar kabul edilir. o yüzden
yeniden boyutlandırma önemlidir

"""
import cv2
img = cv2.imread("lenna.png")

# yeniden boyutlandırma için orjinal boyutu bilmeliyiz

print("Resim boyutu: ", img.shape)

# resmi içe aktar
cv2.imshow("orjinal",img)
#img deki 0 ı silersen 3 kanallı gözükkür. varsayılan 1 atanır


# resized
imgResized = cv2.resize(img, (800,800))
print("Resized img shape: ", imgResized.shape)
cv2.imshow("img resized", imgResized)

# kırpma
imgCropped = img[0:200, 0:500] # pixel alıyoruz
cv2.imshow("kirpik", imgCropped)