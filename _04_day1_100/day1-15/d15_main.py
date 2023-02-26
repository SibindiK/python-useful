from d15_menu import MENU, resources


def get_coins():
    """get user coins and total"""
    pound_coins = int(input("How many £1 coins? "))
    fifty_p_coins = int(input("How many 50p coins? "))
    twenty_p_coins = int(input("How many 20p coins? "))
    ten_p_coins = int(input("How many 10p coins? "))
    five_p_coins = int(input("How many 5p coins? "))
    return ((pound_coins * 1) + (fifty_p_coins * 0.5) + (twenty_p_coins * 0.2)
            + (ten_p_coins * 0.1) + (five_p_coins * 0.05))


def make_coffee(drink, money):
    """make the drink, reduce resources, add to resources money"""
    change = round(money - MENU[drink]['cost'], 2)
    resources["water"] -= MENU[drink]["ingredients"]["water"]
    resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
    if not drink == 'espresso':
        resources["milk"] -= MENU[drink]["ingredients"]["milk"]
    resources["money"] += MENU[drink]["cost"]
    print(f"Here is £{change} in change.")
    print(f"Here is your {drink}. Enjoy!")


def is_enough_resources(drink):
    """check if there are enough resources to make drink"""
    if MENU[drink]['ingredients']['water'] > resources['water']:
        print("Machine does not have enough water")
        return False
    elif MENU[drink]['ingredients']['coffee'] > resources['coffee']:
        print("Machine does not have enough coffee")
        return False
    if drink != "espresso":
        if MENU[drink]['ingredients']['milk'] > resources['milk']:
            print("Machine does not have enough milk")
            return False
    return True
def print_report():
    """display report on screen"""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: £{round(resources['money'], 2)}")


def main():
    machine_off = False
    while not machine_off:
        drink = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if drink == 'off':
            machine_off = True
        elif drink == 'report':
            print_report()
        elif drink not in MENU:
            print(f"{drink} is not available")
        else:
            user_money = get_coins()
            if user_money < MENU[drink]['cost']:
                print(f"Sorry that's not enough money. £{user_money} refunded !!!")
            else:
                if is_enough_resources(drink):
                    make_coffee(drink, user_money)
                else:
                    print(f"£{user_money} refunded !!!")
                    machine_off = True


if __name__ == "__main__":
    main()
