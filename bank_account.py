class BankAccount:
    all_accounts = []
    #don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance = 0): 
        self.int_rate = int_rate/100
        self.balance = balance
        BankAccount.all_accounts.append(self)
        #your code here! (remember, instance attributes go here)
        #don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if self.balance>0 and self.balance>=amount:
            self.balance -= amount
        else:
            print('Insufficent funds: Charging a $5 dollar fee')
            self.balance -=5
        return self
    def display_account_info(self):
        print(f'Balance:{self.balance}')
        return self
    def yield_interest(self):
        if self.balance>0:
            self.balance = self.balance + (self.balance * self.int_rate)
        return self

account1 = BankAccount(1.5,255)
account2 = BankAccount(1.2,300)
account1.deposit(300).deposit(100).deposit(25).withdraw(80).yield_interest().display_account_info()
account2.deposit(500).deposit(40).withdraw(50).withdraw(100).yield_interest().display_account_info()