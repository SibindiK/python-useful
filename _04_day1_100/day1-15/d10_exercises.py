# format a given name to title case
def to_title_case(fname, lname):
    return (f"{fname.title()} {lname.title()}")

#check if a given year is a leap year or not
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

#get the number of days in a given month in a given year
def days_in_month(year, month):
    months30 = (4, 6, 9, 11)
    months31 = (1, 3, 5, 7, 8, 10, 12)
    days = 0
    if month in months30:
        days = 30
    elif month in months31:
        days = 31
    elif month == 2:     
        if is_leap_year(year):
            days = 29
        else:
            days = 28
    return days


def main():
    print(to_title_case("kermit", "sibindi"))

    year = int(input("Enter a year: "))
    month = int(input("Enter a month: "))
    days = days_in_month(year, month)
    print(days)


if __name__ == "__main__":
    main()
