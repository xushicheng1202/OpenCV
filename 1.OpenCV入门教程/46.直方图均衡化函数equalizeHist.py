import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('image/lenacolor.png', cv2.IMREAD_GRAYSCALE)
equ = cv2.equalizeHist(img)

cv2.imshow('original', img)
cv2.imshow('result', equ)

cv2.waitKey()
cv2.destroyAllWindows()

