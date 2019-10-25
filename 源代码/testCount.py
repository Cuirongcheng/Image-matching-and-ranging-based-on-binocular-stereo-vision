#!usr/bin/python
# -*- coding: utf-8 -*-

########利用三角形相似原理进行简单单目测距#########
# author：行歌
# email:1013007057@qq.com

import numpy as np
import cv2

# initialize the known distance from the camera to the object,
# which in this case is 24 inches
KNOWN_DISTANCE = 24.0

# initialize the known object width, which in this case,
# the piece of paper is 11 inches wide
KNOWN_WIDTH = 11.69
KNOWN_HEIGHT = 8.27

# initialize the list of images that we'll be using
IMAGE_PATHS = [ "./img/Picture2.jpg", "./img/Picture3.jpg"]


def find_marker(image):
    gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 将彩色图转化为灰度图

    gray_img = cv2.GaussianBlur(gray_img, (5, 5), 0)
    # 高斯平滑去噪

    edged_img = cv2.Canny(gray_img, 35, 125)
    # Canny算子阈值化
    # cv2.imshow("edged_img",edged_img)

    img, countours, hierarchy = cv2.findContours(edged_img.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    # 注意，findcontours函数会“原地”修改输入的图像。opencv3会返回三个值,分别是img, countours, hierarchy
    # 第二个参数表示轮廓的检索模式,cv2.RETR_EXTERNAL表示只检测外轮廓；v2.RETR_LIST检测的轮廓不建立等级关系
    # cv2.RETR_CCOMP建立两个等级的轮廓；cv2.RETR_TREE建立一个等级树结构的轮廓。
    # 第三个参数method为轮廓的近似办法,cv2.CHAIN_APPROX_NONE存储所有的轮廓点，
    # 相邻的两个点的像素位置差不超过1，即max（abs（x1 - x2），abs（y2 - y1）） == 1
    # cv2.CHAIN_APPROX_SIMPLE压缩水平方向，垂直方向，对角线方向的元素，只保留该方向的终点坐标，
    # 例如一个矩形轮廓只需4个点来保存轮廓信息

    # cv2.drawContours(image,countours,-1,(0,0,255),2,8)
    # # 第三个参数指定绘制轮廓list中的哪条轮廓，如果是-1，则绘制其中的所有轮廓。
    #
    # cv2.imshow('image', image)

    # print(len(countours)),
    # 输出如下：15，即该图检测出15个轮廓

    c = max(countours, key=cv2.contourArea)
    # 提取最大面积矩形对应的点集

    rect = cv2.minAreaRect(c)
    # cv2.minAreaRect()函数返回矩形的中心点坐标，长宽，旋转角度[-90,0)，当矩形水平或竖直时均返回-90
    # c代表点集，返回rect[0]是最小外接矩形中心点坐标，
    # rect[1][0]是width，rect[1][1]是height，rect[2]是角度

    # box = cv2.boxPoints(rect)
    # # 但是要绘制这个矩形，我们需要矩形的4个顶点坐标box, 通过函数cv2.boxPoints()获得，
    # # 即得到box：[[x0, y0], [x1, y1], [x2, y2], [x3, y3]]
    # # print(box)，输出如下：
    # # [[508.09482  382.58597]
    # #  [101.76947  371.29916]
    # #  [109.783356  82.79956]
    # #  [516.1087    94.086365]]
    #
    # # 根据检测到的矩形的顶点坐标box，我们可以将这个矩形绘制出来，如下所示：
    # for i in range(len(box)):
    #     cv2.line(image, (box[i][0],box[i][1]),(box[(i+1)%4][0],box[(i+1)%4][1]),(0,0,255),2,8)
    # cv2.imshow('image', image)

    return rect


def distance_to_camera(knownWidth, focalLength, perWidth):
    return (knownWidth * focalLength) / perWidth


def calculate_focalDistance(img_path):
    first_image = cv2.imread(img_path)
    # cv2.imshow('first image',first_image)

    marker = find_marker(first_image)
    # 得到最小外接矩形的中心点坐标，长宽，旋转角度
    # 其中marker[1][0]是该矩形的宽度，单位为像素

    focalLength = (marker[1][0] * KNOWN_DISTANCE) / KNOWN_WIDTH
    # 获取摄像头的焦距

    print('焦距（focalLength ）= ', focalLength)
    # 将计算得到的焦距打印出来

    return focalLength


def calculate_Distance(image_path, focalLength_value):
    # 加载每一个图像的路径，读取照片，找到A4纸的轮廓
    # 然后计算A4纸到摄像头的距离

    image = cv2.imread(image_path)
    cv2.imshow("image", image)
    cv2.waitKey(300)

    marker = find_marker(image)
    distance_inches = distance_to_camera(KNOWN_WIDTH, focalLength_value, marker[1][0])
    # 计算得到目标物体到摄像头的距离，单位为英寸，
    # 注意，英寸与cm之间的单位换算为： 1英寸=2.54cm

    box = cv2.boxPoints(marker)
    # print( box )，输出类似如下：
    # [[508.09482  382.58597]
    #  [101.76947  371.29916]
    #  [109.783356 82.79956]
    #  [516.1087   94.086365]]

    box = np.int0(box)
    # 将box数组中的每个坐标值都从浮点型转换为整形
    # print( box )，输出类似如下：
    # [[508 382]
    #  [101 371]
    #  [109 82]
    #  [516 94]]

    cv2.drawContours(image, [box], -1, (0, 0, 255), 2)
    # 在原图上绘制出目标物体的轮廓

    cv2.putText(image, "%.2fcm" % (distance_inches * 2.54),
                (image.shape[1] - 300, image.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX,
                2.0, (0, 0, 255), 3)
    # cv2.putText()函数可以在照片上添加文字
    # cv2.putText(img, txt, (int(x),int(y)), fontFace, fontSize, fontColor, fontThickness)
    # 各参即为：照片/添加的文字/左上角坐标/字体/字体大小/颜色/字体粗细

    cv2.imshow("image", image)


if __name__ == "__main__":
    img_path = "./img/Piture2.jpg"
    focalLength = calculate_focalDistance(img_path)
    # 获得摄像头焦

    for image_path in IMAGE_PATHS:
        calculate_Distance(image_path, focalLength)
        cv2.waitKey(1000)
    cv2.destroyAllWindows()

