word = 'Я пишу программу на Python'
print(word[2::3])


n = 20
m = 25
prod = n * m
print(f'Произведение {n} на {m} равно {prod}')  # Вывод: Произведение 20 на 25 равно 500
print('Произведение', n, 'на', m, 'равно', prod)  # Вывод: Произведение 20 на 25 равно 500


# user = input()
# print(f'Hello {user}!')

num = 65536
print(f'Result {num}')

pi = 3.1415926
print(f'Result {pi}')




print(f'Division {22/7}')



var = 'Пример'
print(f'Одинарные кавычки {var}!')
print(f"Двойные кавычки {var}!")
print(f'''Тройные кавычки {var}!''')


pi = 3.1415926
print(f'Result {pi:.2f}')  # Вывод: Result 3.14
print(f'Result {pi:.4f}')  # Вывод: Result 3.1416

print(f'Result {pi:5.2f}')  # Вывод: Result  3.14
print(f'Result {pi:5.3f}')  # Вывод: Result 3.142
print(f'Result {pi:5.4f}')  # Вывод: Result 3.1416

print(f'Result {pi:10.2f}')  # Вывод: Result       3.14
print(f'Result {pi:10.3f}')  # Вывод: Result      3.142
print(f'Result {pi:10.4f}')  # Вывод: Result     3.1416




integer = -1234567890
print(f"Число с разделителем разрядов: {integer:,}")  # Вывод: Число с разделителем разрядов: -1,234,567,890
sep = "_"
print(f"Число с пользовательским разделителем разрядов: {integer:{sep}}")  # Вывод: Число с пользовательским разделителем разрядов: -1_234_567_890

text = "Python"
print(f"|{text:<10}|")
print(f"|{text:>10}|")
print(f"|{text:^10}|")

val = 1/7.0
print(f'{val}')  # Вывод: 0.14285714285714285
print(f'{val:.2%}')  # Вывод: 14.29%



num = 1_200_400_001
print(num)  # Вывод: 1200400001
print(f'{num:_}')  # Вывод: 1_200_400_001
print(f'{num:,}')  # Вывод: 1,200,400,001

x = 1
print(f'{x:02} {x*x:3} {x*x*x:4}')  # Вывод: 01 1 1
x = 5
print(f'{x:02} {x*x:3} {x*x*x:4}')  # Вывод: 05 25 125
x = 10
print(f'{x:02} {x*x:3} {x*x*x:4}')  # Вывод: 10 100 1000
x = 15
print(f'{x:02} {x*x:3} {x*x*x:4}')  # Вывод: 15 225 3375


a = "Hello"
print('|', a.center(10), '|')   # Вывод: |   Hello    |
print(a.rjust(14))              # Вывод:          Hello
print(a.ljust(10))              # Вывод: Hello
print(a.ljust(14, '.'))         # Вывод: Hello.........
print(a.center(14, '.'))        # Вывод: ....Hello.....


y = 1
print(f'{y:05}')  # Вывод: 00001
y = 20
print(f'{y:05}')  # Вывод: 00020
y = 300
print(f'{y:05}')  # Вывод: 00300

y = 300
print(f'{y:.>15}')  # Вывод: ............300
print(f'{y:.<15}')  # Вывод: 300............
print(f'{y:.^15}')  # Вывод: ......300......

val = 300

# hexadecimal lower
print(f'{val:x}')   # Вывод: 12c

# hexadecimal upper
print(f'{val:X}')   # Вывод: 12C

# octal
print(f'{val:o}')   # Вывод: 374

# binary
print(f'{val:b}')   # Вывод: 1100100

# scientific
print(f'{val:e}')   # Вывод: 3.000000e+02