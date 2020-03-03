import cv2

img1 = cv2.imread('image/lena256.bmp', cv2.IMREAD_UNCHANGED)
cv2.imshow('original', img1)

img2 = cv2.Canny(image=img1, threshold1=100, threshold2=200)
cv2.imshow('result2', img2)

img3 = cv2.Canny(image=img1, threshold1=64, threshold2=128)
cv2.imshow('result3', img3)

cv2.waitKey()
cv2.destroyAllWindows()
