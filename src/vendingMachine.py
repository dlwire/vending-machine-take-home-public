class VendingMachine():
    def __init__(self) -> None:
        self.display = 'INSERT COIN'
        self.product = ''

    def checkDisplay(self) -> str:
        return self.display

    def retrieveProduct(self) -> str:
        return self.product
