from binance.client import Client


class MarketDataRepository:
    def __init__(self):
        self.client = Client()

    def get_futures_symbols(self, min_daily_volume):
        # TODO: filter by volume
        futures_exchange_info = self.client.futures_exchange_info()
        symbols = [info['symbol'] for info in futures_exchange_info['symbols'] if info['symbol'] != 'BTCUSDT'
                   and info['symbol'] != 'ETHUSDT']
        return symbols

    # TODO: think about using decimal instead of float

    def get_current_price(self, symbol):
        info = self.client.get_ticker(symbol=symbol)
        return float(info["lastPrice"])

    def get_close_prices(self, symbol, interval='4h', limit=50):
        klines_data = self.client.get_klines(symbol=symbol, interval=interval, limit=limit)
        close_price_index = 4
        close_prices = [float(x[close_price_index]) for x in klines_data]
        return close_prices

    def get_high_prices(self, symbol, interval='4h', limit=50):
        klines_data = self.client.get_klines(symbol=symbol, interval=interval, limit=limit)
        high_price_index = 2
        high_prices = [float(x[high_price_index]) for x in klines_data]
        return high_prices

    def get_low_prices(self, symbol, interval='4h', limit=50):
        klines_data = self.client.get_klines(symbol=symbol, interval=interval, limit=limit)
        low_price_index = 3
        low_prices = [float(x[low_price_index]) for x in klines_data]
        return low_prices


