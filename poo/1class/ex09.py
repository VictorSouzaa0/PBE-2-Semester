class Patient():
    def __init__(self,name,age,historical):
        self.name = name
        self.age = age
        self.historical = historical
    
    def addHist(self):
        addConsult = self.historical = self.historical + 1
        return f'Olá {self.name} sua  consulta foi adicionada, total de consultas  {addConsult}'

patient1 = Patient(name='Claudio',age=58,historical=4)
patient2 = Patient(name='Victor', age=19,historical=1)
print(patient1.addHist())
print(patient2.addHist())