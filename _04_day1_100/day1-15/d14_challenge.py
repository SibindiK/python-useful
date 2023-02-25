# import openpyxl
# import xlrd

# path = str("../data/WUP2018-F13-Capital_Cities.xls")
# try:
#     wb = xlrd.open_workbook(path.strip())
#     ws = wb.sheet_by_index(0)

#     print(f"{wb.nsheets}")
#     print(f"{wb.sheet_names()}")

#     for sheet in wb.sheets():
#         print(sheet)

#     #for row in range(2, max_row+1):
# except Exception as e:
#     print(e)
from d14_data import capital_cities
import random


# randomly select a city from list of available cities
def select_city():
    city = random.choice(capital_cities)
    return city


# check if the currently selected city has already been used in the game
def was_already_selected(city, selected_cities):
    if city in selected_cities:
        return True
    else:
        return False


# compare the population of currently active city and the next city
def compare_populations(active_city, next_city):
    if active_city["population"] > next_city["population"]:
        return "lower"
    else:
        return "higher"


# play the higher or lower game
def play_game(cities_selected, active_city, score):
    next_city = select_city()
    while was_already_selected(next_city['city'], cities_selected):
        next_city = select_city()

    response = input(
        f"is {next_city['city']} population 'higher' or 'lower' than {active_city['city']}\n").lower()
    if response == compare_populations(active_city, next_city):
        score += 1
        print(
            f"That's correct. {next_city['city']} has a population of {next_city['population']:,}")
        print(
            f"and {active_city['city']} has a population of {active_city['population']:,}")
        cities_selected.append(next_city['city'])
        active_city = next_city
        score = play_game(cities_selected, active_city, score)
    else:
        print(
            f"That's wrong. {next_city['city']} has a population of {next_city['population']:,}")
        print(
            f"and {active_city['city']} has a population of {active_city['population']:,}")
    return score


def main():
    play_again = True
    score = 0
    while play_again:
        cities_selected = []
        print("Welcome to higher or lower game")
        active_city = select_city()
        cities_selected.append(active_city['city'])
        print(f"Final Score {play_game(cities_selected, active_city, score)}")
        another_round = input(
            "Type 'yes' to play again or 'no' to quit game: ").lower()
        if another_round == 'no':
            print("Thank you for playing. Goodbye!!!")
            play_again = False


if __name__ == "__main__":
    main()
