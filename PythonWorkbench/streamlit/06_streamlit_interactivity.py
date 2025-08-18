#Streamlit Interactivity Module
#Goal: Learn how to add interactive widgets to your app

import streamlit as st

#Title and Description
st.title("Interactive Widgets in Streamlit")
st.subheader("We will make our app dynamic with buttons, sliders, checkboxes, and more")

#1. Button
if st.button("Click Me"):
    st.success("You clicked the button!")

#2. Checkbox
show_text = st.checkbox("Show extra info")
if show_text:
    st.info("This is additional information shown when checkbox is selected.")

#3. Radio Buttons
color = st.radio("Choose a color:", ["Red", "Green", "Blue"])
st.write(f"You selected: **{color}**")

#4. Slider
score = st.slider("Select your score:", min_value=0, max_value=100, value=50)
st.write(f"Your score is: **{score}**")

#5. Selectbox
language = st.selectbox("Choose a programming language:", ["Python", "Java", "C++", "JavaScript"])
st.write(f"You selected: **{language}**")
