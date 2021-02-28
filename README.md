# SQLAlchemy Homework - Surfs Up!

## Overview

As a reward for surviving 2020, you have decided to trat yourself to a long holiday vacation in Honolulu, Hawaii! To help with your trip planning, you need to do some climate analysis on the area. The following python script, ran in Jupyter Notebook, analyzes the weater measurement data from various stations in Hawaii from a sqlite file. A Flas API is then designed based on the queries created in the analysis. 

## File Structure

sqlalchemy-challenge
* Resources
    * hawaii_measurements.csv
    * hawaii_stations.csv
    * hawaii.sqlite
* climate_starter.ipynb
* precipitation_over_time.png
* temperature_histogram.png

## Output

The final report includes each of the following:

### Climate Analysis and Exploration

Python and SQLAlchemy are used to do basic climate analysis and data exploration of the climate database. All of the following analysis is completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.

#### Precipitation Analysis

The precipitation analysis retrieves the last 12 months of precipitation data through a query.

The results of the query are then plotted on a Bar Chart.

#### Station Analysis

The station analysis retrieves the total number of stations fromt he Stations data table and finds the most active station wthin the Measurement table.

The results of the query are then plotted on a Histogram.

### Climate App

The Flask API was develpped based on the initial analysis queries. 

#### Routes
* `/`

  * Home page.

  * List all available routes

* `/api/v1.0/precipitation`

  * Converts the query results to a list of dictionaries of `date` and `prcp`.

  * Return the JSON representation of the dictionary.

* `/api/v1.0/stations`

  * Return a JSON list of stations from the dataset.

* `/api/v1.0/tobs`
  * Queries the dates and temperature observations of the most active station for the last year of data.
  
  * Returns a JSON list of temperature observations (TOBS) for the previous year.

* `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`

  * Returns a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

    * When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date are returned.

    * When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.