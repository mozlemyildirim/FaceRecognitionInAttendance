from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QDialog,QMainWindow,QMessageBox,QTableWidgetItem
from Login import Ui_MainWindow
import sqlite3
import sys
sys.path.insert(0,'AdminPanel/MainWindow/')
import mainApp
conn = sqlite3.connect('Students.db')
curs = conn.cursor()
class MainApp(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(MainApp,self).__init__(parent)
        self.setupUi(self)
        self.btn_Login.clicked.connect(self.Show_Login)
        #self.Init_Ui()

    def Show_Login(self):
        content = "SELECT * FROM Users"
        res = curs.execute(content)
        for row in enumerate(res):
            data = row[1]
            id = data[0]
            user_name = data[1]
            user_password= data[2]
        text_name = self.txt_username.text()
        text_password = self.txt_password.text()
        if user_name == text_name and user_password == text_password:
            self.adding = mainApp.MainApp()
            self.adding.show()
            self.hide()
        else :
            QMessageBox.about(self, "Sign In", "Undefined username or password, please try again. ")
        


if __name__ == "__main__":
   
    app = QtWidgets.QApplication(sys.argv)
    w = MainApp()
    w.show()
    sys.exit(app.exec_())
