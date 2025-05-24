import os
from dotenv import load_dotenv

# Load .env file content into environment variables
load_dotenv()

API_ID = int(os.getenv("API_ID", ""))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
MONGO_DB_URI = os.getenv("MONGO_DB_URI", "")
OWNER_ID = int(os.getenv("OWNER_ID", ""))
LOG_GROUP_ID = int(os.getenv("LOG_GROUP_ID", ""))

# You can add more config variables here if needed