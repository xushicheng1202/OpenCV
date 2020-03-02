import cv2

img1 = cv2.imread('image/lena256.bmp', cv2.IMREAD_UNCHANGED)
cv2.imshow('original', img1)

sobelx = cv2.Sobel(src=img1, ddepth=cv2.CV_64F, dx=1, dy=0)
sobely = cv2.Sobel(src=img1, ddepth=cv2.CV_64F, dx=0, dy=1)
# X轴上的边界
sobelx = cv2.convertScaleAbs(sobelx)
# Y轴上的边界
sobely = cv2.convertScaleAbs(sobely)
img2 = cv2.addWeighted(src1=sobelx, alpha=0.5, src2=sobely, beta=0.5, gamma=0)

cv2.imshow('result', img2)
cv2.waitKey()
cv2.destroyAllWindows()
