def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_fib = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(next_fib)
    return fib_sequence[:n]

# Пример использования
print("Первые 10 чисел Фибоначчи:", fibonacci(10))  # Вывод: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
