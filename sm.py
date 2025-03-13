students = []

def add_student(name, grade):
    students.append({"name": name, "grade": grade})

def get_average_grade():
    total = 0
    for student in students:
        total += student["grade"]
    return total / len(students) if students else 0

def print_students():
    for student in students:
        print(f"Студент: {student['name']}, Оценка: {student['grade']}")

add_student("Аня", 85)
add_student("Борис", 90)
print_students()
print("Средний балл:", get_average_grade())
