from turtle import *

def click_handler(x, y):
    global color
    print(x, y)
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
    circle(30)
    end_fill()
    return

speed(2)
pensize(1)
penup()
pencolor("black")
color = "pink"

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

window = Screen()
window.onscreenclick(click_handler)

done()
