"""Exercicio 5"""
operacao = input('Escreva a operação desejada: (+, -, / ou *)')
numb1 = float(input('Digite o primeiro numero:'))
numb2 = float(input('Digite o segundo numero'))
if operacao == '+':
    soma = numb1 + numb2
    print(soma)
elif operacao == '-':
    subtraido = numb1 - numb2
    print(subtraido)
elif operacao == '/':
    divisao = numb1 / numb2
    print(f'{divisao:.2f}')
else:
    multi = numb1 * numb2
    print(multi)