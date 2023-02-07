import random

# pick a random element from a given list


def pick_random():
    names = input("Enter names separated by comma\n")
    names = names.split(", ")
    selection = random.randint(0, len(names)-1)
    print(f"{names[selection]} is going to pay the bill today")


def treasure_map():
    row1 = ["😒", "😒", "😒"]
    row2 = ["😒", "😒", "😒"]
    row3 = ["😒", "😒", "😒"]
    map = [row1, row2, row3]
    print(f"{row1}\n{row2}\n{row3}")
    # position should be column row eg 23 for column 2  row 3
    position = input(
        "Provide coordinate to put the treasure map in the form column row eg 13\n")
    column = int(position[0])
    row = int(position[1])
    map[row-1][column-1] = "🧊"
    print(f"{row1}\n{row2}\n{row3}")


def main():
    print("Welcome to day 4 Exercises.")
    print("1. Banker bill payment Roullete")
    print("2. Treasure Map")
    choice = input("Make Selection [1...5] ")
    if choice == '1':
        pick_random()
    elif choice == '2':
        treasure_map()
    else:
        print("Invalid menu option")


if __name__ == "__main__":
    main()
