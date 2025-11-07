#Seaborn Introduction + Comparison with Matplotlib
#Goal: Learn why Seaborn is useful, how it builds on Matplotlib, and how to create basic plots
#Explanation:
    #Matplotlib is the base plotting library in Python — flexible but manual.
    #Seaborn is built on top of Matplotlib — easier, cleaner, and more beautiful.
    #Seaborn works directly with Pandas DataFrames and supports statistical plots.

#Import libraries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#Step 1: Create sample DataFrame
# Example: Student scores grouped by subject
data = {
    "Student": ["Harsha", "Bob", "Rosy", "David", "Eva", "Frank"],
    "Subject": ["Math", "Math", "Science", "Science", "English", "English"],
    "Score": [88, 75, 92, 85, 78, 83]
}
df = pd.DataFrame(data)

#Step 2: Basic bar plot using Matplotlib
plt.figure(figsize=(6, 4))
plt.bar(df["Student"], df["Score"], color="skyblue")
plt.title("Scores by Student (Matplotlib)")
plt.xlabel("Student")
plt.ylabel("Score")
plt.grid(True)
plt.show()

#Step 3: Same plot using Seaborn
# Seaborn automatically handles aesthetics, color, and layout
plt.figure(figsize=(6, 4))
sns.barplot(x="Student", y="Score", data=df, palette="pastel")
plt.title("Scores by Student (Seaborn)")
plt.xlabel("Student")
plt.ylabel("Score")
plt.grid(True)
plt.show()

#What These Graphs Show:
    #Both show student scores using vertical bars
    #Matplotlib requires manual styling (colors, layout)
    #Seaborn adds automatic styling and works directly with DataFrames

