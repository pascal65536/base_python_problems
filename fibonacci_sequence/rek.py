"""
Рекусивная программа поиска минимального элемента последовательности
"""

ls = [10, 2, 3, 4, 5, 6, 7, 4, 5, 7, 8, 5, 7, 9, 9]


def find_max(spisok):
    if not spisok:
        return None
    if len(spisok) == 1:
        return spisok[0]
    first = spisok[0]
    max_rest = find_max(spisok[1:])
    if first > max_rest:
        return first
    return max_rest


print(find_max(ls))
