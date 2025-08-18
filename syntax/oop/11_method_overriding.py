#Method Overriding in Python
#Method Overriding is a feature in object-oriented programming that allows a child class to provide a specific implementation of a method that is already defined in its parent class.
#This enables the child class to modify or extend the behavior of the parent class method.
#It is a way to achieve polymorphism in Python.

class Employee:
    def work(self):
        return "Working 9 to 5"

class Developer(Employee):
    def work(self):
        return "Coding all day"

dev = Developer()
print(dev.work())


