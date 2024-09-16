import tkinter as tk

def draw_a(canvas, x, y, size=30):
    canvas.create_line(x, y + size, x + size / 2, y, fill="blue", width=2)
    canvas.create_line(x + size / 2, y, x + size, y + size, fill="blue", width=2)
    canvas.create_line(x + size / 4, y + size / 2, x + 3 * size / 4, y + size / 2, fill="blue", width=2)

def draw_b(canvas, x, y, size=30):
    canvas.create_line(x, y, x, y + size, fill="blue", width=2)
    canvas.create_line(x, y + size, x + size / 2, y + size, fill="blue", width=2)
    canvas.create_line(x + size / 2, y + size, x + size / 2, y + size / 2, fill="blue", width=2)
    canvas.create_line(x + size / 2, y, x + size, y, fill="blue", width=2)
    canvas.create_line(x + size, y + size / 2, x + size, y + size, fill="blue", width=2)

def draw_c(canvas, x, y, size=30):
    canvas.create_arc(x, y, x + size, y + size, start=90, extent=-180, outline="blue", width=2)

def main():
    root = tk.Tk()
    root.title("Drawing Letters")
    
    canvas = tk.Canvas(root, width=600, height=400)
    canvas.pack()
    
    i = 1
    draw_a(canvas, 50 + i * 100, 100)
    i = 2
    # draw_b(canvas, 150 + i * 100, 100)
    i = 3
    draw_c(canvas, 250 + i * 100, 100)

    # Рисуем буквы
    # for i in range(3):
    #     draw_a(canvas, 50 + i * 100, 100)
    #     draw_b(canvas, 150 + i * 100, 100)
    #     draw_c(canvas, 250 + i * 100, 100)

    root.mainloop()

if __name__ == "__main__":
    main()
