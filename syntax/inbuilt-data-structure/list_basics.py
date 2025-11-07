#This module explains Python lists

#What is a list?
    # A list is a collection of items. We can change it (mutable).
    # It can hold different types: numbers, strings, even other lists.
    #Lists are ordered, meaning items stay in the same order we put them in.

#Creating a list
fruits = ["apple", "banana", "cherry"]

#Accessing items
print(fruits[0])  # "apple" (first item)
print(fruits[-1]) # "cherry" (last item)

#Changing items
fruits[1] = "blueberry"
print(fruits)  # ['apple', 'blueberry', 'cherry']

#Adding items
fruits.append("date")         # Add to end
fruits.insert(1, "avocado")   # Add at index 1
print(fruits)

#Removing items
fruits.remove("apple")        # Remove by value
popped = fruits.pop()         # Remove last item
print(fruits)

#Looping through a list
for fruit in fruits:
    print(fruit)