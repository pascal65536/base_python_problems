from tkinter import *


class Block:
    def __init__(self, master, func):
        self.ent = Entry(master, width=20)
        self.but = Button(master, text='Преобразовать')
        self.lab = Label(master, width=20, bg='black', fg='white')
        self.but['command'] = getattr(self, func)
        self.ent.pack()
        self.but.pack()
        self.lab.pack()

    def sort_words(self):
        s = self.ent.get().split()
        s.sort()
        self.lab['text'] = ' '.join(s)

    def reverse_words(self):
        s = self.ent.get().split()
        s.reverse()
        self.lab['text'] = ' '.join(s)


root = Tk()

first_block = Block(root, 'sort_words')
second_block = Block(root, 'reverse_words')

root.mainloop()