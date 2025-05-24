from pyrogram import Client, filters
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import Message
from pyrogram.errors import RPCError

def is_admin(member):
    return member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]

@Client.on_message(filters.command("ban") & filters.group)
async def ban_user(client, message: Message):
    if not message.reply_to_message:
        return await message.reply("Reply to a user's message to ban them.")

    user = message.reply_to_message.from_user
    if user.is_self:
        return await message.reply("I can't ban myself.")

    member = await client.get_chat_member(message.chat.id, message.from_user.id)
    if not is_admin(member):
        return await message.reply("Only admins can use this command.")

    try:
        await client.ban_chat_member(message.chat.id, user.id)
        await message.reply(f"{user.mention} has been banned from this group.")
    except RPCError as e:
        await message.reply(f"Failed to ban: {e}")