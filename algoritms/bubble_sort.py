def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Пример использования
numbers = [65, 53, 36, 12, 22, 11, 90]
print("Отсортированный массив:", bubble_sort(numbers))
# Вывод: [11, 12, 22, 36, 53, 65, 90]
