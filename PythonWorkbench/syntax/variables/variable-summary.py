#Python variable is a name that refers to a value. Variable can hold numbers, strings, lists, dictionaries, and more.
x = 10
name = "Mark"
items = [1, 2, 3]
user = {"name": "Rani", "age": 30}

#Variables are created when we assign a value to them.
score = 95

#Variables can be reassigned to different values or types.
x = 5
x = "five"  # dynamic typing

#Variables are case-sensitive, meaning 'myVar' and 'myvar' are different variables.
myVar = 1
myvar = 2
print(myVar, myvar)  # 1 2

#Variables can be used in expressions and functions.
a = 5
b = 3
def add(x, y):
    return x + y
print(add(a, b))  # 8

#Variables can be global or local in scope.
x = "global"
def show():
    x = "local"
    print(x)
show()       # local
print(x)     # global

#Variables can be declared using the assignment operator '='.
language = "Python"

# Variables can be used in loops to control repetition.
# Example: Looping through a range of numbers
for i in range(3):  # i takes values 0, 1, 2
    print(i)

#Variables can be used in conditionals to make decisions.
x = 10
if x > 5:  # Checks if x is greater than 5
    print("x is large")

#Variables can be passed as arguments to functions.
def greet(name):
    print("Hello", name)
greet("Rani")

#Variables can be used in list comprehensions.
squares = [x**2 for x in range(5)]

#Variables can be used in string formatting.
name = "Rani"
print("Hello %s" % name)

#Variables can be used in f-strings for formatting.
age = 30
print(f"{name} is {age} years old")

#Variables can be used in string formatting.
name = "Rani"
print("Hello %s" % name)

#Variables can be used in f-strings for formatting.
age = 30
print(f"{name} is {age} years old")

#Variables can be used in type annotations.
x: int = 5
name: str = "Rani"

#Variables can be used in type hints for function parameters and return types.
def add(a: int, b: int) -> int:
    return a + b

#Variables can be used in type casting.
x = int("5")  # 5

#Variables can be used in type coercion.
result = 5 + 3.0  # int + float → float (8.0)

#None is equivalent to null in other languages.
x = None
print(x is None)  # True

#Multiple variables can be assigned in a single line using tuple unpacking.
a, b = 1, 2

#Swapping variables can be done in a single line.
a, b = b, a