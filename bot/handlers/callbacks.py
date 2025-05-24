from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

# Example callback handler function
@Client.on_callback_query()
async def callback_query_handler(client: Client, query: CallbackQuery):
    data = query.data

    if data == "start_add_me":
        # Example: Respond to "Add Me" button click
        await query.answer("Thanks for your interest! You can add me to your group.")
        # Optionally send a message or open URL
        await query.message.edit_text(
            "Click the button below to add me to your group.",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("Add Me to Group", url=f"https://t.me/{client.me.username}?startgroup=true")],
                    [InlineKeyboardButton("Close", callback_data="close")]
                ]
            )
        )

    elif data == "close":
        # Close button clicked - delete the message or remove inline keyboard
        await query.message.delete()

    else:
        # Default fallback for unknown callback data
        await query.answer("Unknown action.", show_alert=True)