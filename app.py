from flask import Flask, render_template, redirect 
from flask_pymongo import PyMongo
import scrape_mars
import os

app = Flask(__name__)
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
mars_results_db = client.mars_results_db

@app.route("/")
def home(): 

    mars_results = mongo.mars_results_db.mars_info.find_one()

    return render_template("index.html", mars_info=mars_results)

@app.route("/scrape")
def scraper():
    mars = mongo.mars_results_db.mars
    mars_data = scrape_mars.scrape()
    mars.update({}, mars_data, upsert=True)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)