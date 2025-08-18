#NumPy Axis Operations Module
#Goal: Learn how to apply functions across rows and columns using axis.

import numpy as np

#reate a 2D array (3 rows, 3 columns)
arr = np.array([[10, 20, 30],
                [40, 50, 60],
                [70, 80, 90]])

print("Original Array:\n", arr)

#Sum of all elements
print("Total Sum:", np.sum(arr))  # Output: 450

#Sum across rows (axis=1)
print("Row-wise Sum:", np.sum(arr, axis=1))  # Output: [60 150 240]

#Sum across columns (axis=0)
print("Column-wise Sum:", np.sum(arr, axis=0))  # Output: [120 150 180]

#Mean across rows
print("Row-wise Mean:", np.mean(arr, axis=1))  # Output: [20. 50. 80.]

#Max value in each column
print("Column-wise Max:", np.max(arr, axis=0))  # Output: [70 80 90]

#Min value in each row
print("Row-wise Min:", np.min(arr, axis=1))  # Output: [10 40 70]

#My Learning Notes:
#axis=0 : down the rows (column-wise)
#axis=1 : across the columns (row-wise)
#Works with sum, mean, max, min, std, etc.