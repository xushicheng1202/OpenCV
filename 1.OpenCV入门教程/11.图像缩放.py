import cv2

img1 = cv2.imread('image/lenacolor.png')
cv2.imshow('original', img1)

img2 = cv2.resize(img1, (200, 100))
cv2.imshow('cv2.resize(img1, (200, 100))', img2)

size3 = (300, 100)
img3 = cv2.resize(img1, size3)
cv2.imshow('cv2.resize(img1, size3)', img3)

rows, cols, chan = img1.shape
size4 = (round(rows * 0.5), round(cols * 1.5))
img4 = cv2.resize(img1, size4)
cv2.imshow('cv2.resize(img1, size4)', img4)

img5 = cv2.resize(img1, None, fx=0.5, fy=1.3)
cv2.imshow('cv2.resize(img1, None, fx=0.5, fy=1.3)', img5)

cv2.waitKey()
cv2.destroyAllWindows()
