stuNumber = "b1610.033035"
x,y = stuNumber.split(".")
r,t = x.split("b")
print(t)
print(y)
print(r)
last = t+y
print(last)


ELECT A.Id,A.IsCame FROM Assignment AS A INNER JOIN StudentCourse AS SC ON SC.Id = A.StudentCourseId INNER JOIN Course AS C ON C.Id = SC.CourseId INNER JOIN Student AS S ON S.StudentId = SC.StudentId WHERE A.Date = '2019-05-18' AND C.Name = 'Visual' ORDER BY A.Id ASC