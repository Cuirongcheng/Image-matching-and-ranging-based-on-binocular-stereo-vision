# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwin.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import img
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnImage = QtWidgets.QPushButton(self.centralwidget)
        self.btnImage.setEnabled(True)
        self.btnImage.setGeometry(QtCore.QRect(140, 420, 90, 40))
        self.btnImage.setStyleSheet("font: 20pt \"汉仪喵魂体W\";\n"
"color: rgb(255, 255, 255);\n"
"border:0px;")
        self.btnImage.setObjectName("btnImage")
        self.btnMatch = QtWidgets.QPushButton(self.centralwidget)
        self.btnMatch.setGeometry(QtCore.QRect(350, 420, 90, 40))
        self.btnMatch.setStyleSheet("font: 20pt \"汉仪喵魂体W\";\n"
"color: rgb(255, 255, 255);\n"
"border:0px;")
        self.btnMatch.setObjectName("btnMatch")
        self.btnCount = QtWidgets.QPushButton(self.centralwidget)
        self.btnCount.setGeometry(QtCore.QRect(560, 420, 90, 40))
        self.btnCount.setStyleSheet("font: 20pt \"汉仪喵魂体W\";\n"
"color: rgb(255, 255, 255);\n"
"border:0px;")
        self.btnCount.setObjectName("btnCount")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.frame.setStyleSheet("border-image: url(:/newPrefix/img/幻灯片1.JPG);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.raise_()
        self.btnImage.raise_()
        self.btnMatch.raise_()
        self.btnCount.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "图像匹配与测距演示系统"))
        self.btnImage.setText(_translate("MainWindow", "图像采集"))
        self.btnMatch.setText(_translate("MainWindow", "图像匹配"))
        self.btnCount.setText(_translate("MainWindow", "距离测量"))


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


