import streamlit as st
import pandas as pd
import numpy as np

# Title
st.title("Hello, Streamlit")

# Text
st.text("Vedant")

# Name input
NAME = st.text_input("Enter your name:")

# Button
if st.button("Greets"):
    st.success(f"Hello {NAME}")

# DataFrame
df = pd.DataFrame(
    np.random.randn(10, 2),
    columns=["a", "b"]
)

st.write(df)

# Line Chart
st.line_chart(df)

# Bar Chart
st.bar_chart(df)

# Image
st.title("Image")

IMAGE_PATH = r"C:\Users\ACER\OneDrive\사진\Screenshots\Screenshot 2026-03-03 141015.png"

try:
    st.image(IMAGE_PATH)
except Exception as e:
    st.error(f"Error loading image: {e}")

# Video
st.title("Video")

st.video("https://youtu.be/7UqiwMDEcUI")

# Form
st.title("Welcome to sample form!")

st.text_input("Enter full name")
st.text_input("Enter College Registration ID")

box = st.checkbox("Are you Student")

if box:
    branch = st.selectbox(
        "Enter your Branch",
        ["ETC", "EE", "ME", "CV", "CSE", "CSD", "CTECH"]
    )
else:
    current_status = st.radio(
        "Current Status",
        ["Intern", "Associate Professor", "Professor", "PhD holder"]
    )