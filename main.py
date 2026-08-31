class Bank:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print("Amount deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Amount withdrawn:", amount)
        else:
            print("Insufficient balance")

    def show_balance(self):
        print("Current balance:", self.__balance)


acc = Bank(1000)

acc.show_balance()
acc.deposit(500)
acc.withdraw(300)
acc.show_balance()
