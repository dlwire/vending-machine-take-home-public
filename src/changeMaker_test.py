import unittest
from changeMaker import makeChange
from coins import NICKEL_COIN, DIME_COIN, QUARTER_DOLLAR_COIN


class ChangeMakerTest(unittest.TestCase):
    def test_make_change_for_5_cents(self):
        self.assertEqual(makeChange(5), [NICKEL_COIN])

    def test_make_change_for_10_cents(self):
        self.assertEqual(makeChange(10), [DIME_COIN])

    def test_make_change_for_25_cents(self):
        self.assertEqual(makeChange(25), [QUARTER_DOLLAR_COIN])
