# Day 15: Bank Account Simulation

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New Balance: {self.balance}")
        else:
            print("Deposit amount must be positive!")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        elif amount <= 0:
            print("Withdrawal amount must be positive!")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New Balance: {self.balance}")
    
    def get_balance(self):
        print(f"Current Balance: {self.balance}")
        return self.balance


# Example usage:
account = BankAccount("Shashank", 1000)

account.deposit(500)
account.withdraw(200)
account.withdraw(2000)  # Should show insufficient funds
account.get_balance()
