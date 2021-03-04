# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddStudentCourse.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AdminStuCourseAdd(object):
    def setupUi(self, AdminStuCourseAdd):
        AdminStuCourseAdd.setObjectName("AdminStuCourseAdd")
        AdminStuCourseAdd.resize(422, 472)
        AdminStuCourseAdd.setStyleSheet("background-color: rgb(186, 186, 186);")
        self.centralwidget = QtWidgets.QWidget(AdminStuCourseAdd)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 30, 341, 221))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setStyleSheet("font: 12pt \"Rockwell Condensed\";\n"
"color: rgb(0, 0, 127);")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setStyleSheet("font: 12pt \"Rockwell Condensed\";\n"
"color: rgb(0, 0, 127);")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.courseCombo = QtWidgets.QComboBox(self.layoutWidget)
        self.courseCombo.setStyleSheet("font: 12pt \"Rockwell Condensed\";\n"
"color: rgb(255,255,255);")
        self.courseCombo.setObjectName("courseCombo")
        self.verticalLayout.addWidget(self.courseCombo)
        self.studentCombo = QtWidgets.QComboBox(self.layoutWidget)
        self.studentCombo.setStyleSheet("font: 12pt \"Rockwell Condensed\";\n"
"color: rgb(255,255,255);")
        self.studentCombo.setObjectName("studentCombo")
        self.verticalLayout.addWidget(self.studentCombo)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.btn_Add = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_Add.setStyleSheet("background-color: rgb(136, 136, 136);\n"
"color: rgb(255, 255, 255);\n"
"font: 12pt \"Rockwell Condensed\";")
        self.btn_Add.setObjectName("btn_Add")
        self.gridLayout.addWidget(self.btn_Add, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 290, 161, 121))
        self.label_2.setStyleSheet("image: url(Aydin.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        AdminStuCourseAdd.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AdminStuCourseAdd)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 422, 21))
        self.menubar.setObjectName("menubar")
        AdminStuCourseAdd.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AdminStuCourseAdd)
        self.statusbar.setObjectName("statusbar")
        AdminStuCourseAdd.setStatusBar(self.statusbar)

        self.retranslateUi(AdminStuCourseAdd)
        QtCore.QMetaObject.connectSlotsByName(AdminStuCourseAdd)

    def retranslateUi(self, AdminStuCourseAdd):
        _translate = QtCore.QCoreApplication.translate
        AdminStuCourseAdd.setWindowTitle(_translate("AdminStuCourseAdd", "Add Student Courses "))
        self.label_3.setText(_translate("AdminStuCourseAdd", "COURSE :"))
        self.label_4.setText(_translate("AdminStuCourseAdd", "STUDENT :"))
        self.btn_Add.setText(_translate("AdminStuCourseAdd", "ADD"))





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AdminStuCourseAdd = QtWidgets.QMainWindow()
    ui = Ui_AdminStuCourseAdd()
    ui.setupUi(AdminStuCourseAdd)
    AdminStuCourseAdd.show()
    sys.exit(app.exec_())
