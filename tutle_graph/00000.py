from turtle import *

speed(10)
pensize(2)
pencolor('yellow')
bgcolor("black")
fillcolor('green')

point_lst = list()

penup()
goto(0, 200)
# 1 branch
r0 = 100
right(90)
forward(r0 * (3 ** 0.5) / 2)
left(90)
pendown()
begin_fill()
forward(r0 / 2)
left(120)
forward(r0)
left(120)
forward(r0)
left(120)
forward(r0 / 2)
end_fill()


# 2 branch
penup()
r0 = 110
right(90)
forward(r0 * (3 ** 0.5) / 2)
left(90)
pendown()
begin_fill()
forward(r0 / 2)
left(120)
forward(r0)
left(120)
forward(r0)
left(120)
forward(r0 / 2)
end_fill()

# 3 branch
penup()
r0 = 130
right(90)
forward(r0 * (3 ** 0.5) / 2)
left(90)
pendown()
begin_fill()
forward(r0 / 2)
left(120)
forward(r0)
left(120)
forward(r0)
left(120)
forward(r0 / 2)
end_fill()

print(point_lst)
# hideturtle()
done()
