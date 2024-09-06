"""
Этот код генерирует 10 случайных имен, каждое из которых состоит 
из трех согласных и трех гласных букв. Гласные и согласные выбираются случайно 
из соответствующих строк "vowel" и "consonant". Каждое сгенерированное имя выводится 
на экран с заглавной буквы.
"""

import random

vowel = "aeiouy"  # гласные
consonant = "bcdfghjklmnpqrstvwxz"  # согласные
i = 0
while i < 10:
    name = ""
    j = 0
    while j < 3:
        name += random.choice(consonant)
        name += random.choice(vowel)
        j += 1
    print(name.capitalize())
    i += 1
