from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN

app = Client(
    "client",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)