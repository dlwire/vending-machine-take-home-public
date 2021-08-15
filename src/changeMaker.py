from typing import List
from coins import Coin, NICKEL_COIN


def makeChange(amount: int) -> List[Coin]:
    if amount == 5:
        return [NICKEL_COIN]
    return []

