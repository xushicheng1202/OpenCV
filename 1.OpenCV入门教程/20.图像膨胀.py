import cv2
import numpy as np

img1 = cv2.imread('image/lena256.bmp', cv2.IMREAD_UNCHANGED)
cv2.imshow('original', img1)

img2 = cv2.dilate(img1, kernel=np.ones((5, 5), dtype=np.uint8), iterations=5)
cv2.imshow('cv2.dilate(img1, kernel=np.ones((5, 5), dtype=np.uint8), iterations=5)', img2)

cv2.waitKey()
cv2.destroyAllWindows()
