class Student:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.grades = []
        
    def add_grade(self, grade: float) -> None:
        self.grades.append(grade)

    def get_average_grade(self) -> float:
        if not self.grades:
            return 0.0
        return round(sum(self.grades) / len(self.grades), 2)

student_elena = Student("Елена", 22)
student_elena.add_grade(5)
print(student_elena.get_average_grade())
