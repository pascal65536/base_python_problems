def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Пример использования
print("НОД(48, 18):", gcd(48, 18))  # Вывод: 6
