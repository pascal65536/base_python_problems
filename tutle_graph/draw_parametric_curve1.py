import tkinter as tk
import math

# Функция для рисования параметрической кривой
def draw_parametric_curve(canvas):
    # Параметр t от 0 до 2π
    for t in range(0, 360):
        # Преобразуем градусы в радианы
        rad = t * (3.14159 / 180)  # π ≈ 3.14159
        # Уравнения для окружности: x = r * cos(t), y = r * sin(t)
        x = 150 + 100 * math.cos(rad)  # Центр (150, 150), радиус 100
        y = 150 + 100 * math.sin(rad)
        canvas.create_line(x, y, x+1, y+1, fill='black')  # Рисуем точку

# Основное окно приложения
root = tk.Tk()
root.title("Параметрическая кривая")

# Создание холста для рисования
canvas = tk.Canvas(root, width=300, height=300, bg='white')
canvas.pack()

# Рисуем кривую
draw_parametric_curve(canvas)

# Кнопка выхода
button_quit = tk.Button(root, text="Выход", command=root.quit)
button_quit.pack()

# Запуск главного цикла приложения
root.mainloop()
