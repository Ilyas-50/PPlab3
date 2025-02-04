class Bank():
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"New balance: ${self.balance}")
        else:
            print("only positive")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"New balance: ${self.balance}")
        else:
            print("invalid attempt")

user = Bank("ilyas", 100)
user.deposit(50)
user.withdraw(30)
user.withdraw(150)  #overdrawing
user.deposit(-20)   #error