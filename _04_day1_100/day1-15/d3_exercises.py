#check if a number is even
def is_num_even():
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is an odd number")

#check height and age to determine price and if person is allowed on rollercoaster
def rollercoaster():
    height = int(input("How tall are you in cm\n"))
    age = int(input("How old are you\n"))
    price = 0
    if height > 120:
        if age < 12:
            price = 5
        elif age <= 18:
            price = 7
        elif age >= 45 and age <= 55:
            print("Everything is going to be alright, have a ride on us")
        else:
            price = 12
        print(f"Price  for your ticket is £{price}")
    else:
        print("Your height does not meet the minimum safety height")


#calculate bmi and provide an intepretation
def bmi_upgrade():
    weight = float(input("Weight in kg?\n"))
    height = float(input("Height in m?\n"))

    bmi = round(weight / height ** 2)
    message = " "
    if bmi < 18.5:
        message = "you are underweight"
    elif bmi < 25:
        message = "you have a normal weight"
    elif bmi < 30:
        message = "you are overweight"
    elif bmi < 35:
        message = "you are obese"
    else:
        message = "you are clinically obese"
    print(f"Your BMI is {bmi}, {message}")

#check if a given year is a leap year using the following rules
#1. year is evenly divisible by 4 but not 100 unless if also evenly divisible by 400
def is_leap_year():
    year = int(input("Enter year: "))
    if int(year) % 4 == 0:
        if int(year) % 100 == 0:
            if int(year) % 400 == 0:
                print(f"{year} is a leap year")
            else:
                print(f"{year} is not a leap year")
        else:
            print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")


#calculate the price of a pizza
def order_pizza():
    price = 0
    small = 15
    medium = 20
    large = 25
    pepperoni_small = 2
    pepperoni_large = 3
    cheese = 1
    print("Welcome to Python Pizza deliveries")
    size = input("what size pizza do you want? S, M, L\n")
    if size == 'S':
        price = small
    elif size == 'M':
        price = medium
    elif size == 'L':
        price = large
    pepperoni = input("Do you want pepperoni? Y, N\n")
    if pepperoni == 'Y':
        if size == 'S':
            price += pepperoni_small
        else:
            price += pepperoni_large
    cheesy = input("Do you want cheese? Y, N\n")
    if cheesy == 'Y':
        price += cheese
    print(f"Your pizza will cost £{price}")


def main():
    print("WELCOME TO DAY 3 EXERCISES. CHOOSE AN OPTION")
    print("1. Even number checker")
    print("2. Rollercoaster prices")
    print("3. Leap year checker")
    print("4. BMI calculator")
    print("5. Pizza Orders")
    print("9. Quit")
    option = int(input("Selection : "))
    if option == 1:
        is_num_even()
    elif option == 2:
        rollercoaster()
    elif option == 3:
        is_leap_year()
    elif option == 4:
        bmi_upgrade()
    elif option == 5:
        order_pizza()
    else:
        print("Invalid option selected")


if __name__ == "__main__":
    main()
