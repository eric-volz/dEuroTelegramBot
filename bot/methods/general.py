import os
from telegram import Update
from telegram.ext import ContextTypes

from bot import bot_path
from bot.logger import logger
from bot.buttons import MAIN_MARKUP
from bot.methods.utils import Utils

""" General Methods """

class GeneralMethods:

    @staticmethod
    async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
        logger.info(f"Start from {update.message.from_user.username}")

        message = (
            "🎉 Welcome to Frankencoin Bot! 🤖 \n\n"
            "🏦 Your gateway to the Frankencoin protocol: \n"
            "📊 Monitor positions \n"
            "💰 Check rates \n"
            "🔔 Get notifications \n\n"
            
            "Need help? Type /help 💡 \n\n"
            "Let's get started! 🚀"
        )

        with open(bot_path + '/media/frankencoin_telegram_bot_logo_black.png', 'rb') as photo:
            await update.message.reply_photo(
                photo=photo,
                caption=message,
                reply_markup=MAIN_MARKUP
            )

    @staticmethod
    async def coming_soon(update: Update, context: ContextTypes.DEFAULT_TYPE):
        logger.info(f"Unknown command from {update.message.from_user.username}: {update.message.text}")

        message = (
            "🚀 This function will be available soon!"
        )

        await Utils.send_msg(update, [message], None, False)

    @staticmethod
    async def unknown_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        logger.info(f"Unknown command from {update.message.from_user.username}: {update.message.text}")

        message = (
            "❓ Oops! I don't know this command. \n"
            "🔍 Try /help to see all available commands. \n\n"
            "Or use the menu below 👇"
        )

        await Utils.send_msg(update, [message], MAIN_MARKUP, False)

    @staticmethod
    async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
        logger.info(f"Help from {update.message.from_user.username}: {update.message.text}")

        await GeneralMethods.coming_soon(update, context)