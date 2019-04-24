# Controler

# Import All Dependencies
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo 

#import the scrape
import scrape_mars

app = Flask(__name__)

# Create the database in Mongo 
mongo = PyMongo(app, uri="mongodb://localhost:27017/mission_to_mars")


@app.route("/")
def index():
    project_mars = mongo.db.project_mars.find_one()
    return render_template("index.html", project_mars=project_mars)


@app.route("/scrape")
def scraper():
    project_mars = mongo.db.project_mars
    scrape_mars_data = scrape_mars.scrape()
    # update, if not, insert it (because we have upser=True)
    project_mars.update({}, scrape_mars_data, upsert=True)
    #redirect to my index page
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
