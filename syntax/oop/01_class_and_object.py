# A class is a template. An object is an instance of that template.

class Person:
    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age

    def greet(self): #self refers to the current object.
        return f"Hi, I'm {self.name} and I'm {self.age} years old."

# Creating objects
person1 = Person("Harsha", 43) #Object is created using ClassName() like java
print(person1.greet())


