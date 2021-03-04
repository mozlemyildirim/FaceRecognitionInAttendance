# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UpdateCourse.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AdminUpdateCourse(object):
    def setupUi(self, AdminUpdateCourse):
        AdminUpdateCourse.setObjectName("AdminUpdateCourse")
        AdminUpdateCourse.resize(352, 409)
        AdminUpdateCourse.setStyleSheet("background-color: rgb(186, 186, 186);")
        self.centralwidget = QtWidgets.QWidget(AdminUpdateCourse)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(70, 10, 211, 181))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setStyleSheet("font: 12pt \"Rockwell Condensed\";\n"
"color: rgb(0, 0, 127);")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setStyleSheet("font: 12pt \"Rockwell Condensed\";\n"
"color: rgb(0, 0, 127);")
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_9.setStyleSheet("font: 12pt \"Rockwell Condensed\";\n"
"color: rgb(0, 0, 127);")
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        self.label_10.setStyleSheet("font: 12pt \"Rockwell Condensed\";\n"
"color: rgb(0, 0, 127);")
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.label_10)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
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
        self.btn_Update = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_Update.setStyleSheet("background-color: rgb(136, 136, 136);\n"
"color: rgb(255, 255, 255);\n"
"font: 12pt \"Rockwell Condensed\";")
        self.btn_Update.setObjectName("btn_Update")
        self.gridLayout.addWidget(self.btn_Update, 1, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(100, 210, 141, 131))
        self.label_11.setStyleSheet("image: url(Aydin.png);")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        AdminUpdateCourse.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AdminUpdateCourse)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 352, 21))
        self.menubar.setObjectName("menubar")
        AdminUpdateCourse.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AdminUpdateCourse)
        self.statusbar.setObjectName("statusbar")
        AdminUpdateCourse.setStatusBar(self.statusbar)

        self.retranslateUi(AdminUpdateCourse)
        QtCore.QMetaObject.connectSlotsByName(AdminUpdateCourse)

    def retranslateUi(self, AdminUpdateCourse):
        _translate = QtCore.QCoreApplication.translate
        AdminUpdateCourse.setWindowTitle(_translate("AdminUpdateCourse", "Update Course"))
        self.label_7.setText(_translate("AdminUpdateCourse", "COURSE :"))
        self.label_8.setText(_translate("AdminUpdateCourse", "DAY:"))
        self.label_9.setText(_translate("AdminUpdateCourse", "START HOUR:"))
        self.label_10.setText(_translate("AdminUpdateCourse", "END HOUR:"))
        self.btn_Update.setText(_translate("AdminUpdateCourse", "UPDATE"))





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AdminUpdateCourse = QtWidgets.QMainWindow()
    ui = Ui_AdminUpdateCourse()
    ui.setupUi(AdminUpdateCourse)
    AdminUpdateCourse.show()
    sys.exit(app.exec_())
