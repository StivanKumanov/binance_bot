from services.IndicatorsCalculator import IndicatorsCalculator
from data.MarketDataRepository import MarketDataRepository
from binance.exceptions import BinanceAPIException


class TradeOrchestrator:
    def __init__(self):
        self.calculator = IndicatorsCalculator()
        self.market_data = MarketDataRepository()

    def _compare_ma(self, ma_50s, ma_200s):
        if len(ma_50s) != len(ma_200s):
            raise ValueError("Length of both arguments should be equal!")

        length = len(ma_50s)
        result = True
        for i in range(length):
            if ma_200s[i] >= ma_50s[i]:
                result = False
                break

        return result

    def try_to_buy(self):
        symbols = self.market_data.get_futures_symbols()
        ticks = 25
        rsi_ticks = 50
        for symbol in symbols:
            try:
                ma_50 = self.calculator.get_50_moving_average(symbol, ticks)
                ma_200 = self.calculator.get_200_moving_average(symbol, ticks)
                dmi = self.calculator.get_dmi(symbol)
                rsi = self.calculator.get_rsi(symbol, rsi_ticks)
                should_buy = self.check_conditions(ma_50, ma_200, 0, 0)
            except BinanceAPIException as ex:
                print(symbol, ex.message)

    def check_conditions(self, ma_50, ma_200, rsi, dmi):
        eligible_to_buy = self._compare_ma(ma_50, ma_200)
        return eligible_to_buy
