from pyrogram import Client, filters
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import Message
from pyrogram.errors import RPCError

def is_admin(member):
    return member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]

@Client.on_message(filters.command("unban") & filters.group)
async def unban_user(client, message: Message):
    if not message.reply_to_message:
        return await message.reply("Reply to a banned user's message to unban them.")

    user = message.reply_to_message.from_user

    member = await client.get_chat_member(message.chat.id, message.from_user.id)
    if not is_admin(member):
        return await message.reply("Only admins can use this command.")

    try:
        await client.unban_chat_member(message.chat.id, user.id)
        await message.reply(f"{user.mention} has been unbanned.")
    except RPCError as e:
        await message.reply(f"Failed to unban: {e}")