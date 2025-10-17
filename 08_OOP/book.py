class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return f"Название: {self.title}, Автор: {self.author}, Год: {self.year}"
    
book = Book("Гарри Поттер и философский камень", "Дж. К. Роулинг", 1997)
print(book.get_info())



          