import lecture
import student 


l201 = lecture.Lecture("201")
l202 = lecture.Lecture("202")
lectures = [l201, l202]

lectures[0].addStudent(student.Student("ebv", 99))


for s in l201.get_student_list():
    print(s.get_name_grade())