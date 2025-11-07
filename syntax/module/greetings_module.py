#A module is just a Python file (.py) that contains code — like variables, functions, or classes , which we can reuse in other programs by importing it.

# greetings_module.py
# This is a Python module. we can import it into other files and reuse the code.

# -------------------------------
# A simple variable (no class)
# -------------------------------

# This variable stores a greeting message
greeting_message = "Hello, welcome to My World!"

# This function prints the greeting
def show_greeting():
    print(greeting_message)


# A class with variables and methods
# -------------------------------

# A class is like a template for creating objects (Like Java classes).
class Greeter:
    # This is a class variable
    default_name = "Guest"

    # This is the constructor method. It runs when we create an object. (Like a Java constructor)
    def __init__(self, name=None):
        # If no name is given, use the default
        self.name = name if name else Greeter.default_name

    # This method prints a personalized greeting
    def greet(self):
        print(f"Hello, {self.name}! Nice to meet you.")

# -------------------------------
# Code that runs only when this file is executed directly
# -------------------------------

if __name__ == "__main__":
    # Run the function without using a class
    show_greeting()

    # Create an object from the class and use it
    person = Greeter("Harsha")
    person.greet()

    # Create another object with no name
    anonymous = Greeter()
    anonymous.greet()