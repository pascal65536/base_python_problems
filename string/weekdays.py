"""
Данный код создает список weekdays_lst, содержащий названия дней недели. Затем он объединяет части слов "Суббота" и "Понедельник", чтобы получить новое слово "ботельник". Наконец, он выводит это новое слово на экран.
"""

weekdays_lst = [
    "Понедельник",
    "Вторник",
    "Среда",
    "Четверг",
    "Пятница",
    "Суббота",
    "Воскресенье",
]
new_word = f"{weekdays_lst[5][3:]}{weekdays_lst[0][-3:]}"
print(new_word)
