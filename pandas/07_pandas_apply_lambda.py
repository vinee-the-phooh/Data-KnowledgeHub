#Pandas Apply + Lambda Module
#Goal: Use .apply() and lambda for custom logic

import pandas as pd

#Sample DataFrame
data = {
    "Name": ["Harsha", "Bob", "Maya", "Rani"],
    "Age": [25, 32, 18, 47],
    "Score": [88, 75, 95, 64]
}
df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

#Apply function to a column (Score → Grade)
def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "D"

df["Grade"] = df["Score"].apply(grade)
print("\nScore to Grade:\n", df)

#Use lambda for inline logic (Age group)
df["AgeGroup"] = df["Age"].apply(lambda x: "Young" if x < 30 else "Adult")
print("\nAge Group:\n", df)

#Apply to entire row (axis=1)
df["Summary"] = df.apply(lambda row: f"{row['Name']} ({row['Age']} yrs) → {row['Grade']}", axis=1)
print("\nRow Summary:\n", df)

#Apply with math logic (Score squared)
df["ScoreSquared"] = df["Score"].apply(lambda x: x**2)
print("\nScore Squared:\n", df)

#My Note:
    #Use .apply(func) to apply logic

    #df["col"].apply(func) : apply to column
    #df.apply(lambda row: ..., axis=1) : apply to row
    #Use lambda for quick logic: x → x**2, x : "Yes" if x > 10 else "No"