def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1  # Если элемент не найден

# Пример использования
numbers = [10, 20, 30, 40, 50]
print("Индекс элемента 30:", linear_search(numbers, 30))  # Вывод: 2
