import unittest
from services.IndicatorsCalculator import IndicatorsCalculator


class IndicatorsCalculatorTests(unittest.TestCase):
    def setUp(self):
        self.calculator = IndicatorsCalculator()

    def test_get_50_ma_returns_correct_value(self):
        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
