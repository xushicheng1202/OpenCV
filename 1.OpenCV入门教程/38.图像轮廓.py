import cv2

img1 = cv2.imread('image/lenacolor.png')
img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
ret, img1_gray_binary = cv2.threshold(img1_gray, 127, 255, cv2.THRESH_BINARY)
img2, img2_contours, img2_hierarchy = cv2.findContours(img1_gray_binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
img1_copy = img1.copy()
result = cv2.drawContours(img1_copy, img2_contours, -1, (0, 255, 0), 2)

cv2.imshow('original', img1)
cv2.imshow('result', result)

cv2.waitKey()
cv2.destroyAllWindows()
