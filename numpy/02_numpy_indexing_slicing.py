#NumPy Indexing & Slicing (Getting a part of the array using a range.) Module
#Goal: Access specific elements, rows, columns, and slices in arrays.

#Use [row, col] to access elements.
#Use [:, col] for columns, [row, :] for rows.
#Slicing: [start:stop], [start:stop:step]
#We can update values directly using indexing.

import numpy as np

#reate a 2D array (3 rows, 3 columns)
arr = np.array([[10, 20, 30],
                [40, 50, 60],
                [70, 80, 90]])

print("Original Array:\n", arr)

#Access a single element: row 1, column 2 (indexing starts at 0)
print("Element at [1, 2]:", arr[1, 2])  # Output: 60

#Access a full row
print("Row 0:", arr[0])  # Output: [10 20 30]

#Access a full column
print("Column 1:", arr[:, 1])  # Output: [20 50 80]

#Slice a sub-array: rows 0 to 1, columns 1 to 2
print("Sub-array:\n", arr[0:2, 1:3])  # Output: [[20 30], [50 60]]

#Reverse a row
print("Reversed Row 2:", arr[2][::-1])  # Output: [90 80 70]

#Slice with step: every second column
print("Every second column:\n", arr[:, ::2])  # Output: [[10 30], [40 60], [70 90]]

#Modify an element
arr[0, 0] = 999
print("Modified Array:\n", arr)


