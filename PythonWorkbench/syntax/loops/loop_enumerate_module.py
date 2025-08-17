# Python Loop Module —  Using enumerate()
# What is enumerate()?
    # It's a built-in function that adds an index to each item in an iterable.
    # We get (index, value) pairs while looping.

fruits = ["apple", "berry", "cherry"]

# 1. Basic usage of enumerate()
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# Output:
# 0: apple
# 1: berry
# 2: cherry

#2. Custom starting index
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}: {fruit}")

# Output:
# 1: apple
# 2: berry
# 3: cherry

