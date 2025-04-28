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
    points_lst.pop(0)
    draw(points_lst)


window = Screen()
speed(100)
window.onscreenclick(click_left, 1)
window.onscreenclick(click_right, 3)

done()
