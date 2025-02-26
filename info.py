import os

class Config:
    # Bot token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7680113655:AAGBrFFksT0yDDfoHEci3B42WM8h31Su3c4")
    
    # API ID & Hash from my.telegram.org
    API_ID = os.environ.get("API_ID", "22430866")
    API_HASH = os.environ.get("API_HASH", "20a0f0284c49fe38bb3676c297fbf947")
    
    # Sudo users (Owner users)
    SUDO = [int(x) for x in os.environ.get("SUDO", "6169016546").split()]
    
    # Start message pic
    START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/29626078a1324cf58ce2a.jpg")
    
    # Support chat link
    SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT", "ilovemovie123")

class Txt:
    # Messages
    START_MSG = """
Hi {}, Welcome to Mass Report Bot.

I can help you mass report Telegram channels/groups.
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
