#Seaborn Categorical Plots: barplot, countplot, boxplot
#Goal: Learn how to visualize categorical data using Seaborn
#Compare with Matplotlib and understand why Seaborn uses plt
#Why Use Seaborn Over Matplotlib?
    #Seaborn handles grouping, aggregation, and styling automatically
    #Matplotlib requires manual data prep (e.g., groupby, value_counts)
    #Seaborn is faster and cleaner for EDA and statistical plots

#Why Do We Still Use plt with Seaborn?
    #Seaborn creates the plot, but plt controls the figure (size, title, labels)
    #plt.show() is needed to display the plot
    #Seaborn is built on top of Matplotlib — they work together


import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

#Step 1: Create sample data
# Example: Survey responses grouped by gender and satisfaction level
data = {
    "Gender": ["Male", "Female", "Female", "Male", "Female", "Male", "Female", "Male"],
    "Satisfaction": ["High", "Low", "Medium", "Medium", "High", "Low", "Medium", "High"],
    "Score": [8, 4, 6, 7, 9, 3, 5, 8]
}
df = pd.DataFrame(data)

#1. Barplot: Average score by gender
#Matplotlib version
plt.figure(figsize=(6, 4))
avg_scores = df.groupby("Gender")["Score"].mean()
plt.bar(avg_scores.index, avg_scores.values, color="skyblue")
plt.title("Average Score by Gender (Matplotlib)")
plt.xlabel("Gender")
plt.ylabel("Average Score")
plt.grid(True)
plt.show()

#Seaborn version
plt.figure(figsize=(6, 4))
sns.barplot(x="Gender", y="Score", data=df, palette="Blues")
plt.title("Average Score by Gender (Seaborn)")
plt.xlabel("Gender")
plt.ylabel("Average Score")
plt.grid(True)
plt.show()

#2. Countplot: Frequency of satisfaction levels
#Matplotlib version
plt.figure(figsize=(6, 4))
counts = df["Satisfaction"].value_counts()
plt.bar(counts.index, counts.values, color="lightgreen")
plt.title("Count of Satisfaction Levels (Matplotlib)")
plt.xlabel("Satisfaction Level")
plt.ylabel("Count")
plt.grid(True)
plt.show()

#Seaborn version
plt.figure(figsize=(6, 4))
sns.countplot(x="Satisfaction", data=df, palette="Greens")
plt.title("Count of Satisfaction Levels (Seaborn)")
plt.xlabel("Satisfaction Level")
plt.ylabel("Count")
plt.grid(True)
plt.show()

#3. Boxplot: Score distribution by satisfaction level
#Matplotlib version
plt.figure(figsize=(6, 4))
groups = [df[df["Satisfaction"] == level]["Score"] for level in df["Satisfaction"].unique()]
plt.boxplot(groups, labels=df["Satisfaction"].unique())
plt.title("Score Distribution by Satisfaction Level (Matplotlib)")
plt.xlabel("Satisfaction Level")
plt.ylabel("Score")
plt.grid(True)
plt.show()

#Seaborn version
plt.figure(figsize=(6, 4))
sns.boxplot(x="Satisfaction", y="Score", data=df, palette="Oranges")
plt.title("Score Distribution by Satisfaction Level (Seaborn)")
plt.xlabel("Satisfaction Level")
plt.ylabel("Score")
plt.grid(True)
plt.show()

