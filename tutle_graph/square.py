import turtle


turtle.shape("turtle")
turtle.shapesize(2)
turtle.color("green")
turtle.speed(10)


for i in range(100):
    turtle.forward(5 + i)
    turtle.right(90)

turtle.hideturtle()
turtle.done()
