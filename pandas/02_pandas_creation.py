#Pandas DataFrame Creation Module
#Goal: Learn how to create DataFrames from lists, dictionaries, and NumPy arrays

import numpy as np
import pandas as pd

#1. From a Python dictionary
#Keys become column names
#Values become column data
data_dict = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["Sydney", "Melbourne", "Brisbane"]
}
df_dict = pd.DataFrame(data_dict)
print("DataFrame from Dictionary:\n", df_dict)

#2. From a list of lists (rows)
#Provide column names separately
data_list = [[101, "Math"], [102, "Science"], [103, "History"]]
df_list = pd.DataFrame(data_list, columns=["ID", "Subject"])
print("\nDataFrame from List of Lists:\n", df_list)

#3. From a NumPy array
np_arr = np.array([[1.5, 2.5], [3.5, 4.5]])
df_np = pd.DataFrame(np_arr, columns=["X", "Y"])
print("\nDataFrame from NumPy Array:\n", df_np)

#4. From a list of dictionaries (each dict = row)
data_rows = [
    {"Product": "Pen", "Price": 1.2},
    {"Product": "Notebook", "Price": 2.5},
    {"Product": "Eraser", "Price": 0.5}
]
df_rows = pd.DataFrame(data_rows)
print("\nDataFrame from List of Dicts:\n", df_rows)

#My Note:
    #Use pd.DataFrame() to create tables from different sources
    #Dictionary: columns from keys
    #List of lists: rows, need column names
    #NumPy array: fast numeric data
    #List of dicts: flexible row-wise structure

    #pd.DataFrame(dict): columns from keys
    #pd.DataFrame(list, columns=[]): rows from list
    #pd.DataFrame(np_array): fast numeric table
    #pd.DataFrame([dict1, dict2]): row-wise data