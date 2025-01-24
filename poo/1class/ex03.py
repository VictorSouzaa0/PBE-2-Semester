class Rectangle():
    def __init__(self, width,height):
        self.width = width
        self.height = height

    def operationArea(self,):
        return f' A área do {self.width * self.height} e o perímetro {(self.width * self.height) + 2}'

rectan = Rectangle(width=10,height=10)
print(rectan.operationArea())
            