from turtle import *

class House:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        # Рисуем квадрат (основу дома)
        penup()
        goto(self.x, self.y)
        pendown()
        
        fillcolor("lightblue")
        begin_fill()
        for _ in range(4):
            forward(100)
            left(90)
        end_fill()

        # Рисуем крышу
        fillcolor("brown")
        begin_fill()
        left(45)
        forward(100)
        right(90)
        forward(100)
        end_fill()
        left(45)

        # Рисуем дверь
        penup()
        goto(self.x - 20, self.y - 50)
        pendown()
        fillcolor("saddlebrown")
        begin_fill()
        for _ in range(2):
            forward(40)
            left(90)
            forward(60)
            left(90)
        end_fill()

        # Рисуем окна
        for offset in [-40, 10]:
            penup()
            goto(self.x + offset, self.y - 20)
            pendown()
            fillcolor("white")
            begin_fill()
            for _ in range(4):
                forward(30)
                left(90)
            end_fill()


class Tree:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        # Рисуем ствол дерева
        penup()
        goto(self.x - 10, self.y - 50)
        pendown()
        fillcolor("saddlebrown")
        begin_fill()
        for _ in range(2):
            forward(20)
            left(90)
            forward(40)
            left(90)
        end_fill()

        # Рисуем крону дерева
        penup()
        goto(self.x - 20, self.y - 50)
        pendown()
        fillcolor("green")
        begin_fill()
        for _ in range(3):
            forward(60)
            left(120)
        end_fill()


class Scene:
    def __init__(self):
        speed(0)
        pensize(3)

    def draw_on_click(self, x, y):
        house = House(x, y)
        house.draw()
        
        tree = Tree(x - 100, y - 50)
        tree.draw()

if __name__ == '__main__':
    # Настройка обработки кликов мыши
    scene = Scene()
    onscreenclick(scene.draw_on_click)

    # Запускаем главный цикл
    done()
