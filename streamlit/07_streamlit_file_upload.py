#Streamlit File Upload Module
#Goal: Let users upload CSV or Excel files and preview the data

import streamlit as st
import pandas as pd

#Title and Description
st.title("Upload CSV or Excel File")
st.subheader("Let users upload files and preview their data")

#File Uploader Widget
uploaded_file = st.file_uploader("Choose a CSV or Excel file", type=["csv", "xlsx"])

#Check if file is uploaded
if uploaded_file is not None:
    try:
        #Read file based on extension
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith(".xlsx"):
            df = pd.read_excel(uploaded_file)

        #Show preview
        st.success("File uploaded successfully!")
        st.write("Preview of uploaded data:")
        st.dataframe(df)

        #Show basic info
        st.write("Shape:", df.shape)
        st.write("Columns:", df.columns.tolist())

    except Exception as e:
        st.error(f"Error reading file: {e}")
else:
    st.info("Please upload a file to continue.")
