# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CaptureDelete.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CaptureDelete(object):
    def setupUi(self, CaptureDelete):
        CaptureDelete.setObjectName("CaptureDelete")
        CaptureDelete.resize(505, 382)
        CaptureDelete.setStyleSheet("background-color: rgb(193, 193, 193);")
        self.centralwidget = QtWidgets.QWidget(CaptureDelete)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(80, 20, 351, 191))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 0, 127);")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.txt_number = QtWidgets.QLineEdit(self.layoutWidget)
        self.txt_number.setStyleSheet("font: 12pt \"Rockwell Condensed\";\n"
"color: rgb(255, 255, 255);")
        self.txt_number.setObjectName("txt_number")
        self.gridLayout.addWidget(self.txt_number, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.btn_Delete = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(12)
        self.btn_Delete.setFont(font)
        self.btn_Delete.setStyleSheet("background-color: rgb(117, 117, 117);\n"
"color: rgb(255, 255, 255);")
        self.btn_Delete.setObjectName("btn_Delete")
        self.gridLayout_2.addWidget(self.btn_Delete, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 230, 171, 111))
        self.label_2.setStyleSheet("image: url(Aydin.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        CaptureDelete.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CaptureDelete)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 505, 21))
        self.menubar.setObjectName("menubar")
        CaptureDelete.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CaptureDelete)
        self.statusbar.setObjectName("statusbar")
        CaptureDelete.setStatusBar(self.statusbar)

        self.retranslateUi(CaptureDelete)
        QtCore.QMetaObject.connectSlotsByName(CaptureDelete)

    def retranslateUi(self, CaptureDelete):
        _translate = QtCore.QCoreApplication.translate
        CaptureDelete.setWindowTitle(_translate("CaptureDelete", "Capture Delete"))
        self.label.setText(_translate("CaptureDelete", "STUDENT NUMBER:"))
        self.btn_Delete.setText(_translate("CaptureDelete", "DELETE"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CaptureDelete = QtWidgets.QMainWindow()
    ui = Ui_CaptureDelete()
    ui.setupUi(CaptureDelete)
    CaptureDelete.show()
    sys.exit(app.exec_())
