# Streamlit Charts Module
#Goal: Create basic charts using built-in Streamlit functions
#Explanation:
    #st.line_chart() : shows trends over time
    #st.bar_chart() : compares values across categories
    #st.area_chart() : like line chart but filled underneath

import streamlit as st
import pandas as pd
import numpy as np

#Title and Description
st.title("Streamlit Built-in Charts")
st.subheader("Visualize data with line, bar, and area charts")

#Sample Data
df = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "Sales": [120, 150, 170, 130, 160],
    "Profit": [30, 45, 50, 35, 40]
})

#Line Chart
st.markdown("###Line Chart: Sales Over Time")
st.line_chart(df.set_index("Month")["Sales"])

#Bar Chart
st.markdown("###Bar Chart: Monthly Profit")
st.bar_chart(df.set_index("Month")["Profit"])

#Area Chart
st.markdown("###Area Chart: Sales and Profit")
st.area_chart(df.set_index("Month"))



