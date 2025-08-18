#This module explains Python tuples.

#What is a tuple?   
    # A tuple is like a list, but we cannot change it (immutable).
    # Use it when we want to protect data from changes.
    # Tuples are ordered meaning items stay in the same order we put them in.

#Creating a tuple
colors = ("red", "green", "blue")

#Accessing items
print(colors[0])  # "red"
print(colors[-1]) # "blue"

#Looping through a tuple
for color in colors:
    print(color)
