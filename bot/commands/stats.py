import os
from pyrogram import Client, filters
from pyrogram.types import Message
from bot.keyboard.start_buttons import start_buttons

@Client.on_message(filters.command("stats") & filters.private)
async def stats_command(client: Client, message: Message):
    caption = "**Bot Stats:**\n\n- Total Users: coming soon\n- Uptime: coming soon\n- Version: v1.0"

    photo_path = "static/stats.png"
    if os.path.exists(photo_path):
        await message.reply_photo(photo=photo_path, caption=caption, reply_markup=start_buttons())
    else:
        await message.reply(caption, reply_markup=start_buttons())