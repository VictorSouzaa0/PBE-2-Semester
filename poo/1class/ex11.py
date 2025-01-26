class Bank():
    def __init__(self,name,number,balance):
        self.name = name
        self.number = number
        self.balance = balance

    def createACC(self):
        agency = (input('Qual instuição você irá criar sua conta bancária?\n'
                       'Banco do Brasil \n'
                       'Banco Santander \n'
                       'Banco Bradesco \n'
                       'Banco Itaú \n'
                       'Insira o um desses bancos aqui:'))
        if agency == 'Banco do Brasil' and 'banco do brasil' :
            agency = 'Banco do Brasil'
            cod = 1
            self.number = cod
            self.name = agency
            return f'Banco selecionado: {self.name} e seu código de agência é {self.number}'
        elif agency == 'Banco Santander' and 'banco santander':
            agency == 'Banco Santander'
            cod = 33
            self.number = cod
            self.name = agency
            return f'Banco selecionado: {self.name} e seu código de agência é {self.number}'
        elif agency == 'Banco Bradesco' and 'banco bradesco':
            agency == 'Bradesco'
            cod = 237
            self.number = cod
            self.name = agency   
            return f'Banco selecionado: {self.name} e seu código de agência é {self.number}'   
        elif agency == 'Banco Itaú' and 'banco itau':
            agency == 'Banco Itaú'
            cod = 341
            self.number = cod
            self.name = agency
            return f'Banco selecionado: {self.name} e seu código de agência é {self.number}'


    def deposit(self):
        deposit = float(input('Quantos você deseja depositar?: '))
        self.balance = deposit

        return f'Deposito efetuado com sucesso na conta {self.name}, saldo atual : R${self.balance}'
    
    def withdraw(self):
        if self.balance <= 0:
            print('Não há saldo suficiente para saque')
        else:
            withdraw = float(input('Quantos deseja sacar?\n'
                               f'saldo atual R${self.balance}'))
            return f'Saque efetuado com sucesso!, saldo atual R${self.balance - withdraw}'
        
cont1 = Bank(name=None,number=None,balance=None)
cont2 = Bank(name=None,number=None,balance=2)
print(cont1.createACC())
print(cont1.deposit())
