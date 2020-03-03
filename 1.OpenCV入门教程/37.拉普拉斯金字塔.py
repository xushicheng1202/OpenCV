import cv2

img1 = cv2.imread('image/lena256.bmp', cv2.IMREAD_UNCHANGED)
cv2.imshow('original', img1)

img1 = img1
img1_D = cv2.pyrDown(img1)
L0 = img1 - cv2.pyrUp(img1_D)
cv2.imshow('0', L0)

img1_D = cv2.pyrDown(img1)
img1_2D = cv2.pyrDown(img1_D)
L1 = img1_D - cv2.pyrUp(img1_2D)
cv2.imshow('1', L1)

cv2.waitKey()
cv2.destroyAllWindows()
