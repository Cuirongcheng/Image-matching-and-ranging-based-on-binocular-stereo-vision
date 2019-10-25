from window.mainwin import *
from window.mainimagewin import *
from window.mainimagewidget import *
from window.mainmatchwin import *
from window.maincountwin import *
from PyQt5.QtWidgets import QApplication,QMainWindow,QDialog
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.main_ui = Ui_MainWindow()
        self.main_ui.setupUi(self)


class MainImageWindow(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child = Ui_Dialog_image()
        self.child.setupUi(self)

# class MainImageWidget(QWidget):
#     def __init__(self):
#         QWidget.__init__(self)
#         self.child = Ui_Form_Image()
#         self.child.setupUi(self)

class MainMatchWindow(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child = Ui_Dialog_match()
        self.child.setupUi(self)


class MainCountWindow(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child = Ui_Dialog_count()
        self.child.setupUi(self)


if __name__=='__main__':

    app = QApplication(sys.argv)

    window = MainWindow()
    imagewindow = MainImageWindow()
    # imagewidget = MainImageWidget()
    matchwindow = MainMatchWindow()
    countwindow = MainCountWindow()


    # 通过toolButton将两个窗体关联
    window.main_ui.btnImage.clicked.connect(imagewindow.show)
    window.main_ui.btnMatch.clicked.connect(matchwindow.show)
    window.main_ui.btnCount.clicked.connect(countwindow.show)

    # 显示
    window.show()
    sys.exit(app.exec_())
