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
fillcolor("red")

goto(300, 300)
fillcolor("red")
pendown()
begin_fill()
for i in range(4):
    forward(30)
    right(90)
end_fill()
penup()

goto(300, 250)
fillcolor("green")
pendown()
begin_fill()
for i in range(4):
    forward(30)
    right(90)
end_fill()
penup()

goto(300, 200)
fillcolor("blue")
pendown()
begin_fill()
for i in range(4):
    forward(30)
    right(90)
end_fill()
penup()

window.onscreenclick(click_handler)

done()
