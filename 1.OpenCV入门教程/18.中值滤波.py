import cv2

img1 = cv2.imread('image/lenacolor.png')
img2 = cv2.medianBlur(img1, 3)

cv2.imshow('original', img1)
cv2.imshow('', img2)

cv2.waitKey()
cv2.destroyAllWindows()
