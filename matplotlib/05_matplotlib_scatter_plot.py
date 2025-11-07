#Matplotlib Scatter Plot Module
#Goal: Show relationship between two variables using dots

import matplotlib.pyplot as plt

#Step 1: Prepare paired data
# Example: Study hours vs exam scores
study_hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # X-axis: hours studied
exam_scores = [50, 55, 60, 65, 70, 72, 75, 78, 85, 90]# Y-axis: exam scores

#Step 2: Create a scatter plot
plt.scatter(study_hours, exam_scores, color="purple", marker="o")

#Step 3: Add chart title and axis labels
plt.title("Study Hours vs Exam Scores") # Title at the top
plt.xlabel("Hours Studied") # X-axis label
plt.ylabel("Exam Score")# Y-axis label

#Step 4: Add grid lines
plt.grid(True)

#Step 5: Show the plot
plt.show()

