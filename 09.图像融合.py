import cv2

img1 = cv2.imread('image/add/boat.bmp')
img2 = cv2.imread('image/add/lena.bmp')
result = cv2.addWeighted(img1, 0.3, img2, 0.6, 0)
cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('cv2.addWeighted', result)
cv2.waitKey()
cv2.destroyAllWindows()
