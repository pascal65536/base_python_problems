"""
Данный код запрашивает у пользователя ввод пароля и проверяет его на соответствие требованиям безопасности. Пароль должен содержать не менее 8 символов, цифры, специальные символы и буквы как в нижнем, так и в верхнем регистре. Если пароль не соответствует этим требованиям, то программа запрашивает новый пароль до тех пор, пока не будет введен правильный пароль. После этого программа выводит сообщение с правильным паролем.
"""

alphabet = "abcdefghijklnmnopqrstuvwxyz"
number = "0123456789"
special = '!@#$%^&*()_-=+?><"][`/\\'
while True:
    flag = True
    password = input("Введи пароль: ")
    if len(password) < 8:
        flag = False
    if len(set(number)) == len(set(number) - set(password)):
        flag = False
    if len(set(special)) == len(set(special) - set(password)):
        flag = False
    if len(set(alphabet)) == len(set(alphabet) - set(password)):
        flag = False
    if len(set(alphabet.upper())) == len(set(alphabet.upper()) - set(password)):
        flag = False

    if flag:
        break

print(f"Самый правильный пароль: {password}")


alphabet = "abcdefghijklnmnopqrstuvwxyz"
number = "0123456789"
special = '!@#$%^&*()_-=+?><"][/\\'
while True:
    flag = True
    password = input("Введи пароль: ")
    if len(password) < 8:
        flag = False
    if not any(char.isdigit() for char in password):
        flag = False
    if not any(char in special for char in password):
        flag = False
    if not any(char.islower() for char in password):
        flag = False
    if not any(char.isupper() for char in password):
        flag = False

    if flag:
        break

print(f"Самый правильный пароль: {password}")
