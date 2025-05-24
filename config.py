import os
from dotenv import load_dotenv

# Load .env file content into environment variables
load_dotenv()

API_ID = os.getenv("API_ID", "21546320")
API_HASH = os.getenv("API_HASH", "c16805d6f2393d35e7c49527daa317c7")
BOT_TOKEN = os.getenv("BOT_TOKEN", "8020578503:AAFWeiecAUXOmzoOIzzTvnZ8BdcluskMSVk")
MONGO_URI = os.getenv("MONGO_DB_URI", "mongodb+srv://manoranjanhor43:somuxd@manoranjan.wsglmdq.mongodb.net/?retryWrites=true&w=majority&appName=Manoranjan")
OWNER_ID = os.getenv("OWNER_ID", "6908972904")
LOG_GROUP_ID = os.getenv("LOG_GROUP_ID", "-1002100433415")

# You can add more config variables here if needed