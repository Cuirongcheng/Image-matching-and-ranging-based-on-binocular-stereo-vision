# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton
from MVGigE import *
import os
import shutil
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QMessageBox, QLabel, QFileDialog, QScrollArea, QComboBox, QLineEdit, QSlider, QGridLayout, QGroupBox, QCheckBox
from PyQt5.QtGui import QPixmap, QPalette, QImage, QIcon
from PyQt5.QtCore import Qt

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(743, 581)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.CamsgroupBox = QtWidgets.QGroupBox(self.centralWidget)
        self.CamsgroupBox.setEnabled(True)
        self.CamsgroupBox.setGeometry(QtCore.QRect(10, 40, 721, 81))
        self.CamsgroupBox.setObjectName("CamsgroupBox")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.CamsgroupBox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(-1, 10, 721, 71))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnOpen = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnOpen.setEnabled(True)
        self.btnOpen.setObjectName("btnOpen")
        self.horizontalLayout.addWidget(self.btnOpen)
        self.btnStart = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnStart.setObjectName("btnStart")
        self.horizontalLayout.addWidget(self.btnStart)
        self.btnSet = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnSet.setObjectName("btnSet")
        self.horizontalLayout.addWidget(self.btnSet)
        self.btnMatch = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnMatch.setObjectName("btnMatch")
        self.horizontalLayout.addWidget(self.btnMatch)
        self.btnTest = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnTest.setObjectName("btnTest")
        self.horizontalLayout.addWidget(self.btnTest)
        self.btnClose = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnClose.setObjectName("btnClose")
        self.horizontalLayout.addWidget(self.btnClose)
        self.btnHelp = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnHelp.setObjectName("btnHelp")
        self.horizontalLayout.addWidget(self.btnHelp)
        self.TitleLable = QtWidgets.QLabel(self.centralWidget)
        self.TitleLable.setGeometry(QtCore.QRect(260, 10, 201, 20))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.TitleLable.setFont(font)
        self.TitleLable.setObjectName("TitleLable")
        self.RCamgroupBox = QtWidgets.QGroupBox(self.centralWidget)
        self.RCamgroupBox.setGeometry(QtCore.QRect(630, 120, 101, 401))
        self.RCamgroupBox.setObjectName("RCamgroupBox")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.RCamgroupBox)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(0, 10, 91, 391))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btnRCam = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.btnRCam.setObjectName("btnRCam")
        self.verticalLayout_3.addWidget(self.btnRCam)
        self.btnRImage = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.btnRImage.setObjectName("btnRImage")
        self.verticalLayout_3.addWidget(self.btnRImage)
        self.btnRState = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.btnRState.setObjectName("btnRState")
        self.verticalLayout_3.addWidget(self.btnRState)
        self.btnRSet = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.btnRSet.setObjectName("btnRSet")
        self.verticalLayout_3.addWidget(self.btnRSet)
        self.btnRMatch = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.btnRMatch.setObjectName("btnRMatch")
        self.verticalLayout_3.addWidget(self.btnRMatch)
        self.btnRTest = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.btnRTest.setObjectName("btnRTest")
        self.verticalLayout_3.addWidget(self.btnRTest)
        self.LCamgroupBox = QtWidgets.QGroupBox(self.centralWidget)
        self.LCamgroupBox.setGeometry(QtCore.QRect(10, 120, 101, 401))
        self.LCamgroupBox.setObjectName("LCamgroupBox")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.LCamgroupBox)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 10, 91, 391))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btnLCam = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btnLCam.setObjectName("btnLCam")
        self.verticalLayout_2.addWidget(self.btnLCam)
        self.btnLImage = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btnLImage.setObjectName("btnLImage")
        self.verticalLayout_2.addWidget(self.btnLImage)
        self.btnLState = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btnLState.setObjectName("btnLState")
        self.verticalLayout_2.addWidget(self.btnLState)
        self.btnLSet = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btnLSet.setObjectName("btnLSet")
        self.verticalLayout_2.addWidget(self.btnLSet)
        self.btnLMatch = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btnLMatch.setObjectName("btnLMatch")
        self.verticalLayout_2.addWidget(self.btnLMatch)
        self.btnLTest = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btnLTest.setObjectName("btnLTest")
        self.verticalLayout_2.addWidget(self.btnLTest)
        self.StategroupBox = QtWidgets.QGroupBox(self.centralWidget)
        self.StategroupBox.setGeometry(QtCore.QRect(120, 410, 501, 111))
        self.StategroupBox.setObjectName("StategroupBox")
        self.ResultLlabel = QtWidgets.QLabel(self.StategroupBox)
        self.ResultLlabel.setGeometry(QtCore.QRect(40, 30, 271, 41))
        self.ResultLlabel.setObjectName("ResultLlabel")
        self.LImageLable = QtWidgets.QLabel(self.centralWidget)
        self.LImageLable.setGeometry(QtCore.QRect(110, 130, 251, 271))
        self.LImageLable.setStyleSheet("background-color: rgb(190, 190, 190);")
        self.LImageLable.setTextFormat(QtCore.Qt.AutoText)
        self.LImageLable.setObjectName("LImageLable")
        self.RImageLable = QtWidgets.QLabel(self.centralWidget)
        self.RImageLable.setGeometry(QtCore.QRect(370, 130, 251, 271))
        self.RImageLable.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.RImageLable.setStyleSheet("background-color: rgb(190, 190, 190);")
        self.RImageLable.setObjectName("RImageLable")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 743, 23))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menuBar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menuBar)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(self.menuBar)
        self.menu_4.setObjectName("menu_4")
        self.menu_5 = QtWidgets.QMenu(self.menuBar)
        self.menu_5.setObjectName("menu_5")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionqidongxiangji = QtWidgets.QAction(MainWindow)
        self.actionqidongxiangji.setObjectName("actionqidongxiangji")
        self.actionCloseCamera = QtWidgets.QAction(MainWindow)
        self.actionCloseCamera.setObjectName("actionCloseCamera")
        self.actionTestCamera = QtWidgets.QAction(MainWindow)
        self.actionTestCamera.setObjectName("actionTestCamera")
        self.actionAboutCamera = QtWidgets.QAction(MainWindow)
        self.actionAboutCamera.setObjectName("actionAboutCamera")
        self.actionOpenImage = QtWidgets.QAction(MainWindow)
        self.actionOpenImage.setObjectName("actionOpenImage")
        self.actionEditImage = QtWidgets.QAction(MainWindow)
        self.actionEditImage.setObjectName("actionEditImage")
        self.actionSaveImage = QtWidgets.QAction(MainWindow)
        self.actionSaveImage.setObjectName("actionSaveImage")
        self.actionSIFT = QtWidgets.QAction(MainWindow)
        self.actionSIFT.setObjectName("actionSIFT")
        self.actionSURF = QtWidgets.QAction(MainWindow)
        self.actionSURF.setObjectName("actionSURF")
        self.actionCount = QtWidgets.QAction(MainWindow)
        self.actionCount.setObjectName("actionCount")
        self.menu.addAction(self.actionqidongxiangji)
        self.menu.addAction(self.actionCloseCamera)
        self.menu.addAction(self.actionTestCamera)
        self.menu.addAction(self.actionAboutCamera)
        self.menu_2.addAction(self.actionOpenImage)
        self.menu_2.addAction(self.actionEditImage)
        self.menu_2.addAction(self.actionSaveImage)
        self.menu_4.addAction(self.actionSIFT)
        self.menu_4.addAction(self.actionSURF)
        self.menu_5.addAction(self.actionCount)
        self.menuBar.addAction(self.menu.menuAction())
        self.menuBar.addAction(self.menu_2.menuAction())
        self.menuBar.addAction(self.menu_3.menuAction())
        self.menuBar.addAction(self.menu_4.menuAction())
        self.menuBar.addAction(self.menu_5.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.CamsgroupBox.setTitle(_translate("MainWindow", "双相机操作"))
        self.btnOpen.setText(_translate("MainWindow", "启动相机"))
        self.btnStart.setText(_translate("MainWindow", "采集图像"))
        self.btnSet.setText(_translate("MainWindow", "特征提取"))
        self.btnMatch.setText(_translate("MainWindow", "立体匹配"))
        self.btnTest.setText(_translate("MainWindow", "双目测距"))
        self.btnClose.setText(_translate("MainWindow", "关闭相机"))
        self.btnHelp.setText(_translate("MainWindow", "帮助文档"))
        self.TitleLable.setText(_translate("MainWindow", "双目测量测试开发平台"))
        self.RCamgroupBox.setTitle(_translate("MainWindow", "右相机操作"))
        self.btnRCam.setText(_translate("MainWindow", "相机操作"))
        self.btnRImage.setText(_translate("MainWindow", "图像处理"))
        self.btnRState.setText(_translate("MainWindow", "特征监测"))
        self.btnRSet.setText(_translate("MainWindow", "相机标定"))
        self.btnRMatch.setText(_translate("MainWindow", "算法匹配"))
        self.btnRTest.setText(_translate("MainWindow", "单目测距"))
        self.LCamgroupBox.setTitle(_translate("MainWindow", "左相机操作"))
        self.btnLCam.setText(_translate("MainWindow", "相机操作"))
        self.btnLImage.setText(_translate("MainWindow", "图像处理"))
        self.btnLState.setText(_translate("MainWindow", "特征监测"))
        self.btnLSet.setText(_translate("MainWindow", "相机标定"))
        self.btnLMatch.setText(_translate("MainWindow", "算法匹配"))
        self.btnLTest.setText(_translate("MainWindow", "单目测距"))
        self.StategroupBox.setTitle(_translate("MainWindow", "检测结果及操作步骤"))
        self.ResultLlabel.setText(_translate("MainWindow", "结果显示"))
        self.LImageLable.setText(_translate("MainWindow", "左图像区域"))
        self.RImageLable.setText(_translate("MainWindow", "右图像区域"))
        self.menu.setTitle(_translate("MainWindow", "相机操作"))
        self.menu_2.setTitle(_translate("MainWindow", "图像操作"))
        self.menu_3.setTitle(_translate("MainWindow", "编辑处理"))
        self.menu_4.setTitle(_translate("MainWindow", "算法匹配"))
        self.menu_5.setTitle(_translate("MainWindow", "立体测距"))
        self.actionqidongxiangji.setText(_translate("MainWindow", "OpenCamera"))
        self.actionCloseCamera.setText(_translate("MainWindow", "CloseCamera"))
        self.actionTestCamera.setText(_translate("MainWindow", "TestCamera"))
        self.actionAboutCamera.setText(_translate("MainWindow", "AboutCamera"))
        self.actionOpenImage.setText(_translate("MainWindow", "OpenImage"))
        self.actionEditImage.setText(_translate("MainWindow", "EditImage"))
        self.actionSaveImage.setText(_translate("MainWindow", "SaveImage"))
        self.actionSIFT.setText(_translate("MainWindow", "SIFT"))
        self.actionSURF.setText(_translate("MainWindow", "SURF"))
        self.actionCount.setText(_translate("MainWindow", "Count"))

        # 信号槽事件
        self.btnOpen.clicked.connect(self.openCam)
        self.btnStart.clicked.connect(self.startGrab)
        # self.btnSet.clicked.connect()
        # if(self.btnSet.isChecked(bool)):
        #     self.ResultLlabel.setText("被点击！")
        # self.btnMatch.clicked.connect()
        # self.btnTest.clicked.connect()
        self.btnClose.clicked.connect(self.closeCam)
        # self.btnHelp.clicked.connect()

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
        self.LImageLable.resize(self.width * 0.19, self.height * 0.28)
        self.LImageLable.setText("左相机检测正常！")
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
        self.RImageLable.resize(self.width * 0.19, self.height * 0.28)
        self.RImageLable.setText("右相机检测正常！")
        # self.ResultLlabel.setText("右相机检测正常！")

        self.ResultLlabel.setText("相机启动正常！")

    # 点击采集图像按钮，相机开始采集执行本函数
    def startGrab(self):
        if(self.btnStart.text() == '采集图像'):
            self.btnStart.setText('暂停采集')
            self.winid = self.LImageLable.winId()  # 获取label对象的句柄
            MVStartGrabWindow(self.hCam, self.winid)  # 将采集的图像传输到指定窗口

            self.winid2 = self.RImageLable.winId()  # 获取label对象的句柄
            MVStartGrabWindow(self.hCam2, self.winid2)  # 将采集的图像传输到指定窗口

            mode = MVGetTriggerMode(self.hCam)  # 获取当前相机采集模式
            source = MVGetTriggerSource(self.hCam)  # 获取当前相机信号源
            if (mode.pMode == TriggerModeEnums.TriggerMode_Off):  # 当触发模式关闭的时候，界面的行为
                MVStartGrabWindow(self.hCam, self.winid)  # 将采集的图像传输到指定窗口
            else:
                if (source.source == TriggerSourceEnums.TriggerSource_Software):  # 当触发模式打开且为软触发的时候，界面的行为
                    MVStartGrabWindow(self.hCam, self.winid)  # 将采集的图像传输到指定窗口
                    MVTriggerSoftware(self.hCam)
                else:  # 当触发模式打开且为外触发的时候，界面的行为
                    MVStartGrabWindow(self.hCam, self.winid)  # 将采集的图像传输到指定窗口
            self.ResultLlabel.setText("图像采集正常！")

            # # print(self.btnStart.isChecked())
            # if(self.btnStart.clicked.connect(self.pauseGrab())):
            #     self.ResultLlabel.setText("图像采集暂停！")

    # 暂停或者继续执行本函数
    def pauseGrab(self):
        if (self.btnStart.text() == '暂停采集'):
            self.btnStart.setText('继续采集')
            MVFreezeGrabWindow(self.hCam, True)  # 暂停将图像传输到指定窗口
            MVFreezeGrabWindow(self.hCam2, True)  # 暂停将图像传输到指定窗口
            self.ResultLlabel.setText("图像采集暂停！")
        if (self.btnStart.text() == '继续采集'):
            self.btnStart.setText('暂停采集')
            MVFreezeGrabWindow(self.hCam, False)  # 恢复图像传输到指定窗口
            MVFreezeGrabWindow(self.hCam2, True)  # 暂停将图像传输到指定窗口
            self.ResultLlabel.setText("图像采集继续！")

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
        self.LImageLable.setPixmap(QPixmap.fromImage(image))  # 加载图片
        mode = MVGetTriggerMode(self.hCam)  # 获取当前相机采集模式

        self.ResultLlabel.setText("图像保存正常！")

    # 点击关闭相机按钮，开始关闭相机
    def closeCam(self):
        result = MVCloseCam(self.hCam)
        result2 = MVCloseCam(self.hCam2)
        if (result.status != MVSTATUS_CODES.MVST_SUCCESS):
            msgBox = QMessageBox(QMessageBox.Warning, '提示', result.status)
            msgBox.exec()
        if (result2.status != MVSTATUS_CODES.MVST_SUCCESS):
            msgBox = QMessageBox(QMessageBox.Warning, '提示', result.status)
            msgBox.exec()

        self.ResultLlabel.setText("相机关闭成功！")


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    sys.exit(app.exec_())