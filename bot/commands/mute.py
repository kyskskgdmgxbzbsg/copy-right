from pyrogram import Client, filters
from pyrogram.types import Message, ChatPermissions
from datetime import timedelta, datetime

@Client.on_message(filters.command("mute") & filters.group)
async def mute_user(client: Client, message: Message):
    # Check if the user is admin
    chat_member = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chat_member.status not in ("administrator", "creator"):
        return await message.reply("You need to be an admin to use this command.")

    # Check if someone is replied to
    if not message.reply_to_message:
        return await message.reply("Reply to a user to mute them.")

    # Check if time duration is given
    if len(message.command) < 2:
        return await message.reply("Usage: /mute <minutes> (reply to a user)")

    try:
        minutes = int(message.command[1])
    except ValueError:
        return await message.reply("Please provide mute duration in minutes.")

    until_date = datetime.utcnow() + timedelta(minutes=minutes)

    try:
        await client.restrict_chat_member(
            chat_id=message.chat.id,
            user_id=message.reply_to_message.from_user.id,
            permissions=ChatPermissions(),  # No permissions
            until_date=until_date
        )
        await message.reply(f"Muted {message.reply_to_message.from_user.mention} for {minutes} minutes.")
    except Exception as e:
        await message.reply(f"Failed to mute: {e}")