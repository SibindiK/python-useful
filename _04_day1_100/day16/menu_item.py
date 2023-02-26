class MenuItem:
    def __init__(self, name, water, coffee, cost, milk=0):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "coffee": coffee,
            "milk": milk,
        }

    def __str__(self):
        return self.name



