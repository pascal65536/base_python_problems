"""
Этот код представляет игру "Города". Программа запрашивает у пользователя 
название города, начинающегося на определенную букву (начинается с буквы "н" 
в данном случае), и проверяет его на соответствие допустимым символам 
из списка "good_char". Если город начинается на правильную букву 
и еще не был использован ранее, он добавляется в список "city_lst", 
а начальная буква для следующего города изменяется на последнюю букву 
предыдущего города. Если же город не соответствует правилам игры, 
программа выводит сообщение об ошибке. Игра продолжается до тех пор, 
пока пользователь не введет пустую строку или неверный город.
"""

good_char = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя- "
bad_char = "ъьйёы"
city_lst = []
char_start = "н"

while True:
    welcome = f"Введите название города, вам на {char_start}:"
    city = input(welcome)
    city = city.strip()
    i = 0
    flag = True
    while i < len(city):
        if city[i].lower() not in good_char:
            flag = False
            break
        i += 1

    if len(city) == 0 and not flag:
        print("Конец игры")
        break

    elif char_start.lower() == city[0].lower() and city not in city_lst:
        if city[-1] in bad_char:
            char_start = city[-2]
        else:
            char_start = city[-1]
        city_lst.append(city)
    else:
        print("Ошибка")
