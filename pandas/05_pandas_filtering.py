#Pandas Filtering Module
#Goal: Learn how to filter rows using conditions and Boolean logic

import pandas as pd

#Sample DataFrame
data = {
    "Name": ["Harsha", "Bob", "Maya", "Amara", "Eva"],
    "Age": [25, 32, 18, 47, 29],
    "Score": [88, 75, 95, 64, 82]
}
df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

#Filter rows where Age > 30
age_filter = df[df["Age"] > 30]
print("\nAge > 30:\n", age_filter)

#Filter rows where Score >= 80
score_filter = df[df["Score"] >= 80]
print("\nScore >= 80:\n", score_filter)

#Combine conditions (AND)
combined_and = df[(df["Age"] > 25) & (df["Score"] > 80)]
print("\nAge > 25 AND Score > 80:\n", combined_and)

#Combine conditions (OR)
combined_or = df[(df["Age"] < 20) | (df["Score"] < 70)]
print("\nAge < 20 OR Score < 70:\n", combined_or)

#Negation (~)
not_high_score = df[~(df["Score"] > 85)]
print("\nNOT Score > 85:\n", not_high_score)

#Filter using .isin()
names = ["Alice", "Eva"]
name_filter = df[df["Name"].isin(names)]
print("\nName is Alice or Eva:\n", name_filter)

#Filter using .between()
age_range = df[df["Age"].between(20, 30)]
print("\nAge between 20 and 30:\n", age_range)

# My Note:
    #Use df[condition] to filter rows
    #Combine conditions with & (AND), | (OR), ~ (NOT)
    #Use .isin() for list-based filtering
    #Use .between() for range filtering

    #df[df["col"] > value] : basic filtering
    #& → AND, | → OR, ~ : NOT
    #df[df["col"].isin([...])] : match list of values
    #df[df["col"].between(start, end)] : range filtering