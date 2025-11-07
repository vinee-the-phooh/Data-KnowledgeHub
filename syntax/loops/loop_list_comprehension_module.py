#Python Loop Module — List Comprehension

#What is a list comprehension?
    # A list comprehension lets us create a new list in a shorter way.
    # It uses a for loop inside square brackets to go through items one by one.
    # We can also add a condition to include only certain items.

#1. Basic list comprehension
# Create a list of squares from 0 to 4
squares = [x**2 for x in range(5)]
print("Squares:", squares)  # [0, 1, 4, 9, 16]

#2. With condition (with filtering)
evens = [x for x in range(10) if x % 2 == 0] # Include only even numbers
print("Even numbers:", evens)  # [0, 2, 4, 6, 8]

#With if-else expression
# Label numbers as "even" or "odd"
labels = ["even" if x % 2 == 0 else "odd" for x in range(5)]
print("Labels:", labels)  # ['even', 'odd', 'even', 'odd', 'even']

#4. Looping over a string
# Convert each character to uppercase
word = "sydney"
upper_chars = [char.upper() for char in word]
print("Uppercase letters:", upper_chars)  # ['S', 'Y', 'D', 'N', 'E', 'Y']

#5. Nested list comprehension
# Flatten a 2D list (Convert this into a single flat list → [1, 2, 3, 4, 5, 6])
matrix = [[1, 2], [3, 4], [5, 6]] # Original 2D list (a list of lists)
# - First loop: for row in matrix → goes through each sublist
# - Second loop: for num in row → goes through each number inside that sublist
# - The result: collect each number into one flat list
flattened = [num for row in matrix for num in row]
print("Flattened list:", flattened)  # [1, 2, 3, 4, 5, 6]

# 6. Using functions inside list comprehension
def square(n):
    return n * n

results = [square(x) for x in range(5)]
print("Function-based squares:", results)  # [0, 1, 4, 9, 16]

#7. List comprehension with strings
names = ["rani", "lili", "bob"]
capitalized = [name.capitalize() for name in names]
print("Capitalized names:", capitalized)  # ['Rani', 'Lili', 'Bob']

#8. Filtering with multiple conditions
# Include numbers divisible by both 2 and 3
filtered = [x for x in range(20) if x % 2 == 0 and x % 3 == 0]
print("Divisible by 2 and 3:", filtered)  # [0, 6, 12, 18]

