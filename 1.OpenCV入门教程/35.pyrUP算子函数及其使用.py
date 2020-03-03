import cv2

img1 = cv2.imread('image/lena256.bmp', cv2.IMREAD_UNCHANGED)
cv2.imshow('original', img1)

img2 = cv2.pyrUp(img1)
cv2.imshow('cv2.pyrUp', img2)

cv2.waitKey()
cv2.destroyAllWindows()
