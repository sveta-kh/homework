
class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0) -> None:
        self.owner = owner
        self.balance =  balance

    def deposit(self, amount: float):
        self.amount = amount
        if amount <=0:
            raise ValueError("Amount must be positive") 
        else:
            self.balance += amount
            return self.balance

    def withdraw(self, amount: float):
        if amount<=0:
            raise ValueError("Amount must be positive")
        if amount > self.balance:
            raise ValueError("Balance is not enough") 
        else:
            self.balance -= amount
            return self.balance



        
  
