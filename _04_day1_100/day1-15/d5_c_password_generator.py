# Script to generate passwords
# ask user how many letters they would like in their password
# ask how many symbols
# ask how many numbers
# generate password

import random

# return a random character


def get_letter():
    letter = [chr(random.randint(65, 91)), chr(random.randint(97, 123))]
    return random.choice(letter)


# return a random symbol


def get_symbol():
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    selected = random.randint(0, len(symbols)-1)
    return symbols[selected]


def main():
    no_of_letters = int(
        input("How many letters do you want in your password?\n"))
    no_of_digits = int(
        input("How many digits do you want in your password?\n"))
    no_of_symbols = int(
        input("How many symbols do you want in your password?\n"))

    password = ""

    for n in range(0, no_of_letters):
        password += get_letter()

    for n in range(0, no_of_digits):
        password += str(random.randint(0, 9))

    for n in range(0, no_of_symbols):
        password += get_symbol()

    # reshuffle all characters in string
    password = ''.join(random.sample(password, len(password)))
    print(f"Suggested passoword is {password}")


if __name__ == "__main__":
    main()
