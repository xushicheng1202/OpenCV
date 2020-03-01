import cv2

img1 = cv2.imread('image/lenacolor.png')
cv2.imshow('original', img1)

img2 = cv2.GaussianBlur(img1, (5, 5), 0)
cv2.imshow('cv2.GaussianBlur(img1, (3, 3), 0)', img2)

cv2.waitKey()
cv2.destroyAllWindows()
