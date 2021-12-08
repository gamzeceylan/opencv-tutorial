import cv2
import matplotlib.pyplot as plt

img = cv2.imread("sudoku.jpg",0)
plt.figure(), plt.imshow(img, cmap="gray"), plt.axis("off"), plt.title("orijinal img")
# cmap = color map

# x gradyan
"""
- x eksenindeki gradyanları bulucaz -> x ler sabitken
- ddepth = outbputun deirnliğini gösterir
- şuan sadece x yönünde yapıyoruz
"""
sobelx = cv2.Sobel(img, ddepth=cv2.CV_16S, dx=1, dy=0, ksize=5)
plt.figure(), plt.imshow(sobelx, cmap="gray"), plt.axis("off"), plt.title("sobelx")

# y gradyan
"""
- y eksenindeki gradyanları bulucaz -> y ler sabitken
"""
sobely = cv2.Sobel(img, ddepth=cv2.CV_16S, dx=0, dy=1, ksize=5)
plt.figure(), plt.imshow(sobely, cmap="gray"), plt.axis("off"), plt.title("sobely")

# laplacian gradyan -> her iki yöndeki
laplacian = cv2.Laplacian(img, ddepth= cv2.CV_16S) 
plt.figure(), plt.imshow(laplacian, cmap="gray"), plt.axis("off"), plt.title("laplacian")
