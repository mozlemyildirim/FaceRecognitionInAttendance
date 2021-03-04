import sqlite3
from datetime import date
from datetime import datetime
import datetime as dt
import itertools # for now lesson
from dbAssignment import UpdateAssignmentWithStudentCourseId
from recognizer import recognizer


conn = sqlite3.connect('Students.db')
from classAssignment import Assignment
c=conn.cursor()

def NowLessonStudents():
    with conn:
        Today = date.today().strftime('%A')
        # Today = 'Monday'
        print(Today)
        HourNow = dt.datetime.today().hour
        # HourNow = 9
        print(HourNow)
        c.execute("""
        SELECT S.StudentId
        FROM Course AS C
        
        INNER JOIN StudentCourse AS SC ON SC.CourseId = C.Id
        INNER JOIN Student AS S ON SC.StudentId = S.Id

        WHERE C.Day=? AND ? BETWEEN C.StartHour AND (c.EndHour-1)

        GROUP BY S.StudentId

        """,(Today,HourNow,))
        items = []
        for item in c:
            items.append(item)
        newList = list(itertools.chain.from_iterable(items))
        return newList


def FindSCIDwithStudentNumber(StudentNumber):
    with conn:
        Today = date.today().strftime('%A')
        # Today = 'Monday'
        # print(Today)
        HourNow = dt.datetime.today().hour
        # HourNow = 9
        # print(HourNow)
        c.execute("""
        SELECT SC.Id
        FROM Course AS C
        
        INNER JOIN StudentCourse AS SC ON SC.CourseId = C.Id
        INNER JOIN Student AS S ON SC.StudentId = S.Id

        WHERE C.Day=? AND ? BETWEEN C.StartHour AND (c.EndHour-1) AND S.StudentId = ?

        GROUP BY SC.Id

        """,(Today,HourNow,StudentNumber,))
        items = []
        for item in c:
            items.append(item)
        newList = list(itertools.chain.from_iterable(items))
        return newList

# print(type(var[0]))
# print(''.join(var[0])) This erases the comas in tuple items

def ifexist():
    with conn:
        c.execute("""
        SELECT * FROM Assignment
        WHERE Date = ? AND StudentCourseId = ? AND
        """)

def TakeAssginmentWithFace():
        MyNumber = recognizer()
        print(MyNumber)
        nowStudentList = NowLessonStudents()
        print(nowStudentList)
        isOkay = 0
        for StudentNumbers in nowStudentList:
                if MyNumber == StudentNumbers:
                        SCID = FindSCIDwithStudentNumber(MyNumber)
                        print(SCID[0])
                        if SCID[0] is not None:
                                temp = Assignment(1,datetime.today().strftime('%Y-%m-%d'),SCID[0],'1')
                                UpdateAssignmentWithStudentCourseId(temp)
                                
                                print('Your assginment has taken')
                                isOkay = 1


        if isOkay == 1:
                print('Assignment Succeed!')
        else:
                print('Error!')
