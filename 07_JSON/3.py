# Пользователь вводит название JSON файла и название ключа верхнего уровня, 
# в качестве значений - список объектов. Каждый объект обязательно содержит ключ 
# "name". Нужно вывести на печать все значения по ключу "name" из списка.
# Не все объекты содержат ключ "name", их нужно игнорировать и ничего не печатать.



import json

filename = input().strip()
key = input().strip()

with open(filename, 'r', encoding='utf-8') as file:
    data = json.load(file)

items = data.get(key, [])

for dc in items:
    if 'name' in dc:
        print(dc['name'])

