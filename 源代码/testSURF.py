import cv2
import numpy as np

img = cv2.imread('./img/lp.bmp')

#灰度处理
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#参数为hessian矩阵的阈值
surf = cv2.xfeatures2d.SURF_create(400)

#找到关键点和描述符
key_query, desc_query = surf.detectAndCompute(img, None)

print(key_query, desc_query)

#把特征点标记到图片上
img=cv2.drawKeypoints(img, key_query, img)

cv2.imshow('testSURF', img)
cv2.waitKey(0)