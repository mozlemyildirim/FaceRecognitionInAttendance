# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AdminAssigment.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Admin_Assignment(object):
    def setupUi(self, Admin_Assignment):
        Admin_Assignment.setObjectName("Admin_Assignment")
        Admin_Assignment.resize(451, 541)
        Admin_Assignment.setStyleSheet("background-color: rgb(203, 203, 203);")
        self.centralwidget = QtWidgets.QWidget(Admin_Assignment)
        self.centralwidget.setObjectName("centralwidget")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(40, 10, 381, 481))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.widget = QtWidgets.QWidget(self.splitter)
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btn_Edit = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(12)
        self.btn_Edit.setFont(font)
        self.btn_Edit.setStyleSheet("background-color: rgb(117, 117, 117);\n"
"color: rgb(255, 255, 255);")
        self.btn_Edit.setObjectName("btn_Edit")
        self.gridLayout_2.addWidget(self.btn_Edit, 0, 0, 1, 1)
        self.btn_Delete = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(12)
        self.btn_Delete.setFont(font)
        self.btn_Delete.setStyleSheet("background-color: rgb(117, 117, 117);\n"
"color: rgb(255, 255, 255);")
        self.btn_Delete.setObjectName("btn_Delete")
        self.gridLayout_2.addWidget(self.btn_Delete, 0, 1, 1, 1)
        self.widget1 = QtWidgets.QWidget(self.splitter)
        self.widget1.setObjectName("widget1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.courseBox = QtWidgets.QComboBox(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(12)
        self.courseBox.setFont(font)
        self.courseBox.setStyleSheet("font: 12pt \"Rockwell Condensed\";\n"
"color: rgb(255,255,255);")
        self.courseBox.setObjectName("courseBox")
        self.verticalLayout.addWidget(self.courseBox)
        self.dateEdit = QtWidgets.QDateEdit(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(12)
        self.dateEdit.setFont(font)
        self.dateEdit.setStyleSheet("font: 12pt \"Rockwell Condensed\";\n"
"color: rgb(255,255,255);")
        self.dateEdit.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(2019, 12, 31), QtCore.QTime(23, 59, 59)))
        self.dateEdit.setMaximumDate(QtCore.QDate(2019, 12, 31))
        self.dateEdit.setMinimumDate(QtCore.QDate(2010, 12, 31))
        self.dateEdit.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.dateEdit.setCurrentSectionIndex(0)
        self.dateEdit.setDate(QtCore.QDate(2019, 4, 1))
        self.dateEdit.setObjectName("dateEdit")
        self.verticalLayout.addWidget(self.dateEdit)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 0, 127);")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 0, 127);")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.btn_Show = QtWidgets.QPushButton(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(12)
        self.btn_Show.setFont(font)
        self.btn_Show.setStyleSheet("background-color: rgb(117, 117, 117);\n"
"color: rgb(255, 255, 255);")
        self.btn_Show.setObjectName("btn_Show")
        self.gridLayout_3.addWidget(self.btn_Show, 1, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.splitter)
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(12)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("color: rgb(0, 0, 127);\n"
"font: 12pt \"Rockwell Condensed\";")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
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
        self.label_3 = QtWidgets.QLabel(self.splitter)
        self.label_3.setGeometry(QtCore.QRect(310, 320, 141, 131))
        self.label_3.setStyleSheet("image: url(Aydin.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        Admin_Assignment.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Admin_Assignment)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 451, 21))
        self.menubar.setObjectName("menubar")
        Admin_Assignment.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Admin_Assignment)
        self.statusbar.setObjectName("statusbar")
        Admin_Assignment.setStatusBar(self.statusbar)

        self.retranslateUi(Admin_Assignment)
        QtCore.QMetaObject.connectSlotsByName(Admin_Assignment)

    def retranslateUi(self, Admin_Assignment):
        _translate = QtCore.QCoreApplication.translate
        Admin_Assignment.setWindowTitle(_translate("Admin_Assignment", "Admin Assignment"))
        self.btn_Edit.setText(_translate("Admin_Assignment", "EDIT"))
        self.btn_Delete.setText(_translate("Admin_Assignment", "DELETE"))
        self.dateEdit.setDisplayFormat(_translate("Admin_Assignment", "d.MM.yyyy"))
        self.label.setText(_translate("Admin_Assignment", "COURSE :"))
        self.label_2.setText(_translate("Admin_Assignment", "DATE :"))
        self.btn_Show.setText(_translate("Admin_Assignment", "SHOW"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Admin_Assignment", "COURSE"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Admin_Assignment", "DATE"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Admin_Assignment", "NUMBER"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Admin_Assignment", "NAME"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Admin_Assignment", "SURNAME"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Admin_Assignment", "IS COME"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Admin_Assignment = QtWidgets.QMainWindow()
    ui = Ui_Admin_Assignment()
    ui.setupUi(Admin_Assignment)
    Admin_Assignment.show()
    sys.exit(app.exec_())
