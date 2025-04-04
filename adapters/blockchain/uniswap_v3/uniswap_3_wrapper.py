import time

from web3 import Web3

from adapters.blockchain.uniswap_v3.uniswap_v3_pool import UniswapV3Pool
from adapters.blockchain.provider import Web3Provider

class UniswapV3Wrapper:
    _initialized: bool = False
    last_updated: float = 0
    update_interval: float = None
    pools: dict = {}

    """ Initialize """

    @classmethod
    def initialize(cls, urls_and_address, update_interval: float = 60):
        if not cls._initialized:
            cls.update_interval = update_interval

            # Init pools and add to list
            cls.pools: dict[UniswapV3Pool] = {}
            for urls, pool_info in urls_and_address:
                address, base_token_index = pool_info.split(",")
                provider = Web3(Web3Provider([Web3.HTTPProvider(url) for url in urls.split(";")]))
                pool = UniswapV3Pool(provider, address.lower(), int(base_token_index))
                cls.pools[address.lower()] = pool
            cls._initialized = True

    @classmethod
    def check(cls) -> bool:
        if not cls._initialized:
            raise Exception("UniswapV3 wrapper is not initialized yet.")

        if cls.last_updated + cls.update_interval < time.time():
            cls.update()
            cls.last_updated = time.time()
        return True

    """ Update """
    @staticmethod
    def update():
        for pool in UniswapV3Wrapper.pools.values():
            pool.update()

    """ Get """
    @staticmethod
    def get_pool(address: str) -> UniswapV3Pool:
        UniswapV3Wrapper.check()
        return UniswapV3Wrapper.pools[address.lower()]

    @staticmethod
    def get_price(address: str) -> float:
        UniswapV3Wrapper.check()
        return UniswapV3Wrapper.pools[address.lower()].get_price()
