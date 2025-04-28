from turtle import *


size = 30
color = 'black'

def click_handler(x, y):
    global size, color
    print(x, y)
    if 0 < x < 100 and 330 < y < 350:
        size = x
        return
    if 400 < x < 430 and 370 < y < 400:
        color = "red"
        return
    if 400 < x < 430 and 320 < y < 350:
        color = "green"
        return
    if 400 < x < 430 and 270 < y < 300:
        color = "blue"
        return        
    penup()
    goto(x, y)
    pendown()
    fillcolor(color)
    begin_fill()
    circle(size)
    end_fill()
    return


window = Screen()

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

# Выбор размера
x_coord = 0
y_coord = 350
penup()
goto(x_coord, y_coord)
pendown()
write("0", align="center", font=("Arial", 24, "normal"))

x_coord = 100
y_coord = 350
penup()
goto(x_coord, y_coord)
pendown()
write("100", align="center", font=("Arial", 24, "normal"))

penup()
goto(0, 350)
pendown()
for i in range(2):
    forward(100)
    right(90)
    forward(20)
    right(90)

window.onscreenclick(click_handler)

done()
