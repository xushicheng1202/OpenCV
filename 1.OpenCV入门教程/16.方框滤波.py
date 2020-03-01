import cv2

img1 = cv2.imread('image/lenacolor.png')
img2 = cv2.boxFilter(img1, -1, (15, 15), normalize=0)
# img2 = cv2.boxFilter(img1, -1, (15, 15), normalize=1)

cv2.imshow('original', img1)
cv2.imshow('cv2.boxFilter(img1, -1, (5, 5), normalize=0)', img2)

cv2.waitKey()
cv2.destroyAllWindows()
