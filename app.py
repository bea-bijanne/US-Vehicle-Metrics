import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt

# Add title
st.title("Vehicle Analysis Dashboard")

#Load data
try:
    us_vehicles = pd.read_csv('vehicles_us.csv')
except FileNotFoundError:
    st.error("CSV file not found")
    st.stop()

# Including controls
show_distribution = st.checkbox("Show Price Distribution", value=True)

# Display visualizations
fig_price = px.histogram(us_vehicles[us_vehicles['price'] < 200000],
                             x='price',
                             color='type',
                             nbins=50,
                             title='Vehicle Price Distribution by Type',
labels={'price': 'Price ($)', 'type': 'Vehicle Type'},
height=600)

st.header("Price Ranges Across Vehicle Categories")
if show_distribution:
    st.plotly_chart(fig_price)

# Add scatterplot
show_scatter = st.checkbox("Show Price vs Mileage", value=True)
fig_scatter = px.scatter(us_vehicles[us_vehicles['price'] < 200000],
                             x='odometer',
                             y='price',
                             color='type',
                             title='Mileage Impact on Price Across Vehicle Types',
labels={'price': 'Price ($)', 'odometer': 'Mileage (miles)',
        'type': 'Vehicle Type'},
height=600)

st.header("Price Depreciation by Mileage for Used Cars")
if show_scatter:
    st.plotly_chart(fig_scatter)


# Add checkbox control scatter matrix
show_matrix = st.checkbox("Show Technical Features Matrix", value=True)

# Create scatter matrix
fig_matrix = px.scatter_matrix(us_vehicles,
    dimensions=['fuel', 'odometer', 'transmission', 'cylinders'],
    color='price',
    title='Technical Features Relationship')

st.header("Exploring Relationships Between Technical Features")
if show_matrix:
   st.plotly_chart(fig_matrix)
    
