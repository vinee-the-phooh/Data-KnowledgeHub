# Encapsulation in Python
# Encapsulation is a fundamental concept in object-oriented programming that restricts direct access to an object's attributes and methods.
# - Use '__' to make variables private.
# - Use getter/setter methods to access private data.

class Account:
    def __init__(self, balance):
        self.__balance = balance  # Private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account = Account(100)
account.deposit(50)
print(account.get_balance())


