class Book():
    def __init__(self,title,autor,pages):
        self.title = title
        self.autor = autor
        self.pages = pages

    def lendbook(self):
        return f'O livro {self.title} de {self.autor} com {self.pages} foi emprestado '

book1 = Book(title='Thor', autor='Eu', pages=323)
print(book1.lendbook())

#Não entendi o enunciado sorry :( 