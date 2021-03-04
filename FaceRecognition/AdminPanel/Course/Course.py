# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Course.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AdminCourse(object):
    def setupUi(self, AdminCourse):
        AdminCourse.setObjectName("AdminCourse")
        AdminCourse.resize(567, 478)
        AdminCourse.setStyleSheet("background-color: rgb(186, 186, 186);")
        self.centralwidget = QtWidgets.QWidget(AdminCourse)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 60, 501, 231))
        self.tableWidget.setStyleSheet("color: rgb(0, 0, 127);\n"
"font: 12pt \"Rockwell Condensed\";")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
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
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(210, 310, 141, 131))
        self.label_8.setStyleSheet("image: url(Aydin.png);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(1, 11, 221, 33))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setStyleSheet("font: 12pt \"Rockwell Condensed\";\n"
"color: rgb(0, 0, 127);")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.deptCombo = QtWidgets.QComboBox(self.layoutWidget)
        self.deptCombo.setStyleSheet("font: 12pt \"Rockwell Condensed\";\n"
"color: rgb(255,255,255);")
        self.deptCombo.setObjectName("deptCombo")
        self.horizontalLayout.addWidget(self.deptCombo)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(232, 11, 301, 33))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_Add = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_Add.setFont(font)
        self.btn_Add.setStyleSheet("background-color: rgb(136, 136, 136);\n"
"color: rgb(255, 255, 255);\n"
"font: 12pt \"Rockwell Condensed\";")
        self.btn_Add.setObjectName("btn_Add")
        self.gridLayout.addWidget(self.btn_Add, 0, 0, 1, 1)
        self.btn_Delete = QtWidgets.QPushButton(self.widget)
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
        self.gridLayout.addWidget(self.btn_Delete, 0, 1, 1, 1)
        self.btn_Edit = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_Edit.setFont(font)
        self.btn_Edit.setStyleSheet("background-color: rgb(136, 136, 136);\n"
"color: rgb(255, 255, 255);\n"
"font: 12pt \"Rockwell Condensed\";")
        self.btn_Edit.setObjectName("btn_Edit")
        self.gridLayout.addWidget(self.btn_Edit, 0, 2, 1, 1)
        AdminCourse.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AdminCourse)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 567, 22))
        self.menubar.setObjectName("menubar")
        AdminCourse.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AdminCourse)
        self.statusbar.setObjectName("statusbar")
        AdminCourse.setStatusBar(self.statusbar)

        self.retranslateUi(AdminCourse)
        QtCore.QMetaObject.connectSlotsByName(AdminCourse)

    def retranslateUi(self, AdminCourse):
        _translate = QtCore.QCoreApplication.translate
        AdminCourse.setWindowTitle(_translate("AdminCourse", "Course"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("AdminCourse", "DEPARTMENT"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("AdminCourse", "COURSE"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("AdminCourse", "DAY"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("AdminCourse", "START HOUR"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("AdminCourse", "END HOUR"))
        self.label.setText(_translate("AdminCourse", "DEPARTMENT:"))
        self.btn_Add.setText(_translate("AdminCourse", "ADD"))
        self.btn_Delete.setText(_translate("AdminCourse", "DELETE"))
        self.btn_Edit.setText(_translate("AdminCourse", "EDIT"))





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AdminCourse = QtWidgets.QMainWindow()
    ui = Ui_AdminCourse()
    ui.setupUi(AdminCourse)
    AdminCourse.show()
    sys.exit(app.exec_())
