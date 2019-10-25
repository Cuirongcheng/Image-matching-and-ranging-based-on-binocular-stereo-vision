from window.newmainwindow import *
import sys

class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    # tuopan = QSystemTrayIcon(myWin)
    # icon1 = QtGui.QIcon('F:\\education_paper\\runimg\\GJ1.jpg')
    # tuopan.setIcon(icon1)
    # tuopan.show()
    sys.exit(app.exec_())