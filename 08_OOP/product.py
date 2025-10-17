class Product:

    def __init__(self, name: str, price: float, quantity: int = 0):
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)

    def update_quantity(self, amount: int) -> None:
        if self.quantity + amount < 0:
            print("Количество не может стать отрицательным.")
            return
        self.quantity += amount

    def get_total_value(self) -> float:
        return self.price * self.quantity


desktop = Product("Настольный ПК", 75000, 5)
desktop.update_quantity(-5) 
print(desktop.get_total_value())
desktop.update_quantity(2) 
print(desktop.get_total_value())
desktop.update_quantity(2) 
print(desktop.get_total_value())
