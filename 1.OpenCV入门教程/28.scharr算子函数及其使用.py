import cv2

img1 = cv2.imread(filename='image/lena256.bmp', flags=cv2.IMREAD_UNCHANGED)
cv2.imshow('original', img1)

scharrx = cv2.Scharr(src=img1, ddepth=cv2.CV_64F, dx=1, dy=0)
scharry = cv2.Scharr(src=img1, ddepth=cv2.CV_64F, dx=0, dy=1)

scharrx = cv2.convertScaleAbs(src=scharrx)
scharry = cv2.convertScaleAbs(src=scharry)

scharrxy = cv2.addWeighted(src1=scharrx, alpha=0.5, src2=scharry, beta=0.5, gamma=0)
cv2.imshow(winname='', mat=scharrxy)

cv2.waitKey()
cv2.destroyAllWindows()
