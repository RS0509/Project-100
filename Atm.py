class Atm:
    def __init__(self,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin

    def CheckBalance(self):
        print("Your balance is 100000")

    def CashWithdrawl(self,amountWithdrawn):
        original_amount = 100000
        new_amount = original_amount - amountWithdrawn
        print("you have withdrawn amount "+str(amountWithdrawn))
        print("Your remaining balance is "+ str(new_amount))


def main():
    card_number = input("insert your card number--> ")
    pin_number  = input("enter your pin number--> ")

    User =  Atm(card_number ,pin_number)

    print("Choose your activity ")
    print("1. Balance Enquriy   2. Cash Withdrawl")
    activity = int(input("enter activity number--> "))

    if (activity == 1):
        User.CheckBalance()
    elif (activity == 2):
        amountWithdrawn = int(input("enter the amount--> "))
        User.CashWithdrawl(amountWithdrawn)
    else:
        print("enter a valid number")


if __name__ == "__main__":
    main()