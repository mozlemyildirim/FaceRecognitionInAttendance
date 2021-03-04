import sys
from PyQt5 import QtWidgets
from AdminMainWindow import Ui_AdminPanel
from PyQt5.QtWidgets import QApplication,QDialog,QMainWindow,QMessageBox,QTableWidgetItem
sys.path.insert(0,'AdminPanel/AdminAssignment/')
sys.path.insert(0,'AdminPanel/Department/')
sys.path.insert(0,'AdminPanel/Course/')
sys.path.insert(0,'AdminPanel/Student/')
sys.path.insert(0,'AdminPanel/StudentCourse/')
import DepartmentApp,AdminAssignApp,StudentCourseApp,CourseApp,StudentApp,captureMainApp

class MainApp(QtWidgets.QMainWindow,Ui_AdminPanel):
    def __init__(self,parent=None):
        super(MainApp,self).__init__(parent)
        self.setupUi(self)
        self.Init_Ui()
    def Init_Ui(self):
        self.show()
        self.btn_Assignment.clicked.connect(self.Show_Assignment)
        self.btn_Department.clicked.connect(self.Show_Department)
        self.btn_StudentCourse.clicked.connect(self.Show_StudentCourse)
        self.btn_Course.clicked.connect(self.Show_Course)
        self.btn_Student.clicked.connect(self.Show_Student)
        self.btn_Capture.clicked.connect(self.Show_Capture)
    
    def Show_Assignment(self):
         self.adding = AdminAssignApp.MainApp()
         self.adding.show()
    def Show_Department(self):
         self.adding = DepartmentApp.MainApp()
         self.adding.show()
    def Show_StudentCourse(self):
         self.adding = StudentCourseApp.MainApp()
         self.adding.show()
    def Show_Course(self):
         self.adding = CourseApp.MainApp()
         self.adding.show()
    def Show_Student(self):
         self.adding = StudentApp.MainApp()
         self.adding.show()
    def Show_Capture(self):
         self.adding = captureMainApp.MainApp()
         self.adding.show()
     