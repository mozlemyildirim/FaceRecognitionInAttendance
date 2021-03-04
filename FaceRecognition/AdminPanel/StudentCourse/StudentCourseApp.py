from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QDialog,QMainWindow,QMessageBox,QTableWidgetItem
from StudentCourse import Ui_AdminStuCourse
from UpdateStudentCourse import Ui_AdminStuCourseUpdate
from AddStudentCourse import Ui_AdminStuCourseAdd
import sqlite3

conn = sqlite3.connect('Students.db')
curs = conn.cursor()

class MainApp(QtWidgets.QMainWindow,Ui_AdminStuCourse):
    def __init__(self,parent=None):
        super(MainApp,self).__init__(parent)
        self.setupUi(self)
        self.btn_add.clicked.connect(self.Show_AddStudentCourse)
        self.btn_Edit.clicked.connect(self.Show_UpdateStudentCourse)
        self.btn_Delete.clicked.connect(self.Delete_Data)
        #self.btn_Show.clicked.connect(self.Load_Database)
        #self.Load_Database()
        self.Init_Ui()
    def Init_Ui(self):
        self.show()
        content = 'SELECT * FROM Department'
        res = curs.execute(content)
        self.dept_Combo.addItem("Select")
        for row in enumerate(res):
            data = row[1]
            name = data[1]
            id  = data[0]
            self.dept_Combo.addItem(name)  
        self.dept_Combo.currentIndexChanged.connect(self.Load_Database)
            

    def Load_Database(self):
        while self.tableWidget.rowCount() > 0 :
            self.tableWidget.removeRow(0)
        name = self.dept_Combo.currentText()
        res = curs.execute("SELECT * FROM Department WHERE Name = ?",(name,))
        for row in enumerate(res):
            data = row[1]
            id = data[0]
        dept_id = id
        content = curs.execute("SELECT C.Name,S.StudentId,S.Name FROM Course AS C INNER JOIN StudentCourse AS SC ON SC.CourseId = C.Id INNER JOIN Department AS D ON D.Id = C.DepartmentId INNER JOIN Student AS S ON S.Id = SC.StudentId WHERE C.DepartmentId = ? ORDER BY SC.Id",(dept_id,))
        for row_index,row_data in enumerate(content):
            self.tableWidget.insertRow(row_index)
            for colm_index,colm_data in enumerate(row_data):
                self.tableWidget.setItem(row_index,colm_index,QTableWidgetItem(str(colm_data)))


    
    def Show_AddStudentCourse(self):
        self.adding = AddStudentCourse()
        self.adding.btn_Add.clicked.connect(self.Add_Data)
        self.adding.courseCombo.addItem("Select")
        name = self.dept_Combo.currentText()
        res = curs.execute("SELECT * FROM Department WHERE Name = ? ",(name,))
        for row in enumerate(res):
                data = row[1]
                id = data[0]
        res2 = curs.execute("SELECT * FROM Course WHERE DepartmentId = ?",(id,))
        for row in enumerate(res2):
            data = row[1]
            course_name = data[1]
            #id = data[0]
            self.adding.courseCombo.addItem(course_name)
        self.adding.studentCombo.addItem("Select") 
        res3 = curs.execute("SELECT * FROM Student")
        for row in enumerate(res3):
            data = row[1]
            stu_id = data[0]
            stu_name = data[3]
            stu_surname = data[4]
            self.adding.studentCombo.addItem(stu_name+"-"+stu_surname)
        self.adding.show()

    def Add_Data(self):
        name = self.adding.courseCombo.currentText()
        res = curs.execute("SELECT * FROM Course WHERE Name = ? ",(name,))
        for row in enumerate(res):
                data = row[1]
                id = data[0]

        stu_name = self.adding.studentCombo.currentText()
        name2,surname = stu_name.split("-")
        res2 = curs.execute("SELECT * FROM Student Where Name = ?",(name2,))
        for row in enumerate(res2):
            data = row[1]
            stu_id = data[0]
        try: 
            curs.execute("INSERT INTO StudentCourse(CourseId,StudentId) VALUES(?,?)",(id,stu_id))
            conn.commit()
            QMessageBox.about(self, "Add Student Course", "The Adding Process is Successful ")
            self.adding.hide()
            self.Load_Database()
        except Exception as error :
            QMessageBox.about(self, "Add StudentCourse Error", "Please Try Again.")
    def Show_UpdateStudentCourse(self):
        self.adding = UpdateStudentCourse()
        self.adding.btn_Update.clicked.connect(self.Update_Data)
        name = self.dept_Combo.currentText()
        res = curs.execute("SELECT * FROM Department WHERE Name = ? ",(name,))
        for row in enumerate(res):
                data = row[1]
                dept_id = data[0]
        res2 = curs.execute("SELECT * FROM Course WHERE DepartmentId = ?",(dept_id,))
        for row in enumerate(res2):
            data = row[1]
            course_name = data[1]
            #id = data[0]
            self.adding.courseCombo.addItem(course_name)
        res3 = curs.execute("SELECT DISTINCT S.Name,S.Surname FROM Course AS C INNER JOIN StudentCourse AS SC ON SC.CourseId = C.Id INNER JOIN Student AS S ON S.Id = SC.StudentId INNER JOIN Department AS D ON D.Id = C.DepartmentId WHERE C.DepartmentId = ?",(dept_id,))
        for row in enumerate(res3):
            data = row[1]
            stu_name = data[0]
            stu_surname = data[1]
            self.adding.studentCombo.addItem(stu_name+"-"+stu_surname)
        self.adding.show()

    def Update_Data(self):
        name = self.dept_Combo.currentText()
        course_name =self.adding.courseCombo.currentText()
        content = curs.execute("SELECT * FROM Course WHERE Name = ?",(course_name,))
        for row in enumerate(content):
            data = row[1]
            cs_id = data[0]
        res = curs.execute("SELECT * FROM Department WHERE Name = ? ",(name,))
        for row in enumerate(res):
                data = row[1]
                dept_id = data[0]
        res2 = curs.execute("SELECT SC.Id,C.Id,S.Id FROM Student AS S INNER JOIN StudentCourse AS SC ON SC.StudentId = S.Id INNER JOIN Course AS C ON C.Id = SC.CourseId INNER JOIN Department AS D ON D.Id = C.DepartmentId WHERE C.DepartmentId = ?",(dept_id,))
        for row in enumerate(res2):
            if row[0] == self.tableWidget.currentRow():
                data = row[1]
                sc_id = data[0]
                c_id = data[1]
                stu_name = self.adding.studentCombo.currentText()
                name2,surname = stu_name.split("-")
                res3 = curs.execute("SELECT * FROM Student WHERE Name = ?",(name2,))
                for row in enumerate(res3):
                    data = row[1]
                    stu_id = data[0]
                    try : 
                        curs.execute("""UPDATE StudentCourse SET CourseId = ?,StudentId = ? WHERE Id = ? """,(cs_id,stu_id,sc_id))
                        conn.commit()
                        QMessageBox.about(self, "Update Student Course", "The Update Process is Successful ")
                        self.adding.hide()
                        self.Load_Database()
                    except Exception as error :
                        QMessageBox.about(self, "Update Student Course Error", "Please Try Again. ")


                        
                

    def Delete_Data(self):
        name = self.dept_Combo.currentText()
        res = curs.execute("SELECT * FROM Department WHERE Name = ?",(name,))
        for row in enumerate(res):
            data = row[1]
            id = data[0]
        content = curs.execute("SELECT SC.Id,C.Id,S.Id FROM Student AS S INNER JOIN StudentCourse AS SC ON SC.StudentId = S.Id INNER JOIN Course AS C ON C.Id = SC.CourseId INNER JOIN Department AS D ON D.Id = C.DepartmentId WHERE C.DepartmentId = ? ORDER BY SC.Id ASC ",(id,))
        for row in enumerate(content):
            if row[0] == self.tableWidget.currentRow():
                data = row[1]
                sc_id = data[0]
                curs.execute("DELETE FROM StudentCourse WHERE Id =?",(sc_id,))
                conn.commit()
                self.Load_Database()
                try :
                    QMessageBox.about(self, "Delete Student Course", "The Delete Process is Successful ")
                except Exception as error :
                    QMessageBox.about(self, "Delete Student Course", "Please Try Again.")

class AddStudentCourse(QtWidgets.QMainWindow, Ui_AdminStuCourseAdd):
    def __init__(self,parent=None):
        super(AddStudentCourse,self).__init__(parent)
        self.setupUi(self)

class UpdateStudentCourse(QtWidgets.QMainWindow,Ui_AdminStuCourseUpdate):
    def __init__(self,parent=None):
        super(UpdateStudentCourse,self).__init__(parent)
        self.setupUi(self)    
       
        
       
      
        

           

        


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainApp()
    w.show()
    sys.exit(app.exec_())
