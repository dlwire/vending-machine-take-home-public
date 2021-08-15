from typing import List
from coinEvaluator import evaluateCoin, Coin

class VendingMachine():
    def __init__(self) -> None:
        self.credit = 0
        self.coin_return = []
        self.display = 'INSERT COIN'
        self.product = ''

    def checkDisplay(self) -> str:
        return self.display

    def insertCoin(self, coin: Coin) -> None:
        value = evaluateCoin(coin)
        if value:
            self.credit += value
        else:
            self.coin_return.append(coin)

    def orderCola(self) -> None:
        if self.credit >= 100:
            self.product = 'cola'
            self.credit -= 100
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
