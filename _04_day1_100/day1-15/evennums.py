# check if a given number is even

def is_num_even(num):
    if (num % 2 == 0):
        return True
    else:
        return False


def main():
    number = int(input("Enter a number: "))
    if (is_num_even(number)):
        print(f"{number} is even")
    else:
        print(f"{number} is an odd number")


if __name__ == "__main__":
    main()
