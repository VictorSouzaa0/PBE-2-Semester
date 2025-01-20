print('PORTUGUÊS')
PortugueseNotes = float(input('Insira a nota: '))
print('MATEMÁTICA')
MathNotes = float(input('Insira a nota: '))
print('GEORGRAFIA')
GeoNotes = float(input('Insira a nota: '))
print('HISTÓRIA')
HistoryNotes = float(input('Insira a nota: '))
print('CIÊNCIAS')
ScienceNotes = float(input('Insira a nota: '))

operation = (PortugueseNotes + MathNotes + GeoNotes + HistoryNotes + ScienceNotes)/5

if operation <= 2.4:
    print(f'Sua média foi de {operation} REPROVADO')
elif operation >=2.5 and operation <= 4:
    print(f'Sua média foi de {operation} RECUPERAÇÃO')
else:
    print(f'Sua média foi de {operation} APROVADO')