# #!usr/bin/python
# # -*- coding: utf-8 -*-
# # 定义编码，中文注释
#
# # import the necessary packages
# import numpy as np
# import cv2
#
#
# # 找到目标函数
# def find_marker(image):
#     # convert the image to grayscale, blur it, and detect edges
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     gray = cv2.GaussianBlur(gray, (5, 5), 0)
#     edged = cv2.Canny(gray, 35, 125)
#
#     # find the contours in the edged image and keep the largest one;
#     # we'll assume that this is our piece of paper in the image
#     # (cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
#     (_, cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
#
#     # 求最大面积
#     c = max(cnts, key=cv2.contourArea)
#
#     # compute the bounding box of the of the paper region and return it
#     # cv2.minAreaRect() c代表点集，返回rect[0]是最小外接矩形中心点坐标，
#     # rect[1][0]是width，rect[1][1]是height，rect[2]是角度
#     return cv2.minAreaRect(c)
#
#
# # 距离计算函数
# def distance_to_camera(knownWidth, focalLength, perWidth):
#     # compute and return the distance from the maker to the camera
#     return (knownWidth * focalLength) / perWidth
#
#
# # initialize the known distance from the camera to the object, which
# # in this case is 24 inches
# KNOWN_DISTANCE = 24.0
#
# # initialize the known object width, which in this case, the piece of
# # paper is 11 inches wide
# # A4纸的长和宽(单位:inches)
# KNOWN_WIDTH = 11.69
# KNOWN_HEIGHT = 8.27
#
# # initialize the list of images that we'll be using
# IMAGE_PATHS = ["./Picture1.jpg", "./Picture2.jpg", "./Picture3.jpg"]
#
# # load the furst image that contains an object that is KNOWN TO BE 2 feet
# # from our camera, then find the paper marker in the image, and initialize
# # the focal length
# # 读入第一张图，通过已知距离计算相机焦距
# image = cv2.imread(IMAGE_PATHS[0])
# marker = find_marker(image)
# focalLength = (marker[1][0] * KNOWN_DISTANCE) / KNOWN_WIDTH
#
# # 通过摄像头标定获取的像素焦距
# # focalLength = 811.82
# print('focalLength = ', focalLength)
#
# # 打开摄像头
# camera = cv2.VideoCapture(0)
#
# while camera.isOpened():
#     # get a frame
#     (grabbed, frame) = camera.read()
#     marker = find_marker(frame)
#     if marker == 0:
#         print(marker)
#         continue
#     inches = distance_to_camera(KNOWN_WIDTH, focalLength, marker[1][0])
#
#     # draw a bounding box around the image and display it
#     # box = np.int0(cv2.cv.BoxPoints(marker))
#     box = cv2.boxPoints(marker)
#     box = np.int0(box)
#
#     cv2.drawContours(frame, [box], -1, (0, 255, 0), 2)
#
#     # inches 转换为 cm
#     cv2.putText(frame, "%.2fcm" % (inches * 30.48 / 12),
#                 (frame.shape[1] - 200, frame.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX,
#                 2.0, (0, 255, 0), 3)
#
#     # show a frame
#     cv2.imshow("capture", frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# camera.release()
# cv2.destroyAllWindows()
#

# !/usr/bin/python
# -*- coding: utf-8 -*-
import cv2
import time

AUTO = True  # 自动拍照，或手动按s键拍照
INTERVAL = 2  # 自动拍照间隔

cv2.namedWindow("left")
cv2.namedWindow("right")
cv2.moveWindow("left", 0, 0)
cv2.moveWindow("right", 400, 0)
left_camera = cv2.VideoCapture(0)
# cv2.waitKey(50)
# left_camera.set(cv2.CV_CAP_PROP_FRAME_WIDTH,320)
# left_camera.set(cv2.CV_CAP_PROP_FRAME_HEIGHT,240)
right_camera = cv2.VideoCapture(1)
# right_camera.set(cv2.CV_CAP_PROP_FRAME_WIDTH,320)
# right_camera.set(cv2.CV_CAP_PROP_FRAME_HEIGHT,240)

counter = 0
utc = time.time()
pattern = (12, 8)  # 棋盘格尺寸
folder = "./snapshot/"  # 拍照文件目录


def shot(pos, frame):
    global counter
    path = folder + pos + "_" + str(counter) + ".jpg"

    cv2.imwrite(path, frame)
    print("snapshot saved into: " + path)


while True:
    ret, left_frame = left_camera.read()
    ret, right_frame = right_camera.read()

    cv2.imshow("left", left_frame)
    cv2.imshow("right", right_frame)

    now = time.time()
    if AUTO and now - utc >= INTERVAL:
        shot("left", left_frame)
        shot("right", right_frame)
        counter += 1
        utc = now

    key = cv2.waitKey(1)
    if key == ord("q"):
        break
    elif key == ord("s"):
        shot("left", left_frame)
        shot("right", right_frame)
        counter += 1

left_camera.release()
right_camera.release()
cv2.destroyWindow("left")
cv2.destroyWindow("right")

