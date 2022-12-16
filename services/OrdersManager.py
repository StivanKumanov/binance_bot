from binance.um_futures import UMFutures
import time
from binance.enums import *
import settings


class OrdersManager:
    def __init__(self):
        self.api_key = settings.BINANCE_API_KEY
        self.api_secret = settings.BINANCE_API_SECRET
        self.client = UMFutures(key=self.api_key, secret=self.api_secret, base_url="https://testnet.binancefuture.com")

    def _get_quantity(self, coin_price, order_amount):
        qty = order_amount / coin_price
        return round(qty, 3)

    def open_short_trailing_stop(self, symbol, activation_price, current_price):
        params = {
            "symbol": symbol,
            "type": "TRAILING_STOP_MARKET",
            "callbackRate": 0.1,
            "activationPrice": round(activation_price, 2),
            "side": "SELL",
            "positionSide": "SHORT",
            "quantity": self._get_quantity(current_price, settings.INITIAL_ORDER_AMOUNT),
            "timestamp": time.time(),
            "recvWindow": 600000
        }

        response = self.client.new_order(**params)
        return response

    def _get_limit_order_params(self, symbol, price):
        params = {
            "symbol": symbol,
            "type": "LIMIT",
            "side": "SELL",
            "timeInForce": "GTC",
            "positionSide": "SHORT",
            "price": price,
            "quantity": self._get_quantity(price, settings.LIMIT_ORDER_AMOUNT),
            "timestamp": time.time(),
            "recvWindow": 600000

        }
        return params

    def open_limit_orders(self, count, symbol, current_price):
        if count > 5:
            raise ValueError("Count must be smaller than 5!")

        responses = []
        for i in range(count):
            current_price = round(current_price * 1.2, 2)
            order = self._get_limit_order_params(symbol, current_price)
            response = self.client.new_order(**order)
            responses.append(response)

        return responses

