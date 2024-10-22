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


class LSystem:
    def __init__(self, x, y, epoch=1, length=100, angle=60):
        self.epoch = epoch
        self.turtle_x = x
        self.turtle_y = y
        self.turtle_a = 0
        # self.name = 'Koch Snowflake'
        # self.axiom = 'F'
        # self.rules = {'F': 'F+F--F+F'}

        # self.name = "Nice tree"
        # self.axiom = "----F"
        # self.rules = {"F": "FF+[+F-F-F]-[-F+F+F]"}

        # self.name = "Кривая Серпинского"
        # self.axiom = "L--F--L--F"
        # self.rules = {"L": "+R-F-R+", "R": "-L+F+L-"}

        # self.name = "Кривая Гилберта"
        # self.axiom = "X"
        # self.rules = {"Y": "+XF-YFY-FX+", "X": "-YF+XFX+FY-", "F": "F"}
        
        # self.name = "Двоичное дерево"
        # self.axiom = "X"
        # self.rules = {"X": "F[-X][+X]"}
        
        self.name = "Кривая Леви"
        self.axiom = "++F"
        self.rules = {"F": "-F++F-"}
        
        self.angle = angle
        self.length = length
        self.stack = list()

    def calc(self):
        axiom = self.axiom
        for _ in range(self.epoch):
            a = ""
            for ax in axiom:
                a += self.rules.get(ax, ax)
            axiom = a
        return axiom

    def draw(self, flow):
        penup()
        goto(self.turtle_x, self.turtle_y)
        right(self.turtle_a)
        for f in flow:
            match f:
                case "F":
                    pendown()
                    forward(self.length)
                    penup()
                case "+":
                    left(self.angle)
                case "-":
                    right(self.angle)
                case "[":
                    self.stack.append((pos(), heading()))
                case "]":
                    t = self.stack.pop()
                    goto(t[0])
                    setheading(t[1])


class Scene:
    def __init__(self):
        # hideturtle()
        # dot()
        speed(1000)
        pensize(2)
        fractal = LSystem(-200, 0, 20, 10, 45)
        flow = fractal.calc()
        fractal.draw(flow)

    def draw_on_click(self, x, y):
        pass


if __name__ == "__main__":
    scene = Scene()
    # onscreenclick(scene.draw_on_click)
    done()


"""
L-systems can be extended to generate 3D fractals, allowing for more complex and visually interesting structures. Here are some examples of L-systems specifically designed for 3D fractals:

▎Basic Concepts

In 3D L-systems, we typically use three-dimensional space for drawing, which involves rotation around multiple axes. The symbols used in the production rules can represent different actions, such as moving forward, turning, and branching.

▎Example L-Systems for 3D Fractals

1. 3D Tree Structure

   • Axiom: X

   • Rules:

     • X -> F[+X][-X]

     • F -> FF

   • Interpretation:

     • F moves forward and draws a line.

     • + and - represent rotations around the Y-axis.

     • [ and ] are used to save and restore the current position and orientation.

2. 3D Sierpiński Tetrahedron

   • Axiom: F

   • Rules:

     • F -> F[+F]F[-F]F

   • Interpretation:

     • This rule generates a 3D fractal similar to the 2D Sierpiński triangle, but in three dimensions.

3. 3D Koch Snowflake

   • Axiom: F

   • Rules:

     • F -> F+F--F+F

   • Interpretation:

     • Similar to the 2D version, but you can apply rotations around different axes to create a 3D appearance.

4. 3D Dragon Curve

   • Axiom: FX

   • Rules:

     • X -> X+Y

     • Y -> -X+Y

   • Interpretation:

     • The + and - symbols can represent rotations in different axes, creating a complex 3D structure.

5. Fractal Plant

   • Axiom: X

   • Rules:

     • X -> F[+X]F[-X]F

     • F -> FF

   • Interpretation:

     • Similar to the basic tree structure but can be adjusted to create more complex branching patterns.

▎Drawing 3D L-Systems

When implementing a 3D L-system, you can use a graphics library (like OpenGL, Unity, or Processing) to visualize the generated structures. Here are some steps to consider:

1. Positioning: Use a stack to keep track of the current position and orientation when branching occurs.

2. Rotations: Define how the symbols affect the orientation in 3D space. You might have rules for rotating around the X, Y, and Z axes.

3. Rendering: Draw lines or shapes based on the movement commands (F) and apply transformations according to the rotation commands.

▎Conclusion

3D L-systems offer a powerful way to create intricate fractal structures that can mimic natural forms like trees, plants, and even abstract shapes. By tweaking the axioms and rules, you can explore a wide variety of fractal patterns in three-dimensional space.

"""
