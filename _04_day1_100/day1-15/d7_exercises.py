#exercise 7.1 - choose ran dom word from list, ask user to guess a letter, check if letter is in word
import random
import os
from d7_hangman_guillotine import HANGMAN_PICS as hangman
from d7_hangman_words import hangman_words

#generate a random word from the list of hangman words
def generate_random_word(word_list):
    chosen_word = random.choice(word_list)
    return chosen_word

#generate a list of underscores to represent blank characters
def generate_blanks(word):
    blanks = []
    for index in range(len(word)):
         blanks += "_"
    return blanks

#check if a letter exists in a word
def  check_letter(char, word, blanks):
    found = False
    for count, letter in enumerate(word):
        if char == letter:
            blanks[count] = char
            found = True
    return blanks, found
def main():
    word_list = hangman_words
    lives = 6
    false_guesses = 0
    chosen_word = generate_random_word(word_list)
    blanks = generate_blanks(chosen_word)
    print(f"{chosen_word} {blanks}")
    completed = False
    while not completed:
        char = input("Guess a letter: ").lower()
        blanks, char_found = check_letter(char, chosen_word, blanks)
        print(blanks)
        if "_" not in blanks:
            print("Amazing, you've won!!")
            completed = True
        if not char_found:
            print(hangman[false_guesses])
            lives -= 1
            false_guesses += 1
            print(f"Sorry, {char} is not in the word, you have {lives} lives left")
            if lives == 0:
                print("Sorry you lose")
                completed = True

if __name__ == "__main__":
    main()