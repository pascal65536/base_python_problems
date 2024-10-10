from turtle import *

t = Pen()
t.speed(0)
t.pensize(3)
t.pencolor('blue')

n = 6
for x in range(n):
    t.left(360 / n)
    t.circle(100, 360, n)

done()
