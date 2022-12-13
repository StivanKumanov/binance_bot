from data.MarketDataRepository import MarketDataRepository
from services.IndicatorsCalculator import IndicatorsCalculator
from services.TradeOrchestrator import TradeOrchestrator
from services.OrdersManager import OrdersManager

t = TradeOrchestrator()
o = OrdersManager()
# t.try_to_buy()
o.open_short("BCHUSDT")
