#treasure island game to demonstrate conditionals
#def left_or_right():
def main():
    print("Welcome to Treasure Island. Your mission is to find the treasure.")
    left_or_right = input("You're at a crossroads, where do you want to go 'left' or 'right'?\n")
    if left_or_right.lower() == "right":
        print("Oh no, you've fallen into a sinkhole...Game Over!!!")
    elif left_or_right.lower() == "left":
        swim_or_wait = input("You have arrived at a lake, do you 'swim' or 'wait'?\n")
        if swim_or_wait.lower() == "swim":
            print("Oh no, this is a crocodile infested lake. You've been chowed. Game Over!!!")
        elif swim_or_wait.lower() == "wait":
            door = input("Which door. 'red', 'yellow' or 'blue'?\n")
            if door.lower() == "red" or door.lower() == "blue":
                print("Game Over!!!")
            elif door.lower() == "yellow":
                print("Huzzah, you've found the treasure!!")    
        else:
            print("Invalid option, try again!!")
    else:
        print("Invalid option, try again!!")

if __name__ == "__main__":
    main()