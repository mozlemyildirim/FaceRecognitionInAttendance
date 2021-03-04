# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Capture.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AdminCapture(object):
    def setupUi(self, AdminCapture):
        AdminCapture.setObjectName("AdminCapture")
        AdminCapture.resize(397, 379)
        AdminCapture.setStyleSheet("background-color: rgb(184, 184, 184);")
        self.centralwidget = QtWidgets.QWidget(AdminCapture)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(80, 0, 241, 201))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_Add = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(20)
        self.btn_Add.setFont(font)
        self.btn_Add.setStyleSheet("background-color: rgb(131, 131, 131);\n"
"color: rgb(255, 255, 255);")
        self.btn_Add.setObjectName("btn_Add")
        self.gridLayout.addWidget(self.btn_Add, 0, 0, 1, 1)
        self.btn_Delete = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(20)
        self.btn_Delete.setFont(font)
        self.btn_Delete.setStyleSheet("background-color: rgb(134, 134, 134);\n"
"color: rgb(255, 255, 255);")
        self.btn_Delete.setObjectName("btn_Delete")
        self.gridLayout.addWidget(self.btn_Delete, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 220, 151, 111))
        self.label_2.setStyleSheet("image: url(Aydin.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        AdminCapture.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AdminCapture)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 397, 21))
        self.menubar.setObjectName("menubar")
        AdminCapture.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AdminCapture)
        self.statusbar.setObjectName("statusbar")
        AdminCapture.setStatusBar(self.statusbar)

        self.retranslateUi(AdminCapture)
        QtCore.QMetaObject.connectSlotsByName(AdminCapture)

    def retranslateUi(self, AdminCapture):
        _translate = QtCore.QCoreApplication.translate
        AdminCapture.setWindowTitle(_translate("AdminCapture", "Capture"))
        self.btn_Add.setText(_translate("AdminCapture", "ADD"))
        self.btn_Delete.setText(_translate("AdminCapture", "DELETE"))


# import asd_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AdminCapture = QtWidgets.QMainWindow()
    ui = Ui_AdminCapture()
    ui.setupUi(AdminCapture)
    AdminCapture.show()
    sys.exit(app.exec_())
