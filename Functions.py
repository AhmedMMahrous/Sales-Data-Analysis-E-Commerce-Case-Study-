import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# 📅 Most Sales by Month
def most_month_sale_plotly(data):
    """Generates a bar chart showing total sales per month."""
    data = data.copy()
    
    # Convert date column and filter valid rows
    data['Order Date'] = pd.to_datetime(data['Order Date'], errors='coerce')
    data = data.dropna(subset=['Order Date'])
    
    # Extract month
    data['Month'] = data['Order Date'].dt.month
    data['Quantity Ordered'] = pd.to_numeric(data['Quantity Ordered'], errors='coerce')
    data['Price Each'] = pd.to_numeric(data['Price Each'], errors='coerce')
    
    # Compute total sales
    data["Sales"] = data["Quantity Ordered"] * data["Price Each"]
    sales_by_month = data.groupby('Month', as_index=False)['Sales'].sum()

    # Create bar chart
    fig = px.bar(
        sales_by_month, x='Month', y='Sales', 
        title="📅 Best Month for Sales", 
        labels={'Month': 'Month', 'Sales': 'Total Sales'}, 
        color='Sales', color_continuous_scale='viridis'
    )
    return fig


# 🏙️ City-wise Order Distribution
def city_order(data, col):
    """Generates a pie chart showing the city-wise order distribution."""
    data = data.copy()
    data = data.dropna(subset=[col])

    # Extract city names safely
    def extract_city(address):
        parts = address.split(',')
        return parts[1].strip() if len(parts) > 1 else "Unknown"

    data['City'] = data[col].apply(extract_city)

    # Remove "Unknown" cities
    data = data[data['City'] != "Unknown"]

    city_counts = data['City'].value_counts().reset_index()
    city_counts.columns = ['City', 'Count']

    fig = px.pie(
        city_counts, values='Count', names='City', 
        title='🏙️ City-wise Order Distribution', 
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    return fig


# 📦 Most Sold Products & Their Prices
def product_sold(data, col1, col2, col3):
    """Generates an interactive bar and line chart using Plotly to analyze the most sold products and their average price."""
    data = data.copy()

    # Convert columns to numeric
    data[col2] = pd.to_numeric(data[col2], errors='coerce')
    data[col3] = pd.to_numeric(data[col3], errors='coerce')

    # Drop missing values
    data = data.dropna(subset=[col2, col3])

    # Aggregate sales and mean price
    product_sold = data.groupby(col1, as_index=False).agg({
        col2: 'sum', 
        col3: 'mean'
    })

    # Sort by total quantity sold
    product_sold = product_sold.sort_values(by=col2, ascending=False)

    # Create Plotly figure
    fig = go.Figure()

    # Add bar chart for total quantity sold
    fig.add_trace(go.Bar(
        x=product_sold[col1], 
        y=product_sold[col2],
        name="Total Quantity Sold",
        marker=dict(color='#84B026'),
        yaxis="y1"
    ))

    # Add line chart for average price
    fig.add_trace(go.Scatter(
        x=product_sold[col1], 
        y=product_sold[col3],
        name="Average Price ($)",
        mode="lines+markers",
        marker=dict(color='#217373'),
        yaxis="y2"
    ))

    # Update layout
    fig.update_layout(
        title="📦 Most Sold Products & Their Prices",
        xaxis=dict(title="Product Name", tickangle=45),
        yaxis=dict(title="Total Quantity Sold", side="left"),
        yaxis2=dict(title="Average Price ($)", overlaying="y", side="right"),
        legend=dict(x=0.1, y=1.1),
        template="plotly_white"
    )
    return fig


# 📈 Trend of Top 5 Sold Products
def Trend(data, col1, col2):
    """Visualizes the trend of the top 5 most sold products over months using Plotly."""
    data = data.copy()

    # Drop duplicates & missing values
    data = data.drop_duplicates().dropna()

    # Extract month from the date column
    data['Month'] = pd.to_datetime(data[col1], errors='coerce').dt.month
    data = data.dropna(subset=['Month'])
    data['Month'] = data['Month'].astype(int)

    # Identify top 5 most sold products
    top_products = data[col2].value_counts().nlargest(5).index
    filtered_data = data[data[col2].isin(top_products)]

    # Aggregate sales count per product per month
    pivot = filtered_data.groupby(['Month', col2]).size().reset_index(name='Count')

    # Create interactive line chart using Plotly
    fig = px.line(
        pivot, x='Month', y='Count', color=col2,
        markers=True,
        title="📈 Trend of Top 5 Most Sold Products",
        labels={'Month': "Month", 'Count': "Sales Count", col2: "Product Name"},
        template="plotly_white"
    )

    # Customize layout
    fig.update_xaxes(tickmode='array', tickvals=list(range(1, 13)), title="Month")
    fig.update_yaxes(title="Number of Sales")

    return fig


# 🔗 Most Frequently Sold-Together Products
def most_often_sold_together(data, col1, col2, col3):
    """Visualizes the top 5 most frequently sold-together product combinations using Plotly."""
    data = data.copy()

    # Identify duplicated Order IDs
    duplicated_orders = data[data[col1].duplicated(keep=False)]

    # Group products by Order ID into a single string
    grouped_products = duplicated_orders.groupby(col1)[col2].apply(lambda x: ', '.join(x)).reset_index()
    grouped_products.rename(columns={col2: 'grouped_products'}, inplace=True)

    # Merge grouped products back with original data
    merged_data = duplicated_orders.merge(grouped_products, how='left', on=col1)

    # Remove duplicate Order IDs
    unique_combinations = merged_data.drop_duplicates(subset=[col1])

    # Get top 5 most frequent product combinations
    top_combinations = unique_combinations[col3].value_counts().nlargest(5)

    # Create a DataFrame for visualization
    combinations_df = pd.DataFrame({
        'Combination': top_combinations.index,
        'Count': top_combinations.values
    })

    # Create interactive pie chart using Plotly
    fig = px.pie(
        combinations_df, values='Count', names='Combination',
        title="🔗 Most Frequently Sold-Together Products",
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    return fig
