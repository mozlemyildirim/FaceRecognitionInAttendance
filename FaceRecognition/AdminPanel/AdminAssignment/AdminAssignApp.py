from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QDialog,QMainWindow,QMessageBox,QTableWidgetItem
from AdminAssignment import Ui_Admin_Assignment
from AdminAssigmentEdit import Ui_AdminAssEdit
import sqlite3
conn = sqlite3.connect('Students.db')
curs = conn.cursor()

class MainApp(QtWidgets.QMainWindow,Ui_Admin_Assignment):
    def __init__(self,parent=None):
        super(MainApp,self).__init__(parent)
        self.setupUi(self)
        self.btn_Show.clicked.connect(self.Load_Database)
        self.btn_Edit.clicked.connect(self.Show_UpdateAssignment)
        self.btn_Delete.clicked.connect(self.Delete_Data)
        self.Init_Ui()
    def Init_Ui(self):
        self.show()
        content = 'SELECT * FROM Course'
        res = curs.execute(content)
        self.courseBox.addItem("Select")
        for row in enumerate(res):
            data = row[1]
            name = data[1]
            self.courseBox.addItem(name) 
    def Load_Database(self):
        while self.tableWidget.rowCount() > 0 :
            self.tableWidget.removeRow(0)
        course_Name = self.courseBox.currentText()
        date = self.dateEdit.date()
        course_Date = date.toPyDate()
        res = curs.execute("SELECT C.Name,A.Date,S.StudentId,S.Name,S.Surname,A.IsCame FROM Assignment AS A INNER JOIN StudentCourse AS SC ON SC.Id = A.StudentCourseId INNER JOIN Student AS S ON S.Id = SC.StudentId INNER JOIN Course AS C ON C.Id = SC.CourseId WHERE A.Date = ? AND C.Name = ? ORDER BY A.Id ASC",(course_Date,course_Name))
        for row_index,row_data in enumerate(res):
           self.tableWidget.insertRow(row_index)
           for colm_index,colm_data in enumerate(row_data):
               self.tableWidget.setItem(row_index,colm_index,QTableWidgetItem(str(colm_data)))
            
    def Show_UpdateAssignment(self):
        self.adding = UpdateAssignment()
        self.adding.btn_Update.clicked.connect(self.Update_Data)
        self.adding.show()
        course_Name = self.courseBox.currentText()
        date = self.dateEdit.date()
        course_Date = date.toPyDate()
        content = curs.execute("""SELECT A.Id,A.IsCame FROM Assignment AS A INNER JOIN StudentCourse AS SC ON SC.Id = A.StudentCourseId INNER JOIN Student AS S ON S.Id = SC.StudentId INNER JOIN Course AS C ON C.Id = SC.CourseId WHERE A.Date = ? AND C.Name = ?  ORDER BY A.Id ASC""",(course_Date,course_Name))
        for row in enumerate(content): 
            if row[0] == self.tableWidget.currentRow():
                data = row[1]
                id = data[0]
                is_Came = data[1]
                self.adding.txt_Iscome.setText(is_Came)
    def Update_Data(self):
        course_Name = self.courseBox.currentText()
        date = self.dateEdit.date()
        course_Date = date.toPyDate()
        content = curs.execute("""SELECT A.Id,A.IsCame FROM Assignment AS A INNER JOIN StudentCourse AS SC ON SC.Id = A.StudentCourseId INNER JOIN Student AS S ON S.Id = SC.StudentId INNER JOIN Course AS C ON C.Id = SC.CourseId WHERE A.Date = ? AND C.Name = ?  ORDER BY A.Id ASC""",(course_Date,course_Name))
        name = self.adding.txt_Iscome.text()
        for row in enumerate(content):
            data= row[1]
            id =  data[0]
            is_Came = data[1]
            try :
                curs.execute("UPDATE Assignment SET IsCame = ? WHERE Id = ?",(name,id))
                conn.commit()
                QMessageBox.about(self, "Update Assignment", "The Update Process is Successful ")
                self.adding.hide()
                self.Load_Database()
            except Exception as error :
                    QMessageBox.about(self, "Update Assignment Error", "Please Try Again")
    def Delete_Data(self):
        course_Name = self.courseBox.currentText()
        date = self.dateEdit.date()
        course_Date = date.toPyDate()
        content = curs.execute("""SELECT A.Id,A.IsCame FROM Assignment AS A INNER JOIN StudentCourse AS SC ON SC.Id = A.StudentCourseId INNER JOIN Student AS S ON S.Id = SC.StudentId INNER JOIN Course AS C ON C.Id = SC.CourseId WHERE A.Date = ? AND C.Name = ?  ORDER BY A.Id ASC""",(course_Date,course_Name))
        for row in enumerate(content): 
            if row[0] == self.tableWidget.currentRow():
                 data = row[1]
                 id = data[0]
                 try :
                    curs.execute("DELETE FROM Assignment WHERE Id = ?",(id,))
                    conn.commit()
                    QMessageBox.about(self, "Delete Assignment", "The Delete Process is Successful")
                    self.Load_Database()
                 except Exception as error :
                    QMessageBox.about(self, "Delete Assignment Error", "Please Try Again")

class UpdateAssignment(QtWidgets.QMainWindow,Ui_AdminAssEdit):
    def __init__(self,parent=None):
        super(UpdateAssignment,self).__init__(parent)
        self.setupUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainApp()
    w.show()
    sys.exit(app.exec_())
