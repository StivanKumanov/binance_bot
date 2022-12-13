from services.IndicatorsCalculator import IndicatorsCalculator
from data.MarketDataRepository import MarketDataRepository
from binance.exceptions import BinanceAPIException


class TradeOrchestrator:
    def __init__(self):
        self.calculator = IndicatorsCalculator()
        self.market_data = MarketDataRepository()

    def _check_ma(self, ma_50s, ma_200s):
        if len(ma_50s) != len(ma_200s):
            raise ValueError("Length of both arguments should be equal!")

        length = len(ma_50s)
        result = True
        for i in range(length):
            if ma_200s[i] >= ma_50s[i]:
                result = False
                break

        return result

    def _check_rsi(self, rsi, symbol):
        highest_point = rsi.max()
        current_rsi = rsi[-1]
        prices = self.market_data.get_close_prices(symbol, limit=2)
        price_increased = prices[1] >= prices[0] * 1.2
        if current_rsi < highest_point and price_increased:
            return True
        return False

    def try_to_buy(self):
        min_daily_volume = 25000000
        symbols = self.market_data.get_futures_symbols(min_daily_volume)
        ticks = 25
        rsi_ticks = 50
        for symbol in symbols:
            try:
                ma_50 = self.calculator.get_50_moving_average(symbol, ticks)
                ma_200 = self.calculator.get_200_moving_average(symbol, ticks)
                # TODO: Last candle close
                dmi = self.calculator.get_dmi(symbol)
                rsi = self.calculator.get_rsi(symbol, rsi_ticks)
                should_buy = self.check_conditions(ma_50, ma_200, rsi, dmi, symbol)

                if should_buy:
                    pass
            except BinanceAPIException as ex:
                print(symbol, ex.message)

    def check_conditions(self, ma_50, ma_200, rsi, dmi, symbol):
        eligible_to_buy = self._check_ma(ma_50, ma_200) and self._check_rsi(rsi, symbol)
        return eligible_to_buy
