#################### BLACK JACK RULES #######################
# The deck is unlimited size
# There are no jokers
# The Jack/Queen/King all count as 10
# The Ace can count as 11 or 1
# All cards have equal probability of being drawn
# Cards are not removed from the deck after being drawn
#
#############################################################

import random


def get_card(cards_deck):
    '''return a random card from the given deck of cards'''
    card = random.choice(list(cards_deck))
    return card


def total_cards(cards_picked, cards_deck):
    '''total the given list of cards'''
    total = 0
    for card in cards_picked:
        total += cards_deck[card]
    return total


def show_final_result(result, player_cards, dealer_cards, cards_deck):
    '''display final result on screen'''
    print(
        f"You {result}, your final hand {player_cards}, score {total_cards(player_cards, cards_deck)}")
    print(
        f"Dealer's final hand: {dealer_cards}, score {total_cards(dealer_cards, cards_deck)}")


def show_inplay_cards(player_cards, dealer_cards, cards_deck):
    '''display inplay player and computer cards'''
    print(
        f"Your cards are [{player_cards[0]}] [{get_card(player_cards[1])}], current score {total_cards(player_cards, cards_deck)}")
    print(
        f"Dealer open card is [{dealer_cards[0]}], dealer score {total_cards(dealer_cards, cards_deck)}")


def play_black_jack(player_cards, dealer_cards, cards_deck):
    '''play the black jack game'''
    player_cards.append(get_card(cards_deck))
    player_cards.append(get_card(cards_deck))
    dealer_cards.append(get_card(cards_deck))
    show_inplay_cards(player_cards, dealer_cards, cards_deck)
    another_card = True
    count = 2
    while another_card:
        draw_again = input("Type'd' to draw again or 's' to stand: ")
        if draw_again == 'd':
            player_cards.append(get_card(cards_deck))
            print(f"You have drawn [{player_cards[-1]}]")
            count += 1
        elif draw_again == 's':
            # todo add logic for dealer to draw until total is over 17
            dealer_cards.append(get_card(cards_deck))
            print(f"Dealer hand is [{dealer_cards[-1]}]")
            player_total = total_cards(player_cards, cards_deck)
            dealer_total = total_cards(dealer_cards, cards_deck)
            if player_total > dealer_total and player_total < 22:
                show_final_result("WIN", player_cards,
                                  dealer_cards, cards_deck)
            elif player_total < dealer_total or player_total > 21:
                show_final_result("LOSE", player_cards,
                                  dealer_cards, cards_deck)
            elif player_total == dealer_total and player_total < 21:
                show_final_result("DRAW", player_cards,
                                  dealer_cards, cards_deck)

            another_card = False


def main():
    deck = {
        'A': 11,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'J': 10,
        'Q': 10,
        'K': 10,
    }

    another_game = True
    while another_game:
        play_game = input(
            "Do you want to play a game of BlackJack? Type 'y' or 'n': ").lower()
        if play_game == 'y':
            player_cards = []
            dealer_cards = []
            play_black_jack(player_cards, dealer_cards, deck)
        elif play_game == 'n':
            another_game = False


if __name__ == "__main__":
    main()
