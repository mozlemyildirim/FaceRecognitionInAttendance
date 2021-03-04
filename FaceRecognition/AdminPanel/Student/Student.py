# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Student.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AdminStudent(object):
    def setupUi(self, AdminStudent):
        AdminStudent.setObjectName("AdminStudent")
        AdminStudent.resize(742, 496)
        AdminStudent.setAcceptDrops(False)
        AdminStudent.setStyleSheet("background-color: rgb(186, 186, 186);")
        self.centralwidget = QtWidgets.QWidget(AdminStudent)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(9, 44, 701, 241))
        self.tableWidget.setStyleSheet("color: rgb(0, 0, 127);\n"
"font: 12pt \"Rockwell Condensed\";")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(310, 320, 141, 131))
        self.label_8.setStyleSheet("image: url(Aydin.png);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(9, 9, 291, 23))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label = QtWidgets.QLabel(self.splitter)
        self.label.setStyleSheet("font: 12pt \"Rockwell Condensed\";\n"
"color: rgb(0, 0, 127);")
        self.label.setObjectName("label")
        self.stu_Combo = QtWidgets.QComboBox(self.splitter)
        self.stu_Combo.setStyleSheet("font: 12pt \"Rockwell Condensed\";\n"
"color: rgb(255,255,255);")
        self.stu_Combo.setObjectName("stu_Combo")
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setGeometry(QtCore.QRect(480, 10, 225, 27))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.btn_Add = QtWidgets.QPushButton(self.splitter_2)
        self.btn_Add.setStyleSheet("background-color: rgb(136, 136, 136);\n"
"color: rgb(255, 255, 255);\n"
"font: 12pt \"Rockwell Condensed\";\n"
"")
        self.btn_Add.setObjectName("btn_Add")
        self.btn_Edit = QtWidgets.QPushButton(self.splitter_2)
        self.btn_Edit.setStyleSheet("background-color: rgb(136, 136, 136);\n"
"color: rgb(255, 255, 255);\n"
"font: 12pt \"Rockwell Condensed\";")
        self.btn_Edit.setObjectName("btn_Edit")
        self.btn_Delete = QtWidgets.QPushButton(self.splitter_2)
        self.btn_Delete.setStyleSheet("background-color: rgb(136, 136, 136);\n"
"color: rgb(255, 255, 255);\n"
"font: 12pt \"Rockwell Condensed\";")
        self.btn_Delete.setObjectName("btn_Delete")
        AdminStudent.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AdminStudent)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 742, 21))
        self.menubar.setObjectName("menubar")
        AdminStudent.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AdminStudent)
        self.statusbar.setObjectName("statusbar")
        AdminStudent.setStatusBar(self.statusbar)

        self.retranslateUi(AdminStudent)
        QtCore.QMetaObject.connectSlotsByName(AdminStudent)

    def retranslateUi(self, AdminStudent):
        _translate = QtCore.QCoreApplication.translate
        AdminStudent.setWindowTitle(_translate("AdminStudent", "Student"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("AdminStudent", "TC"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("AdminStudent", "STUDENT ID"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("AdminStudent", "NAME"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("AdminStudent", "SURNAME"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("AdminStudent", "FATHER NAME"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("AdminStudent", "BIRTH DATE"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("AdminStudent", "BIRTH PLACE"))
        self.label.setText(_translate("AdminStudent", "SELECT DEPARTMENT :"))
        self.btn_Add.setText(_translate("AdminStudent", "ADD"))
        self.btn_Edit.setText(_translate("AdminStudent", "EDIT"))
        self.btn_Delete.setText(_translate("AdminStudent", "DELETE"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AdminStudent = QtWidgets.QMainWindow()
    ui = Ui_AdminStudent()
    ui.setupUi(AdminStudent)
    AdminStudent.show()
    sys.exit(app.exec_())
