#add together the two digits of any given 2 digit number
number = input("Enter number: ")
result = int(number[0]) + int(number[1])
print(result)

#bmi calculator
weight = float(input("Weight in kg: "))
height = float(input("Height in metres: "))
bmi = weight/height**2
print(f"Your BMI is {int(bmi)}")

#calculate life in weeks from current age to 90
age = int(input("How old are you now? "))
months = (90-age) * 12
weeks = (90-age) * 52
days = (90-age) * 365
print(f"You have {months} months or {weeks} weeks or {days} days")