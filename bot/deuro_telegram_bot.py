import os

from telegram.ext import CommandHandler, ContextTypes, Application, MessageHandler, filters

from bot.logger import logger

# Methods
from bot.methods.general import *
from bot.methods.handler import *

class dEuroTelegramBot:

    def __init__(self, token: str) -> None:

        # Variables
        self.token = token

        # Telegram Bot
        self.app = Application.builder().token(token).build()
        self.app.add_handler(CommandHandler("start", GeneralMethods.start))
        self.app.add_handler(MessageHandler(filters.TEXT, Handler.handler))

    def run(self):
        """
        Run the bot
        """
        self.app.run_polling(1)  # Check for messages every 0.5 seconds

