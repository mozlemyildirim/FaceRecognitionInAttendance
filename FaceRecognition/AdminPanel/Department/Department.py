# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Department.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Department(object):
    def setupUi(self, Department):
        Department.setObjectName("Department")
        Department.resize(632, 540)
        font = QtGui.QFont()
        font.setPointSize(9)
        Department.setFont(font)
        Department.setStyleSheet("background-color: rgb(186, 186, 186);")
        self.centralwidget = QtWidgets.QWidget(Department)
        self.centralwidget.setObjectName("centralwidget")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(140, 10, 361, 481))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.btn_edit = QtWidgets.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_edit.setFont(font)
        self.btn_edit.setStyleSheet("background-color: rgb(136, 136, 136);\n"
"color: rgb(255, 255, 255);\n"
"font: 12pt \"Rockwell Condensed\";")
        self.btn_edit.setObjectName("btn_edit")
        self.btn_add = QtWidgets.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_add.setFont(font)
        self.btn_add.setStyleSheet("background-color: rgb(136, 136, 136);\n"
"color: rgb(255, 255, 255);\n"
"font: 12pt \"Rockwell Condensed\";")
        self.btn_add.setObjectName("btn_add")
        self.btn_Delete = QtWidgets.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_Delete.setFont(font)
        self.btn_Delete.setStyleSheet("background-color: rgb(136, 136, 136);\n"
"color: rgb(255, 255, 255);\n"
"font: 12pt \"Rockwell Condensed\";")
        self.btn_Delete.setObjectName("btn_Delete")
        self.tableWidget = QtWidgets.QTableWidget(self.splitter)
        self.tableWidget.setStyleSheet("font: 12pt \"Rockwell Condensed\";\n"
"color: rgb(0, 0, 127);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.label_2 = QtWidgets.QLabel(self.splitter)
        self.label_2.setGeometry(QtCore.QRect(310, 320, 141, 131))
        self.label_2.setStyleSheet("image: url(Aydin.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        Department.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Department)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 632, 21))
        self.menubar.setObjectName("menubar")
        Department.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Department)
        self.statusbar.setObjectName("statusbar")
        Department.setStatusBar(self.statusbar)

        self.retranslateUi(Department)
        QtCore.QMetaObject.connectSlotsByName(Department)

    def retranslateUi(self, Department):
        _translate = QtCore.QCoreApplication.translate
        Department.setWindowTitle(_translate("Department", "Department"))
        self.btn_edit.setText(_translate("Department", "EDIT"))
        self.btn_add.setText(_translate("Department", "ADD"))
        self.btn_Delete.setText(_translate("Department", "DELETE"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Department", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Department", "NAME"))





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Department = QtWidgets.QMainWindow()
    ui = Ui_Department()
    ui.setupUi(Department)
    Department.show()
    sys.exit(app.exec_())
