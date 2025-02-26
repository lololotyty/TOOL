from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from info import Config, Txt
import os
import sys

# Start Command
@Client.on_message(filters.command("start") & filters.private)
async def start_command(client: Client, message: Message):
    try:
        await message.reply_text(
            text=Txt.START_MSG.format(message.from_user.mention),
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Help", callback_data="help"),
                 InlineKeyboardButton("About", callback_data="about")]
            ]),
            disable_web_page_preview=True
        )
    except Exception as e:
        print(f"Error in start command: {e}")

# Help Command
@Client.on_message(filters.command("help") & filters.private)
async def help_command(client: Client, message: Message):
    try:
        await message.reply_text(
            text=Txt.HELP_MSG,
            disable_web_page_preview=True
        )
    except Exception as e:
        print(f"Error in help command: {e}")

# About Command
@Client.on_message(filters.command("about") & filters.private)
async def about_command(client: Client, message: Message):
    try:
        await message.reply_text(
            text=Txt.ABOUT_MSG,
            disable_web_page_preview=True
        )
    except Exception as e:
        print(f"Error in about command: {e}")

# Restart Command
@Client.on_message(filters.command("restart") & filters.private & filters.user(Config.SUDO))
async def restart_bot(client: Client, message: Message):
    try:
        restart_message = await message.reply_text("🔄 Restarting bot...")
        os.execl(sys.executable, sys.executable, *sys.argv)
    except Exception as e:
        print(f"Error in restart command: {e}")
