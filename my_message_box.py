from Ui_Warning import Ui_warning_form
from Ui_success import Ui_success_form
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5 import QtCore
import datetime

class warning_form(QWidget,Ui_warning_form):
    comfirm_signal = pyqtSignal(str)
    def __init__(self,tip,butt_num):
        super(warning_form, self).__init__()
        # 定义 warning 显示的警告信息
        self.tip = tip
        # 定义 warning 下方的按钮数目
        self.butt_num = butt_num
        self.setupUi(self)
        self.initUi()
        self.connect_relation()

    def initUi(self):
        icon = QPixmap('./img_src/warning.png').scaled(60, 60, QtCore.Qt.KeepAspectRatio)
        self.waning_ico.setPixmap(icon)
        self.warning_tip.setText(self.tip)
        self.setWindowIcon(QIcon("./img_src/warning_ico.png"))

    def connect_relation(self):
        if self.butt_num == 1:
            self.cancel_butt.hide()
            self.confirm_butt.setFocus()
            self.confirm_butt.setShortcut(Qt.Key_Enter)
            self.confirm_butt.setShortcut(Qt.Key_Return)
            self.confirm_butt.clicked.connect(self.closeUi)
        else:
            self.cancel_butt.setFocus()
            self.cancel_butt.setShortcut(Qt.Key_Enter)
            self.cancel_butt.setShortcut(Qt.Key_Return)
            self.confirm_butt.clicked.connect(self.send_comfirm)
            self.cancel_butt.clicked.connect(self.closeUi)

    def send_comfirm(self):
        self.comfirm_signal.emit("True")
        self.closeUi()

    def closeUi(self):
        self.close()


class success_form(QWidget,Ui_success_form):
    def __init__(self,tip):
        super(success_form,self).__init__()
        self.setupUi(self)
        self.tip = tip
        self.initUi()
        self.connect_relation()

    def initUi(self):
        icon = QPixmap('./img_src/success.png').scaled(60, 60, QtCore.Qt.KeepAspectRatio)
        self.success_ico.setPixmap(icon)
        self.success_tip.setText(self.tip)
        self.setWindowIcon(QIcon("./img_src/success_ico.png"))

    def connect_relation(self):
        self.confirm_butt.setFocus()
        self.confirm_butt.setShortcut(Qt.Key_Enter)
        self.confirm_butt.setShortcut(Qt.Key_Return)
        self.confirm_butt.clicked.connect(self.closeUi)

    def closeUi(self):
        self.close()