#program to define a class to simulate bank account then implement it

class BankAccount:
  def __init__(self):
    self.balance = 0
  
  def deposit(self, amount):
    self.balance += amount
    return self.balance
  
  def withdraw(self, amount):
    if self.balance - amount < 0:
      return "Insufficient Funds"
    self.balance -= amount
    return self.balance

myAccount = BankAccount()

myAccount.deposit(2000)
print("Balance =", myAccount.balance)
myAccount.withdraw(500)
print("Balance =", myAccount.balance)