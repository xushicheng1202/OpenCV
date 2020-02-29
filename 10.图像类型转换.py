import cv2

img1 = cv2.imread('image/lenacolor.png')
img4 = cv2.imread('image/lena256.bmp', cv2.IMREAD_UNCHANGED)
img2 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img3 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img5 = cv2.cvtColor(img4, cv2.COLOR_GRAY2BGR)

print(img4.shape)
cv2.imshow('img1', img1)
cv2.imshow('cv2.COLOR_BGR2GRAY', img2)
cv2.imshow('cv2.COLOR_BGR2RGB', img3)
cv2.imshow('cv2.COLOR_GRAY2BGR', img5)

cv2.waitKey()
cv2.destroyAllWindows()
