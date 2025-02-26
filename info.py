import os

class Config:
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7680113655:AAGBrFFksT0yDDfoHEci3B42WM8h31Su3c4")
    API_ID = int(os.environ.get("API_ID", "22430866"))  # Convert to int
    API_HASH = os.environ.get("API_HASH", "20a0f0284c49fe38bb3676c297fbf947")
    SUDO = [int(x) for x in os.environ.get("SUDO", "6169016546").split()]
    START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/29626078a1324cf58ce2a.jpg")
    SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT", "ilovemovie123")
    OWNER = int(os.environ.get("OWNER", "6169016546"))  # Add owner ID

class Txt:
    START_MSG = """
👋 Hi {}, Welcome to Mass Report Bot!

I can help you mass report Telegram channels/groups.
Use /help to see available commands.
    """
    
    HELP_MSG = """
**🛠 Available Commands:**

/start - Start the bot
/help - Show this help message
/make_config - Create new config
/add_account - Add new account
/target - Check current target
/report - Start reporting target
    """
    
    ABOUT_MSG = """
**About This Bot:**

A Telegram bot to mass report channels/groups.

• Creator: @ROHAN_KING_KING
• Language: Python
• Framework: Pyrogram
    """
    
    SEND_SESSION_MSG = "Please send your session string..."
