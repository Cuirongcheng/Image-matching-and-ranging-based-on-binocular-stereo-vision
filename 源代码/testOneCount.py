#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Date: 18-10-29

import numpy as np      # 导入numpy库
import cv2              # 导入Opencv库

KNOWN_DISTANCE = 32   # 这个距离自己实际测量一下

KNOWN_WIDTH = 11.69     # A4纸的宽度
KNOWN_HEIGHT = 8.27

IMAGE_PATHS = ["./img/Picture2.jpg", "./img/Picture3.jpg"]  # 将用到的图片放到了一个列表中


# 定义目标函数
def find_marker(image):
    gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 将彩色图转化为灰度图
    gray_img = cv2.GaussianBlur(gray_img, (5, 5), 0)    # 高斯平滑去噪
    edged_img = cv2.Canny(gray_img, 35, 125)     # Canny算子阈值化
    cv2.imshow("降噪效果图", edged_img)          # 显示降噪后的图片
    # 获取纸张的轮廓数据
    img, countours, hierarchy = cv2.findContours(edged_im  g.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    print(len(countours))
    c = max(countours, key=cv2.contourArea)    # 获取最大面积对应的点集
    rect = cv2.minAreaRect(c)       # 最小外接矩形
    return rect


# 定义距离函数
def distance_to_camera(knownWidth, focalLength, perWidth):
    return (knownWidth * focalLength) / perWidth


# 计算摄像头的焦距（内参）
def calculate_focalDistance(img_path):
    first_image = cv2.imread(img_path)      # 这里根据准备的第一张图片，计算焦距
    cv2.imshow('first image', first_image)
    marker = find_marker(first_image)       # 获取矩形的中心点坐标，长度，宽度和旋转角度
    focalLength = (marker[1][0] * KNOWN_DISTANCE) / KNOWN_WIDTH  # 获取摄像头的焦距
    # print(marker[1][0])
    print('焦距(focalLength) = ', focalLength)        # 打印焦距的值
    return focalLength


# 计算摄像头到物体的距离
def calculate_Distance(image_path, focalLength_value):
    image = cv2.imread(image_path)
    cv2.imshow("原图", image)
    marker = find_marker(image)     # 获取矩形的中心点坐标，长度，宽度和旋转角度， marke[1][0]代表宽度
    distance_inches = distance_to_camera(KNOWN_WIDTH, focalLength_value, marker[1][0])
    box = cv2.boxPoints(marker)
    print("Box = ", box)
    box = np.int0(box)
    print("Box = ", box)
    cv2.drawContours(image, [box], -1, (0, 255, 0), 2)      # 绘制物体轮廓
    cv2.putText(image, "%.2fcm" % (distance_inches * 2.54), (image.shape[1] - 300, image.shape[0] - 20),
                cv2.FONT_HERSHEY_SIMPLEX, 2.0, (0, 255, 0), 3)
    cv2.imshow("单目测距", image)

if __name__ == "__main__":
    img_path = "./img/Picture2.jpg"
    focalLength = calculate_focalDistance(img_path)

    for image_path in IMAGE_PATHS:
        calculate_Distance(image_path, focalLength)
        cv2.waitKey(0)
    cv2.destroyAllWindows()