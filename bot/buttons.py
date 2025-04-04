from telegram import ReplyKeyboardMarkup, KeyboardButton


NEXT_BUTTON = "➡️ Next"
BACK_BUTTON = "⬅️ Back"

""" MAIN MENU """

PRICES_BUTTON = "Prices"
ALERTS_BUTTON = "Alerts"
STATISTICS_BUTTON = "Statistics"
SETTINGS_BUTTON = "Settings"

MAIN_MARKUP = ReplyKeyboardMarkup(
    [
        [KeyboardButton(PRICES_BUTTON), KeyboardButton(ALERTS_BUTTON)],
        [KeyboardButton(STATISTICS_BUTTON), KeyboardButton(SETTINGS_BUTTON)]
    ],
    resize_keyboard=True
)

""" PRICES """

DEURO_DEPS_BUTTON = "dEURO | DEPS Mainnet"
COLLATERAL_BUTTON = "Collateral Oracles"
DEX_DEURO_BUTTON = "DEX dEURO"
DEX_DEPS_BUTTON = "DEX DEPS"

PRICES_MARKUP = ReplyKeyboardMarkup(
    [
        [KeyboardButton(DEURO_DEPS_BUTTON), KeyboardButton(COLLATERAL_BUTTON)],
        [KeyboardButton(DEX_DEURO_BUTTON), KeyboardButton(DEX_DEPS_BUTTON)],
        [KeyboardButton(BACK_BUTTON)]
    ],
    resize_keyboard=True
)