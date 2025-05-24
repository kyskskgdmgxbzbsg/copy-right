import time
import os
from pyrogram import Client, filters
from pyrogram.types import Message
from bot.keyboard.start_buttons import start_buttons
from bot.utils.uptime import get_uptime

START_TIME = time.time()

@Client.on_message(filters.command("ping") & filters.private)
async def ping_command(client: Client, message: Message):
    start = time.time()
    m = await message.reply("Pinging...")
    end = time.time()

    latency = round((end - start) * 1000, 2)
    uptime = get_uptime(START_TIME)

    caption = f"**Pong!**\nLatency: `{latency} ms`\nUptime: `{uptime}`"
    photo_path = "static/ping.png"

    if os.path.exists(photo_path):
        await m.delete()
        await message.reply_photo(photo=photo_path, caption=caption, reply_markup=start_buttons())
    else:
        await m.edit(caption, reply_markup=start_buttons())