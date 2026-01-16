class Account:
    count = 0
    def __init__(self, name, accno, balance):
        self.name = name
        self.accno = accno
        self.balance = balance
        Account.count += 1
    def deposit(self, amt):
        self.balance += amt
        print("Deposited:", amt)
    def withdraw(self, amt):
        if amt <= self.balance:
            self.balance -= amt
            print("Withdrawn:", amt)
        else:
            print("Insufficient Balance!")
    def check_balance(self):
        print("Current Balance:", self.balance)
a1 = Account("Sujit", 1001, 5000)
a2 = Account("Riya", 1002, 8000)
a1.deposit(1000)
a1.withdraw(3000)
a1.check_balance()
a2.withdraw(9000)
a2.check_balance()
print("Total Accounts Created =", Account.count)
