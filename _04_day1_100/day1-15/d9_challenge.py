# blind auction
# get user name (key)
# get bid (value)

# get user details for a new bid
def get_new_bid():
    name = input("What is your name?: ")
    price = float(input("What's your bid?: £"))
    return (name, price)

# Find the highest bid from the dictionary of bidders


def get_highest_bid(bidders):
    highest_bid = 0
    highest_bidder = ()
    for bidder in bidders:
        if bidders[bidder] > highest_bid:
            highest_bid = bidders[bidder]
            highest_bidder = (bidder, bidders[bidder])
    return highest_bidder


def main():
    bids = {}
    another_bid = True
    while another_bid:
        add_bid = input("Type [y] for another bid or [n] to quit: ").lower()
        if add_bid == 'y':
            new_bidder = get_new_bid()
            bids[new_bidder[0]] = new_bidder[1]
        elif add_bid == 'n':
            another_bid = False
            if len(bids) > 0:
                print("===========================")
                print("\tBIDS RECEIVED")
                print("===========================")
                for bidder in bids:
                    print(f"{bidder} bid £{bids[bidder]}")
                print("=====HIGHEST BID======")
                winner = get_highest_bid(bids)
                print(f"The winner is {winner[0]} wih a bid of £{winner[1]}")
            else:
                print("No bids entered")
        else:
            print("Invalid choice, TRY AGAIN!!")


if __name__ == "__main__":
    main()
