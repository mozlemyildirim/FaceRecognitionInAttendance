# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AdminMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AdminPanel(object):
    def setupUi(self, AdminPanel):
        AdminPanel.setObjectName("AdminPanel")
        AdminPanel.resize(488, 436)
        AdminPanel.setStyleSheet("background-color: rgb(195, 195, 195);")
        self.centralwidget = QtWidgets.QWidget(AdminPanel)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btn_Department = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(20)
        self.btn_Department.setFont(font)
        self.btn_Department.setStyleSheet("\n"
"background-color: rgb(122, 122, 122);color: rgb(255, 255, 255);")
        self.btn_Department.setObjectName("btn_Department")
        self.gridLayout_2.addWidget(self.btn_Department, 1, 0, 1, 1)
        self.btn_StudentCourse = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(20)
        self.btn_StudentCourse.setFont(font)
        self.btn_StudentCourse.setStyleSheet("\n"
"background-color: rgb(122, 122, 122);color: rgb(255, 255, 255);")
        self.btn_StudentCourse.setObjectName("btn_StudentCourse")
        self.gridLayout_2.addWidget(self.btn_StudentCourse, 2, 0, 1, 1)
        self.btn_Capture = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(20)
        self.btn_Capture.setFont(font)
        self.btn_Capture.setStyleSheet("\n"
"background-color: rgb(122, 122, 122);color: rgb(255, 255, 255);")
        self.btn_Capture.setObjectName("btn_Capture")
        self.gridLayout_2.addWidget(self.btn_Capture, 5, 0, 1, 1)
        self.btn_Course = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(20)
        self.btn_Course.setFont(font)
        self.btn_Course.setStyleSheet("\n"
"background-color: rgb(122, 122, 122);color: rgb(255, 255, 255);")
        self.btn_Course.setObjectName("btn_Course")
        self.gridLayout_2.addWidget(self.btn_Course, 3, 0, 1, 1)
        self.btn_Student = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(20)
        self.btn_Student.setFont(font)
        self.btn_Student.setStyleSheet("\n"
"background-color: rgb(122, 122, 122);color: rgb(255, 255, 255);")
        self.btn_Student.setObjectName("btn_Student")
        self.gridLayout_2.addWidget(self.btn_Student, 4, 0, 1, 1)
        self.btn_Assignment = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(20)
        self.btn_Assignment.setFont(font)
        self.btn_Assignment.setStyleSheet("\n"
"background-color: rgb(122, 122, 122);\n"
"color: rgb(255, 255, 255);")
        self.btn_Assignment.setObjectName("btn_Assignment")
        self.gridLayout_2.addWidget(self.btn_Assignment, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        AdminPanel.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AdminPanel)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 488, 21))
        self.menubar.setObjectName("menubar")
        AdminPanel.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AdminPanel)
        self.statusbar.setObjectName("statusbar")
        AdminPanel.setStatusBar(self.statusbar)

        self.retranslateUi(AdminPanel)
        QtCore.QMetaObject.connectSlotsByName(AdminPanel)

    def retranslateUi(self, AdminPanel):
        _translate = QtCore.QCoreApplication.translate
        AdminPanel.setWindowTitle(_translate("AdminPanel", "AdminPanel"))
        self.btn_Department.setText(_translate("AdminPanel", "DEPARTMENT"))
        self.btn_StudentCourse.setText(_translate("AdminPanel", "STUDENT COURSE"))
        self.btn_Capture.setText(_translate("AdminPanel", "CAPTURE"))
        self.btn_Course.setText(_translate("AdminPanel", "COURSE"))
        self.btn_Student.setText(_translate("AdminPanel", "STUDENT"))
        self.btn_Assignment.setText(_translate("AdminPanel", "ASSIGNMENT"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AdminPanel = QtWidgets.QMainWindow()
    ui = Ui_AdminPanel()
    ui.setupUi(AdminPanel)
    AdminPanel.show()
    sys.exit(app.exec_())
