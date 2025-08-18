#Method Overloading in Python
    # Method Overloading is a feature in object-oriented programming that allows a class to have multiple methods with the same name but different parameters.
    # In Python, method overloading is not supported in the same way as in languages like Java.
    # However, we can achieve similar functionality using default arguments or variable-length arguments (*args and **kwargs).

class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

calc = Calculator()
print(calc.add(2))
print(calc.add(2, 3))
print(calc.add(2, 3, 4))
