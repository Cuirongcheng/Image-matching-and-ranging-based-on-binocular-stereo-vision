import cv2
import glob
import numpy as np

'''
cbraw和cbcol是我自己加的。tutorial用的棋盘足够大包含了7×6以上
个角点，我自己用的只有6×4。这里如果角点维数超出的话，标定的时候会报错。
'''
cbraw = 8
cbcol = 6
# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((cbraw * cbcol, 3), np.float32)
'''
设定世界坐标下点的坐标值，因为用的是棋盘可以直接按网格取；
假定棋盘正好在x-y平面上，这样z值直接取0，简化初始化步骤。
mgrid把列向量[0:cbraw]复制了cbcol列，把行向量[0:cbcol]复制了cbraw行。
转置reshape后，每行都是4×6网格中的某个点的坐标。
'''
objp[:, :2] = np.mgrid[0:cbraw, 0:cbcol].T.reshape(-1, 2)

objpoints = []  # 3d point in real world space
imgpoints = []  # 2d points in image plane.
# glob是个文件名管理工具
images = glob.glob('./calibrateImages/Left/*.jpg')
for fname in images:
    # 对每张图片，识别出角点，记录世界物体坐标和图像坐标
    img = cv2.imread(fname)  # source image
    # 我用的图片太大，缩小了一半
    img = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 转灰度
    # cv2.imshow('img',gray)
    # cv2.waitKey(1000)
    # 寻找角点，存入corners，ret是找到角点的flag
    ret, corners = cv2.findChessboardCorners(gray, (8, 6), None)
    # criteria:角点精准化迭代过程的终止条件
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
    # 执行亚像素级角点检测
    corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)

    objpoints.append(objp)
    imgpoints.append(corners2)
    # 在棋盘上绘制角点,只是可视化工具
    img = cv2.drawChessboardCorners(gray, (8, 6), corners2, ret)
    cv2.imshow('img', img)
    # cv2.waitKey(1000)
'''
传入所有图片各自角点的三维、二维坐标，相机标定。
每张图片都有自己的旋转和平移矩阵，但是相机内参和畸变系数只有一组。
mtx，相机内参；dist，畸变系数；revcs，旋转矩阵；tvecs，平移矩阵。
'''
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

print("ret:", ret)
print("内参数矩阵mtx:\n", mtx)  # 内参数矩阵
print("dist:\n", dist)  # 畸变系数   distortion cofficients = (k_1,k_2,p_1,p_2,k_3)
print("rvecs:\n", rvecs)  # 旋转向量  # 外参数
print("tvecs:\n", tvecs)  # 平移向量  # 外参数