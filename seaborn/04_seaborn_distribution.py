#Seaborn Distribution Plots: histplot, kdeplot
#Goal: Learn how to visualize the distribution (spread) of numeric data
#Compare with Matplotlib and understand why Seaborn uses plt

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#Step 1: Create sample data
#Example: Simulated test scores of 100 students
np.random.seed(42)  # for reproducibility
scores = np.random.normal(loc=70, scale=10, size=100)  # mean=70, std=10
df = pd.DataFrame({"Score": scores})

#1. Histogram: Frequency of score ranges
#Matplotlib version
plt.figure(figsize=(6, 4))
plt.hist(df["Score"], bins=10, color="skyblue", edgecolor="black")
plt.title("Score Distribution (Matplotlib Histogram)")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

#Seaborn version
plt.figure(figsize=(6, 4))
sns.histplot(df["Score"], bins=10, kde=False, color="blue")
plt.title("Score Distribution (Seaborn histplot)")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

#2. KDE Plot: Smooth curve showing distribution shape
#Matplotlib version (manual KDE using scipy)
from scipy.stats import gaussian_kde
kde = gaussian_kde(df["Score"])
x_vals = np.linspace(df["Score"].min(), df["Score"].max(), 100)
plt.figure(figsize=(6, 4))
plt.plot(x_vals, kde(x_vals), color="green")
plt.title("Score Density (Matplotlib KDE)")
plt.xlabel("Score")
plt.ylabel("Density")
plt.grid(True)
plt.show()

#Seaborn version
plt.figure(figsize=(6, 4))
sns.kdeplot(df["Score"], color="darkgreen", fill=True)
plt.title("Score Density (Seaborn kdeplot)")
plt.xlabel("Score")
plt.ylabel("Density")
plt.grid(True)
plt.show()
