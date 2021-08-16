from typing import List
from coinEvaluator import evaluateCoin
from changeMaker import makeChange
from coins import Coin
from products import PRODUCT_COSTS


def centsToString(amount: int) -> str:
    return '${:01d}.{:02d}'.format(amount // 100, amount % 100)


class VendingMachine():
    def __init__(self) -> None:
        self.credit = 0
        self.coin_return = []
        self.display = 'INSERT COIN'
        self.product = ''

    def checkDisplay(self) -> str:
        display = self.display

        if self.credit:
            self.display = centsToString(self.credit)
        else:
            self.display = 'INSERT COIN'

        return display

    def insertCoin(self, coin: Coin) -> None:
        value = evaluateCoin(coin)
        if value:
            self.credit += value
            self.display = centsToString(self.credit)
        else:
            self.coin_return.append(coin)

    def order(self, product: str) -> None:
        if self.credit >= PRODUCT_COSTS[product]:
            self.product = product
            self.credit -= PRODUCT_COSTS[product]
            self.display = 'THANK YOU'
        else:
            cost = PRODUCT_COSTS[product]
            self.display = centsToString(cost)

    def retrieveChange(self) -> List[Coin]:
        self.coin_return.extend(makeChange(self.credit)[0])
        coin_return = self.coin_return[:]

        self.credit = 0
        self.coin_return = []

        return coin_return

    def retrieveProduct(self) -> str:
        product = self.product
        self.product = ''
        self.display = 'INSERT COIN'
        return product
