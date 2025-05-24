# bot/core/client.py
from pyrogram import client
from config import API_ID, API_HASH, BOT_TOKEN

app = Client("copy_right_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)