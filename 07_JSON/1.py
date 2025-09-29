# Пользователь вводит название JSON файла. Вывести его на печать

import json

filename = input()

with open(filename, 'r', encoding='utf-8') as file:
    data = json.load(file)
   
print(data)
