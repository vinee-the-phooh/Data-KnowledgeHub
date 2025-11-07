#Seaborn Heatmap: Visualizing correlation and matrix-style data
#Goal: Learn how to create annotated heatmaps using Seaborn
#Compare with Matplotlib and understand why Seaborn uses plt

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#Step 1: Create sample data
# Example: Student performance across subjects
data = {
    "Math": [88, 75, 92, 85, 78, 83],
    "Science": [90, 80, 95, 88, 76, 85],
    "English": [70, 65, 78, 72, 68, 75],
    "History": [60, 58, 65, 62, 55, 63]
}
df = pd.DataFrame(data)

#Step 2: Compute correlation matrix
# Correlation shows how strongly variables are related (range: -1 to +1)
corr_matrix = df.corr()

#1. Heatmap using Matplotlib (manual)
plt.figure(figsize=(6, 5))
plt.imshow(corr_matrix, cmap="coolwarm", interpolation="none")
plt.colorbar()
plt.xticks(ticks=np.arange(len(corr_matrix.columns)), labels=corr_matrix.columns)
plt.yticks(ticks=np.arange(len(corr_matrix.columns)), labels=corr_matrix.columns)
plt.title("Subject Correlation (Matplotlib Heatmap)")
plt.grid(False)
plt.show()

#2. Heatmap using Seaborn
plt.figure(figsize=(6, 5))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Subject Correlation (Seaborn Heatmap)")
plt.show()
