import pandas_ta as ta
from data.MarketDataRepository import MarketDataRepository
from pandas import Series


class IndicatorsCalculator:
    def __init__(self):
        self.market_data = MarketDataRepository()

    def get_50_moving_average(self, symbol, ticks):
        length = 50
        close_prices = Series(self.market_data.get_close_prices(symbol, limit=length + ticks))
        moving_average = ta.sma(close_prices, length).array[-ticks:]
        return moving_average

    def get_200_moving_average(self, symbol, ticks):
        length = 200
        close_prices = Series(self.market_data.get_close_prices(symbol, limit=length + ticks))
        moving_average = ta.sma(close_prices, length).array[-ticks:]
        return moving_average

    def get_rsi(self, symbol, ticks):
        length = 15
        close_prices = Series(self.market_data.get_close_prices(symbol, limit=length + ticks))
        rsi = ta.rsi(close_prices, length).array[-ticks:]
        return rsi

    def get_dmi(self, symbol):
        length = 50
        high_prices = Series(self.market_data.get_high_prices(symbol, limit=length + 1))
        low_prices = Series(self.market_data.get_low_prices(symbol, limit=length + 1))
        close_prices = Series(self.market_data.get_close_prices(symbol, limit=length + 1))
        dmi = ta.adx(high=high_prices, low=low_prices, close=close_prices, mamode="sma", length=length)["DMP_50"].array[-1]
        return dmi

