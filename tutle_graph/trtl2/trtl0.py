from turtle import *


def click_handler(x, y):
    print(x, y)

window = Screen()
window.onscreenclick(click_handler)

done()
