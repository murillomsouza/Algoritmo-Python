"""Exercicio 1"""
numb1 = float(input('Digite o primeiro numero:'))
numb2 = float(input('Digite o segundo numero:'))
if numb1 > numb2:
    print(f'O numero {numb1} é maior que {numb2}.')
elif numb1 < numb2:
    print(f'O numero {numb2} é maior que {numb1}.')
else:
    print('Os numeros são iguais')