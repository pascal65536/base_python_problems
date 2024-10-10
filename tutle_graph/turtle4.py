from turtle import *

t = Pen()
t.speed(0)
t.pensize(3)
color_lst = ["maroon", "green", "red", "magenta", "blue", "orange"]
for x in range(30):
    t.pencolor(color_lst[x % len(color_lst)])
    t.left(360 / len(color_lst))
    t.forward(100 - x*3)
    
done()
