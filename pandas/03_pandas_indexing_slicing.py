#Pandas Indexing & Slicing Module
#Goal: Learn how to access rows, columns, and values using loc, iloc, and slicing

import pandas as pd

#Create a sample DataFrame
data = {
    "Name": ["Harsha", "Bob", "Amara", "Nayana"],
    "Age": [25, 30, 35, 40],
    "City": ["Sydney", "Melbourne", "Brisbane", "Perth"]
}
df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

#Access a single column
print("\nColumn 'Name':\n", df["Name"])

#Access multiple columns
print("\nColumns 'Name' and 'City':\n", df[["Name", "City"]])

#Access a single row by index (label-based)
    # Accessing a single row using label-based indexing with .loc[]
    # .loc[] is used for label-based access, not position-based.
    # In this case, since the DataFrame uses default integer index labels (0, 1, 2, ...),
    # df.loc[2] accesses the row with label '2' — which happens to be the third row.
    # This works only because the index labels are integers by default.
    # If the index were changed to custom labels (e.g., strings like "A", "B", "C"),
    # then df.loc[2] would raise an error because label '2' wouldn't exist.
    # For position-based access (i.e., third row regardless of label), use df.iloc[2] instead.
print("\nRow at index 2 using loc:\n", df.loc[2])

#Access a single row by position (number-based)
print("\nRow at position 2 using iloc:\n", df.iloc[2])

#Slice rows (first 2 rows)
print("\nFirst 2 rows:\n", df[:2])

#Access specific value: row 1, column 'City'
print("\nValue at row 1, column 'City':", df.loc[1, "City"])

#Modify a value
df.loc[0, "Age"] = 26
print("\nModified Age for Alice:\n", df)

#Boolean filtering: people older than 30
print("\nAge > 30:\n", df[df["Age"] > 30])

# My Note:
    #df["col"]: access column
    #df.loc[row_index]: access row by label
    #df.iloc[row_position]: access row by number
    #df.loc[row, col]: access specific value
    #df[row_slice]: slice rows

    #loc: label-based access (row index name)
    #iloc: position-based access (row number)
    #df["col"]: column access
    #df[row_slice]: slice rows like a list