from coffee_maker import CoffeeMaker
from menu_item import MenuItem
from menu import Menu
from money_machine import MoneyMachine


def main():
    drinks = [MenuItem("espresso", 50, 18, 1.5),
              MenuItem("latte", 200, 24, 2.5, 150),
              MenuItem("cappuccino", 250, 24, 3, 100)]
    menu = Menu(drinks)
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    is_off = False
    while not is_off:
        choice = input(f"What would you like {menu.get_items()}: ").lower()
        if choice == "off":
            is_off = True
        elif choice == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            drink = menu.find_drink(choice)
            if drink is not None:
                if coffee_maker.is_resource_sufficient(drink, coffee_maker) and money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)


if __name__ == "__main__":
    main()
