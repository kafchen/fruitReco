from Ui_MainWindow import Ui_Main_w
from my_message_box import *
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon,QPixmap,QDesktopServices,QImage
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import sys
import os

class Mian_w(QMainWindow, Ui_Main_w):
    def __init__(self):
        super(Mian_w,self).__init__()
        self.setupUi(self)
        # 0 为传统方法,  1 为神经网络的方法
        self.classier_way = 0
        self.setWindowIcon(QIcon("./img_src/window_ico.png"))
        self.rad_tra.clicked.connect(self.change_tra)
        self.rad_net.clicked.connect(self.change_net)
        self.upload_butt.clicked.connect(self.openfile)
        self.confirm_butt.clicked.connect(self.show_img)
        self.begin_classier.clicked.connect(self.operate)

    def change_tra(self):
        self.classier_way = 0
        print(self.classier_way)

    def change_net(self):
        self.classier_way = 1
        print(self.classier_way)

    def dragEnterEvent(self,e):
        if e.mimeData().urls()[0].fileName()[-4:] == ".jpg":
            e.acceptProposedAction()
        else:
            e.ignore()

    def dropEvent(self,e):
        self.path_edit.setText(e.mimeData().urls()[0].toLocalFile())
        self.show_img()

    def openfile(self):
        openfile_name = QFileDialog.getOpenFileName(self, '选择图片', '','*.jpg')
        print(openfile_name)
        if openfile_name[0] != "":
            self.path_edit.setText(openfile_name[0])
            img = QImage()
            img.load(openfile_name[0])
            img.scaled(self.img_sheet.size(),Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.img_sheet.setScaledContents(True)
            self.img_sheet.setPixmap(QPixmap.fromImage(img))

    def show_img(self):
        path = self.path_edit.text()

        if os.path.exists(path):
            img = QImage()
            img.load(path)
            img.scaled(self.img_sheet.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.img_sheet.setScaledContents(True)
            self.img_sheet.setPixmap(QPixmap.fromImage(img))
            return True
        else:
            self.warn_w = warning_form("请输入有效的图片路径",1)
            self.warn_w.show()
            return False

    # 传入图片到分类器中进行处理，同时进行图片的展示工作
    def operate(self):
        flag = self.show_img()
        if flag:
            # 图片的路径
            path = self.path_edit.text()
            # 进行图片识别
            # 写自己的分类函数 可用参数为 --->>> 图片的 path
            pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = Mian_w()
    MainWindow.show()
    sys.exit(app.exec_())