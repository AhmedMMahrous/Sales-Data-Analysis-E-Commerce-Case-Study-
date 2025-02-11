import streamlit as st
from PIL import Image

def home():
    # Set the title of the web app
    st.title("📊 Sales Data Analysis: E-Commerce Case Study")

    # Load and display an image (Ensure 'pic.jpg' is in the correct directory)
    image = Image.open('E:/My Projects/Machine Learning Projects/Sales Analysies/images/pic.jpg')
    st.image(image, caption="E-Commerce Sales Analysis" , use_container_width = False)

    # Introduction
    st.write("""
    Welcome to the **Sales Data Analysis website**! 📈  
    In this guide, we'll explore e-commerce sales data, uncover insights, and optimize sales strategies.
    """)

    # Objectives
    st.markdown("### 🎯 Objectives:")
    st.markdown("""
    1️⃣ **Importing Libraries and Dataset** – Setting up tools and data.  
    2️⃣ **Basic Data Exploration** – Understanding the dataset.  
    3️⃣ **Data Cleaning** – Preparing data for analysis.  
    4️⃣ **Exploratory Data Analysis (EDA)** – Answering key questions:
       - 📅 **Which is the best month for sales?**
       - 🏙️ **Which city has the highest order volume?**
       - 📦 **What products sold the most and why?**
       - 📊 **Understanding trends of best-selling products.**
       - 🔄 **Identifying products often sold together.**
    """)

