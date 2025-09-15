phonebook_lst = [
    {
        "name": "Александр Пушкин",
        "phone": "89992233456",
        "address": "ул. Ленина, д. 1, кв 12",
    },
    {
        "name": "Александр Блок",
        "phone": "8 (999) 224-56-22",
        "address": "ул. Мира, д. 2, кв 23",
    },
    {
        "name": "Иван Бунин",
        "phone": "8-999-224-52-23",
        "address": "ул. Советская, д. 12, кв 3",
    },
]


while True:
    print("-" * 10)
    print("1 - Просмотр всего справочника")
    print("2 - Поиск по имени")
    print("3 - Поиск по телефону")
    print("4 - Поиск по адресу")
    print("0 - Выход")
    key = input("Введите пункт меню: ")
    if key == "0":
        break
    elif key == "1":
        for phonebook in phonebook_lst[:10]:
            print(phonebook["name"], phonebook["phone"], phonebook["address"])
    elif key == "2":
        search = input("Введите часть имени: ")
        result_lst = list()
        for phonebook in phonebook_lst:
            if search in phonebook["name"]:
                result_lst.append(phonebook)
        for phonebook in result_lst[:10]:
            print(phonebook["name"], phonebook["phone"], phonebook["address"])
    elif key == "3":
        pass
    elif key == "4":
        pass
