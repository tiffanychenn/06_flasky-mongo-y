'''
Name of JSON database: Giphy Crazy
Name of our database: CrazedAndDepraved
Description: GIFs related to the word "crazy"
How it's organized: organized by GIF
Hyperlink: http://api.giphy.com/v1/gifs/search?q=crazy&api_key=dc6zaTOxFJmzC
Import mechanism: Used the requests and json libraries to read in the database
'''

import pymongo
import requests
import json
from flask import Flask, render_template, request, session, redirect, url_for, flash

connection = pymongo.MongoClient("homer.stuy.edu")

db = connection.CrazedAndDepraved
collection = db.CrazyGIFs

link = "http://api.giphy.com/v1/gifs/search?q=crazy&api_key=dc6zaTOxFJmzC"
r = requests.get(link)      #make the API call
data = r.json()             #convert to a json object

for i in data["data"]:
    collection.insert_one(i)

#collection.insert_many(data)

#rating = collection.find({"rating":"g"})
#width = collection.find({"images.original.width":"146"})

app = Flask(__name__)

@app.route("/")
def root():
    return render_template("index.html")

@app.route("/gifs")
def gifs():
    form_stuff = request.args
    rating = form_stuff["rating"]
    try:
        verified = form_stuff["verified"]
        verified = True
    except:
        verified = False
    print rating, verified
    GIFs = collection.find({"rating": rating, "user.is_verified": verified})
    list_of_gifs = []
    for i in GIFs:
        list_of_gifs.append(i["images"]["original"]["url"])
    if len(list_of_gifs) == 0:
        return render_template("none.html")
    return render_template("gifs.html", gifs = list_of_gifs)

if __name__ == '__main__':
    app.debug = True
    app.run()