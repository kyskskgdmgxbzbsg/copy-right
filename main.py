from bot.commands import warn
from bot.handlers import logs
from bot.commands import ban
from bot.commands import mute
from bot.commands import stats
from bot.commands import ping
from pyrogram import Client
import logging

# Client config
app = Client("mybot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# IMPORT ALL HANDLERS
from bot.commands import start  # /start
from bot.handlers import callbacks  # ❌ close button

# Start the bot
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    print("Bot is running...")
    app.run()