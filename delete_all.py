import pymongo as pm

client = pm.MongoClient("mongodb://localhost:27017")
database = client["cover_scrape"]
collection = database["A54_Covers"]

collection.delete_many({})