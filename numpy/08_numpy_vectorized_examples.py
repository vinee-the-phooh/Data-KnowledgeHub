# ✅ NumPy Vectorized Operations Module
# 🧠 Goal: Replace loops with fast, readable NumPy operations.

import numpy as np

# 🔹 Create a large array
arr = np.arange(1, 6)  # [1 2 3 4 5]
print("Original Array:", arr)

# 🔸 Traditional loop: square each element
squared_loop = []
for x in arr:
    squared_loop.append(x ** 2)
print("Squared (loop):", squared_loop)

# 🔸 Vectorized version: no loop needed
squared_np = arr ** 2
print("Squared (NumPy):", squared_np)

# 🔸 Traditional loop: add index to each element
added_loop = []
for i in range(len(arr)):
    added_loop.append(arr[i] + i)
print("Add index (loop):", added_loop)

# 🔸 Vectorized version
indices = np.arange(len(arr))
added_np = arr + indices
print("Add index (NumPy):", added_np)

# 🔸 Apply a custom formula: (x * 2 + 3)
custom_np = arr * 2 + 3
print("Custom formula:", custom_np)

# 🔸 Conditional logic: replace values < 3 with 0
cond_np = np.where(arr < 3, 0, arr)
print("Condition applied:", cond_np)

#My Learning Notes:
    #Vectorized = no loops, faster, cleaner.
    #Use math directly on arrays: arr + 5, arr * 2, etc.
    #Use np.where() for conditional logic.
    #Vectorized: Operations applied directly to arrays without loops.
    #Faster and more readable than traditional for-loops.
    #np.where(condition, value_if_true, value_if_false):conditional logic.