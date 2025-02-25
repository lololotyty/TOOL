from pyrogram import (
    Client,
    __version__
)
from pyrogram.raw.all import layer
from info import Config
import logging
from datetime import datetime
import logging.config, os
from pytz import timezone
from aiohttp import web
from plugins import web_server
import pyromod

# Configure logging
logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="ReportBot",
            in_memory=True,
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN,
            plugins={'root': 'plugins'}
        )

    async def start(self):
        try:
            await super().start()
            me = await self.get_me()
            
            # Log bot credentials for debugging
            logging.info(f"Bot credentials loaded - API_ID: {Config.API_ID}, Username: {me.username}")
            
            # Start web server first
            app = web.AppRunner(await web_server())
            await app.setup()
            bind_address = "0.0.0.0"
            port = int(os.environ.get("PORT", 8080))  # Get port from environment or default to 8080
            await web.TCPSite(app, bind_address, port).start()
            logging.info(f"Web server started on port {port}")
            
            # Rest of your bot initialization
            self.mention = me.mention
            self.username = me.username
            logging.info(f"✅ {me.first_name} with Pyrogram v{__version__} (Layer {layer}) started on {me.username}. ✅")
            
            if Config.OWNER:
                try:
                    await self.send_message(Config.OWNER, f"**__{me.first_name} Iꜱ Sᴛᴀʀᴛᴇᴅ.....✨️__**")
                except Exception as e:
                    logging.error(f"Failed to send startup message to owner: {str(e)}")
            
        except Exception as e:
            logging.error(f"Failed to start bot: {str(e)}")
            raise e

    async def stop(self, *args):
        try:
            await super().stop()
            logging.info("Bot Stopped ⛔")
        except Exception as e:
            logging.error(f"Error while stopping bot: {str(e)}")

def main():
    try:
        bot = Bot()
        bot.run()
    except Exception as e:
        logging.error(f"Fatal error: {str(e)}")
        raise e

if __name__ == "__main__":
    main()
