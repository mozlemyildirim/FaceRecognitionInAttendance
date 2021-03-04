# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AdminAssigmentEdit.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AdminAssEdit(object):
    def setupUi(self, AdminAssEdit):
        AdminAssEdit.setObjectName("AdminAssEdit")
        AdminAssEdit.resize(350, 336)
        AdminAssEdit.setStyleSheet("background-color: rgb(185, 185, 185);")
        self.centralwidget = QtWidgets.QWidget(AdminAssEdit)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_Update = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Update.setGeometry(QtCore.QRect(220, 100, 80, 25))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(12)
        self.btn_Update.setFont(font)
        self.btn_Update.setStyleSheet("background-color: rgb(117, 117, 117);\n"
"color: rgb(255, 255, 255);")
        self.btn_Update.setObjectName("btn_Update")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 20, 271, 51))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 0, 127);")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.txt_Iscome = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(12)
        self.txt_Iscome.setFont(font)
        self.txt_Iscome.setStyleSheet("color: rgb(255, 255, 255);")
        self.txt_Iscome.setObjectName("txt_Iscome")
        self.horizontalLayout.addWidget(self.txt_Iscome)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 170, 151, 111))
        self.label_2.setStyleSheet("image: url(Aydin.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        AdminAssEdit.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AdminAssEdit)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 350, 21))
        self.menubar.setObjectName("menubar")
        AdminAssEdit.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AdminAssEdit)
        self.statusbar.setObjectName("statusbar")
        AdminAssEdit.setStatusBar(self.statusbar)

        self.retranslateUi(AdminAssEdit)
        QtCore.QMetaObject.connectSlotsByName(AdminAssEdit)

    def retranslateUi(self, AdminAssEdit):
        _translate = QtCore.QCoreApplication.translate
        AdminAssEdit.setWindowTitle(_translate("AdminAssEdit", "Admin Assignment Edit"))
        self.btn_Update.setText(_translate("AdminAssEdit", "EDIT"))
        self.label.setText(_translate("AdminAssEdit", "IS COME :"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AdminAssEdit = QtWidgets.QMainWindow()
    ui = Ui_AdminAssEdit()
    ui.setupUi(AdminAssEdit)
    AdminAssEdit.show()
    sys.exit(app.exec_())
