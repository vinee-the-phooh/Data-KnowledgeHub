#Inheritance in Python allows a class (child) to inherit attributes and methods from another class (parent).
#Use class Child(Parent) syntax.
#Child class inherits all public methods and attributes.

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def move(self):
        return f"{self.brand} is moving."

class Car(Vehicle):
    def honk(self):
        return "Beep beep!"

car = Car("Toyota")
print(car.move())
print(car.honk())
