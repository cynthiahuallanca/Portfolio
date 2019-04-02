# Surfs Up!

![surfs-up.jpeg](Images/surfs-up.jpeg)


What if you want to take a holiday vacation to Honolulu, Hawaii? To help with your trip planning, we can do some climate analysis on the area. The following outlines what we can do.

## Step 1 - Climate Analysis and Exploration

Basic climate analysis and data exploration of climate database. All of the following analysis were completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.

* Databases used: [starter notebook](climate_starter.ipynb) and [hawaii.sqlite](Resources/hawaii.sqlite) files.

### Precipitation Analysis

* Query to retrieve the last 12 months of precipitation data.

* Plot of last 12 months of precipitation data 

  ![precipitation](Images/precipitation.png)

### Station Analysis

* Histogram plot with `bins=12` of last 12 months of temperature observation data (tobs) for the most active station.

    ![station-histogram](Images/station-histogram.png)
- - -

## Step 2 - Climate App

Flask API based on the above queries developed.

### Routes

* `/api/v1.0/precipitation`
  * Query results into a Dictionary using `date` as the key and `prcp` as the value.
  * Return the JSON representation of the dictionary.

* `/api/v1.0/stations`
  * Return a JSON list of stations from the dataset.
