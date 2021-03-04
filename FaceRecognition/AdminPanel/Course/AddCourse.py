# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddCourse.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AdminAddCourse(object):
    def setupUi(self, AdminAddCourse):
        AdminAddCourse.setObjectName("AdminAddCourse")
        AdminAddCourse.resize(352, 375)
        AdminAddCourse.setStyleSheet("background-color: rgb(186, 186, 186);")
        self.centralwidget = QtWidgets.QWidget(AdminAddCourse)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(80, 0, 204, 184))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setStyleSheet("font: 12pt \"Rockwell Condensed\";\n"
"color: rgb(0, 0, 127);")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setStyleSheet("font: 12pt \"Rockwell Condensed\";\n"
"color: rgb(0, 0, 127);")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
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
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setStyleSheet("font: 12pt \"Rockwell Condensed\";\n"
"color: rgb(0, 0, 127);")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.dept_Combo = QtWidgets.QComboBox(self.layoutWidget)
        self.dept_Combo.setStyleSheet("font: 12pt \"Rockwell Condensed\";\n"
"color: rgb(255,255,255);")
        self.dept_Combo.setObjectName("dept_Combo")
        self.verticalLayout.addWidget(self.dept_Combo)
        self.txt_Course = QtWidgets.QLineEdit(self.layoutWidget)
        self.txt_Course.setStyleSheet("font: 12pt \"Rockwell Condensed\";\n"
"color: rgb(255,255,255);")
        self.txt_Course.setObjectName("txt_Course")
        self.verticalLayout.addWidget(self.txt_Course)
        self.txt_Day = QtWidgets.QLineEdit(self.layoutWidget)
        self.txt_Day.setStyleSheet("font: 12pt \"Rockwell Condensed\";\n"
"color: rgb(255,255,255);")
        self.txt_Day.setObjectName("txt_Day")
        self.verticalLayout.addWidget(self.txt_Day)
        self.txt_StartHour = QtWidgets.QLineEdit(self.layoutWidget)
        self.txt_StartHour.setStyleSheet("font: 12pt \"Rockwell Condensed\";\n"
"color: rgb(255,255,255);")
        self.txt_StartHour.setObjectName("txt_StartHour")
        self.verticalLayout.addWidget(self.txt_StartHour)
        self.txt_EndHour = QtWidgets.QLineEdit(self.layoutWidget)
        self.txt_EndHour.setStyleSheet("font: 12pt \"Rockwell Condensed\";\n"
"color: rgb(255,255,255);")
        self.txt_EndHour.setObjectName("txt_EndHour")
        self.verticalLayout.addWidget(self.txt_EndHour)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.btn_Add = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_Add.setStyleSheet("background-color: rgb(136, 136, 136);\n"
"color: rgb(255, 255, 255);\n"
"font: 12pt \"Rockwell Condensed\";")
        self.btn_Add.setObjectName("btn_Add")
        self.gridLayout.addWidget(self.btn_Add, 1, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(90, 200, 181, 131))
        self.label_8.setStyleSheet("image: url(Aydin.png);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        AdminAddCourse.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AdminAddCourse)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 352, 21))
        self.menubar.setObjectName("menubar")
        AdminAddCourse.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AdminAddCourse)
        self.statusbar.setObjectName("statusbar")
        AdminAddCourse.setStatusBar(self.statusbar)

        self.retranslateUi(AdminAddCourse)
        QtCore.QMetaObject.connectSlotsByName(AdminAddCourse)

    def retranslateUi(self, AdminAddCourse):
        _translate = QtCore.QCoreApplication.translate
        AdminAddCourse.setWindowTitle(_translate("AdminAddCourse", "Add Course"))
        self.label.setText(_translate("AdminAddCourse", "DEPARTMENT :"))
        self.label_2.setText(_translate("AdminAddCourse", "COURSE :"))
        self.label_3.setText(_translate("AdminAddCourse", "DAY:"))
        self.label_4.setText(_translate("AdminAddCourse", "START HOUR:"))
        self.label_5.setText(_translate("AdminAddCourse", "END HOUR:"))
        self.btn_Add.setText(_translate("AdminAddCourse", "ADD"))





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AdminAddCourse = QtWidgets.QMainWindow()
    ui = Ui_AdminAddCourse()
    ui.setupUi(AdminAddCourse)
    AdminAddCourse.show()
    sys.exit(app.exec_())
