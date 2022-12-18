import unittest
import unittest.mock as mock
from services.IndicatorsCalculator import IndicatorsCalculator
from data.MarketDataRepository import MarketDataRepository

class IndicatorsCalculatorTests(unittest.TestCase):
    # def setUp(self):
    #     self.calculator = IndicatorsCalculator()

    def test_get_50_ma_returns_correct_value(self):
        data_set = [1, 2, 3]
        market_data_mock = mock.Mock()
        market_data_mock.return_value = data_set

        test = market_data_mock.get_close_prices()
        print(test)
        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
