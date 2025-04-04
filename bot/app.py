import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../")))

# Load config
from bot.config import config
current_dir: str = os.path.dirname(__file__)
config.init(f"{current_dir}/config.ini")

# Load logger
from bot.logger import logger

# Load ENV
from dotenv import load_dotenv
load_dotenv(verbose=True)

logger.info("Initialized config dependencies...")

# Init UniswapV3 Pools
from adapters.blockchain import UniswapV3Wrapper
urls_and_address: list = []
for rpc_name, rpc_urls in config.get_section("RPC_ADDRESSES").items():
    # ZCHF Pools
    for network_identifier, address in config.get_section("DEURO_UNISWAP_V3_POOLS").items():
        if rpc_name == network_identifier:
            urls_and_address.append((rpc_urls, address))
    # FPS Pools
    for network_identifier, address in config.get_section("DEPS_UNISWAP_V3_POOLS").items():
        if rpc_name == network_identifier:
            urls_and_address.append((rpc_urls, address))

UniswapV3Wrapper.initialize(urls_and_address)
logger.info("Initialized uniswap v3 pools...")

# Init and start FrankencoinTelegramBot
from bot.deuro_telegram_bot import dEuroTelegramBot
logger.info("Starting telegram bot...")
bot = dEuroTelegramBot(os.environ.get("TELEGRAM_TOKEN"))
bot.run()