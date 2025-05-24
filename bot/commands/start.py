from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import OWNER_ID, BOT_USERNAME
import os

@Client.on_message(filters.command("start") & filters.private)
async def start_command(client: Client, message: Message):
    photo_path = "static/start.png"
    caption = "Welcome! I'm your assistant bot.\nUse me to manage your groups with powerful moderation tools."

    keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("➕ Add Me", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
             InlineKeyboardButton("❌ Close", callback_data="close")],
            [InlineKeyboardButton("👤 Support", user_id=OWNER_ID)]
        ]
    )

    if os.path.exists(photo_path):
        await message.reply_photo(photo=photo_path, caption=caption, reply_markup=keyboard)
    else:
        await message.reply_text(caption, reply_markup=keyboard)
from bot.keyboards.start_buttons import start_buttons

...

await message.reply_photo(photo=photo_path, caption=caption, reply_markup=start_buttons())