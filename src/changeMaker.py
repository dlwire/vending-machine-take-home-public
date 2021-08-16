from typing import List
from coins import Coin, COIN_VALUES


SORTED_COINS = [(coin, value) for coin, value in COIN_VALUES.items()]
SORTED_COINS.sort(key=lambda x: x[1], reverse=True)


def makeChange(amount: int) -> List[Coin]:
    change = []

    coin_length = len(SORTED_COINS)
    coin_index = 0
    while amount > 0 and coin_index < coin_length:
        while coin_index < coin_length and SORTED_COINS[coin_index][1] > amount:
            coin_index += 1

        if coin_index < coin_length:
            coin, value = SORTED_COINS[coin_index]
            change.append(coin)
            amount -= value

    return change
