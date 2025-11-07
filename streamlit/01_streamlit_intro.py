#Streamlit Intro Module
#Goal: Understand what Streamlit is and how to build a basic app
#Why Use Streamlit?
    #Easy to build apps with just Python — no HTML/CSS/JS needed
    #Great for sharing results, dashboards, and models
    #Works well with Pandas, Matplotlib, Seaborn, and ML libraries

#Import Streamlit
import streamlit as st

#Step 1: Add a title and description
st.title("Streamlit Introduction")
st.subheader("Build interactive Python apps for data science")
st.markdown("""
Streamlit lets us turn Python scripts into web apps — great for sharing data, models, and dashboards.
""")

#Step 2: Display simple text
st.write("This is a basic Streamlit app. We can add text, charts, widgets, and more!")

#Step 3: Show a sample DataFrame
import pandas as pd
df = pd.DataFrame({
    "Name": ["Harsha", "Buddy", "Lili"],
    "Score": [85, 92, 78]
})
st.write("Sample DataFrame:")
st.dataframe(df)

#Step 4: Add a metric
st.metric(label="Average Score", value=round(df["Score"].mean(), 2))

# What I have learned:
    #I use Streamlit to turn my Python scripts into interactive dashboards. It’s perfect for sharing EDA results or model outputs with non-technical users.

#Explanation:
    #st.title(), st.subheader(), st.markdown(): add text
    #st.write(): display anything (text, data, charts)
    #st.dataframe(): show tables with scroll and sort
    #st.metric(): show key numbers (important number (e.g., average score))