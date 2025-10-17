class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f'Cat meow')

    def __str__(self):
        return f'My name is {self.name}. I`m {self.age} old'
    
    def __repr__(self):
        return f'My name is {self.name}. I`m {self.age} old'

# bob = Cat('Bob', 2)
# print(bob)

