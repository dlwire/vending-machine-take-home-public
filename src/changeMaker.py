from typing import List
from coins import Coin, NICKEL_COIN, DIME_COIN, QUARTER_DOLLAR_COIN


def makeChange(amount: int) -> List[Coin]:
    if amount == 5:
        return [NICKEL_COIN]
    elif amount == 10:
        return [DIME_COIN]
    elif amount == 25:
        return [QUARTER_DOLLAR_COIN]
    return []

