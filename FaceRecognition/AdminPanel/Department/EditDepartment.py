# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EditDepartment.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AdminUpdateDepartment(object):
    def setupUi(self, AdminUpdateDepartment):
        AdminUpdateDepartment.setObjectName("AdminUpdateDepartment")
        AdminUpdateDepartment.resize(346, 335)
        AdminUpdateDepartment.setStyleSheet("color: rgb(0, 0, 127);\n"
"font: 12pt \"Rockwell Condensed\";\n"
"background-color: rgb(184, 184, 184);")
        self.centralwidget = QtWidgets.QWidget(AdminUpdateDepartment)
        self.centralwidget.setObjectName("centralwidget")
        self.txt_deptName = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_deptName.setGeometry(QtCore.QRect(140, 40, 113, 25))
        self.txt_deptName.setStyleSheet("font: 12pt \"Rockwell Condensed\";\n"
"color: rgb(255,255,255);")
        self.txt_deptName.setObjectName("txt_deptName")
        self.btn_update = QtWidgets.QPushButton(self.centralwidget)
        self.btn_update.setGeometry(QtCore.QRect(170, 80, 80, 25))
        self.btn_update.setStyleSheet("background-color: rgb(117, 117, 117);\n"
"color: rgb(255, 255, 255);")
        self.btn_update.setObjectName("btn_update")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 40, 54, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 170, 151, 111))
        self.label_2.setStyleSheet("image: url(Aydin.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        AdminUpdateDepartment.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AdminUpdateDepartment)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 346, 25))
        self.menubar.setObjectName("menubar")
        AdminUpdateDepartment.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AdminUpdateDepartment)
        self.statusbar.setObjectName("statusbar")
        AdminUpdateDepartment.setStatusBar(self.statusbar)

        self.retranslateUi(AdminUpdateDepartment)
        QtCore.QMetaObject.connectSlotsByName(AdminUpdateDepartment)

    def retranslateUi(self, AdminUpdateDepartment):
        _translate = QtCore.QCoreApplication.translate
        AdminUpdateDepartment.setWindowTitle(_translate("AdminUpdateDepartment", "Update Department"))
        self.btn_update.setText(_translate("AdminUpdateDepartment", "UPDATE"))
        self.label.setText(_translate("AdminUpdateDepartment", "NAME :"))





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AdminUpdateDepartment = QtWidgets.QMainWindow()
    ui = Ui_AdminUpdateDepartment()
    ui.setupUi(AdminUpdateDepartment)
    AdminUpdateDepartment.show()
    sys.exit(app.exec_())
