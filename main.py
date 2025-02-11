import streamlit as st
import pandas as pd
# Set page configuration (must be the first Streamlit command)
st.set_page_config(page_title="Sales Analysis", layout="wide")

# Now import other modules
from streamlit_option_menu import option_menu
import Home, Analysis, About  # Ensure these files exist
# Sidebar navigation
with st.sidebar:
    app = option_menu(
        menu_title='Sales Analysis',
        options=['Home', 'Analysis', 'About'],
        icons=['house-fill', 'bar-chart-fill', 'info-circle-fill'],
        menu_icon='graph-up',
        default_index=0,
        styles={
            "container": {"padding": "5!important", "background-color": "black"},
            "icon": {"color": "white", "font-size": "23px"},
            "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px", "--hover-color": "blue"},
            "nav-link-selected": {"background-color": "#02ab21"},
        }
    )

# Page navigation
if app == "Home":
    Home.home()  # Ensure Home.py has an `app()` function
elif app == "Analysis":
    Analysis.analysis()
# Ensure Analysis.py has an `app()` function
elif app == "About":
    About.about()  # Ensure About.py has an `app()` function
