#Streamlit EDA App Template
#Goal: Build a reusable dashboard for data exploration

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Title and Description
st.title("EDA Dashboard Template")
st.subheader("Upload data, filter, and explore with summary and plots")

#Sidebar: File Upload
st.sidebar.header("Upload Your Data File")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

#Load Data
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("File uploaded successfully!")

    #Sidebar Filters
    st.sidebar.header("Filter Options")
    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    selected_col = st.sidebar.selectbox("Select numeric column for analysis", numeric_cols)

    #Main: Summary Stats
    st.header("Summary Statistics")
    st.write(df.describe())

    #Main: Histogram
    st.header(f"Distribution of {selected_col}")
    fig1, ax1 = plt.subplots()
    sns.histplot(df[selected_col], kde=True, ax=ax1, color="skyblue")
    st.pyplot(fig1)

    #Main: Correlation Heatmap
    st.header("Correlation Matrix")
    fig2, ax2 = plt.subplots()
    sns.heatmap(df[numeric_cols].corr(), annot=True, cmap="coolwarm", ax=ax2)
    st.pyplot(fig2)

else:
    st.info("Please upload a CSV file to begin.")
