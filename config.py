import os
from dotenv import load_dotenv

load_dotenv()  # .env file load kore

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID"))
BOT_USERNAME = os.getenv("BOT_USERNAME")
LOG_CHANNEL_ID=-1001234567890
MONGO_URI = os.getenv("MONGO_URI")