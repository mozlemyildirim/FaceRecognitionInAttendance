# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(615, 474)
        #MainWindow.setStyleSheet("background-image: url(:/newPrefix/012.jpg);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(410, 30, 265, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-60, -30, 731, 471))
        self.label.setStyleSheet("image: url(aaaa.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.btn_adminPanel = QtWidgets.QPushButton(self.centralwidget)
        self.btn_adminPanel.setGeometry(QtCore.QRect(350, 320, 191, 39))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(20)
        self.btn_adminPanel.setFont(font)
        self.btn_adminPanel.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(80, 126, 59, 200);")
        self.btn_adminPanel.setObjectName("btn_adminPanel")
        self.btn_Assignment = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Assignment.setGeometry(QtCore.QRect(100, 320, 201, 39))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(20)
        self.btn_Assignment.setFont(font)
        self.btn_Assignment.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(80, 126, 59, 200);")
        self.btn_Assignment.setObjectName("btn_Assignment")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 615, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_adminPanel.setText(_translate("MainWindow", "ADMIN PANEL"))
        self.btn_Assignment.setText(_translate("MainWindow", "ASSIGNMENT"))


# import ma_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
