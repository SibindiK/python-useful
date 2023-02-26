class Menu:
    def __init__(self, available_drinks):
        self.available_drinks = available_drinks

    def get_items(self):
        """return names of all the available menu items"""
        items = ""
        for item in self.available_drinks:
            items += f"{item}/"
        return items

    def find_drink(self, order_name):
        """searches the menu for a particular drink by name.
        Returns a MenuItem object if it exists else returns none"""
        for item in self.available_drinks:
            if order_name == f"{item}":
                return item
        return None
