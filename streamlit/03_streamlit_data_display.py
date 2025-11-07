#Streamlit Data Display Module
#Goal: Learn how to show data using tables, metrics, and JSON
#Explanation:
    #st.dataframe() : scrollable, sortable table
    #st.table() : static table (no scroll or sort)
    #st.metric() : highlight key numbers (e.g., average, total)
    #st.json() : show structured data (like dictionaries)

import streamlit as st
import pandas as pd
import numpy as np

#Title and Description
st.title("Displaying Data in Streamlit")
st.subheader("Use tables, metrics, and JSON to present data clearly")

#Sample DataFrame
data = {
    "Name": ["Harsha", "Amara", "Nayana"],
    "Score": [85, 92, 78],
    "Passed": [True, True, False]
}
df = pd.DataFrame(data)

#Display as interactive table
st.dataframe(df, use_container_width=True)

#Display as static table
st.table(df)

#Show key metric
average_score = round(df["Score"].mean(), 2)
st.metric(label="Average Score", value=average_score)

#Display JSON-style data
student_info = {
    "class": "Data Science 101",
    "students": len(df),
    "average_score": average_score
}
st.json(student_info)







