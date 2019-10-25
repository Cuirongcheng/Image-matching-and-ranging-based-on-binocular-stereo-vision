import cv2
import numpy as np
import time


# 1) 打开图像
img1 = cv2.imread("./img/image1.jpg")
img2 = cv2.imread("./img/image5.jpg")


# 2) 图像灰度化
img1_gray = cv2.cvtColor(img1, cv2.IMREAD_GRAYSCALE)
img2_gray = cv2.cvtColor(img2, cv2.IMREAD_GRAYSCALE)

# 3) SIFT特征计算
sift = cv2.xfeatures2d.SIFT_create()

kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)
# kp1, des1 = sift.detectAndCompute(img1_gray, None)
# kp2, des2 = sift.detectAndCompute(img2_gray, None)


# 设置算法运行开始时间
start = time.clock()
# 4) Flann特征匹配
FLANN_INDEX_KDTREE = 1
index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
search_params = dict(checks=50)
flann = cv2.FlannBasedMatcher(index_params, search_params)
matches = flann.knnMatch(des1, des2, k=2)
goodMatch = []
# 匹配优化
for m, n in matches:
    if m.distance < 0.50*n.distance:
        goodMatch.append(m)
# 增加一个维度
goodMatch = np.expand_dims(goodMatch, 1)
flann_img_out = cv2.drawMatchesKnn(img1, kp1, img2, kp2, goodMatch[:20], None, flags=2)
flann_time = (time.clock() - start)
print("flann_time:", '% 4f' % (flann_time*1000))

# 5) BFmatcher with default parms
bf = cv2.BFMatcher(cv2.NORM_L2)
matches = bf.knnMatch(des1, des2, k=2)
goodMatch = []
# 匹配优化
for m, n in matches:
    if m.distance < 0.50 * n.distance:
        goodMatch.append(m)
# 增加一个维度
goodMatch = np.expand_dims(goodMatch, 1)
bf_img_out = cv2.drawMatchesKnn(img1, kp1, img2, kp2, goodMatch[:20], None, flags=2)
bf_time = (time.clock() - start)
print("bf_time:", '% 4f' % (bf_time*1000))

cv2.imshow('flannmatch', flann_img_out)#展示图片
cv2.imshow('bfmatch', bf_img_out)#展示图片
cv2.waitKey(0)#等待按键按下
cv2.destroyAllWindows()#清除所有窗口
