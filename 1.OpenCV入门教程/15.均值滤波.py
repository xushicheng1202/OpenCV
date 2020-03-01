import cv2

img1 = cv2.imread('image/lenacolor.png')
cv2.imshow('original', img1)

img2 = cv2.blur(img1, (5, 5))
cv2.imshow('cv2.blur(img1, (10, 10))', img2)

cv2.waitKey()
cv2.destroyAllWindows()
