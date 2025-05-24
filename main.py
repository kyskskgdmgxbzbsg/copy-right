from config import API_ID, API_HASH, BOT_TOKEN, OWNER_ID, LOG_GROUP_ID, MONGO_URI
from bot.commands import unban
from bot.commands import warn
from bot.commands import wordlist
from bot.handlers import filter
from bot.commands import broadcast
from bot.commands import warn
from bot.handlers import logs
from bot.commands import ban
from bot.commands import mute
from bot.commands import stats
from bot.commands import ping
from bot.core.cilent import app
from pyrogram import cilent
from config import API_ID, API_HASH, BOT_TOKEN
import logging

# Client config
app = Client("bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# IMPORT ALL HANDLERS
# main.py
from bot.core.client import app
from bot.handlers import filter   # just for handler import

if __name__ == "__main__":
    print("Bot is starting...")
    app.run()