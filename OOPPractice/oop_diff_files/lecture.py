import student

class Lecture:
    def __init__(self, code):
        self._code = code
        self._students = []
        self.addStudent(student.Student("tamer", 6.00))

    def addStudent(self, s: student.Student):
        self._students.append(s)
    
    def get_student_list(self):
        return self._students


