from turtle import *

def house(size):
    pendown()
    right(90)
    forward(size)
    dot()
    right(90)
    forward(size)
    dot()
    right(90)
    forward(size)
    dot()
    right(90)
    forward(size)
    dot()
    left(45 + 90)
    forward(size / 2 ** 0.5)
    dot()
    left(90)
    forward(size / 2 ** 0.5)
    dot()
    penup()
    left(180 - 45)


clear()
speed(2)

penup()
goto(300, 300)
house(100)
goto(0, 300)
house(100)
goto(-300, 300)
house(100)

goto(300, 0)
house(50)
goto(0, 0)
house(50)
goto(-300, 0)
house(50)

goto(300, -300)
house(25)
goto(0, -300)
house(25)
goto(-300, -300)
house(25)

hideturtle()
done()
