#Streamlit Model Input Module
#Goal: Create input widgets for ML prediction and show results

import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

#Title and Description
st.title("ML Model Prediction Interface")
st.subheader("Enter values and get predictions from a simple model")

#Sample Model (Linear Regression)
#Train a dummy model for demo purposes
X_train = np.array([[1], [2], [3], [4], [5]])
y_train = np.array([100, 150, 200, 250, 300])
model = LinearRegression().fit(X_train, y_train)

#Sidebar Inputs
st.sidebar.header("Input Features")
feature_value = st.sidebar.slider("Feature Value (e.g., Years of Experience)", 0, 10, 5)

#Predict Button
if st.sidebar.button("Predict"):
    input_array = np.array([[feature_value]])
    prediction = model.predict(input_array)[0]
    st.success(f"Predicted Output: {round(prediction, 2)}")

#Show Model Info
with st.expander("📘 Model Details"):
    st.write("Model: Linear Regression")
    st.write("Formula: y = a * x + b")
    st.write(f"Coefficient (a): {round(model.coef_[0], 2)}")
    st.write(f"Intercept (b): {round(model.intercept_, 2)}")