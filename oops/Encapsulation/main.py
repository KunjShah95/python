"""
Encapsulation
Encapsulation means hiding internal data and restricting direct access.

In Python, we use private attributes with a leading underscore _ or double underscore __ to indicate "private" variables.

Access through getter and setter methods or properties.
    
    """
    
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance   # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance

account = BankAccount("Alice", 1000)
print(account.owner)          # Alice
print(account.get_balance())  # 1000
account.withdraw(500)
print(account.get_balance())  # 500
# print(account.__balance)    # Error: AttributeError
