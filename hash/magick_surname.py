"""
Пользователь вводит фамилию
Волшебная фамилия та, у которой все буквы уникальные

Этот код запрашивает у пользователя ввод фамилии, затем приводит ее к нижнему регистру. 
Далее он проверяет, есть ли в фамилии повторяющиеся буквы, используя функцию set(), 
которая удаляет все дубликаты из строки. Если длина множества уникальных букв равна 
длине исходной строки, то программа выводит сообщение "Ваша фамилия магическая!", 
в противном случае выводится сообщение "Ваша фамилия простая". 
Таким образом, программа определяет, является ли фамилия уникальной 
по своей структуре или нет.
"""

surname = input("Введи фамилию: ")
surname = surname.lower()
if len(set(surname)) == len(surname):
    print("Ваша фамилия магическая!")
else:
    print("Ваша фамилия простая")
