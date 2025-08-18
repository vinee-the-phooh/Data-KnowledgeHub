#Streamlit Text & Input Widgets
#Goal: Learn how to display text and collect user input

#Explanation:
    #st.title(), st.subheader(), st.markdown() : show formatted text
    #t.text_input() : single-line input
    #st.text_area() : multi-line input
    #st.code() : show code blocks
    #st.divider() : horizontal line for layout
    #st.success(), st.info() : show colored messages

import streamlit as st

#Title and Subheader
st.title("Text & Input Widgets in Streamlit")
st.subheader("Display information and collect user input")

#Markdown for formatted text (simple way to format text (like HTML but easier))
st.markdown("""
###Markdown Basics
We can use markdown to format text:
- **Bold**
- *Italic*
- `Code`
- [Links](https://streamlit.io)
""")

#Plain text
st.text("This is plain text — no formatting.")

#Code block
st.code("print('Hello, Streamlit!')", language='python')

#Divider
st.divider()

#User Input: Text box
name = st.text_input("Enter your name:")

#User Input: Text area
feedback = st.text_area("Share your feedback:")

#Display input
if name:
    st.success(f"Welcome, {name}!")

if feedback:
    st.info("Thanks for your feedback!")


