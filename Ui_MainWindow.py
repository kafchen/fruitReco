# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\LZC-solo\Desktop\aut\digital_\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Main_w(object):
    def setupUi(self, Main_w):
        Main_w.setObjectName("Main_w")
        Main_w.resize(800, 600)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        Main_w.setPalette(palette)
        Main_w.setAcceptDrops(True)
        self.centralwidget = QtWidgets.QWidget(Main_w)
        self.centralwidget.setObjectName("centralwidget")
        self.img_sheet = QtWidgets.QLabel(self.centralwidget)
        self.img_sheet.setGeometry(QtCore.QRect(20, 80, 541, 471))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.img_sheet.setFont(font)
        self.img_sheet.setText("")
        self.img_sheet.setObjectName("img_sheet")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 20, 761, 46))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.widget.setFont(font)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.path_edit = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.path_edit.setFont(font)
        self.path_edit.setPlaceholderText("")
        self.path_edit.setObjectName("path_edit")
        self.horizontalLayout.addWidget(self.path_edit)
        self.confirm_butt = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.confirm_butt.setFont(font)
        self.confirm_butt.setObjectName("confirm_butt")
        self.horizontalLayout.addWidget(self.confirm_butt)
        self.upload_butt = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.upload_butt.setFont(font)
        self.upload_butt.setObjectName("upload_butt")
        self.horizontalLayout.addWidget(self.upload_butt)
        self.begin_classier = QtWidgets.QPushButton(self.centralwidget)
        self.begin_classier.setGeometry(QtCore.QRect(650, 400, 89, 26))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.begin_classier.setFont(font)
        self.begin_classier.setObjectName("begin_classier")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(600, 490, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.widget_2.setFont(font)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.result_lab = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.result_lab.setFont(font)
        self.result_lab.setText("")
        self.result_lab.setObjectName("result_lab")
        self.horizontalLayout_2.addWidget(self.result_lab)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(630, 290, 137, 101))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.rad_tra = QtWidgets.QRadioButton(self.groupBox)
        self.rad_tra.setChecked(True)
        self.rad_tra.setObjectName("rad_tra")
        self.verticalLayout.addWidget(self.rad_tra)
        self.rad_net = QtWidgets.QRadioButton(self.groupBox)
        self.rad_net.setObjectName("rad_net")
        self.verticalLayout.addWidget(self.rad_net)
        Main_w.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Main_w)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        self.help = QtWidgets.QMenu(self.menubar)
        self.help.setObjectName("help")
        Main_w.setMenuBar(self.menubar)
        self.vision_action = QtWidgets.QAction(Main_w)
        self.vision_action.setObjectName("vision_action")
        self.about_action = QtWidgets.QAction(Main_w)
        self.about_action.setObjectName("about_action")
        self.help.addAction(self.vision_action)
        self.help.addSeparator()
        self.help.addAction(self.about_action)
        self.menubar.addAction(self.help.menuAction())

        self.retranslateUi(Main_w)
        QtCore.QMetaObject.connectSlotsByName(Main_w)

    def retranslateUi(self, Main_w):
        _translate = QtCore.QCoreApplication.translate
        Main_w.setWindowTitle(_translate("Main_w", "水果分类助手"))
        self.label_2.setText(_translate("Main_w", "图片路径："))
        self.confirm_butt.setText(_translate("Main_w", "确认"))
        self.confirm_butt.setShortcut(_translate("Main_w", "Return"))
        self.upload_butt.setText(_translate("Main_w", "上传文件"))
        self.begin_classier.setText(_translate("Main_w", "开始分类"))
        self.label.setText(_translate("Main_w", "结果为："))
        self.groupBox.setTitle(_translate("Main_w", "分类方式"))
        self.rad_tra.setText(_translate("Main_w", "传统方法"))
        self.rad_net.setText(_translate("Main_w", "神经网络"))
        self.help.setTitle(_translate("Main_w", "关于"))
        self.vision_action.setText(_translate("Main_w", "版本"))
        self.about_action.setText(_translate("Main_w", "关于我们"))
