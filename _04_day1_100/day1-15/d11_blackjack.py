import random


def get_card(cards_deck):
    '''pick a random card from a given deck of cards'''
    card = random.choice(list(cards_deck))
    return card


def total_cards(cards_picked, cards_deck):
    '''total the given list of cards'''
    total = 0
    for card in cards_picked:
        total += cards_deck[card]
    return total


def main():
    deck = {
        'A': 1,
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

    player_cards = []
    dealer_cards = []
    player_cards.append(get_card(deck))
    player_cards.append(get_card(deck))
    print(f"Your cards are [{player_cards[0]}] [{get_card(player_cards[1])}] ")
    dealer_cards.append(get_card(deck))
    print(f"Dealer open card is [{dealer_cards[0]}] ")
    another_card = True
    count = 2
    while another_card:
        draw_again = input("Type'd' to draw again or 's' to stand: ")
        if draw_again == 'd':
            player_cards.append(get_card(deck))
            print(f"You have drawn [{player_cards[-1]}]")
            count += 1
        elif draw_again == 's':
            dealer_cards.append(get_card(deck))
            print(f"Dealer second card is [{dealer_cards[-1]}]")
            player_total = total_cards(player_cards, deck)
            dealer_total = total_cards(dealer_cards, deck)
            if player_total > dealer_total:
                print(
                    f"You WIN, your cards total {player_total} and Dealer's cards total {dealer_total}")
            elif player_total < dealer_total:
                print(
                    f"You LOSE, your cards total {player_total} and Dealer's cards total {dealer_total}")
            another_card = False


if __name__ == "__main__":
    main()
