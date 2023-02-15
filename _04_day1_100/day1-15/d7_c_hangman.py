# hangman game
def display_start():
    print("\t  +-----+")
    print("\t  |     |")
    print("\t  |     O")
    for count in range(3):
        print("\t  |")
    print("\t===============")


def main():
    display_start()


if __name__ == "__main__":
    main()
