import cv2

img1 = cv2.imread('image/lenacolor.png')
img2 = cv2.flip(img1, -1)

cv2.imshow('original', img1)
cv2.imshow('cv2.flip(img1, 0)', img2)

cv2.waitKey()
cv2.destroyAllWindows()
