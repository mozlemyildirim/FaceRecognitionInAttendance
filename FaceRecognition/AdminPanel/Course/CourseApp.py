from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QDialog,QMainWindow,QMessageBox,QTableWidgetItem
from Course import Ui_AdminCourse
from AddCourse import Ui_AdminAddCourse
from UpdateCourse import Ui_AdminUpdateCourse
import sqlite3
conn = sqlite3.connect('Students.db')
curs = conn.cursor()
class MainApp(QtWidgets.QMainWindow,Ui_AdminCourse):
    def __init__(self,parent=None):
        super(MainApp,self).__init__(parent)
        self.setupUi(self)
        #self.Load_Database()
        self.Init_Ui()
    def Init_Ui(self):
        self.show()
        self.btn_Add.clicked.connect(self.Show_AddCourse)
        self.btn_Edit.clicked.connect(self.Show_UpdateCourse)
        self.btn_Delete.clicked.connect(self.Delete_Data)
        content = 'SELECT * FROM Department'
        res = curs.execute(content)
        self.deptCombo.addItem("Select")
        for row in enumerate(res):
            data = row[1]
            name = data[1]
            id = data[0]
            self.deptCombo.addItem(name)
        self.deptCombo.currentIndexChanged.connect(self.Load_Database)
    def Load_Database(self):
        while self.tableWidget.rowCount() > 0 :
            self.tableWidget.removeRow(0)
        name = self.deptCombo.currentText()
        res = curs.execute("SELECT * FROM Department WHERE Name = ? ",(name,))
        for row in enumerate(res):
                data = row[1]
                id = data[0]
        content = curs.execute("SELECT D.Name,C.Name,C.Day,C.StartHour,C.EndHour FROM Course AS C INNER JOIN Department AS D ON D.Id = C.DepartmentId WHERE C.DepartmentId  = ?",(id,))
        for row_index,row_data in enumerate(content):
           self.tableWidget.insertRow(row_index)
           for colm_index,colm_data in enumerate(row_data):
               self.tableWidget.setItem(row_index,colm_index,QTableWidgetItem(str(colm_data)))
        return

    def Show_AddCourse(self):
        self.adding = AddCourse()
        self.adding.btn_Add.clicked.connect(self.Add_Data)
        content = 'SELECT * FROM Department'
        res = curs.execute(content)
        self.adding.dept_Combo.addItem("Select") 
        for row in enumerate(res):
            data = row[1]
            name = data[1]
            id = data[0]
            self.adding.dept_Combo.addItem(name)
        
        self.adding.show()
    
    def Add_Data(self):
        name = self.adding.dept_Combo.currentText()
        res = curs.execute("SELECT * FROM Department WHERE Name = ? ",(name,))
        for row in enumerate(res):
                data = row[1]
                id = data[0]
        dept_id = id
        course_Name = self.adding.txt_Course.text()
        day = self.adding.txt_Day.text()
        start_Hour = self.adding.txt_StartHour.text()
        end_Hour = self.adding.txt_EndHour.text()
        try:
            curs.execute('INSERT INTO Course(Name,Day,StartHour,EndHour,DepartmentId) VALUES (?,?,?,?,?)',(course_Name,day,start_Hour,end_Hour,dept_id))
            conn.commit()
            QMessageBox.about(self, "Add Course", "The Adding Process is Successful")
            self.adding.hide()
            self.Load_Database()
        except Exception as error :
            QMessageBox.about(self, "Add Course Error", "Please Try Again")
    
    def Show_UpdateCourse(self):
        self.adding = UpdateCourse()
        self.adding.btn_Update.clicked.connect(self.Update_Data)
        name = self.deptCombo.currentText()
        res = curs.execute("SELECT * FROM Department WHERE Name = ? ",(name,))
        for row in enumerate(res):
                data = row[1]
                id = data[0]
        dep_id = id
        content = curs.execute("SELECT D.Name,C.Name,C.Day,C.StartHour,C.EndHour FROM Course AS C INNER JOIN Department AS D ON D.Id = C.DepartmentId WHERE C.DepartmentId  = ?",(dep_id,))
        for row in enumerate(res): 
            if row[0] == self.tableWidget.currentRow():
                data = row[1]
                course_Name = data[1]
                day = data[2]
                start_Hour = data[3]
                end_Hour = data[4]
                self.adding.txt_Course.setText(str(course_Name))
                self.adding.txt_Day.setText(str(day))
                self.adding.txt_StartHour.setText(str(start_Hour))
                self.adding.txt_EndHour.setText(str(end_Hour))
        self.adding.show()

    def Update_Data(self):
        course_Name = self.adding.txt_Course.text()
        day = self.adding.txt_Day.text()
        start_Hour = self.adding.txt_StartHour.text()
        end_Hour = self.adding.txt_EndHour.text()
        name = self.deptCombo.currentText()
        res = curs.execute("SELECT * FROM Department WHERE Name = ? ",(name,))
        for row in enumerate(res):
                data = row[1]
                id = data[0]
        dept_id = id
        res2 = curs.execute('SELECT * FROM Course WHERE DepartmentId = ?',(id,))
        for row in enumerate(res2): 
            if row[0] == self.tableWidget.currentRow():
                data = row[1]
                id = data[0]
        try:
            curs.execute('UPDATE Course SET Name = ?,Day = ?,StartHour = ?,EndHour = ?,DepartmentId = ? WHERE Id = ?',(course_Name,day,start_Hour,end_Hour,dept_id,id))
            conn.commit()
            QMessageBox.about(self, "Update Course", "The Update Process is Successful")
            self.adding.hide()
            self.Load_Database()
        except Exception as error :
            QMessageBox.about(self, "Update Course Error", "Please Try Again")

    def Delete_Data(self):
        name = self.deptCombo.currentText()
        res = curs.execute("SELECT * FROM Department WHERE Name = ? ",(name,))
        for row in enumerate(res):
                data = row[1]
                id = data[0]
        res2 = curs.execute('SELECT * FROM Course WHERE DepartmentId = ?',(id,))
        for row in enumerate(res2): 
            if row[0] == self.tableWidget.currentRow():
                data = row[1]
                id = data[0]
                #print(name)
                try:
                    curs.execute("DELETE FROM Course WHERE Id = ? ",(id,))
                    conn.commit()
                    QMessageBox.about(self, "Delete Course", "The Delete Process is Successful")
                    self.Load_Database()
                except Exception as error :
                    QMessageBox.about(self, "Delete Course Error", "Please Try Again")
class AddCourse(QtWidgets.QMainWindow,Ui_AdminAddCourse):
    def __init__(self,parent=None):
        super(AddCourse,self).__init__(parent)
        self.setupUi(self)

class UpdateCourse(QtWidgets.QMainWindow,Ui_AdminUpdateCourse):
    def __init__(self,parent=None):
        super(UpdateCourse,self).__init__(parent)
        self.setupUi(self)
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainApp()
    w.show()
    sys.exit(app.exec_())
