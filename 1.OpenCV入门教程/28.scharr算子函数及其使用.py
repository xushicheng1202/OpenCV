import cv2

img1 = cv2.imread('image/lena256.bmp', cv2.IMREAD_UNCHANGED)
cv2.imshow('original', img1)

scharrx = cv2.Scharr(src=img1, ddepth=cv2.CV_64F, dx=1, dy=0)
scharry = cv2.Scharr(src=img1, ddepth=cv2.CV_64F, dx=0, dy=1)

scharrx = cv2.convertScaleAbs(scharrx)
scharry = cv2.convertScaleAbs(scharry)

scharrxy = cv2.addWeighted(scharrx, 0.5, scharry, 0.5, 0)
cv2.imshow('', scharrxy)

cv2.waitKey()
cv2.destroyAllWindows()
