#Matplotlib Pie Chart Module
#Goal: Show proportions of categories as slices of a circle

import matplotlib.pyplot as plt

#Step 1: Prepare category data
#Example: Market share of 4 companies
companies = ["Company A", "Company B", "Company C", "Company D"]
market_share = [40, 25, 20, 15] # Percentages (must add up to 100)

#Step 2: Create a pie chart
plt.pie(market_share,
        labels=companies,# Show category names
        autopct="%1.1f%%", # Show percentage on each slice
        startangle=90, # Rotate chart for better layout
        colors=["gold", "lightblue", "lightgreen", "salmon"]) # Optional colors

#Step 3: Add chart title
plt.title("Market Share Distribution")

#Step 4: Show the plot
plt.show()

