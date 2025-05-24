from pyrogram import Client, filters
from pyrogram.types import Message
from bot.utils.db import add_blacklist_word, add_whitelist_word

@Client.on_message(filters.command("blword") & filters.group)
async def add_bl_word(client, message: Message):
    if len(message.command) < 2:
        return await message.reply("Usage: /blword word")

    word = message.text.split(None, 1)[1]
    add_blacklist_word(message.chat.id, word)
    await message.reply(f"Added to blacklist: `{word}`")

@Client.on_message(filters.command("wlword") & filters.group)
async def add_wl_word(client, message: Message):
    if len(message.command) < 2:
        return await message.reply("Usage: /wlword word")

    word = message.text.split(None, 1)[1]
    add_whitelist_word(message.chat.id, word)
    await message.reply(f"Added to whitelist: `{word}`")