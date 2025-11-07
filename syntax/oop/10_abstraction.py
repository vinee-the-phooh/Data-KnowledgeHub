# Abstraction in Python'
    # Abstraction is a fundamental concept in object-oriented programming that allows we to define abstract methods.
    # They are meant to be subclassed, and their abstract methods must be implemented by subclasses like in Java.
    # It helps in hiding the implementation details and exposing only the necessary parts of the class.
    # Use ABC and @abstractmethod from abc module.
    #Abstract classes cannot be instantiated directly.


from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

circle = Circle(5)
print(circle.area())


