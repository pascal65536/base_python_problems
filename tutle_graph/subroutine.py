import turtle


def square(x, y, size=100):
    turtle.penup()
    turtle.setposition(x, y)
    turtle.pendown()
    for i in range(4):
        turtle.forward(size)
        turtle.right(90)
    turtle.penup()


turtle.shape("turtle")
turtle.shapesize(2)
turtle.color("blue")
turtle.speed(0)

for x in range(-300, 300, 35):
    for y in range(-200, 300, 35):
        square(x, y, 30)

turtle.hideturtle()
turtle.done()
