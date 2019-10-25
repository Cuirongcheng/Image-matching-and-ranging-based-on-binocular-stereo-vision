# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainmatchwin.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import img
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import cv2
import numpy as np
import time
class Ui_Dialog_match(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 600)
        self.LLabel = QtWidgets.QLabel(Dialog)
        self.LLabel.setGeometry(QtCore.QRect(70, 135, 325, 331))
        self.LLabel.setStyleSheet("font: 14pt \"汉仪喵魂体W\";\n"
"color: rgb(255, 255, 255);\n"
"border:2px;\n"
"border-style:dotted;\n"
"border-color: rgb(135, 229, 169);")
        self.LLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.LLabel.setObjectName("LLabel")
        self.btnSIFTMatch = QtWidgets.QPushButton(Dialog)
        self.btnSIFTMatch.setGeometry(QtCore.QRect(490, 70, 100, 35))
        self.btnSIFTMatch.setStyleSheet("font: 14pt \"汉仪喵魂体W\";\n"
"color: rgb(0,0,0);\n"
"border:2px solid;\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(135, 229, 169);")
        self.btnSIFTMatch.setObjectName("btnSIFTMatch")
        self.btnSURFFeather = QtWidgets.QPushButton(Dialog)
        self.btnSURFFeather.setGeometry(QtCore.QRect(350, 70, 100, 35))
        self.btnSURFFeather.setStyleSheet("font: 14pt \"汉仪喵魂体W\";\n"
"color: rgb(0,0,0);\n"
"border:2px solid;\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(135, 229, 169);")
        self.btnSURFFeather.setObjectName("btnSURFFeather")
        self.btnOpenImage = QtWidgets.QPushButton(Dialog)
        self.btnOpenImage.setGeometry(QtCore.QRect(70, 70, 100, 35))
        self.btnOpenImage.setStyleSheet("font: 14pt \"汉仪喵魂体W\";\n"
"color: rgb(0,0,0);\n"
"border:2px solid;\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(135, 229, 169);")
        self.btnOpenImage.setObjectName("btnOpenImage")
        self.btnSURFMatch = QtWidgets.QPushButton(Dialog)
        self.btnSURFMatch.setGeometry(QtCore.QRect(630, 70, 100, 35))
        self.btnSURFMatch.setStyleSheet("font: 14pt \"汉仪喵魂体W\";\n"
"color: rgb(0,0,0);\n"
"border:2px solid;\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(135, 229, 169);")
        self.btnSURFMatch.setObjectName("btnSURFMatch")
        self.btnSIFTFeather = QtWidgets.QPushButton(Dialog)
        self.btnSIFTFeather.setGeometry(QtCore.QRect(210, 70, 100, 35))
        self.btnSIFTFeather.setStyleSheet("font: 14pt \"汉仪喵魂体W\";\n"
"color: rgb(0,0,0);\n"
"border:2px solid;\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(135, 229, 169);")
        self.btnSIFTFeather.setObjectName("btnSIFTFeather")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.frame.setStyleSheet("border-image: url(:/newPrefix/img/background.jpg);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.ResultLable = QtWidgets.QLabel(Dialog)
        self.ResultLable.setGeometry(QtCore.QRect(70, 485, 660, 70))
        self.ResultLable.setStyleSheet("font: 12pt \"汉仪喵魂体W\";\n"
                                       "color: rgb(0, 0, 0);\n"
                                       "border:2px solid;\n"
                                       "border-color: rgb(255, 255, 255);\n"
                                       "background-color: rgb(135, 229, 169);")
        self.ResultLable.setAlignment(QtCore.Qt.AlignCenter)
        self.ResultLable.setObjectName("ResultLable")
        self.StatusLable = QtWidgets.QLabel(Dialog)
        self.StatusLable.setGeometry(QtCore.QRect(70, 490, 660, 70))
        self.StatusLable.setStyleSheet("font: 12pt \"汉仪喵魂体W\";\n"
                                       "color: rgb(0, 0, 0);\n"
                                       "border:2px solid;\n"
                                       "border-color: rgb(255, 255, 255);\n"
                                       "background-color: rgb(135, 229, 169);")
        self.StatusLable.setAlignment(QtCore.Qt.AlignCenter)
        self.StatusLable.setObjectName("StatusLable")
        self.RLabel = QtWidgets.QLabel(Dialog)
        self.RLabel.setGeometry(QtCore.QRect(405, 135, 325, 331))
        self.RLabel.setStyleSheet("font: 14pt \"汉仪喵魂体W\";\n"
"color: rgb(255, 255, 255);\n"
"border:2px;\n"
"border-style:dotted;\n"
"border-color: rgb(135, 229, 169);")
        self.RLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.RLabel.setObjectName("RLabel")
        self.MatchLabel = QtWidgets.QLabel(Dialog)
        self.MatchLabel.setGeometry(QtCore.QRect(70, 135, 660, 330))
        self.MatchLabel.setStyleSheet("font: 14pt \"汉仪喵魂体W\";\n"
"color: rgb(255, 255, 255);\n"
"border:2px;\n"
"border-style:dotted;\n"
"border-color: rgb(135, 229, 169);")
        self.MatchLabel.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.MatchLabel.setObjectName("MatchLabel")
        self.MatchLabel.setVisible(False)
        self.frame.raise_()
        self.LLabel.raise_()
        self.btnSIFTMatch.raise_()
        self.btnSURFFeather.raise_()
        self.btnOpenImage.raise_()
        self.btnSURFMatch.raise_()
        self.btnSIFTFeather.raise_()
        self.ResultLable.raise_()
        self.StatusLable.raise_()
        self.StatusLable.setVisible(False)
        self.RLabel.raise_()
        self.MatchLabel.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "图像匹配"))
        self.LLabel.setText(_translate("Dialog", "左图像区域"))
        self.btnSIFTMatch.setText(_translate("Dialog", "SIFT匹配"))
        self.btnSURFFeather.setText(_translate("Dialog", "SURF特征"))
        self.btnOpenImage.setText(_translate("Dialog", "打开图像"))
        self.btnSURFMatch.setText(_translate("Dialog", "SURF匹配"))
        self.btnSIFTFeather.setText(_translate("Dialog", "SIFT特征"))
        self.ResultLable.setText(_translate("Dialog", "状态显示区域"))
        self.StatusLable.setText(_translate("Dialog", "结果显示区域"))
        self.RLabel.setText(_translate("Dialog", "右图像区域"))
        self.MatchLabel.setText(_translate("Dialog", "匹配图像区域"))

        # -------------------------设置按钮点击事件-------------------------------------
        self.btnOpenImage.clicked.connect(self.openImage)
        self.btnSIFTFeather.clicked.connect(self.siftFeature)
        self.btnSURFFeather.clicked.connect(self.surfFeature)
        self.btnSIFTMatch.clicked.connect(self.siftMatch)
        self.btnSURFMatch.clicked.connect(self.surfMatch)

    def openImage(self):
        self.imgName, self.imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "*.bmp;;*.jpg;;*.png;;All Files(*)")
        self.img = QtGui.QPixmap(self.imgName).scaled(self.LLabel.width(), self.LLabel.height())
        self.LLabel.setPixmap(self.img)
        self.ResultLable.setText("左图像打开成功！")
        self.imgName2, self.imgType2 = QFileDialog.getOpenFileName(self, "打开图片", "", "*.bmp;;*.jpg;;*.png;;All Files(*)")
        self.img2 = QtGui.QPixmap(self.imgName2).scaled(self.RLabel.width(), self.RLabel.height())
        self.RLabel.setPixmap(self.img2)
        self.ResultLable.setText("右图像打开成功！")
        self.ResultLable.setText("图像打开成功！\n"
                                 "左图像打开路径：" + str(self.imgName) + "\n"
                                 "右图像打开路径：" + str(self.imgName2))

    def siftFeature(self):
        # 设置算法运行开始时间
        start = time.clock()

        # 左图像提取
        print(self.imgName)
        # 获取图像路径
        self.img_sift = cv2.imread(self.imgName)
        # 灰度处理
        self.gray_sift = cv2.cvtColor(self.img_sift, cv2.COLOR_BGR2GRAY)
        # 使用SIFT算法
        sift = cv2.xfeatures2d.SIFT_create()
        # 找到关键点和描述符
        self.kp_sift, self.desc_sift = sift.detectAndCompute(self.gray_sift, None)
        # 输出特征点个数
        print(len(self.kp_sift))
        # 绘制关键点
        self.img_sift_draw = cv2.drawKeypoints(self.gray_sift, self.kp_sift, self.img_sift)
        # opencv图像对象转换成qtQImage对象
        # self.Llabel.setPixmap(img)
        self.QtImgSIFT = QtGui.QImage(self.img_sift_draw.data,
                                  self.img_sift_draw.shape[1],
                                  self.img_sift_draw.shape[0],
                                  QtGui.QImage.Format_RGB888)
        self.LLabel.setPixmap(QtGui.QPixmap.fromImage(self.QtImgSIFT))
        cv2.imshow('testSIFT', self.img_sift_draw)
        self.ResultLable.setText("左图像SIFT特征提取成功！")

        #右图像提取
        print(self.imgName2)
        # 获取图像路径
        self.img_sift2 = cv2.imread(self.imgName2)
        # 灰度处理
        self.gray_sift2 = cv2.cvtColor(self.img_sift2, cv2.COLOR_BGR2GRAY)
        # 使用SIFT算法
        sift = cv2.xfeatures2d.SIFT_create()
        # 找到关键点和描述符
        self.kp_sift2, self.desc_sift2 = sift.detectAndCompute(self.gray_sift2, None)
        # 输出特征点个数
        print(len(self.kp_sift2))
        # 绘制关键点
        self.img_sift_draw2 = cv2.drawKeypoints(self.gray_sift2, self.kp_sift2, self.img_sift2)
        # opencv图像对象转换成qtQImage对象
        # self.Llabel.setPixmap(img)
        self.QtImgSIFT2 = QtGui.QImage(self.img_sift_draw2.data,
                                      self.img_sift_draw2.shape[1],
                                      self.img_sift_draw2.shape[0],
                                      QtGui.QImage.Format_RGB888)
        self.RLabel.setPixmap(QtGui.QPixmap.fromImage(self.QtImgSIFT2))
        cv2.imshow('testSIFT2', self.img_sift_draw2)
        self.ResultLable.setText("右图像SIFT特征提取成功！")

        # 输出特征点个数
        print("SIFT Feature number:",len(self.kp_sift)+len(self.kp_sift2))
        # 算法结束时间
        self.sift_time = (time.clock() - start)
        print("SIFT Time used:", self.sift_time)
        self.ResultLable.setText("图像SIFT特征提取成功！\n "
                                 "左图像提取特征点个数：" + str(len(self.kp_sift)) +"，右图像提取特征点个数：" + str(len(self.kp_sift2)) + "\n" +
                                 "总提取个数：" + str(len(self.kp_sift)+len(self.kp_sift2)) + "，总提取时间：" + str(self.sift_time))

    def surfFeature(self):
        # 设置算法运行开始时间
        start = time.clock()

        # 左图像提取
        print(self.imgName)
        # 获取图像路径
        self.img_surf = cv2.imread(self.imgName)
        # 灰度处理
        self.gray_surf = cv2.cvtColor(self.img_surf, cv2.COLOR_BGR2GRAY)
        # 参数为hessian矩阵的阈值
        surf = cv2.xfeatures2d.SURF_create(400)
        # 找到关键点和描述符
        self.kp_surf, self.desc_surf = surf.detectAndCompute(self.img_surf, None)
        # 输出特征点个数
        print(len(self.kp_surf))
        # 把特征点标记到图片上
        self.img_surf_draw = cv2.drawKeypoints(self.gray_surf, self.kp_surf, self.img_surf)
        # opencv图像对象转换成qtQImage对象
        self.QtImgSURF = QtGui.QImage(self.img_surf_draw.data,
                                  self.img_surf_draw.shape[1],
                                  self.img_surf_draw.shape[0],
                                  QtGui.QImage.Format_RGB888)
        self.LLabel.setPixmap(QtGui.QPixmap.fromImage(self.QtImgSURF))
        cv2.imshow('testSURF', self.img_surf_draw)
        # print("左ok")
        self.ResultLable.setText("左图像SURF特征提取成功！")

        # 右图像提取
        print(self.imgName2)
        # 获取图像路径
        self.img_surf2 = cv2.imread(self.imgName2)
        # 灰度处理
        self.gray_surf2 = cv2.cvtColor(self.img_surf2, cv2.COLOR_BGR2GRAY)
        # 参数为hessian矩阵的阈值
        surf = cv2.xfeatures2d.SURF_create(400)
        # 找到关键点和描述符
        self.kp_surf2, self.desc_surf2 = surf.detectAndCompute(self.img_surf2, None)
        # 输出特征点个数
        print(len(self.kp_surf2))
        # 把特征点标记到图片上
        self.img_surf_draw2 = cv2.drawKeypoints(self.gray_surf2, self.kp_surf2, self.img_surf2)
        # opencv图像对象转换成qtQImage对象
        self.QtImgSURF2 = QtGui.QImage(self.img_surf_draw2.data,
                                      self.img_surf_draw2.shape[1],
                                      self.img_surf_draw2.shape[0],
                                      QtGui.QImage.Format_RGB888)
        self.RLabel.setPixmap(QtGui.QPixmap.fromImage(self.QtImgSURF2))
        cv2.imshow('testSURF2',  self.img_surf_draw2)
        # print("右ok")
        self.ResultLable.setText("右图像SURF特征提取成功！")

        # 输出特征点个数
        print("SURF Feature number:", len(self.kp_surf) + len(self.kp_surf2))
        # 算法结束时间
        self.surf_time = (time.clock() - start)
        print("SURF Time used:", self.surf_time)
        self.ResultLable.setText("图像SURF特征提取成功！\n "
                                 "左图像提取特征点个数：" + str(len(self.kp_surf)) + "，右图像提取特征点个数：" + str(len(self.kp_surf2)) + "\n" +
                                 "总提取个数：" + str(len(self.kp_surf) + len(self.kp_surf2)) + "，总提取时间：" + str(self.surf_time))


    def siftMatch(self):
        # 设置算法运行开始时间
        start = time.clock()

        # 打开图像
        img1 = cv2.imread(self.imgName)
        img2 = cv2.imread(self.imgName2)
        # print("open")
        # 图像灰度处理
        img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
        # print("gray")
        # sift = cv2.SIFT()
        # sift = cv2.SURF()
        # 调用sift算法
        sift = cv2.xfeatures2d.SIFT_create()
        # print("sift")
        # 提取特征点
        kp1, des1 = sift.detectAndCompute(img1_gray, None)
        kp2, des2 = sift.detectAndCompute(img2_gray, None)
        # print("kp")
        # BFmatcher with default parms
        bf = cv2.BFMatcher(cv2.NORM_L2)
        matches = bf.knnMatch(des1, des2, k=2)
        # print("match")
        goodMatch = []
        for m, n in matches:
            if m.distance < 0.50 * n.distance:
                goodMatch.append(m)
        # print("append")
        # self.drawMatchesKnn_cv2(img1_gray, kp1, img2_gray, kp2, goodMatch[:20])

        # 增加一个维度
        goodMatch = np.expand_dims(goodMatch, 1)
        # print(goodMatch[:20])

        # 进行特征匹配
        img_out = cv2.drawMatchesKnn(img1_gray, kp1, img2_gray, kp2, goodMatch[:15], None, flags=2)

        cv2.imshow('SIFTMatch', img_out)  # 展示图片
        # cv2.waitKey(0)  # 等待按键按下
        # cv2.destroyAllWindows()  # 清除所有窗口

        # 算法结束时间
        self.sift_Match_time = (time.clock() - start)
        print("SIFT Match Time used:", self.sift_Match_time)
        self.ResultLable.setText("图像SIFT特征匹配成功！\n "
                                 "SIFT + BF优化匹配特征点对数：15\n"
                                 "SIFT + BF算法总用时：" + str(self.sift_Match_time))

    def surfMatch(self):
        # 设置算法运行开始时间
        start = time.clock()

        # 打开图像
        img1 = cv2.imread(self.imgName)
        img2 = cv2.imread(self.imgName2)
        # print("open")
        # 图像灰度处理
        img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
        # print("gray")
        # sift = cv2.SIFT()
        # sift = cv2.SURF()
        # 调用sift算法
        surf = cv2.xfeatures2d.SURF_create()
        # print("sift")
        # 提取特征点
        kp1, des1 = surf.detectAndCompute(img1_gray, None)
        kp2, des2 = surf.detectAndCompute(img2_gray, None)
        # print("kp")
        # BFmatcher with default parms
        bf = cv2.BFMatcher(cv2.NORM_L2)
        matches = bf.knnMatch(des1, des2, k=2)
        # print("match")
        goodMatch = []
        for m, n in matches:
            if m.distance < 0.50 * n.distance:
                goodMatch.append(m)
        # print("append")
        # self.drawMatchesKnn_cv2(img1_gray, kp1, img2_gray, kp2, goodMatch[:20])

        # 增加一个维度
        goodMatch = np.expand_dims(goodMatch, 1)
        # print(goodMatch[:20])

        # 进行特征匹配
        img_out = cv2.drawMatchesKnn(img1_gray, kp1, img2_gray, kp2, goodMatch[:15], None, flags=2)

        cv2.imshow('SURFMatch', img_out)  # 展示图片
        # cv2.waitKey(0)  # 等待按键按下
        # cv2.destroyAllWindows()  # 清除所有窗口

        # 算法结束时间
        self.surf_Match_time = (time.clock() - start)
        print("SURF Match Time used:", self.surf_Match_time)
        self.ResultLable.setText("图像SURF特征匹配成功！\n "
                                 "SURF + BF优化匹配特征点对数：15\n"
                                 "SURF + BF算法总用时：" + str(self.surf_Match_time))

class MyWindow(QtWidgets.QMainWindow, Ui_Dialog_match):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    sys.exit(app.exec_())

