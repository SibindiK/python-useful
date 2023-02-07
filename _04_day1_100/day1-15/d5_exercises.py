# loops
def for_loops():
    fruits = ["Apples", "Pears", "Bananas"]
    for fruit in fruits:
        print(fruit)

# convert a string list of numbers separated by a blank space to integers


def change_elements_to_int(list):
    list = list.split(" ")
    for n in range(0, len(list)):
        list[n] = int(list[n])
    return list

# calculating average heights without using sum and len functions


def calculate_average_heights(student_heights):
    total = 0
    count = 0
    for height in student_heights:
        total += height
        count += 1
    print(
        f"Average height to the nearest whole number = {round(total / count)}")

# get the highest score from a given list of scores


def get_highest_score(scores):
    h_score = 0
    for score in scores:
        if score > h_score:
            h_score = score
    return h_score

# add all even numbers from 1 - 100


def add_even_numbers():
    sum = 0
    for number in range(0, 101, 2):
        sum += number
    return sum


def main():
    for_loops()
    heights = input("Enter student heights separated by a space\n")
    heights = change_elements_to_int(heights)
    calculate_average_heights(heights)
    scores = input("Enter list of scores separated by a space\n")
    print(
        f"Highest score is {get_highest_score(change_elements_to_int(scores))}")
    print(f"Sum of all even numbers from 0-100 = {add_even_numbers()}")


if __name__ == "__main__":
    main()
