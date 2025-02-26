import logging
from pyrogram import Client
from info import Config
import logging.config

# Setup logging
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="ReportBot",
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN,
            plugins=dict(root="plugins")  # This line loads plugins
        )
        self.logger = logger

    async def start(self):
        await super().start()
        self.logger.info("Bot started!")

    async def stop(self):
        await super().stop()
        self.logger.info("Bot stopped!")

def main():
    try:
        bot = Bot()
        bot.run()
    except Exception as e:
        logging.error(f"Fatal error: {str(e)}")
        raise e

if __name__ == "__main__":
    main()
