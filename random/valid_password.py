"""
Пароль считается правильным, если он длиной >= 8 символов и содержит
большие и маленькие буквы латинского алфавита, цифры и служебные символы
Проверить пароль на правильность
"""

alpha = "abcdefghijklmnopqrstuvwxyz"
ALPHABET = set(alpha.upper())
alphabet = set(alpha.lower())
number = set("0123456789")
special = set('!@#$%^&*()_-=+?><"][`/\\') | set("'~{}")

while True:
    flag = True
    password_str = input("Введите пароль: ")
    password = set(password_str)
    if len(password_str) < 8:
        print("8")
        flag = False
    if password & number == set():
        print("number")
        flag = False
    if password & special == set():
        print("special")
        flag = False
    if password & alphabet == set():
        print("alphabet")
        flag = False
    if password & ALPHABET == set():
        print("ALPHABET")
        flag = False
    if flag == True:
        break

print(f"Правильный пароль - {password_str}")
