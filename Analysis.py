import streamlit as st
import pandas as pd
import plotly.express as px
# Ensure this function is correctly defined
from Functions import most_month_sale_plotly , city_order , product_sold , Trend , most_often_sold_together



def analysis():
    # Set the title and subtitle
    st.title("📊 Sales Data Analysis")
    st.subheader("🔍 Exploring E-Commerce Sales Trends")

    # Load Data
    @st.cache_data
    def load_data():
        return pd.read_feather("Data/Sales_data.ftr")

    data = load_data()

    # Display the first few rows
    st.write("### 🔹 Sample Data")
    st.dataframe(data.head())

    # Monthly Sales Analysis
    st.subheader("📅 Most Sales by Month")
    st.plotly_chart(most_month_sale_plotly(data))
    
    # Which city has max order?
    st.subheader("📅 Which city has max order?")
    st.plotly_chart(city_order(data ,'Purchase Address'))
    
    # Most Sold Products & Their Prices
    st.subheader("📦 Most Sold Products & Their Prices")
    st.plotly_chart(product_sold(data, 'Product', 'Quantity Ordered','Price Each'))
    
    st.write("### Insights:")
    st.write("1. The top selling product is 'AAA Batteries'.")
    st.write("2. The top selling products seems to have a correlation with the price of the product.")
    st.write("3. The cheaper the product higher the quantity ordered and vice versa.")
    
    st.subheader("📈 Sales Trend of Top 5 Products")
    st.plotly_chart(Trend(data, 'Order Date' ,'Product'))
    
    st.write("### Insights:")
    st.write("Products have been sold more in Oct , Nov , Dec ")
    
    st.subheader("🔗 Frequently Sold-Together Products")
    st.plotly_chart(most_often_sold_together(data, 'Order ID' , 'Product' , 'grouped_products'))
    
    st.write("### Insights:")
    st.write("1. as soon as any Person will bought Iphone , we can recommend him charging cable , wired headphones.")
    st.write("2. as soon as any Person will bought Google phone , we can recommend him USB-c charging cable.")
    st.write("3. This is a very important insight if someone is building recommendation system.")

    



