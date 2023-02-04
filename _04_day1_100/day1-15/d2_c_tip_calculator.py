#script calculates how much each person should pay on a given bill and tip
print("Welcome to the tip Calculator")
bill_total = float(input("What was the total bill?\n"))
people = int(input("How many people are sharing the bill?\n"))
tip_p = float(input("What percentage tip do you want to give? eg 5, 12.5\n"))
tip_amount = round((bill_total + (bill_total * (tip_p/100))) / people, 2)
print(f"You will each pay {tip_amount}")