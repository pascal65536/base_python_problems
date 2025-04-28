from turtle import *


size=100
color='pink'
figure='circle'


def click_handler(x,y):
    global color, size, figure
    print(x,y)
    if 0<x<100 and 340<y<360 :
        print('size')
        size=x
        return
    if 200<x<230 and 170<y<200:
        figure='square'
        print('figure')
        return
    if x <=430 and x >=400 and y <= 400 and y >=370:
        color="red"
        pencolor="red"
        print('красный')
        return
    elif 400 <= x <=430 and 320 <= y <=350:
        color="green"
        pencolor="green"
        print('зелёни')
        return
    elif 400<=x<=430 and 270<=y<=300:
        color="blue"
        pencolor="blue"
        print('сини')
        return

    print(figure)
    if figure == 'circle':
        penup()
        goto(x,y)
        pendown()
        fillcolor(color)
        begin_fill()
        circle(size)
        end_fill()
    elif figure == 'square':
        penup()
        goto(x,y)
        pendown()
        fillcolor(color)
        begin_fill()
        for i in range(4):
            forward(size)
            right(90)
        end_fill()        
    return

y_coord=400
for word in ('red','green','blue'):
    penup()
    goto(400,y_coord)
    pendown()
    fillcolor(word)
    begin_fill()
    for i in range(4):
        forward(30)
        right(90)
    end_fill()
    y_coord-=50

penup()
goto(0,360)
pendown()
for i in range(2):
    forward(100)
    right(90)
    forward(20)
    right(90)


penup()
goto(200,200)
pendown()
for i in range(4):
    forward(30)
    right(90)


penup()
goto(0,360)
pendown()
write('0')

penup
goto(100,360)
pendown()
write('100')

speed(0)
pensize(2)
fillcolor("blue")

window = Screen()
window.onscreenclick(click_handler)

done()
