from turtle import *
import random

def up():
    tim.setheading(90)
    tim.forward(100)

def down():
    tim.setheading(270)
    tim.forward(100)

def left():
    tim.set_heading(180)
    tim.forward(100)

def right():
    tim.setheading(0)
    tim.forward(100)

listen()

onkey(up, "Up")  # This will call the up function if the "Left" arrow key is pressed
onkey(down, "Down")
onkey(left, "Left")
onkey(right, "Right")

mainloop()  # This will make sure the program continues to run 
