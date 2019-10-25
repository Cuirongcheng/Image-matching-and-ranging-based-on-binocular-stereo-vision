from PyQt5 import QtCore, QtGui, QtWidgets
from MVGigE import *
import sys
import main
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
    main.Ui_MainWindow.LImageLable.resize(self.width * 0.5, self.height * 0.5)

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
    main.Ui_MainWindow.RImageLable.resize(self.width * 0.5, self.height * 0.5)


# 相机开始采集执行本函数
def startGrab(self):
    self.winid = main.Ui_MainWindow.LImageLable.winId()  # 获取label对象的句柄
    MVStartGrabWindow(self.hCam, self.winid)  # 将采集的图像传输到指定窗口

    self.winid2 = main.Ui_MainWindow.RImageLable.winId()  # 获取label对象的句柄
    MVStartGrabWindow(self.hCam2, self.winid2)  # 将采集的图像传输到指定窗口