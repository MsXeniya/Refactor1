from student_manager import StudentManager

manager = StudentManager()

manager.add_student("Аня", 85)
manager.add_student("Борис", 90)

manager.print_students()

print("Средний балл:", manager.get_average_grade())

