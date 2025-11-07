#Pandas Feature Engineering Module
#Goal: Create new features from existing columns (numeric, text, date, category)

import pandas as pd
import numpy as np

#Sample DataFrame
data = {
    "Name": ["Harsha Dush", "Bob Lee", "Maya Wijay", "Rani Kotha"],
    "Age": [25, 32, 18, 47],
    "Score": [88, 75, 95, 64],
    "JoinDate": pd.to_datetime(["2023-01-10", "2022-06-15", "2023-03-20", "2021-12-01"]),
    "Department": ["Sales", "HR", "Sales", "IT"]
}
df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

#1. Math-based features
df["Score_z"] = (df["Score"] - df["Score"].mean()) / df["Score"].std()  # Z-score
df["Score_log"] = np.log(df["Score"] + 1)  # Log transform
df["Age_Score_Interaction"] = df["Age"] * df["Score"]  # Feature interaction

#2. Text-based features
df["NameLength"] = df["Name"].str.len()  # Length of name
df["FirstName"] = df["Name"].str.split().str[0]  # Extract first name
df["Has_Smith"] = df["Name"].str.contains("Smith")  # Flag if name contains "Smith"

#3. Date-based features
df["JoinYear"] = df["JoinDate"].dt.year
df["JoinMonth"] = df["JoinDate"].dt.month
df["JoinWeekday"] = df["JoinDate"].dt.day_name()
df["DaysSinceJoin"] = (pd.Timestamp("2025-08-18") - df["JoinDate"]).dt.days

#4. Categorical encoding
df["Dept_Code"] = df["Department"].astype("category").cat.codes  # Label encoding
df_dummies = pd.get_dummies(df["Department"], prefix="Dept")  # One-hot encoding
df = pd.concat([df, df_dummies], axis=1)

#5. Binning
df["AgeGroup"] = pd.cut(df["Age"], bins=[0, 20, 35, 50], labels=["Teen", "Young", "Adult"])

#My Note:
    #Math: z-score, log, interaction
    #Text: length, keyword, split
    #Date: extract parts, time gaps
    #Category: label + one-hot encoding
    #Binning: convert numeric to category
print("\nFeature Engineered DataFrame:\n", df)

    #Z-score: (x - mean) / std
    #Log transform: np.log(x + 1)
    #.str.len(), .str.split(), .str.contains() : text features
    #.dt.year, .dt.day_name() : date features
    #cat.codes : label encoding
    #pd.get_dummies() : one-hot encoding
    #pd.cut() : bin numeric values