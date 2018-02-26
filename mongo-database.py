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

connection = pymongo.MongoClient("homer.stuy.edu")

db = connection.CrazedAndDepraved
collection = db.CrazyGIFs

link = "http://api.giphy.com/v1/gifs/search?q=crazy&api_key=dc6zaTOxFJmzC"
r = requests.get(link)		#make the API call
data = r.json()				#convert to a json object

for i in data["data"]:
	collection.insert_one(i)

#collection.insert_many(data)

rating = collection.find({"rating":"g"})

print "All GIFs in a specified rating (g)"

print "\n\n\n"

for i in rating:
	print i

print "\n\n\n"

width = collection.find({"images.original.width":"146"})

print "All GIFs with a specified width of 146"

print "\n\n\n"

for i in width:
	print i

print "\n\n\n"

dimensions = collection.find({"images.original.width":"146", "images.original.height": "93"})

print "All GIFs with a specified width of 146 and a height of 93"

print "\n\n\n"

for i in dimensions:
	print i

print "\n\n\n"

index = collection.find({"rating":"pg", "is_indexable": {"$gt":0}})

print "All GIFs with a specified rating (pg) and are indexable"

print "\n\n\n"

for i in index:
	print i

print "\n\n\n"

names = collection.find({"$or": [{"rating": "pg"}, {"images.original.width": "300"}]})

print "All GIFs with a specified rating (pg) or an original width of 300"

print "\n\n\n"

for i in names:
	print i