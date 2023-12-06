# This entrypoint file to be used in development. Start by reading README.md
import budget
from budget import create_spend_chart
#from unittest import main

food = budget.Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")

clothing = budget.Category("Clothing")
print('This is ',clothing.name, ' ledger \n', clothing.ledger)
food.transfer(50, clothing)
print(food.get_balance())
print('This is ',clothing.name, ' ledger \n', clothing.ledger)
clothing.withdraw(25.55)
clothing.withdraw(100)
print(clothing.get_balance())


auto = budget.Category("Auto")
auto.deposit(2000, "initial deposit")
auto.withdraw(15)
print('===========')
print('This is ',food.name, ' ledger \n', food.ledger)
print('===========')
print(clothing.ledger)
print('===========')
print(auto.ledger)

#print(create_spend_chart([food, clothing, auto]))

# Run unit tests automatically
#main(module='test_module', exit=False)