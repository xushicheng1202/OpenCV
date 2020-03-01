import cv2

img1 = cv2.imread('image/lena512.bmp', cv2.IMREAD_UNCHANGED)
cv2.imshow('original', img1)

thresh2, img2 = cv2.threshold(img1, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('cv2.THRESH_BINARY', img2)

thresh3, img3 = cv2.threshold(img1, 127, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('cv2.THRESH_BINARY_INV', img3)

thresh4, img4 = cv2.threshold(img1, 127, 255, cv2.THRESH_TRUNC)
cv2.imshow('cv2.THRESH_TRUNC', img4)

thresh5, img5 = cv2.threshold(img1, 127, 255, cv2.THRESH_TOZERO_INV)
cv2.imshow('cv2.THRESH_TOZERO_INV', img5)

thresh6, img6 = cv2.threshold(img1, 127, 255, cv2.THRESH_TOZERO)
cv2.imshow('cv2.THRESH_TOZERO', img6)

cv2.waitKey()
cv2.destroyAllWindows()
