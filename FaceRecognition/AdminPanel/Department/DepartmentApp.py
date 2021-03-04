from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QDialog,QMainWindow,QMessageBox,QTableWidgetItem
from Department import Ui_Department
from AddDepartment import Ui_AdminAddDepartment
from EditDepartment import Ui_AdminUpdateDepartment
import sqlite3
conn = sqlite3.connect('Students.db')
curs = conn.cursor()

class MainApp(QtWidgets.QMainWindow,Ui_Department):
  
    def __init__(self,parent=None):
        super(MainApp,self).__init__(parent)
        self.setupUi(self)
        self.Load_Database()
        self.Init_Ui()
    def Init_Ui(self):
        self.show()
        self.btn_add.clicked.connect(self.Show_AddDepartment)
        self.btn_edit.clicked.connect(self.Show_UpdateDepartment)
        self.btn_Delete.clicked.connect(self.Delete_Data)
    def Load_Database(self):
        while self.tableWidget.rowCount() > 0 :
            self.tableWidget.removeRow(0)
        conn = sqlite3.connect('Students.db')
        content = 'SELECT * FROM Department'
        res = curs.execute(content)
        for row_index,row_data in enumerate(res):
            self.tableWidget.insertRow(row_index)
            for colm_index,colm_data in enumerate(row_data):
                self.tableWidget.setItem(row_index,colm_index,QTableWidgetItem(str(colm_data)))
    def Show_AddDepartment(self):
        self.adding = AddDepartment()
        self.adding.btn_add.clicked.connect(self.Add_Data)
        self.adding.show()
    def Add_Data(self):
        name = self.adding.txt_deptName.text()
        try:
            curs.execute('INSERT INTO Department(Name) VALUES (?)',(name,))
            conn.commit()
            #print('Done')
            QMessageBox.about(self, "Add Department", "The Adding Process is Successful")
            self.adding.hide()
            self.Load_Database()

        except Exception as error :
            QMessageBox.about(self, "Add Department Error", "Please Try Again.")

    
    def Show_UpdateDepartment(self):
        self.adding = UpdateDepartment()
        self.adding.btn_update.clicked.connect(self.Update_Data)
        content = 'SELECT * FROM Department'
        res = curs.execute(content)
        for row in enumerate(res): 
            if row[0] == self.tableWidget.currentRow():
                data = row[1]
                name = data[1]
                self.adding.txt_deptName.setText(name)
        self.adding.show()
    
    def Update_Data(self):
        name = self.adding.txt_deptName.text()
        content = 'SELECT * FROM Department'
        res = curs.execute(content)
        for row in enumerate(res): 
            if row[0] == self.tableWidget.currentRow():
                data = row[1]
                id = data[0]
        try:
            curs.execute('UPDATE Department SET Name = ? WHERE Id = ?',(name,id))
            conn.commit()
            QMessageBox.about(self, "Update Department", "The Update Process is Successful")
            self.adding.hide()
            self.Load_Database()
        except Exception as error :
            QMessageBox.about(self, "Update Department Error", "Please Try Again")


    def Delete_Data(self):
        content = 'SELECT * FROM Department'
        res = curs.execute(content)
        for row in enumerate(res): 
            if row[0] == self.tableWidget.currentRow():
                data = row[1]
                id = data[0]
                #print(name)
                try : 
                    curs.execute("DELETE FROM Department WHERE Id = ? ",(id,))
                    conn.commit()
                    QMessageBox.about(self, "Delete Department", "The Delete Process is Successful")
                    self.Load_Database()
                except Exception as error :
                    QMessageBox.about(self, "Delete Department Error", "Please Try Again")
class AddDepartment(QtWidgets.QMainWindow,Ui_AdminAddDepartment):
    def __init__(self,parent=None):
        super(AddDepartment,self).__init__(parent)
        self.setupUi(self)

class UpdateDepartment(QtWidgets.QMainWindow,Ui_AdminUpdateDepartment):
    def __init__(self,parent=None):
        super(UpdateDepartment,self).__init__(parent)
        self.setupUi(self)
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainApp()
    w.show()
    sys.exit(app.exec_())
