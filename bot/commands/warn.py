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
from pyrogram import Client, filters
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import Message
from bot.utils.db import increase_warn, get_warn_count, reset_warn, decrease_warn

def is_admin(member):
    return member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]

@Client.on_message(filters.command("warn") & filters.group)
async def warn_user(client, message: Message):
    if not message.reply_to_message:
        return await message.reply("Reply to a message to warn.")
    
    user = message.reply_to_message.from_user
    member = await client.get_chat_member(message.chat.id, message.from_user.id)
    if not is_admin(member):
        return

    count = increase_warn(message.chat.id, user.id)
    await message.reply(f"{user.mention} has been warned ({count}/3)")

@Client.on_message(filters.command("unwarn") & filters.group)
async def unwarn_user(client, message: Message):
    if not message.reply_to_message:
        return await message.reply("Reply to a message to unwarn.")

    user = message.reply_to_message.from_user
    member = await client.get_chat_member(message.chat.id, message.from_user.id)
    if not is_admin(member):
        return

    decrease_warn(message.chat.id, user.id)
    count = get_warn_count(message.chat.id, user.id)
    await message.reply(f"{user.mention}'s warning reduced ({count}/3)")

@Client.on_message(filters.command("resetwarn") & filters.group)
async def reset_warn_user(client, message: Message):
    if not message.reply_to_message:
        return await message.reply("Reply to a message to reset warn.")

    user = message.reply_to_message.from_user
    member = await client.get_chat_member(message.chat.id, message.from_user.id)
    if not is_admin(member):
        return

    reset_warn(message.chat.id, user.id)
    await message.reply(f"{user.mention}'s warning has been reset.")
