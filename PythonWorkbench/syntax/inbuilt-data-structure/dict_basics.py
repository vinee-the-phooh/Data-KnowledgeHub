#This module explains Python dictionaries

#What is a dictionary?
    # A dictionary stores data as key-value pairs.
    # Each key must be unique. Values can be anything.
    # Dictionaries are useful for looking up data quickly using keys.
    # Keys can be strings, numbers, or tuples (but not lists).
    # Keys must be immutable (unchangeable)

#Creating a dictionary
person = {
    "name": "Harsha",
    "age": 43,
    "city": "Sydney"
}

#Accessing values
print(person["name"])  # "Harsha"

#Changing values
person["age"] = 44

#Adding new key-value pairs
person["job"] = "Senior Water Quality Analyst"

#Removing items
del person["city"]

#Looping through a dictionary
for key in person:
    print(key, "→", person[key])

