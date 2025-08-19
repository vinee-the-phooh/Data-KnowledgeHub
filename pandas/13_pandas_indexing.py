#Pandas Indexing Module
#Goal: Access rows/columns using loc[], iloc[], and custom index

import pandas as pd

#Sample DataFrame
data = {
    "ID": [101, 102, 103, 104],
    "Name": ["Harsha", "Bob", "Maya", "Rani"],
    "Score": [88, 75, 95, 64]
}
df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

#Set custom index
df.set_index("ID", inplace=True)
print("\nDataFrame with ID as index:\n", df)

#Access row by label (loc)
row_102 = df.loc[102]
print("\nRow with ID 102:\n", row_102)

#Access row by position (iloc)
row_pos_1 = df.iloc[1]
print("\nRow at position 1:\n", row_pos_1)

#Access multiple rows
rows_101_103 = df.loc[[101, 103]]
print("\nRows with ID 101 and 103:\n", rows_101_103)

#Access specific cell
score_maya = df.loc[103, "Score"]
print("\nScore of Maya (ID 103):", score_maya)

#Slice rows by position
slice_rows = df.iloc[1:3]
print("\nSlice rows 1 to 2:\n", slice_rows)

#Add new column using loc
df.loc[:, "Passed"] = df["Score"] >= 70
print("\nAdded 'Passed' column:\n", df)

#My Note:
    #.loc[label] : access by index label
    #.iloc[position] : access by row/column position
    #Use slicing, selection, and assignment with loc/iloc
    #Set custom index for meaningful access

    #.loc[label] : access by index label
    #.iloc[position] : access by position
    #df.loc[:, "col"] : select column
    #df.iloc[1:3] : slice rows by position