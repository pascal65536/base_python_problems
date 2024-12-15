a = 'py.'
print(a * 4)  # Вывод py.py.py.py.
print(4 * a)  # Вывод py.py.py.py.


print(a * -4)  # Вывод пустая строка



s = 'Python'
print(s in 'I like Python.')  # Вывод True
print(s in 'I like Java.')  # Вывод False


print('z' in 'abc')  # Вывод False
print('z' not in 'abc')  # Вывод True


word = 'Python'
print(len(word))  # Вывод 6


num = 100
print(str(num))  # Вывод '100'
print(str(str))  # Вывод <class 'str'>


alphabet = 'abcdefghijklmnopqrstuvwxyz'
print(alphabet[0])  # Вывод 'a'
print(alphabet[-1])  # Вывод 'z'


print(min(a, s, word))


word = 'Скоро Новый год'
word = word.lower()
word = word.replace('о', '0')
word = word.replace('ы', 'b1')
word = word.replace('р', 'p')
word = word.replace('к', '1<')
print(word)
