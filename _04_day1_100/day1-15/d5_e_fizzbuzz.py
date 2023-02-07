# FizzBuzz Script to print all numbers from 1 - 100
# if a number is divisible by 3, print fizz
# if a number is divisible by 5 print buzz
# if a number is divisible by both 3 and 5, print fizz buzz

def main():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)


if __name__ == "__main__":
    main()
