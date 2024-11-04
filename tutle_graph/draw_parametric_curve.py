import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

# Функция для создания параметрической кривой
def draw_parametric_curve():
    # Параметры кривой
    t = np.linspace(0, 2 * np.pi, 100)  # Параметр t от 0 до 2π
    x = np.sin(t)  # Координаты x
    y = np.cos(t)  # Координаты y

    # Создаем фигуру и оси
    fig, ax = plt.subplots()
    ax.plot(x, y, label='Параметрическая кривая')
    ax.set_title('Параметрическая кривая: x = sin(t), y = cos(t)')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.axhline(0, color='black',linewidth=0.5, ls='--')
    ax.axvline(0, color='black',linewidth=0.5, ls='--')
    ax.grid()
    ax.legend()

    return fig

# Основное окно приложения
root = tk.Tk()
root.title("Параметрическая кривая")

# Создание графика
fig = draw_parametric_curve()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Кнопка выхода
button_quit = tk.Button(root, text="Выход", command=root.quit)
button_quit.pack(side=tk.BOTTOM)

# Запуск главного цикла приложения
root.mainloop()
