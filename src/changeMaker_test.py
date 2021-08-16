import unittest
from changeMaker import makeChange
from coins import (
    NICKEL_COIN,
    DIME_COIN,
    QUARTER_DOLLAR_COIN,
    HALF_DOLLAR_COIN,
    ONE_DOLLAR_COIN,
)


class ChangeMakerTest(unittest.TestCase):
    def test_make_change_for_5_cents(self):
        self.assertEqual(makeChange(5), [NICKEL_COIN])

    def test_make_change_for_10_cents(self):
        self.assertEqual(makeChange(10), [DIME_COIN])

    def test_make_change_for_25_cents(self):
        self.assertEqual(makeChange(25), [QUARTER_DOLLAR_COIN])

    def test_make_change_for_50_cents(self):
        self.assertEqual(makeChange(50), [HALF_DOLLAR_COIN])

    def test_make_change_for_100_cents(self):
        self.assertEqual(makeChange(100), [ONE_DOLLAR_COIN])

    def test_make_change_for_65_cents(self):
        self.assertEqual(makeChange(65), [HALF_DOLLAR_COIN, DIME_COIN, NICKEL_COIN])

    def test_bad_value(self):
        self.assertEqual(makeChange(1), [])
