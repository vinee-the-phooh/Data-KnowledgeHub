#NumPy Broadcasting Module
#Goal: Learn how NumPy automatically adjusts shapes to perform operations.

import numpy as np

#Create a 1D array
arr1 = np.array([1, 2, 3])
print("Original arr1:", arr1)

#Add a single number to all elements (scalar broadcasting)
print("arr1 + 10:", arr1 + 10)  # Output: [11 12 13]

#Create a 2D array (3 rows, 1 column)
arr2 = np.array([[1],
                 [2],
                 [3]])
print("2D arr2:\n", arr2)

#Create a 1D array with 3 columns
arr3 = np.array([10, 20, 30])
print("1D arr3:", arr3)

#Add arr2 and arr3 → shapes: (3,1) + (3,) → result: (3,3)
result = arr2 + arr3
print("Broadcasted Result:\n", result)

#Broadcasting works when dimensions are compatible:
    #arr2 shape: (3, 1)
    #arr3 shape: (   3,) : treated as (1, 3)
    #NumPy stretches them to (3, 3)

#Example: Multiply a column vector with a row vector
col = np.array([[1], [2], [3]])  # shape (3,1)
row = np.array([10, 20, 30])     # shape (3,)
print("Multiplication:\n", col * row)  # Output: 3x3 matrix

#My Learning Notes:
    #Broadcasting lets NumPy work with arrays of different shapes.
    #It stretches smaller arrays to match larger ones (if compatible).
    #Saves memory and avoids writing loops.

