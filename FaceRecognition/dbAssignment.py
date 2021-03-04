from classAssignment import Assignment
import sqlite3
import itertools 


conn = sqlite3.connect('Students.db')

c=conn.cursor()

def InsertAssignment(Assignment):
    with conn:
        c.execute('INSERT INTO Assignment ([Date],StudentCourseId,IsCame) VALUES(?,?,?)',(Assignment.Date,Assignment.StudentCourseId,Assignment.IsCame))

def UpdateAssignment(Assignment):
        with conn:
            c.execute("""UPDATE Assignment SET [Date] = ? , StudentCourseId = ? , IsCame = ? WHERE Id = ? """,(Assignment.Date, Assignment.StudentCourseId, Assignment.IsCame, Assignment.Id,))

def UpdateAssignmentWithStudentCourseId(Assignment):
        print(Assignment.IsCame)
        with conn:
            c.execute("""UPDATE Assignment SET IsCame = ? WHERE StudentCourseId = ? AND [Date] = ?""",('1', Assignment.StudentCourseId,Assignment.Date,))

