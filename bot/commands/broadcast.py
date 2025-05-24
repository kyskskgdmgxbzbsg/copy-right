from pyrogram import Client, filters
from pyrogram.types import Message
from config import OWNER_ID
from bot.utils.db import get_all_users

@Client.on_message(filters.command("broadcast") & filters.private)
async def broadcast_message(client: Client, message: Message):
    if message.from_user.id != OWNER_ID:
        return await message.reply("Only the bot owner can use this command.")

    if len(message.command) < 2:
        return await message.reply("Usage: /broadcast Your message here")

    text = message.text.split(None, 1)[1]
    sent, failed = 0, 0

    for user_id in get_all_users():
        try:
            await client.send_message(user_id, text)
            sent += 1
        except:
            failed += 1

    await message.reply(f"Broadcast done!\n✅ Sent: {sent}\n❌ Failed: {failed}")