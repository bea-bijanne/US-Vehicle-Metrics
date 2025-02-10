import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt

# Add title
st.title("Vehicle Analysis Dashboard")

#Load data
try:
    us_vehicles = pd.read_csv('../vehicles_us.csv')
except FileNotFoundError:
    st.error("CSV file not found")
    st.stop()

# Define oxidation risk levels based on paint color
def categorize_oxidation(color):
    high_exposure = ["silver", "blue", "red", "green", "yellow", "orange"]
    medium_exposure = ["grey", "brown", "purple", "custom"]
    low_exposure = ["white", "black", "unknown"]

    if color in high_exposure:
        return "High Oxidation Exposure in Sun/Heat in Certain Hot Climates"
    elif color in medium_exposure:
        return "Medium Oxidation Exposure due to Normal Aging Exposure"
    else:
        return "Lower Oxidation Risk"

# Apply categorization to create the oxidation_risk column
us_vehicles['oxidation_risk'] = us_vehicles['paint_color'].apply(categorize_oxidation)
st.write("Oxidation Risk Categories in Dataset:", us_vehicles['oxidation_risk'].unique())

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


# Add checkbox control
show_matrix = st.checkbox("Show Technical Features Matrix", value=True)

# Create scatter matrix
fig_matrix = px.scatter_matrix(us_vehicles,
    dimensions=['fuel', 'odometer', 'transmission', 'cylinders'],
    color='price',
    title='Technical Features Relationship')

st.header("Exploring Relationships Between Technical Features")
if show_matrix:
   st.plotly_chart(fig_matrix)

# Add checkbox control
show_oxidation_impact = st.checkbox("Show Price vs Oxidation Risk by Mileage", value=True)

# Define oxidation risk levels
oxidation_colors = {
    "High Oxidation Risk in Certain Hot Sun/Heat Climates": "red",
    "Medium Oxidation Risk due to Normal Aging Exposure": "orange",
    "Lower Oxidation Risk": "green"
}

# Create scatter plot
fig_oxidation_impact = px.scatter(
 us_vehicles, x='odometer', y='price', color='oxidation_risk',
 title='Price vs Mileage and Oxidation Risk',
 labels={'odometer': 'Mileage (miles)', 'price': 'Price ($)', 'oxidation_risk': 'Oxidation Risk Level'},
 color_discrete_map=oxidation_colors   
)

st.header("Oxidation Exposure and Its Impact on Vehicle Pricing")
if show_oxidation_impact:
    st.plotly_chart(fig_oxidation_impact)
    