import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread('image/lenacolor.png', cv2.IMREAD_GRAYSCALE)
mask = np.zeros(img1.shape, np.uint8)
mask[200:400, 200:400] = 255
histO = cv2.calcHist(images=[img1], channels=[0], mask=None, histSize=[256], ranges=[0, 255])
histM = cv2.calcHist(images=[img1], channels=[0], mask=mask, histSize=[256], ranges=[0, 255])

cv2.imshow('original', histO)
cv2.imshow('result', histM)

cv2.waitKey()
cv2.destroyAllWindows()

# plt.plot(histO)
# plt.plot(histM)
# 无法显示图片，plt.plot()，方式有问题
