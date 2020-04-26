from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import Mission_to_Mars

# Create an instance of Flask
app = Flask(__name__)

# Use flask_PyMongo to establish Mongo connection
app.config['MONGO_URI'] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)


# Route to render index.html template using data from Mongo
@app.route("/")
def index():
    news_articles=mongo.db.news_title.find_one()
    return render_template("index.html", news_title=news_title)


# Route that will trigger the scrape function
@app.route("/scrape")
def scraper():
    news_articles = mongo.db.news_title


    # Run the scrape function
    #costa_data = scrape_costa.scrape_info()

    # Update the Mongo database using update and upsert=True
    #mongo.db.collection.update({}, costa_data, upsert=True)

    # Redirect back to home page
    #return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
