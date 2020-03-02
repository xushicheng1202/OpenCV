import cv2
import numpy as np

img1 = cv2.imread('image/lena256.bmp', cv2.IMREAD_UNCHANGED)
cv2.imshow('original', img1)

img2 = cv2.morphologyEx(src=img1, op=cv2.MORPH_CLOSE, kernel=np.ones(shape=(5, 5), dtype=np.uint8))
cv2.imshow('q', img2)

cv2.waitKey()
cv2.destroyAllWindows()
