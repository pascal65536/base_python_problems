def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

# Пример использования
print("Являются ли 'listen' и 'silent' анаграммами:")
print(are_anagrams("listen", "silent"))
# Вывод: True


numbers  = [1, 3, 3, 4, 54, 56, 7, 7, 8, 9]
sum_of_squares = sum([n * n for n in numbers])
print("Сумма чисел:", sum_of_squares)  # Вывод: 6360


is_even = lambda num: num % 2 == 0
print(f'{is_even(8)=}')

numbers = [3, 5, 2, 8, 1]
find_max = max(numbers)
print("Максимальный элемент:", find_max)  # Вывод: 8


numbers = [10, 20, 4, 45, 99]
second_max = sorted(numbers, reverse=True)[1]
print("Второй максимальный элемент:", second_max)  # Вывод: 45



numbers = [10, 20, 30, 40, 50]
linear_search = numbers.index(30)
print("Индекс элемента 30:", linear_search)  # Вывод: 2




