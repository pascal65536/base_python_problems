def caesar_decode(mystr):
    """
    Расшифровать
    """
    mystr = mystr.upper()
    return mystr


def caesar_code(mystr):
    """
    Зашифровать
    """
    mystr = mystr.lower()
    return mystr


while True:
    print("1 - Зашифровать")
    print("2 - Расшифровать")
    print("0 - Выход")
    inp = input("Введите 0, 1, 2: ")
    if inp == "0":
        break
    elif inp == "1":
        result = caesar_code(input("Введите строку: "))
        print(result)
    elif inp == "2":
        result = caesar_decode(input("Введите строку: "))
        print(result)
