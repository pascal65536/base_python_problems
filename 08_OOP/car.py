class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print('Автомобиль заведен.')
    
    def stop(self):
        print('Автомобиль остановлен.')
    
car4 = Car("Tesla", "Model S", 2023)
car4.start()
car4.start()
car4.stop()
car4.start()
car4.stop()
car4.stop()
