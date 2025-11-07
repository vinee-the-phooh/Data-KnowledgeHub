#NumPy Basics Module
#Goal: create arrays, check shapes, and use basic operations.

    #Use np.array() to create arrays.
    #Use .shape, .dtype, .max(), .mean(), etc. to explore arrays.
    #Arrays support math operations and reshaping.

#NumPy is a powerful library for numerical computing.
import numpy as np  

#Create a 1D array (like a simple list)
arr1 = np.array([1, 2, 3, 4])
print("1D Array:", arr1)

#Create a 2D array (like a table or matrix)
arr2 = np.array([[1, 2], [3, 4]])
print("2D Array:\n", arr2)

#Check the shape (rows, columns)
print("Shape of arr2:", arr2.shape)  # Output: (2, 2)

#Check the data type of elements
print("Data type:", arr1.dtype)  # Output: int64 (depends on system)

#Create arrays with zeros, ones, or random numbers
zeros = np.zeros((2, 3))  # 2 rows, 3 columns
ones = np.ones((3, 2))    # 3 rows, 2 columns
rand = np.random.rand(2, 2)  # Random numbers between 0 and 1

print("Zeros:\n", zeros) #Output: 2x3 array of zeros
print("Ones:\n", ones) # Output: 3x2 array of ones
print("Random:\n", rand) # Output: 2x2 array of random numbers

#Basic math operations
arr3 = np.array([10, 20, 30])
print("Add 5:", arr3 + 5)      # Adds 5 to each element
print("Multiply by 2:", arr3 * 2)  # Multiplies each element by 2

#Element-wise operations between arrays
arr4 = np.array([1, 2, 3])
arr5 = np.array([4, 5, 6])
print("Sum of arrays:", arr4 + arr5)  # [5, 7, 9]

#Useful functions
print("Max value:", arr5.max())      # 6
print("Mean value:", arr5.mean())    # 5.0
print("Reshape:", arr5.reshape((3, 1)))  # Change shape to 3 rows, 1 column


