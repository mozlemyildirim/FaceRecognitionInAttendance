import sqlite3
from datetime import date
from datetime import datetime
import datetime as dt
import itertools # for now lesson
from dbAssignment import InsertAssignment
# from recognizer import faceRecognizer
import asd
import time

conn = sqlite3.connect('Students.db')
from classAssignment import Assignment
c=conn.cursor()

def TodaysLessonStudents():
    with conn:
        Today=date.today().strftime('%A')
        # Today = 'Monday'
        print(Today)
        c.execute("""
        SELECT SC.Id
        FROM Course AS C
        
        INNER JOIN StudentCourse AS SC ON SC.CourseId = C.Id
        INNER JOIN Student AS S ON SC.StudentId = S.Id

        WHERE C.Day=?

        GROUP BY SC.Id

        """,(Today,))
        items = []
        for item in c:
            items.append(item)
        newList = list(itertools.chain.from_iterable(items))
        return newList



def takeAllForToday():
    nowStudentCourseList = TodaysLessonStudents()
    print(nowStudentCourseList)
    for StudentCourseNumbers in nowStudentCourseList:
        print(StudentCourseNumbers)
        if StudentCourseNumbers is not None:
            temp = Assignment(1,datetime.today().strftime('%Y-%m-%d'),StudentCourseNumbers,'0')
            InsertAssignment(temp)

def lastinsert():
    with conn:
        c.execute("""SELECT Date FROM Assignment""")
        lastDate = ''
        for item in c:
            lastDate = item
        lastDate = (''.join(lastDate))
        return lastDate

def alwaysRunning():
        lastDate = lastinsert()
        if datetime.today().strftime('%Y-%m-%d') != lastDate:
            print('Assignments have taken for today.')
            takeAllForToday()
        # time.sleep(3)
        print('Assignment already done.')
