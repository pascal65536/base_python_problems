'''
Напишите программу на Python, которая откроет JSON-файл и прочитает 
из него список учеников класса. Для каждого ученика вычислить средний 
балл, округлить его до двух знаков после запятой и отобрать тех, 
у кого средний балл больше 4 и при этом отсутствуют оценки ниже двойки.
Итоговый список таких учеников вывести на экран, отсортировав по имени 
в алфавитном порядке, отображая средний балл с точностью до двух знаков 
после запятой.
'''

import json

filename = input()

with open(filename, 'r', encoding='utf-8') as file:
    data = json.load(file)

students = data.get("class", [])

qualified_students = []
for student in students:
    grades = student.get("grade", [])
    if grades and min(grades) > 1:
        avg = sum(grades) / len(grades)
        if avg >= 4:
            qualified_students.append((f'{student["surname"]} {student["name"]}', avg))

qualified_students.sort(key=lambda x: x[0])

for name, avg_grade in qualified_students:
    print(f"{name}: {avg_grade:.2f}")
