#Streamlit Sidebar Module
#Goal: Use sidebar for filters, navigation, and cleaner layout

import streamlit as st
import pandas as pd

#Title and Description
st.title("Sidebar Layout in Streamlit")
st.subheader("Organize filters and inputs using the sidebar")

#Sample Data
data = {
    "Name": ["Harsha", "Vineetha", "Sucha", "Maya", "Rani"],
    "Age": [25, 30, 35, 40, 45],
    "Department": ["Environment", "IT", "Health", "IT", "HR"]
}
df = pd.DataFrame(data)

#Sidebar Widgets
st.sidebar.header("Filter Options")

#Age Filter
min_age = st.sidebar.slider("Minimum Age", 20, 50, 25)
max_age = st.sidebar.slider("Maximum Age", 20, 50, 45)

#Department Filter
selected_dept = st.sidebar.selectbox("Select Department", df["Department"].unique())

#Apply Filters
filtered_df = df[
    (df["Age"] >= min_age) &
    (df["Age"] <= max_age) &
    (df["Department"] == selected_dept)
]

#Show Results
st.write("Filtered Data:")
st.dataframe(filtered_df)
