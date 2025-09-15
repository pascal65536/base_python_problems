import random

s1 = random.randint(1, 100)
s2 = random.randint(1, 100)
summa = s1 + s2

res = input("Сколько будет " + str(s1) + "+" + str(s2) + "? ")

if not res.isdigit():
    print("Надо ввести ответ цифрами")
elif int(res) == summa:
    print("Правильно!")
else:
    print("Не правильно ((")
