import cv2

# img1 = cv2.imread('image/lenacolor.png')
# img2 = img1[220:400, 250:350]
# cv2.imshow('original', img1)
# cv2.imshow('face', img2)
# cv2.waitKey()
# cv2.destroyAllWindows()

img1 = cv2.imread('image/lenacolor.png')
img2 = img1[220:400, 250:350]
img3 = cv2.imread('image/girl.bmp')
img3[0:180, 0:100] = img2
cv2.imshow('original', img3)
cv2.waitKey()
cv2.destroyAllWindows()
