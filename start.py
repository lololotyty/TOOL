from pyrogram import Client, filters
from pyrogram.types import Message
from info import Config, Txt

@Client.on_message(filters.private & filters.command("start"))
async def start_command(bot: Client, msg: Message):
    await msg.reply_text(
        text=Txt.START_MSG.format(msg.from_user.mention),
        disable_web_page_preview=True
    )

@Client.on_message(filters.private & filters.command("help"))
async def help_command(bot: Client, msg: Message):
    await msg.reply_text(
        text=Txt.HELP_MSG,
        disable_web_page_preview=True
    )

@Client.on_message(filters.private & filters.command("about"))
async def about_command(bot: Client, msg: Message):
    await msg.reply_text(
        text=Txt.ABOUT_MSG,
        disable_web_page_preview=True
    )

#Restart to cancel all process 
@Client.on_message(filters.private & filters.command("restart") & filters.user(Config.SUDO))
async def restart_bot(b, m):
    await m.reply_text("💥__Rᴇꜱᴛᴀʀᴛɪɴɢ.....__")
    os.execl(sys.executable, sys.executable, *sys.argv)
