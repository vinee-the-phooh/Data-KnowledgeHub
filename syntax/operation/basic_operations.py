#This module explains basic arithmetic and assignment operations in Python.

#Arithmetic Operators
    # These operators are used to do math with numbers

a = 10
b = 3

print("Addition:", a + b)        #  13
print("Subtraction:", a - b)     #  7
print("Multiplication:", a * b)  # 30
print("Division:", a / b)        #Divides: 3.333...
print("Floor Division:", a // b) #Removes decimal: 3
print("Modulus:", a % b)         #Remainder: 1
print("Exponent:", a ** b)       #Power: 10^3 = 1000


#Assignment Operators
    # These are used to store values in variables

x = 5       # Assigns value 5 to x
x += 2      # Same as x = x + 2: x becomes 7
x *= 3      # Same as x = x * 3: x becomes 21
x -= 1      # Same as x = x - 1:x becomes 20
x /= 4      # Same as x = x / 4:x becomes 5.0

print("Final value of x:", x)