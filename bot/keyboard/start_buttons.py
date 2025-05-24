from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import BOT_USERNAME, OWNER_ID

def start_buttons():
    return InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("➕ Add Me", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
             InlineKeyboardButton("❌ Close", callback_data="close")],
            [InlineKeyboardButton("👤 Support", user_id=OWNER_ID)]
        ]
    )