from turtle import *



speed(1)
pensize(3)

penup()
goto(100, 100)
pendown()
        
fillcolor("lightblue")
begin_fill()
for _ in range(4):
    forward(100)
    left(90)
end_fill()


fillcolor("brown")
begin_fill()
left(45)
forward(100)
right(90)
forward(100)
end_fill()
left(45)


penup()
goto(20, 50)
pendown()
fillcolor("saddlebrown")
begin_fill()
for _ in range(2):
    forward(40)
    left(90)
    forward(60)
    left(90)
end_fill()
        
done()
