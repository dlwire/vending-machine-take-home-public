from typing import List, NamedTuple


class Coin(NamedTuple):
    material: str
    weight_g: float
    diameter_mm: float
    thickness_mm: float


AMERICAN_INNOVATION_1_COIN = (
    'Manganese-Brass',
    8.1,
    26.49,
    2.00,
)


class VendingMachine():
    def __init__(self) -> None:
        self.credit = 0.00
        self.coin_return = []
        self.display = 'INSERT COIN'
        self.product = ''

    def checkDisplay(self) -> str:
        return self.display

    def insertCoin(self, coin: Coin):
        if coin == AMERICAN_INNOVATION_1_COIN:
            self.credit = 1
        else:
            self.coin_return.append(coin)

    def orderCola(self) -> None:
        if self.credit >= 1.00:
            self.product = 'cola'
            self.credit -= 1.00
            self.display = 'THANK YOU'

    def retrieveChange(self) -> List[Coin]:
        coin_return = self.coin_return[:]
        self.coin_return = []
        return coin_return

    def retrieveProduct(self) -> str:
        product = self.product
        self.product = ''
        self.display = 'INSERT COIN'
        return product
