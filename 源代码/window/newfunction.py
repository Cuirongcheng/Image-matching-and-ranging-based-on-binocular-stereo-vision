# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newfunction.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import img

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(821, 571)
        Dialog.setStyleSheet("border-image: url(./img/bg2.JPG);")
        self.btnCams = QtWidgets.QPushButton(Dialog)
        self.btnCams.setGeometry(QtCore.QRect(140, 370, 101, 41))
        self.btnCams.setObjectName("btnCams")
        self.btnMatch = QtWidgets.QPushButton(Dialog)
        self.btnMatch.setGeometry(QtCore.QRect(350, 370, 101, 41))
        self.btnMatch.setObjectName("btnMatch")
        self.btnCount = QtWidgets.QPushButton(Dialog)
        self.btnCount.setGeometry(QtCore.QRect(570, 370, 101, 41))
        self.btnCount.setObjectName("btnCount")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "主要演示功能"))
        self.btnCams.setText(_translate("Dialog", "图像采集"))
        self.btnCams.setVisible(False)
        self.btnMatch.setText(_translate("Dialog", "图像匹配"))
        self.btnMatch.setVisible(False)
        self.btnCount.setText(_translate("Dialog", "距离测量"))
        self.btnCount.setVisible(False)

class MyWindow(QMainWindow, Ui_Dialog):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    sys.exit(app.exec_())