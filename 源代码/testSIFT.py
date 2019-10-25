import cv2
import numpy as np

img = cv2.imread('./img/image1.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
sift = cv2.xfeatures2d.SIFT_create()

kp = sift.detect(gray, None)  # 找到关键点
print(len(kp))

img = cv2.drawKeypoints(gray, kp, img)  # 绘制关键点

cv2.imshow('testSIFT', img)
cv2.waitKey(0)