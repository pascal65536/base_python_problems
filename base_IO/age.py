age = input("Ваш возраст: ")
age = int(age)
if age < 14:
    print("Вы слишком молоды")
elif age > 60:
    print("Вам лучше прогуляться возле дома. Хотя...")
    training = input("У вас есть соответствующая подготовка, напишите 1-если да и 0-если нет: ")
    training = int(training)
    if training == 1:
        print("Да, вы можете попробовать подняться на Эльбрус.")
    else:
        print("Все-таки вам лучше остаться дома.")
else:
    print("Да, можете попытаться покорить Эльбрус")
