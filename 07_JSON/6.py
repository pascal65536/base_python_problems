'''
Написать программу на Python, которая открывает JSON-файл с данными класса, 
где у каждого ученика есть имя, фамилия и список оценок по учебным предметам. 
Пользователь вводит имя файла, затем через запятую список учебных предметов 
(этот список соответствует порядку оценок в упомянутом списке).
Далее пользователь вводит название предмета. Программа должна вывести 
в алфавитном порядке по имени всех учеников, у которых оценка по выбранному 
предмету тройка и ниже.
'''

import json

filename = input()
subjects_input = input()
subjects = list()
for subject in subjects_input.split(","):
    subjects.append(subject.strip())
subject_to_check = input().strip()

with open(filename, 'r', encoding='utf-8') as file:
    data = json.load(file)

students = data.get("class", [])

subject_index = subjects.index(subject_to_check)
filtered_students = list()
for student in students:
    grade = student['grade'][subject_index]
    if grade <= 3:
        filtered_students.append(f'{student["surname"]} {student["name"]}')

filtered_students.sort()

if filtered_students:
    for stu in filtered_students:
        print(stu)
