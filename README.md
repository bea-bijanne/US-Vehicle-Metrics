# US-Vehicle-Metrics
This project develops an interactive web application for analyzing and visualizing **US vehicle data** using **Python** and **Streamlit**. The application provides **dynamic insights into vehicle pricing trends, mileage impact, fuel type, and technical attributes** through interactive charts and filters.

## Key features include: 
- Price distribution visualization - Understand market pricing trends and anomalies
An interactive histogram that illustrates how vehicle prices are distributed across the dataset. This feature helps buyers understand price distribution within specific vehicle categories, while enabling sellers to strategically price their vehicles by comparing them to similar listings. The chart provides insights into price ranges, common price points, and potential pricing anomalies within the used car market. It showcases how factors such as model year, color,  and technical features influence overall pricing trends and market valuation 

- Price vs mileage analysis - Explore how odometer readings affect vehicle value
An interactive scatter plot visualization that examines the relationship between mileage (odometer readings) and vehicle price across different vehicle types. This feature helps buyers and sellers understand how higher or lower mileage affects pricing trends within the used car market. By categorizing vehicles by type, the chart provides insights into price depreciation patterns, outliers, and potential value retention based on mileage

- Technical features comparison - Identify correlations between fuel type, mileage, transmission, and pricing
An interactive scatter matrix that explores the relationships between key technical features such as fuel type, mileage (odometer readings), transmission, and cylinder count, with vehicle pricing. This visualization helps identify patterns, correlations, and potential outliers in how technical specifications influence market value. By analyzing multiple attributes simultaneously, buyers and sellers can gain deeper insights into pricing trends based on vehicle performance characteristics. 

- Interactive filters and checkboxes - Toggle between visualizations for a tailored analysis experience
The scatter matrix compares how technical features like fuel type, mileage, transmission, and cylinders relate to vehicle prices. This shows which features most strongly affect a vehicle's value and highlights any unusual price patterns based on these specifications.


## Technologies Used
- Python 3.x
The primary programming language used for developing the application's backend logic and data processing.

- Streamlit
A framework for creating the interactive web application interface, enabling real-time data visualization and user interaction.

- Pandas
A data manipulation library employed for handling and analyzing structured data efficiently.

- Plotly
A graphing library used to create interactive and dynamic visualizations within the application.

- Altair (instead of Seaborn, as the code uses Altair)
A declarative statistical visualization library utilized for generating informative and concise charts, replacing Seaborn in this project.

## Installation
1. Clone the repository
Begin by cloning the repository to your local machine:
git clone https://github.com/bea-bijanne/US-Vehicle-Metrics
cd US-Vehicle-Metrics

2. Install required packages
Ensure you have a requirements.txt file with the following content:
pandas==2.0.3
plotly==5.15.0
altair==5.0.1
streamlit==1.25.0

Then, install the packages:
pip install -r requirements.txt

3. Run the application
Start the Streamlit application:
streamlit run app.py

4. Access the application
Once the application is running, it will automatically open in your default web browser at the External URL:
http://34.213.214.55:10000

If it doesn't open automatically, you can manually navigate to this URL.

Note: Ensure you have Python 3.x and Git installed on your system before proceeding.

## Project Structure
The project is organized as follows:

US-Vehicle-Metrics/
├── us_vehicles_notebooks/
|   └──EDA.ipynb
├── app.py
├── requirements.txt

## Directory and File Overview
- us_vehicles_notebooks/: This directory contains Jupyter notebooks used for exploratory data analysis
 - EDA.ipynb: A notebook that performs initial data exploration and visualization to understand the dataset's components and shape subsequent analysis.
- app.py: The main application script built with Streamlit, serving as the entry point for the interactive web application. It integrates data processing and visualizaion components to ptovide users with aninteractive experience.
- requirements.txt: A list of Python packages and their specific versionsrequired to run the application. This file ensures that all necessary dependencies are installed for consistency across different environments.
