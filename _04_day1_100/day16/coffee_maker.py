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

    #Parameter drink: MenuItem The MenuItem object to make
    def is_resource_sufficient(self, drink):
        """Returns true when drink order can be made.
        False if ingredients are insufficient"""
        for resource in drink.ingredients:
        #TODO 1: iterate through resources
        #     if self.resource < drink.ingredients[resource]:
        #         print(f"Not enough {resource}")
        #         return False
        # return True
            print(f"{resource}: {drink.ingredients[resource]}")
        print(dir(drink))

