from turtle import *

points_lst = list()

def draw(points_lst):
    clear()
    for num, point in enumerate(points_lst):
        if num == 0:
            penup()
        else:
            pendown()
        goto(point[0], point[1])
        dot(5)

def click_left(x, y):
    print(x, y)
    points_lst.append((x, y))
    draw(points_lst)

def click_right(x, y):
    print(x, y)
    if points_lst:
        points_lst.pop(0)
        draw(points_lst)

def move_up():
    global points_lst
    new_lst = list()
    for point in points_lst:
        new_lst.append((point[0], point[1] + 10))
    points_lst = new_lst
    draw(points_lst)

def move_down():
    global points_lst
    new_lst = list()
    for point in points_lst:
        new_lst.append((point[0], point[1] - 10))
    points_lst = new_lst
    draw(points_lst)

window = Screen()
speed(100)
window.onscreenclick(click_left, 1)
window.onscreenclick(click_right, 3)
window.listen()
window.onkey(move_up, "Up")
window.onkey(move_down, "Down")

done()
