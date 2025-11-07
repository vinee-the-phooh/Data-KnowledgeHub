# NumPy Boolean Masking Module
# Goal: Learn how to filter arrays using conditions (True/False masks)

import numpy as np

#Create a simple array
arr = np.array([5, 10, 15, 20, 25])
print("Original Array:", arr)

#Create a boolean mask: values greater than 15
mask = arr > 15
print("Mask (arr > 15):", mask)  # Output: [False False False  True  True]

#Use the mask to filter values
filtered = arr[mask]
print("Filtered values:", filtered)  # Output: [20 25]

#Combine conditions: values between 10 and 25
mask2 = (arr >= 10) & (arr <= 25)
print("Mask (10 ≤ arr ≤ 25):", mask2)  # Output: [False  True  True  True  True]
print("Filtered:", arr[mask2])        # Output: [10 15 20 25]

#Apply masking to a 2D array
arr2d = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

#Mask: values > 4
mask2d = arr2d > 4
print("2D Mask:\n", mask2d)

#Filtered values (flattened)
print("Filtered from 2D:", arr2d[mask2d])  # Output: [5 6 7 8 9]

#My Learning Note:
    #Boolean masks are arrays of True/False values.
    #Use masks to filter elements that match a condition.
    #Combine conditions with & (and), | (or), ~ (not).
    #Works with 1D and 2D arrays.