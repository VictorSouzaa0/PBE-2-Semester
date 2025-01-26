class Triangle():
    def __init__(self,side1,side2,base):
        self.side1 = side1
        self.side2 = side2
        self.base = base
    
    def verify(self):

        if self.side1 + self.side2 == self.base:
            return f' A área do triangulho é de {(self.side1 * self.side2 /2)}'
        else:
            return f'Esse triangulo não é valido'
    
firstTri = Triangle(side1=5, side2= 6 ,base= 11 )
secondTri = Triangle(side1=5,side2=10, base=10)
print(firstTri.verify())
print(secondTri.verify())

