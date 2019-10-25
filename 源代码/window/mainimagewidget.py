# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainimagewidget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
from MVGigE import *
import os
import shutil
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QMessageBox, QLabel, QFileDialog, QScrollArea, QComboBox, QLineEdit, QSlider, QGridLayout, QGroupBox, QCheckBox
from PyQt5.QtGui import QPixmap, QPalette, QImage, QIcon
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form_Image(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        self.btnStartGrab = QtWidgets.QPushButton(Form)
        self.btnStartGrab.setGeometry(QtCore.QRect(210, 70, 100, 35))
        self.btnStartGrab.setStyleSheet("font: bold 14pt \"汉仪喵魂体W\";\n"
"color: rgb(255, 255, 255);\n"
"border:2px solid;\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(242, 216, 121);")
        self.btnStartGrab.setObjectName("btnStartGrab")
        self.btnStopGrab = QtWidgets.QPushButton(Form)
        self.btnStopGrab.setGeometry(QtCore.QRect(350, 70, 100, 35))
        self.btnStopGrab.setStyleSheet("font: bold 14pt \"汉仪喵魂体W\";\n"
"color: rgb(255, 255, 255);\n"
"border:2px solid;\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(242, 216, 121);")
        self.btnStopGrab.setObjectName("btnStopGrab")
        self.ResultLabel = QtWidgets.QLabel(Form)
        self.ResultLabel.setGeometry(QtCore.QRect(70, 485, 660, 70))
        self.ResultLabel.setStyleSheet("font: 12pt \"汉仪喵魂体W\";\n"
"color: rgb(0, 0, 0);\n"
"border:2px solid;\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(242, 216, 121);")
        self.ResultLabel.setObjectName("ResultLabel")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.frame.setStyleSheet("border-image: url(:/newPrefix/img/background.jpg);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.btnSaveImage = QtWidgets.QPushButton(Form)
        self.btnSaveImage.setGeometry(QtCore.QRect(490, 70, 100, 35))
        self.btnSaveImage.setStyleSheet("font: bold 14pt \"汉仪喵魂体W\";\n"
"color: rgb(255, 255, 255);\n"
"border:2px solid;\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(242, 216, 121);")
        self.btnSaveImage.setObjectName("btnSaveImage")
        self.btnCloseCam = QtWidgets.QPushButton(Form)
        self.btnCloseCam.setGeometry(QtCore.QRect(630, 70, 100, 35))
        self.btnCloseCam.setStyleSheet("font: bold 14pt \"汉仪喵魂体W\";\n"
"color: rgb(255, 255, 255);\n"
"border:2px solid;\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(242, 216, 121);")
        self.btnCloseCam.setObjectName("btnCloseCam")
        self.RLabel = QtWidgets.QLabel(Form)
        self.RLabel.setGeometry(QtCore.QRect(405, 135, 325, 331))
        self.RLabel.setStyleSheet("font: 14pt \"汉仪喵魂体W\";\n"
"color: rgb(255, 255, 255);\n"
"border:2px;\n"
"border-style:dotted;\n"
"border-color: rgb(242, 216, 121);")
        self.RLabel.setObjectName("RLabel")
        self.LLabel = QtWidgets.QLabel(Form)
        self.LLabel.setGeometry(QtCore.QRect(70, 135, 325, 331))
        self.LLabel.setStyleSheet("font: 14pt \"汉仪喵魂体W\";\n"
"color: rgb(255, 255, 255);\n"
"border:2px;\n"
"border-style:dotted;\n"
"border-color: rgb(242, 216, 121);")
        self.LLabel.setObjectName("LLabel")
        self.btnOpenCam = QtWidgets.QPushButton(Form)
        self.btnOpenCam.setGeometry(QtCore.QRect(70, 70, 100, 35))
        self.btnOpenCam.setStyleSheet("font: bold 14pt \"汉仪喵魂体W\";\n"
"color: rgb(255, 255, 255);\n"
"border:2px solid;\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(242, 216, 121);")
        self.btnOpenCam.setObjectName("btnOpenCam")
        self.frame.raise_()
        self.btnStartGrab.raise_()
        self.btnStopGrab.raise_()
        self.ResultLabel.raise_()
        self.btnSaveImage.raise_()
        self.btnCloseCam.raise_()
        self.RLabel.raise_()
        self.LLabel.raise_()
        self.btnOpenCam.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btnStartGrab.setText(_translate("Form", "采集图像"))
        self.btnStopGrab.setText(_translate("Form", "停止采集"))
        self.ResultLabel.setText(_translate("Form", "结果显示区域"))
        self.btnSaveImage.setText(_translate("Form", "保存图像"))
        self.btnCloseCam.setText(_translate("Form", "关闭相机"))
        self.RLabel.setText(_translate("Form", "右图像区域"))
        self.LLabel.setText(_translate("Form", "左图像区域"))
        self.btnOpenCam.setText(_translate("Form", "启动相机"))

# -------------------------设置按钮点击事件-------------------------------------
        self.btnOpenCam.clicked.connect(self.openCam)
        self.btnStartGrab.clicked.connect(self.startGrab)
        self.btnStopGrab.clicked.connect(self.stopGrab)
        self.btnCloseCam.clicked.connect(self.closeCam)
        self.btnSaveImage.clicked.connect(self.saveImage)

    # 点击启动相机按钮，开始打开左右相机
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
        if (nCams.status != MVSTATUS_CODES.MVST_SUCCESS):
            msgBox = QMessageBox(QMessageBox.Warning, '提示', nCams.status)
            msgBox.exec()
            return
        if (nCams.num == 0):
            msgBox = QMessageBox(QMessageBox.Warning, '提示', '没有找到相机,请确认连接和相机IP设置!')
            msgBox.exec()
            return

        # 左相机
        hCam = MVOpenCamByIndex(0)  # 根据相机的索引返回相机句柄
        if (hCam.hCam == 0):
            if (hCam.status == MVSTATUS_CODES.MVST_ACCESS_DENIED):
                msgBox = QMessageBox(QMessageBox.Warning, '提示', '无法打开相机，可能正被别的软件控制!')
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
        if (self.pixelFormat == MV_PixelFormatEnums.PixelFormat_Mono8):
            self.himage = MVImageCreate(self.width, self.height, 8).himage  # 创建图像句柄
        else:
            self.himage = MVImageCreate(self.width, self.height, 24).himage  # 创建图像句柄
        # self.LLImage.resize(self.width * 0.25, self.height * 0.25)
        self.LLabel.resize(self.width * 0.25, self.height * 0.35)
        self.LLabel.setText("左相机检测正常！")
        # self.ResultLlabel.setText("左相机检测正常！")

        # 右相机
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
        # self.LRImage.resize(self.width2 * 0.25, self.height2 * 0.25)
        self.RLabel.resize(self.width * 0.25, self.height * 0.35)
        self.RLabel.setText("右相机检测正常！")
        # self.ResultLlabel.setText("右相机检测正常！")

        self.ResultLabel.setText("相机启动正常！")

    # 点击采集图像按钮，相机开始采集执行本函数
    def startGrab(self):
        self.winid = self.LLabel.winId()  # 获取label对象的句柄
        mode = MVGetTriggerMode(self.hCam)  # 获取当前相机采集模式
        source = MVGetTriggerSource(self.hCam)  # 获取当前相机信号源
        self.winid2 = self.RLabel.winId()  # 获取label对象的句柄
        mode2 = MVGetTriggerMode(self.hCam2)  # 获取当前相机采集模式
        source2 = MVGetTriggerSource(self.hCam2)  # 获取当前相机信号源
        if (self.btnStartGrab.text() == '采集图像'):
            if ((mode.pMode == TriggerModeEnums.TriggerMode_Off) & (mode2.pMode == TriggerModeEnums.TriggerMode_Off)):  # 当触发模式关闭的时候，界面的行为
                # self.btnStartGrab.setText('停止采集')
                MVStartGrabWindow(self.hCam, self.winid)  # 将采集的图像传输到指定窗口
                MVStartGrabWindow(self.hCam2, self.winid2)  # 将采集的图像传输到指定窗口
            else:
                if ((source.source == TriggerSourceEnums.TriggerSource_Software) & (source2.source == TriggerSourceEnums.TriggerSource_Software)):  # 当触发模式打开且为软触发的时候，界面的行为
                    MVStartGrabWindow(self.hCam, self.winid)  # 将采集的图像传输到指定窗口
                    MVStartGrabWindow(self.hCam2, self.winid2)  # 将采集的图像传输到指定窗口
                    MVTriggerSoftware(self.hCam)
                    MVTriggerSoftware(self.hCam2)
                else:  # 当触发模式打开且为外触发的时候，界面的行为
                    MVStartGrabWindow(self.hCam, self.winid)  # 将采集的图像传输到指定窗口
                    MVStartGrabWindow(self.hCam2, self.winid2)  # 将采集的图像传输到指定窗口
            self.ResultLabel.setText("图像采集开始！")
        # else:
        #     self.btnStartGrab.setText('开始采集')
        #     MVStopGrabWindow(self.hCam)  # 停止采集
        #     MVStopGrabWindow(self.hCam2)  # 停止采集
        #     self.btnStopGrab.setEnabled(False)
        #     self.ResultLabel.setText("图像采集停止！")

    # 暂停或者继续执行本函数
    def stopGrab(self):
        if (self.btnStopGrab.text() == '继续采集'):
            self.btnStopGrab.setText('暂停采集')
            MVFreezeGrabWindow(self.hCam, False)  # 恢复图像传输到左窗口
            MVFreezeGrabWindow(self.hCam2, False)  # 恢复将图像传输到右窗口
            self.ResultLabel.setText("图像采集继续！")
        else:
            self.btnStopGrab.setText('继续采集')
            MVFreezeGrabWindow(self.hCam, True)  # 暂停将图像传输到左窗口
            MVFreezeGrabWindow(self.hCam2, True)  # 暂停将图像传输到右窗口
            self.ResultLabel.setText("图像采集暂停！")


    # 保存图片执行本函数，在非触发模式时，只有采集暂停是才可以保存
    def saveImage(self):

        idn = MVGetSampleGrab(self.hCam, self.himage)
        print("01")
        fname = QFileDialog.getSaveFileName(
            self, '打开文件', './Images' + str(idn.idn) + '.bmp', ("Images (*.bmp *.jpg *.tif *.raw)"))
        print("02")
        filename = os.path.basename(fname[0])  # 获取到需要存储的文件名
        pathname = os.path.join(os.getcwd(), filename)  # 获取带有文件名的文件路径
        newfile = '\\'.join(fname[0].split('/')[:-1])  # 需要存储到的新文件夹
        print("03")
        MVImageSave(self.himage, filename.encode('utf-8'))  # 将图片保存下来
        print("04")
        if (newfile != os.getcwd()):  # 将图片移动到指定文件夹下
            try:
                shutil.move(pathname, newfile)
            except:
                os.unlink(os.path.join(newfile, filename))
                shutil.move(pathname, newfile)
        image = QImage(newfile + '\\' + filename)
        self.label.setPixmap(QPixmap.fromImage(image))  # 加载图片
        mode = MVGetTriggerMode(self.hCam)  # 获取当前相机采集模式

        #保存左图像
        # idn = MVGetSampleGrab(self.hCam, self.himage)
        # fname = QFileDialog.getSaveFileName(
        #     self, '打开文件', './Images' + str(idn.idn) + '.bmp', ("Images (*.bmp *.jpg *.tif *.raw)"))
        # filename = os.path.basename(fname[0])  # 获取到需要存储的文件名
        # pathname = os.path.join(os.getcwd(), filename)  # 获取带有文件名的文件路径
        # newfile = '\\'.join(fname[0].split('/')[:-1])  # 需要存储到的新文件夹
        # MVImageSave(self.himage, filename.encode('utf-8'))  # 将图片保存下来
        # if (newfile != os.getcwd()):  # 将图片移动到指定文件夹下
        #     try:
        #         shutil.move(pathname, newfile)
        #     except:
        #         os.unlink(os.path.join(newfile, filename))
        #         shutil.move(pathname, newfile)
        # image = QImage(newfile + '\\' + filename)
        # self.LLabel.setPixmap(QPixmap.fromImage(image))  # 加载图片

        #保存右图像
        # idn = MVGetSampleGrab(self.hCam2, self.himage2)
        # fname = QFileDialog.getSaveFileName(
        #     self, '打开文件', './Images' + str(idn.idn) + '.bmp', ("Images (*.bmp *.jpg *.tif *.raw)"))
        # filename = os.path.basename(fname[0])  # 获取到需要存储的文件名
        # pathname = os.path.join(os.getcwd(), filename)  # 获取带有文件名的文件路径
        # newfile = '\\'.join(fname[0].split('/')[:-1])  # 需要存储到的新文件夹
        # MVImageSave(self.himage2, filename.encode('utf-8'))  # 将图片保存下来
        # if (newfile != os.getcwd()):  # 将图片移动到指定文件夹下
        #     try:
        #         shutil.move(pathname, newfile)
        #     except:
        #         os.unlink(os.path.join(newfile, filename))
        #         shutil.move(pathname, newfile)
        # image2 = QImage(newfile + '\\' + filename)
        # self.RLabel.setPixmap(QPixmap.fromImage(image2))  # 加载图片

        self.ResultLabel.setText("图像保存正常！")

    # 点击关闭相机按钮，开始关闭相机
    def closeCam(self):
        result = MVCloseCam(self.hCam)# 关闭左相机
        result2 = MVCloseCam(self.hCam2)# 关闭右相机
        if (result.status != MVSTATUS_CODES.MVST_SUCCESS):
            msgBox = QMessageBox(QMessageBox.Warning, '提示', result.status)
            msgBox.exec()
        if (result2.status != MVSTATUS_CODES.MVST_SUCCESS):
            msgBox = QMessageBox(QMessageBox.Warning, '提示', result.status)
            msgBox.exec()

        self.ResultLabel.setText("相机关闭成功！")
import img

import sys
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Ui_Form_Image()
    # 显示
    window.show()
    sys.exit(app.exec_())