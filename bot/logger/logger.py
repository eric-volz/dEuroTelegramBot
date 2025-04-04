import logging
import sys
import os
from datetime import datetime

from bot.config import config


class Logger:
    _instance = None

    def __new__(cls, name: str, debug: bool = False):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance._init(name, debug)
        return cls._instance

    def _init(self, name: str, debug: bool = False):
        # Create logs directory if it doesn't exist
        logs_dir = os.path.join(sys.path[0], 'logs')
        os.makedirs(logs_dir, exist_ok=True)

        # Create logger
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG if debug else logging.INFO)

        # Define formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s'
        )

        # Console Handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

        # File Handler
        file_handler = logging.FileHandler(
            logs_dir + f'/{datetime.now().strftime("%Y-%m-%d_%H:%M:%S")}.log'
        )
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)


    def debug(self, message: str):
        self.logger.debug(message)

    def info(self, message: str):
        self.logger.info(message)

    def warning(self, message: str):
        self.logger.warning(message)

    def error(self, message: str):
        self.logger.error(message)

# Global logger instance
logger = Logger(config.get_value('GENERAL', "NAME"))