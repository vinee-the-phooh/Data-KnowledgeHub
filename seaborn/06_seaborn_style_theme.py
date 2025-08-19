#Seaborn Styling & Themes: set_theme, set_style, set_context, color_palette
#Goal: Learn how to customize the look and feel of Seaborn plots
#Compare with Matplotlib and understand why Seaborn uses plt
#Explanation:
    #set_theme(): sets overall style (background, grid, ticks)
    #set_context(): adjusts font size for different use cases
    #color_palette(): controls color scheme for plots

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

#Step 1: Create sample data
# Example: Monthly sales of two products
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Product A": [100, 120, 130, 150, 160, 170],
    "Product B": [90, 110, 125, 140, 155, 165]
}
df = pd.DataFrame(data)

#Step 2: Set Seaborn theme (affects all plots)
sns.set_theme(style="whitegrid")  # Options: "darkgrid", "whitegrid", "dark", "white", "ticks"

#Step 3: Set context (controls font size and scale)
sns.set_context("notebook")  # Options: "paper", "notebook", "talk", "poster"

#Step 4: Choose a color palette
palette = sns.color_palette("Set2")  # Options: "Set1", "Set2", "pastel", "deep", "muted", etc.

#Step 5: Plot with custom style
plt.figure(figsize=(7, 4))
sns.lineplot(x="Month", y="Product A", data=df, label="Product A", color=palette[0], marker="o")
sns.lineplot(x="Month", y="Product B", data=df, label="Product B", color=palette[1], marker="s")
plt.title("Monthly Sales Comparison")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()
plt.grid(True)
plt.show()

#Matplotlib version (manual styling)
plt.figure(figsize=(7, 4))
plt.plot(df["Month"], df["Product A"], label="Product A", color="blue", marker="o")
plt.plot(df["Month"], df["Product B"], label="Product B", color="green", marker="s")
plt.title("Monthly Sales Comparison (Matplotlib)")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()
plt.grid(True)
plt.show()




