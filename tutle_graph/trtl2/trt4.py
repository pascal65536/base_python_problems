from turtle import *
speed(2)
pensize(1)
pencolor('black')
figure = 'circle'
size = 100
color="blue"

y_cord = 400
for word in [ 'red', 'green', 'blue', 'grey']:
    penup()
    goto(400, y_cord)
    pendown()
    fillcolor(word)
    begin_fill()
    for i in range(4):
        forward(30)
        right(90)
    end_fill()
    y_cord-= 50

y_cord = 400
for word in [ 'black', 'white', 'yellow', 'grey']:
    penup()
    goto(300, y_cord)
    pendown()
    fillcolor(word)
    begin_fill()
    for i in range(4):
        forward(30)
        right(90)
    end_fill()
    y_cord-= 50

def click_handler(x, y):
    global color, size, figure
    print(x, y)
    if 430>x>400 and 300> y >270:
        color="blue"
        print('ты попал в синий квадрат')
        return
    elif 430>x>400 and 400>y>370:
        color="red"
        print('ты попал в красный квадрат')
        return
    elif 430>x>400 and 350>y>320:
        color="green"
        print('ты попал в зеленый квадрат')
        return
    elif 330>x>300 and 400>y>370:
        color="black"
        print('ты попал в черный квадрат')
        return
    elif 330>x>300 and 350>y>320:
        color="white"
        print('ты попал в белый квадрат')
        return
    elif 330>x>300 and 300>y>270:
        color="yellow"
        print('ты попал в желтый квадрат')
        return
    elif 100>x>0 and 360>y>340:
        size=x
        print('size')
        return
    elif 330>x>300 and 250>y>220:
        figure = 'circle'
        print('circle')
        return
    elif 430>x>400 and 250>y>220:
        figure = 'square'
        print('square')
        return
    
    penup()
    goto(x, y)
    pendown()
    fillcolor(color)
    begin_fill()
    if figure == 'circle':
        circle(size)
    elif figure == 'square':
        for i in range(4):
            forward(size)
            right(90)        
    end_fill()
        
penup()
goto(0, 360)
pendown()
for i in range(2):
    forward(100)
    right(90)
    forward(20)
    right(90)

penup()
goto(0, 360)
pendown()
write('0')

penup()
goto(100, 360)
pendown()
write('100')

penup()
goto(316.0, 232.0)
pendown()
write('o')
penup()
goto(415.0 ,233.0)
pendown()
write('■')
penup()

window = Screen()
window.onscreenclick(click_handler)

done()
