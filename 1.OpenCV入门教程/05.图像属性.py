import cv2

img1 = cv2.imread('image/lena256.bmp', cv2.IMREAD_UNCHANGED)
img2 = cv2.imread('image/lenacolor.png', cv2.IMREAD_UNCHANGED)

# 获取图像属性：形状
print(img1.shape)
print(img2.shape)
# 获取图像属性：像素数目
print(img1.size)
print(img2.size)
# 获取图像属性：像素数据类型
print(img1.dtype)
print(img2.dtype)
