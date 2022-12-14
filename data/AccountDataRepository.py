import settings
from binance.client import Client
from binance.um_futures import UMFutures
import time


class AccountDataRepository:
    def __init__(self):
        # self.client = Client(settings.BINANCE_API_KEY, settings.BINANCE_API_SECRET, testnet=True)
        self.client = UMFutures(settings.BINANCE_API_KEY, settings.BINANCE_API_SECRET, base_url="https://testnet.binancefuture.com")


    def get_orders(self):
        params = {
            "timestamp": time.time(),
            "recvWindow": 600000
        }
        orders = self.client.get_orders(**params)
        pass