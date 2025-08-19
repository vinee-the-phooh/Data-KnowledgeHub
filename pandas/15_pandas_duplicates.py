#Pandas Duplicates Module
#Goal: Detect and remove duplicate rows

import pandas as pd

#Sample DataFrame with duplicates
data = {
    "Name": ["Harsha", "Bob", "Maya", "Harsha", "Bob"],
    "Age": [25, 32, 18, 25, 32],
    "Score": [88, 75, 95, 88, 75]
}
df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

#Detect duplicates (entire row)
duplicates = df.duplicated()
print("\nDuplicate rows (True = duplicate):\n", duplicates)

#Detect duplicates based on subset of columns
dup_name_age = df.duplicated(subset=["Name", "Age"])
print("\nDuplicates based on Name and Age:\n", dup_name_age)

#Keep first occurrence, drop others
df_no_dupes = df.drop_duplicates()
print("\nDrop duplicate rows (keep first):\n", df_no_dupes)

#Keep last occurrence
df_keep_last = df.drop_duplicates(keep="last")
print("\nDrop duplicates (keep last):\n", df_keep_last)

#Drop duplicates based on subset
df_subset = df.drop_duplicates(subset=["Name"])
print("\nDrop duplicates by Name (keep first):\n", df_subset)

# My Note:
    #.duplicated() :detect duplicates
    #.drop_duplicates() : remove duplicates
    #subset=["col1", "col2"] : check specific columns
    #keep="first"/"last"/False:control which to keep

    #df.duplicated(): True for duplicate rows
    #df.drop_duplicates() : remove duplicates
    #subset=["col1", "col2"] :check specific columns
    #keep="first"/"last"/False : control which to keep