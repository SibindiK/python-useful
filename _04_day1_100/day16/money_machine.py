class MoneyMachine:
    def __init__(self):
        self.profit = 0

    def report(self):
        """Prints the current profit"""
        print(f"Money: £{self.profit}")

    def make_payment(self, cost):
        """Return true if payment is accepted, or
        False if insufficient funds"""
        # Parameter cost: (float) cost of the drink
        quarters = int(input("How many quarters: ")) * 0.25
        dimes = int(input("How many dimes: ")) * 0.1
        nickels = int(input("How many nickels: ")) * 0.05
        pennies = int(input("How many pennies: ")) * 0.01
        total = quarters + dimes + nickels + pennies
        if total < cost:
            print(f"Sorry, that's not enough money. ${round(total, 2)} refunded.")
            return False
        elif total > cost:
            self.profit += cost
            print(f"Here is ${round(total-cost, 2)} in change.")
            return True
