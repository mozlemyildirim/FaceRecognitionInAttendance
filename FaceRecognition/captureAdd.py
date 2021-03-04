# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'captureAdd.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AdminCaptureAdd(object):
    def setupUi(self, AdminCaptureAdd):
        AdminCaptureAdd.setObjectName("AdminCaptureAdd")
        AdminCaptureAdd.resize(506, 371)
        AdminCaptureAdd.setStyleSheet("background-color: rgb(190, 190, 190);")
        self.centralwidget = QtWidgets.QWidget(AdminCaptureAdd)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(70, 0, 371, 191))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btn_Add = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(12)
        self.btn_Add.setFont(font)
        self.btn_Add.setStyleSheet("background-color: rgb(117, 117, 117);\n"
"color: rgb(255, 255, 255);")
        self.btn_Add.setObjectName("btn_Add")
        self.gridLayout_2.addWidget(self.btn_Add, 1, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.txt_number = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(12)
        self.txt_number.setFont(font)
        self.txt_number.setStyleSheet("font: 12pt \"Rockwell Condensed\";\n"
"color: rgb(255,255,255);")
        self.txt_number.setObjectName("txt_number")
        self.gridLayout.addWidget(self.txt_number, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 0, 127);")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 220, 171, 111))
        self.label_2.setStyleSheet("image: url(Aydin.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        AdminCaptureAdd.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AdminCaptureAdd)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 506, 21))
        self.menubar.setObjectName("menubar")
        AdminCaptureAdd.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AdminCaptureAdd)
        self.statusbar.setObjectName("statusbar")
        AdminCaptureAdd.setStatusBar(self.statusbar)

        self.retranslateUi(AdminCaptureAdd)
        QtCore.QMetaObject.connectSlotsByName(AdminCaptureAdd)

    def retranslateUi(self, AdminCaptureAdd):
        _translate = QtCore.QCoreApplication.translate
        AdminCaptureAdd.setWindowTitle(_translate("AdminCaptureAdd", "Capture Add"))
        self.btn_Add.setText(_translate("AdminCaptureAdd", "ADD"))
        self.label.setText(_translate("AdminCaptureAdd", "STUDENT NUMBER:"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AdminCaptureAdd = QtWidgets.QMainWindow()
    ui = Ui_AdminCaptureAdd()
    ui.setupUi(AdminCaptureAdd)
    AdminCaptureAdd.show()
    sys.exit(app.exec_())
