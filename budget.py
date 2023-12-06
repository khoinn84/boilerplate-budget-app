class Category:
  
    def __init__(self, n):
        self.name = n
        self.balance = 0.00
        self.ledger = []

    def deposit(self, amount, description=''):
        object1 = {"amount": amount, "description": description}
        self.ledger.append(object1)
        self.balance = self.balance + amount

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            object2 = {"amount": -amount, "description": description}
            self.ledger.append(object2)
            self.balance = self.balance - amount
            return True
        else:
          return False
      
    def get_balance(self):
        return self.balance
      
    def transfer(self, amount, ins):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + ins.name)
            ins.deposit(amount, "Transfer from " + self.name)
            return True
        else:
            return False

    def check_funds(self, amount):
        return not amount > self.balance

          

def create_spend_chart(categories):
    return True
