import settings
from binance.client import Client
from binance.um_futures import UMFutures
import time


class AccountDataRepository:
    def __init__(self):
        self.client = UMFutures(settings.BINANCE_API_KEY, settings.BINANCE_API_SECRET, base_url="https://testnet.binancefuture.com")

    def get_account_positions(self):
        params = {
            "timestamp": time.time(),
            "recvWindow": 600000
        }
        all_positions = self.client.account(**params)["positions"]
        account_positions = []
        for position in all_positions:
            entry_price = float(position['entryPrice'])
            if entry_price > 0:
                account_positions.append(position)

        return account_positions
