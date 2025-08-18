#This module explains comparison and logical operations in Python.

#Comparison Operators
    # These are used to compare values and return True or False

a = 10
b = 5

print("Equal:", a == b)           # Is a equal to b:  False
print("Not Equal:", a != b)       # Is a not equal to b:True
print("Greater than:", a > b)     # Is a bigger than b:True
print("Less than:", a < b)        # Is a smaller than b:False
print("Greater or equal:", a >= b)# Is a ≥ b:True
print("Less or equal:", a <= b)   # Is a ≤ b:False


#Logical Operators
    # These are used to combine multiple conditions

x = 7

print("x is between 5 and 10:", x > 5 and x < 10)  #Both conditions must be True (Like Java's &&)
print("x is less than 5 or greater than 10:", x < 5 or x > 10)  #Only one condition must be True (Like Java's ||)
print("Not True:", not True)  #Reverses the result:False (Like Java's !)