'''
Напишите программу, которая проверяет, является ли сегодняшний день Днём программиста, и выводит соответствующее сообщение.
Требования к программе:
Получите текущую дату и время с помощью модуля datetime.
Если сегодняшний месяц и день совпадают с "0913" (13 сентября), программа должна вывести на экран сообщение: "Happy Programmer's Day!".
В противном случае программа должна вывести сообщение: "Nothing interesting".
'''


import datetime

def happy():
    today = datetime.datetime.now()
    msg = "Nothing interesting"
    if today.strftime("%m%d") == "0913":
        msg = "Happy Programmer's Day!"
    return msg
