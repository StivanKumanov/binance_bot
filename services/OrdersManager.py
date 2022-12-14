from binance.um_futures import UMFutures
import time
from binance.enums import *
import settings


class OrdersManager:
    def __init__(self):
        self.api_key = settings.BINANCE_API_KEY
        self.api_secret = settings.BINANCE_API_SECRET
        self.client = UMFutures(key=self.api_key, secret=self.api_secret, base_url="https://testnet.binancefuture.com")

    def open_short(self, symbol, activation_price):
        params = {
            "symbol": symbol,
            "type": "MARKET",
            # "activationPrice": activation_price,
            "side": "SELL",
            "positionSide": "SHORT",
            # "quantity": 0.1,
            # "price": settings.INITIAL_ORDER_AMOUNT,
            "timestamp": time.time(),
            "recvWindow": 600000
        }

        response = self.client.new_order(**params)
        pass

