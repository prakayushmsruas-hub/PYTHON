class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def deposit(self):
        amount = float(input("Enter amount to deposit: "))
        self.__balance += amount
        print("Successfully deposited:", amount)

    def withdraw(self):
        amount = float(input("Enter amount to withdraw: "))

        if amount <= self.__balance:
            self.__balance -= amount
            print("Successfully withdrawn:", amount)
        else:
            print("Insufficient Balance!")

    def get_balance(self):
        return self.__balance


account = BankAccount("Prakayush", 5000)

account.deposit()
account.withdraw()

print("Current Balance:", account.get_balance())