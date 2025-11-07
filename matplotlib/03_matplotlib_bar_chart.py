#Matplotlib Bar Chart Module
#Goal: Compare values across categories using vertical bars

import matplotlib.pyplot as plt

#Step 1: Prepare category data
# Example: Sales of different products
products = ["Product A", "Product B", "Product C", "Product D"]  # X-axis: categories
sales = [250, 400, 150, 300]                                     # Y-axis: values

#Step 2: Create a vertical bar chart
plt.bar(products, sales, color="skyblue")  # Draw bars for each product

#Step 3: Add chart title and axis labels
plt.title("Sales by Product") # Title at the top
plt.xlabel("Product")# Label for categories
plt.ylabel("Sales") # Label for values

#Step 4: Add grid lines (horizontal only for bar charts)
plt.grid(axis="y") # Grid lines on Y-axis only

#Step 5: Show the plot
plt.show()
