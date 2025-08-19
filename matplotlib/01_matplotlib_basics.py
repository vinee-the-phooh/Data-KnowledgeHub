#Matplotlib Basics Module
#Goal: Learn how to create a simple line plot with labels, title, and grid

#Import the plotting library
import matplotlib.pyplot as plt

#Step 1: Prepare sample data
x = [1, 2, 3, 4, 5]           
y = [10, 20, 25, 30, 40]      

#Step 2: Create a basic line plot
plt.plot(x, y)                # Draw a line connecting the points

#Step 3: Add chart title and axis labels
plt.title("Basic Line Plot") # Title shown at the top
plt.xlabel("X-axis (Time)") # Label for horizontal axis
plt.ylabel("Y-axis (Value)") # Label for vertical axis

#Step 4: Add grid lines for better readability
plt.grid(True) # Shows horizontal and vertical grid lines

#Step 5: Display the plot
plt.show() # Opens a window with the chart
