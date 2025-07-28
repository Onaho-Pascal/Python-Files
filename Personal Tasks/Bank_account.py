# Create a bankacount that 1)stores n owner name and balance 2) has methods to deposit, withdraw, and get balance,
# 3) prevent withdrawals that exceed the current balance

class account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def withdrawal(self):
        withdraw = int(input(f"Hello {self.name}! \nHow much would you like to withdraw?: "))
        if withdraw > self.balance:
            return "Amount attempted to be withdrawn is greater than total balance"
        elif withdraw >= 0:
            self.balance -= withdraw
            return f"You have withdrawn {withdraw} naira. Your balance is {self.balance} naira."
        else:
            return f"Please choose a valid amount from 0 naira to {self.balance} naira."
        
    def deposition(self):
        deposit = int(input(f"Hello {self.name}! \n How much would you like to deposit into your account?: "))
        if deposit >=0:
            self.balance += deposit
            return f"You have deposited {deposit} naira. Your balance is {self.balance} naira."
        else:
            return "Please deposit a valid amount!"
        

money = account("John", 2500)

print(money.deposition())