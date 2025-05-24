from pyrogram.errors import RPCError
from pyrogram.types import ChatPermissions
from pyrogram import filters
from pyrogram import filters
from pyrogram.types import Message
from bot.core.client import app


@app.on_message(filters.text & filters.group)
async def check_text(client, message: Message):
    await message.reply("Message received.")
@app.on_message(filters.text & filters.group)
async def filter_abuse(client, message):
    ...
    for word in words:
        if is_abusive(word, message.chat.id):
            await message.delete()
            warn_count = increase_warn(message.chat.id, message.from_user.id)

            if warn_count >= 3:
                try:
                    await client.restrict_chat_member(
                        message.chat.id,
                        message.from_user.id,
                        ChatPermissions()
                    )
                    await message.reply(
                        f"{message.from_user.mention} has been muted for reaching 3 warnings."
                    )
                except RPCError:
                    pass
            else:
                await message.reply(
                    f"Abusive word isn't allowed!\n{message.from_user.mention} warned ({warn_count}/3)"
                )
            return
# bot/handlers/filter.py
from pyrogram import filters
from bot.core.client import app

@app.on_message(filters.text & filters.group)
async def filter_words(client, message):
    await message.reply("This message has been filtered.")