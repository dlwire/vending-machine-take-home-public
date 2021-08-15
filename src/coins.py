from typing import NamedTuple


class Coin(NamedTuple):
    material: str
    weight_g: float
    diameter_mm: float
    thickness_mm: float


ONE_DOLLAR_COIN: Coin = (
    'Manganese-Brass',
    8.1,
    26.49,
    2.00,
)

HALF_DOLLAR_COIN: Coin = (
    'Cupro-Nickel',
    11.340,
    30.61,
    2.15,
)

QUARTER_DOLLAR_COIN: Coin = (
    'Cupro-Nickel',
    5.670,
    24.26,
    1.75
)


COIN_VALUES = {
    ONE_DOLLAR_COIN: 100,
    HALF_DOLLAR_COIN: 50,
    QUARTER_DOLLAR_COIN: 25,
}
