from faker import Faker
import random
import json

fake = Faker("ru_RU")

students = []

for _ in range(100):
    gender = random.choice(['male', 'female'])
    if gender == 'male':
        name = fake.first_name_male()
        surname = fake.last_name_male()
    else:
        name = fake.first_name_female()
        surname = fake.last_name_female()

    grades = [random.randint(2, 5) for _ in range(5)]
    student = {
        "name": name,
        "surname": surname,
        "grade": grades
    }
    students.append(student)

data = {"class": students}

with open("class_100_gender_consistent.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
