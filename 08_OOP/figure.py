class Figure():
    def __init__(self, width=None, height=None):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def __str__(self):
        return f"Фигура со сторонами {self.width} и {self.height}"
    
    def __repr__(self):
        return f"Figure({self.width}, {self.height})"

class Rectangle(Figure):
    def __init__(self, width, height):
        super().__init__(width, height)

    def __str__(self):
        return f"Прямоугольник со сторонами {self.width} и {self.height}"

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

class Square(Figure):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

    def __str__(self):
        return f"Квадрат со стороной {self.width}"

    def __repr__(self):
        return f"Square({self.width})"
    


# Примеры использования
rectangle1 = Rectangle(3, 4)
square1 = Square(5)
print(rectangle1)
print(rectangle1.perimeter())
print(square1)   
print(square1.area())   


# Дополнительные примеры
rectangle2 = Rectangle(6, 8)
square2 = Square(10)
print(rectangle2)
print(square2)
