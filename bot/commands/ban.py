from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("ban") & filters.group)
async def ban_user(client: Client, message: Message):
    # Check if the user is an admin
    chat_member = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chat_member.status not in ("administrator", "creator"):
        return await message.reply("You need to be an admin to use this command.")

    # Check if the command is a reply
    if not message.reply_to_message:
        return await message.reply("Reply to the user's message to ban them.")

    user_id = message.reply_to_message.from_user.id

    try:
        await client.ban_chat_member(message.chat.id, user_id)
        await message.reply(f"Banned {message.reply_to_message.from_user.mention} from the group.")
    except Exception as e:
        await message.reply(f"Failed to ban user: {e}")