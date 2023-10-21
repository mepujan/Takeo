class Bank:
    def __init__(self, balance=0.0, account_number='123455678') -> None:
        self.__balance = balance
        self.__account_number = account_number

    def deposite(self, amount):
        self.__balance += amount
        print("Successfuly deposited $", amount, ' into your account')
        print("New Balance is: $", self.get_balance())

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Balance Not Sufficient")
        else:
            self.__balance -= amount
            print("Successfuly withdrawn $", amount, ' from your account')
            print("New Balance is: $", self.get_balance())

    def get_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__account_number


bank = Bank(20000, '64733565')
bank.deposite(3000)
bank.withdraw(5000)
bank.withdraw(50000)
print(bank.get_balance())
print(bank.get_account_number())
