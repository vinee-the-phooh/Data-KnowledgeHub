#Streamlit EDA Plots Module
#Goal: Add Matplotlib and Seaborn plots to the dashboard

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Title and Description
st.title("EDA Visualizations with Matplotlib & Seaborn")
st.subheader("Explore the data with interactive plots")

#Sample Data
df = pd.DataFrame({
    "Department": ["HR", "IT", "Finance", "IT", "HR", "Finance", "IT"],
    "Salary": [50000, 60000, 55000, 62000, 52000, 58000, 61000],
    "Experience": [2, 5, 3, 6, 2, 4, 5]
})

#Sidebar Filters
st.sidebar.header("Filter Options")
selected_dept = st.sidebar.multiselect("Select Departments", df["Department"].unique(), default=df["Department"].unique())

#Filtered Data
filtered_df = df[df["Department"].isin(selected_dept)]

#1.Bar Plot (Matplotlib)
st.write("Average Salary by Department")
fig1, ax1 = plt.subplots()
avg_salary = filtered_df.groupby("Department")["Salary"].mean()
ax1.bar(avg_salary.index, avg_salary.values, color="skyblue")
ax1.set_ylabel("Average Salary")
st.pyplot(fig1)

#2.Scatter Plot (Seaborn)
st.write("Experience vs Salary")
fig2, ax2 = plt.subplots()
sns.scatterplot(data=filtered_df, x="Experience", y="Salary", hue="Department", ax=ax2)
st.pyplot(fig2)
