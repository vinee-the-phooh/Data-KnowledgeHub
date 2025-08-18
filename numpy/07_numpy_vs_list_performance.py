#NumPy vs Python List Performance Module
#Goal: Compare speed and memory between NumPy arrays and Python lists.

import numpy as np
import time

#Create a large list and a large NumPy array
size = 1_000_000
py_list = list(range(size))
np_array = np.arange(size)

#Time: Add 5 to each element using Python list (loop)
start_list = time.time()
py_result = [x + 5 for x in py_list]
end_list = time.time()
print("Python List Time:", end_list - start_list, "seconds")

#Time: Add 5 to each element using NumPy (vectorized)
start_np = time.time()
np_result = np_array + 5
end_np = time.time()
print("NumPy Array Time:", end_np - start_np, "seconds")

#Memory usage
print("List Memory (approx):", len(py_list) * py_list[0].__sizeof__(), "bytes")
print("NumPy Memory:", np_array.nbytes, "bytes")

#My Learning Notes: 
    #NumPy is much faster for large data (no loops).
    #NumPy uses less memory.
    #Vectorized operations = clean + fast.