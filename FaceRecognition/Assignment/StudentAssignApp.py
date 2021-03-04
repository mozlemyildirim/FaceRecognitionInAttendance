from StudentAssignment import Ui_Student_Assignmet
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWidgets import QApplication,QDialog,QMainWindow,QMessageBox,QTableWidgetItem
from datetime import date
import datetime
import sqlite3
import asd
conn = sqlite3.connect('Students.db')
curs = conn.cursor()
class MainApp(QtWidgets.QMainWindow,Ui_Student_Assignmet):
    def __init__(self,parent=None):
        super(MainApp,self).__init__(parent)
        self.setupUi(self)
        self.Load_Database()
        self.btn_Assignment.clicked.connect(self.Show_TakeAssignment)
        self.Init_Ui()
    def Init_Ui(self):
        self.show()
    def Show_TakeAssignment(self):
        asd.TakeAssginmentWithFace()
      

    def Load_Database(self):
      today = str(date.today())
      print(today)
      now = datetime.datetime.now()
      print(now.hour)
      content = curs.execute('''
      SELECT S.StudentId,S.Name,S.Surname,C.Name,A.Date,A.IsCame 
      FROM Student AS S INNER JOIN StudentCourse AS SC ON SC.StudentId = S.Id 
      INNER JOIN Assignment AS A ON A.StudentCourseId = SC.Id 
      INNER JOIN Course AS C ON C.Id = SC.CourseId 
      WHERE A.Date = ? AND ? BETWEEN C.StartHour AND (c.EndHour-1)
      ''',(today,now.hour))
      for row_index,row_data in enumerate(content):
           self.tableWidget.insertRow(row_index)
           for colm_index,colm_data in enumerate(row_data):
               self.tableWidget.setItem(row_index,colm_index,QTableWidgetItem(str(colm_data)))









import sys
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainApp()
    w.show()
    sys.exit(app.exec_())