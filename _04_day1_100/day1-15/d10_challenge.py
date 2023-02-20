# calculator

def add(fnum, snum):
    '''Add two numbers'''
    return fnum + snum


def subtract(fnum, snum):
    '''Subtract two numbers'''
    return fnum - snum


def multiply(fnum, snum):
    '''multiply two numbers'''
    return fnum * snum


def divide(fnum, snum):
    '''divide two numbers'''
    return fnum / snum


def main():
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }
    another_calculation = True
    first_number = float(input("What's the first number?: "))
    while another_calculation:
        for symbol in operations:
            print(symbol)
        operator = input("Pick an operation: ")
        second_number = float(input("What's the next number?: "))
        # get the function from the dictionary of functions
        calc_function = operations[operator]
        result = calc_function(first_number, second_number)
        print(f"{first_number} {operator} {second_number} = {result}")
        proceed = input(
            f"Type 'y' to continue calculating with {result} or type 'n' to start a new calculation: ")
        if proceed == 'y':
            first_number = result
        if proceed == 'n':
            another_calculation = False
            main()


if __name__ == "__main__":
    main()
