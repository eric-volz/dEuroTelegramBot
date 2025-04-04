from web3 import Web3
from web3.providers.base import BaseProvider



class Web3Provider(BaseProvider):
    def __init__(self, providers: list[Web3.HTTPProvider]):
        super().__init__()
        self.providers: list[Web3.HTTPProvider] = providers
        self.last_id: int = 0
        self.chain_id: str = ""

        # Test connection to providers
        for provider in self.providers:
            if not provider.is_connected():
                self.providers.remove(provider)
                continue

        if not self.providers:
            raise RuntimeError("Could not connect to any RPC")

    def get_chain_id(self) -> dict:
        return {'jsonrpc': '2.0', 'id': self.last_id + 1, 'result': self.chain_id}

    def make_request(self, method, params):
        if method == "eth_chainId" and self.chain_id:
            response: dict = self.get_chain_id()
            self.last_id += 1
            return response

        for provider in self.providers:
            try:
                data = provider.make_request(method, params)
                if method == "eth_chainId":
                    self.chain_id = data["result"]
                self.last_id = data['id']
                if "error" in data:
                    continue
                return data
            except Exception as e:
                continue
        raise Exception("All providers failed")