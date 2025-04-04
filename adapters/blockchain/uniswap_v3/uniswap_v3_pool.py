from decimal import Decimal
import math

from web3 import Web3

# ABIs
from adapters.blockchain.default_abi import TOKEN_ABI
from adapters.blockchain.uniswap_v3.uniswap_v3_abi import UNISWAP_V3_POOL_ABI

Q96: Decimal = Decimal(2 ** 96)

class UniswapV3Pool:

    def __init__(self, provider: Web3, address: str, base_token_index: int):
        self.provider = provider
        self.address = address
        self.base_token_index = base_token_index
        self.contract = self.provider.eth.contract(address=Web3.to_checksum_address(self.address), abi=UNISWAP_V3_POOL_ABI)

        # Constants
        self.tokens = self.request_tokens()
        self.fee = self.request_fee()

        # Dynamic
        self.slot0 = self.request_slot0()

    def update(self):
        self.slot0 = self.request_slot0()

    """ Get """
    def get_tokens(self) -> dict:
        return self.tokens

    def get_fee(self) -> float:
        return self.fee

    def get_slot0(self) -> list:
        return self.slot0

    def get_current_tick(self) -> int:
        return self.slot0[1]

    def get_price(self) -> float:
        price: float = self.get_price_at_tick(self.get_current_tick())
        return price if self.base_token_index else price ** -1


    """ Request """
    def request_tokens(self) -> dict:
        result: dict = {}
        for token_address in (
                self.contract.functions.token0().call(), self.contract.functions.token1().call()):
            token_contract = self.provider.eth.contract(address=token_address, abi=TOKEN_ABI)
            symbol: str = token_contract.functions.symbol().call()
            decimals: int = token_contract.functions.decimals().call()
            result[symbol] = {"address": token_address, "decimals": decimals}
        return result

    def request_slot0(self) -> list:
        return self.contract.functions.slot0().call()

    def request_fee(self) -> float:
        return self.contract.functions.fee().call() / 10 ** 6

    """ Calculation """
    def get_price_at_tick(self, tick: float):
        price = Decimal(1.0001) ** Decimal(tick)
        sqrt_price = Decimal(math.sqrt(price)) * Q96
        decimal_0: int = list(self.tokens.values())[0]["decimals"]
        decimal_1: int = list(self.tokens.values())[1]["decimals"]
        return UniswapV3Pool._convert_q96_to_float(int(sqrt_price), decimal_0, decimal_1)

    @staticmethod
    def _convert_q96_to_float(q96_price: int, decimal0: int, decimal1: int) -> float:
        factor0 = Decimal(10 ** decimal0)
        factor1 = Decimal(10 ** decimal1)
        return float(Decimal((q96_price / Q96) ** 2) * factor0 / factor1)
