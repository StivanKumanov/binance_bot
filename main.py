from data.MarketDataRepository import MarketDataRepository
from services.IndicatorsCalculator import IndicatorsCalculator
from services.TradeOrchestrator import TradeOrchestrator
from services.OrdersManager import OrdersManager
from data.AccountDataRepository import AccountDataRepository


t = TradeOrchestrator()
a = AccountDataRepository()
o = OrdersManager()
# t.try_to_buy()
# o.open_short("BCHUSDT", 0)
t = a.get_orders()