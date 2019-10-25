# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'maincountwin.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import img
import cv2
import numpy as np
import glob
import camera_configs
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog

class Ui_Dialog_count(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 600)
        self.RLabel = QtWidgets.QLabel(Dialog)
        self.RLabel.setGeometry(QtCore.QRect(405, 135, 325, 331))
        self.RLabel.setStyleSheet("font: 14pt \"汉仪喵魂体W\";\n"
"color: rgb(255, 255, 255);\n"
"border:2px;\n"
"border-style:dotted;\n"
"border-color: rgb(129, 211, 222);")
        self.RLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.RLabel.setObjectName("RLabel")
        self.btnOpenImage = QtWidgets.QPushButton(Dialog)
        self.btnOpenImage.setGeometry(QtCore.QRect(210, 70, 100, 35))
        self.btnOpenImage.setStyleSheet("font: bold 14pt \"汉仪喵魂体W\";\n"
"color: rgb(0, 0, 0);\n"
"border:2px solid;\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(129, 211, 222);")
        self.btnOpenImage.setObjectName("btnOpenImage")
        self.btnImageGrey = QtWidgets.QPushButton(Dialog)
        self.btnImageGrey.setGeometry(QtCore.QRect(490, 70, 100, 35))
        self.btnImageGrey.setStyleSheet("font: bold 14pt \"汉仪喵魂体W\";\n"
"color: rgb(0, 0, 0);\n"
"border:2px solid;\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(129, 211, 222);")
        self.btnImageGrey.setObjectName("btnImageGrey")
        self.LLabel = QtWidgets.QLabel(Dialog)
        self.LLabel.setGeometry(QtCore.QRect(70, 135, 325, 331))
        self.LLabel.setStyleSheet("font: 14pt \"汉仪喵魂体W\";\n"
"color: rgb(255, 255, 255);\n"
"border:2px;\n"
"border-style:dotted;\n"
"border-color: rgb(129, 211, 222);")
        self.LLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.LLabel.setObjectName("LLabel")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.frame.setStyleSheet("border-image: url(:/newPrefix/img/background.jpg);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.ResultLabel = QtWidgets.QLabel(Dialog)
        self.ResultLabel.setGeometry(QtCore.QRect(70, 485, 660, 70))
        self.ResultLabel.setStyleSheet("font: 12pt \"汉仪喵魂体W\";\n"
"color: rgb(0, 0, 0);\n"
"border:2px solid;\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(129, 211, 222);")
        self.ResultLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ResultLabel.setObjectName("ResultLabel")
        self.btnImageReset = QtWidgets.QPushButton(Dialog)
        self.btnImageReset.setGeometry(QtCore.QRect(350, 70, 100, 35))
        self.btnImageReset.setStyleSheet("font: bold 14pt \"汉仪喵魂体W\";\n"
"color: rgb(0, 0, 0);\n"
"border:2px solid;\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(129, 211, 222);")
        self.btnImageReset.setObjectName("btnImageReset")
        self.btnCamCalibrate = QtWidgets.QPushButton(Dialog)
        self.btnCamCalibrate.setGeometry(QtCore.QRect(70, 70, 100, 35))
        self.btnCamCalibrate.setStyleSheet("font: bold 14pt \"汉仪喵魂体W\";\n"
"color: rgb(0, 0, 0);\n"
"border:2px solid;\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(129, 211, 222);")
        self.btnCamCalibrate.setObjectName("btnCamCalibrate")
        self.btnCount = QtWidgets.QPushButton(Dialog)
        self.btnCount.setGeometry(QtCore.QRect(630, 70, 100, 35))
        self.btnCount.setStyleSheet("font: bold 14pt \"汉仪喵魂体W\";\n"
"color: rgb(0, 0, 0);\n"
"border:2px solid;\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(129, 211, 222);")
        self.btnCount.setObjectName("btnCount")
        self.frame.raise_()
        self.RLabel.raise_()
        self.btnOpenImage.raise_()
        self.btnImageGrey.raise_()
        self.LLabel.raise_()
        self.ResultLabel.raise_()
        self.btnImageReset.raise_()
        self.btnCamCalibrate.raise_()
        self.btnCount.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "测量距离"))
        self.RLabel.setText(_translate("Dialog", "右图像区域"))
        self.btnOpenImage.setText(_translate("Dialog", "打开图像"))
        self.btnImageGrey.setText(_translate("Dialog", "图像灰度化"))
        self.LLabel.setText(_translate("Dialog", "左图像区域"))
        self.ResultLabel.setText(_translate("Dialog", "结果显示区域"))
        self.btnImageReset.setText(_translate("Dialog", "图像重构"))
        self.btnCamCalibrate.setText(_translate("Dialog", "相机标定"))
        self.btnCount.setText(_translate("Dialog", "深度测距"))

        # -------------------------设置按钮点击事件-------------------------------------
        self.btnCamCalibrate.clicked.connect(self.camCalibrate)
        self.btnOpenImage.clicked.connect(self.openImage)
        self.btnImageReset.clicked.connect(self.imageReset)
        self.btnImageGrey.clicked.connect(self.imageGray)
        self.btnCount.clicked.connect(self.dispCount)

    def camCalibrate(self):
        # 找棋盘格角点
        # 阈值
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
        # 棋盘格模板规格
        w = 8
        h = 6
        # 世界坐标系中的棋盘格点,例如(0,0,0), (1,0,0), (2,0,0) ....,(8,5,0)，去掉Z坐标，记为二维矩阵
        objp = np.zeros((w * h, 3), np.float32)
        objp[:, :2] = np.mgrid[0:w, 0:h].T.reshape(-1, 2)
        # 储存棋盘格角点的世界坐标和图像坐标对
        objpoints = []  # 在世界坐标系中的三维点
        imgpoints = []  # 在图像平面的二维点

        imagesL = glob.glob('E:/PycharmProject/demo2/calibrateImages/Left/*.bmp')
        for fname in imagesL:
            img = cv2.imread(fname)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # 找到棋盘格角点
            ret, corners = cv2.findChessboardCorners(gray, (w, h), None)
            # 如果找到足够点对，将其存储起来
            if ret == True:
                cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
                objpoints.append(objp)
                imgpoints.append(corners)
                # 将角点在图像上显示
                cv2.drawChessboardCorners(img, (w, h), corners, ret)
                cv2.destroyAllWindows()
                cv2.imshow('LeftfindCorners', img)
                self.QtImg = QtGui.QImage(img.data,
                                          img.shape[1],
                                          img.shape[0],
                                          QtGui.QImage.Format_RGB888)
                self.LLabel.setPixmap(QtGui.QPixmap.fromImage(self.QtImg))
                cv2.waitKey(1)

        self.ret, self.mtx, self.dist,self.rvecs, self.tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
        print(("ret:"), self.ret)
        print(("mtx:\n"), self.mtx)  # 内参数矩阵
        print(("dist:\n"), self.dist)  # 畸变系数   distortion cofficients = (k_1,k_2,p_1,p_2,k_3)
        print(("rvecs:\n"), self.rvecs)  # 旋转向量  # 外参数
        print(("tvecs:\n"), self.tvecs)  # 平移向量  # 外参数
        fw = open("leftparam.txt", "w")
        fw.write(("ret:") + str(self.ret) + "\n")
        fw.write(("mtx:\n") + str(self.mtx) + "\n")  # 内参数矩阵
        fw.write(("dist:\n") + str(self.dist) + "\n")  # 畸变系数   distortion cofficients = (k_1,k_2,p_1,p_2,k_3)
        fw.write(("rvecs:\n") + str(self.rvecs) + "\n")  # 旋转向量  # 外参数
        fw.write(("tvecs:\n") + str(self.tvecs) + "\n")  # 平移向量  # 外参数
        fw.close()

        imagesL = glob.glob('E:/PycharmProject/demo2/calibrateImages/Right/*.bmp')
        for fname in imagesL:
            img = cv2.imread(fname)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # 找到棋盘格角点
            ret, corners = cv2.findChessboardCorners(gray, (w, h), None)
            # 如果找到足够点对，将其存储起来
            print("ok")
            if ret == True:
                cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
                objpoints.append(objp)
                imgpoints.append(corners)
                # 将角点在图像上显示
                cv2.drawChessboardCorners(img, (w, h), corners, ret)
                cv2.destroyAllWindows()
                cv2.imshow('RightfindCorners', img)
                self.QtImg = QtGui.QImage(img.data,
                                          img.shape[1],
                                          img.shape[0],
                                          QtGui.QImage.Format_RGB888)
                self.RLabel.setPixmap(QtGui.QPixmap.fromImage(self.QtImg))
                cv2.waitKey(1)
        cv2.destroyAllWindows()

        self.ret2, self.mtx2, self.dist2, self.rvecs2, self.tvecs2 = cv2.calibrateCamera(objpoints, imgpoints,gray.shape[::-1], None, None)
        print(("ret:"), self.ret2)
        print(("mtx:\n"), self.mtx2)  # 内参数矩阵
        print(("dist:\n"), self.dist2)  # 畸变系数   distortion cofficients = (k_1,k_2,p_1,p_2,k_3)
        print(("rvecs:\n"), self.rvecs2)  # 旋转向量  # 外参数
        print(("tvecs:\n"), self.tvecs2)  # 平移向量  # 外参数
        fw = open("rightparam.txt", "w")
        fw.write(("ret:") + str(self.ret2) + "\n")
        fw.write(("mtx:\n") + str(self.mtx2) + "\n")  # 内参数矩阵
        fw.write(("dist:\n") + str(self.dist2) + "\n")  # 畸变系数   distortion cofficients = (k_1,k_2,p_1,p_2,k_3)
        fw.write(("rvecs:\n") + str(self.rvecs2) + "\n")  # 旋转向量  # 外参数
        fw.write(("tvecs:\n") + str(self.tvecs2) + "\n")  # 平移向量  # 外参数
        fw.close()

        self.ResultLabel.setText("相机标定成功！标定结果保存到./leftparam.txt和./rightparam.txt")

    def openImage(self):
        self.imgName, self.imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "*.bmp;;*.jpg;;*.png;;All Files(*)")
        self.img = QtGui.QPixmap(self.imgName).scaled(self.LLabel.width(), self.LLabel.height())
        self.LLabel.setPixmap(self.img)
        self.ResultLabel.setText("左图像打开成功！")
        self.imgName2, self.imgType2 = QFileDialog.getOpenFileName(self, "打开图片", "", "*.bmp;;*.jpg;;*.png;;All Files(*)")
        self.img2 = QtGui.QPixmap(self.imgName2).scaled(self.RLabel.width(), self.RLabel.height())
        self.RLabel.setPixmap(self.img2)
        self.ResultLabel.setText("右图像打开成功！")
        self.ResultLabel.setText("图像打开成功！\n"
                                 "左图像打开路径：" + str(self.imgName) + "\n"
                                 "右图像打开路径：" + str(self.imgName2))

    def imageReset(self):
        # 打开图像
        frame1 = cv2.imread(self.imgName)
        frame2 = cv2.imread(self.imgName2)
        # 根据打开的图像和相机参数更正map对图片进行重构
        self.img1_rectified = cv2.remap(frame1, camera_configs.left_map1, camera_configs.left_map2, cv2.INTER_LINEAR)
        self.img2_rectified = cv2.remap(frame2, camera_configs.right_map1, camera_configs.right_map2, cv2.INTER_LINEAR)
        self.QtImg1 = QtGui.QImage(self.img1_rectified.data,
                                   self.img1_rectified.shape[1],
                                   self.img1_rectified.shape[0],
                                   QtGui.QImage.Format_RGB888)
        self.LLabel.setPixmap(QtGui.QPixmap.fromImage(self.QtImg1))
        self.QtImg2 = QtGui.QImage(self.img2_rectified.data,
                                   self.img2_rectified.shape[1],
                                   self.img2_rectified.shape[0],
                                   QtGui.QImage.Format_RGB888)
        self.RLabel.setPixmap(QtGui.QPixmap.fromImage(self.QtImg2))
        cv2.imshow("rect1", self.img1_rectified)
        cv2.imshow("rect2", self.img2_rectified)
        self.ResultLabel.setText("图像重构成功！")

    def imageGray(self):
        # 将图片置为灰度图，为StereoBM作准备
        self.imgL = cv2.cvtColor(self.img1_rectified, cv2.COLOR_BGR2GRAY)
        self.imgR = cv2.cvtColor(self.img2_rectified, cv2.COLOR_BGR2GRAY)
        self.QtImgL = QtGui.QImage(self.imgL.data,
                                   self.imgL.shape[1],
                                   self.imgL.shape[0],
                                   QtGui.QImage.Format_RGB888)
        self.LLabel.setPixmap(QtGui.QPixmap.fromImage(self.QtImgL))
        self.QtImgR = QtGui.QImage(self.imgR.data,
                                   self.imgR.shape[1],
                                   self.imgR.shape[0],
                                   QtGui.QImage.Format_RGB888)
        self.RLabel.setPixmap(QtGui.QPixmap.fromImage(self.QtImgR))
        cv2.imshow("gray1", self.imgL)
        cv2.imshow("gray2", self.imgR)
        self.ResultLabel.setText("图像灰度化成功！")

    def dispCount(self):
        # 添加点击事件，打印当前点的距离

        def callbackFunc(e, x, y, f, p):
            if e == cv2.EVENT_LBUTTONDOWN:
                print(x, y)
                # print(threeD)
                str1 = ' '
                str2 = str1.join(str(i) for i in threeD[y][x])
                # print(isinstance(str2, str))
                # print(isinstance(str2, int))
                # print(str2)
                # print(str(str2))
                print(threeD[y][x])
                fw = open("result.txt", "w")
                fw.write("匹配点对图像像素坐标：（" + str(x) + ", " + str(y) + ")\n" + "对应特征点三维坐标：" + str2)
                fw.close()
                self.ResultLabel.setText("匹配点对图像像素坐标：（" + str(x) + ", " + str(y) + ")\n" +
                                         "对应特征点三维坐标：（" + str2 + "）")


        while True:
            # 两个trackbar用来调节不同的参数查看效果
            num = cv2.getTrackbarPos("num", "depth")
            blockSize = cv2.getTrackbarPos("blockSize", "depth")
            if blockSize % 2 == 0:
                blockSize += 1
            if blockSize < 5:
                blockSize = 5

            # 根据Block Maching方法生成差异图（opencv里也提供了SGBM/Semi-Global Block Matching算法）
            stereo = cv2.StereoBM_create(numDisparities=16 * num, blockSize=blockSize)
            # stereo = cv2.StereoSGBM_create(numDisparities=16 * num, blockSize=blockSize)
            disparity = stereo.compute(self.imgL, self.imgR)

            disp = cv2.normalize(disparity, disparity, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
            # 将图片扩展至3d空间中，其z方向的值则为当前的距离
            threeD = cv2.reprojectImageTo3D(disparity.astype(np.float32) / 16., camera_configs.Q)

            cv2.imshow("depth", disp)
            key = cv2.waitKey(1)
            if key == ord("q"):
                break

            cv2.setMouseCallback("depth", callbackFunc, None)
        cv2.destroyAllWindows()

class MyWindow(QtWidgets.QMainWindow, Ui_Dialog_count):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    sys.exit(app.exec_())

