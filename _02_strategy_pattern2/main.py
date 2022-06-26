#demonstrate strategy pattern by passing in strategies as functions,
#Pythonic because python allows passing of functions as variables  
def execute_strategy(func=None):
    if (func == None):
        print("Strategy not found")
    print(func)

def add_strategy(arg1, arg2):
    return (arg1 + arg2)

def subtract_strategy(arg1, arg2):
    return (arg1 - arg2)

def main():
    execute_strategy()
    execute_strategy(add_strategy(10, 20))
    execute_strategy(subtract_strategy(10, 20))

if __name__ == "__main__":
    main()
