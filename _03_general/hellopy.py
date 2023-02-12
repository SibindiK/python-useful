#create an empty list and populate it with user's choice of animals
def get_animals():
    animals = []
    no_of_animals = int(input("How many animals do you have?"))
    x = 0;
    while (x < no_of_animals):
        animals.insert(x, input("Enter animal type eg lion "))
        x+=1
    return animals

#printing list items and their position in the list
def seasons():
    seasons = ["Winter", "Spring", "Summer", "Fall"]
    count = 1
    for season in seasons:
        print(f"{count} {season}")
        count+=1
def main():
    choice = -1
    while (choice != 0):
        print("1. Tell us about your animals")
        print("2. Seasons")
        choice = int(input("Select Menu Option [1..] or 0 to quit\n"))
        if choice == 1:
            print(get_animals())
        elif choice == 2:
            seasons()
        elif choice == 0:
            print("Thank  you for taking part, Goodbye!!")

if __name__ == "__main__":
    main()
