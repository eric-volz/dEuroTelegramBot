from telegram import Update
from telegram.ext import ContextTypes

from bot.logger import logger

""" Handler """
from bot.buttons import *

from bot.methods.utils import Utils
from bot.methods.general import GeneralMethods
from bot.methods.prices import PricesMethods

class Handler:

    @staticmethod
    async def handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
        """
        This method incoming handles messages
        """
        logger.info(f"Message: {update.message.text} from {update.message.from_user.username}")

        # Set back markup to main markup if user data is none
        context.user_data['back_markup'] = [MAIN_MARKUP] if not context.user_data.get('back_markup') \
            else context.user_data['back_markup']

        # Handle Back Button
        if update.message.text == BACK_BUTTON:
            back_markup = context.user_data['back_markup'].pop()
            await Utils.send_msg(update, ["⬅️ Back"], back_markup)

        # Handle Help Request
        if update.message.text == "/help":
            await GeneralMethods.help(update, context)

        # Handle Navigation
        elif update.message.text == PRICES_BUTTON:
            await Utils.send_msg(update, ["➡️ Prices"], PRICES_MARKUP)
            context.user_data['back_markup'].append(MAIN_MARKUP)

        elif update.message.text == ALERTS_BUTTON:
            await GeneralMethods.coming_soon(update, context)

        elif update.message.text == STATISTICS_BUTTON:
            await GeneralMethods.coming_soon(update, context)

        elif update.message.text == SETTINGS_BUTTON:
            await GeneralMethods.coming_soon(update, context)

        # Handle method calls
        elif update.message.text == DEURO_DEPS_BUTTON:
            await PricesMethods.deuro_deps(update, context)

        elif update.message.text == COLLATERAL_BUTTON:
            await PricesMethods.collateral(update, context)

        elif update.message.text == DEX_DEURO_BUTTON:
            await PricesMethods.dex_deuro(update, context)

        elif update.message.text == DEX_DEPS_BUTTON:
            await PricesMethods.dex_deps(update, context)

        else:
            await GeneralMethods.unknown_command(update, context)