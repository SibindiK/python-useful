#debugging tips
#1. Describe the problem
#2. Reproduce the bug
# def my_function():
#     for i in range(1, 21):
#         if i == 20:
#             print("You got it")
#
# my_function()

# from random import randint
# dice_imgs = ['1','2','3','4','5','6']
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])

# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#     print("Millenial")
# elif year >= 1994:
#     print("Gen Z")

pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(f"pages = {pages}")
print(f"word_per_page = {word_per_page}")
print(total_words)