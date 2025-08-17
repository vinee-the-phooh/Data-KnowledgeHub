# constructor_examples.py
# This module shows different ways to use constructors in Python classes.
# A constructor is a special method called __init__ that runs when we create an object.
# It helps set up the object with initial values.

# Why use 'self'?
    # 'self' is a reference to the current object.
    # It lets each object store its own data and use its own methods. 
    # Without 'self', all objects would share the same data — which is not what we need.


# Case 1: Basic constructor with one variable
class SimpleGreeter:
    def __init__(self, name):
        # 'self.name' stores the name inside the object
        # Each object gets its own 'name' value
        self.name = name

    def greet(self):
        # 'self.name' lets us access the name stored in this object
        print(f"Hello, {self.name}!")


# Case 2: Constructor with default values
class GreeterWithDefault:
    def __init__(self, name="Guest"):
        # 'self.name' stores the name or uses "Guest" if none is given
        self.name = name

    def greet(self):
        # 'self.name' is used to print the personalized greeting
        print(f"Welcome, {self.name}!")

# Case 3: Constructor with multiple variables

class Person:
    def __init__(self, name, age, city):
        # 'self.name', 'self.age', and 'self.city' store values inside the object
        self.name = name
        self.age = age
        self.city = city

    def introduce(self):
        # We use 'self' to access the stored values
        print(f"My name is {self.name}, I'm {self.age} years old, and I live in {self.city}.")



# Case 4: Using class variables vs instance variables
class Counter:
    # Class variable: shared by all objects (Like a global variable for the class)
    count = 0

    def __init__(self):
        # Instance variable: unique to each object
        # 'self.id' stores the current count for this object
        self.id = Counter.count
        Counter.count += 1  # Increase the shared count

    def show_id(self):
        # 'self.id' is used to show the object's unique ID
        print(f"My ID is {self.id}")

#Case 5: Inheritance and using super()
# Parent class
class Animal:
    def __init__(self, species):
        # 'self.species' stores the type of animal
        self.species = species

    def speak(self):
        # 'self.species' is used to describe the animal
        print(f"I am a {self.species}")

# Child class
class Dog(Animal):
    def __init__(self, name):
        # 'super()' calls the parent constructor to set species
        super().__init__("Dog")
        # 'self.name' stores the dog's name
        self.name = name

    def speak(self):
        # 'self.name' is used to personalize the dog's speech
        print(f"{self.name} says: Woof!")


#Runs only when file is executed directly)

if __name__ == "__main__":
    # Case 1
    g1 = SimpleGreeter("Harsha")
    g1.greet()

    # Case 2
    g2 = GreeterWithDefault()
    g2.greet()

    g3 = GreeterWithDefault("Alex")
    g3.greet()

    # Case 3
    p1 = Person("Dush", 43, "Sydney")
    p1.introduce()

    # Case 4
    c1 = Counter()
    c2 = Counter()
    c1.show_id()
    c2.show_id()

    # Case 5
    d1 = Dog("Buddy")
    d1.speak()