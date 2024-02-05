class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self):
        self.box = int(input(f"Hello, {self.owner}! Enter money to deposit: "))
        self.balance += self.box
        print(f"Your balance now: {self.balance}")
    
    def withdraw(self):
        self.box = int(input(f"Hello, {self.owner}! Enter money to withdraw: "))
        if self.box > self.balance:
            print(f"You can\'t withdraw more than you have!\nYour balance now {self.balance}")
        else:
            self.balance -= self.box
            print(f"Your balance now: {self.balance}")

person1 = Account("Aslan", 10000)
person1.deposit()
person1.withdraw()