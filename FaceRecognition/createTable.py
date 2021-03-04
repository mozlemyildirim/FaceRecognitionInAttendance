import sqlite3

def createTable(sqlString):
    print(sqlite3.version)
    connection = sqlite3.connect('Students.db')
    if connection:
        print('succes!')
    else:
        print('error!')
    database= connection.cursor()
    database.execute(sqlString)


sqlStringStudent = """CREATE TABLE Student(
        Id integer PRIMARY KEY, 
        StudentId text NOT NULL UNIQUE,
        TC text NOT NULL,
        Name text NOT NULL,
        Surname text NOT NULL,
        FatherName text NOT NULL,
        BirthDate date NOT NULL,
        BirthPlace text NOT NULL
        );"""

sqlStringAssignment = """CREATE TABLE Assignment(
        Id integer PRIMARY KEY, 
        Date date NOT NULL,
        StudentCourseId int NOT NULL,
        IsCame text NOT NULL
        );"""

sqlStringStudentCourse = """CREATE TABLE StudentCourse(
        Id integer PRIMARY KEY, 
        CourseId int NOT NULL,
        StudentId int NOT NULL
        );"""


sqlStringCourse = """CREATE TABLE Course(
        Id integer PRIMARY KEY, 
        Name text NOT NULL,
        Day text NOT NULL,
        StartHour int NOT NULL,
        EndHour int NOT NULL,
        DepartmentId int NOT NULL
        );"""

sqlStringDepartment = """CREATE TABLE Department(
        Id integer PRIMARY KEY, 
        Name text NOT NULL
        );"""

sqlStringUser = """ CREATE TABLE Users(
        Id integer PRIMARY KEY, 
        username text NOT NULL,
        password text NOT NULL
        );
"""

sqlStringAddUser = """ INSERT INTO Users(username,password) VALUES('admin','1234');

"""



createTable(sqlStringStudent)
createTable(sqlStringAssignment)
createTable(sqlStringStudentCourse)
createTable(sqlStringCourse)
createTable(sqlStringDepartment)
createTable(sqlStringUser)
createTable(sqlStringAddUser)

