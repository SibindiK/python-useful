#calculate the love  compatibility between 2 people based on their names and how many times
#letters from the words "true love" occur in each name
#Requirements @ www.buzzfeed.com/ariannarebolini/what-are-the-chances-your-crush-is-actually-your-true-love

#count the occurence of a char in a given word
def count_char(name, char):
    count = name.lower().count(char)
    return count

#total the count of each letter in the name
def count_sum(name, chars):
    sum = 0
    for char in chars:
        sum += count_char(name,char)
    return sum

#print the result and extra message
def print_message(score, message):
    print(f"Your score is {score}, {message}")
def main():
    true_sum = 0
    love_sum = 0
    chars1 = ('t','r','u','e')
    chars2 = ('l','o','v','e')

    print("Welcome to the Love Calculator")
    name1 = input("What is your name?\n")
    name2 = input("What is your partner's name?\n")
    true_sum = count_sum(name1 + name2,chars1)
    love_sum = count_sum(name1 + name2,chars2)
    result = str(true_sum) + str(love_sum)
    result = int(result)
    message = " "
    if result < 10 or result > 90:
        message = "you go together like coke and menthos"
    elif  result >= 40 and result <= 50:
        message = "you are alright together"
    print_message(result, message)

if __name__ == "__main__":
    main()