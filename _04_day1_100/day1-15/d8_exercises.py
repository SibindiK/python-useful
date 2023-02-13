#functions
import math
#calculate the number of paint cans required given a wall height and width
def paint_area_calculator(height, width,  coverage):
    wall_area = height * width
    return math.ceil(wall_area / coverage)

#check if a number is prime
def prime_number_checker(n):
    prime = True
    for i in range(2, n):
        if n % i == 0:
            prime = False
            break
    return prime

def main():
    choice = -1
    while choice != 0:
        print("1. How many cans of paint required")
        print("2. Prime number checker")
        choice = int(input("Select menu choice or 0 to quit\n"))
        if choice == 1:
            height = float(input("Height of wall? \n"))
            width = float(input("Width of wall?\n"))
            coverage = 5 #wall area covered by one can of paint
            print(f"You will need {paint_area_calculator(height, width, coverage)} cans of paint")
        elif choice == 2:
            number = int(input("Enter number: "))
            if prime_number_checker(number):
                print(f"It's a prime number {number}")
            else:
                print(f"It's not a prime number {number} is a composite number")
        elif choice == 0:
            print("Thank you for taking part, Goodbye")





if __name__ == "__main__":
    main()
