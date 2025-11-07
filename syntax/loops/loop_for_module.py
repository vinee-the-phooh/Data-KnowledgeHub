#Python Loop Module —  for loop
# What is a for loop?
    # A for loop is used to repeat a block of code for each item in a sequence (like a list, string, or range).
    # It automatically assigns each item to a variable and runs the loop body.


#1. Looping through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Output:
# apple
# banana
# cherry

#2. Looping through a string
# Each character in the string is treated as an item
word = "hello"
for char in word:
    print(char)

#3. Using range() to loop over numbers
# range(start, stop) generates numbers from start to stop-1
for i in range(3):
    print("Iteration:", i)

# Output:
# Iteration: 0
# Iteration: 1
# Iteration: 2

#4. Looping with range(start, stop, step)
# We can control the step (increment or decrement)
for num in range(1, 10, 2):
    print("Odd number:", num)

# Output:
# Odd number: 1
# Odd number: 3
# Odd number: 5
# Odd number: 7
# Odd number: 9

#5. Using break to exit early
# break stops the loop immediately
for letter in "python":
    if letter == "h":
        break
    print(letter)

# Output:
# p
# y
# t

#6. Using continue to skip an item
# continue skips the current iteration and moves to the next
for letter in "python":
    if letter == "h":
        continue
    print(letter)

# Output:
# p
# y
# t
# o
# n

#7. Using else with for loop
# The else block runs only if the loop completes without break
for num in range(5):
    print(num)
else:
    print("Loop finished without break")

#8. Nested for loops
# A loop inside another loop — useful for grids, matrices
for i in range(2):
    for j in range(3):
        print(f"i={i}, j={j}")

#9. Looping with enumerate()
# enumerate gives index and value — useful for tracking position
colors = ["red", "green", "blue"]
for index, color in enumerate(colors):
    print(f"Color {index}: {color}")

#10. Looping with zip()
# zip combines multiple sequences into pairs
names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 95]
for name, score in zip(names, scores):
    print(f"{name} scored {score}")

