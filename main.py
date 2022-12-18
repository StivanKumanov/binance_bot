from data.MarketDataRepository import MarketDataRepository
from services.IndicatorsCalculator import IndicatorsCalculator
from services.TradeOrchestrator import TradeOrchestrator
from services.OrdersManager import OrdersManager
from data.AccountDataRepository import AccountDataRepository

m = MarketDataRepository()
i = IndicatorsCalculator(m)
a = AccountDataRepository()
o = OrdersManager()
t = TradeOrchestrator(i,o,m,a)
t.try_to_buy()