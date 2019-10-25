# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'openbtn.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
from PyQt5.QtWidgets import QApplication,QMainWindow,QDialog
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
import cv2
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(464, 409)
        self.btnopenL = QtWidgets.QPushButton(Dialog)
        self.btnopenL.setGeometry(QtCore.QRect(40, 30, 75, 23))
        self.btnopenL.setObjectName("btnopenL")
        self.Llabel = QtWidgets.QLabel(Dialog)
        self.Llabel.setGeometry(QtCore.QRect(40, 110, 161, 211))
        self.Llabel.setObjectName("Llabel")
        self.btnopenR = QtWidgets.QPushButton(Dialog)
        self.btnopenR.setGeometry(QtCore.QRect(350, 30, 75, 23))
        self.btnopenR.setObjectName("btnopenR")
        self.Rlabel = QtWidgets.QLabel(Dialog)
        self.Rlabel.setGeometry(QtCore.QRect(250, 110, 161, 211))
        self.Rlabel.setObjectName("Rlabel")
        self.btnopen = QtWidgets.QPushButton(Dialog)
        self.btnopen.setGeometry(QtCore.QRect(190, 30, 75, 23))
        self.btnopen.setObjectName("btnopen")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btnopenL.setText(_translate("Dialog", "打开左图像"))
        self.Llabel.setText(_translate("Dialog", "左图像"))
        self.btnopenR.setText(_translate("Dialog", "右图像"))
        self.Rlabel.setText(_translate("Dialog", "右图像"))
        self.btnopen.setText(_translate("Dialog", "打开图像"))

        self.btnopenL.clicked.connect(self.openImageL)
        self.btnopenR.clicked.connect(self.openImageR)
        # self.btnopen.clicked.connect(self.openImage)
        self.btnopen.clicked.connect(self.sift)

    def openImageL(self):
        self.imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "*.bmp;;*.jpg;;*.png;;All Files(*)")
        self.jpg = QtGui.QPixmap(self.imgName).scaled(self.Llabel.width(), self.Llabel.height())
        self.Llabel.setPixmap(self.jpg)
        print(self.imgName)

    def openImageR(self):
        imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "*.bmp;;*.jpg;;*.png;;All Files(*)")
        jpg = QtGui.QPixmap(imgName).scaled(self.Rlabel.width(), self.Rlabel.height())
        self.Rlabel.setPixmap(jpg)

    def openImage(self):
        self.imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "./", "*.bmp;;*.jpg;;*.png;;All Files(*)")
        jpg = QtGui.QPixmap(self.imgName).scaled(self.Llabel.width(), self.Llabel.height())
        self.Llabel.setPixmap(jpg)
        print(self.imgName)
        self.imgName2, imgType2 = QFileDialog.getOpenFileName(self, "打开图片", "", "*.bmp;;*.jpg;;*.png;;All Files(*)")
        jpg2 = QtGui.QPixmap(self.imgName2).scaled(self.Rlabel.width(), self.Rlabel.height())
        self.Rlabel.setPixmap(jpg2)
        print(self.imgName2)

    def sift(self):
        print(self.imgName)
        img = cv2.imread(self.imgName)
        print("open")
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        print("gray")
        sift = cv2.xfeatures2d.SIFT_create()
        print("sift")
        kp = sift.detect(gray, None)  # 找到关键点
        print("kp")
        img = cv2.drawKeypoints(gray, kp, img)  # 绘制关键点
        print("hui")
        # self.Llabel.setPixmap(img)
        self.QtImg = QtGui.QImage(img.data,
                                  img.shape[1],
                                  img.shape[0],
                                  img.shape[1]*3,
                                  QtGui.QImage.Format_RGB888)
        self.Llabel.setPixmap(QtGui.QPixmap.fromImage(self.QtImg))
        cv2.imshow('testSIFT', img)
        cv2.waitKey(0)

class MyWindow(QtWidgets.QMainWindow, Ui_Dialog):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    sys.exit(app.exec_())



