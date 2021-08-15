from typing import NamedTuple


class Coin(NamedTuple):
    material: str
    weight_g: float
    diameter_mm: float
    thickness_mm: float


AMERICAN_INNOVATION_1_COIN: Coin = (
    'Manganese-Brass',
    8.1,
    26.49,
    2.00,
)


def evaluateCoin(coin: Coin) -> int:
    if coin == AMERICAN_INNOVATION_1_COIN:
        return 100
    return 0