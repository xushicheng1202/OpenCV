import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('image/lenacolor.png', cv2.IMREAD_GRAYSCALE)
equ = cv2.equalizeHist(img)

# plt.hist(img.ravel(), 256)
# plt.figure()
# plt.hist(equ.ravel(), 256)
# 无法显示图片，plt.plot()，方式有问题
