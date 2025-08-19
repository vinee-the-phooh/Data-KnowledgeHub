#Pandas Introduction Module
#Goal: Understand Pandas DataFrame vs NumPy Array
#Why we use Pandas for EDA and modeling

import numpy as np
import pandas as pd

#Create a NumPy array (just numbers, no labels)
np_arr = np.array([[1, 2],
                   [3, 4]])
print("NumPy Array:\n", np_arr)

#Convert NumPy array to Pandas DataFrame
#Add column names for better readability
df = pd.DataFrame(np_arr, columns=["A", "B"])
print("\nPandas DataFrame:\n", df)

#Access underlying NumPy array from DataFrame
#df.values returns the raw array (without labels)
print("\nBack to NumPy Array:\n", df.values)

#Use NumPy functions on Pandas columns
#Pandas columns behave like NumPy arrays
print("\nMean of column A:", np.mean(df["A"]))  # Output: 2.0

#What is a NumPy Array?
    #A grid of numbers (1D, 2D, etc.)
    #Fast and memory-efficient
    #No labels (just positions)

#What is a Pandas DataFrame?
    #A table with rows and columns
    #Each column has a name (label)
    #Can hold numbers, text, dates, etc.
    #Easier to read and work with than raw arrays

#Why use Pandas for EDA (Exploratory Data Analysis)?
    #Clear column names : easier to understand
    #Built-in functions for summary, filtering, grouping
    #Handles missing data (NaN) gracefully
    #Works well with CSV, Excel, and other file formats

#Why use Pandas for Modeling?
#Clean structure : easy to select features and targets
#Compatible with scikit-learn, statsmodels, etc.
#Easy to preprocess: scaling, encoding, splitting

#My Note:
    #NumPy = fast arrays (no labels)
    #Pandas = labeled tables (great for real-world data)
    #Use Pandas for EDA and modeling: readable, flexible, powerful

    #NumPy Array: fast, unlabeled, numeric
    #Pandas DataFrame: labeled, readable, flexible
    #df.values: returns raw NumPy array from DataFrame