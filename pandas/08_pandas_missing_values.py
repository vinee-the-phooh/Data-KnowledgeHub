#Pandas Missing Values Module
#Goal: Handle missing data using isna(), fillna(), dropna()

import pandas as pd
import numpy as np

#Sample DataFrame with missing values
data = {
    "Name": ["Harsha", "Bob", "Maya", "Rani", "Eva"],
    "Age": [25, np.nan, 18, 47, np.nan],
    "Score": [88, 75, np.nan, 64, 82]
}
df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

#Detect missing values
print("\nMissing values (True = missing):\n", df.isna())

#Count missing values per column
print("\nMissing count per column:\n", df.isna().sum())

#Drop rows with any missing values
df_drop = df.dropna()
print("\nDrop rows with missing values:\n", df_drop)

#Fill missing values with constant
df_fill_const = df.fillna(0)
print("\nFill missing with 0:\n", df_fill_const)

#Fill missing with column mean
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Score"] = df["Score"].fillna(df["Score"].mean())
print("\nFill missing with column mean:\n", df)

#Forward fill (use previous value)
df_ffill = df.fillna(method="ffill")
print("\nForward fill:\n", df_ffill)

#Backward fill (use next value)
df_bfill = df.fillna(method="bfill")
print("\nBackward fill:\n", df_bfill)

#My Note:
    #.isna() : detect missing values
    #.fillna(value): fill with constant or logic
    #.dropna(): remove rows with missing data
    # method="ffill"/"bfill": fill using nearby values

    #df.isna(): True for missing cells
    #df.fillna(value): fill missing with value
    #df.dropna(): remove rows with missing
    #method="ffill"/"bfill": fill using nearby values