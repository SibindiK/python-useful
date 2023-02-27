class CoffeeMaker:
    def __init__(self):
        self.water = 300
        self.coffee = 100
        self.milk = 200

    def report(self):
        """prints a report of all resources"""
        print(f"Water: {self.water}ml")
        print(f"Milk: {self.milk}ml")
        print(f"Coffee: {self.coffee}g")

    def is_resource_sufficient(self, drink, c_maker):
        """Returns true when drink order can be made.
        False if ingredients are insufficient"""
        # Parameter drink: MenuItem The MenuItem object to make
        is_enough = True
        for resource in drink.ingredients:
            if vars(c_maker)[resource] < drink.ingredients[resource]:
                print(f"Not enough {resource}")
                is_enough = False
        return is_enough

    def make_coffee(self, order):
        self.water -= order.ingredients['water']
        self.coffee -= order.ingredients['coffee']
        self.milk -= order.ingredients['milk']
        print(f"Here is your {order}. Enjoy!")
