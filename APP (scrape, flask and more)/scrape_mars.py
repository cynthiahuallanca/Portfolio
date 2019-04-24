# Model 
# Import All Dependencies
from bs4 import BeautifulSoup
from splinter import Browser
import os
import pandas as pd
from selenium import webdriver

def init_browser():
    executable_path = {"executable_path": "/Users/BohuCyn/Anaconda/pkgs/selenium-chromedriver-2.27-0/Library/bin/chromedriver"}  
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()
    project_mars = {}

    # ** 1. Scrapping latest news about mars from nasa **
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    # Scrape page into Soup
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    news_title = soup.find("div",class_="content_title").text
    news_paragraph = soup.find('div', class_='article_teaser_body').text
    
    project_mars['news_title'] = news_title
    project_mars['news_paragraph'] = news_paragraph 

    #return project_mars

    # ** 2. Scraping featured image ** 
    image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=featured#submit'
    browser.visit(image_url)

    # Pass the url to BeautifulSoup
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    results = soup.find_all("li", class_='slide')
    
    for result in results:
        link = result.a['data-fancybox-href']
        break
    
    base_url = 'https://www.jpl.nasa.gov'

    featured_image_url = base_url + link
    
    project_mars["featured_image_url"] = featured_image_url


   # ** 3. Scraping Mars Weather ** 

    # Set url to visit with splinter
    weather_url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(weather_url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    mars_weather = soup.find("p",class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text

    project_mars["mars_weather"] = mars_weather

    # ** 4. Scraping Mars Facts Table ** 

    url_facts = "https://space-facts.com/mars/"
    tables = pd.read_html(url_facts)
    df = tables[0]

    mars_facts_table = df.to_html(buf=None, columns=None, col_space=None, header=False, index=False, \
                    na_rep='NaN', index_names=False, justify='right', bold_rows=True, classes=None, \
                    escape=True, max_rows=None, max_cols=None, show_dimensions=False, \
                    notebook=False, decimal='.', border=1)

    project_mars["mars_facts_table"] = mars_facts_table


    # ** 5. Scraping Mars # Mars Hemispheres ** 

    # URL general 
    hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemispheres_url)
    
    html_hemispheres = browser.html

    # Use Beautiful Soup
    soup = BeautifulSoup(html_hemispheres, 'html.parser')

    # Obtain hemispheres box
    items = soup.find_all('div', class_='item')

    hemisphere_image_urls = []

# URL base 
    main_url = 'https://astrogeology.usgs.gov' 

    # For loop to go through the items
    for item in items: 
        # Hemisphere Title
        title = item.find('h3').text
                
        # URL with relative path for full sized image
        href = item.find('a', class_='itemLink product-item')['href']
                
        # Visit the link that contains the full image website 
        browser.visit(main_url + href)
                
        # HTML Object of individual hemisphere information website 
        partial_img_html = browser.html
                
        # Parse HTML with Beautiful Soup for every individual hemisphere information website 
        soup = BeautifulSoup( partial_img_html, 'html.parser')
                
        # Obtain full image url 
        img_url = main_url + soup.find('img', class_='wide-image')['src']
                
        # Append the information into a list of dictionaries 
        hemisphere_image_urls.append({"title" : title, "img_url" : img_url})

    project_mars['hemisphere_image_urls'] = hemisphere_image_urls

        # Return dictionary of scraped values we created
    return project_mars

# For debugging  
if __name__ == "__main__":
    project_mars = scrape()
    print(project_mars)
