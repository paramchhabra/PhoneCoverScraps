from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient("mongodb://localhost:27017")

database = client["cover_scrape"]
collection = database["A54_Covers"]

async def insert_in_db(name, brand, price, website):
    item = {"name":name, "price":price, "brand":brand, "website":website}
    await collection.insert_one(item)