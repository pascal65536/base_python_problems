def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Пример использования
print("Факториал 5:", factorial(5))  # Вывод: 120
