from turtle import *

speed(1000)
pensize(2)
pencolor('yellow')
bgcolor("black")
fillcolor('green')

point_lst = list()

# 1 branch
penup()
goto(0, 200)
r0 = 100
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
goto(0, 100)
r0 = 120
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
goto(0, 0)
r0 = 140
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

# 4 branch
penup()
goto(0, -100)
r0 = 160
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

# 5 branch
penup()
goto(0, -200)
r0 = 180
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

# Рисуем ствол ёлки
penup()
pendown()
fillcolor('brown')
begin_fill()
forward(20)
right(90)
forward(100)
right(90)
forward(40)
right(90)
forward(100)
right(90)
end_fill()

penup()
goto(-60.00,100.00)
pendown()
right(90)
forward(25)
left(90)

fillcolor('red')
begin_fill()
circle(10)
end_fill()

print(point_lst)
# hideturtle()
done()
