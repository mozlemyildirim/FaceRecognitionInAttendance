from Student import Ui_AdminStudent
from AddStudent import  Ui_AdminAddStudent
from EditStudent import Ui_AdminUpdateStudent
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWidgets import QApplication,QDialog,QMainWindow,QMessageBox,QTableWidgetItem

import sqlite3
conn = sqlite3.connect('Students.db')
curs = conn.cursor()

class MainApp(QtWidgets.QMainWindow,Ui_AdminStudent):
    def __init__(self,parent=None):
        super(MainApp,self).__init__(parent)
        self.setupUi(self)
       # self.Load_AllStudents()
        self.Init_Ui()
    def Init_Ui(self):
        self.show()
        self.btn_Add.clicked.connect(self.Show_Add_Student)
        self.btn_Edit.clicked.connect(self.Show_Update_Student)
        #self.btn_GetAll.clicked.connect(self.Load_Database)
        self.btn_Delete.clicked.connect(self.Delete_Data)
        content = 'SELECT * FROM Department'
        res = curs.execute(content)
        self.stu_Combo.addItem("Select")
        for row in enumerate(res):
            data = row[1]
            name = data[1]
            id = data[0]
            self.stu_Combo.addItem(name) 
        self.stu_Combo.currentIndexChanged.connect(self.Load_Database)
    
    def Load_AllStudents(self):
        res = curs.execute("SELECT TC,StudentId,Name,Surname,FatherName,BirthDate,BirthPlace FROM Student")
        for row_index,row_data in enumerate(res):
            self.tableWidget.insertRow(row_index)
            for colm_index,colm_data in enumerate(row_data):
               self.tableWidget.setItem(row_index,colm_index,QTableWidgetItem(str(colm_data)))
            
    def Load_Database(self):
        while self.tableWidget.rowCount() > 0 :
            self.tableWidget.removeRow(0)
        name = self.stu_Combo.currentText()
        res = curs.execute("SELECT * FROM Department WHERE Name = ? ",(name,))
        for row in enumerate(res):
                data = row[1]
                id = data[0]
        content = curs.execute("SELECT DISTINCT  TC,S.StudentId,S.Name,S.Surname,S.FatherName,S.BirthDate,S.BirthPlace FROM Student AS S INNER JOIN StudentCourse AS SC ON SC.StudentId = S.Id INNER JOIN Course AS C ON C.Id = SC.CourseId INNER JOIN Department AS D ON D.Id = C.DepartmentId WHERE D.Id =?",(id,))
        for row_index,row_data in enumerate(content):
           self.tableWidget.insertRow(row_index)
           for colm_index,colm_data in enumerate(row_data):
               self.tableWidget.setItem(row_index,colm_index,QTableWidgetItem(str(colm_data)))
        return
    def Show_Add_Student(self):
        self.adding = AddStudent()
        self.adding.btn_Add.clicked.connect(self.Add_Data)
        self.adding.show()
    def Add_Data(self):
        s_id = self.adding.txt_StudentId.text()
        tc = self.adding.txt_Tc.text()
        name = self.adding.txt_Name.text()
        surname = self.adding.txt_Surname.text()
        fathername = self.adding.txt_FatherName.text()
        date = self.adding.dateEdit.date()
        birthDate = date.toPyDate()
        birthPlace = self.adding.txt_BirthPlace.text()
        try:
            curs.execute('INSERT INTO Student(StudentId,TC,Name,Surname,FatherName,BirthDate,BirthPlace) VALUES (?,?,?,?,?,?,?)',(s_id,tc,name,surname,fathername,birthDate,birthPlace))
            conn.commit()
            QMessageBox.about(self, "Add Student", "The Adding Process is Successful")
            self.adding.hide()
            # self.Load_Database()
        except Exception as error :
            QMessageBox.about(self, "Add Student Error", "Please Try Again.")
    def Show_Update_Student(self):
        self.adding = UpdateStudent()
        self.adding.btn_Add.clicked.connect(self.Update_Data)
        name = self.stu_Combo.currentText()
        res = curs.execute("SELECT * FROM Department WHERE Name = ? ",(name,))
        for row in enumerate(res):
                data = row[1]
                id = data[0]
        content = curs.execute("SELECT DISTINCT  TC,S.StudentId,S.Name,S.Surname,S.FatherName,S.BirthDate,S.BirthPlace FROM Student AS S INNER JOIN StudentCourse AS SC ON SC.StudentId = S.Id INNER JOIN Course AS C ON C.Id = SC.CourseId INNER JOIN Department AS D ON D.Id = C.DepartmentId WHERE D.Id =?",(id,))
        for row in enumerate(content): 
            if row[0] == self.tableWidget.currentRow():
                data = row[1]
                tc = data[0]
                stu_id = data[1]
                name = data[2]
                surname = data[3]
                fathername = data[4]
                #birthDate = data[5]
                birthPlace = data[6]
                self.adding.txt_StudentId.setText(stu_id)
                self.adding.txt_Tc.setText(tc)
                self.adding.txt_Name.setText(name)
                self.adding.txt_Surname.setText(surname)
                self.adding.txt_FatherName.setText(fathername)
                self.adding.dateEdit_2.setDate(QtCore.QDate(1998, 6, 23))
                self.adding.txt_BirthPlace.setText(birthPlace)
        self.adding.show()
    def Update_Data(self):
        s_id = self.adding.txt_StudentId.text()
        tc = self.adding.txt_Tc.text()
        name = self.adding.txt_Name.text()
        surname = self.adding.txt_Surname.text()
        fathername = self.adding.txt_FatherName.text()
        date = self.adding.dateEdit_2.date()
        birthDate = date.toPyDate()
        birthPlace = self.adding.txt_BirthPlace.text()
        content = 'SELECT * FROM Student'
        res = curs.execute(content)
        for row in enumerate(res): 
            if row[0] == self.tableWidget.currentRow():
                data = row[1]
                ids = data[0]
                s_ids = data[1]
                tcs = data[2]
                names = data[3]
                surnames = data[4]
                fathernames = data[5]
                birthDates = data[6]
                birthPlaces = data[7]
        try:
            curs.execute('UPDATE Student SET StudentId = ?,TC = ?,Name = ?,Surname  =?,FatherName = ?,BirthDate = ?,BirthPlace = ?  WHERE Id = ?',(s_id,tc,name,surname,fathername,birthDate,birthPlace,ids))
            conn.commit()
            QMessageBox.about(self, "Update Student", "The Update Process is Successful")
            self.adding.hide()
            self.Load_Database()
        except Exception as error :
            QMessageBox.about(self, "Update Student Error", "Please Try Again.")
    
  
    def  Delete_Data(self):
        name = self.stu_Combo.currentText()
        res = curs.execute("SELECT * FROM Department WHERE Name = ? ",(name,))
        for row in enumerate(res):
                data = row[1]
                id = data[0]
        content = curs.execute("SELECT DISTINCT S.Id,SC.StudentId,SC.CourseId FROM Student AS S INNER JOIN StudentCourse AS SC ON SC.StudentId = S.Id INNER JOIN Course AS C ON C.Id = SC.CourseId INNER JOIN Department AS D ON D.Id = C.DepartmentId WHERE D.Id =?",(id,))
        for row in enumerate(content): 
            if row[0] == self.tableWidget.currentRow():
                data = row[1]
                id = data[0]
                stu_id = data[1]
                course_id = data[2]
                try : 
                    curs.execute("DELETE FROM Student WHERE Id = ? ",(id,))
                    conn.commit()
                    curs.execute("DELETE FROM StudentCourse WHERE StudentId = ? AND CourseId = ? ",(stu_id,course_id))
                    conn.commit()
                    QMessageBox.about(self, "Delete Student", "The Delete Process is Successful")
                    self.Load_Database()
                except Exception as error :
                    QMessageBox.about(self, "Update Student Error", "Please Try Again.")


class AddStudent(QtWidgets.QMainWindow,Ui_AdminAddStudent):
    def __init__(self,parent=None):
        super(AddStudent,self).__init__(parent)
        self.setupUi(self)

class UpdateStudent(QtWidgets.QMainWindow,Ui_AdminUpdateStudent):
    def __init__(self,parent=None):
        super(UpdateStudent,self).__init__(parent)
        self.setupUi(self)

import sys
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainApp()
    w.show()
    sys.exit(app.exec_())