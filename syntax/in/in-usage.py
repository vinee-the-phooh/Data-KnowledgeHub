# Python 'in' Keyword
# - 'in' checks membership in containers (string, list, tuple, set, dict)
# - In dictionaries, it checks keys by default
# - Used in loops, conditionals, and comprehensions
# - Not used for checking if a variable is defined
# - Case-sensitive when used with strings
# - Can be customized in user-defined classes via __contains__()


#1. 'in' with Strings
# Checks if a substring exists inside a string
text = "Python is powerful"
print("Python" in text)     # True
print("java" in text)       # False

# Note: Case-sensitive comparison
print("python" in text)     # False

#2. 'in' with Lists
# Checks if an item exists in a list
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)   # True
print("grape" in fruits)    # False

#3. 'in' with Tuples
# Works the same as with lists
colors = ("red", "green", "blue")
print("green" in colors)    # True

#4. 'in' with Sets
# Fast membership testing
numbers = {1, 2, 3, 4}
print(3 in numbers)         # True
print(5 in numbers)         # False

#5. 'in' with Dictionaries
# Checks if a key exists (not the value!)
user = {"name": "Harsha", "age": 30}
print("name" in user)       # True
print("Harsha" in user)     # False

# To check values:
print("Harsha" in user.values())  # True

#6.'in' with Loops (for-in)
# Iterates over items in a container
for fruit in fruits:
    print(fruit)

#7. 'in' with Conditionals
# Used to make decisions based on membership
if "apple" in fruits:
    print("Apple is available")

#8. 'in' with List Comprehensions
# Filters items based on membership
available = [f for f in fruits if f in ["banana", "cherry"]]
print(available)  # ['banana', 'cherry']

#9. Incorrect: Checking if a variable exists using 'in'
# 'in' does NOT check if a variable is defined
# This will raise an error if 'x' is not defined

# try:
#     if "x" in locals():  # Not reliable for beginners
#         print("x exists")
# except NameError:
#     print("Variable not defined")

#Instead, use try/except
try:
    print(x)
except NameError:
    print("Variable x does not exist")

#10. 'in' with Custom Containers (Advanced)
# You can define __contains__() in a class to customize 'in' behavior

class Basket:
    def __init__(self, items):
        self.items = items

    def __contains__(self, item):
        return item in self.items

my_basket = Basket(["apple", "orange"])
print("apple" in my_basket)  # True
print("banana" in my_basket) # False
