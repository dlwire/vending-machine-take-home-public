import unittest
from coinEvaluator import evaluateCoin
from coins import (
    ONE_DOLLAR_COIN,
    HALF_DOLLAR_COIN,
    QUARTER_DOLLAR_COIN,
    DIME_COIN,
    NICKEL_COIN,
)


class CoinEvaluatorTest(unittest.TestCase):
    def test_DollarCoin(self):
        self.assertEqual(evaluateCoin(ONE_DOLLAR_COIN), 100)

    def test_HalfDollarCoin(self):
        self.assertEqual(evaluateCoin(HALF_DOLLAR_COIN), 50)

    def test_QuarterDollarCoin(self):
        self.assertEqual(evaluateCoin(QUARTER_DOLLAR_COIN), 25)

    def test_DimeCoin(self):
        self.assertEqual(evaluateCoin(DIME_COIN), 10)

    def test_NickelCoin(self):
        self.assertEqual(evaluateCoin(NICKEL_COIN), 5)

    def test_invalidCoin(self):
        self.assertEqual(evaluateCoin(('', 1, 1, 1)), 0)
