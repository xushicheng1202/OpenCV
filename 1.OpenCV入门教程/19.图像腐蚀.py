import cv2
import numpy as np

img1 = cv2.imread('image/lena256.bmp', cv2.IMREAD_UNCHANGED)

img2 = cv2.erode(img1, kernel=np.ones((5, 5), np.uint8), iterations=1)

cv2.imshow('original', img1)
cv2.imshow('1', img2)

cv2.waitKey()
cv2.destroyAllWindows()
