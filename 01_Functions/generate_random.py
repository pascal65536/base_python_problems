'''
Напишите программу, которая выполняет генерацию списка случайных целых чисел в заданном количестве.
Требования к программе:
Создайте функцию с именем generate, которая принимает один необязательный параметр count — количество генерируемых чисел. 
По умолчанию count равно 10.
Функция должна возвращать список из count случайных целых чисел в диапазоне от 0 до 100 включительно.
'''

import random


def generate(count=10):
    i = 0
    random_lst = list()
    while i < count:
        random_lst.append(random.randint(0, 100))
        i += 1
    return random_lst


ret = generate()
print(ret)
ret = generate(20)
print(ret)
