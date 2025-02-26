from pyrogram import Client
import logging
import logging.config
from info import Config
from aiohttp import web
from plugins.web_server import web_server  # Updated import
import pyromod
import os

# Configure logging
logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="ReportBot",
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN,
            plugins=dict(root="plugins"),
            in_memory=True
        )
        self.logger = logging.getLogger(__name__)

    async def start(self):
        await super().start()
        me = await self.get_me()
        self.logger.info(f"Bot started as {me.first_name} [@{me.username}]")
        
        # Start web server
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        port = int(os.environ.get("PORT", 8080))
        await web.TCPSite(app, bind_address, port).start()
        self.logger.info(f"Web server started on port {port}")

    async def stop(self):
        await super().stop()
        self.logger.info("Bot stopped!")

def main():
    bot = Bot()
    bot.run()

if __name__ == "__main__":
    main()
