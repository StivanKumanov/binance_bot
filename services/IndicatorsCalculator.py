import pandas_ta as ta
from data.MarketDataRepository import MarketDataRepository
from pandas import Series


class IndicatorsCalculator:
    def __init__(self):
        self.market_data = MarketDataRepository()

    def get_50_moving_average(self, symbol):
        close_prices = Series(self.market_data.get_close_prices(symbol))
        moving_average = ta.sma(close_prices, 50).array[-1]
        return moving_average

    def get_200_moving_average(self, symbol):
        length = 200
        close_prices = Series(self.market_data.get_close_prices(symbol, limit=length))
        moving_average = ta.sma(close_prices, length).array[-1]
        return moving_average

    def get_rsi(self, symbol):
        # TODO: configure the length parameter
        length = 50
        close_prices = Series(self.market_data.get_close_prices(symbol, limit=51))
        rsi = ta.rsi(close_prices, length)
        return rsi

    def get_dmi(self, symbol):
        length = 50
        high_prices = Series(self.market_data.get_high_prices(symbol, limit=70))
        low_prices = Series(self.market_data.get_low_prices(symbol, limit=70))
        dmi = ta.dm(high_prices, low_prices, length)
        print(dmi)
        return dmi

