#Pandas Value Counts Module
#Goal: Analyze categorical data using value_counts(), unique(), nunique()

import pandas as pd

#Sample DataFrame
data = {
    "Name": ["Harsha", "Bob", "Maya", "Harsha", "Bob", "Eva"],
    "Department": ["Sales", "HR", "Sales", "HR", "Sales", "IT"]
}
df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

#Count frequency of values
dept_counts = df["Department"].value_counts()
print("\nDepartment frequency:\n", dept_counts)

#Normalize counts (get proportions)
dept_props = df["Department"].value_counts(normalize=True)
print("\nDepartment proportions:\n", dept_props)

#Get unique values
unique_depts = df["Department"].unique()
print("\nUnique departments:\n", unique_depts)

#Count number of unique values
num_unique = df["Department"].nunique()
print("\nNumber of unique departments:", num_unique)

#Sort value counts
sorted_counts = df["Department"].value_counts().sort_index()
print("\nSorted department counts:\n", sorted_counts)

# My Note:
    #.value_counts() : frequency of values
    #normalize=True : get proportions
    #.unique(): list of unique values
    #.nunique(): count of unique values
    #sort_index(): sort by category name

    #.value_counts() : frequency count
    #.value_counts(normalize=True) : proportions
    #.unique(): list of unique values
    #.nunique():  number of unique values
    #.sort_index(): sort by category name