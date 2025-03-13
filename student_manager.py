from student import Student


class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, name, grade):
        student = Student(name, grade)
        self.students.append(student) #добавляю студента в общий список студентов

    def get_average_grade(self):
        if not self.students:
            return 0
        total = sum(student.grade for student in self.students)
        return total / len(self.students)

    def print_students(self):
        for student in self.students:
            print(student)
