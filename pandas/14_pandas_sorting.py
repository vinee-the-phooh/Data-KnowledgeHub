#Pandas Sorting Module
#Goal: Sort rows and columns by values or index

import pandas as pd

#Sample DataFrame
data = {
    "Name": ["Alice", "Bob", "Harsha", "Dayana"],
    "Age": [25, 32, 18, 47],
    "Score": [88, 75, 95, 64]
}
df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

#Sort by Score (ascending)
sorted_score = df.sort_values("Score")
print("\nSorted by Score (ascending):\n", sorted_score)

#Sort by Score (descending)
sorted_score_desc = df.sort_values("Score", ascending=False)
print("\nSorted by Score (descending):\n", sorted_score_desc)

#Sort by multiple columns (Score then Age)
multi_sort = df.sort_values(by=["Score", "Age"])
print("\nSorted by Score then Age:\n", multi_sort)

#Sort by index
df_indexed = df.set_index("Name")
sorted_index = df_indexed.sort_index()
print("\nSorted by index (Name):\n", sorted_index)

#Sort columns alphabetically
sorted_cols = df[sorted(df.columns)]
print("\nSorted columns alphabetically:\n", sorted_cols)

#My Note:
    #sort_values("col"): sort by column
    #ascending=False: descending order
    #sort_values(by=[...]) : multi-column sort
    #sort_index() : sort by index
    #sorted(df.columns): sort column names

    #df.sort_values("col"):  sort by column
    #df.sort_values(by=["col1", "col2"]):  multi-column sort
    #df.sort_index() : sort by index
    #sorted(df.columns) : alphabetically sort columns