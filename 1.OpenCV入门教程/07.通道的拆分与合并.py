import cv2

img1 = cv2.imread('image/lenacolor.png')
b, g, r = cv2.split(img1)
cv2.imshow('original', img1)
cv2.imshow('B', b)
cv2.imshow('G', g)
cv2.imshow('R', r)
img2 = cv2.merge([b, g, r])
cv2.imshow('merge', img2)
cv2.waitKey()
cv2.destroyAllWindows()
