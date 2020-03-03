import cv2

img1 = cv2.imread(filename='image/lena256.bmp', flags=cv2.IMREAD_UNCHANGED)
cv2.imshow(winname='original', mat=img1)

img2 = cv2.Laplacian(src=img1, ddepth=cv2.CV_64F)
img2 = cv2.convertScaleAbs(src=img2)
cv2.imshow(winname='result', mat=img2)

cv2.waitKey()
cv2.destroyAllWindows()
