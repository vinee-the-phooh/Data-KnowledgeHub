#This module explains identity and membership operators in Python.

#Identity Operators
    # These check if two variables point to the same object in memory

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print("a is b:", a is b)     #True - same object
print("a is c:", a is c)     #False — same content, different object
print("a is not c:", a is not c)  #True


#Membership Operators
    # These check if a value exists inside a sequence (list, string, etc.)

fruits = ["apple", "banana", "cherry"]

print("Is 'banana' in fruits?", "banana" in fruits)  #True
print("Is 'grape' not in fruits?", "grape" not in fruits)  #True