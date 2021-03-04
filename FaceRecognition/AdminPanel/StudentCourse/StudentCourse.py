# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StudentCourse.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AdminStuCourse(object):
    def setupUi(self, AdminStuCourse):
        AdminStuCourse.setObjectName("AdminStuCourse")
        AdminStuCourse.resize(504, 492)
        AdminStuCourse.setStyleSheet("background-color: rgb(188, 188, 188);")
        self.centralwidget = QtWidgets.QWidget(AdminStuCourse)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 90, 451, 221))
        self.tableWidget.setStyleSheet("font: 12pt \"Rockwell Condensed\";\n"
"color: rgb(0, 0, 127);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 81, 17))
        self.label.setStyleSheet("color: rgb(0, 0, 127);\n"
"font: 12pt \"Rockwell Condensed\";")
        self.label.setObjectName("label")
        self.dept_Combo = QtWidgets.QComboBox(self.centralwidget)
        self.dept_Combo.setGeometry(QtCore.QRect(110, 20, 121, 25))
        self.dept_Combo.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"Rockwell Condensed\";")
        self.dept_Combo.setObjectName("dept_Combo")
        self.btn_Edit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Edit.setGeometry(QtCore.QRect(330, 20, 80, 25))
        self.btn_Edit.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(136, 136, 136);\n"
"font: 12pt \"Rockwell Condensed\";")
        self.btn_Edit.setObjectName("btn_Edit")
        self.btn_Delete = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Delete.setGeometry(QtCore.QRect(410, 20, 80, 25))
        self.btn_Delete.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(136, 136, 136);\n"
"font: 12pt \"Rockwell Condensed\";")
        self.btn_Delete.setObjectName("btn_Delete")
        self.btn_Show = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Show.setGeometry(QtCore.QRect(150, 60, 80, 25))
        self.btn_Show.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(136, 136, 136);\n"
"font: 12pt \"Rockwell Condensed\";")
        self.btn_Show.setObjectName("btn_Show")
        self.btn_add = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add.setGeometry(QtCore.QRect(240, 20, 80, 25))
        self.btn_add.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(136, 136, 136);\n"
"font: 12pt \"Rockwell Condensed\";")
        self.btn_add.setObjectName("btn_add")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 330, 161, 121))
        self.label_2.setStyleSheet("image: url(Aydin.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        AdminStuCourse.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AdminStuCourse)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 504, 21))
        self.menubar.setObjectName("menubar")
        AdminStuCourse.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AdminStuCourse)
        self.statusbar.setObjectName("statusbar")
        AdminStuCourse.setStatusBar(self.statusbar)

        self.retranslateUi(AdminStuCourse)
        QtCore.QMetaObject.connectSlotsByName(AdminStuCourse)

    def retranslateUi(self, AdminStuCourse):
        _translate = QtCore.QCoreApplication.translate
        AdminStuCourse.setWindowTitle(_translate("AdminStuCourse", "Student Course"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("AdminStuCourse", "COURSE"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("AdminStuCourse", "NUMBER"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("AdminStuCourse", "STUDENT NAME"))
        self.label.setText(_translate("AdminStuCourse", "DEPARTMENT :"))
        self.btn_Edit.setText(_translate("AdminStuCourse", "EDIT"))
        self.btn_Delete.setText(_translate("AdminStuCourse", "DELETE"))
        self.btn_Show.setText(_translate("AdminStuCourse", "SHOW"))
        self.btn_add.setText(_translate("AdminStuCourse", "ADD"))





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AdminStuCourse = QtWidgets.QMainWindow()
    ui = Ui_AdminStuCourse()
    ui.setupUi(AdminStuCourse)
    AdminStuCourse.show()
    sys.exit(app.exec_())
