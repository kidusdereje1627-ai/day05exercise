class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{self.owner} withdrew {amount}")
        else:
            print("Insufficient balance")

    def statement(self):
        print(f"Account: {self.owner}")
        print(f"Balance: {self.balance}")
        print("-" * 25)


class SavingsAccount(Account):
    def __init__(self, owner, balance=0, interest_rate=0.05):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest


class CurrentAccount(Account):
    def __init__(self, owner, balance=0, overdraft=500):
        super().__init__(owner, balance)
        self.overdraft = overdraft

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft:
            self.balance -= amount
            print(f"{self.owner} withdrew {amount}")
        else:
            print("Overdraft limit exceeded")


# Create Accounts
acc1 = SavingsAccount("Kidus", 1000, 0.10)
acc2 = CurrentAccount("Abel", 500, 300)

# Savings Account
acc1.deposit(200)
acc1.add_interest()

# Current Account
acc2.withdraw(700)

# Polymorphism
accounts = [acc1, acc2]

for account in accounts:
    account.statement()