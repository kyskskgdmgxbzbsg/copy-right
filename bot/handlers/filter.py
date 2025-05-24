from pyrogram import Client, filters
from bot.utils.db import is_abusive, increase_warn
from pyrogram.types import Message

@Client.on_message(filters.text & filters.group)
async def filter_abuse(client, message: Message):
    if message.from_user is None or message.from_user.is_bot:
        return

    words = message.text.lower().split()
    for word in words:
        if is_abusive(word, message.chat.id):
            await message.delete()
            warn_count = increase_warn(message.chat.id, message.from_user.id)
            await message.reply(
                f"Abusive word isn't allowed!\n{message.from_user.mention} has been warned ({warn_count}/3)"
            )
            return