import unittest
from coinEvaluator import evaluateCoin, AMERICAN_INNOVATION_1_COIN


class CoinEvaluatorTest(unittest.TestCase):
    def test_DollarCoins(self):
        self.assertEqual(evaluateCoin(AMERICAN_INNOVATION_1_COIN), 100)

    def test_invalidCoin(self):
        self.assertEqual(evaluateCoin(()), 0)