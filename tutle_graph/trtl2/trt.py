import turtle

# Создание окна и черепашки
window = turtle.Screen()
t = turtle.Turtle()
t.hideturtle()

# Переменная для хранения цвета
colors = ["red", "green", "blue", "yellow", "purple", "orange"]
color_index = 0


# Функция обработки клика
def click_handler(x, y):
    global color_index
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.dot(10, colors[color_index])
    color_index = (color_index + 1) % len(colors)


# Назначение обработчика
window.onscreenclick(click_handler)

# Запуск основного цикла
turtle.done()
