# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StudentAssignment.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Student_Assignmet(object):
    def setupUi(self, Student_Assignmet):
        Student_Assignmet.setObjectName("Student_Assignmet")
        Student_Assignmet.resize(697, 513)
        Student_Assignmet.setStyleSheet("background-color: rgb(212, 212, 212);")
        self.centralwidget = QtWidgets.QWidget(Student_Assignmet)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_Assignment = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Assignment.setGeometry(QtCore.QRect(50, 0, 311, 46))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_Assignment.setFont(font)
        self.btn_Assignment.setStyleSheet("background-color: rgb(129, 129, 129);\n"
"color: rgb(255, 255, 255);\n"
"font: 24pt \"Rockwell Condensed\";")
        self.btn_Assignment.setObjectName("btn_Assignment")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(50, 50, 601, 401))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.tableWidget = QtWidgets.QTableWidget(self.splitter)
        self.tableWidget.setStyleSheet("font: 12pt \"Rockwell Condensed\";\n"
"color: rgb(0, 0, 127);")
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
        self.label_2 = QtWidgets.QLabel(self.splitter)
        self.label_2.setGeometry(QtCore.QRect(310, 320, 141, 131))
        self.label_2.setStyleSheet("image: url(Aydin.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        Student_Assignmet.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Student_Assignmet)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 697, 22))
        self.menubar.setObjectName("menubar")
        Student_Assignmet.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Student_Assignmet)
        self.statusbar.setObjectName("statusbar")
        Student_Assignmet.setStatusBar(self.statusbar)

        self.retranslateUi(Student_Assignmet)
        QtCore.QMetaObject.connectSlotsByName(Student_Assignmet)

    def retranslateUi(self, Student_Assignmet):
        _translate = QtCore.QCoreApplication.translate
        Student_Assignmet.setWindowTitle(_translate("Student_Assignmet", "Student Assignmet"))
        self.btn_Assignment.setText(_translate("Student_Assignmet", "TAKE ASSIGNMENT"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Student_Assignmet", "STUDENT ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Student_Assignmet", "NAME"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Student_Assignmet", "SURNAME"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Student_Assignmet", "COURSE"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Student_Assignmet", "DATE"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Student_Assignmet", "ASSIGNMENT"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Student_Assignmet = QtWidgets.QMainWindow()
    ui = Ui_Student_Assignmet()
    ui.setupUi(Student_Assignmet)
    Student_Assignmet.show()
    sys.exit(app.exec_())
