class Ecommerece():
    def __init__(self,products):
        self.products = products
    prod = []
    copy = []
    def singupProd(self,):
        prod = []
        entryWhile = 'S'
        while entryWhile == 'S':
            self.products = input('Cadastre o produto desejado : ')
            prod.append(self.products)
            print (f'{self.products} adicionado com sucesso na lista deseja continuar? S/N?')
            entryWhile = input('Insira a opção: ')
        
        print (f'Produtos cadastrados: {prod}')

prod1 = Ecommerece(products=any)
print(prod1.singupProd())

#Irei terminar essa lista até o fim dessa semana