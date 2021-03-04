import sys
from PyQt5 import QtWidgets
from MainWindow import Ui_MainWindow
from PyQt5.QtWidgets import QApplication,QDialog,QMainWindow,QMessageBox,QTableWidgetItem
sys.path.insert(0,'AdminPanel/Login')
sys.path.insert(0,'Assignment/')
import LoginApp
import StudentAssignApp,allAssignments
    

class MainApp(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(MainApp,self).__init__(parent)
        self.setupUi(self)
        allAssignments.alwaysRunning()
        self.Init_Ui()
    def Init_Ui(self):
        self.show()
        self.btn_adminPanel.clicked.connect(self.Show_AdminAssignment)
        self.btn_Assignment.clicked.connect(self.Show_StudentAssignment)

    def Show_AdminAssignment(self):
         self.adding = LoginApp.MainApp()
         self.adding.show()
    def Show_StudentAssignment(self):
         self.adding = StudentAssignApp.MainApp()
         self.adding.show()

#allAssignments.alwaysRunning()
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainApp()
    w.show()
    sys.exit(app.exec_())
