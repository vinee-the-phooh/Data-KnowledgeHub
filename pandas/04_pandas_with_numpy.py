#Pandas with NumPy Module
#Goal: Learn how Pandas and NumPy work together for numeric operations

import numpy as np
import pandas as pd

#Create a NumPy array (2D)
np_arr = np.array([[1, 2],
                   [3, 4]])
print("NumPy Array:\n", np_arr)

#Convert NumPy array to Pandas DataFrame
df = pd.DataFrame(np_arr, columns=["A", "B"])
print("\nDataFrame from NumPy Array:\n", df)

#Access underlying NumPy array from DataFrame
print("\nBack to NumPy Array:\n", df.values)

#Use NumPy functions on Pandas columns
print("\nMean of column A:", np.mean(df["A"]))  # Output: 2.0
print("Standard deviation of column B:", np.std(df["B"]))  # Output: 0.82...

#Apply NumPy function to entire DataFrame
print("\nSquare root of all values:\n", np.sqrt(df))

#Add a new column using NumPy logic
df["Sum"] = np_arr.sum(axis=1)
print("\nDataFrame with 'Sum' column:\n", df)

#Use NumPy to normalize a column (min-max scaling)
col = df["A"]
normalized = (col - np.min(col)) / (np.max(col) - np.min(col))
df["A_normalized"] = normalized
print("\nNormalized 'A' column:\n", df)

#My Note:
    #Pandas is built on NumPy: they work together smoothly
    #You can apply NumPy functions to Pandas columns
    #Use df.values to access raw NumPy array
    #Great for feature engineering and numeric transformations

    #df.values: returns NumPy array from DataFrame
    #np.mean(df["col"]): apply NumPy function to column
    #np.sqrt(df): apply to entire DataFrame
    #Use NumPy for scaling, transformation, math