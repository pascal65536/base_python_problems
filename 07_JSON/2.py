# Пользователь вводит название JSON файла. 
# Вывести на печать список его ключей отсортированных по алфавиту



import json

filename = input().strip()

with open(filename, 'r', encoding='utf-8') as file:
    data = json.load(file)
   
keys = sorted(list(data.keys()))


for k in keys:
    print(k)
