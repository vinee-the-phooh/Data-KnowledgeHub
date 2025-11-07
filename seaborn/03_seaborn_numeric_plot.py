#Seaborn Numeric Plots: scatterplot, lineplot, regplot
#Goal: Learn how to visualize relationships and trends between numeric variables
#Compare with Matplotlib and understand why Seaborn uses plt

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

#Step 1: Create sample data
# Example: Sales data over time with advertising budget
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [200, 220, 250, 270, 300, 320],
    "Ad_Budget": [20, 25, 30, 35, 40, 45]
}
df = pd.DataFrame(data)

#1. Scatterplot: Relationship between Ad_Budget and Sales
#Matplotlib version
plt.figure(figsize=(6, 4))
plt.scatter(df["Ad_Budget"], df["Sales"], color="purple")
plt.title("Sales vs Ad Budget (Matplotlib)")
plt.xlabel("Ad Budget ($K)")
plt.ylabel("Sales ($K)")
plt.grid(True)
plt.show()

#Seaborn version
plt.figure(figsize=(6, 4))
sns.scatterplot(x="Ad_Budget", y="Sales", data=df, color="blue", s=100)
plt.title("Sales vs Ad Budget (Seaborn)")
plt.xlabel("Ad Budget ($K)")
plt.ylabel("Sales ($K)")
plt.grid(True)
plt.show()

#2. Lineplot: Trend of Sales over Months
#Matplotlib version
plt.figure(figsize=(6, 4))
plt.plot(df["Month"], df["Sales"], marker="o", linestyle="-", color="green")
plt.title("Monthly Sales Trend (Matplotlib)")
plt.xlabel("Month")
plt.ylabel("Sales ($K)")
plt.grid(True)
plt.show()

#Seaborn version
plt.figure(figsize=(6, 4))
sns.lineplot(x="Month", y="Sales", data=df, marker="o", color="darkgreen")
plt.title("Monthly Sales Trend (Seaborn)")
plt.xlabel("Month")
plt.ylabel("Sales ($K)")
plt.grid(True)
plt.show()

#3. Regplot: Scatterplot with regression line
#Matplotlib version (manual regression line)
import numpy as np
plt.figure(figsize=(6, 4))
plt.scatter(df["Ad_Budget"], df["Sales"], color="orange")
m, b = np.polyfit(df["Ad_Budget"], df["Sales"], 1)
plt.plot(df["Ad_Budget"], m * df["Ad_Budget"] + b, color="red")
plt.title("Sales vs Ad Budget with Regression (Matplotlib)")
plt.xlabel("Ad Budget ($K)")
plt.ylabel("Sales ($K)")
plt.grid(True)
plt.show()

#Seaborn version
plt.figure(figsize=(6, 4))
sns.regplot(x="Ad_Budget", y="Sales", data=df, color="orange", line_kws={"color": "red"})
plt.title("Sales vs Ad Budget with Regression (Seaborn)")
plt.xlabel("Ad Budget ($K)")
plt.ylabel("Sales ($K)")
plt.grid(True)
plt.show()

