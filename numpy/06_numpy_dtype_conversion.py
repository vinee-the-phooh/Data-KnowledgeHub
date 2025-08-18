#NumPy Data Type Conversion Module
#Goal: Learn how to check and change data types in arrays.

import numpy as np

#Create an array of integers
arr_int = np.array([1, 2, 3, 4])
print("Integer Array:", arr_int)
print("Data Type:", arr_int.dtype)  # Output: int64 (may vary)

#Convert to float
arr_float = arr_int.astype(float)
print("Converted to Float:", arr_float)
print("New Data Type:", arr_float.dtype)  # Output: float64

#Convert to string
arr_str = arr_int.astype(str)
print("Converted to String:", arr_str)
print("New Data Type:", arr_str.dtype)  # Output: <U21 (Unicode string)

#Convert float to int (truncates decimals)
arr_f = np.array([1.9, 2.5, 3.1])
arr_f_to_int = arr_f.astype(int)
print("Float to Int:", arr_f_to_int)  # Output: [1 2 3]

#Memory usage comparison
print("Size of int array (bytes):", arr_int.nbytes)
print("Size of float array (bytes):", arr_float.nbytes)

#My Learnings Notes:
    #Use .dtype to check data type.
    #Use .astype(new_type) to convert.
    #Converting float : int removes decimals.
    #Data type affects memory and performance.
