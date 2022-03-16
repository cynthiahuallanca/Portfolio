# Mission to Mars

![mission_to_mars](Images/mission_to_mars.jpg)

To build a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page.

## Step 1 - Scraping

Initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

* Using Jupyter Notebook file called `mission_to_mars.ipynb` to complete all scraping and analysis. 

### NASA Mars News

* Scraping the [NASA Mars News Site](https://mars.nasa.gov/news/) and collecting the latest News Title and Paragraph Text. 

```python
# Example:
news_title = "NASA's Next Mars Mission to Investigate Interior of Red Planet"

news_p = "Preparation of NASA's next spacecraft to Mars, InSight, has ramped up this summer, on course for launch next May from Vandenberg Air Force Base in central California -- the first interplanetary launch in history from America's West Coast."
```

### JPL Mars Space Images - Featured Image

* Website for JPL Featured Space Image [here](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars).

* Using splinter to navigate the site and finding the image url for the current Featured Mars Image and assigning the url string to the variable `featured_image_url`.

* Making sure to find the image url to the full size `.jpg` image.

* Making sure to save a complete url string for this image.

```python
# Example:
featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA16225_hires.jpg'
```

### Mars Weather

* Mars Weather twitter account [here](https://twitter.com/marswxreport?lang=en). Scraping the latest Mars weather tweet from the pagenad saving the tweet text for the weather report as `mars_weather`.

```python
# Example:
mars_weather = 'Sol 1801 (Aug 30, 2017), Sunny, high -21C/-5F, low -80C/-112F, pressure at 8.82 hPa, daylight 06:09-17:55'
```

### Mars Facts

* Mars Facts webpage [here](http://space-facts.com/mars/), using Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.

* Using Pandas to convert the data to a HTML table string.

### Mars Hemispheres

* USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars), obtaining high resolution images for each of Mar's hemispheres.

* Saving both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Using a Python dictionary to store the data using the keys `img_url` and `title`.

* Appending the dictionary with the image url string and the hemisphere title to a list. (The list contains one dictionary for each hemisphere.)

```python
# Example:
hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "..."},
    {"title": "Cerberus Hemisphere", "img_url": "..."},
    {"title": "Schiaparelli Hemisphere", "img_url": "..."},
    {"title": "Syrtis Major Hemisphere", "img_url": "..."},
]
```

- - -

## Step 2 - MongoDB and Flask Application

Using MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

* Converting the Jupyter notebook into a Python script `scrape_mars.py` with a function called `scrape` that will execute all of the scraping code from above and return one Python dictionary containing all of the scraped data.

* Creating a route called `/scrape` that will import the `scrape_mars.py` script and call the function `scrape`.

  * Storing the return value in Mongo as a Python dictionary.

* Creating a root route `/` that query Mongo database and pass the mars data into an HTML template to display the data.

* Creating a template HTML file called `index.html` that takes the mars data dictionary and displays all of the data in the appropriate HTML elements.
