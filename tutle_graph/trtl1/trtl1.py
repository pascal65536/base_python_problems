from turtle import *


def click_handler(x, y):
    print(x, y)
    penup()
    goto(x, y)
    pendown()
    begin_fill()
    circle(30)
    end_fill()


speed(2)
pensize(1)
pencolor("black")
fillcolor("red")

window = Screen()
window.onscreenclick(click_handler)

done()
