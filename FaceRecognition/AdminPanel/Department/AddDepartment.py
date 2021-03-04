# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddDepartment.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AdminAddDepartment(object):
    def setupUi(self, AdminAddDepartment):
        AdminAddDepartment.setObjectName("AdminAddDepartment")
        AdminAddDepartment.resize(346, 343)
        AdminAddDepartment.setStyleSheet("font: 12pt \"Rockwell Condensed\";\n"
"color: rgb(0, 0, 127);\n"
"background-color: rgb(190, 190, 190);")
        self.centralwidget = QtWidgets.QWidget(AdminAddDepartment)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 30, 54, 20))
        self.label.setObjectName("label")
        self.txt_deptName = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_deptName.setGeometry(QtCore.QRect(140, 30, 113, 25))
        self.txt_deptName.setStyleSheet("color: rgb(255, 255, 255);")
        self.txt_deptName.setText("")
        self.txt_deptName.setObjectName("txt_deptName")
        self.btn_add = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add.setGeometry(QtCore.QRect(170, 70, 80, 25))
        self.btn_add.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(126, 126, 126);")
        self.btn_add.setObjectName("btn_add")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 150, 161, 121))
        self.label_2.setStyleSheet("image: url(Aydin.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        AdminAddDepartment.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AdminAddDepartment)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 346, 25))
        self.menubar.setObjectName("menubar")
        AdminAddDepartment.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AdminAddDepartment)
        self.statusbar.setObjectName("statusbar")
        AdminAddDepartment.setStatusBar(self.statusbar)

        self.retranslateUi(AdminAddDepartment)
        QtCore.QMetaObject.connectSlotsByName(AdminAddDepartment)

    def retranslateUi(self, AdminAddDepartment):
        _translate = QtCore.QCoreApplication.translate
        AdminAddDepartment.setWindowTitle(_translate("AdminAddDepartment", "Add Department"))
        self.label.setText(_translate("AdminAddDepartment", "NAME :"))
        self.btn_add.setText(_translate("AdminAddDepartment", "INSERT"))





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AdminAddDepartment = QtWidgets.QMainWindow()
    ui = Ui_AdminAddDepartment()
    ui.setupUi(AdminAddDepartment)
    AdminAddDepartment.show()
    sys.exit(app.exec_())
