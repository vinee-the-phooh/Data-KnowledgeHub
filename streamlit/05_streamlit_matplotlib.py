#Streamlit + Matplotlib/Seaborn Module
#Goal: Embed custom plots using Matplotlib and Seaborn
#Explanation:
    #Matplotlib : low-level, customizable plotting library
    #Seaborn : high-level, beautiful plots built on Matplotlib
    #st.pyplot(fig) : display any Matplotlib figure in Streamlit

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Title and Description
st.title("Custom Charts with Matplotlib & Seaborn")
st.subheader("Use advanced plotting libraries inside Streamlit")

#Sample Data
df = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "Sales": [120, 150, 170, 130, 160],
    "Profit": [30, 45, 50, 35, 40]
})

#Matplotlib Line Plot
st.markdown("###Matplotlib Line Plot: Sales Over Time")
fig1, ax1 = plt.subplots()
ax1.plot(df["Month"], df["Sales"], marker='o', color='blue')
ax1.set_title("Monthly Sales")
ax1.set_xlabel("Month")
ax1.set_ylabel("Sales")
st.pyplot(fig1)

#Seaborn Bar Plot
st.markdown("###Seaborn Bar Plot: Monthly Profit")
fig2, ax2 = plt.subplots()
sns.barplot(x="Month", y="Profit", data=df, ax=ax2, palette="viridis")
ax2.set_title("Monthly Profit")
st.pyplot(fig2)


