class Course:
    def __init__(self, title, instructor):
        self.title = title
        self.instructor = instructor
        self.students = []

    def add_student(self, student):
        if student in self.students:
            print(f'Студент "{student}" уже есть в списке.')        
        self.students.append(student)

    def remove_student(self, student):
        if student not in self.students:
            print(f'Нет студента "{student}" в списке!')
        if student in self.students:
            self.students.remove(student)

    def get_student_list(self):
        return self.students

course = Course("Python для начинающих", "Мария")
course.add_student("Иван")
course.add_student("Иван")
course.add_student("Анна")
print(course.get_student_list())
course.remove_student("Иван")
print(course.get_student_list())