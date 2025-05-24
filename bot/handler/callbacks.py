# bot/handlers/callbacks.py

from pyrogram import Client, filters
from pyrogram.types import CallbackQuery

@Client.on_callback_query(filters.regex("close"))
async def close_message(client: Client, callback_query: CallbackQuery):
    await callback_query.message.delete()
    await callback_query.answer()