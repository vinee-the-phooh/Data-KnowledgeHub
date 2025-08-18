# 'super()' lets we call methods from the parent class.

class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call parent constructor
        self.breed = breed

dog = Dog("Timi", "Labrador")
print(dog.name)
print(dog.breed)
