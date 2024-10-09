def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

# Пример использования
print("Сумма цифр числа 65536:", sum_of_digits(65536))  # Вывод: 25
