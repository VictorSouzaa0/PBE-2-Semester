''' 
Crie uma classe chamada “Círculo” que possua um atributo para armazenar o raio e 
métodos para calcular a área e o perímetro do círculo.
'''
#Criando classe pai
class Circle():
    def __init__(self,radio,):
        self.radio = radio
#inserindo o método calcular área do perímetro
    def countArea(self,count):
        count = (self.radio**2) * 3.14

        return count
#Criando objeto 
circle1 = Circle(1)
print(f'A área total do seu triângulo é equivalente há {circle1.countArea(1)} e seu perímetro é de {circle1.countArea(8)*6.28:.2f}')