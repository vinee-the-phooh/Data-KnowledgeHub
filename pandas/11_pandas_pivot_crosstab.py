#Pandas Pivot & Crosstab Module
#Goal: Reshape and summarize data using pivot and crosstab

import pandas as pd

#Sample DataFrame
data = {
    "Name": ["Harsha", "Bob", "Vinee", "Rani", "Bob"],
    "Department": ["Sales", "HR", "Sales", "HR", "Sales"],
    "Score": [88, 75, 95, 82, 79]
}
df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

#Pivot: reshape data (Name as index, Department as columns)
pivoted = df.pivot(index="Name", columns="Department", values="Score")
print("\nPivoted DataFrame:\n", pivoted)

#Pivot Table: aggregate values (mean score per Name/Dept)
pivot_table = pd.pivot_table(df, index="Name", columns="Department", values="Score", aggfunc="mean")
print("\nPivot Table (mean):\n", pivot_table)

#Crosstab: frequency count
crosstab = pd.crosstab(df["Name"], df["Department"])
print("\nCrosstab (count of entries):\n", crosstab)

#Crosstab with normalization
crosstab_norm = pd.crosstab(df["Name"], df["Department"], normalize="index")
print("\nCrosstab (normalized by row):\n", crosstab_norm)

# My Note:
    #pivot() : reshape data (no aggregation)
    #pivot_table() : reshape + aggregate
    #crosstab() : frequency table (like Excel pivot count)
    #normalize : get proportions

    #df.pivot(index, columns, values) : reshape
    #pd.pivot_table(..., aggfunc="mean") : aggregate
    #pd.crosstab(row, col) : frequency count
    #normalize="index"/"columns" : get proportions