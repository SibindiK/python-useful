import random

#pick a random element from a given list
def pick_random(my_list):
    selection = random.randint(0, len(my_list)-1)
    return (my_list[selection])

def main():
    names = input("Enter names separated by comma\n")
    names = names.split(", ")
    print(f"{pick_random(names)} is going to pay the bill today")

if __name__ == "__main__":
    main()