import cv2

img1 = cv2.imread('image/lena256.bmp')
img2 = img1
img3 = img1 + img2
img4 = cv2.add(img1, img2)
cv2.imshow('original', img1)
cv2.imshow('img1 + img2', img3)
cv2.imshow('cv2.add(img1, img2)', img4)
cv2.waitKey()
cv2.destroyAllWindows()
