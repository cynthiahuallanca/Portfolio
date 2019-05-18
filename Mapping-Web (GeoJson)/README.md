Visualizing Data with Leaflet

## Background

The USGS (United States Geological Survey) is responsible for providing scientific data about natural hazards, the health of our ecosystems and environment; and the impacts of climate and land-use change. Their scientists develop new methods and tools to supply timely, relevant, and useful information about the Earth and its processes.

To visualize an earthquake data set: 

1. The USGS provides earthquake data in a number of different formats, updated every 5 minutes. Visit the [USGS GeoJSON Feed](http://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php) page and pick a data set to visualize. When you click on a data set, for example 'All Earthquakes from the Past 7 Days', you will be given a JSON representation of that data. 

2. Map using Leaflet that plots all of the earthquakes from your data set based on their longitude and latitude.


## To run the map: 

1. Obtain an API Key from [Mapbox](https://www.mapbox.com/) and add it to the config file 
2. Open your cmd and run the code with: 

```
python -m http.server
```

3. Open your localhost and voila! 



Enjoy the ride
~CH
