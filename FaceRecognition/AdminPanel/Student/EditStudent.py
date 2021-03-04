# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EditStudent.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AdminUpdateStudent(object):
    def setupUi(self, AdminUpdateStudent):
        AdminUpdateStudent.setObjectName("AdminUpdateStudent")
        AdminUpdateStudent.resize(447, 530)
        AdminUpdateStudent.setStyleSheet("background-color: rgb(186, 186, 186);")
        self.centralwidget = QtWidgets.QWidget(AdminUpdateStudent)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(101, 10, 239, 237))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("font: 12pt \"Rockwell Condensed\";\n"
"color: rgb(0, 0, 127);")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)
        self.txt_Tc = QtWidgets.QLineEdit(self.layoutWidget)
        self.txt_Tc.setStyleSheet("font: 12pt \"Rockwell Condensed\";\n"
"color: rgb(255,255,255);")
        self.txt_Tc.setObjectName("txt_Tc")
        self.gridLayout.addWidget(self.txt_Tc, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 12pt \"Rockwell Condensed\";\n"
"color: rgb(0, 0, 127);")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.txt_StudentId = QtWidgets.QLineEdit(self.layoutWidget)
        self.txt_StudentId.setStyleSheet("font: 12pt \"Rockwell Condensed\";\n"
"color: rgb(255,255,255);")
        self.txt_StudentId.setObjectName("txt_StudentId")
        self.gridLayout.addWidget(self.txt_StudentId, 1, 1, 1, 1)
        self.txt_Name = QtWidgets.QLineEdit(self.layoutWidget)
        self.txt_Name.setStyleSheet("font: 12pt \"Rockwell Condensed\";\n"
"color: rgb(255,255,255);")
        self.txt_Name.setObjectName("txt_Name")
        self.gridLayout.addWidget(self.txt_Name, 2, 1, 1, 1)
        self.dateEdit_2 = QtWidgets.QDateEdit(self.layoutWidget)
        self.dateEdit_2.setStyleSheet("font: 12pt \"Rockwell Condensed\";\n"
"color: rgb(255,255,255);")
        self.dateEdit_2.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(2015, 12, 31), QtCore.QTime(23, 59, 59)))
        self.dateEdit_2.setMaximumDate(QtCore.QDate(2015, 12, 31))
        self.dateEdit_2.setMinimumDate(QtCore.QDate(1920, 9, 15))
        self.dateEdit_2.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.dateEdit_2.setCurrentSectionIndex(0)
        self.dateEdit_2.setDate(QtCore.QDate(1998, 3, 18))
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.gridLayout.addWidget(self.dateEdit_2, 8, 1, 1, 1)
        self.txt_BirthPlace = QtWidgets.QLineEdit(self.layoutWidget)
        self.txt_BirthPlace.setStyleSheet("font: 12pt \"Rockwell Condensed\";\n"
"color: rgb(255,255,255);")
        self.txt_BirthPlace.setObjectName("txt_BirthPlace")
        self.gridLayout.addWidget(self.txt_BirthPlace, 9, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("font: 12pt \"Rockwell Condensed\";\n"
"color: rgb(0, 0, 127);")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 8, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("font: 12pt \"Rockwell Condensed\";\n"
"color: rgb(0, 0, 127);")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 9, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font: 12pt \"Rockwell Condensed\";\n"
"color: rgb(0, 0, 127);")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("font: 12pt \"Rockwell Condensed\";\n"
"color: rgb(0, 0, 127);")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.txt_Surname = QtWidgets.QLineEdit(self.layoutWidget)
        self.txt_Surname.setStyleSheet("font: 12pt \"Rockwell Condensed\";\n"
"color: rgb(255,255,255);")
        self.txt_Surname.setObjectName("txt_Surname")
        self.gridLayout.addWidget(self.txt_Surname, 3, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("font: 12pt \"Rockwell Condensed\";\n"
"color: rgb(0, 0, 127);")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.txt_FatherName = QtWidgets.QLineEdit(self.layoutWidget)
        self.txt_FatherName.setStyleSheet("font: 12pt \"Rockwell Condensed\";\n"
"color: rgb(255,255,255);")
        self.txt_FatherName.setObjectName("txt_FatherName")
        self.gridLayout.addWidget(self.txt_FatherName, 4, 1, 1, 1)
        self.btn_Add = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Add.setGeometry(QtCore.QRect(260, 270, 81, 31))
        self.btn_Add.setStyleSheet("background-color: rgb(136, 136, 136);\n"
"color: rgb(255, 255, 255);\n"
"font: 12pt \"Rockwell Condensed\";")
        self.btn_Add.setObjectName("btn_Add")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(140, 340, 181, 131))
        self.label_8.setStyleSheet("image: url(Aydin.png);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        AdminUpdateStudent.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AdminUpdateStudent)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 447, 21))
        self.menubar.setObjectName("menubar")
        AdminUpdateStudent.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AdminUpdateStudent)
        self.statusbar.setObjectName("statusbar")
        AdminUpdateStudent.setStatusBar(self.statusbar)

        self.retranslateUi(AdminUpdateStudent)
        QtCore.QMetaObject.connectSlotsByName(AdminUpdateStudent)

    def retranslateUi(self, AdminUpdateStudent):
        _translate = QtCore.QCoreApplication.translate
        AdminUpdateStudent.setWindowTitle(_translate("AdminUpdateStudent", "Edit Student"))
        self.label_7.setText(_translate("AdminUpdateStudent", "STUDENT ID:"))
        self.label.setText(_translate("AdminUpdateStudent", "TC:"))
        self.dateEdit_2.setDisplayFormat(_translate("AdminUpdateStudent", "d.MM.yyyy"))
        self.label_5.setText(_translate("AdminUpdateStudent", "BIRTHDATE:"))
        self.label_6.setText(_translate("AdminUpdateStudent", "BIRTHPLACE:"))
        self.label_2.setText(_translate("AdminUpdateStudent", "NAME:"))
        self.label_3.setText(_translate("AdminUpdateStudent", "SURNAME:"))
        self.label_4.setText(_translate("AdminUpdateStudent", "FATHER NAME:"))
        self.btn_Add.setText(_translate("AdminUpdateStudent", "UPDATE"))





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AdminUpdateStudent = QtWidgets.QMainWindow()
    ui = Ui_AdminUpdateStudent()
    ui.setupUi(AdminUpdateStudent)
    AdminUpdateStudent.show()
    sys.exit(app.exec_())
