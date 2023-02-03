#script to demo basic class inheritance in python
#base class is Member and child classes are admin and user

import datetime as dt

class Member:
    EXPIRY_DAYS = 365 # number of days before membership expires
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.date_joined = dt.date.today()
        self.expiry_date = self.date_joined + dt.timedelta(days = Member.EXPIRY_DAYS)

    def toString(self):
        return(self.first_name +" " + self.last_name + " joined " +
         str(self.date_joined) + " expires " + str(self.expiry_date))

class Admin(Member):
    pass

class User(Member):
    pass

def main():
    a1 = Admin("David", "Striker")
    print(a1.toString())

if __name__ == "__main__":
    main()
