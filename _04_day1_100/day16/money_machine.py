class MoneyMachine:
    def __init__(self):
        self.profit = 0

    def report(self):
        """Prints the current profit"""
        print(f"Money: £{self.profit}")


    #@ Parameter cost: (float) cost of the drink
    def make_payment(self, cost):
        """Return true if payment is accepted, or
        False if insufficient funds"""