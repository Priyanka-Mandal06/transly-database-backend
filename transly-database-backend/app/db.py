import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")
client = None
db = None


async def connect_to_mongo():
    global client, db
    if not MONGO_URL:
        raise ValueError("❌ MONGO_URL is missing from .env")
    client = AsyncIOMotorClient(MONGO_URL)
    db = client["transly"]
    print("✅ MongoDB Connected!")


async def get_db():
    global db, client
    if db is None:
        print("⚠️ Reconnecting to MongoDB...")
        await connect_to_mongo()
    return db


async def close_mongo_connection():
    global client, db
    if client:
        client.close()
        client = None
        db = None
        print("🔌 MongoDB Connection Closed")
