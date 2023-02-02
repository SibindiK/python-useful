# Author: Kermit Sibindi - 25/01/2023
# Purpose of this script is to demonstrate printing and basic string manipulation
# Code asks a user for the town they grew up in and their pet name then combines
# the two to suggest a band name  

def create_bandname(city, petname):
    return (city + " " + petname)

def main():
    city = input("What city/town/village did you grow up in: ")
    petname = input("What is/was the name of your pet:")
    print("Consider naming your band.... " + create_bandname(city, petname))

if __name__ == "__main__":
    main()