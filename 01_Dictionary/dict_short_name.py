# Дан словарь перевода уменьшительных имён в полные имена
# Спросить у пользователя, как его зовут и обратиться по полному имени
# Если такого короткого имени в словаре нет, то обращаться так, как
# человек представился
# использовать функцию get()

short_name_dct = {
    "Ромка": "Роман",
    "Вася": "Василий",
    "Маша": "Мария",
    "Санечка": "Александр",
}

username = input("Как тебя зовут? ")

full_name = short_name_dct.get(username)
print(f"Привет, {full_name}")

full_name = username
if username in short_name_dct:
    full_name = short_name_dct[username]
    
print(f"Привет, {full_name}")
