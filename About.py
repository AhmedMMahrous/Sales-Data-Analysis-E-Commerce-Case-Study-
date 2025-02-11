import streamlit as st

def about():
    st.title("About Me")

    # Add profile picture
    st.image("E:/My Projects/Machine Learning Projects/Sales Analysies/images/me.jpeg", width=300)  # Replace with your image file

    # Introduction
    st.write("""
    **Hello! I'm a Data Analyst.**  
    I specialize in analyzing business data using Power BI, Flourish Studio, and Python.  
    My expertise includes data visualization, dashboards, and predictive analytics.
    """)

    # Contact Information & Links
    st.write("### Connect with me:")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://www.linkedin.com/in/ahmed-mohamed-mahrous-19304517b/)")

    with col2:
        st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-Follow-black)](https://github.com/AhmedMMahrous)")

    with col3:
        st.markdown("[![Fiverr](https://img.shields.io/badge/Fiverr-Hire-green)](https://www.fiverr.com/s/pd5ABrN)")

    # Skills Section
    st.write("### My Skills")
    st.markdown("""
    - 📊 **Power BI, Flourish Studio** - Dashboard design & data visualization  
    - 🧠 **Machine Learning** - Predictive modeling & Time Series Analysis 
    - 🛠 **Data Cleaning** - Handling missing values, outliers & transformation  
    - 🏆 **Freelancing Experience** - Working with businesses to generate insights
    """)

