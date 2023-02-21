# welcome user to game
# ask user to select difficulty level
# ask user to enter a number
# compare user number to computer number
# tell user if too high or too low
# repeat until number of chances is 0
import random


def get_level():
    level = input("Type preferred game difficulty, 'hard' / 'easy'? ").lower()
    if level == 'hard':
        chances = 5
    elif level == 'easy':
        chances = 10
    return chances


def compare_numbers(u_num, c_num):
    is_match = False
    if u_num > c_num:
        print("Too High")
    elif u_num < c_num:
        print("Too Low")
    elif u_num == c_num:
        print("YOU GOT IT!!")
        is_match = True
    return is_match


print("Welcome to the number guessing game.")
print("I am thinking of a number between [1 and 100].")
comp_number = random.randint(1, 100)
lives = get_level()
print(f"number is {comp_number}")
print(f"You have {lives} attempts remaining to guess the number.")
user_number = int(input("Guess a number: "))
is_correct_guess = compare_numbers(user_number, comp_number)
while not is_correct_guess and lives > 1:
    lives -= 1
    if lives == 1:
        print(f"You have {lives} last attempt remaining to guess the number.")
    else:
        print(f"You have {lives} attempts remaining to guess the number.")
    user_number = int(input("Guess again: "))
    is_correct_guess = compare_numbers(user_number, comp_number)
