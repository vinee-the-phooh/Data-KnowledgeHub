#Matplotlib Histogram Module
#Goal: Visualize the distribution of numeric data using bins

import matplotlib.pyplot as plt

#Step 1: Prepare sample numeric data
# Example: Exam scores of 20 students
scores = [55, 60, 65, 70, 72, 75, 78, 80, 82, 85,
          88, 90, 92, 95, 96, 98, 99, 100, 100, 100]

#Step 2: Create a histogram
# bins = number of groups (ranges) to divide the data
plt.hist(scores, bins=5, color="lightgreen", edgecolor="black")

#Step 3: Add chart title and axis labels
plt.title("Distribution of Exam Scores")  # Title at the top
plt.xlabel("Score Range")  # X-axis: score intervals
plt.ylabel("Number of Students")# Y-axis: frequency count

#Step 4: Add grid lines
plt.grid(True)

#Step 5: Show the plot
plt.show()
