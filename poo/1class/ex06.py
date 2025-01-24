class Product():
    def __init__(self,name,price,amount):
        self.name = name
        self.price = price
        self.amount = amount

    def calculateStock(self):
        product = bool(input('Tem produto no seu stock? SIM [True], NAO [False]: '))
        if product == True:
            amount = int(input("Quantos produtos tem no seu estoque?:"))
            price = float(input("Qual valor do seus produtos?: "))
            self.price = amount * price
            return f'{self.price}'
        else:
            return f'estoque vazio'
        