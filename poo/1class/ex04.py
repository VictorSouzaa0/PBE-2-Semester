class Student():
    def __init__(self,name,registration,grades):
        self.name = name
        self.registration = registration
        self.grades = grades
        
    def gradeStudents(self,):
        grade1 = float(input('Insira primeira nota: '))
        grade2 = float(input('Insira primeira nota: '))
        grade3 = float(input('Insira primeira nota: '))
        grade4 = float(input('Insira primeira nota:'))
        self.grades = (grade1 + grade2 + grade3 + grade4)/4
         
        if self.grades <5:
            return f' A nota do aluno {self.name}  foi de {self.grades:.2f} Reprovado'
        else:
            return f' A nota do aluno {self.name}  foi de {self.grades:.2f} Aprovado'

Student1 = Student('Victor',123,grades=None)
print(Student1.gradeStudents())