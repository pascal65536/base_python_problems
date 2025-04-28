from turtle import *

color = "pink"
size = 100
figure = 'circle'


def click_handler(x, y):
    global color, size
    print(x, y)
    if 400 < x < 430 and 370 < y < 400:
        color = "red"
        print('red')
        return
    if 400 < x < 430 and 320 < y < 350:
        color = "green"
        print('green')
        return
    if 400 < x < 430 and 270 < y < 300:
        color = "blue"
        print('blue')
        return
    if 0 < x <100 and 340 < y <360:
        size = x
        print('size')
        return    
    penup()
    goto(x, y)
    pendown()
    fillcolor(color)
    begin_fill()
    circle(size)
    end_fill()
    return

speed(2)
pensize(1)
penup()
pencolor("black")


# Палитра
x_coord = 400
y_coord = 400
for color in ["red", "green", "blue"]:
    goto(x_coord, y_coord)
    fillcolor(color)
    pendown()
    begin_fill()
    for i in range(4):
        forward(30)
        right(90)
    end_fill()
    penup()
    y_coord -= 50

# Регулятор
penup()
goto(0, 360)
pendown()
for i in range(2):
    forward(100)
    right(90)
    forward(20)
    right(90)

penup()
goto(0, 360)
pendown()
write('0')

penup()
goto(100, 360)
pendown()
write('100')

# 1. Добавить кнопки + и -, чтобы изменять размер на +5 и -5
# 2. Добавить кнопки КРУГ и КВАДРАТ, чтобы рисовать разные фигуры


window = Screen()
window.onscreenclick(click_handler)


done()
