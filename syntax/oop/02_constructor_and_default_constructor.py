# '__init__' is the constructor method in Python.
# It runs automatically when an object is created like a constructor in Java.
# We can only define one __init__ per class. However, we can simulate multiple constructors using default arguments like Book("Python Basics", "Harsha") and  Book().

class Book:
    def __init__(self, title="Untitled", author="Unknown"):
        self.title = title
        self.author = author

    def info(self):
        return f"{self.title} by {self.author}"

book1 = Book("Python Basics", "Harsha")
book2 = Book()  # Uses default values defined in the constructor
print(book1.info())
print(book2.info())
