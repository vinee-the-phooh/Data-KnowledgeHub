#Matplotlib Multiple Line Plot Module
#Goal: Compare multiple trends using different lines, colors, and legends

import matplotlib.pyplot as plt

#Step 1: Prepare multiple sets of data
# Example: Comparing sales of 3 products over 5 months
months = [1, 2, 3, 4, 5] # X-axis: months

product_A = [10, 15, 20, 25, 30] # Y-axis: sales of Product A
product_B = [12, 18, 22, 28, 35] # Y-axis: sales of Product B
product_C = [8, 13, 19, 24, 29] # Y-axis: sales of Product C

#Step 2: Plot each line with a label and style
plt.plot(months, product_A, label="Product A", color="blue", linestyle="-")
plt.plot(months, product_B, label="Product B", color="green", linestyle="--")
plt.plot(months, product_C, label="Product C", color="red", linestyle=":")

#Step 3: Add chart title and axis labels
plt.title("Monthly Sales Comparison")
plt.xlabel("Month")
plt.ylabel("Sales")

#Step 4: Add legend to identify each line
plt.legend()  # Shows labels for each line

#Step 5: Add grid for readability
plt.grid(True)

#Step 6: Show the plot
plt.show()

