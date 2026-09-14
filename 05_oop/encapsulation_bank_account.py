
class BankAccount:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f'Deposited: {amount}')
        else:
            print('Deposit must be greater than 0')

    def withdraw(self, amount):
        if amount > self.__balance:
            print(f'Insufficient funds. Current balance: {self.__balance}')
        else:
            self.__balance -= amount
            print(f'Withdrew: {amount}')

    def get_balance(self):
        return self.__balance

    def show(self):
        print(f'Owner: {self.owner} | Balance: {self.__balance}')


if __name__ == "__main__":

    acc = BankAccount('Maria', 5000)
    acc.show()

    acc.deposit(1500)       
    acc.deposit(-200)      
    acc.withdraw(10000)   
    acc.show()

    print('Balance through getter:', acc.get_balance())
    print('Balance through name mangling:', acc._BankAccount__balance)

