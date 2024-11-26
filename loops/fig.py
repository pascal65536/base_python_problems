def yolochka(n):
  """Выводит елочку из символов "*" высотой n."""
  for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

def treugolnik(n):
  """Выводит треугольник из символов "*" высотой n."""
  for i in range(1, n + 1):
    print("*" * i)

def romb(n):
  """Выводит ромб из символов "*" высотой n."""
  for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
  for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))

def kvadrat(n):
  """Выводит квадрат из символов "*" размером n x n."""
  for i in range(n):
    print("*" * n)

# Получаем число N от пользователя
n = int(input("Введите число N: "))

# Выбор фигуры
figura = input("Выберите фигуру (ёлочка, треугольник, ромб, квадрат): ")

if figura == "ёлочка":
  yolochka(n)
elif figura == "треугольник":
  treugolnik(n)
elif figura == "ромб":
  romb(n)
elif figura == "квадрат":
  kvadrat(n)
else:
  print("Неверный выбор фигуры.") 
