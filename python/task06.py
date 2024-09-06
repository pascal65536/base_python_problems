"""
Совсем недавно Вася занялся программированием и решил реализовать собственную программу 
для игры в шахматы. Но у него возникла проблема определения правильности хода конем, 
который делает пользователь. Т.е. если пользователь вводит значение «C7-D5», 
то программа должна определить это как правильный ход, если же введено «E2-E4», 
то ход неверный. Также нужно проверить корректность записи ввода: если например, 
введено «D9-N5», то программа должна определить данную запись как ошибочную. 
Помогите ему осуществить эту проверку!

Входные данные

В единственной строке входного файла INPUT.TXT записан текст хода (непустая строка), 
который указал пользователь. Пользователь не может ввести строку, длиннее 5 символов.

Выходные данные

В выходной файл OUTPUT.TXT нужно вывести «YES», если указанный ход конем верный, 
если же запись корректна (в смысле правильности записи координат), но ход невозможен, 
то нужно вывести «NO». Если же координаты не определены или заданы некорректно, 
то вывести сообщение «ERROR».
"""


def check_move(move):
    transform = " ABCDEFGH"
    try:
        bb, ee = move.split('-')
        B1 = transform.index(bb[0])
        B2 = int(bb[1])
        E1 = transform.index(ee[0])
        E2 = int(ee[1])
        assert 1 <= B2 <= 8
        assert 1 <= E2 <= 8
        horse = [abs(B1 - E1), abs(B2 - E2)]
        h = f"{max(horse)}{min(horse)}"
        res = "NO"
        if h == "21":
            res = "YES"
    except Exception:
        res = "ERROR"
    return res


if __name__ == "__main__":
    # assert check_move("D9-C0") == "ERROR"
    # assert check_move("J7-C1") == "ERROR"
    # assert check_move("D8-C0") == "ERROR"
    # assert check_move("E2-E4") == "NO"
    # assert check_move("C3-C1") == "NO"
    # assert check_move("C3-E1") == "NO"
    # assert check_move("C3-B1") == "YES"
    # assert check_move("C3-D1") == "YES"
    # assert check_move("C3-A2") == "YES"
    # assert check_move("C3-E2") == "YES"
    # assert check_move("C3-A4") == "YES"
    # assert check_move("C3-E4") == "YES"
    # assert check_move("C3-B5") == "YES"
    # assert check_move("C3-D5") == "YES"
    # assert check_move("C7-D5") == "YES"

    with open("INPUT.TXT") as f:
        filestr = f.readline().strip()

    res = check_move(filestr)

    with open("OUTPUT.TXT", "w") as f:
        f.write(res)
