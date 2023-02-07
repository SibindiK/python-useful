import random
rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
'''
paper = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
'''
scissors = '''
        _______
    ---'   ____)____
            ________)
           ____________)
          (_____)
    ---.__(___)
'''


def main():
    tie_text = "IT'S A TIE!!! GO AGAIN"
    lose_text = "SORRY, YOU LOSE!!!"
    win_text = "YAAY BIG DOG....YOU'VE WON!!!"
    player_choice = input("Rock, Paper or Scissors?\n").lower()
    computer_choice = random.randint(0, 2)
    print("Computer Selected")
    if computer_choice == 0:
        print(rock)
        if player_choice == "rock":
            print(tie_text)
        elif player_choice == "paper":
            print(win_text)
        elif player_choice == "scissors":
            print(lose_text)
    elif computer_choice == 1:
        print(paper)
        if player_choice == "rock":
            print(lose_text)
        elif player_choice == "paper":
            print(tie_text)
        elif player_choice == "scissors":
            print(win_text)
    elif computer_choice == 2:
        print(scissors)
        if player_choice == "rock":
            print(win_text)
        elif player_choice == "paper":
            print(lose_text)
        elif player_choice == "scissors":
            print(tie_text)
        
if __name__ == "__main__":
    main()
