class Empoyee():
    def __init__(self,name,payment,position):
        self.name = name
        self.payment = payment
        self.position = position

    def salary_calculates(self):
        cash = float(input('Insira o Salário: '))
        self.payment = (cash * 0.15) 
        return f'O funcionário cadastrado no nome de {self.name} no cargo de {self.position} será pago de imposto de  15% no valor de =: {self.payment:.2f} reais'
    
firstEmpo = Empoyee(name='Victor',payment=None,position='Engenheiro')
print(firstEmpo.salary_calculates())
