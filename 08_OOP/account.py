class BankAccount:
    def __init__(self, account_holder: str, balance: float = 0.0):
        self.account_holder = account_holder
        self.balance = float(balance)

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            print("Сумма депозита должна быть положительной.")
            return
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            print("Сумма снятия должна быть положительной.")
            return
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Недостаточно средств.")

    def get_balance(self) -> float:
        return self.balance

account = BankAccount("Татьяна", 0)
account.withdraw(1000)
account.withdraw(1000)
account.withdraw(1000)
account.withdraw(1000)
account.withdraw(1000)
account.withdraw(1000)
account.withdraw(1000)
print(account.get_balance()) 
account.deposit(100)
print(account.get_balance()) 
