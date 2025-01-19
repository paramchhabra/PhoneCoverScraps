from motor.motor_asyncio import AsyncIOMotorClient
import asyncio

client = AsyncIOMotorClient("mongodb://localhost:27017")

database = client["cover_scrape"]
collection = database["A54_Covers"]

async def insert_in_db(name, brand, price, website):
    item = {"name":name, "price":price, "brand":brand, "website":website}
    await collection.insert_one(item)

async def get_data():
    data = collection.find({},{'_id':0})
    with open("data.csv", "w") as f:
        f.write("Name,Price,Brand,Website")
        f.write("\n")
        f.close()
    with open("data.csv", "a") as f:
        async for d in data:
            f.write(f"{d['name']},{d['price']},{d['brand']},{d['website']}")
            f.write("\n")
        f.close()
    print("CSV DATA ADDED")
