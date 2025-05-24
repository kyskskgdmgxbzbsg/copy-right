from pyrogram.enums import ChatMemberStatus
from pyrogram.types import Message

# Check if user is admin
async def is_admin(client, chat_id, user_id):
    member = await client.get_chat_member(chat_id, user_id)
    return member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]

# Get mention of user
def mention_user(user):
    if user.username:
        return f"@{user.username}"
    return f"<a href='tg://user?id={user.id}'>{user.first_name}</a>"

# Validate message is reply
def is_reply(message: Message):
    return bool(message.reply_to_message)