from coins import Coin, COIN_VALUES


def evaluateCoin(coin: Coin) -> int:
    return COIN_VALUES[coin] if coin in COIN_VALUES else 0
