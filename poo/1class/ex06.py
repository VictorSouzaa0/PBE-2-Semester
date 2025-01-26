

class Product():
    def __init__(self,name,price,amount):
        self.name = name
        self.price = price
        self.amount = amount

    def totalStock(self):
        if self.amount == 0:
            return f'não a produtos em seu stock'
        else:
            operation = self.amount * self.price
            return f'No seu stock há {self.amount} {self.name} e o valor do seu stock está em {operation}'

prod1 = Product(name='Pneu de carro', price=400,amount=50)
print(prod1.totalStock())