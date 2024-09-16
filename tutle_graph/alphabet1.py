import turtle
import tkinter as tk
from turtle import RawTurtle, ScrolledCanvas

def draw_a(t):
    t.penup()
    t.goto(-50, 0)
    t.pendown()
    t.setheading(75)
    t.forward(100)
    t.setheading(285)
    t.forward(100)
    t.setheading(180)
    t.forward(50)
    t.setheading(75)
    t.penup()
    t.goto(-25, 40)
    t.pendown()
    t.forward(25)

def draw_b(t):
    t.penup()
    t.goto(-50, 0)
    t.pendown()
    t.setheading(90)
    t.forward(100)
    t.setheading(0)
    t.forward(50)
    t.setheading(180)
    t.circle(-25, 180)
    t.setheading(0)
    t.forward(50)
    t.setheading(270)
    t.circle(-25, 180)

def draw_c(t):
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.setheading(90)
    t.circle(25, 180)

def main():
    root = tk.Tk()
    root.title("Drawing Letters with Turtle")

    canvas = ScrolledCanvas(root)
    canvas.pack(fill=tk.BOTH, expand=tk.YES)

    t = RawTurtle(canvas)

    # Рисуем буквы
    draw_a(t)
    
    # # Перемещаемся для следующей буквы
    # t.penup()
    # t.goto(-200, -100)  # Сдвинем вниз
    # t.pendown()
    
    # draw_b(t)

    # # Перемещаемся для следующей буквы
    # t.penup()
    # t.goto(-200, -200)  # Сдвинем вниз
    # t.pendown()
    
    # draw_c(t)

    root.mainloop()

if __name__ == "__main__":
    main()
