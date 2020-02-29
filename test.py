import cv2

# i = cv2.imread('image/lena256.bmp', cv2.IMREAD_UNCHANGED)
# print(i[100, 100])
# i[100, 100] = 255
# print(i[100, 100])

# i = cv2.imread('image/lenacolor.png', cv2.IMREAD_UNCHANGED)
# print(i[100, 100])
# i[100, 100] = [255, 255, 255]
# print(i[100, 100])

# i = cv2.imread('image/lenacolor.png', cv2.IMREAD_UNCHANGED)
# print(i[100, 100])
# i[100, 100, 2] = 255
# print(i[100, 100])

i = cv2.imread('image/lenacolor.png', cv2.IMREAD_UNCHANGED)
cv2.imshow('original', i)
i[100:150, 100:150] = [255, 255, 255]
cv2.imshow('result', i)
cv2.waitKey(0)
cv2.destroyAllWindows()
