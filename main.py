from data.MarketDataRepository import MarketDataRepository
from services.IndicatorsCalculator import IndicatorsCalculator

repo = MarketDataRepository()
symbol = 'BTCUSDT'
test = IndicatorsCalculator()
# ma = test.get_50_moving_average(symbol)
# ma200 = test.get_200_moving_average(symbol)
rsi = test.get_rsi(symbol)