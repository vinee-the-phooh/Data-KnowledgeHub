#Streamlit Layout Module
#Goal: Organize 0ur app using columns, containers, and expanders
#Explanation:
    #columns: split screen horizontally
    #container: group elements together
    #expander: collapsible section for extra info

import streamlit as st
import pandas as pd

#Title and Description
st.title("Streamlit Layout Techniques")
st.subheader("Use columns, containers, and expanders for clean dashboards")

#Sample Data
df = pd.DataFrame({
    "Name": ["Harsha", "Vineetha", "Sucha", "Maya"],
    "Score": [85, 92, 78, 88]
})

#1.Columns
col1, col2 = st.columns(2)
with col1:
    st.metric("Average Score", round(df["Score"].mean(), 2))
with col2:
    st.metric("Max Score", df["Score"].max())

#2.Container
with st.container():
    st.write("Full Data Table:")
    st.dataframe(df)

#3.Expander
with st.expander("🔍 Show Summary Stats"):
    st.write(df.describe())
