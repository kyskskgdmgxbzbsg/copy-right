from pyrogram import Client, filters
from pyrogram.types import Message
from config import LOG_CHANNEL_ID

# Log when someone starts the bot (private chat)
@Client.on_message(filters.command("start") & filters.private)
async def log_user_start(client: Client, message: Message):
    user = message.from_user
    log_text = f"**New /start Command:**\n\n**Name:** {user.first_name}\n**Username:** @{user.username}\n**ID:** `{user.id}`"
    
    try:
        await client.send_message(chat_id=LOG_CHANNEL_ID, text=log_text)
    except:
        pass

# Log when bot is added to a new group
@Client.on_message(filters.new_chat_members)
async def log_bot_added(client: Client, message: Message):
    for member in message.new_chat_members:
        if member.id == (await client.get_me()).id:
            group = message.chat
            user = message.from_user

            log_text = f"**Bot Added to Group:**\n\n**Group Name:** {group.title}\n**Group ID:** `{group.id}`\n**Username:** @{group.username if group.username else 'N/A'}\n\n**Added By:** {user.first_name} (`{user.id}`)"
            
            try:
                await client.send_message(chat_id=LOG_CHANNEL_ID, text=log_text)
            except:
                pass