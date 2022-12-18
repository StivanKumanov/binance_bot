from binance.exceptions import BinanceAPIException
from binance.error import ClientError
import logging

class TradeOrchestrator:
    def __init__(self, calculator, orders_manager, market_data, account_data):
        self.calculator = calculator
        self.orders_manager = orders_manager
        self.market_data = market_data
        self.account_data = account_data

    def try_to_buy(self):
        min_daily_volume = 1000000
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
                should_buy = self._check_conditions(ma_50, ma_200, rsi, dmi, symbol)

                if should_buy:
                    activation_price = ma_200[-1]
                    current_price = self.market_data.get_current_price(symbol)
                    tr_stop_order_response = self.orders_manager.open_short_trailing_stop(symbol, activation_price, current_price)
                    limit_order_response = self.orders_manager.open_limit_orders(3, symbol, current_price)
                    logging.info(tr_stop_order_response, limit_order_response)
                else:
                    print(symbol)

            except BinanceAPIException as ex:
                logging.error(symbol, ex.message)

            except ClientError as ex:
                logging.error(symbol, ex)

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
        rsi_and_price = self.calculator.get_rsi_and_price(symbol, rsi)
        highest_rsi = rsi_and_price["highest_rsi"]
        current_rsi = rsi_and_price["current_price"]
        price_at_rsi = rsi_and_price["price_at_rsi"]
        current_price = rsi_and_price["current_price"]

        price_increased = current_price >= price_at_rsi * 1.2
        if current_rsi < highest_rsi and price_increased:
            return True
        return False

    def _check_dmi(self, dmi):
        return True

    def _check_positions_count(self):
        positions = self.account_data.get_account_positions()
        if len(positions) <= 5:
            return True
        return False


    def _check_conditions(self, ma_50, ma_200, rsi, dmi, symbol):
        less_than_5_positions = self._check_positions_count()
        eligible_to_buy = self._check_ma(ma_50, ma_200) and self._check_rsi(rsi, symbol) and less_than_5_positions and self._check_dmi(dmi)
        return eligible_to_buy
