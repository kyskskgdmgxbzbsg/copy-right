from pyrogram import Client, filters
from pyrogram.types import Message
from bot.utils.db import increase_warn, get_warn_count, reset_warn

@Client.on_message(filters.command("warn") & filters.group)
async def warn_user(client: Client, message: Message):
    if not message.reply_to_message:
        return await message.reply("Reply to a user to warn them.")

    admin = await client.get_chat_member(message.chat.id, message.from_user.id)
    if admin.status not in ("administrator", "creator"):
        return await message.reply("Only admins can warn users.")

    user = message.reply_to_message.from_user
    warn_count = increase_warn(message.chat.id, user.id)

    if warn_count >= 3:
        await message.reply(f"{user.mention} has been banned due to exceeding warning limit (3/3).")
        await client.ban_chat_member(message.chat.id, user.id)
        reset_warn(message.chat.id, user.id)
    else:
        await message.reply(f"{user.mention} has been warned! ({warn_count}/3)")