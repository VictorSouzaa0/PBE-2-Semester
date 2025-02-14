num = 0
numbers = []
while num >= 0:
    num = float(input('Insira o número: '))
    print(f'voce selecionou {num}')
    numbers.append(num)
    

print('Parabéns você descobriu o esquema :)' ,'e maior inserido foi:',max(numbers))