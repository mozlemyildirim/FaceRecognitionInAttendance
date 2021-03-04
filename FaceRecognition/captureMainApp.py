from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QDialog,QMainWindow,QMessageBox,QTableWidgetItem
from captureAdd import Ui_AdminCaptureAdd
from CaptureMain import Ui_AdminCapture
from CaptureDelete import Ui_CaptureDelete
import sqlite3
import capture
import trainer
conn = sqlite3.connect('Students.db')
curs = conn.cursor()
class MainApp(QtWidgets.QMainWindow,Ui_AdminCapture):
    def __init__(self,parent=None):
        super(MainApp,self).__init__(parent)
        self.setupUi(self)
        # self.Load_Database()
        self.Init_Ui()
    def Init_Ui(self):
         self.show()
         self.btn_Add.clicked.connect(self.Show_AddCapture)
         self.btn_Delete.clicked.connect(self.Show_DeleteCapture)
    

    def Show_AddCapture(self):
        self.adding = AddCapture()
        self.adding.btn_Add.clicked.connect(self.Add_Data)
        self.adding.show()
        
    def Add_Data(self):
        stu_Number = self.adding.txt_number.text()
        capture.CreateFace(stu_Number)
        trainer.train()
    def Show_DeleteCapture(self):
        self.adding = DeleteCapture()
        self.adding.btn_Delete.clicked.connect(self.Delete_Data)
        self.adding.show()

    def Delete_Data(self):
        stu_Number = self.adding.txt_number.text()
        capture.DeleteFace(stu_Number)
        trainer.train()
class AddCapture(QtWidgets.QMainWindow,Ui_AdminCaptureAdd):
    def __init__(self,parent=None):
        super(AddCapture,self).__init__(parent)
        self.setupUi(self)

class DeleteCapture(QtWidgets.QMainWindow,Ui_CaptureDelete):
    def __init__(self,parent=None):
        super(DeleteCapture,self).__init__(parent)
        self.setupUi(self)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MainApp()
    w.show()
    sys.exit(app.exec_())