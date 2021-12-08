"""

"""
import cv2
import numpy as np

img = cv2.imread("lenna.png")
cv2.imshow("original", img)

# horizontal -> yanaya
"""
- içine tuple alır
"""
hor = np.hstack((img, img))
cv2.imshow("horizontal", hor)

# vertivcal -> dikey
ver = np.vstack((img, img))
cv2.imshow("vertical", ver)


cv2.waitKey(0)
cv2.destroyAllWindows()