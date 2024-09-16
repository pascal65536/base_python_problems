import turtle

def draw_triangle(points, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.goto(points[0])
    turtle.goto(points[1])
    turtle.goto(points[2])
    turtle.goto(points[0])
    turtle.end_fill()

def sierpinski(points, depth):
    if depth == 0:
        draw_triangle(points, "blue")
    else:
        mid1 = ((points[0][0] + points[1][0]) / 2, (points[0][1] + points[1][1]) / 2)
        mid2 = ((points[1][0] + points[2][0]) / 2, (points[1][1] + points[2][1]) / 2)
        mid3 = ((points[0][0] + points[2][0]) / 2, (points[0][1] + points[2][1]) / 2)
        
        sierpinski([points[0], mid1, mid3], depth - 1)
        sierpinski([points[1], mid1, mid2], depth - 1)
        sierpinski([points[2], mid2, mid3], depth - 1)

def main():
    turtle.speed(0)  # Установите максимальную скорость рисования
    turtle.bgcolor("white")
    
    # Задайте начальные точки треугольника
    points = [(-200, -150), (0, 200), (200, -150)]
    
    sierpinski(points, 4)  # Уровень глубины фрактала
    
    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()
