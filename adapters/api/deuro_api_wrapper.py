from adapters.api.deuro_api import dEuroAPI


class dEuroAPIWrapper:
    _initialized: bool = False
    mint_token: dict = {}
    equity_token: dict = {}
    collateral_token_list: dict = {}

    """ Initialize """
    @classmethod
    def initialize(cls):
        if not cls._initialized:
            # Init mint token
            mint_token: dict = dEuroAPI.get_prices_erc20_mint()
            cls.mint_token[mint_token["symbol"]] = mint_token

            # Init equity token
            equity_token: dict = dEuroAPI.get_prices_erc20_fps()
            cls.equity_token[equity_token["symbol"]] = equity_token

            # Init collateral list
            for address, value in dEuroAPI.get_prices_erc20_collateral().items():
                cls.collateral_token_list[value["symbol"]] = value

            cls._initialized = True

    """ Prices """
    @staticmethod
    def get_prices() -> dict:
        dEuroAPIWrapper.initialize()
        results: dict = {}
        for data in dEuroAPI.get_prices_list():
            try:
                results[data["symbol"]] = {"usd": data["price"]["usd"], "eur": data["price"]["eur"]}
            except Exception as e:
                pass
        return results

    @staticmethod
    def get_mint_token_price() -> dict:
        return dEuroAPIWrapper.get_prices()[list(dEuroAPIWrapper.mint_token.keys())[0]]

    @staticmethod
    def get_equity_token_price() -> dict:
        return dEuroAPIWrapper.get_prices()[list(dEuroAPIWrapper.equity_token.keys())[0]]

    @staticmethod
    def get_collateral_tokens_prices() -> dict:
        results: dict = {}
        prices: dict = dEuroAPIWrapper.get_prices()
        for collateral_token in dEuroAPIWrapper.collateral_token_list.keys():
            results[collateral_token] = prices[collateral_token]
        return results


if __name__ == "__main__":
    print(dEuroAPIWrapper.get_prices())