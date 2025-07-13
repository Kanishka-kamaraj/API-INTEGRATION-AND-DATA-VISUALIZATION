# API-INTEGRATION-AND-DATA-VISUALIZATION

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: KANISHKA K

*INTERN ID*: CT04DH1742

*DOMAIN*: PYTHON PROGRAMMING

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH

# Project Description:
As part of the CodTech Internship Task 1, this project involves integrating a public API and creating insightful visualizations from the data retrieved. The primary objective is to fetch real-time weather data from the OpenWeatherMap API and represent the information graphically using Python libraries like Matplotlib and Seaborn.

The project is divided into two main components:

API Integration

Data Visualization Dashboard

1. API Integration:
The first step is to connect to a public API to extract data. We chose OpenWeatherMap, which provides access to a wide range of weather data including temperature, humidity, wind speed, and weather conditions for any location around the globe.

We created a free account on OpenWeatherMap and generated a unique API key, which is essential for authentication. Using the requests library in Python, we made HTTP GET requests to the OpenWeatherMap Current Weather Data API, fetching live temperature data for multiple major Indian cities such as Chennai, Delhi, Mumbai, Kolkata, and Bangalore.

The response from the API is in JSON format, which we parsed to extract specific fields like city name and current temperature. These values were then stored in a list of dictionaries to be passed into the visualization section of the script.

2. Data Visualization:
After collecting the temperature data, the next step was to visualize it using Seaborn and Matplotlib. A bar chart was chosen to display the temperature readings for the selected cities, providing a clear and comparative view of the current weather conditions.

The cities were plotted on the X-axis, while their respective temperatures (in Celsius) were plotted on the Y-axis. A coolwarm color palette was used to enhance the visual appeal and make temperature differences easier to distinguish.

The chart was customized with a title ("Current Temperature in Major Indian Cities"), axis labels, and proper layout formatting to ensure clarity. The project was executed using IDLE, Python's default development environment, and successfully displayed the temperature data both as printed text in the shell and as a visual bar chart.

3.Technologies Used:
Python 3

OpenWeatherMap API

Requests Library

Matplotlib

Seaborn

IDLE (Python IDE)

4.Deliverables:
A Python script (weather_project.py) that:

Connects to the OpenWeatherMap API

Fetches and parses current temperature data

Plots the data using Seaborn/Matplotlib

A real-time visual dashboard (bar chart) displaying the weather data

5.Learning Outcome:
This task provided hands-on experience in working with APIs, handling JSON data, and using Python for real-world data visualization. It enhanced our understanding of how to integrate external data sources into Python applications and visualize the output for better insights — a key skill in both Data Science and Software Development domains.
