class BankAcount():
    def __init__(self,number,name,balance):
        self.number = number
        self.name = name
        self.balance = balance

    def welcome(self):
        return f'Seja bem vindo {self.name}\n  O número da sua conta é de {self.number}'

    def deposit(self,money,balance):
        self.balance = balance + money
        return f'Deposito com valor de {money} reais, saldo atual{self.balance}'
    
    def withdraw(self,money,balance):
        self.balance = balance - money

        return f'Saque com valor de {money} reais, saldo atual {self.balance}'
    
firstAcc = BankAcount('1020','Victor',balance=None)
print(firstAcc.welcome())
print(firstAcc.withdraw(balance=5000,money=3))