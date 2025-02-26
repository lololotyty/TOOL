from pyrogram import Client, filters
from pyrogram.types import CallbackQuery
from info import Txt

@Client.on_callback_query()
async def callback_query(client: Client, callback_query: CallbackQuery):
    try:
        if callback_query.data == "help":
            await callback_query.message.edit_text(
                text=Txt.HELP_MSG,
                disable_web_page_preview=True
            )
        elif callback_query.data == "about":
            await callback_query.message.edit_text(
                text=Txt.ABOUT_MSG,
                disable_web_page_preview=True
            )
    except Exception as e:
        print(f"Error in callback query: {e}")
