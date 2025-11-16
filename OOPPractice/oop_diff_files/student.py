class Student:
    def __init__(self, name, grade):
        self._name = name
        self._grade = grade

    def get_name_grade(self):
        return self._name, self._grade
    