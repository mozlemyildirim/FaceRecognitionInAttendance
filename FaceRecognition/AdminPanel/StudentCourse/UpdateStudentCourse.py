# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UpdateStudentCourse.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AdminStuCourseUpdate(object):
    def setupUi(self, AdminStuCourseUpdate):
        AdminStuCourseUpdate.setObjectName("AdminStuCourseUpdate")
        AdminStuCourseUpdate.resize(438, 401)
        AdminStuCourseUpdate.setStyleSheet("background-color: rgb(186, 186, 186);")
        self.centralwidget = QtWidgets.QWidget(AdminStuCourseUpdate)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 0, 341, 221))
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
        self.btn_Update = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_Update.setStyleSheet("background-color: rgb(136, 136, 136);\n"
"color: rgb(255, 255, 255);\n"
"font: 12pt \"Rockwell Condensed\";")
        self.btn_Update.setObjectName("btn_Update")
        self.gridLayout.addWidget(self.btn_Update, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 240, 161, 121))
        self.label_2.setStyleSheet("image: url(Aydin.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        AdminStuCourseUpdate.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AdminStuCourseUpdate)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 438, 21))
        self.menubar.setObjectName("menubar")
        AdminStuCourseUpdate.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AdminStuCourseUpdate)
        self.statusbar.setObjectName("statusbar")
        AdminStuCourseUpdate.setStatusBar(self.statusbar)

        self.retranslateUi(AdminStuCourseUpdate)
        QtCore.QMetaObject.connectSlotsByName(AdminStuCourseUpdate)

    def retranslateUi(self, AdminStuCourseUpdate):
        _translate = QtCore.QCoreApplication.translate
        AdminStuCourseUpdate.setWindowTitle(_translate("AdminStuCourseUpdate", "Student Course Update"))
        self.label_3.setText(_translate("AdminStuCourseUpdate", "COURSE :"))
        self.label_4.setText(_translate("AdminStuCourseUpdate", "STUDENT :"))
        self.btn_Update.setText(_translate("AdminStuCourseUpdate", "UPDATE"))





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AdminStuCourseUpdate = QtWidgets.QMainWindow()
    ui = Ui_AdminStuCourseUpdate()
    ui.setupUi(AdminStuCourseUpdate)
    AdminStuCourseUpdate.show()
    sys.exit(app.exec_())
