# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from MVGigE import *
import os
import shutil
import cv2
import sys
import os
import shutil
from MVGigE import *
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QMessageBox, QLabel, QFileDialog, QScrollArea, QComboBox, QLineEdit, QSlider, QGridLayout, QGroupBox, QCheckBox
from PyQt5.QtGui import QPixmap, QPalette, QImage, QIcon
from PyQt5.QtCore import Qt

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(575, 538)
        self.btnOpenCam = QtWidgets.QPushButton(Form)
        self.btnOpenCam.setGeometry(QtCore.QRect(30, 70, 75, 23))
        self.btnOpenCam.setObjectName("btnOpenCam")
        self.btnStartGrab = QtWidgets.QPushButton(Form)
        self.btnStartGrab.setGeometry(QtCore.QRect(150, 70, 75, 23))
        self.btnStartGrab.setObjectName("btnStartGrab")
        self.btnStopGrab = QtWidgets.QPushButton(Form)
        self.btnStopGrab.setGeometry(QtCore.QRect(250, 70, 75, 23))
        self.btnStopGrab.setObjectName("btnStopGrab")
        self.btnSave = QtWidgets.QPushButton(Form)
        self.btnSave.setGeometry(QtCore.QRect(350, 70, 75, 23))
        self.btnSave.setObjectName("btnSave")
        self.btnColseCam = QtWidgets.QPushButton(Form)
        self.btnColseCam.setGeometry(QtCore.QRect(470, 70, 75, 23))
        self.btnColseCam.setObjectName("btnColseCam")
        self.LTitle = QtWidgets.QLabel(Form)
        self.LTitle.setGeometry(QtCore.QRect(200, 10, 191, 21))
        self.LTitle.setStyleSheet("font: 14pt Bold \"方正兰亭超细黑简体\";")
        self.LTitle.setIndent(-1)
        self.LTitle.setObjectName("LTitle")
        self.LLImage = QtWidgets.QLabel(Form)
        self.LLImage.setGeometry(QtCore.QRect(20, 120, 261, 371))
        self.LLImage.setStyleSheet("background-color: rgb(150, 150, 150);")
        self.LLImage.setTextFormat(QtCore.Qt.PlainText)
        self.LLImage.setObjectName("LLImage")
        self.LRImage = QtWidgets.QLabel(Form)
        self.LRImage.setGeometry(QtCore.QRect(300, 120, 261, 371))
        self.LRImage.setStyleSheet("background-color: rgb(150, 150, 150);")
        self.LRImage.setObjectName("LRImage")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btnOpenCam.setText(_translate("Form", "打开相机"))
        self.btnStartGrab.setText(_translate("Form", "开始采集"))
        self.btnStopGrab.setText(_translate("Form", "暂停采集"))
        self.btnSave.setText(_translate("Form", "保存图像"))
        self.btnColseCam.setText(_translate("Form", "特征提取"))
        self.LTitle.setText(_translate("Form", "双目测量测试开发平台"))
        self.LLImage.setText(_translate("Form", "左图像"))
        self.LRImage.setText(_translate("Form", "右图像"))



        #信号槽事件
        self.btnOpenCam.clicked.connect(self.openCam)
        self.btnStartGrab.clicked.connect(self.startGrab)
        self.btnStopGrab.clicked.connect(self.stopGrab)
        self.btnSave.clicked.connect(self.saveImage)
        self.btnColseCam.clicked.connect(self.testSIFT)


    # 点击界面打开相机按钮，执行本函数
    def openCam(self):
        r = MVInitLib()  # 初始化函数库
        if (r != MVSTATUS_CODES.MVST_SUCCESS):
            msgBox = QMessageBox(QMessageBox.Warning, '提示', '函数库初始化失败！')
            msgBox.exec()
            return
        r = MVUpdateCameraList()  # 查找连接到计算机上的相机
        if (r != MVSTATUS_CODES.MVST_SUCCESS):
            msgBox = QMessageBox(QMessageBox.Warning, '提示', '查找连接计算机失败！')
            msgBox.exec()
            return
        nCams = MVGetNumOfCameras()  # 获取相机数量
        if(nCams.status != MVSTATUS_CODES.MVST_SUCCESS):
            msgBox = QMessageBox(QMessageBox.Warning, '提示', nCams.status)
            msgBox.exec()
            return
        if(nCams.num == 0):
            msgBox = QMessageBox(QMessageBox.Warning, '提示', '没有找到相机,请确认连接和相机IP设置!')
            msgBox.exec()
            return

        #左相机
        hCam = MVOpenCamByIndex(0)  # 根据相机的索引返回相机句柄
        if(hCam.hCam == 0):
            if(hCam.status == MVSTATUS_CODES.MVST_ACCESS_DENIED):
                msgBox = QMessageBox(QMessageBox.Warning,'提示', '无法打开相机，可能正被别的软件控制!')
                msgBox.exec()
                return
            else:
                msgBox = QMessageBox(QMessageBox.Warning, '提示', '无法打开相机!')
                msgBox.exec()
                return
        w = MVGetWidth(hCam.hCam)  # 获取图像宽度
        h = MVGetHeight(hCam.hCam)  # 获取图像高度
        pf = MVGetPixelFormat(hCam.hCam)  # 获取图像格式
        self.hCam = hCam.hCam
        self.width = w.width
        self.height = h.height
        self.pixelFormat = pf.pixelFormat
        if(self.pixelFormat == MV_PixelFormatEnums.PixelFormat_Mono8):
            self.himage = MVImageCreate(self.width, self.height, 8).himage  # 创建图像句柄
        else:
            self.himage = MVImageCreate(self.width, self.height, 24).himage  # 创建图像句柄
        self.LLImage.resize(self.width*0.18, self.height*0.3)

        #右相机
        hCam2 = MVOpenCamByIndex(1)  # 根据相机的索引返回相机句柄
        if (hCam2.hCam == 0):
            if (hCam2.status == MVSTATUS_CODES.MVST_ACCESS_DENIED):
                msgBox = QMessageBox(QMessageBox.Warning, '提示', '无法打开相机，可能正被别的软件控制!')
                msgBox.exec()
                return
            else:
                msgBox = QMessageBox(QMessageBox.Warning, '提示', '无法打开相机!')
                msgBox.exec()
                return
        w2 = MVGetWidth(hCam2.hCam)  # 获取图像宽度
        h2 = MVGetHeight(hCam2.hCam)  # 获取图像高度
        pf2 = MVGetPixelFormat(hCam2.hCam)  # 获取图像格式
        self.hCam2 = hCam2.hCam
        self.width2 = w2.width
        self.height2 = h2.height
        self.pixelFormat2 = pf2.pixelFormat
        if (self.pixelFormat2 == MV_PixelFormatEnums.PixelFormat_Mono8):
            self.himage2 = MVImageCreate(self.width2, self.height2, 8).himage  # 创建图像句柄
        else:
            self.himage2 = MVImageCreate(self.width2, self.height2, 24).himage  # 创建图像句柄
        self.LRImage.resize(self.width2*0.18, self.height2*0.3)

    # 相机开始采集执行本函数
    def startGrab(self):
        self.winid = self.LLImage.winId()  # 获取label对象的句柄
        MVStartGrabWindow(self.hCam, self.winid)  # 将采集的图像传输到指定窗口

        self.winid2 = self.LRImage.winId()  # 获取label对象的句柄
        MVStartGrabWindow(self.hCam2, self.winid2)  # 将采集的图像传输到指定窗口

    def stopGrab(self):
        MVFreezeGrabWindow(self.hCam, True)  # 暂停将图像传输到指定窗口
        MVFreezeGrabWindow(self.hCam2, True)  # 暂停将图像传输到指定窗口

    # 保存图片执行本函数，在非触发模式时，只有采集暂停是才可以保存
    def saveImage(self):
        idn = MVGetSampleGrab(self.hCam, self.himage)
        fname = QFileDialog.getSaveFileName(
            self, '打开文件', './Images' + str(idn.idn) + '.bmp', ("Images (*.bmp *.jpg *.tif *.raw)"))
        filename = os.path.basename(fname[0])  # 获取到需要存储的文件名
        pathname = os.path.join(os.getcwd(), filename)  # 获取带有文件名的文件路径
        newfile = '\\'.join(fname[0].split('/')[:-1])  # 需要存储到的新文件夹
        MVImageSave(self.himage, filename.encode('utf-8'))  # 将图片保存下来
        if (newfile != os.getcwd()):  # 将图片移动到指定文件夹下
            try:
                shutil.move(pathname, newfile)
            except:
                os.unlink(os.path.join(newfile, filename))
                shutil.move(pathname, newfile)
        image = QImage(newfile + '\\' + filename)
        self.LLImage.setPixmap(QPixmap.fromImage(image))  # 加载图片

        idn = MVGetSampleGrab(self.hCam2, self.himage2)
        fname = QFileDialog.getSaveFileName(
            self, '打开文件', './Images' + str(idn.idn) + '.bmp', ("Images (*.bmp *.jpg *.tif *.raw)"))
        filename = os.path.basename(fname[0])  # 获取到需要存储的文件名
        pathname = os.path.join(os.getcwd(), filename)  # 获取带有文件名的文件路径
        newfile = '\\'.join(fname[0].split('/')[:-1])  # 需要存储到的新文件夹
        MVImageSave(self.himage2, filename.encode('utf-8'))  # 将图片保存下来
        if (newfile != os.getcwd()):  # 将图片移动到指定文件夹下
            try:
                shutil.move(pathname, newfile)
            except:
                os.unlink(os.path.join(newfile, filename))
                shutil.move(pathname, newfile)
        image2 = QImage(newfile + '\\' + filename)
        self.LRImage.setPixmap(QPixmap.fromImage(image2))  # 加载图片

    def testSIFT(self):
        img = cv2.imread(self.himage)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        sift = cv2.xfeatures2d.SIFT_create()

        kp = sift.detect(gray, None)  # 找到关键点

        img = cv2.drawKeypoints(gray, kp, img)  # 绘制关键点

        cv2.imshow('testSIFT', img)
        cv2.waitKey(0)

class MyWindow(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    sys.exit(app.exec_())