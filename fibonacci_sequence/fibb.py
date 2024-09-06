"""
Этот код генерирует числа Фибоначчи до тех пор, пока не достигнет числа больше или 
равного 1000. Первый блок кода использует цикл while и переменные a и b для генерации 
чисел Фибоначчи. Второй блок кода использует функцию fib, которая возвращает 
сумму двух последних элементов списка fibb_lst, чтобы генерировать числа Фибоначчи 
и добавлять их в список, пока не достигнет числа больше или равного 1000. 
Каждое новое число Фибоначчи и список, содержащий все сгенерированные числа, 
выводятся на экран.
"""

def fib(fibb_lst):
    return fibb_lst[-1] + fibb_lst[-2]


if __name__ == "__main__":
    fibb_lst = [0, 1]

    i = fib(fibb_lst)
    while i < 1000:
        fibb_lst.append(i)
        i = fib(fibb_lst)
    print(fibb_lst)
