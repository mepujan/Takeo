from abc import ABC, abstractmethod


class BankTransaction(ABC):
    def __init__(self, balance) -> None:
        self.balance = balance
        super().__init__()

    @abstractmethod
    def deposite_amount(self):
        pass

    @abstractmethod
    def withdraw_amount(self):
        pass


class SavingAccount(BankTransaction):
    def __init__(self, balance) -> None:
        super().__init__(balance)

    def deposite_amount(self, amount):
        self.balance += amount
        print("Successfully deposited $", amount, ' in Saving Account')
        print("New Balance is : $", self.balance)

    def withdraw_amount(self, amount):
        if self.balance < amount:
            print("Insufficient Balance. Try Again...")
        else:
            self.balance -= amount
            print("Successfully withdrawn $", amount, ' in Saving Account')
            print("New Balance is : $", self.balance)


class CheckingAccount(BankTransaction):
    def deposite_amount(self, amount):
        self.balance += amount
        print("Successfully deposited $", amount, ' in Checking Accoount')
        print("New Balance is : $", self.balance)

    def withdraw_amount(self, amount):
        if self.balance < amount:
            print("Insufficient Balance. Try Again...")
        else:
            self.balance -= amount
            print("Successfully withdrawn $", amount, ' in Checking Accoount')
            print("New Balance is : $", self.balance)


saving_account = SavingAccount(5000)
checking_account = CheckingAccount(7000)

saving_account.deposite_amount(3000)
checking_account.deposite_amount(4000)
saving_account.withdraw_amount(2000)
checking_account.withdraw_amount(10000)
checking_account.withdraw_amount(20000)
