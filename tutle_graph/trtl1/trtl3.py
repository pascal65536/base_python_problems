from turtle import *


def click_handler(x, y):
    print(x, y)
    penup()
    goto(x, y)
    pendown()
    dot(5)


window = Screen()

speed(2)
pensize(1)
penup()
pencolor("black")


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


window.onscreenclick(click_handler)

done()
